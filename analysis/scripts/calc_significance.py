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

histograms_defs = [    
    #NORMAL
    { "obs" : "invMass", "minX" : 0, "maxX" : 30, "bins" : 90, "units" : "GeV" },
    { "obs" : "trackBDT", "minX" : 0, "maxX" : 0.7, "bins" : 30 },
    { "obs" : "dilepBDT", "minX" : -0.2, "maxX" : 0.6, "bins" : 30 },
]

cuts = [
    #{"name":"MET", "title": "MET", "condition" : "Met >= 250 && invMass < 30"},
    {"name":"dilepBDT", "title": "dilepBDT", "condition" : "Met >= 200 && dilepBDT > -0.3 && invMass < 30"}
]

paths = {
    "1t1l" : "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1",
    "2l" : "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1"
}

def performScanForFile(file, maxSignalRange=None):
    scan = []
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
        hist = utils.getHistogramFromTree("sig_" + "{:.2f}".format(dilepBDT), c, "invMass", binsNumber, 0, 30, cond, True)
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
    
    bgHistograms = {}
    signalHistograms = {}    
    significance = {}

    for type in ["1t1l","2l"]:
        bgHistograms[type] = {}
        signalHistograms[type] = {}
        significance[type] = {}
        for trainGroup in utils.trainGroupsOrder + ["all"]:
            print "Checking train group " + trainGroup
        
            signalHistograms[type][trainGroup] = {}
        
            maxSignalRange = 0
        
            groups = None
            if trainGroup == "all":
                groups = ["all"]
            else:
                groups = utils.trainGroups[trainGroup]
        
        
            for group in groups:
                print "Checking group", group
                signalFilesPath = None
                if group == "all":
                    signalFilesPath = paths[type] + "/signal/skim_dilepton_signal_bdt_all/single/*"
                else:
                    signalFilesPath = paths[type] + "/signal/skim_dilepton_signal_bdt/single/*" + group + "*"
                signalFiles = glob(signalFilesPath)
                for signalFile in signalFiles:
                    signalFileName = os.path.basename(signalFile).split(".")[0]
                    print "Scanning file", signalFileName
                    signalHistograms[type][trainGroup][signalFileName] = performScanForFile(signalFile)
                    if len(signalHistograms[type][trainGroup][signalFileName]) > maxSignalRange:
                        maxSignalRange = len(signalHistograms[type][trainGroup][signalFileName])
        
            print "Maximum signal range for", trainGroup, " is", maxSignalRange
            bgFilesPath = None
            if trainGroup == "all":
                bgFilesPath = paths[type] + "/bg/skim_dilepton_signal_bdt_all/single/*"
            else:
                bgFilesPath = paths[type] + "/bg/skim_dilepton_signal_bdt/" + trainGroup + "/single/*"
            #print "Checking files", bgFilesPath
            print "bgFilesPath", bgFilesPath
            bgFiles = glob(bgFilesPath)
        
            for bgFile in bgFiles:
                print "Scanning", bgFile
                scan = performScanForFile(bgFile, maxSignalRange)
                if bgHistograms[type].get(trainGroup) is None:
                    bgHistograms[type][trainGroup] = scan
                else:
                    for i in range(len(scan)):
                        if i >= len(bgHistograms[type][trainGroup]):
                            print "Expending scan"
                            bgHistograms[type][trainGroup].append(scan[i])
                        else:
                            bgHistograms[type][trainGroup][i].Add(scan[i])
        
        for trainGroup in utils.trainGroupsOrder + ["all"]:
            bgScan = bgHistograms[type][trainGroup]
            for signalFileName in signalHistograms[type][trainGroup]:
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
                    sigNum = 0
                    bgNum = 0
                    accumulate = False
                    for bin in range(1, binsNumber + 1):
                        if accumulate:
                            sigNum += sigHist.GetBinContent(bin)
                            bgNum += bgHist.GetBinContent(bin)
                        else:
                            sigNum = sigHist.GetBinContent(bin)
                            bgNum = bgHist.GetBinContent(bin)
                        if bgNum == 0:
                            accumulate = True
                        else:
                            accumulate = False
                            if bin <= binsNumber and bgHist.Integral(bin+1, binsNumber) == 0:
                                sigNum += sigHist.Integral(bin, binsNumber)
                                sig += 0.1 * sigNum / math.sqrt(bgNum)
                                break
                            else:
                                sig += 0.1 * sigNum / math.sqrt(bgNum)
                    sigScan.append(sig)
            
                print "sigScan for", trainGroup, signalFileName, sigScan, "max", max(sigScan)
                if significance[type].get(trainGroup) is None:
                    significance[type][trainGroup] = {}
                significance[type][trainGroup][signalFileName] = max(sigScan)
    
    print " "
    print " "
    print " "
    for trainGroup in significance["1t1l"]:
        if trainGroup == "all":
            continue
        for signalFileName in sorted(significance["1t1l"][trainGroup]):
            fileNameParts = signalFileName.split("_")
            mu = fileNameParts[1]
            dm = fileNameParts[2].split("Chi")[0]
            print mu, dm, "{:.2f}".format(significance["1t1l"][trainGroup][signalFileName]), "{:.2f}".format(significance["1t1l"]["all"][signalFileName]), "{:.2f}".format(significance["2l"][trainGroup][signalFileName]), "{:.2f}".format(significance["2l"]["all"][signalFileName]), "{:.2f}".format(significance["1t1l"][trainGroup][signalFileName] + significance["2l"][trainGroup][signalFileName]), "{:.2f}".format(significance["2l"]["all"][signalFileName] + significance["1t1l"]["all"][signalFileName])

    
    
    
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


