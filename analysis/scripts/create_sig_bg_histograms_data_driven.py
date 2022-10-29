#!/usr/bin/env python3.8

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
import analysis_selections

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

gSystem.Load('LumiSectMap_C')
from ROOT import LumiSectMap

#lumi = 5746.370
#weight = lumi / utils.LUMINOSITY

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Creates root files for limits and significance.')
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
args = parser.parse_args()

sam = True

wanted_year = "2017"

print("WANTED YEAR " + wanted_year)

required_category = "all"


required_category = "tracks"
required_category = "leptons"

use_uniform_binning = True

# required_lepton = "Muons"
# jetiso = "CorrJetNoMultIso10Dr0.6"
# 
# required_lepton = "Electrons"
# jetiso = "CorrJetNoMultIso10Dr0.5"


output_file = None

if args.output_file:
    output_file = args.output_file[0]
else:
    output_file = "sig_bg_histograms_data_driven_" + wanted_year + "_" + required_category + ("_uniform_binning" if use_uniform_binning else "") + ".root"

print("output_file=" + output_file)


signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_sam/sum"
bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/slim_sum_total"
data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim/slim_sum"

if required_category != "leptons":
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim/sum"

data_pattern = "*"

if wanted_year != "2016":
    if wanted_year == "2017":
        signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_phase1/sum"
    elif wanted_year == "2018":
        signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_phase1_2018/sum"
    if required_category != "leptons":
        bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_phase1/sum/type_sum"
        data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_phase1/sum"
        if wanted_year == "2017":
            data_pattern = "Run2017*"
        elif wanted_year == "2018":
            data_pattern = "Run2018*"
    else:
        bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_phase1/sum/slim_sum_total"
        if wanted_year == "2017":
            data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_phase1/slim_2017"
        elif wanted_year == "2018":
            data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_phase1/slim_2018"
        elif wanted_year == "phase1":
            data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_phase1/slim_sum"

#luminosity = analysis_selections.luminosities[wanted_year]
#lumi_weight = luminosity * 1000.

# mtautauveto = " && (nmtautau%%% > 130 || nmtautau%%% < 40)"
# veto_tautau = True
# 
# mtautauVetos = {
#     "Muons" : " && (nmtautau%%% > 130 || nmtautau%%% < 40)",
#     "Electrons" : " && (nmtautau%%% > 160 || nmtautau%%% < 0)"
# }



# sfs = {
#     "1t" : {
#         "Electrons" : [0.925311207771,0.0859777069028],
#         "Muons" : [0.997950792313,0.063920042557]
#     },
#     "2l" : {
#         "Electrons" : [0.384615391493,0.202398004455],
#         "Muons" : [0.460431665182,0.069552990166]
#     }
# }

#uniform_binning = 40

#print("lumi_weight_for_data", lumi_weight_for_data)
#exit(0)

######## END OF CMDLINE ARGUMENTS ########

