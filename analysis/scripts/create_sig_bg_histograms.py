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

signal_1t_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_sam_dilepton_signal_bdt_all/single"
bg_1t_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dilepton_signal_bdt/all/single"

signal_2l_dir = "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1/signal/skim_sam_dilepton_signal_bdt_all/single"
bg_2l_dir = "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1/bg/skim_dilepton_signal_bdt/all/single"

if args.output_file:
    output_file = args.output_file[0]
else:
    output_file = "histograms.root"

######## END OF CMDLINE ARGUMENTS ########


def createPlotsFast(rootfiles, type, histograms, weight=1, prefix=""):
    print "Processing "
    print rootfiles
    lumiSecs = LumiSectMap()
    
    for f in rootfiles:
        print f
        rootFile = TFile(f)
        c = rootFile.Get('tEvent')
        if type == "data":
            lumis = rootFile.Get('lumiSecs')
            col = TList()
            col.Add(lumis)
            lumiSecs.Merge(col)
        
        for cut in cuts:
            for hist_def in histograms_defs:
                if prefix != "":
                    histName =  prefix + "_" + cut["name"] + "_" + hist_def["obs"] + "_" + type
                else:
                    histName =  cut["name"] + "_" + hist_def["obs"] + "_" + type
                #if type != "data" and type != "signal":
                #    hist = utils.getHistogramFromTree(histName, c, hist_def["obs"], hist_def["bins"], hist_def["minX"], hist_def["maxX"], "puWeight * (" + cut["condition"] + ")")
                #else:
                if type != "data":
                    hist = utils.getHistogramFromTree(histName, c, hist_def["obs"], hist_def["bins"], hist_def["minX"], hist_def["maxX"], weightString[plot_kind] + " * " + str(weight) + "* Weight * (" + cut["condition"] + ")", plot_overflow)
                else:
                    hist = utils.getHistogramFromTree(histName, c, hist_def["obs"], hist_def["bins"], hist_def["minX"], hist_def["maxX"], weightString[plot_kind] + " * (" +cut["condition"] + ")", plot_overflow)
                if hist is None:
                    continue
                hist.GetXaxis().SetTitle("")
                hist.SetTitle("")
                hist.Sumw2()
                #if type != "data":
                #    c.GetEntry(0)
                #    hist.Scale(c.Weight * weight)
                if histograms.get(histName) is None:
                    histograms[histName] = hist
                else:
                    histograms[histName].Add(hist)
        
        rootFile.Close()
    
    if type == "data":
        return calculatedLumi.get(plot_kind)
        #return calculatedLumi.get('SingleMuon')
        
        if calculatedLumi.get('MET') is not None:
            print "Found lumi=" + str(calculatedLumi['MET'])
            return calculatedLumi['MET']
        else:
            return utils.calculateLumiFromLumiSecs(lumiSecs)
        #Z PEAK
        #return 27.677786572
        #Norman
        return 35.579533154
        #return utils.calculateLumiFromLumiSecs(lumiSecs)

def main():
    print "Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    fnew = TFile(output_file,'recreate')
    c1 = TCanvas("c1", "c1", 800, 800)
    c1.cd()
    
    print "Getting 1t signals..."
    
    for filename in glob(signal_1t_dir + "/*"):
        print "Opening", filename    
        deltaM = utils.getPointFromSamFileName(filename)
        print "deltaM=" + deltaM
        f = TFile(filename)
        c = f.Get('tEvent')
        c1.cd()
        hist = utils.getHistogramFromTree(deltaM + "_1t", c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 *  Weight * BranchingRatio * (Mht >= 220 && Met >= 200 && invMass < 30)", True)
        hist.Sumw2()
        fnew.cd()
        hist.Write()
        f.Close()
    
    bg_1t_hist = None
    
    print "Getting 1t BG..."
    
    for filename in glob(bg_1t_dir + "/*"):
        print "Opening", filename
        f = TFile(filename)
        c = f.Get('tEvent')
        c1.cd()
        basename = os.path.basename(filename).split(".")[0]
        hist = utils.getHistogramFromTree(basename, c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * (Mht >= 220 && Met >= 200 && invMass < 30)", True)
        hist.Sumw2()
        if bg_1t_hist is None:
            bg_1t_hist = hist
        else:
            bg_1t_hist.Add(hist)
        f.Close()
    
    fnew.cd()
    bg_1t_hist.Write("bg_1t")
    
    print "Getting 2l signals..."
    
    for filename in glob(signal_2l_dir + "/*"):
        print "Opening", filename   
        deltaM = utils.getPointFromSamFileName(filename)
        print "deltaM=" + deltaM
        f = TFile(filename)
        c = f.Get('tEvent')
        c1.cd()
        hist = utils.getHistogramFromTree(deltaM + "_2l", c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * ((leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && Mht >= 220 &&  Met >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1)", True)
        hist.Sumw2()
        fnew.cd()
        hist.Write()
        f.Close()
    
    bg_2l_hist = None
    
    print "Getting 2l BG..."
    
    for filename in glob(bg_2l_dir + "/*"):
        print "Opening", filename
        f = TFile(filename)
        c = f.Get('tEvent')
        c1.cd()
        basename = os.path.basename(filename).split(".")[0]
        hist = utils.getHistogramFromTree(basename, c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * ((leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && Mht >= 220 &&  Met >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1)", True)
        hist.Sumw2()
        if bg_2l_hist is None:
            bg_2l_hist = hist
        else:
            bg_2l_hist.Add(hist)
        f.Close()
    
    fnew.cd()
    bg_2l_hist.Write("bg_2l")
    fnew.Close()
    
    exit(0)

main()


