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

parser = argparse.ArgumentParser(description='Creates root files for limits and significance.')
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
#parser.add_argument('-s', '--single', dest='single', help='Single', action='store_true')
#parser.add_argument('-c', '--cut', nargs=1, help='Cut', required=False)
#parser.add_argument('-obs', '--obs', nargs=1, help='Obs', required=False)
args = parser.parse_args()

output_file = None

sam = True

signal_dir = None
bg_dir = None
data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim/sum"
slim_bg_file = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/slim_sum.root"

if sam:
    signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_sam/sum"
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
else:
    signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_0.4/sum"
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_0.4/sum/type_sum"


if args.output_file:
    output_file = args.output_file[0]
else:
    output_file = "sig_bg_histograms_data_driven_run2.root"

jetIsos = {
    "Electrons": "CorrJetNoMultIso11Dr0.5",
    "Muons" : "CorrJetNoMultIso10Dr0.6"
}

binning = {
    "1t" : {
        "Electrons" : [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,1],
        "Muons" : [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,1]
    },
    "2l" : {
        #"Electrons" : [0,0.1,0.2,0.3,0.35,1],
        #"Muons" : [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,1]
        "Electrons" : [0,0.1,0.2,0.3,1],
        "Muons" : [0,0.05,0.15,0.25,0.35,0.45,0.6,1]
    }
}

tautauSf = {
    "Electrons" : [0.348541885614,0.49607271619],
    "Muons" : [1.44864225388,0.467723615216],
}

sfs = {
    "1t" : {
        "Electrons" : [0.925311207771,0.0859777069028],
        "Muons" : [0.997950792313,0.063920042557]
    },
    "2l" : {
        "Electrons" : [0.384615391493,0.202398004455],
        "Muons" : [0.460431665182,0.069552990166]
    }
}

luminosity = 35.7389543
lumi_weight = luminosity * 1000.
lumi_weight_for_data = utils.LUMINOSITY / lumi_weight

print("lumi_weight_for_data", lumi_weight_for_data)
#exit(0)

######## END OF CMDLINE ARGUMENTS ########

