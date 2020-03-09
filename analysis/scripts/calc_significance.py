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
import numpy

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes"))
import utils
import analysis_ntuples

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
TH1D.SetDefaultSumw2()

gROOT.ProcessLine(open(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes/calcLlhdSingleCount.cc")).read())
exec('from ROOT import *')

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Plot skims for x1x2x1 process with BDTs.')
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
args = parser.parse_args()

output_file = None

if args.output_file:
    output_file = args.output_file[0]
else:
    output_file = "obs.pdf"

######## END OF CMDLINE ARGUMENTS ########

binsNumber = 30

sig_method = "rsb"
#sig_method = "Llhd"

histograms_defs = [    
    #NORMAL
    { "obs" : "invMass", "minX" : 0, "maxX" : 30, "bins" : 90, "units" : "GeV" },
    { "obs" : "trackBDT", "minX" : 0, "maxX" : 0.7, "bins" : 30 },
    { "obs" : "dilepBDT", "minX" : -0.2, "maxX" : 0.6, "bins" : 30 },
]

cuts = {
    "2l" : "deltaR <= 1.2  && leptons[0].Pt() < 15 && Ht >= 120 && leptons[1].Pt() <= 3 && deltaEta < 1 && mt1 <= 40 && mt2 <= 40 && dilepHt >= 170 && DeltaPhiLeadingJetDilepton >= 1.7",
    "1t1l" : "lepton.Pt() < 15 && Mht >=140 && mtl <= 60 && deltaR <= 1.7 && MinDeltaPhiMhtJets >= 1 && DeltaEtaLeadingJetDilepton <= 2.2 && DeltaPhiLeadingJetDilepton >= 1.8 && deltaPhi <= 1.3 && deltaEta <= 1.2 && LeadingJetPt >= 100 && mtt <= 50 && mt1 <= 60 && mt2 <= 50 && Ht >= 140 &&  MinDeltaPhiMetJets >= 1.3"
}

paths = {
    "1t1l" : "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1",
    "2l" : "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1"
}

def performScanForFile(file, type, maxSignalRange=None):
    scan = []
    basicCond = None
    if type == "2l":
        basicCond = str(utils.LUMINOSITY) + " * Weight * (leptons[1].Pt() <= 3 && Met >= 200 && invMass < 30 && dilepBDT >= "
    else:
        basicCond = str(utils.LUMINOSITY) + " * Weight * (Met >= 200 && invMass < 30 && dilepBDT >= "
    rootFile = TFile(file)
    c = rootFile.Get('tEvent')
    i = 0
    for dilepBDT in numpy.arange(-0.3, 0.6, 0.05):
        i += 1
        if maxSignalRange is not None and i > maxSignalRange:
            print "*** breaking scan because of signal"
            break
        cond = basicCond + "{:.2f}".format(dilepBDT) + ")"
        #print "cond=" + cond
        hist = utils.getHistogramFromTree("sig_" + "{:.2f}".format(dilepBDT), c, "invMass", binsNumber, 0, 15, cond, True)
        if not hist:
            print "WTF"
            exit(0)
        if hist.Integral() == 0:
            #print "Stopping at value", dilepBDT
            break
        scan.append(hist)
    return scan

def main():
    print "Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    # AFTER OOOOOOPPPPS! lhdH1 9.06252290502e-16 lhdH0 7.19943784186e-16 sigNum 32.349407196 bgNum 7768.57617188 bgError 4855.31444616 Z 0.678446169087
#     u = 100000.
#     lhdH0 = lhd(double N,double s,double B,double dB)
#     lhdH0 = lhd(7768.57617188,0,7768.57617188,4855.31444616)
#     print "Npx", lhdH0.GetNpx()
#     lhdH0.Draw()
#     line = TLine()
#     line.DrawLine(7768.576, 0, 7768.576, 100000)
#     line2 = TLine()
#     line2.DrawLine(7768.576 + 32, 0, 7768.576 + 32, 100000)
#     c1.SetLogy(True)
#     c1.Update()
#     
#     utils.pause()
#     print lhdH0
#     lhdH1 = lhd(7768.57617188,0.1 * 32.349407196,7768.57617188,4855.31444616)
#     c1.Update()
#     utils.pause()
#     print "Z", utils.calcZ(lhdH1, lhdH0), lhdH0, lhdH1
#     
#     
#     lhdH0 = lhd(u/10.,u/10.,u/10.,math.sqrt(u/10.))
#     print str(lhdH0)
#     lhdH1 = lhd(2*u/10.,u/10.,u/10.,math.sqrt(u/10.))
#     #print "Z2", calcZ(lhdH1, lhdH0)
#     print "Z3", calcZ(lhdH1**10, lhdH0**10)
#     
#     exit(0)
# 

    
    significance = {}
    for type in ["1t1l","2l"]:
        bgHistograms = {}
        signalHistograms = {}    
        bgHistograms[type] = {}
        signalHistograms[type] = {}
        significance[type] = {}
        for trainGroup in utils.trainGroupsOrder + ["all", "1t1l","2l"]:
            print "Checking train group " + trainGroup
        
            signalHistograms[type][trainGroup] = {}
        
            maxSignalRange = 0
        
            groups = None
            if trainGroup in ["all", "1t1l","2l"]:
                groups = [trainGroup]
            else:
                groups = utils.trainGroups[trainGroup]
        
            for group in groups:
                print "Checking group", group
                signalFilesPath = None
                if group in ["all", "1t1l","2l"]:
                    signalFilesPath = paths[type] + "/signal/skim_dilepton_signal_bdt_all/single/*"
                else:
                    signalFilesPath = paths[type] + "/signal/skim_dilepton_signal_bdt/single/*" + group + "*"
                signalFiles = glob(signalFilesPath)
                for signalFile in signalFiles:
                    signalFileName = os.path.basename(signalFile).split(".")[0]
                    print "Scanning file", signalFileName
                    if group in ["1t1l","2l"]:
                        if group != type:
                            continue
                        cond = str(utils.LUMINOSITY) + " * Weight * (Met >= 200 && invMass < 30 && " + cuts[group] + ")"
                        print "opening file", signalFile, "with cond ", cond
                        rootFile = TFile(signalFile)
                        c = rootFile.Get('tEvent')
                        hist = utils.getHistogramFromTree("sig_" + group, c, "invMass", binsNumber, 0, 15, cond, True)
                        signalHistograms[type][trainGroup][signalFileName] = hist
                    else:
                        signalHistograms[type][trainGroup][signalFileName] = performScanForFile(signalFile, type)
                        if len(signalHistograms[type][trainGroup][signalFileName]) > maxSignalRange:
                            maxSignalRange = len(signalHistograms[type][trainGroup][signalFileName])
        
            print "Maximum signal range for", trainGroup, " is", maxSignalRange
            bgFilesPath = None
            if trainGroup in ["all", "1t1l","2l"]:
                bgFilesPath = paths[type] + "/bg/skim_dilepton_signal_bdt_all/single/*"
            else:
                bgFilesPath = paths[type] + "/bg/skim_dilepton_signal_bdt/" + trainGroup + "/single/*"
            #print "Checking files", bgFilesPath
            print "bgFilesPath", bgFilesPath
            bgFiles = glob(bgFilesPath)
        
            for bgFile in bgFiles:
                print "Scanning", bgFile
                if trainGroup in ["1t1l","2l"]:
                    print ">>>>>>> trainGroup", trainGroup
                    if trainGroup != type:
                        print "Skipping trainGroup", trainGroup, "for type", type
                        continue
                    print "******* BG trainGroup", trainGroup
                    cond = str(utils.LUMINOSITY) + " * Weight * (Met >= 200 && invMass < 30 && " + cuts[group] + ")"
                    rootFile = TFile(bgFile)
                    c = rootFile.Get('tEvent')
                    hist = utils.getHistogramFromTree("bg_" + group, c, "invMass", binsNumber, 0, 15, cond, True)
                    if bgHistograms[type].get(trainGroup) is None:
                        bgHistograms[type][trainGroup] = hist
                    else:
                        bgHistograms[type][trainGroup].Add(hist)
                else:
                    scan = performScanForFile(bgFile, type, maxSignalRange)
                    if bgHistograms[type].get(trainGroup) is None:
                        bgHistograms[type][trainGroup] = scan
                    else:
                        for i in range(len(scan)):
                            if i >= len(bgHistograms[type][trainGroup]):
                                print "Expending scan"
                                bgHistograms[type][trainGroup].append(scan[i])
                            else:
                                bgHistograms[type][trainGroup][i].Add(scan[i])
            if bgHistograms[type].get(trainGroup) is None:
                print "bgHistograms not ready for", trainGroup
                continue
            bgScan = bgHistograms[type][trainGroup]
            for signalFileName in signalHistograms[type][trainGroup]:
                if trainGroup in ["1t1l","2l"]:
                    if trainGroup != type:
                        continue
                    sigHist = signalHistograms[type][trainGroup][signalFileName]
                    bgHist = bgHistograms[type][trainGroup]
                    sig = 0
                    if sig_method == "rsb":
                        sig = utils.calcSignificance(sigHist, bgHist)
                    else:
                        sig = utils.calcSignificanceLlhdSingleCount(sigHist, bgHist)
                    
                    #if sig > 0:
                    #    print "Greater!", sig, "for rect", signalFileName
                    if significance[type].get(trainGroup) is None:
                        significance[type][trainGroup] = {}
                    significance[type][trainGroup][signalFileName] = sig
                else:
                    #print "Calculating Significance for", signalFileName
                    sigScan = []
                    dilepBDT = -0.3
                    i = 0
                    for sigHist in signalHistograms[type][trainGroup][signalFileName]:
                        #print "dilepBDT=" + str(dilepBDT)
                        i += 1
                        dilepBDT += 0.05
                        if i > len(bgHistograms[type][trainGroup]):
                            print "Breaking scan at ", dilepBDT
                            break
                        bgHist = bgHistograms[type][trainGroup][i-1]
                        sig = 0
                        if sig_method == "rsb":
                            sig = utils.calcSignificance(sigHist, bgHist)
                        else:
                            sig = utils.calcSignificanceLlhdSingleCount(sigHist, bgHist)
                        #if sig > 0:
                        #    print "Greater!", sig, "for", type, signalFileName
                        sigScan.append(sig)
            
                    print "sigScan for", trainGroup, signalFileName, sigScan#, "min", min(sigScan)
                    if significance[type].get(trainGroup) is None:
                        significance[type][trainGroup] = {}
                    if len(sigScan) == 0:
                        significance[type][trainGroup][signalFileName] = 0
                    else:
                        if sig_method == "rsb":
                            significance[type][trainGroup][signalFileName] = max(sigScan)
                        else:
                            significance[type][trainGroup][signalFileName] = min(sigScan)
    
    print " "
    print " "
    print " "
    for trainGroup in significance["1t1l"]:
        if trainGroup in ["all", "1t1l","2l"]:
            continue
        for signalFileName in sorted(significance["1t1l"][trainGroup]):
            fileNameParts = signalFileName.split("_")
            mu = fileNameParts[1]
            dm = fileNameParts[2].split("Chi")[0]
            print mu, dm, "{:.2f}".format(significance["1t1l"][trainGroup][signalFileName]), "{:.2f}".format(significance["1t1l"]["all"][signalFileName]), "{:.2f}".format(significance["1t1l"]["1t1l"][signalFileName]), "{:.2f}".format(significance["2l"][trainGroup][signalFileName]), "{:.2f}".format(significance["2l"]["all"][signalFileName]), "{:.2f}".format(significance["2l"]["2l"][signalFileName]), "{:.2f}".format(math.sqrt((significance["1t1l"][trainGroup][signalFileName])**2 + (significance["2l"][trainGroup][signalFileName])**2)), "{:.2f}".format(math.sqrt((significance["2l"]["all"][signalFileName])**2 + (significance["1t1l"]["all"][signalFileName])**2)), "{:.2f}".format(math.sqrt((significance["2l"]["2l"][signalFileName])**2 + (significance["1t1l"]["1t1l"][signalFileName])**2))

    # c1 = TCanvas("c1", "c1", 800, 800)
#     c1.SetBottomMargin(0.16)
#     c1.SetLeftMargin(0.18)
#     c1.cd()
#     histPad = c1
#     histPad.Draw()
#     c1.Print("output.pdf[");
#     sigHist = signalHistograms["1t1l"]["low"]["higgsino_mu100_dm4p30Chi20Chipm"][10]
#     bgHist = bgHistograms["1t1l"]["low"][10]
#     utils.formatHist(bgHist, utils.signalCp[1], 0.8)
#     bgHist.Draw("hist")
#     sigHist.Draw("hist same")
#     c1.Print("output.pdf");
#     c1.Print("output.pdf]");
#     sig = utils.calcSignificance(sigHist, [bgHist])
#     print "sig=", sig
    
#     trainGroups = {
#     "dm0" : ["dm0p"],
#     "dm1" : ["dm1p"],
#     "low" : ["dm2p", "dm3p", "dm4p"],
#     "dm7" : ["dm7p"],
#     "dm9" : ["dm9p"],
#     "high" : ["dm12p", "dm13p"]
# }
# 
# trainGroupsOrder = ["dm0", "dm1", "low", "dm7", "dm9", "high"]
    
    print "End: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    exit(0)

main()


