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

gSystem.Load('LumiSectMap_C')
from ROOT import LumiSectMap

#lumi = 5746.370
#weight = lumi / utils.LUMINOSITY

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Plot skims for x1x2x1 process with BDTs.')
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
#parser.add_argument('-s', '--single', dest='single', help='Single', action='store_true')
#parser.add_argument('-c', '--cut', nargs=1, help='Cut', required=False)
#parser.add_argument('-obs', '--obs', nargs=1, help='Obs', required=False)
args = parser.parse_args()

output_file = None

signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_sam/sum"
bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"

if args.output_file:
    output_file = args.output_file[0]
else:
    output_file = "histograms.root"

######## END OF CMDLINE ARGUMENTS ########

# if lepNum == "reco":
#     preselection = "twoLeptons" + iso + str(ptRange) + cat + " == 1 && BTagsDeepMedium == 0 && @leptons" + iso + str(ptRange) + cat + ".size() == 2 && leptonFlavour" + iso + str(ptRange) + cat  + " == \"" + lep + "\"" + " && sameSign" + iso + str(ptRange) + cat + " == 0"
# else:
#     preselection = "exclusiveTrack" + iso + str(ptRange) + cat + ' == 1 && BTagsDeepMedium == 0 && exclusiveTrackLeptonFlavour' + iso + str(ptRange) + cat  + " == \"" + lep + "\""
#  
# prefixVars = ""
# if prefix == "exTrack":
#     prefixVars = "exTrack_"
# eventPassed = False
# leptonFlavour = ""
# if prefix == "reco":
#     if eval("tree.twoLeptons"  + postfix) == 1 and tree.BTagsDeepMedium == 0 and eval("tree.leptons"  + postfix).size() == 2:
#         eventPassed = True
#         leptonFlavour = eval("tree.leptonFlavour"  + postfix)
# elif eval("tree.exclusiveTrack"  + postfix) == 1 and tree.BTagsDeepMedium == 0:
#     eventPassed = True
#     leptonFlavour = eval("tree.exclusiveTrackLeptonFlavour"  + postfix)

def main():
    print "Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    fnew = TFile(output_file,'recreate')
    c1 = TCanvas("c1", "c1", 800, 800)
    c1.cd()
    
    print "Getting signals..."
    
    for filename in glob(signal_dir + "/*"):
        print "Opening", filename    
        deltaM = utils.getPointFromSamFileName(filename)
        print "deltaM=" + deltaM
        f = TFile(filename)
        c = f.Get('tEvent')

        for lep in ["Muons", "Electrons"]:
            c1.cd()
            hist = utils.getHistogramFromTree(deltaM + "_1t_" + lep, c, "exTrack_dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 *  Weight * BranchingRatio * (exclusiveTrack == 1 && MHT >= 220 && MET >= 200 && exTrack_invMass < 30 && BTagsDeepMedium == 0 && exclusiveTrackLeptonFlavour == \"" + lep + "\")", True)
            hist.Sumw2()
            fnew.cd()
            hist.Write()
            
            hist = utils.getHistogramFromTree(deltaM + "_2l_" + lep, c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons == 1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && BTagsDeepMedium == 0 && vetoElectronsTightID == 0 && vetoMuonsPassIso == 0 && @leptons.size() == 2 && leptonFlavour == \"" + lep + "\" && sameSign == 0)", True)
            #non-orth
            #hist = utils.getHistogramFromTree(deltaM + "_2l", c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1)", True)
            hist.Sumw2()
            fnew.cd()
            hist.Write()
            
        f.Close()
    
    bg_1t_hist = {}
    bg_2l_hist = {}
    
    print "Getting BG..."
    
    for filename in glob(bg_dir + "/*"):
        print "Opening", filename
        f = TFile(filename)
        c = f.Get('tEvent')
        
        for lep in ["Muons", "Electrons"]:
        
            c1.cd()
            basename = os.path.basename(filename).split(".")[0]
            hist = utils.getHistogramFromTree(basename, c, "exTrack_dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * (exclusiveTrack == 1 && MHT >= 220 && MET >= 200 && exTrack_invMass < 30 && BTagsDeepMedium == 0 && exclusiveTrackLeptonFlavour == \"" + lep + "\")", True)
            hist.Sumw2()
            if bg_1t_hist.get(lep) is None:
                bg_1t_hist[lep] = hist
            else:
                bg_1t_hist[lep].Add(hist)
        
            hist = utils.getHistogramFromTree(basename, c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * (twoLeptons == 1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && BTagsDeepMedium == 0 && vetoElectronsTightID == 0 && vetoMuonsPassIso == 0 && @leptons.size() == 2 && leptonFlavour == \"" + lep + "\" && sameSign == 0)", True)
            #non-orth
            #hist = utils.getHistogramFromTree(basename, c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * (MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1)", True)
            hist.Sumw2()
            if bg_2l_hist.get(lep) is None:
                bg_2l_hist[lep] = hist
            else:
                bg_2l_hist[lep].Add(hist)
        
        f.Close()
    
    fnew.cd()
    for lep in ["Muons", "Electrons"]:
        bg_1t_hist[lep].Write("bg_1t_" + lep)
        bg_2l_hist[lep].Write("bg_2l_" + lep)
    fnew.Close()
    
    exit(0)
    
    # print "Getting 2l signals..."
#     
#     for filename in glob(signal_2l_dir + "/*"):
#         print "Opening", filename   
#         deltaM = utils.getPointFromSamFileName(filename)
#         print "deltaM=" + deltaM
#         f = TFile(filename)
#         c = f.Get('tEvent')
#         c1.cd()
#         #orth
#         hist = utils.getHistogramFromTree(deltaM + "_2l", c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * ((leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && BTagsDeepMedium == 0 && vetoElectronsTightID == 0 && vetoMuonsPassJetIso == 0)", True)
#         #non-orth
#         #hist = utils.getHistogramFromTree(deltaM + "_2l", c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1)", True)
#         hist.Sumw2()
#         fnew.cd()
#         hist.Write()
#         f.Close()
    
    
    
    # print "Getting 2l BG..."
#     
#     for filename in glob(bg_2l_dir + "/*"):
#         print "Opening", filename
#         f = TFile(filename)
#         c = f.Get('tEvent')
#         c1.cd()
#         basename = os.path.basename(filename).split(".")[0]
#         #orth
#         hist = utils.getHistogramFromTree(basename, c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * ((leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && BTagsDeepMedium == 0 && vetoElectronsTightID == 0 && vetoMuonsPassJetIso == 0)", True)
#         #non-orth
#         #hist = utils.getHistogramFromTree(basename, c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * (MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1)", True)
#         hist.Sumw2()
#         if bg_2l_hist is None:
#             bg_2l_hist = hist
#         else:
#             bg_2l_hist.Add(hist)
#         f.Close()
#     
#     fnew.cd()
#     bg_2l_hist.Write("bg_2l")
#     fnew.Close()
#     
#     exit(0)

main()

# tEvent.Branch('BTagsLoose', var_BTagsLoose,'BTagsLoose/I')
# tEvent.Branch('BTagsMedium', var_BTagsMedium,'BTagsMedium/I')
# tEvent.Branch('BTagsDeepLoose', var_BTagsDeepLoose,'BTagsDeepLoose/I')
# tEvent.Branch('BTagsDeepMedium', var_BTagsDeepMedium,'BTagsDeepMedium/I')
