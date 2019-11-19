#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
from array import array
import argparse
import sys
import os

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Run TMVA.')
parser.add_argument('-i', '--input', nargs='*', help='Signal Files', required=True)
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=True)
parser.add_argument('-bg', '--bg', nargs='*', help='Input Background Files', required=True)
parser.add_argument('-nn', '--no_norm', dest='no_norm', help='No renormalization of weights', action='store_true')
parser.add_argument('-all', '--all', dest='all', help='All methods', action='store_true')
args = parser.parse_args()

input_files = args.input
bg_files = args.bg

output_file_name = None
if args.output_file:
    output_file_name = args.output_file[0]
else:
    output_file_name = "tmva_output.root"

no_norm = args.no_norm
all = args.all

print "No norm=" + str(no_norm)
print "All=" + str(all)

	
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
                                     
dataloader = TMVA.DataLoader("dataset")

bgFiles = []
bTrees = []
sFiles = []
sTrees = []

for input_file in input_files:
    print "Opening File " + input_file
    fsignal = TFile(input_file, "update")
    sTree = fsignal.Get("tEvent")
    print sTree
    if sTree.GetEntries() == 0:
        print "Emtpy. Skipping"
        continue
    sFiles.append(fsignal)
    sTrees.append(sTree)
    dataloader.AddSignalTree(sTree, 1);
for bg_file in bg_files:
    fbackground = TFile(bg_file, "update")
    bTree = fbackground.Get("tEvent")
    if bTree.GetEntries() == 0:
        print "Emtpy. Skipping"
        continue
    bgFiles.append(fbackground)
    bTrees.append(bTree)
    dataloader.AddBackgroundTree(bTree, 1)

# Variables
dataloader.AddVariable('track.Eta()', 'F')
dataloader.AddVariable('track.Pt()', 'F')
dataloader.AddVariable('track.Phi()', 'F')
dataloader.AddVariable('dxyVtx', 'F')
dataloader.AddVariable('dzVtx', 'F')
dataloader.AddVariable('deltaEtaLJ', 'F')
dataloader.AddVariable('deltaRLJ', 'F')


## FULL
dataloader.AddVariable('deltaEtaLL', 'F')
dataloader.AddVariable('deltaRLL', 'F')
dataloader.AddVariable('trkMiniRelIso', 'F')
dataloader.AddVariable('trkRelIso', 'F')
dataloader.AddVariable('mtt', 'F')
#dataloader.AddVariable('deltaRMet', 'F')
dataloader.AddVariable('deltaPhiMet', 'F')
dataloader.AddVariable('lepton.Eta()', 'F')
dataloader.AddVariable('lepton.Phi()', 'F')
dataloader.AddVariable('lepton.Pt()', 'F')
dataloader.AddVariable('invMass', 'F')


#dataloader.AddVariable('chi2perNdof', 'F')


# cuts defining the signal and background sample
preselectionCut = TCut("")
if no_norm:
    dataloader.PrepareTrainingAndTestTree(preselectionCut, "SplitMode=random:!V:NormMode=None")
else:
    dataloader.PrepareTrainingAndTestTree(preselectionCut, "SplitMode=random:!V")
factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDT", "NTrees=200:MaxDepth=3")
#factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDT2","NTrees=2000:nEventsMin=2000:MaxDepth=4:BoostType=AdaBoost:AdaBoostBeta=0.6:UseRandomisedTrees=True:UseNVars=6:nCuts=2000:PruneMethod=CostComplexity:PruneStrength=-1")
if all:
    factory.BookMethod(dataloader, TMVA.Types.kMLP, "MLP", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:!UseRegulator" )
#factory.BookMethod(dataloader, TMVA.Types.kMLP, "MLP_ANN", "" );
factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()
outputFile.Close()






