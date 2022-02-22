#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import os
import re
from datetime import datetime
import math

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes"))
import utils
import analysis_ntuples

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Slim skims for jet iso scan..')
parser.add_argument('-s', '--signal', dest='signal', help='Signal', action='store_true')
parser.add_argument('-bg', '--background', dest='bg', help='Background', action='store_true')
parser.add_argument('-data', '--data', dest='data', help='Background', action='store_true')
args = parser.parse_args()

signal = args.signal
bg = args.bg
data = args.data

if not signal and not bg and not data:
    bg = True

signal_dir = None
bg_dir = None

if signal:
    input_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum"
    output_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/slim"
elif bg:
    input_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
    output_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/slim"
else:
    input_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim/sum"
    output_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim/slim"

print "input_dir", input_dir
print "output_dir", output_dir

######## END OF CMDLINE ARGUMENTS ########

variablesUsed = []

variablesUsed.append("BTagsDeepMedium")
variablesUsed.append("MinDeltaPhiMetJets")
variablesUsed.append("MinDeltaPhiMhtJets")
variablesUsed.append("passedMhtMet6pack")
variablesUsed.append("tEffhMetMhtRealXMht2016")
variablesUsed.append("Weight")
variablesUsed.append("BranchingRatio")
variablesUsed.append("MET")
variablesUsed.append("MHT")
variablesUsed.append("vetoElectronsPassIso")
variablesUsed.append("vetoMuonsPassIso")
variablesUsed.append("NJets")
variablesUsed.append("LeadingJetPt")
variablesUsed.append("LeadingJet")
variablesUsed.append("HT")
variablesUsed.append("Weight")
variablesUsed.append("passedMhtMet6pack")
variablesUsed.append("tEffhMetMhtRealXMht2016")
variablesUsed.append("CrossSection")
variablesUsed.append("puWeight")


# basic_histograms_defs = [
#         { "obs" : "invMass%%%", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
#         { "obs" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
#         { "obs" : "dilepBDT%%%_fine", "formula" : "dilepBDT%%%","minX" : -1, "maxX" : 1, "bins" : 15, "blind" : [None,0.1]},
#         { "obs" : "dilepBDT%%%_custom", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1], "customBins"  : [-1,-0.6,-0.3,0,0.10,0.26,0.34,0.38,0.42,1] },
#         { "obs" : "deltaR%%%", "minX" : 0, "maxX" : 3.5, "bins" : 8},
#         { "obs" : "dilepHt%%%", "minX" : 200, "maxX" : 800, "bins" : 8},
#         { "obs" : "dileptonPt%%%", "minX" : 0, "maxX" : 30, "bins" : 8},
#         { "obs" : "MHT", "minX" : 220, "maxX" : 800, "bins" : 8},
#         { "obs" : "MET", "minX" : 200, "maxX" : 800, "bins" : 8},
#         { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 3.5, "bins" : 8},
#         { "obs" : "leptons%%%[0].Pt()", "minX" : 0, "maxX" : 20, "bins" : 8},
#         { "obs" : "deltaPhiMetLepton1%%%", "minX" : 0, "maxX" : 3.5, "bins" : 8},
#         { "obs" : "mt1%%%", "minX" : 0, "maxX" : 200, "bins" : 8},
#         { "obs" : "leptons%%%[0].Eta()", "minX" : -2.4, "maxX" : 2.4, "bins" : 8},
#         { "obs" : "NJets", "minX" : 0, "maxX" : 6, "bins" : 6},
#         { "obs" : "deltaPhiMetLepton2%%%", "minX" : 0, "maxX" : 3.5, "bins" : 8},
#         { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 500, "bins" : 8},
#         { "obs" : "LeadingJet.Eta()", "minX" : -2.4, "maxX" : 2.4, "bins" : 8},
#         { "obs" : "deltaEta%%%", "minX" : 0, "maxX" : 5, "bins" : 8},
#         { "obs" : "HT", "minX" : 0, "maxX" : 500, "bins" : 8},
#         { "obs" : "leptons%%%[0].Phi()", "minX" : 0, "maxX" : 3.5, "bins" : 8},
#      ]
#     
# notautau_cuts = [
#         {"name":"none", "title": "None", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 200 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
#         {"name":"bdt", "title": "BDT > 0.35", "condition" : "(dilepBDT%%% > 0.35 &&  MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 200 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
#     ]