def main():
    print "Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    bg_1t_hist = {}
    bg_2l_hist = {}
    
    fnew = TFile(output_file,'recreate')
    c1 = TCanvas("c1", "c1", 800, 800)
    c1.cd()
    
    i=0
    print "Getting DATA DRIVEN BG..."
    data_files = glob(data_dir + "/*")
    for filename in data_files:
        print "Opening", filename
        f = TFile(filename)
        c = f.Get('tEvent')
        
        for lep in ["Muons", "Electrons"]:
        
            c1.cd()
            
            histName = "bg_1t_" + lep
            #drawString = str(utils.LUMINOSITY) + " * passedMhtMet6pack * tEffhMetMhtRealXMht2016 *  Weight * BranchingRatio * (exclusiveTrack" + jetIsos[lep] + " == 1 && MET >= 140 && MHT >= 220 && exTrack_invMass" + jetIsos[lep] + " < 12 && BTagsDeepMedium == 0 && exclusiveTrackLeptonFlavour" + jetIsos[lep] + " == \"" + lep + "\")"
            
            
            base_cond = "(passedMhtMet6pack == 1 && passesUniversalSelection == 1 && MinDeltaPhiMhtJets > 0.4 && MHT >= 220 &&  MET >= 140 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)"
            sc_cond =  "(" + ("sc_exTrack_deltaR > 0.05 && " if lep == "Electrons" else "") + "sc_exclusiveTrack%%% == 1 && sc_trackBDT%%% > 0 && sc_exTrack_invMass%%% < 12 && sc_exTrack_dilepBDT%%% > 0 && sc_exclusiveTrackLeptonFlavour%%% == \""+lep+"\")"
            cond = base_cond + " && " + sc_cond
            drawString = cond.replace("%%%", jetIsos[lep])
            
            
            #drawString = str(lumi_weight_for_data) + " * passesUniversalSelection * passedMhtMet6pack * (MinDeltaPhiMhtJets > 0.4 && MHT >= 220 &&  MET >= 140 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && exclusiveTrack" + jetIsos[lep] + " == 1 && exTrack_invMass" + jetIsos[lep] + " < 12 && exclusiveTrackLeptonFlavour" + jetIsos[lep] + " == \"" + lep + "\"" + (" && exTrack_deltaR" + jetIsos[lep] + " > 0.05" if lep == "Electrons" else "") +  " && trackBDT" + jetIsos[lep] + " > 0)"
            hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, "sc_exTrack_dilepBDT" + jetIsos[lep], binning["1t"][lep], drawString, False)
            #hist = utils.getHistogramFromTree(, c, , bins, -1, 1, , True)
            #hist = utils.getHistogramFromTree(deltaM + "_1t_" + lep, c, "MET", bins, 0, 500, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 *  Weight * BranchingRatio * (exclusiveTrack" + jetIsos[lep] + " == 1 && MHT >= 220 && exTrack_invMass" + jetIsos[lep] + " < 12 && BTagsDeepMedium == 0 && exclusiveTrackLeptonFlavour" + jetIsos[lep] + " == \"" + lep + "\")", True)
            print("For 1t", lep, "got histogram with", hist.Integral())
            hist.Sumw2()
            print("Scaling historgram with", lumi_weight_for_data)
            hist.Scale(lumi_weight_for_data)
            utils.scaleHistogram(hist, sfs["1t"][lep][0], sfs["1t"][lep][1])
            if bg_1t_hist.get(histName) is None:
                bg_1t_hist[histName] = hist
            else:
                bg_1t_hist[histName].Add(hist)
            
            
            orthOpt = [True, False] if lep == "Muons" else [False]
            orth_cond = " && (leptons" + jetIsos[lep] + "[1].Pt() <= 3.5 || deltaR" + jetIsos[lep] + " <= 0.3)"
            for orth in orthOpt:
                c1.cd()
                print("2l",lep,orth)
                drawString = "(passedMhtMet6pack == 1 && passesUniversalSelection == 1 && twoLeptons%%% == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMhtJets > 0.4 && MET >= 140 && MHT >= 220 && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && leptonFlavour%%% == \"" + lep + "\" && sameSign%%% == 0 && isoCr%%% >= 1 )"
                drawString = drawString.replace("%%%", jetIsos[lep])
                histName = "bg_2l_" + lep + ("_orth" if orth else "")
                hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, "dilepBDT" + jetIsos[lep], binning["2l"][lep], drawString, False)
                hist.Sumw2()
                hist.Scale(lumi_weight_for_data)
                utils.scaleHistogram(hist, sfs["2l"][lep][0], sfs["2l"][lep][1])
                
                if bg_2l_hist.get(histName) is None:
                    bg_2l_hist[histName] = hist
                else:
                    bg_2l_hist[histName].Add(hist)
        
        f.Close()
        #i += 1
        #if i > 5:
        #    break
    
    print("bg_2l_hist", bg_2l_hist)
    
    print "Getting signals..."
    
    signal_hists = {}
    i = 0
    for filename in glob(signal_dir + "/*"):
        print "Opening", filename  
        if sam:
            deltaM = utils.getPointFromSamFileName(filename)
        else:
            deltaM = utils.getPointFromFileName(filename)  
        #if deltaM != "mChipm140GeV_dm4p28GeV":
        #    continue
        print "deltaM=" + deltaM
        f = TFile(filename)
        c = f.Get('tEvent')

        for lep in ["Muons", "Electrons"]:
            c1.cd()
            # prev
            #hist = utils.getHistogramFromTree(deltaM + "_1t_" + lep, c, "exTrack_dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 *  Weight * BranchingRatio * (exclusiveTrack == 1 && MHT >= 220 && MET >= 200 && exTrack_invMass < 30 && BTagsDeepMedium == 0 && exTrack_dilepBDT >= 0 && exclusiveTrackLeptonFlavour == \"" + lep + "\")", True)
            # Making new version without trackBDT precut
            histName = deltaM + "_1t_" + lep
            #drawString = str(utils.LUMINOSITY) + " * passedMhtMet6pack * tEffhMetMhtRealXMht2016 *  Weight * BranchingRatio * (exclusiveTrack" + jetIsos[lep] + " == 1 && MET >= 140 && MHT >= 220 && exTrack_invMass" + jetIsos[lep] + " < 12 && BTagsDeepMedium == 0 && exclusiveTrackLeptonFlavour" + jetIsos[lep] + " == \"" + lep + "\")"
            drawString = str(utils.LUMINOSITY) + " * FastSimWeightPR31285To36122 * passesUniversalSelection * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (MinDeltaPhiMhtJets > 0.4 && MHT >= 220 &&  MET >= 140 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && exclusiveTrack" + jetIsos[lep] + " == 1 && exTrack_invMass" + jetIsos[lep] + " < 12 && exclusiveTrackLeptonFlavour" + jetIsos[lep] + " == \"" + lep + "\"" + (" && exTrack_deltaR" + jetIsos[lep] + " > 0.05" if lep == "Electrons" else "") +  " && trackBDT" + jetIsos[lep] + " > 0)"
            hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, "exTrack_dilepBDT" + jetIsos[lep], binning["1t"][lep], drawString, False)
            #hist = utils.getHistogramFromTree(, c, , bins, -1, 1, , True)
            #hist = utils.getHistogramFromTree(deltaM + "_1t_" + lep, c, "MET", bins, 0, 500, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 *  Weight * BranchingRatio * (exclusiveTrack" + jetIsos[lep] + " == 1 && MHT >= 220 && exTrack_invMass" + jetIsos[lep] + " < 12 && BTagsDeepMedium == 0 && exclusiveTrackLeptonFlavour" + jetIsos[lep] + " == \"" + lep + "\")", True)
            
            hist.Sumw2()
            if signal_hists.get(histName) is None:
                signal_hists[histName] = hist
            else:
                signal_hists[histName].Add(hist)
            
            
            orthOpt = [True, False] if lep == "Muons" else [False]
            orth_cond = " && (leptons" + jetIsos[lep] + "[1].Pt() <= 3.5 || deltaR" + jetIsos[lep] + " <= 0.3)"
            for orth in orthOpt:
                c1.cd()
                
                
                drawString = str(utils.LUMINOSITY) + " * FastSimWeightPR31285To36122* passesUniversalSelection * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons" + jetIsos[lep] + " == 1 " + (orth_cond if orth else "") + " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && invMass" + jetIsos[lep] + " < 12  && invMass" + jetIsos[lep] + " > 0.4 && !(invMass" + jetIsos[lep] + " > 3 && invMass" + jetIsos[lep] + " < 3.2) && !(invMass" + jetIsos[lep] + " > 0.75 && invMass" + jetIsos[lep] + " < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && leptonFlavour" + jetIsos[lep] + " == \"" + lep + "\" && sameSign" + jetIsos[lep] + " == 0 && isoCr" + jetIsos[lep] + " == 0)"
                histName = deltaM + "_2l_" + lep + ("_orth" if orth else "")
                hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, "dilepBDT" + jetIsos[lep], binning["2l"][lep], drawString, False)
                #hist = utils.getHistogramFromTree(deltaM + "_2l_" + ("orth_" if orth else "") + lep , c, "dilepBDT" + jetIsos[lep], bins, -1, 1, cond, True)
                #hist = utils.getHistogramFromTree(, c, , bins, -1, 1, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons" + jetIsos[lep] + " == 1 " + (orth_cond if orth else "") + " && MET >= 140 && MHT >= 220 && invMass" + jetIsos[lep] + " < 12  && invMass" + jetIsos[lep] + " > 0.4 && !(invMass" + jetIsos[lep] + " > 3 && invMass" + jetIsos[lep] + " < 3.2) && !(invMass" + jetIsos[lep] + " > 0.75 && invMass" + jetIsos[lep] + " < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && @leptons" + jetIsos[lep] + ".size() == 2 && leptonFlavour" + jetIsos[lep] + " == \"" + lep + "\" && sameSign" + jetIsos[lep] + " == 0 && isoCr" + jetIsos[lep] + " == 0)", True)
                #hist = utils.getHistogramFromTree(deltaM + "_2l_" + ("orth_" if orth else "") + lep, c, "MET", bins, 0, 500, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons" + jetIsos[lep] + " == 1 " + (orth_cond if orth else "") + " && MHT >= 220 && invMass" + jetIsos[lep] + " < 12  && invMass" + jetIsos[lep] + " > 0.4 && !(invMass" + jetIsos[lep] + " > 3 && invMass" + jetIsos[lep] + " < 3.2) && !(invMass" + jetIsos[lep] + " > 0.75 && invMass" + jetIsos[lep] + " < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && @leptons" + jetIsos[lep] + ".size() == 2 && leptonFlavour" + jetIsos[lep] + " == \"" + lep + "\" && sameSign" + jetIsos[lep] + " == 0 && isoCr" + jetIsos[lep] + " == 0)", True)
                #non-orth
                #hist = utils.getHistogramFromTree(deltaM + "_2l", c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1)", True)
                if signal_hists.get(histName) is None:
                    signal_hists[histName] = hist
                else:
                    signal_hists[histName].Add(hist)
        f.Close()
        #i += 1
        #if i > 5:
        #    break
    
    print "Getting Mtautau BG..."
    bg_slim_files = [slim_bg_file]
    for filename in bg_slim_files:
        print "Opening", filename
        f = TFile(filename)
        c = f.Get('tEvent')
        
        for lep in ["Muons", "Electrons"]:
        
            c1.cd()
            orthOpt = [True, False] if lep == "Muons" else [False]
            orth_cond = " && (leptons" + jetIsos[lep] + "[1].Pt() <= 3.5 || deltaR" + jetIsos[lep] + " <= 0.3)"
            for orth in orthOpt:
                c1.cd()
                print("2l",lep,orth)
                
                drawString = str(utils.LUMINOSITY) + " * passesUniversalSelection * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons" + jetIsos[lep] + " == 1 " + (orth_cond if orth else "") + " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && invMass" + jetIsos[lep] + " < 12  && invMass" + jetIsos[lep] + " > 0.4 && !(invMass" + jetIsos[lep] + " > 3 && invMass" + jetIsos[lep] + " < 3.2) && !(invMass" + jetIsos[lep] + " > 0.75 && invMass" + jetIsos[lep] + " < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && leptonFlavour" + jetIsos[lep] + " == \"" + lep + "\" && sameSign" + jetIsos[lep] + " == 0 && isoCr" + jetIsos[lep] + " == 0 && tautau" + jetIsos[lep] + ")"
                histName = "bg_2l_" + lep + ("_orth" if orth else "")
                hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, "dilepBDT" + jetIsos[lep], binning["2l"][lep], drawString, False)
                hist.Sumw2()
                utils.scaleHistogram(hist, tautauSf[lep][0], tautauSf[lep][1])
                if bg_2l_hist.get(histName) is None:
                    print("WTF!! histName", histName)
                    bg_2l_hist[histName] = hist
                else:
                    bg_2l_hist[histName].Add(hist)
                
                
                #hist = utils.getHistogramFromTree("bg_2l_" + lep + ("_orth" if orth else ""), c, "dilepBDT" + jetIsos[lep], bins, -1, 1, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons" + jetIsos[lep] + " == 1 "  + (orth_cond if orth else "") +  " && MET >= 140 && MHT >= 220 && invMass" + jetIsos[lep] + " < 12  && invMass" + jetIsos[lep] + " > 0.4 && !(invMass" + jetIsos[lep] + " > 3 && invMass" + jetIsos[lep] + " < 3.2) && !(invMass" + jetIsos[lep] + " > 0.75 && invMass" + jetIsos[lep] + " < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && @leptons" + jetIsos[lep] + ".size() == 2 && leptonFlavour" + jetIsos[lep] + " == \"" + lep + "\" && sameSign" + jetIsos[lep] + " == 0 && isoCr" + jetIsos[lep] + " == 0)", True)
                #hist = utils.getHistogramFromTree(basename, c, "MET", bins, 0, 500, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons" + jetIsos[lep] + " == 1 "  + (orth_cond if orth else "") +  " && MHT >= 220 && invMass" + jetIsos[lep] + " < 12  && invMass" + jetIsos[lep] + " > 0.4 && !(invMass" + jetIsos[lep] + " > 3 && invMass" + jetIsos[lep] + " < 3.2) && !(invMass" + jetIsos[lep] + " > 0.75 && invMass" + jetIsos[lep] + " < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && @leptons" + jetIsos[lep] + ".size() == 2 && leptonFlavour" + jetIsos[lep] + " == \"" + lep + "\" && sameSign" + jetIsos[lep] + " == 0 && isoCr" + jetIsos[lep] + " == 0)", True)
                #non-orth
                #hist = utils.getHistogramFromTree(basename, c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * (MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1)", True)
        
        f.Close()
    
    
    fnew.cd()
    
    for hist in signal_hists:
        signal_hists[hist].Write()
    for hist in bg_1t_hist:
        bg_1t_hist[hist].Write()
    for hist in bg_2l_hist:
        bg_2l_hist[hist].Write()
    
    # for lep in ["Muons", "Electrons"]:
#         
#         bg_1t_hist[lep].Write("bg_1t_" + lep)
#         orthOpt = [True, False] if lep == "Muons" else [False]
#         for orth in orthOpt:
#             bg_2l_hist[lep + ("_orth" if orth else "")].Write("bg_2l_" + ("orth_" if orth else "") + lep)
    fnew.Close()
    
    exit(0)
    
main()