def main():
    print("Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
    
    bg_1t_hist = {}
    bg_2l_hist = {}
    
    fnew = TFile(output_file,'recreate')
    c1 = TCanvas("c1", "c1", 800, 800)
    c1.cd()
    
    i=0
    print("Getting DATA DRIVEN BG...")
    data_files = glob(data_dir + "/" + data_pattern)
    for filename in data_files:
        #continue
        print("Opening", filename)
        f = TFile(filename)
        c = f.Get('tEvent')
        
        for lep in ["Muons", "Electrons"]:
        
            c1.cd()
            
            if required_category != "leptons":
            
                histName = "bg_1t_" + lep
            
                # base_cond = "(passedMhtMet6pack == 1 && passesUniversalSelection == 1 && MinDeltaPhiMhtJets > 0.4 && MHT >= 220 &&  MET >= 140 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)"
#                 sc_cond =  "(" + ("sc_exTrack_deltaR%%% > 0.05 && " if lep == "Electrons" else "") + "sc_exclusiveTrack%%% == 1 && sc_trackBDT%%% > 0 && sc_exTrack_invMass%%% < 12 && sc_exTrack_dilepBDT%%% > 0 && sc_exclusiveTrackLeptonFlavour%%% == \""+lep+"\")"
#                 cond = base_cond + " && " + sc_cond
#                 drawString = cond.replace("%%%", analysis_selections.jetIsos[lep])
#                 
#                 hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, "sc_exTrack_dilepBDT" + analysis_selections.jetIsos[lep], analysis_selections.binning["1t"][lep], drawString, False)
#                 print("For 1t", lep, "got histogram with", hist.Integral())
#                 hist.Sumw2()
#                 old_sum = hist.Integral()
#                 print("old number", old_sum)
#                 
            
                obs = analysis_selections.exTrackSameSignDilepBDTString[wanted_year] + analysis_selections.jetIsos[lep]
                conditions = analysis_selections.sc_ex_track_full_range_selections
                if lep == "Electrons":
                    conditions = analysis_selections.sc_ex_track_full_range_selections_electrons
                drawString = analysis_selections.getDataString(wanted_year, lep, conditions)
                hist = None
                if use_uniform_binning:
                    hist = utils.getHistogramFromTree(histName, c, obs, analysis_selections.uniform_binning_number, -1, 1, drawString, False)
                else:
                    hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, obs, analysis_selections.binning["1t"][lep], drawString, False)
                new_sum = hist.Integral()
                print("new number", new_sum)
                #print("dif", new_sum-old_sum)
                
                #print("Scaling historgram with", lumi_weight_for_data)
                #hist.Scale(lumi_weight_for_data)
                utils.scaleHistogram(hist, analysis_selections.sfs["tracks"][wanted_year][lep][0], analysis_selections.sfs["tracks"][wanted_year][lep][1])
                if bg_1t_hist.get(histName) is None:
                    bg_1t_hist[histName] = hist
                else:
                    bg_1t_hist[histName].Add(hist)
            
            if required_category != "tracks":
                orthOpt = [True, False] if lep == "Muons" else [False]
                #orth_cond = " && (leptons" + analysis_selections.jetIsos[lep] + "[1].Pt() <= 3.5 || deltaR" + analysis_selections.jetIsos[lep] + " <= 0.3)"
                for orth in orthOpt:
                    c1.cd()
                    print("2l",lep,orth)
                    #drawString = "(passedMhtMet6pack == 1 && passesUniversalSelection == 1 && twoLeptons%%% == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMhtJets > 0.4 && MET >= 140 && MHT >= 220 && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && leptonFlavour%%% == \"" + lep + "\" && sameSign%%% == 0 && isoCr%%% >= 1 " + (mtautauveto if veto_tautau else "") + ")"
                    #drawString = drawString.replace("%%%", analysis_selections.jetIsos[lep])
                    histName = "bg_2l_" + lep + ("_orth" if orth else "")
                    #print("\n\nhistName=" + histName)
                    #print("old drawString="+drawString)
                
                
                
                    #hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, "dilepBDT" + analysis_selections.jetIsos[lep], analysis_selections.binning["2l"][lep], drawString, False)
                    #hist.Sumw2()
                    #hist.Scale(lumi_weight_for_data)
                    #old_sum = hist.Integral()
                    #print("old number", old_sum)
                
                    conditions = analysis_selections.two_leptons_full_bdt_iso_sb_outside_mtautau_window
                    if orth:
                        conditions = analysis_selections.two_leptons_full_bdt_iso_sb_outside_mtautau_window_sos
                    drawString = analysis_selections.getDataString(wanted_year, lep, conditions)
                
                    observable = analysis_selections.dilepBDTString[wanted_year] + analysis_selections.jetIsos[lep]
                    
                    hist = None
                    if use_uniform_binning:
                        hist = utils.getHistogramFromTree(histName, c, observable, analysis_selections.uniform_binning_number, -1, 1, drawString, False)
                    else:
                        hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, observable, analysis_selections.binning["2l"][lep], drawString, False)
                    hist.Sumw2() 
                
                    #print("\n\nnew drawString="+drawString)
                    #hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, "dilepBDT" + analysis_selections.jetIsos[lep], analysis_selections.binning["2l"][lep], drawString, False)
                    #hist.Sumw2()
                    new_sum = hist.Integral()
                    print("\n\nnew number", new_sum)
                    #print("difference", old_sum-new_sum)
                    print("\n\n")
                
                    utils.scaleHistogram(hist, analysis_selections.sfs["leptons"][wanted_year][lep][0], analysis_selections.sfs["leptons"][wanted_year][lep][1])
                
                    if bg_2l_hist.get(histName) is None:
                        bg_2l_hist[histName] = hist
                    else:
                        bg_2l_hist[histName].Add(hist)
        
        f.Close()
        #i += 1
        #if i > 5:
        #    break
    
    print("bg_2l_hist", bg_2l_hist)
    
    print("Getting signals...")
    
    signal_hists = {}
    i = 0
    for filename in glob(signal_dir + "/*"):
        #continue
        print("Opening", filename)
        if sam:
            deltaM = utils.getPointFromSamFileName(filename)
        else:
            deltaM = utils.getPointFromFileName(filename)  
        #if deltaM != "mChipm140GeV_dm4p28GeV":
        #    continue
        print("deltaM=" + deltaM)
        f = TFile(filename)
        c = f.Get('tEvent')

        for lep in ["Muons", "Electrons"]:
            c1.cd()
            
            if required_category != "leptons":
            
                histName = deltaM + "_1t_" + lep
                #drawString = str(utils.LUMINOSITY) + " * passedMhtMet6pack * tEffhMetMhtRealXMht2016 *  Weight * BranchingRatio * (exclusiveTrack" + analysis_selections.jetIsos[lep] + " == 1 && MET >= 140 && MHT >= 220 && exTrack_invMass" + analysis_selections.jetIsos[lep] + " < 12 && BTagsDeepMedium == 0 && exclusiveTrackLeptonFlavour" + analysis_selections.jetIsos[lep] + " == \"" + lep + "\")"
                
                # drawString = "{:.2f}".format(analysis_selections.luminosities[wanted_year]*1000) + " * FastSimWeightPR31285To36122 * passesUniversalSelection * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (MinDeltaPhiMhtJets > 0.4 && MHT >= 220 &&  MET >= 140 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && exclusiveTrack" + analysis_selections.jetIsos[lep] + " == 1 && exTrack_invMass" + analysis_selections.jetIsos[lep] + " < 12 && exclusiveTrackLeptonFlavour" + analysis_selections.jetIsos[lep] + " == \"" + lep + "\"" + (" && exTrack_deltaR" + analysis_selections.jetIsos[lep] + " > 0.05" if lep == "Electrons" else "") +  " && trackBDT" + analysis_selections.jetIsos[lep] + " > 0)"
