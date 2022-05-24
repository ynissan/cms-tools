#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import os
import re
from datetime import datetime
import cppyy
from ctypes import *

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib/classes"))
import utils

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

signals = [
    #"mu100_dm4p30",
    "mu100_dm3p28",
    #"mu100_dm2p51",
    #"mu100_dm1p47",
    #"mu100_dm1p13"
]

wanted_lepton = "Electrons"

def main():
    print "Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    histogram_file = TFile("sig_bg_histograms_for_jet_iso_scan.root", "read")
    
    significance = {}
    signal_count = {}
    signal_count_cr = {}
    bg_count = {}
    bg_count_cr = {}
    bg_transfer_factor_histogram = {}
    bg_sc_transfer_factor_histogram = {}
    transfer_factor = {}
    transfer_factor_error = {}
    
    
    for lep in ["Muons", "Electrons"]:
        
        if lep != wanted_lepton:
            continue
        
        if significance.get(lep) is None:
            significance[lep] = {}
            signal_count[lep] = {}
            signal_count_cr[lep] = {}
            bg_count[lep] = {}
            bg_count_cr[lep] = {}
            bg_transfer_factor_histogram[lep] = {}
            bg_sc_transfer_factor_histogram[lep] = {}
            transfer_factor[lep] = {}
            transfer_factor_error[lep] = {}
        
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
                        
                        if significance[lep].get(jetiso) is None:
                            significance[lep][jetiso] = {}
                            signal_count[lep][jetiso] = {}
                            signal_count_cr[lep][jetiso] = {}
                            bg_count[lep][jetiso] = {}
                            bg_count_cr[lep][jetiso] = {}
                            bg_transfer_factor_histogram[lep][jetiso] = {}
                            bg_sc_transfer_factor_histogram[lep][jetiso] = {}
                            transfer_factor[lep][jetiso] = {}
                            transfer_factor_error[lep][jetiso] = {}
                        
                        orthOpt = [True, False] if lep == "Muons" else [False]
                        isoCrs = [True, False] if iso == "CorrJetIso" else [False]
                        isoCr = False
                        
                        for orth in orthOpt:
                            orthStr = "orth" if orth else "non-orth"
                            if significance[lep][jetiso].get(orthStr) is None:
                                significance[lep][jetiso][orthStr] = {}
                                signal_count[lep][jetiso][orthStr] = {}
                                signal_count_cr[lep][jetiso][orthStr] = {}
                                bg_transfer_factor_histogram[lep][jetiso][orthStr] = {}
                                bg_sc_transfer_factor_histogram[lep][jetiso][orthStr] = {}
                                transfer_factor[lep][jetiso][orthStr] = {}
                                transfer_factor_error[lep][jetiso][orthStr] = {}
                                #bg_count[lep][jetiso][orthStr] = {}
                            
                            bg_hist_name = "bg_2l_" + ("orth_" if orth else "") + lep + "_" + jetiso
                            bg_hist_name_cr = "bg_2l_" + ("orth_" if orth else "") + lep + "_" + jetiso + "_isoCr"
                            print "Getting", bg_hist_name
                            bg_hist = histogram_file.Get(bg_hist_name)#.Rebin(5)
                            if iso == "CorrJetIso":
                                print "Getting", bg_hist_name_cr
                                bg_hist_cr = histogram_file.Get(bg_hist_name_cr)
                                intError  = c_double()
                                bg_count_cr[lep][jetiso][orthStr] = bg_hist_cr.IntegralAndError(bg_hist_cr.FindBin(-1), bg_hist_cr.FindBin(0),intError)
                                bg_sc_transfer_factor_histogram[lep][jetiso][orthStr] = TH1F(bg_hist_name_cr + "_bg_transfer_factor_histogram", "", 1, 0, 1)
                                bg_sc_transfer_factor_histogram[lep][jetiso][orthStr].Sumw2()
                                bg_sc_transfer_factor_histogram[lep][jetiso][orthStr].SetBinContent(1,bg_count_cr[lep][jetiso][orthStr])
                                bg_sc_transfer_factor_histogram[lep][jetiso][orthStr].SetBinError(1,intError)
                            else:
                                print("What?")
                            intError  = c_double()
                            bg_count[lep][jetiso][orthStr] = bg_hist.IntegralAndError(bg_hist.FindBin(-1), bg_hist.FindBin(0), intError)
                            bg_transfer_factor_histogram[lep][jetiso][orthStr] = TH1F(bg_hist_name + "_bg_transfer_factor_histogram", "", 1, 0, 1)
                            bg_transfer_factor_histogram[lep][jetiso][orthStr].Sumw2()
                            bg_transfer_factor_histogram[lep][jetiso][orthStr].SetBinContent(1,bg_count[lep][jetiso][orthStr])
                            bg_transfer_factor_histogram[lep][jetiso][orthStr].SetBinError(1,intError)
                            if iso == "CorrJetIso":
                                print("Going to divide",bg_sc_transfer_factor_histogram[lep][jetiso][orthStr])
                                bg_transfer_factor_histogram[lep][jetiso][orthStr].Divide(bg_sc_transfer_factor_histogram[lep][jetiso][orthStr])
                           
                            for signal in signals:
                                sig_hist_name = signal + "_2l_" + ("orth_" if orth else "") + lep + "_" + jetiso
                                sig_hist = histogram_file.Get(sig_hist_name)#.Rebin(5)
                                print "Getting", sig_hist
                                sig_hist_name_cr = signal + "_2l_" + ("orth_" if orth else "") + lep + "_" + jetiso + "_isoCr"
                                sig_hist_cr = histogram_file.Get(sig_hist_name_cr)#.Rebin(5)
                                print "Getting", sig_hist_cr
                                
                                signal_count[lep][jetiso][orthStr][signal] = sig_hist.Integral(sig_hist.FindBin(0), sig_hist.FindBin(1))
                                if iso == "CorrJetIso":
                                    signal_count_cr[lep][jetiso][orthStr][signal] = sig_hist_cr.Integral(sig_hist_cr.FindBin(0), sig_hist_cr.FindBin(1))
                               
                                #significance[lep][jetiso][orthStr][signal] = utils.calcSignificanceNoAcc(sig_hist, bg_hist, True)
                                
                                
                                if iso != "CorrJetIso":
                                    continue
                                
                                newSigHist = sig_hist.Rebin(5,"newSigHist")
                                newBgHist = bg_hist_cr.Rebin(5,"newBgHist")
                                transferFactor = bg_transfer_factor_histogram[lep][jetiso][orthStr].GetBinContent(1)
                                transferFactorError = bg_transfer_factor_histogram[lep][jetiso][orthStr].GetBinError(1)
                                significance[lep][jetiso][orthStr][signal] = utils.calcSignificanceTransferFactor(newSigHist, newBgHist, transferFactor, transferFactorError)
                                
                            #for isoCr in isoCrs:
                                
                                #hist = utils.getHistogramFromTree(deltaM + "_2l_" + ("orth_" if orth else "") + lep + "_" + jetiso + ("_isoCr" if isoCr else ""), c, "dilepBDT" + jetiso, bins, -1, 1, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons" + jetiso + " == 1 " + (orth_cond if orth else "") + " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && invMass" + jetiso + " < 12  && invMass" + jetiso + " > 0.4 && !(invMass" + jetiso + " > 3 && invMass" + jetiso + " < 3.2) && !(invMass" + jetiso + " > 0.75 && invMass" + jetiso + " < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && sameSign" + jetiso + " == 0 " + (("&& isoCr" + jetiso + (" >= 1" if isoCr else " == 0")) if len(cuts) > 0 else "") + ")", True)
                                    
                                    
    #fitHist.Integral(fitHist.FindBin(3.0), fitHist.FindBin(3.2))
    
    orthStr = "non-orth"
    signal = "mu100_dm3p28"
    #signal = "mu100_dm1p47"
    
    print significance
    print "=============================================\n\n\n\n"
    print "Significance"
    print "pt/dr," + ",".join([str(dr) for dr in utils.leptonCorrJetIsoDrCuts])
    for lep in ["Muons", "Electrons"]:
        if lep != wanted_lepton:
            continue
        for iso in utils.leptonIsolationList:
            if iso != "CorrJetIso":
                continue
            for cat in utils.leptonIsolationCategories:
                ptRanges = [""]
                drCuts = [""]
                if iso == "CorrJetIso":
                    ptRanges = utils.leptonCorrJetIsoPtRange
                    drCuts = utils.leptonCorrJetIsoDrCuts
                for ptRange in ptRanges:
                    pt_dr_sig = [str(ptRange)]
                    for drCut in drCuts:
                        cuts = ""
                        if len(str(ptRange)) > 0:
                            cuts = str(ptRange) + "Dr" + str(drCut)
                        jetiso = iso + cuts + cat
                        pt_dr_sig.append("{:.2f}".format(significance[lep][jetiso][orthStr][signal]))
                    print ",".join(pt_dr_sig)
    print "\n\n\n\n"
    print "Signal Efficiency"
    print "pt/dr," + ",".join([str(dr) for dr in utils.leptonCorrJetIsoDrCuts])
    for lep in ["Muons", "Electrons"]:
        if lep != wanted_lepton:
            continue
        for iso in utils.leptonIsolationList:
            if iso != "CorrJetIso":
                continue
            for cat in utils.leptonIsolationCategories:
                ptRanges = [""]
                drCuts = [""]
                if iso == "CorrJetIso":
                    ptRanges = utils.leptonCorrJetIsoPtRange
                    drCuts = utils.leptonCorrJetIsoDrCuts
                for ptRange in ptRanges:
                    pt_dr_sig = [str(ptRange)]
                    for drCut in drCuts:
                        cuts = ""
                        if len(str(ptRange)) > 0:
                            cuts = str(ptRange) + "Dr" + str(drCut)
                        jetiso = iso + cuts + cat
                        pt_dr_sig.append("{:.2f}".format(signal_count[lep][jetiso][orthStr][signal]/signal_count[lep]["NoIso"][orthStr][signal]))
                    print ",".join(pt_dr_sig)
    print "\n\n\n\n"
    
    print "Background Efficiency"
    print "pt/dr," + ",".join([str(dr) for dr in utils.leptonCorrJetIsoDrCuts])
    for lep in ["Muons", "Electrons"]:
        if lep != wanted_lepton:
            continue
        for iso in utils.leptonIsolationList:
            if iso != "CorrJetIso":
                continue
            for cat in utils.leptonIsolationCategories:
                ptRanges = [""]
                drCuts = [""]
                if iso == "CorrJetIso":
                    ptRanges = utils.leptonCorrJetIsoPtRange
                    drCuts = utils.leptonCorrJetIsoDrCuts
                for ptRange in ptRanges:
                    pt_dr_sig = [str(ptRange)]
                    for drCut in drCuts:
                        cuts = ""
                        if len(str(ptRange)) > 0:
                            cuts = str(ptRange) + "Dr" + str(drCut)
                        jetiso = iso + cuts + cat
                        pt_dr_sig.append("{:.2f}".format(bg_count[lep][jetiso][orthStr]/bg_count[lep]["NoIso"][orthStr]))
                    print ",".join(pt_dr_sig)
    print "\n\n\n\n"
    
    
    print "Background CR Ratio"
    print "pt/dr," + ",".join([str(dr) for dr in utils.leptonCorrJetIsoDrCuts])
    for lep in ["Muons", "Electrons"]:
        if lep != wanted_lepton:
            continue
        for iso in utils.leptonIsolationList:
            if iso != "CorrJetIso":
                continue
            for cat in utils.leptonIsolationCategories:
                ptRanges = [""]
                drCuts = [""]
                if iso == "CorrJetIso":
                    ptRanges = utils.leptonCorrJetIsoPtRange
                    drCuts = utils.leptonCorrJetIsoDrCuts
                for ptRange in ptRanges:
                    pt_dr_sig = [str(ptRange)]
                    for drCut in drCuts:
                        cuts = ""
                        if len(str(ptRange)) > 0:
                            cuts = str(ptRange) + "Dr" + str(drCut)
                        jetiso = iso + cuts + cat
                        pt_dr_sig.append("{:.2f}".format(bg_count_cr[lep][jetiso][orthStr]/bg_count[lep][jetiso][orthStr]))
                    print ",".join(pt_dr_sig)
    print "\n\n\n\n"
    
    print "Signal Contamination"
    print "pt/dr," + ",".join([str(dr) for dr in utils.leptonCorrJetIsoDrCuts])
    for lep in ["Muons", "Electrons"]:
        if lep != wanted_lepton:
            continue
        for iso in utils.leptonIsolationList:
            if iso != "CorrJetIso":
                continue
            for cat in utils.leptonIsolationCategories:
                ptRanges = [""]
                drCuts = [""]
                if iso == "CorrJetIso":
                    ptRanges = utils.leptonCorrJetIsoPtRange
                    drCuts = utils.leptonCorrJetIsoDrCuts
                for ptRange in ptRanges:
                    pt_dr_sig = [str(ptRange)]
                    for drCut in drCuts:
                        cuts = ""
                        if len(str(ptRange)) > 0:
                            cuts = str(ptRange) + "Dr" + str(drCut)
                        jetiso = iso + cuts + cat
                        pt_dr_sig.append("{:.2f}".format(signal_count_cr[lep][jetiso][orthStr][signal]/bg_count[lep][jetiso][orthStr]))
                    print ",".join(pt_dr_sig)
    print "\n\n\n\n"
    
    print "Signal CR to SR ratio"
    print "pt/dr," + ",".join([str(dr) for dr in utils.leptonCorrJetIsoDrCuts])
    for lep in ["Muons", "Electrons"]:
        if lep != wanted_lepton:
            continue
        for iso in utils.leptonIsolationList:
            if iso != "CorrJetIso":
                continue
            for cat in utils.leptonIsolationCategories:
                ptRanges = [""]
                drCuts = [""]
                if iso == "CorrJetIso":
                    ptRanges = utils.leptonCorrJetIsoPtRange
                    drCuts = utils.leptonCorrJetIsoDrCuts
                for ptRange in ptRanges:
                    pt_dr_sig = [str(ptRange)]
                    for drCut in drCuts:
                        cuts = ""
                        if len(str(ptRange)) > 0:
                            cuts = str(ptRange) + "Dr" + str(drCut)
                        jetiso = iso + cuts + cat
                        pt_dr_sig.append("{:.2f}".format(signal_count_cr[lep][jetiso][orthStr][signal]/signal_count[lep][jetiso][orthStr][signal]))
                    print ",".join(pt_dr_sig)
    print "\n\n\n\n"
    
    
    print "Transfer Factor"
    print "pt/dr," + ",".join([str(dr) for dr in utils.leptonCorrJetIsoDrCuts])
    for lep in ["Muons", "Electrons"]:
        if lep != wanted_lepton:
            continue
        for iso in utils.leptonIsolationList:
            if iso != "CorrJetIso":
                continue
            for cat in utils.leptonIsolationCategories:
                ptRanges = [""]
                drCuts = [""]
                if iso == "CorrJetIso":
                    ptRanges = utils.leptonCorrJetIsoPtRange
                    drCuts = utils.leptonCorrJetIsoDrCuts
                for ptRange in ptRanges:
                    pt_dr_sig = [str(ptRange)]
                    for drCut in drCuts:
                        cuts = ""
                        if len(str(ptRange)) > 0:
                            cuts = str(ptRange) + "Dr" + str(drCut)
                        jetiso = iso + cuts + cat
                        
                        pt_dr_sig.append("{:.2f}".format(bg_transfer_factor_histogram[lep][jetiso][orthStr].GetBinContent(1)))
                    print ",".join(pt_dr_sig)
    print "\n\n\n\n"
    
    print "Transfer Factor Error"
    print "pt/dr," + ",".join([str(dr) for dr in utils.leptonCorrJetIsoDrCuts])
    for lep in ["Muons", "Electrons"]:
        if lep != wanted_lepton:
            continue
        for iso in utils.leptonIsolationList:
            if iso != "CorrJetIso":
                continue
            for cat in utils.leptonIsolationCategories:
                ptRanges = [""]
                drCuts = [""]
                if iso == "CorrJetIso":
                    ptRanges = utils.leptonCorrJetIsoPtRange
                    drCuts = utils.leptonCorrJetIsoDrCuts
                for ptRange in ptRanges:
                    pt_dr_sig = [str(ptRange)]
                    for drCut in drCuts:
                        cuts = ""
                        if len(str(ptRange)) > 0:
                            cuts = str(ptRange) + "Dr" + str(drCut)
                        jetiso = iso + cuts + cat
                        
                        pt_dr_sig.append("{:.2f}".format(bg_transfer_factor_histogram[lep][jetiso][orthStr].GetBinError(1)))
                    print ",".join(pt_dr_sig)
    print "\n\n\n\n"
    
    
    histogram_file.Close()
    
    print "\n\n\nEnd: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    exit(0)
main()
exit(0)