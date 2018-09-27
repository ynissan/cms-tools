#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
from rgsutil import *
import argparse
import sys
import math
import pickle

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Run TMVA.')
parser.add_argument('-bdt', '--bdt', nargs=1, help='BDT Input File', required=True)
parser.add_argument('-rgs', '--rgs', nargs=1, help='RGS Input File', required=True)
args = parser.parse_args()


bdt_file = args.bdt[0]
rgs_file = args.rgs[0]
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

def plot_rocs():
	ts = 0
	tb = 0

	sCount = None
	bCount = None
	
	bestZ   = -1    # best Z value
	bestRow = -1    # row with best cut-point

	print "Opening pickle!"
	with open(rgs_file, "rb") as f:
		data = pickle.load(f)
		ts = data[0]
		tb = data[1]
		sCount = data[2]
		bCount = data[3]

	setStyle()

	# Create a 2-D histogram for ROC plot
	xbins =   1000
	xmin  =  0.0
	xmax  =  1
	ybins =   1000
	ymin  =  0.0
	ymax  =  1
	hist  = mkhist2("hroc",
		    "#font[12]{#epsilon_{S}}",
		    "background rejection (1 - #font[12]{#epsilon_{B}})",
		    xbins, xmin, xmax,
		    ybins, ymin, ymax,
		    color = kBlue+1)
	hist.SetMinimum(0)
	hroc.SetMarkerSize(0.2)
	
	
	print "Totals:"
	print "Signal: " + str(ts)
	print "Background: " + str(tb)
	for row, b in enumerate(bCount):
	
		b  = bCount[row] #  background count        
		s  = sCount[row] #  signal count

		fs = s / ts
		fb = b / tb

		hist.Fill(fs, 1-fb)
		#print "----------------------------"
		#print "Fraction Signal: " + str(fs)
		#print "Fraction Background: " + str(fb)
		
		Z = 0
		if s+b:
			Z = s / math.sqrt(s+b)
		if Z > bestZ:
			bestZ = Z
			bestRow = row


	print "weighted totals (sg, bg): %s, %s" % (ts, tb)

	# Save plots
	canvas = TCanvas("roc", "roc", 520, 10, 1000, 1000)
	canvas.SetTopMargin(0.5 * canvas.GetTopMargin())
	canvas.SetBottomMargin(0.9 * canvas.GetBottomMargin())
	canvas.SetLeftMargin(1.0 * canvas.GetLeftMargin())
	canvas.SetRightMargin(0.3 * canvas.GetRightMargin())

	#hist.SetMarkerColor(1)
	#hist.SetMarkerSize(1.2)
	#hist.SetFillColor(0)
	hist.Draw("p")
	hist.GetYaxis().SetTitleOffset(2.0)

	# include comparison hand-picked cut results:
# 	hpicked = TGraph()
# 	if "short" in name:
# 	hpicked.SetPoint(0, handpicked.cutbased_short_values["eff_sg"], 1-handpicked.cutbased_short_values["eff_bg"])
# 	elif "medium" in name:
# 	hpicked.SetPoint(0, handpicked.cutbased_medium_values["eff_sg"], 1-handpicked.cutbased_medium_values["eff_bg"])
# 	elif "long" in name:
# 	hpicked.SetPoint(0, handpicked.cutbased_long_values["eff_sg"], 1-handpicked.cutbased_long_values["eff_bg"])
# 	hpicked.SetMarkerColor(kOrange+7)
# 	hpicked.SetMarkerSize(2)
# 	hpicked.SetFillColor(0)
# 	hpicked.Draw("p same")

	# include comparison to TMVA results:
