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

parser = argparse.ArgumentParser(description='Calculate scale and normalisation factors.')
#parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
#parser.add_argument('-s', '--single', dest='single', help='Single', action='store_true')
#parser.add_argument('-c', '--cut', nargs=1, help='Cut', required=False)
#parser.add_argument('-obs', '--obs', nargs=1, help='Obs', required=False)
args = parser.parse_args()

output_file = None

signal_dir = None
bg_dir = None

bg_slim_file = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/slim_sum.root"
data_slim_file = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim/slim_sum/slim_sum.root"

luminosity = 35.712736198
lumi_weight = luminosity * 1000.

######## END OF CMDLINE ARGUMENTS ########

def main():
    print "Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    jetiso = "CorrJetIso10.5Dr0.55"
    
    c1 = TCanvas("c1", "c1", 800, 800)
    c1.cd()
       
    bg_1t_hist = {}
    
    bg_2l_hist = {}
    data_2l_hist = {}
    
    mtautau_min = 0
    mtautau_max = 160
    
    print "Getting BG..."
    bg_files = [bg_slim_file]
    for filename in bg_files:#glob(bg_dir + "/*"):
        print "=====================================\n\n\n\n\n\n\n\n\n\n\n"
        print "Opening", filename
        f = TFile(filename)
        c = f.Get('tEvent')
        
        for lep in ["Muons", "Electrons"]:
            
            if lep == "Electrons":
                continue

            c1.cd()

            orthOpt = [True, False] if lep == "Muons" else [False]
            orth_cond = " && (leptons" + jetiso + "[1].Pt() <= 3.5 || deltaR" + jetiso + " <= 0.3)"
            
            orthOpt = [False]
            
            for orth in orthOpt:
                
                isoCr = False
                
                c1.cd()
                # Get M-tau-tau count
                #(name, tree, obs, bins, minX, maxX, condition, overflow=True, tmpName="hsqrt"
                condition = str(lumi_weight) + " * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * puWeight * (twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && invMass" + jetiso + " < 12  && invMass" + jetiso + " > 0.4 && !(invMass" + jetiso + " > 3 && invMass" + jetiso + " < 3.2) && !(invMass" + jetiso + " > 0.75 && invMass" + jetiso + " < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && mtautau" + jetiso + " > 60 && mtautau"  + jetiso + " < 120 && dilepBDT" + jetiso + " < 0)"
                
                 # Tau-Tau BG inside M-tau-tau Window
                #condition = str(lumi_weight) + " * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * puWeight * (twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && mtautau" + jetiso + " > 60 && mtautau"  + jetiso + " < 120 && dilepBDT" + jetiso + " < 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && tautau" + jetiso + " == 1)"
                condition = str(lumi_weight) + " * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * puWeight * (twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && nmtautau" + jetiso + " > " + str(mtautau_min) + " && nmtautau"  + jetiso + " < " + str(mtautau_max) + " && dilepBDT" + jetiso + " < 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && tautau" + jetiso + " == 1)"
                print "condition=" + condition
                hist = utils.getHistogramFromTree("bg_2l_" + lep + ("_orth" if orth else "") + "_" + jetiso + ("_isoCr" if isoCr else ""), c, "dilepBDT" + jetiso, 1, -1, 1, condition, False)
                hist.Sumw2()
                histName = "inside_mtautau_tautau_" + lep + ("_orth" if orth else "") + "_" + jetiso + ("_isoCr" if isoCr else "")
                if bg_2l_hist.get(histName) is None:
                    bg_2l_hist[histName] = hist
                else:
                    bg_2l_hist[histName].Add(hist)
                
                for isoCr in [True, False]:
                    
                    
                    # Non-Tau-Tau BG inside M-tau-tau Window
                    #condition = str(lumi_weight) + " * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * puWeight * (twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && mtautau" + jetiso + " > 60 && mtautau"  + jetiso + " < 120 && dilepBDT" + jetiso + " < 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && tautau" + jetiso + " == 0)"
                    condition = str(lumi_weight) + " * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * puWeight * (twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && nmtautau" + jetiso + " > " + str(mtautau_min) + " && nmtautau"  + jetiso + " < " + str(mtautau_max) + " && dilepBDT" + jetiso + " < 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && tautau" + jetiso + " == 0)"
                    print "condition=" + condition
                    hist = utils.getHistogramFromTree("bg_2l_" + lep + ("_orth" if orth else "") + "_" + jetiso + ("_isoCr" if isoCr else ""), c, "dilepBDT" + jetiso, 1, -1, 1, condition, False)
                    hist.Sumw2()
                    histName = "inside_mtautau_nontautau_" + lep + ("_orth" if orth else "") + "_" + jetiso + ("_isoCr" if isoCr else "")
                    if bg_2l_hist.get(histName) is None:
                        bg_2l_hist[histName] = hist
                    else:
                        bg_2l_hist[histName].Add(hist)
                
                    # Non-Tau-Tau BG outside nM-tau-tau Window (two versions for iso-cr and non-isocr)
                    condition = str(lumi_weight) + " * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * puWeight * (twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && ( nmtautau" + jetiso + " < " + str(mtautau_min) + " || nmtautau"  + jetiso + " > " + str(mtautau_max) + " ) && dilepBDT" + jetiso + " < 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && tautau" + jetiso + " == 0)"
                    
                    
                    #condition = str(lumi_weight) + " * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * puWeight * (twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && invMass" + jetiso + " < 12  && invMass" + jetiso + " > 0.4 && !(invMass" + jetiso + " > 3 && invMass" + jetiso + " < 3.2) && !(invMass" + jetiso + " > 0.75 && invMass" + jetiso + " < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && ( nmtautau" + jetiso + " < 0 || nmtautau"  + jetiso + " > 160 ) && dilepBDT" + jetiso + " < 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && tautau" + jetiso + " == 0)"
                    
                    #condition = str(lumi_weight) + " * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * puWeight * (twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && dilepBDT" + jetiso + " < 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && tautau" + jetiso + " == 0)"
                    histName = "outside_nmtautau_nontautau_" + lep + ("_orth" if orth else "") + "_" + jetiso + ("_isoCr" if isoCr else "")
                    
                    print "\n\n\n\n\n\n\nname=" + histName + " condition=" + condition
                    hist = utils.getHistogramFromTree("bg_2l_" + lep + ("_orth" if orth else "") + "_" + jetiso + ("_isoCr" if isoCr else ""), c, "dilepBDT" + jetiso, 1, -1, 1, condition, False)
                    hist.Sumw2()
                    
                    if bg_2l_hist.get(histName) is None:
                        bg_2l_hist[histName] = hist
                    else:
                        bg_2l_hist[histName].Add(hist)
                
                
        f.Close()
    print bg_2l_hist
    
    print "\n\n\n\n\n\n"
    for bgHistName in bg_2l_hist:
        bgHist = bg_2l_hist[bgHistName]
        bgNum = bgHist.GetBinContent(1)
        bgError = bgHist.GetBinError(1)
        print bgHistName, "bgNum", bgNum, "bgError", bgError
    
    
    print "\n\n\niso-cr MC scale factor - Non-Tau-Tau BG outside nM-tau-tau Window, BDT sideband"
    numHist = bg_2l_hist["outside_nmtautau_nontautau_Muons_CorrJetIso10.5Dr0.55"].Clone()
    denHist = bg_2l_hist["outside_nmtautau_nontautau_Muons_CorrJetIso10.5Dr0.55_isoCr"]
    print "num", numHist.GetBinContent(1), "den", denHist.GetBinContent(1)
    numHist.Divide(denHist)
    print "nf", numHist.GetBinContent(1), "err", numHist.GetBinError(1), "rel-err", numHist.GetBinError(1)/numHist.GetBinContent(1)
    
    numHist = bg_2l_hist["inside_mtautau_tautau_Muons_CorrJetIso10.5Dr0.55"].Clone()
    denHist = bg_2l_hist["inside_mtautau_nontautau_Muons_CorrJetIso10.5Dr0.55"].Clone()
    
    denHist.Add(numHist)
    numHist.Divide(denHist)
    
    print "\n\n\ntau-tau MC purity inside nM-tau-tau Window, BDT sideband, [" + str(mtautau_min) + "," + str(mtautau_max) + "]"
    print "tautau MC", bg_2l_hist["inside_mtautau_tautau_Muons_CorrJetIso10.5Dr0.55"].GetBinContent(1), "err", bg_2l_hist["inside_mtautau_tautau_Muons_CorrJetIso10.5Dr0.55"].GetBinError(1)
    print "non-tautau MC", bg_2l_hist["inside_mtautau_nontautau_Muons_CorrJetIso10.5Dr0.55"].GetBinContent(1), "err", bg_2l_hist["inside_mtautau_nontautau_Muons_CorrJetIso10.5Dr0.55"].GetBinError(1)
    print "tautau MC purity", numHist.GetBinContent(1), "err", numHist.GetBinError(1), "rel-err", numHist.GetBinError(1)/numHist.GetBinContent(1)
    

    print "\n\n\n\n\n\n\n\n\n\n\nGetting Data..."
    data_files = [data_slim_file]
    for filename in data_files:#glob(bg_dir + "/*"):
        print "====================================="
        print "Opening", filename
        f = TFile(filename)
        c = f.Get('tEvent')
        
        for lep in ["Muons", "Electrons"]:
            
            if lep == "Electrons":
                continue

            c1.cd()

            orthOpt = [True, False] if lep == "Muons" else [False]
            orth_cond = " && (leptons" + jetiso + "[1].Pt() <= 3.5 || deltaR" + jetiso + " <= 0.3)"
            #orthOpt = [False,True]
            print "orthOpt", orthOpt
            for orth in orthOpt:
                
                isoCr = False
                
                c1.cd()
                # Get M-tau-tau count
                #(name, tree, obs, bins, minX, maxX, condition, overflow=True, tmpName="hsqrt"
                condition = "(twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && invMass" + jetiso + " < 12  && invMass" + jetiso + " > 0.4 && !(invMass" + jetiso + " > 3 && invMass" + jetiso + " < 3.2) && !(invMass" + jetiso + " > 0.75 && invMass" + jetiso + " < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && mtautau" + jetiso + " > 60 && mtautau"  + jetiso + " < 120 && dilepBDT" + jetiso + " < 0)"
                
                condition = "(twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && mtautau" + jetiso + " > 60 && mtautau"  + jetiso + " < 120 && dilepBDT" + jetiso + " < 0)"
                
                condition = "(twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && mtautau" + jetiso + " > 60 && mtautau"  + jetiso + " < 120 && dilepBDT" + jetiso + " < 0 && leptonFlavour" + jetiso + " == \"" + lep + "\")"
                
                condition = "(twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && nmtautau" + jetiso + " > " + str(mtautau_min) + " && nmtautau"  + jetiso + " < " + str(mtautau_max) + " && dilepBDT" + jetiso + " < 0 && leptonFlavour" + jetiso + " == \"" + lep + "\")"
                
                #print "condition=" + condition
                histName = "inside_mtautau_" + lep + ("_orth" if orth else "") + "_" + jetiso + ("_isoCr" if isoCr else "")
                hist = utils.getHistogramFromTree("data_2l_" + lep + ("_orth" if orth else "") + "_" + jetiso + ("_isoCr" if isoCr else ""), c, "dilepBDT" + jetiso, 1, -1, 1, condition, False)
                hist.Sumw2()
                
                print "-----orth", orth, "histName", histName
                if data_2l_hist.get(histName) is None:
                    data_2l_hist[histName] = hist
                else:
                    data_2l_hist[histName].Add(hist)
                
                isoCr = True
                
                histName = "inside_mtautau_nontautau_" + lep + ("_orth" if orth else "") + "_" + jetiso + ("_isoCr" if isoCr else "")
                condition = "(twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && mtautau" + jetiso + " > 60 && mtautau"  + jetiso + " < 120 && dilepBDT" + jetiso + " < 0 && leptonFlavour" + jetiso + " == \"" + lep + "\")"
                condition = "(twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && nmtautau" + jetiso + " > " + str(mtautau_min) + " && nmtautau"  + jetiso + " < " + str(mtautau_max) + "  && dilepBDT" + jetiso + " < 0 && leptonFlavour" + jetiso + " == \"" + lep + "\")"
                hist = utils.getHistogramFromTree("inside_mtautau_nontautau_data_2l_" + lep + ("_orth" if orth else "") + "_" + jetiso + ("_isoCr" if isoCr else ""), c, "dilepBDT" + jetiso, 1, -1, 1, condition, False)
                hist.Sumw2()
                #hist.Scale(0.996039628983)
                tmpHist = TH1F("nf", "nf", 1, 0, 1)
                tmpHist.Sumw2()
                tmpHist.SetBinContent(1, 0.876146793365)
                tmpHist.SetBinError(1, 0.0868347577866)
                hist.Multiply(tmpHist)
                if data_2l_hist.get(histName) is None:
                    data_2l_hist[histName] = hist
                else:
                    data_2l_hist[histName].Add(hist)
                

                # Get iso-cr count
                for isoCr in [True, False]:
                    #condition = "(twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && invMass" + jetiso + " < 12  && invMass" + jetiso + " > 0.4 && !(invMass" + jetiso + " > 3 && invMass" + jetiso + " < 3.2) && !(invMass" + jetiso + " > 0.75 && invMass" + jetiso + " < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && mtautau" + jetiso + " > 200 && dilepBDT" + jetiso + " < 0)"
                    #condition = "(twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && invMass" + jetiso + " > 0.4 && !(invMass" + jetiso + " > 3 && invMass" + jetiso + " < 3.2) && !(invMass" + jetiso + " > 0.75 && invMass" + jetiso + " < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && ( nmtautau" + jetiso + " < " + str(mtautau_min) + " || nmtautau"  + jetiso + " > " + str(mtautau_max) + " ) && dilepBDT" + jetiso + " < 0)"
                    
                    condition = "(twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && invMass" + jetiso + " < 12  && invMass" + jetiso + " > 0.4 && !(invMass" + jetiso + " > 3 && invMass" + jetiso + " < 3.2) && !(invMass" + jetiso + " > 0.75 && invMass" + jetiso + " < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && ( nmtautau" + jetiso + " < " + str(mtautau_min) + " || nmtautau"  + jetiso + " > " + str(mtautau_max) + " ) && dilepBDT" + jetiso + " < 0)"
                    
                    
                    #print "condition=" + condition
                    hist = utils.getHistogramFromTree("data_2l_" + lep + ("_orth" if orth else "") + "_" + jetiso + ("_isoCr" if isoCr else ""), c, "dilepBDT" + jetiso, 1, -1, 1, condition, False)
                    hist.Sumw2()
                    histName = "iso_cr_" + lep + ("_orth" if orth else "") + "_" + jetiso + ("_isoCr" if isoCr == True else "")
                    if data_2l_hist.get(histName) is None:
                        data_2l_hist[histName] = hist
                    else:
                        data_2l_hist[histName].Add(hist)
                
        f.Close()
    print "\n\n\n\n\n"
    print data_2l_hist
    print "\n\n\n\n\n"
    for dataHistName in data_2l_hist:
        dataHist = data_2l_hist[dataHistName]
        dataNum = dataHist.GetBinContent(1)
        dataError = dataHist.GetBinError(1)
        print dataHistName, "dataNum", dataNum, "dataError", dataError
    
    print "=====================================\n\n\n\n\n\n\n\n\n\n\n"
        
    print "\n\n\niso-cr scale factor"
    numHist = data_2l_hist["iso_cr_Muons_CorrJetIso10.5Dr0.55"]
    denHist = data_2l_hist["iso_cr_Muons_CorrJetIso10.5Dr0.55_isoCr"]
    print "num", numHist.GetBinContent(1), "den", denHist.GetBinContent(1)
    numHist.Divide(denHist)
    print "sf", numHist.GetBinContent(1), "err", numHist.GetBinError(1), "rel-err", numHist.GetBinError(1)/numHist.GetBinContent(1)
 
 
    print "\n\n\niso-cr scale factor - ANALYSIS ORTH"
    numHist = data_2l_hist["iso_cr_Muons_orth_CorrJetIso10.5Dr0.55"]
    denHist = data_2l_hist["iso_cr_Muons_orth_CorrJetIso10.5Dr0.55_isoCr"]
    print "num", numHist.GetBinContent(1), "den", denHist.GetBinContent(1)
    numHist.Divide(denHist)
    print "sf", numHist.GetBinContent(1), "err", numHist.GetBinError(1), "rel-err", numHist.GetBinError(1)/numHist.GetBinContent(1)
    
    