preselection = "MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && "
twoLeptonsConds = []

for iso in utils.leptonIsolationList:
    for cat in utils.leptonIsolationCategories:
        ptRanges = [""]
        drCuts = [""]
        if iso == "CorrJetIso":
            ptRanges = utils.leptonCorrJetIsoPtRange
            drCuts = utils.leptonCorrJetIsoDrCuts
        for ptRange in ptRanges:
            for drCut in drCuts:
                cuts = ""
                if len(str(ptRange)) > 0:
                    cuts = str(ptRange) + "Dr" + str(drCut)
                jetiso = iso + cuts + cat
                variablesUsed.append("leptons" + jetiso)
                variablesUsed.append("deltaR" + jetiso)
                variablesUsed.append("dilepHt" + jetiso)
                variablesUsed.append("dileptonPt" + jetiso)
                variablesUsed.append("deltaPhiMetLepton1" + jetiso)
                variablesUsed.append("deltaPhiMetLepton2" + jetiso)
                variablesUsed.append("mt1" + jetiso)
                variablesUsed.append("deltaEta" + jetiso)
                variablesUsed.append("twoLeptons" + jetiso)
                variablesUsed.append("dilepBDT" + jetiso)
                variablesUsed.append("leptonFlavour" + jetiso)
                variablesUsed.append("sameSign" + jetiso)
                variablesUsed.append("isoCr" + jetiso)
                variablesUsed.append("invMass" + jetiso)
                
                
                variablesUsed.append("tc" + jetiso)
                variablesUsed.append("tautau" + jetiso)
                variablesUsed.append("other" + jetiso)
                variablesUsed.append("omega" + jetiso)
                variablesUsed.append("rho_0" + jetiso)
                variablesUsed.append("eta" + jetiso)
                variablesUsed.append("eta_prime" + jetiso)
                variablesUsed.append("j_psi" + jetiso)
                variablesUsed.append("upsilon_1" + jetiso)
                variablesUsed.append("upsilon_2" + jetiso)
                variablesUsed.append("phi" + jetiso)
                variablesUsed.append("n_body" + jetiso)
                variablesUsed.append("sc" + jetiso)
                variablesUsed.append("rf" + jetiso)
                variablesUsed.append("ff" + jetiso)
                                
                twoLeptonsConds.append("twoLeptons" + jetiso + " == 1")
                

preselection += "(" + " || ".join(twoLeptonsConds) + ")"

print "Preselection:"
print preselection

def main():
    print "Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    
    files = glob(input_dir + "/*")
    
    for filename in files:
        print "Opening", filename
        baseFileName = os.path.basename(filename)
        output_file = output_dir + "/" + baseFileName
        print "output_file", output_file
        
        if os.path.isfile(output_file):
            print "File exits. Skipping", output_file
            continue

        f = TFile(filename)
        c = f.Get('tEvent')
        if c.GetEntries() == 0:
            print "Emtpy. Skipping"
            f.Close()
            continue

        print "old tree has", c.GetEntries()
        c.SetBranchStatus("*",0);
        for branch in variablesUsed:
            #print "Setting branch on", branch
            c.SetBranchStatus(branch,1)
        newfile = TFile(output_file,'recreate')
        newTree = c.CopyTree(preselection)
        print "new tree has", newTree.GetEntries()
        
        if newTree.GetEntries() == 0:
            print "Resulting tree is empty. Skipping."
            f.Close()
            newTree.Delete()
            newfile.Close()
            os.remove(output_file)
            continue
        
        
        
        newfile.cd()
        newTree.Write("tEvent");
        newfile.Close();
    
        print "Done copying."

        c.Delete()
        f.Close() 
    
    print "End: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
main()
exit(0)