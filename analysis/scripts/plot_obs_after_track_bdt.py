#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import os

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools/lib")
import utils

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Plot skims for x1x2x1 process with BDTs.')
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=True)
parser.add_argument('-s', '--signal', nargs=1, help='Signal', required=True)
parser.add_argument('-bg', '--background', nargs=1, help='Background', required=True)
args = parser.parse_args()
	

output_file = None
signal_dir = None
bg_dir = None
if args.output_file:
	output_file = args.output_file[0]
if args.signal:
	signal_dir = args.signal[0]
if args.background:
	bg_dir = args.background[0]
######## END OF CMDLINE ARGUMENTS ########


def createPlots(rootfiles, type, memory, weight=None):
	print "Processing "
	print rootfiles
	mll = utils.UOFlowTH1F(type, "M_{ll}", 50, 0, 30)
	memory.append(mll)
	for f in rootfiles:
		print "***"
		filename = os.path.basename(f).split(".")[0]
		rootFile = TFile(f)
		c = rootFile.Get('tEvent')
		nentries = c.GetEntries()
		print 'Analysing', nentries, "entries"
		for ientry in range(nentries):
			if ientry % 1000 == 0:
				print "Processing " + str(ientry)
			c.GetEntry(ientry)
			#if c.Met < 200:
			#	continue
			t = c.tracks[0]
			l = None
			if c.Electrons.size():
				l = c.Electrons[0]
			else:
				l = c.Muons[0]
			if weight is not None:
				mll.Fill((t + l).M(), c.Weight * weight)
			else:
				mll.Fill((t + l).M(), c.Weight)
	return mll

def main():

	print "Plotting observable"
	#print os.path.normpath("a/b/c")
	#print os.path.normpath("a/b/c/")
	c1 = TCanvas("c1")

	titlePad = TPad("titlePad", "",0.0,0.93,1.0,1.0)
	histPad = TPad("histPad", "",0.0,0.0,1.0,0.93)

	titlePad.Draw()

	t = TPaveText(0.0,0.93,1.0,1.0,"NB")
	t.SetFillStyle(0)
	t.SetLineColor(0)
	t.SetTextFont(40);
	t.AddText("Invariant Mass For Different Signals")
	t.Draw()
	histPad.Draw()
	histPad.Divide(3,2)

	memory = []
	c1.Print(output_file+"[");

	plot_num = 0
	
	pId = 1
	needToDraw = False
	
	signal_files = glob(signal_dir + "/*")
	signal_files.sort()
	for signal_file in signal_files:
		needToDraw = True
		pad = histPad.cd(pId)
		
		plot_num += 1
	
		signal_name = os.path.splitext(os.path.basename(signal_file))[0]
		print "Plotting for signal=" + signal_name
	
		bg_files_dir = bg_dir + "/" + signal_name + "/single"
	
		bg_files = glob(bg_files_dir + "/*")
	
		sumTypes = {}
	
		for f in bg_files: 
			filename = os.path.basename(f).split(".")[0]
			types = filename.split("_")
			if types[0] not in sumTypes:
				sumTypes[types[0]] = {}
			sumTypes[types[0]][types[1]] = True
		histograms = {}
		for type in sumTypes:
			if utils.existsInCoumpoundType(type):
				continue
			print "Summing type", type
			rootfiles = glob(bg_files_dir + "/*" + type + "*.root")
			mll = createPlots(rootfiles, type, memory)
			histograms[type] = mll
		for cType in utils.compoundTypes:
			print "Creating compound type", cType
			rootFiles = []
			for type in utils.compoundTypes[cType]:
				rootFiles.extend(glob(bg_files_dir + "/*" + type + "*.root"))
			if len(rootFiles):
				mll = createPlots(rootFiles, cType, memory)
				histograms[type] = mll
			else:
				print "**Couldn't find file for " + cType

		print histograms
		
		sigHist = createPlots([signal_file], "signal", memory, 4.0)
		utils.formatHist(sigHist, utils.signalCp[0], 0.8)
		
		hs = THStack("invMass","")
		memory.append(hs)
		types = [k for k in utils.bgOrder]
		types = sorted(types, key=lambda a: utils.bgOrder[a])
		typesInx = []
		i = 0
		for type in types:
			if histograms.get(type) is not None:
				hs.Add(histograms[type])
				typesInx.append(i)
			i += 1
		
		bgMax = hs.GetMaximum()
		sigMax = sigHist.GetMaximum()
		
		maximum = max(bgMax, sigMax)
		
		legend = TLegend(.69,.55,.89,.89)
		memory.append(legend)
		newBgHist = utils.styledStackFromStack(hs, memory, legend, "", typesInx)
		newBgHist.SetMaximum(maximum)
		newBgHist.SetMinimum(0.01)
		#hFrame.Draw()
		
		newBgHist.Draw("hist")
		newBgHist.SetTitle(signal_name)
 		newBgHist.GetXaxis().SetTitle("GeV")
 		
 		legend.AddEntry(sigHist, "signal", 'l')
		sigHist.SetMaximum(maximum)
		sigHist.SetMinimum(0.01)
			
		sigHist.Draw("HIST SAME")
		legend.Draw("SAME")
		
		#pad.SetLogy()
		c1.Update()
		
		pId += 1
		
		if pId > 6:
			pId = 1
			c1.Print(output_file);
			needToDraw = False;
			

	if needToDraw:
		for id in range(pId, 7):
			print "Clearing pad " + str(id)
			pad = histPad.cd(id)
			pad.Clear()
		c1.Print(output_file);
		
	c1.Print(output_file+"]");

main()