#     print "\n\n\nmtautau normalisation factor - Orth"
#     numHist = data_2l_hist["Muons_orth_CorrJetIso10.5Dr0.55"]
#     denHist = bg_2l_hist["Muons_orth_CorrJetIso10.5Dr0.55"]
#     print "num", numHist.GetBinContent(1), "den", denHist.GetBinContent(1)
#     numHist.Divide(denHist)
#     print "sf", numHist.GetBinContent(1), "err", numHist.GetBinError(1), "rel-err", numHist.GetBinError(1)/numHist.GetBinContent(1)
    
    # print "\n\n\nmtautau normalisation factor"
#     numHist = data_2l_hist["Muons_CorrJetIso10.5Dr0.55"]
#     denHist = bg_2l_hist["Muons_CorrJetIso10.5Dr0.55"]
#     print "num", numHist.GetBinContent(1), "den", denHist.GetBinContent(1)
#     numHist.Divide(denHist)
#     print "sf", numHist.GetBinContent(1), "err", numHist.GetBinError(1), "rel-err", numHist.GetBinError(1)/numHist.GetBinContent(1)
#    
    
    print "\n\n\nmtautau normalisation factor - non-tautau removed"
    numHist = data_2l_hist["inside_mtautau_Muons_CorrJetIso10.5Dr0.55"]
    print "num", numHist.GetBinContent(1), "err", numHist.GetBinError(1), "rel-err", numHist.GetBinError(1)/numHist.GetBinContent(1)
    nonTautauHist = data_2l_hist["inside_mtautau_nontautau_Muons_CorrJetIso10.5Dr0.55_isoCr"]
    print "nonTautauHist", nonTautauHist.GetBinContent(1), "err", nonTautauHist.GetBinError(1), "rel-err", nonTautauHist.GetBinError(1)/nonTautauHist.GetBinContent(1)

    nonTautauHistMC = bg_2l_hist["inside_mtautau_nontautau_Muons_CorrJetIso10.5Dr0.55"]
    print "nonTautauHistMC", nonTautauHistMC.GetBinContent(1), "err", nonTautauHistMC.GetBinError(1), "rel-err", nonTautauHistMC.GetBinError(1)/nonTautauHistMC.GetBinContent(1)
    
    
    denHist = bg_2l_hist["inside_mtautau_tautau_Muons_CorrJetIso10.5Dr0.55"]
    print "num", numHist.GetBinContent(1), "den", denHist.GetBinContent(1)
    
    print "After Subtraction"
    numHist.Add(nonTautauHist, -1)
    print "num", numHist.GetBinContent(1), "den", denHist.GetBinContent(1)
    
    numHist.Divide(denHist)
    print "sf", numHist.GetBinContent(1), "err", numHist.GetBinError(1), "rel-err", numHist.GetBinError(1)/numHist.GetBinContent(1)
   
    
    exit(0)
    
main()
