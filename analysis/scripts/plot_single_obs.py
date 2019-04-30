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

gROOT.SetBatch(True)
gStyle.SetOptStat(0)


####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Plot skims for x1x2x1 process with BDTs.')
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=True)
args = parser.parse_args()


output_file = None
signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu100_dm12p84Chi20Chipm.root"
bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dilepton_signal_bdt/high/single"
#skim_dilepton_signal_bdt
#skim_signal_bdt
if args.output_file:
    output_file = args.output_file[0]
######## END OF CMDLINE ARGUMENTS ########

def createPlots(rootfiles, type, memory, weight=None):
    print "Processing "
    print rootfiles
    mll = utils.UOFlowTH1F(type, "", 30, 0, 30)
    utils.histoStyler(mll)
    memory.append(mll)
    sum = 0
    for f in rootfiles:
        print "***"
        filename = os.path.basename(f).split(".")[0]
        rootFile = TFile(f)
        c = rootFile.Get('tEvent')
        nentries = c.GetEntries()
        print 'Analysing', nentries, "entries"
        for ientry in range(nentries):
            if ientry % 10000 == 0:
                print "Processing " + str(ientry)
            c.GetEntry(ientry)
            if c.Met < 200:
               continue
            if c.trackBDT < 0.1:
                continue
            if c.univBDT < -0.2:
                continue
            #if c.dilepBDT < 0.1:
            #    continue
            if c.tracks[0].Pt() <5:
                continue
            #if c.tracks[0].Eta() > 2.5:
            #    continue
            
            if weight is not None:
                print "****"
                sum += c.Weight * weight
                mll.Fill(c.invMass, c.Weight * weight)
            else:
                sum += c.Weight
                mll.Fill(c.invMass, c.Weight)
    print "Filled total of sum:", sum
    return mll

def main():

    print "Plotting observable"

    c1 = TCanvas("c1", "c1", 800, 800)
    c1.SetBottomMargin(0.16)
    c1.SetLeftMargin(0.18)

    c1.Print(output_file+"[");

    bg_files = glob(bg_dir + "/*")
    sumTypes = {}
    memory = []

    for f in bg_files: 
        filename = os.path.basename(f).split(".")[0]
        types = filename.split("_")
        if types[0] not in sumTypes:
            sumTypes[types[0]] = {}
        sumTypes[types[0]][types[1]] = True
    histograms = {}
    print sumTypes
    for type in sumTypes:
        if utils.existsInCoumpoundType(type):
            continue
        print "Summing type", type
        rootfiles = glob(bg_dir + "/*" + type + "*.root")
        #rootfiles.append(signal_file)
        #rootfiles = [signal_file] + rootfiles
        mll = createPlots(rootfiles, type, memory)
        print type
        histograms[type] = mll
    
    for cType in utils.compoundTypes:
        print "Creating compound type", cType
        rootFiles = []
        for type in utils.compoundTypes[cType]:
            rootFiles.extend(glob(bg_dir + "/*" + type + "*.root"))
        if len(rootFiles):
            mll = createPlots(rootFiles, cType, memory)
            histograms[type] = mll
        else:
            print "**Couldn't find file for " + cType

    sigHist = createPlots([signal_dir], "signal", memory)

    utils.formatHist(sigHist, utils.signalCp[0], 0.8)

    hs = THStack("invMass","")
    memory.append(hs)
    types = [k for k in utils.bgOrder]
    types = sorted(types, key=lambda a: utils.bgOrder[a])
    typesInx = []

    i = 0
    foundBg = False
    for type in types:
        if histograms.get(type) is not None:
            hs.Add(histograms[type])
            typesInx.append(i)
            foundBg = True
        i += 1
    #hs.Add(sigHist)
    #typesInx.append(i)

    sigMax = sigHist.GetMaximum()
    maximum = sigMax
    if foundBg:
        bgMax = hs.GetMaximum()
        maximum = max(bgMax, sigMax)

    #legend = TLegend(.69,.55,.89,.89)
    legend = TLegend(.20,.60,.89,.89)
    legend.SetNColumns(2)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    memory.append(legend)
    if foundBg:
        newBgHist = utils.styledStackFromStack(hs, memory, legend, "", typesInx, True)
        #newBgHist.SetFillColorAlpha(fillC, 0.35)
        newBgHist.SetMaximum(maximum*1000)
        newBgHist.SetMinimum(0.01)
        newBgHist.Draw("hist")
        utils.histoStyler(newBgHist)
        newBgHist.GetXaxis().SetTitle("M_{ll}")
        newBgHist.GetYaxis().SetTitle("Number of events")
        newBgHist.GetYaxis().SetTitleOffset(1.15)
        #newBgHist.GetXaxis().SetLabelSize(0.055)
        c1.Modified()
        #newBgHist.SetTitle(signal_name)

    #sigHist.SetTitle(signal_name)
    legend.AddEntry(sigHist, "signal", 'l')
    if foundBg:
        sigHist.SetMaximum(maximum)
    sigHist.SetMinimum(0.01)
    sigHist.SetLineWidth(2)
    sigHist.GetXaxis().SetTitle("GeV")
    if foundBg:
        sigHist.Draw("HIST SAME")
    else:
        sigHist.Draw("HIST")
    legend.Draw("SAME")
    gPad.SetLogy();
    utils.stamp_plot()
    c1.Update()
    c1.Print(output_file);

    c1.Print(output_file+"]");

main()


