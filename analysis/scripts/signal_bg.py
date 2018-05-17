#!/usr/bin/python

from ROOT import *
from glob import glob
from math import *
from sys import exit
from array import array
from os import system
import argparse
import sys

# load FWLite C++ libraries
# gSystem.Load("libFWCoreFWLite.so");
# gSystem.Load("libDataFormatsFWLite.so");
# FWLiteEnabler.enable()

# load FWlite python libraries
# from DataFormats.FWLite import Handle, Events
# import FWCore.ParameterSet.Config as cms

gROOT.SetBatch(1)

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import histograms
from lib import utils

SIG_FILES = [	"/afs/desy.de/user/n/nissanuv/cms-tools/sim_x10x20x10/dm20.root",
		"/afs/desy.de/user/n/nissanuv/cms-tools/sim_x10x20x10/dm13.root",
		"/afs/desy.de/user/n/nissanuv/cms-tools/sim_x10x20x10/dm7.root",
	     ]

SIG_NAMES = ["dm20", "dm13", "dm7"]

BG_FILE  = "/afs/desy.de/user/n/nissanuv/cms-tools/bg/output/sum/stack/stacked_histograms.root"
OUTPUT_FILE = "/afs/desy.de/user/n/nissanuv/cms-tools/analysis/output/signal_bg.pdf"

sigFiles = []
for sigFile in SIG_FILES:
	sigFiles.append(TFile(sigFile))

bgFile = TFile(BG_FILE)

sigCuts = utils.getSortedCutsFromRootFile(sigFiles[0])

c1 = TCanvas("c1")

titlePad = TPad("titlePad", "",0.0,0.93,1.0,1.0)
histPad = TPad("histPad", "",0.0,0.0,1.0,0.93)

titlePad.Draw()

#t =  TText();
#t.SetTextAlign(22);
#t.SetText(0.5,0.96,"")
#t.Draw();

t = TPaveText(0.0,0.93,1.0,1.0,"NB")
t.SetFillStyle(0)
t.SetLineColor(0)
t.SetTextFont(40);
t.Draw()

latex = TLatex()
latex.SetTextAlign(12); 
latex.DrawLatex(0.5,0.5,"")


histPad.Draw()
histPad.Divide(3,2)

#This disgusting thing is because THStack is a disaster class with stupid garbage collection.
memory = []


c1.Print(OUTPUT_FILE+"["); 


# Loop over cuts

for i, cut in enumerate(sigCuts):
	cutName = cut["name"]
	cutDef = histograms.cutsDefs.get(cutName)
	print "cutName=" + cutName
	print "******"
	t.Clear()
	t.AddText(cutDef["title"])
	#t.AddText("#sigma")
	t.Draw();
	#latex.DrawLatexNDC(0.5,0.95,"This is a title #tau")
	titlePad.Update()

	pId = 1
	needToDraw = False
	for histName in cut["hists"]:
		print "histName=" + histName
		histKey = histName
		if cutName != "none":
			histKey += "_" + cut["name"]
		print "histKey=" + histKey
		
		needToDraw = True
		pad = histPad.cd(pId)
		sigHists = []
		for i, sigFile in enumerate(sigFiles):
			sigHist = sigFile.Get(histKey)
			sigHist.SetStats(0)
			utils.formatHist(sigHist, utils.signalCp[i], 0.8)
			sigHists.append(sigHist)
		histDef = histograms.getHistDef(histName)
	
		if bgFile.GetListOfKeys().Contains(histKey):
			bgHist = bgFile.Get(histKey)
			if bgHist is None:
				print "****************** SKIPPING"
				continue
			bgMax = bgHist.GetMaximum()
			sigMax = 0
			for sigHist in sigHists:
				sigMax = max(sigMax, sigHist.GetMaximum())
			
			maximum = max(bgMax, sigMax)
			#hFrame = sigHist.Clone("hFrame")
			#hFrame.Reset()
			#hFrame.GetYaxis().SetRangeUser(1, maximum * 1.2)
			
			legend = TLegend(.69,.55,.89,.89)
			memory.append(legend)
			newBgHist = utils.styledStackFromStack(bgHist, memory, legend)
			
			for i, sigHist in enumerate(sigHists):
				legend.AddEntry(sigHist, SIG_NAMES[i], 'F')
				sigHist.SetMaximum(maximum)
				sigHist.SetMinimum(0.01)
			
			newBgHist.SetMaximum(maximum)
			newBgHist.SetMinimum(0.01)
			#hFrame.Draw()
			
			newBgHist.Draw("e HIST")
			if histDef is not None:
				utils.setLabels(newBgHist, histDef)
				
			for sigHist in sigHists:
				sigHist.Draw("e HIST SAME")
			legend.Draw("SAME")
		else:
			print "Not shared"
			continue
			if histDef is not None:
				utils.setLabels(sigHist, histDef)
			legend = TLegend(.69,.81,.89,.89)
			memory.append(legend)
			legend.AddEntry(sigHist, "Signal", 'F')
			sigHist.Draw("HIST")
			legend.Draw("SAME")
			
		
		pad.SetLogy()
		c1.Update()
		
		pId += 1
		
		if pId > 6:
			pId = 1
			c1.Print(OUTPUT_FILE);
			needToDraw = False;
			

	if needToDraw:
		for id in range(pId, 7):
			print "Clearing pad " + str(id)
			pad = histPad.cd(id)
			pad.Clear()
		c1.Print(OUTPUT_FILE);
	

c1.Print(OUTPUT_FILE+"]");

sigFile.Close()
bgFile.Close()