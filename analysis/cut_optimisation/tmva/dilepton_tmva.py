#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
from array import array
import argparse
import sys
import os
from tempfile import mkdtemp
import shutil

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops"))
from lib import utils
from lib import analysis_observables

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Run TMVA.')
parser.add_argument('-i', '--input', nargs='*', help='Signal Files', required=True)
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=True)
parser.add_argument('-bg', '--bg', nargs=1, help='Input Background Directory', required=False)
parser.add_argument('-nn', '--no_norm', dest='no_norm', help='No renormalization of weights', action='store_true')
parser.add_argument('-all', '--all', dest='all', help='All methods', action='store_true')

parser.add_argument('-lepNum', '--lepNum', nargs=1, help='lepNum', required=True)
parser.add_argument('-lep', '--lep', nargs=1, help='lep', required=True)
parser.add_argument('-iso', '--iso', nargs=1, help='iso', required=True)
parser.add_argument('-ptRange', '--ptRange', nargs='?', help='ptRange', const="", required=False)
parser.add_argument('-cat', '--cat', nargs='?', help='cat', const="", required=False)
args = parser.parse_args()

input_files = args.input

output_file_name = None
if args.output_file:
    output_file_name = args.output_file[0]
else:
    output_file_name = "tmva_output.root"
bg_dir = None
if args.bg:
    bg_dir = args.bg[0]

no_norm = args.no_norm
all = args.all

print "No norm=" + str(no_norm)
print "All=" + str(all)

#tmp_dir = "/afs/desy.de/user/n/nissanuv/nfs/tmp/"

lepNum = args.lepNum[0]
lep = args.lep[0]
iso = args.iso[0]
if args.ptRange:
    ptRange = args.ptRange
else:
    ptRange = ""
if args.cat:
    cat = args.cat
else:
    cat = ""

print "lepNum", lepNum, "lep", lep, "iso", iso, "ptRange", ptRange, "cat", cat

######## END OF CMDLINE ARGUMENTS ########

dir = os.path.dirname(output_file_name)
print "Changing directory to", dir
os.chdir(dir)

gROOT.SetBatch(1)
TMVA.Tools.Instance()
outputFile = TFile(output_file_name,'RECREATE')
factory = TMVA.Factory("TMVAClassification", outputFile,
                            ":".join([
                                "!V",
                                "!Silent",
                                "Color",
                                "DrawProgressBar",
                                "Transformations=I;D;P;G,D",
                                "AnalysisType=Classification"]
                                     ))

dataloaders = {}
preselections = {}


bTrees = []
sTrees = []

newFiles = []
newTrees = []

foundCategory = {}

totalEvents = 0
weights = 0

bg_files = glob(bg_dir + "/*")
print bg_files

prefix = ""
if lepNum == "exTrack":
    prefix = "exTrack_"


variablesUsed = []

variablesUsed.append("BTagsDeepMedium") 
variablesUsed.append("MinDeltaPhiMhtJets")
variablesUsed.append("Weight")

variablesUsed.append(prefix + 'deltaPhi' + iso + str(ptRange) + cat)
variablesUsed.append(prefix + 'deltaEta' + iso + str(ptRange) + cat)
variablesUsed.append(prefix + 'deltaR' + iso + str(ptRange) + cat)
variablesUsed.append(prefix + 'dilepHt' + iso + str(ptRange) + cat)
variablesUsed.append(prefix + 'invMass' + iso + str(ptRange) + cat)

for obs in analysis_observables.dileptonBDTeventObservables:
    if "LeadingJet." in obs:
        variablesUsed.append("LeadingJet")
    else:
        variablesUsed.append(obs)

preselection = None

preselection = "twoLeptons" + iso + str(ptRange) + cat + " == 1 && MinDeltaPhiMhtJets > 0.4 && leptonFlavour" + iso + str(ptRange) + cat  + " == \"" + lep + "\"" + " && sameSign" + iso + str(ptRange) + cat + " == 0"


variablesUsed.append("twoLeptons" + iso + str(ptRange) + cat)
variablesUsed.append("leptonFlavour" + iso + str(ptRange) + cat)
variablesUsed.append("sameSign" + iso + str(ptRange) + cat)
variablesUsed.append("isoCr" + iso + str(ptRange) + cat)

variablesUsed.append('dileptonPt' + iso + str(ptRange) + cat)
variablesUsed.append('mth1' + iso + str(ptRange) + cat) 

variablesUsed.append('leptons' + iso + str(ptRange) + cat)

variablesUsed.append('deltaPhiMhtLepton1' + iso + str(ptRange) + cat)
variablesUsed.append('deltaPhiMhtLepton2' + iso + str(ptRange) + cat)

#variablesUsed.append("BTagsDeepMedium")

print "Variables used", variablesUsed 

tmpDir = mkdtemp(prefix="nissanuv", dir="/tmp") + '/'
print "tmpDir=",tmpDir

