#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
from rgsutil import *
import argparse
import sys
import math
import pickle
import os

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

colors = [kBlack, kBlue-4, kRed+1, kGreen+1, kRed-7, kOrange+1, kTeal-7, kViolet-1, 28, kBlue+1, kMagenta, kYellow, kRed, kSpring, kTeal, kTeal+1, kTeal+2,kTeal+3,kTeal+4,kTeal+5,kTeal+6,kTeal+7,kTeal+8]
mstyles = [20,21,22,23,29,33,34,47,43,45]
mstyles*=3
lstyles = [1, kDashed, kDotted]
lstyles*=5

colorInx = 0

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Run TMVA.')
parser.add_argument('-bdt', '--bdt', nargs='*', help='BDT Input File', required=False)
parser.add_argument('-mlp', '--mlp', nargs='*', help='MLP Input File', required=False)
parser.add_argument('-rgs', '--rgs', nargs='*', help='RGS Input File', required=False)
parser.add_argument('-o', '--output', nargs=1, help='Output File', required=False)
args = parser.parse_args()

print args

bdt_files = args.bdt
mlp_files = args.mlp
rgs_files = args.rgs
outputFile = "roc_comparison.pdf"
if args.output:
	outputFile = args.output[0]

######## END OF CMDLINE ARGUMENTS ########

def get_TMVA_effs(tmva_output_file):

	fin = TFile(tmva_output_file)
	h_mva_bdt_effB = fin.Get("Method_BDT/BDT/MVA_BDT_effB")
	h_mva_bdt_effS = fin.Get("Method_BDT/BDT/MVA_BDT_effS")

	list_classifier = []
	list_sg_eff = []
	list_bg_eff = []

	for i in range(h_mva_bdt_effS.GetNbinsX()):
		classifier = h_mva_bdt_effS.GetBinCenter(i)
		S = h_mva_bdt_effS.GetBinContent(i)
		B = h_mva_bdt_effB.GetBinContent(i)
		list_classifier.append(classifier)
		list_sg_eff.append(S)
		list_bg_eff.append(B)

	fin.Close()
	return list_classifier, list_sg_eff, list_bg_eff

def get_method_hists(folders, method, gtestBGHists=None, gtrainBGHists=None, gtestSignalHists=None, gtrainSignalHists=None, gmethods=None, gnames=None):
	testBGHists = []
	trainBGHists = []
	testSignalHists = []
	trainSignalHists = []
	methods=[]
	names=[]
	if not folders:
		if not gtestBGHists:
			return (testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names)
		else:
			return (gtestBGHists, gtrainBGHists, gtestSignalHists, gtrainSignalHists, gmethods, gnames)
	for dir in folders:
		
		names.append(os.path.basename(dir))
		
		inputFile = dir + "/output.root"
		print "Opening file", inputFile
		fin = TFile(inputFile)
		
		trainTree = fin.Get("dataset/TrainTree")
		testTree = fin.Get("dataset/TestTree")
		
		testTree.Draw(method + ">>hsqrt(10000)", "weight * (classID==0)")
		testSignalHist = testTree.GetHistogram().Clone()
		testSignalHist.SetDirectory(0)
		testTree.Draw(method + ">>hsqrt(10000)", "weight * (classID==1)")
		testBgHist = testTree.GetHistogram().Clone()
		testBgHist.SetDirectory(0)
		trainTree.Draw(method + ">>hsqrt(10000)", "weight * (classID==0)")
		trainSignalHist = trainTree.GetHistogram().Clone()
		trainSignalHist.SetDirectory(0)
		trainTree.Draw(method + ">>hsqrt(10000)", "weight * (classID==1)")
		trainBgHist = trainTree.GetHistogram().Clone()
		trainBgHist.SetDirectory(0)
	
		minX = max(testBgHist.GetXaxis().GetXmin(), testSignalHist.GetXaxis().GetXmin(), trainSignalHist.GetXaxis().GetXmin(), trainBgHist.GetXaxis().GetXmin())
		maxX = min(testBgHist.GetXaxis().GetXmax(), testSignalHist.GetXaxis().GetXmax(), trainSignalHist.GetXaxis().GetXmax(), trainBgHist.GetXaxis().GetXmax())
	
		#print minX, maxX
	
		testTree.Draw(method + ">>hsqrt(10000," + str(minX) + "," + str(maxX) + ")", "weight * (classID==0)")
		testSignalHist = testTree.GetHistogram().Clone()
		testSignalHist.SetDirectory(0)
		testTree.Draw(method + ">>hsqrt(10000," + str(minX) + "," + str(maxX) + ")", "weight * (classID==1)")
		testBgHist = testTree.GetHistogram().Clone()
		testBgHist.SetDirectory(0)
		trainTree.Draw(method + ">>hsqrt(10000," + str(minX) + "," + str(maxX) + "", "weight * (classID==0)")
		trainSignalHist = trainTree.GetHistogram().Clone()
		trainSignalHist.SetDirectory(0)
		trainTree.Draw(method + ">>hsqrt(10000," + str(minX) + "," + str(maxX) + "", "weight * (classID==1)")
		trainBgHist = trainTree.GetHistogram().Clone()
		trainBgHist.SetDirectory(0)
		
		testBGHists.append(testBgHist)
		trainBGHists.append(trainBgHist)
		testSignalHists.append(testSignalHist)
		trainSignalHists.append(trainSignalHist)
		methods.append(method)
		
		fin.Close()
	if gtestBGHists is None:
		return (testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names)
	else:
		gtestBGHists.extend(testBGHists)
		gtrainBGHists.extend(trainBGHists)
		gtestSignalHists.extend(testSignalHists)
		gtrainSignalHists.extend(trainSignalHists)
		gmethods.extend(methods)
		gnames.extend(names)
		return (gtestBGHists, gtrainBGHists, gtestSignalHists, gtrainSignalHists, gmethods, gnames)
	

