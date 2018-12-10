from ROOT import *
import sys
import numpy as np
import os

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
		name = os.path.basename(dir)
		print "dir=" + dir
		print "name=" + name
		names.append(name)
		
		inputFile = dir + "/" + name  + ".root"
		print "Opening file", inputFile
		fin = TFile(inputFile)
		
		trainTree = fin.Get("dataset/TrainTree")
		testTree = fin.Get("dataset/TestTree")
		
		testTree.Draw(method + ">>hsqrt(10000)", "weight * (classID==0)")
		testSignalHist = testTree.GetHistogram().Clone()
		#print method + " testSignalHist=" + str(testSignalHist.Integral())
		testSignalHist.SetDirectory(0)
		testTree.Draw(method + ">>hsqrt(10000)", "weight * (classID==1)")
		testBgHist = testTree.GetHistogram().Clone()
		#print method + " testBgHist=" + str(testBgHist.Integral())
		testBgHist.SetDirectory(0)
		trainTree.Draw(method + ">>hsqrt(10000)", "weight * (classID==0)")
		trainSignalHist = trainTree.GetHistogram().Clone()
		#print method + " trainSignalHist=" + str(trainSignalHist.Integral())
		trainSignalHist.SetDirectory(0)
		trainTree.Draw(method + ">>hsqrt(10000)", "weight * (classID==1)")
		trainBgHist = trainTree.GetHistogram().Clone()
		#print method + " trainBgHist=" + str(trainBgHist.Integral())
		trainBgHist.SetDirectory(0)
		
		#print "max=", trainSignalHist.GetXaxis().GetXmax()
		
		minX = min(testBgHist.GetXaxis().GetXmin(), testSignalHist.GetXaxis().GetXmin(), trainSignalHist.GetXaxis().GetXmin(), trainBgHist.GetXaxis().GetXmin())
		maxX = max(testBgHist.GetXaxis().GetXmax(), testSignalHist.GetXaxis().GetXmax(), trainSignalHist.GetXaxis().GetXmax(), trainBgHist.GetXaxis().GetXmax())
		#print "======="
		#print minX, maxX
	
		testTree.Draw(method + ">>hsqrt(10000," + str(minX) + "," + str(maxX) + ")", "weight * (classID==0)")
		testSignalHist = testTree.GetHistogram().Clone()
		testSignalHist.SetDirectory(0)
		#print method + " testSignalHist=" + str(testSignalHist.Integral())
		testTree.Draw(method + ">>hsqrt(10000," + str(minX) + "," + str(maxX) + ")", "weight * (classID==1)")
		testBgHist = testTree.GetHistogram().Clone()
		testBgHist.SetDirectory(0)
		#print method + " testBgHist=" + str(testBgHist.Integral())
		trainTree.Draw(method + ">>hsqrt(10000," + str(minX) + "," + str(maxX) + "", "weight * (classID==0)")
		trainSignalHist = trainTree.GetHistogram().Clone()
		trainSignalHist.SetDirectory(0)
		#print method + " trainSignalHist=" + str(trainSignalHist.Integral())
		trainTree.Draw(method + ">>hsqrt(10000," + str(minX) + "," + str(maxX) + "", "weight * (classID==1)")
		trainBgHist = trainTree.GetHistogram().Clone()
		trainBgHist.SetDirectory(0)
		#print method + " trainBgHist=" + str(trainBgHist.Integral())
		
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
