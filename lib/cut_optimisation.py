from ROOT import *
import sys
import numpy as np
import os
import math
import xml.etree.ElementTree as ET
from array import array

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

def getHighestZ(trainSignalHist, trainBGHist, testSignalHist, testBGHist, h=None):
	highestZ = 0
	highestS = 0
	highestB = 0
	highestBDT = 0
	
	numOfBins = testBGHist.GetNbinsX()
	#print "numOfBins=" , numOfBins

	ST = trainSignalHist.Integral() + testSignalHist.Integral()
	BT = trainBGHist.Integral() + testBGHist.Integral()
	#print "=================="
	#print "Signal: " + str(ST)
	#print "Background: " + str(BT)

	for i in range(numOfBins):
		S = trainSignalHist.Integral(i,numOfBins+1) + testSignalHist.Integral(i,numOfBins+1)
		B = trainBGHist.Integral(i,numOfBins+1) + testBGHist.Integral(i,numOfBins+1)
		if h is not None:
			h.SetPoint(i,S/ST, 1 - B/BT)
		if S + B:
			Z = 1.0 * S/math.sqrt(S+B)
			if Z > highestZ:
				highestZ = Z
				highestS = S
				highestB = B
				highestMVA = trainSignalHist.GetBinCenter(i)
	
	#print "=================="
	
	return highestZ, highestS, highestB, highestMVA, ST, BT

def getVariablesFromXMLWeightsFile(file):
	tree = ET.parse(file)
	root = tree.getroot()
	vars = root.find('Variables')
	varsFromFile = []
	for var in vars.iter('Variable'):
		varsFromFile.append({"name" : var.get('Expression'), "type" : var.get('Type')})
	return varsFromFile

def getVariablesMemMap(vars):
	memMap = {}
	for var in vars:
		memMap[var["name"]] = array('f', [0])
	return memMap

def prepareReader(xmlfilename, vars, varsMap):
	reader = TMVA.Reader()
	for var in vars:
		print "AddVar=" + var["name"]
		reader.AddVariable(var["name"], varsMap[var["name"]])
	reader.BookMVA("BDT", xmlfilename)
	return reader
