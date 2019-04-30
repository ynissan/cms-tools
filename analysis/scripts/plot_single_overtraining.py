#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import os
import re

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools/lib")
import utils
import analysis_ntuples
import analysis_tools
import cut_optimisation

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Plot observealbes for tracks.')
parser.add_argument('-i', '--input', nargs=1, help='Input Range', required=False)
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=True)
args = parser.parse_args()


output_file = None
input = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/cut_optimisation/tmva/dilepton_bdt/high"
if args.output_file:
    output_file = args.output_file[0]
if args.input:
    input = args.input[0]
######## END OF CMDLINE ARGUMENTS ########

print "Running for input: " + input

def main():

    print "Plotting observable"
    c2 = TCanvas("c2")
    c1 = TCanvas("c1", "c1", 800, 800)
    c1.SetBottomMargin(0.16)
    c1.SetLeftMargin(0.18)
    #c1 = utils.mkcanvas()
    #memory = []
    
    
    file = [input]
    c2.cd()
    (testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names) = cut_optimisation.get_bdt_hists(file, None, None, None, None, None, None, 40)
    #cut_optimisation.get_mlp_hists(file, testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names)
    c1.cd()
    
    c1.Print(output_file+"[");
    
    legend = TLegend(0.65, 0.70, 0.87, 0.875)
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.05)
    
    for inx in range(len(testBGHists)):
    
        testBGHist, trainBGHist, testSignalHist, trainSignalHist, method, name = testBGHists[inx], trainBGHists[inx], testSignalHists[inx], trainSignalHists[inx], methods[inx], names[inx]
        
        ST = trainSignalHist.Integral() + testSignalHist.Integral()
        BT = trainBGHist.Integral() + testBGHist.Integral()

        #trainSignalHist.Scale(1./ST)
        #testSignalHist.Scale(1./ST)
        #testBGHist.Scale(1./BT)
        #trainBGHist.Scale(1./BT)
        maxY = max(trainSignalHist.GetMaximum(), testSignalHist.GetMaximum(), testBGHist.GetMaximum(), trainBGHist.GetMaximum())
        
        cpBlue = utils.colorPalette[2]
        cpRed = utils.colorPalette[6]
        utils.histoStyler(trainBGHist)
        trainBGHist.SetTitle("")
        trainBGHist.GetXaxis().SetTitle("BDT Output")
        trainBGHist.GetYaxis().SetTitle("Number of events")
        trainBGHist.GetYaxis().SetTitleOffset(1.4)
        trainBGHist.GetXaxis().SetLabelSize(0.055)
        trainBGHist.SetMaximum(maxY + 0.02)

        fillC = TColor.GetColor(cpRed["fillColor"])
        lineC = TColor.GetColor(cpRed["lineColor"])
        trainBGHist.SetFillStyle(cpRed["fillStyle"])
        trainBGHist.SetFillColorAlpha(fillC, 0.35)
        trainBGHist.SetLineColor(lineC)
        trainBGHist.SetLineWidth(1)
        trainBGHist.SetOption("HIST")
        
        trainBGHist.Draw("HIST")

        legend.AddEntry(trainBGHist, "B (train)", 'F')

        fillC = TColor.GetColor(cpBlue["fillColor"])
        lineC = TColor.GetColor(cpBlue["lineColor"])
        trainSignalHist.SetFillStyle(cpBlue["fillStyle"])
        trainSignalHist.SetFillColorAlpha(fillC, 0.35)
        trainSignalHist.SetLineColor(lineC)
        trainSignalHist.SetLineWidth(1)
        trainSignalHist.SetOption("HIST")
        trainSignalHist.Draw("HIST SAME")
        
        legend.AddEntry(trainSignalHist, "S (train)", 'F')
        
        testBGHist.SetMarkerColor(kRed)
        testBGHist.SetMarkerSize(0.5)
        testBGHist.SetMarkerStyle(20)
        testBGHist.SetOption("p E1")
        testBGHist.SetLineColor(kRed)
        testBGHist.Draw("SAME p E1")
        
        legend.AddEntry(testBGHist, "B (test)", "p e2")
        
        testSignalHist.SetMarkerColor(kBlue)
        testSignalHist.SetMarkerSize(0.5)
        testSignalHist.SetMarkerStyle(20)
        testSignalHist.SetOption("p E1")
        testSignalHist.SetLineColor(kBlue)
        testSignalHist.Draw("SAME p E1")
        
        legend.AddEntry(testSignalHist, "S (test)", "p e2")
    
        legend.Draw("SAME")

    utils.stamp_plot()
    gPad.SetLogy();
    #utils.stampFab("35.9")
    c1.Print(output_file);
    c1.Print(output_file+"]");
    exit(0)

main()