for input_file in input_files:
    print "Opening File " + input_file
    fsignal = TFile(input_file)
    sTree = fsignal.Get("tEvent")
    if sTree.GetEntries() == 0:
        print "Emtpy. Skipping"
        continue

    if dataloaders.get(lepNum + lep + iso + str(ptRange) + cat) is None:
        dataloaders[lepNum + lep + iso + str(ptRange) + cat] = TMVA.DataLoader("dataset")
    print "Getting", iso + str(ptRange) + cat

    baseFileName = os.path.basename(input_file)
    newfile = TFile(tmpDir + baseFileName, "recreate");
    
    print "old tree has", sTree.GetEntries()
    sTree.SetBranchStatus("*",0);
    for branch in variablesUsed:
        print "Setting branch on", branch
        sTree.SetBranchStatus(branch,1);
    #newSTree = sTree.CloneTree(0)
    print "Coping tree with preselection", preselection
    newSTree = sTree.CopyTree(preselection)
    print "new tree has", newSTree.GetEntries()
    
    if newSTree.GetEntries() == 0:
        newfile.Close()
        sTree.Delete()
        fsignal.Close() 
        continue
    
    newfile.cd()
    newSTree.Write("tEvent");
    newfile.Close();
    
    print "Done copying."
    sTree.Delete()
    fsignal.Close() 
    
    newfile = TFile(tmpDir + baseFileName, "read");
    newFiles.append(newfile)
    sTree = newfile.Get("tEvent")
    newTrees.append(sTree)
    dataloaders[lepNum + lep + iso + str(ptRange) + cat].AddSignalTree(sTree, 1) 

for bg_file in bg_files:
    if "QCD" in bg_file:
        print "Skipping QCD", bg_file
        continue
    if len(bg_file) == 0 or bg_file.isspace():
        continue
    print "Processing", bg_file
    
    fbackground = TFile(bg_file)
    bTree = fbackground.Get("tEvent")
    
    baseFileName = os.path.basename(bg_file)
    newfile = TFile(tmpDir + baseFileName, "recreate");
    
    bTree.SetBranchStatus("*",0);
    for branch in variablesUsed:
        bTree.SetBranchStatus(branch,1);
    newBTree = bTree.CopyTree(preselection)
    print "new tree has", newBTree.GetEntries()
    if newBTree.GetEntries() == 0:
        newfile.Close()
        bTree.Delete()
        fbackground.Close() 
        continue
    
    newfile.cd()
    newBTree.Write("tEvent");
    newfile.Close();
    print "Done copying."
    bTree.Delete()
    fbackground.Close()
    
    newfile = TFile(tmpDir + baseFileName, "read")
    newFiles.append(newfile)
    bTree = newfile.Get("tEvent")
    bTrees.append(bTree)
    dataloaders[lepNum + lep + iso + str(ptRange) + cat].AddBackgroundTree(bTree, 1)
    

dataloader = dataloaders[lepNum + lep + iso + str(ptRange) + cat]

dataloader.AddVariable(prefix + 'deltaPhi' + iso + str(ptRange) + cat, 'F')
dataloader.AddVariable(prefix + 'deltaEta' + iso + str(ptRange) + cat, 'F')
dataloader.AddVariable(prefix + 'deltaR' + iso + str(ptRange) + cat, 'F')

dataloader.AddVariable(prefix + 'dilepHt' + iso + str(ptRange) + cat, 'F')
dataloader.AddVariable(prefix + 'invMass' + iso + str(ptRange) + cat, 'F')

for obs in analysis_observables.dileptonBDTeventObservables:
    dataloader.AddVariable(obs, analysis_observables.dileptonBDTeventObservables[obs])
    
preselectionCut = None
    
preselectionCut = TCut(preselection)
preselections[lepNum + lep + iso + str(ptRange) + cat] = preselectionCut
dataloader.AddCut(preselection)
dataloader.AddVariable('dileptonPt' + iso + str(ptRange) + cat, 'F')
dataloader.AddVariable('mth1' + iso + str(ptRange) + cat, 'F')
dataloader.AddVariable('leptons' + iso + str(ptRange) + cat + '[0].Pt()', 'F')
dataloader.AddVariable('leptons' + iso + str(ptRange) + cat + '[0].Eta()', 'F')
dataloader.AddVariable('leptons' + iso + str(ptRange) + cat + '[0].Phi()', 'F')
dataloader.AddVariable('deltaPhiMhtLepton1' + iso + str(ptRange) + cat, 'F')
dataloader.AddVariable('deltaPhiMhtLepton2' + iso + str(ptRange) + cat, 'F')
dataloader.AddVariable('BTagsDeepMedium', 'I')

# Spectators
dataloader.AddSpectator('Weight','F')
if no_norm:
   dataloader.PrepareTrainingAndTestTree(preselectionCut, "SplitMode=random:!V:NormMode=None")
else:
   dataloader.PrepareTrainingAndTestTree(preselectionCut, "SplitMode=random:!V")
factory.BookMethod(dataloader, TMVA.Types.kBDT, lepNum + lep + iso + str(ptRange) + cat, "NTrees=120:MaxDepth=3")

factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()
outputFile.Close()

print "deleting tmp dir", tmpDir
shutil.rmtree(tmpDir)
exit(0)