# 	print "Opening file", bdt_file
# 	fin = TFile(bdt_file)
# 	
# 	trainTree = fin.Get("dataset/TrainTree")
# 	testTree = fin.Get("dataset/TestTree")
# 	
# 	testTree.Draw("BDT>>hsqrt(10000)", "weight * (classID==0)")
# 	testSignalHistBDT = testTree.GetHistogram().Clone()
# 	testSignalHistBDT.SetDirectory(0)
# 	testTree.Draw("BDT>>hsqrt(10000)", "weight * (classID==1)")
# 	testBgHistBDT = testTree.GetHistogram().Clone()
# 	testBgHistBDT.SetDirectory(0)
# 	trainTree.Draw("BDT>>hsqrt(10000)", "weight * (classID==0)")
# 	trainSignalHistBDT = trainTree.GetHistogram().Clone()
# 	trainSignalHistBDT.SetDirectory(0)
# 	trainTree.Draw("BDT>>hsqrt(10000)", "weight * (classID==1)")
# 	trainBgHistBDT = trainTree.GetHistogram().Clone()
# 	trainBgHistBDT.SetDirectory(0)
# 	
# 	minX = max(testBgHistBDT.GetXaxis().GetXmin(), testSignalHistBDT.GetXaxis().GetXmin(), trainSignalHistBDT.GetXaxis().GetXmin(), trainBgHistBDT.GetXaxis().GetXmin())
# 	maxX = min(testBgHistBDT.GetXaxis().GetXmax(), testSignalHistBDT.GetXaxis().GetXmax(), trainSignalHistBDT.GetXaxis().GetXmax(), trainBgHistBDT.GetXaxis().GetXmax())
# 	
# 	print minX, maxX
# 	
# 	testTree.Draw("BDT>>hsqrt(10000," + str(minX) + "," + str(maxX) + ")", "weight * (classID==0)")
# 	testSignalHistBDT = testTree.GetHistogram().Clone()
# 	testSignalHistBDT.SetDirectory(0)
# 	testTree.Draw("BDT>>hsqrt(10000," + str(minX) + "," + str(maxX) + ")", "weight * (classID==1)")
# 	testBgHistBDT = testTree.GetHistogram().Clone()
# 	testBgHistBDT.SetDirectory(0)
# 	trainTree.Draw("BDT>>hsqrt(10000," + str(minX) + "," + str(maxX) + "", "weight * (classID==0)")
# 	trainSignalHistBDT = trainTree.GetHistogram().Clone()
# 	trainSignalHistBDT.SetDirectory(0)
# 	trainTree.Draw("BDT>>hsqrt(10000," + str(minX) + "," + str(maxX) + "", "weight * (classID==1)")
# 	trainBgHistBDT = trainTree.GetHistogram().Clone()
# 	trainBgHistBDT.SetDirectory(0)
# 	
#  	print "testSignalHistBDT"
#  	print testSignalHistBDT.Integral(), testSignalHistBDT.GetNbinsX(), testSignalHistBDT.GetXaxis().GetXmin(), testSignalHistBDT.GetXaxis().GetXmax()
#  	print "testBgHistBDT"
#  	print testBgHistBDT.Integral(), testBgHistBDT.GetNbinsX(), testBgHistBDT.GetXaxis().GetXmin(), testBgHistBDT.GetXaxis().GetXmax()
# 
# 	numOfBins = testBgHistBDT.GetNbinsX()
# 	print "numOfBins=" , numOfBins
# 	
# 	ST = trainSignalHistBDT.Integral() + testSignalHistBDT.Integral()
# 	BT = trainBgHistBDT.Integral() + testBgHistBDT.Integral()
# 	
# 	print "ST=",ST
# 	print "BT=",BT
# 	
# 	hbdt = TGraph()
# 	
# 	for i in range(numOfBins):
# 		
# 		S = trainSignalHistBDT.Integral(i,numOfBins+1) + testSignalHistBDT.Integral(i,numOfBins+1)
#  		B = trainBgHistBDT.Integral(i,numOfBins+1) + testBgHistBDT.Integral(i,numOfBins+1)
# 		hbdt.SetPoint(i,S/ST, 1 - B/BT)
# 
# 	hbdt.SetMarkerColor(4)
# 	hbdt.SetMarkerSize(1)
# 	hbdt.SetFillColor(0)
# 	hbdt.Draw("p same")
# 
# 	# include point with highest Z:
# 	canvas.cd()

# 	hHighestZ = TGraph()
# 	hHighestZ.SetPoint(0, eff_scale_sg*best_significance["eff_sg"], 1-(eff_scale_bg*best_significance["eff_bg"]))
# 	hHighestZ.SetMarkerColor(kMagenta)
# 	hHighestZ.SetMarkerSize(2)
# 	hHighestZ.SetFillColor(0)
# 	hHighestZ.Draw("p same")

# 	latex=TLatex()
# 	latex.SetNDC()
# 	latex.SetTextAngle(0)
# 	latex.SetTextColor(kBlack)
# 	latex.SetTextFont(42)
# 	latex.SetTextSize(0.035)
# 	latex.DrawLatex(0.4, 0.45, "#epsilon = #frac{# tracks passing selection}{# tracks with p_{T}>10 GeV}")

	legend = TLegend(0.5, 0.2, 0.89, 0.4)
	#legend.SetHeader("short tracks")
	legend.AddEntry(hist, "RGS")
	#legend.AddEntry(hbdt, "BDT")
	#legend.AddEntry(hHighestZ, "BDT (highest S/#sqrt{S+B})")
	legend.SetBorderSize(0)
	legend.SetFillStyle(0)
	legend.SetNColumns(1)
	legend.Draw()

	canvas.Update()
	canvas.SaveAs("roc_comparison.pdf")

if __name__ == "__main__":
	plot_rocs()