def get_bdt_hists(folders, testBGHists=None, trainBGHists=None, testSignalHists=None, trainSignalHists=None, methods=None, names=None):
	return get_method_hists(folders, "BDT", testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names)

def get_mlp_hists(folders, testBGHists=None, trainBGHists=None, testSignalHists=None, trainSignalHists=None, methods=None, names=None):
	return get_method_hists(folders, "MLP", testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names)

#needed for the legend
memory = []

def plot_rocs():
	
	(testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names) = get_bdt_hists(bdt_files)
	get_mlp_hists(mlp_files, testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names)
	
	# Create canvas
	canvas = TCanvas("roc", "roc", 520, 10, 1000, 1000)
	canvas.SetTopMargin(0.5 * canvas.GetTopMargin())
	canvas.SetBottomMargin(1 * canvas.GetBottomMargin())
	canvas.SetLeftMargin(1 * canvas.GetLeftMargin())
	canvas.SetRightMargin(0.5 * canvas.GetRightMargin())
	
	setStyle()

	# Create a 2-D histogram for ROC plot
	xbins =   1000
	xmin  =  0.0
	xmax  =  1
	ybins =   1000
	ymin  =  0
	ymax  =  1
	hist  = mkhist2("hroc",
		    "#font[12]{#epsilon_{S}}",
		    "background rejection (1 - #font[12]{#epsilon_{B}})",
		    xbins, xmin, xmax,
		    ybins, ymin, ymax,
		    color = kBlue+1)
	
	hist.SetMinimum(0)
	hist.SetMarkerSize(0.2)
	hist.SetLabelSize(0.02, "x")
	hist.SetLabelSize(0.02, "y")
	hist.SetTitleSize(0.02, "x")
	hist.SetTitleSize(0.02, "y")
	hist.GetXaxis().SetTitleOffset(2)
	hist.GetYaxis().SetTitleOffset(3)
	
	hist.Draw("p")
	hist.GetYaxis().SetTitleOffset(2.0)
	
	legend = TLegend(0.2, 0.2, 0.89, 0.7)

	for inx in range(len(testBGHists)):
		
		testBGHist, trainBGHist, testSignalHist, trainSignalHist, method, name = testBGHists[inx], trainBGHists[inx], testSignalHists[inx], trainSignalHists[inx], methods[inx], names[inx]

		h = TGraph()
		memory.append(h)
	
		highestZ = 0
		highestS = 0
		highestB = 0
	
		# print "testSignalHistBDT"
# 		print testSignalHistBDT.Integral(), testSignalHistBDT.GetNbinsX(), testSignalHistBDT.GetXaxis().GetXmin(), testSignalHistBDT.GetXaxis().GetXmax()
# 		print "testBgHistBDT"
# 		print testBgHistBDT.Integral(), testBgHistBDT.GetNbinsX(), testBgHistBDT.GetXaxis().GetXmin(), testBgHistBDT.GetXaxis().GetXmax()

		numOfBins = testBGHist.GetNbinsX()
		#print "numOfBins=" , numOfBins
	
		ST = trainSignalHist.Integral() + testSignalHist.Integral()
		BT = trainBGHist.Integral() + testBGHist.Integral()
		print "=================="
		print method + " " + name
		print "Signal: " + str(ST)
		print "Background: " + str(BT)
	
		for i in range(numOfBins):
			S = trainSignalHist.Integral(i,numOfBins+1) + testSignalHist.Integral(i,numOfBins+1)
			B = trainBGHist.Integral(i,numOfBins+1) + testBGHist.Integral(i,numOfBins+1)
			h.SetPoint(i,S/ST, 1 - B/BT)
			if S + B:
				Z = 1.0 * S/math.sqrt(S+B)
				if Z > highestZ:
					highestZ = Z
					highestS = S
					highestB = B
	
