#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import os
import re
from datetime import datetime

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes"))
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

def main():
    print "Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    histogram_file = TFile("sig_bg_histograms_for_jet_iso_scan.root", "read")
    
    significance = {}
    signal_count = {}
    signal_count_cr = {}
    bg_count = {}
    bg_count_cr = {}
    
    for lep in ["Muons", "Electrons"]:
        
        if lep == "Electrons":
            continue
        
        if significance.get(lep) is None:
            significance[lep] = {}
            signal_count[lep] = {}
            signal_count_cr[lep] = {}
            bg_count[lep] = {}
            bg_count_cr[lep] = {}
        
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
                        
                        orthOpt = [True, False] if lep == "Muons" else [False]
                        isoCrs = [True, False] if iso == "CorrJetIso" else [False]
                        isoCr = False
                        
                        for orth in orthOpt:
                            orthStr = "orth" if orth else "non-orth"
                            if significance[lep][jetiso].get(orthStr) is None:
                                significance[lep][jetiso][orthStr] = {}
                                signal_count[lep][jetiso][orthStr] = {}
                                signal_count_cr[lep][jetiso][orthStr] = {}
                                #bg_count[lep][jetiso][orthStr] = {}
                            
                            bg_hist_name = "bg_2l_" + ("orth_" if orth else "") + lep + "_" + jetiso
                            bg_hist_name_cr = "bg_2l_" + ("orth_" if orth else "") + lep + "_" + jetiso + "_isoCr"
                            print "Getting", bg_hist_name
                            bg_hist = histogram_file.Get(bg_hist_name)#.Rebin(5)
                            if iso == "CorrJetIso":
                                print "Getting", bg_hist_name_cr
                                bg_hist_cr = histogram_file.Get(bg_hist_name_cr)
                                bg_count_cr[lep][jetiso][orthStr] = bg_hist_cr.Integral(bg_hist_cr.FindBin(0), bg_hist_cr.FindBin(1))
                            bg_count[lep][jetiso][orthStr] = bg_hist.Integral(bg_hist.FindBin(0), bg_hist.FindBin(1))
                            for signal in signals:
                                sig_hist_name = signal + "_2l_" + ("orth_" if orth else "") + lep + "_" + jetiso
                                sig_hist = histogram_file.Get(sig_hist_name)#.Rebin(5)
                                print "Getting", sig_hist
                                sig_hist_name_cr = signal + "_2l_" + ("orth_" if orth else "") + lep + "_" + jetiso + "_isoCr"
                                sig_hist_cr = histogram_file.Get(sig_hist_name_cr)#.Rebin(5)
                                print "Getting", sig_hist_cr
                                
                                significance[lep][jetiso][orthStr][signal] = utils.calcSignificanceNoAcc(sig_hist, bg_hist, True)
                                signal_count[lep][jetiso][orthStr][signal] = sig_hist.Integral(sig_hist.FindBin(0), sig_hist.FindBin(1))
                                if iso == "CorrJetIso":
                                    signal_count_cr[lep][jetiso][orthStr][signal] = sig_hist_cr.Integral(sig_hist_cr.FindBin(0), sig_hist_cr.FindBin(1))
                                
                            #for isoCr in isoCrs:
                                
                                #hist = utils.getHistogramFromTree(deltaM + "_2l_" + ("orth_" if orth else "") + lep + "_" + jetiso + ("_isoCr" if isoCr else ""), c, "dilepBDT" + jetiso, bins, -1, 1, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons" + jetiso + " == 1 " + (orth_cond if orth else "") + " && MinDeltaPhiMetJets > 0.4 && MET >= 140 && MHT >= 220 && invMass" + jetiso + " < 12  && invMass" + jetiso + " > 0.4 && !(invMass" + jetiso + " > 3 && invMass" + jetiso + " < 3.2) && !(invMass" + jetiso + " > 0.75 && invMass" + jetiso + " < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && sameSign" + jetiso + " == 0 " + (("&& isoCr" + jetiso + (" >= 1" if isoCr else " == 0")) if len(cuts) > 0 else "") + ")", True)
                                    
                                    
    #fitHist.Integral(fitHist.FindBin(3.0), fitHist.FindBin(3.2))
    
    orthStr = "non-orth"
    signal = "mu100_dm3p28"
    
    print significance
    print "=============================================\n\n\n\n"
    print "Significance"
    print "pt/dr," + ",".join([str(dr) for dr in utils.leptonCorrJetIsoDrCuts])
    for lep in ["Muons", "Electrons"]:
        if lep == "Electrons":
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
        if lep == "Electrons":
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
        if lep == "Electrons":
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
        if lep == "Electrons":
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
        if lep == "Electrons":
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
        if lep == "Electrons":
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
    
    
    
    histogram_file.Close()
    
    print "\n\n\nEnd: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    exit(0)
main()
exit(0)