#                 hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, "exTrack_dilepBDT" + analysis_selections.jetIsos[lep], analysis_selections.binning["1t"][lep], drawString, False)
#                 #hist = utils.getHistogramFromTree(, c, , bins, -1, 1, , True)
#                 #hist = utils.getHistogramFromTree(deltaM + "_1t_" + lep, c, "MET", bins, 0, 500, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 *  Weight * BranchingRatio * (exclusiveTrack" + analysis_selections.jetIsos[lep] + " == 1 && MHT >= 220 && exTrack_invMass" + analysis_selections.jetIsos[lep] + " < 12 && BTagsDeepMedium == 0 && exclusiveTrackLeptonFlavour" + analysis_selections.jetIsos[lep] + " == \"" + lep + "\")", True)
#                 hist.Sumw2()
#                 
#                 old_sum = hist.Integral()
#                 print("old number", old_sum)
                
                obs = analysis_selections.exTrackDilepBDTString[wanted_year] + analysis_selections.jetIsos[lep]
                conditions = analysis_selections.ex_track_full_range_selections
                if lep == "Electrons":
                    conditions = analysis_selections.ex_track_full_range_selections_electrons
                drawString = analysis_selections.getFastSimString(wanted_year, lep, conditions)
                hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, obs, analysis_selections.binning["1t"][lep], drawString, False)
                new_sum = hist.Integral()
                print("new_sum", new_sum)
                #print("difference", old_sum-new_sum)
                if signal_hists.get(histName) is None:
                    signal_hists[histName] = hist
                else:
                    signal_hists[histName].Add(hist)
            
            if required_category != "tracks":
                orthOpt = [True, False] if lep == "Muons" else [False]
                orth_cond = " && (leptons%%%[1].Pt() <= 3.5 || deltaR%%% <= 0.3)"
                for orth in orthOpt:
                    c1.cd()
                
                    histName = deltaM + "_2l_" + lep + ("_orth" if orth else "")
                    #drawString = "{:.2f}".format(analysis_selections.luminosities[wanted_year]*1000) + " * FastSimWeightPR31285To36122* passesUniversalSelection * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons%%% == 1 " + (orth_cond if orth else "") + " && MinDeltaPhiMhtJets > 0.4 && MET >= 140 && MHT >= 220 && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && leptonFlavour%%% == \"" + lep + "\" && sameSign%%% == 0 && isoCr%%% == 0 " + (mtautauveto if veto_tautau else "") + "  )"
                    #drawString = drawString.replace("%%%", analysis_selections.jetIsos[lep])
                
                
                    #print("\n\nhistName=" + histName)
                    #print("old drawString="+drawString)
                

                    #hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, "dilepBDT" + analysis_selections.jetIsos[lep], analysis_selections.binning["2l"][lep], drawString, False)
                    #hist.Sumw2()
                    #hist.Scale(lumi_weight_for_data)
                    #old_sum = hist.Integral()
                    #print("old number", old_sum)
                
                    conditions = analysis_selections.two_leptons_full_bdt_conditions_outside_mtautau_window
                    if orth:
                        conditions = analysis_selections.two_leptons_full_bdt_conditions_outside_mtautau_window_sos
                    drawString = analysis_selections.getFastSimString(wanted_year, lep, conditions)
                
                    observable = analysis_selections.dilepBDTString[wanted_year] + analysis_selections.jetIsos[lep]
                    
                    hist = None
                    if use_uniform_binning:
                        hist = utils.getHistogramFromTree(histName, c, observable, analysis_selections.uniform_binning_number, -1, 1, drawString, False)
                    else:
                        hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, observable, analysis_selections.binning["2l"][lep], drawString, False)
                    hist.Sumw2() 
                
                
                    #hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, "dilepBDT" + analysis_selections.jetIsos[lep], analysis_selections.binning["2l"][lep], drawString, False)
                    #hist.Sumw2() 

                    new_sum = hist.Integral()
                    print("\n\nnew sum", new_sum)
                    #print("difference", old_sum-new_sum)
                    #print("\n\n")
                
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
    
    if required_category != "tracks":
    
        print("Getting Mtautau BG...")
        bg_slim_files = glob(bg_dir + "/*")
        for filename in bg_slim_files:
            print("Opening", filename)
            f = TFile(filename)
            c = f.Get('tEvent')
        
            for lep in ["Muons", "Electrons"]:
        
                c1.cd()
                orthOpt = [True, False] if lep == "Muons" else [False]
                orth_cond = " && (leptons%%%[1].Pt() <= 3.5 || deltaR%%% <= 0.3)"
                for orth in orthOpt:
                    c1.cd()
                    print("2l",lep,orth)
                
                    #drawString = "{:.2f}".format(analysis_selections.luminosities[wanted_year]*1000) + " * passesUniversalSelection * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons%%% == 1 " + (orth_cond if orth else "") + " && MinDeltaPhiMhtJets > 0.4 && MET >= 140 && MHT >= 220 && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && leptonFlavour%%% == \"" + lep + "\" && sameSign%%% == 0 && isoCr%%% == 0 && tautau%%%" + (mtautauveto if veto_tautau else "") + " )"
                    #drawString = drawString.replace("%%%", analysis_selections.jetIsos[lep])
                    histName = "bg_2l_" + lep + ("_orth" if orth else "")
                    #hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, "dilepBDT" + analysis_selections.jetIsos[lep], analysis_selections.binning["2l"][lep], drawString, False)
                    #hist.Sumw2()
                    
                    #old_sum = hist.Integral()
                    #print("old number", old_sum)
                    
                    
                    conditions = analysis_selections.two_leptons_full_bdt_tautau_outside_mtautau_window_prediction
                    if orth:
                        conditions = analysis_selections.two_leptons_full_bdt_tautau_outside_mtautau_window_prediction_sos
                    drawString = analysis_selections.getFullSimString(wanted_year, lep, conditions)
                    
                    observable = analysis_selections.dilepBDTString[wanted_year] + analysis_selections.jetIsos[lep]
                    
                    hist = None
                    if use_uniform_binning:
                        hist = utils.getHistogramFromTree(histName, c, observable, analysis_selections.uniform_binning_number, -1, 1, drawString, False)
                    else:
                        hist = utils.getHistogramFromTreeCutsomBinsX(histName, c, observable, analysis_selections.binning["2l"][lep], drawString, False)
                    hist.Sumw2() 

                    new_sum = hist.Integral()
                    print("\n\nnew sum", new_sum)
                    #print("difference", old_sum-new_sum)
                    
                    
                    utils.scaleHistogram(hist, analysis_selections.tautau_factors[wanted_year][lep][0], analysis_selections.tautau_factors[wanted_year][lep][1])
                    if bg_2l_hist.get(histName) is None:
                        print("WTF!! histName", histName)
                        bg_2l_hist[histName] = hist
                    else:
                        bg_2l_hist[histName].Add(hist)
        
            f.Close()
    
    fnew.cd()
    
    for hist in signal_hists:
        signal_hists[hist].Write()
    for hist in bg_1t_hist:
        bg_1t_hist[hist].Write()
    for hist in bg_2l_hist:
        bg_2l_hist[hist].Write()
    
    fnew.Close()
    
    exit(0)
    
main()
