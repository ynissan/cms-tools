#!/usr/bin/python

from ROOT import *
from glob import glob
from math import *
from sys import exit
import os

TYPE_SUM_DIR = "/afs/desy.de/user/n/nissanuv/cms-tools/bg/output/sum/type_sum_all"
NEWEST_SIM_DIR="/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/Production2016v1"
LUMINOSITY = 35900.

fileList = glob(TYPE_SUM_DIR + "/*");
for f in fileList:
	filename = os.path.basename(f).split(".")[0]
	#print "Processing f=" + filename
	type, HtBin = filename.split("_")
	orig_file = glob(NEWEST_SIM_DIR + "/Summer16." + type + "*" + HtBin + "*")[0];
	#print "Checking file " + orig_file
	c = TChain("TreeMaker2/PreSelection");
	c.Add(orig_file)
	c.GetEntry(0)
	cs = c.CrossSection
	#print str(cs)
	fhists = TFile(f)
	HT = fhists.Get("HT")
	numOfEvents = HT.Integral(-1,99999999)+0.000000000001
	weight = (LUMINOSITY * cs)/numOfEvents
	print filename + " " + str(weight)
	
	