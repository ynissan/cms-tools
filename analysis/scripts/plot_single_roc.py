#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import os
import re

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib/classes"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib"))
import utils
import analysis_ntuples
import analysis_tools
import cut_optimisation

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Plot observealbes for tracks.')
parser.add_argument('-i', '--input', nargs=1, help='Input Range', required=False)
parser.add_argument('-m', '--method', nargs=1, help='Method', required=False)
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=True)
parser.add_argument('-w', '--weight', dest='weight', help='Plot With Weight', action='store_true')
args = parser.parse_args()


output_file = None
method = ""
weight = args.weight
input = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/cut_optimisation/tmva/dilepton_bdt/exTrackElectronsCorrJetIso10"
if args.output_file:
    output_file = args.output_file[0]
if args.input:
    input = args.input[0]
if args.method:
    method = args.method[0]

print "input", input
print "method", method
######## END OF CMDLINE ARGUMENTS ########

print "Running for input: " + input

def main():

    print "Plotting observable"
    c2 = TCanvas("c2")
    c1 = TCanvas("c1", "c1", 800, 800)
    c1.SetBottomMargin(0.16)
    c1.SetLeftMargin(0.16)
    #c1 = utils.mkcanvas()
    #memory = []
    
    global method
    
    file = [input]
    c2.cd()
    #(testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names) = cut_optimisation.get_bdt_hists(file, None, None, None, None, None, None, 40)
    (testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names) = cut_optimisation.get_method_hists(file, method, None, None, None, None, None, None, 40, "", weight)
    #cut_optimisation.get_mlp_hists(file, testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names)
    #def get_bdt_hists(folders, testBGHists=None, trainBGHists=None, testSignalHists=None, trainSignalHists=None, methods=None, names=None, bins=10000,  condition=""):
    #    return get_method_hists(folders, "BDT", testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names, bins, condition)

    c1.cd()
    
    c1.Print(output_file+"[");
    
    hist = TH1F("hroc", "", 1000, 0, 1)
    hist.SetMinimum(0)
    hist.SetMaximum(1)
    hist.GetXaxis().SetTitle("#font[12]{#epsilon_{S}}")
    hist.GetYaxis().SetTitle("background rejection (1 - #font[12]{#epsilon_{B}})")
    utils.histoStyler(hist)
    hist.GetYaxis().SetTitleOffset(1.20)
    hist.GetXaxis().SetLabelSize(0.055)
    hist.Draw()
    
    legend = TLegend(0.2, 0.2, 0.7, 0.45)
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.05)
    
    for inx in range(len(testBGHists)):
    
        testBGHist, trainBGHist, testSignalHist, trainSignalHist, method, name = testBGHists[inx], trainBGHists[inx], testSignalHists[inx], trainSignalHists[inx], methods[inx], names[inx]
        
        h = TGraph()
        highestZ, highestS, highestB, highestMVA, ST, BT = cut_optimisation.getHighestZ(trainSignalHist, trainBGHist, testSignalHist, testBGHist, h)
        h.SetTitle(name)
        h.SetLineColor(kBlack)
        h.SetMarkerSize(0.2)
        #hbdt.SetFillColor(kRed)

        h.Draw("same")
        legend.Draw("same")

    
    #legend.Draw("SAME")
    utils.stamp_plot()
    #utils.stampFab("35.9")
    c1.Print(output_file);
    c1.Print(output_file+"]");
    exit(0)

main()