# 		print "highestBdtZ=" + str(highestBdtZ)
# 		print "highestBdtS=" + str(highestBdtS)
# 		print "highestBdtB=" + str(highestBdtB)
# 		print "highestBdtFS=" + str(highestBdtS/BdtST)
# 		print "highestBdtFB=" + str(highestBdtB/BdtBT)
		global colorInx
		color = colors[colorInx]
		colorInx += 1
		
		h.SetLineColor(color)
		h.SetMarkerSize(0.2)
		#hbdt.SetFillColor(kRed)

		h.Draw("same")
		
		print "highestZ=" + str(highestZ)
		print "highestS=" + str(highestS)
		print "highestB=" + str(highestB)
 
		hHighestZ = TGraph()
		hHighestZ.SetPoint(0, highestS/ST, 1-highestB/BT)
		color = colors[colorInx]
		colorInx += 1
		hHighestZ.SetMarkerColor(color)
		hHighestZ.SetMarkerSize(2)
		hHighestZ.SetFillColor(0)
 		hHighestZ.Draw("p same")
 		
 		memory.append(hHighestZ)
 		
 		legend.AddEntry(h, method + " " + name, "l")
 		legend.AddEntry(hHighestZ, method + " " + name + " " + "(highest S/#sqrt{S+B})=" + str(highestZ), "p")
	
	hi = 0
	
	for rgs_dir in rgs_files:

		RgsTs = 0
		RgsTb = 0

		sCount = None
		bCount = None
	
		bestRgsZ   = -1    # best Z value
		bestRgsFs = -1    
		bestRgsFb = -1
		bestRgsS = -1
		bestRgsB = -1
		
		name = os.path.basename(rgs_dir)

		print "Opening pickle!"
		with open(rgs_dir + "/output.pickle", "rb") as f:
			data = pickle.load(f)
			RgsTs = data[0]
			RgsTb = data[1]
			sCount = data[2]
			bCount = data[3]
	
		print "===========  RGS =============="
		print "Totals RGS " + name + ":"
		print "Signal: " + str(RgsTs)
		print "Background: " + str(RgsTb)
		
		color = colors[colorInx]
		colorInx += 1
		
		h = mkhist2("hroc" + str(hi),
		    "#font[12]{#epsilon_{S}}",
		    "background rejection (1 - #font[12]{#epsilon_{B}})",
		    xbins, xmin, xmax,
		    ybins, ymin, ymax,
		    color = color)
		h.SetMinimum(0)
		h.SetMarkerSize(0.2)
		
		
		hi += 1
		
		memory.append(h)
		
		for row, b in enumerate(bCount):
	
			b  = bCount[row] #  background count        
			s  = sCount[row] #  signal count

			fs = s / RgsTs
			fb = b / RgsTb
			h.Fill(fs, 1-fb)
			
			#print "----------------------------"
			#print "Fraction Signal: " + str(fs)
			#print "Fraction Background: " + str(fb)
		
			Z = 0
			if s+b:
				Z = s / math.sqrt(s+b)
			if Z > bestRgsZ:
				bestRgsZ = Z
				bestRgsFs = fs
				bestRgsFb = fb
				bestRgsS = s
				bestRgsB = b
	
		print "Best RGS Z=" + str(bestRgsZ)
		print "Best RGS FS=" + str(bestRgsFs)
		print "Best RGS FB=" + str(bestRgsFb)
		print "Best RGS s=" + str(bestRgsS)
		print "Best RGS b=" + str(bestRgsB)
	
		# include point with highest Z RGS

		canvas.cd()

		h.Draw("p same")

		hHighestRgsZ = TGraph()
		hHighestRgsZ.SetPoint(0, bestRgsFs, 1-bestRgsFb)
		color = colors[colorInx]
		colorInx += 1
		hHighestRgsZ.SetMarkerColor(color)
		hHighestRgsZ.SetMarkerSize(2)
		hHighestRgsZ.SetFillColor(0)
		hHighestRgsZ.Draw("p same")
		
		memory.append(hHighestRgsZ)
		
		legend.AddEntry(h, "RGS - " + name, "p")
		legend.AddEntry(hHighestRgsZ, "RGS -" + name + "- (highest S/#sqrt{S+B})=" + str(bestRgsZ), "p")
	

	legend.SetBorderSize(0)
	legend.SetFillStyle(0)
	legend.SetNColumns(1)
	legend.Draw()

	canvas.Update()
	canvas.SaveAs(outputFile)

if __name__ == "__main__":
	plot_rocs()

