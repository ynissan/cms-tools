#!/usr/bin/python

from ROOT import *
from glob import glob
from math import *
from sys import exit
from array import array
from os import system
import argparse
import os
import sys

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import utils

# load FWLite C++ libraries
# gSystem.Load("libFWCoreFWLite.so");
# gSystem.Load("libDataFormatsFWLite.so");
# FWLiteEnabler.enable()

# load FWlite python libraries
# from DataFormats.FWLite import Handle, Events
# import FWCore.ParameterSet.Config as cms

COMPOUND_TYPES = {
	"Rare" : ["WZZ", "WWZ", "ZZZ"],
	"DiBoson" : ["WZ", "WW", "ZZ"]
}
	
parser = argparse.ArgumentParser(description='Sum BG histograms.')
parser.add_argument('-hadd', '--hadd', dest='hadd', help='Add histogram', action='store_true')
parser.add_argument('-cp', '--create_plots', dest='cp', help='Create plots', action='store_true')
parser.add_argument('-a', '--all', dest='all', help='Perform all', action='store_true')
parser.add_argument('-s', '--stack', dest='stack', help='Perform stack', action='store_true')
parser.add_argument('-skim', '--skim', dest='skim', help='Work on skim', action='store_true')
args = parser.parse_args()

hadd = args.hadd
cp = args.cp
all = args.all
stack = args.stack
skim = args.skim

BG_OUTPUT = "/afs/desy.de/user/n/nissanuv/work/x1x2x1/bg/hist"
if skim:
	BG_OUTPUT = "/afs/desy.de/user/n/nissanuv/work/x1x2x1/bg/skim"	
BG_SINGLE_OUTPUT = BG_OUTPUT + "/single"
BG_OUTPUT_SUM = BG_OUTPUT + "/sum"
BG_OUTPOUT_TYPE_SUM = BG_OUTPUT_SUM + "/type_sum"
BG_OUTPOUT_PROCESSED = BG_OUTPUT_SUM + "/processed"
BG_OUTPOUT_STACK = BG_OUTPUT_SUM + "/stack"
LUMINOSITY = 35900.

if not os.path.isdir(BG_OUTPUT_SUM):
	os.mkdir(BG_OUTPUT_SUM)
	
if not os.path.isdir(BG_OUTPOUT_TYPE_SUM):
	os.mkdir(BG_OUTPOUT_TYPE_SUM)

if not os.path.isdir(BG_OUTPOUT_PROCESSED):
	os.mkdir(BG_OUTPOUT_PROCESSED)

if not os.path.isdir(BG_OUTPOUT_STACK):
	os.mkdir(BG_OUTPOUT_STACK)
	
bgTypes = {}

def existsInCoumpoundType(key):
	for cType in COMPOUND_TYPES:
		if key in COMPOUND_TYPES[cType]:
			return True
	return False
	
def createPlots(rootfiles, outputFileName):

	print rootfiles

	fnew = TFile(BG_OUTPOUT_PROCESSED + "/" + outputFileName +'.root','recreate')
	fhists0 = TFile(rootfiles[0])
	keys = fhists0.GetListOfKeys()
	HT = fhists0.Get("HT").Clone()
	for key in keys:
		name = key.GetName()#histogram name
		h = fhists0.Get(name).Clone()
		numOfEvents = HT.Integral(-1,99999999)+0.000000000001
		#print "numOfEvents=" + str(numOfEvents)
		weight = LUMINOSITY/numOfEvents
		#print "weight=" + str(weight)
		#print "file=" +  rootfiles[0] + " key=" + name + " numOfEvents=" + str(numOfEvents) + " weight=" + str(weight)
		if name != "HT":
			#print "scaling hist=" + name + " weight=" + str(weight)
			h.Scale(weight)
		for fname in rootfiles[1:]:
			#print "******"
			f_ = TFile(fname)
			fhists0.cd()
			h_ = f_.Get(name).Clone()
			hHT_ = f_.Get("HT").Clone()
			numOfEvents = hHT_.Integral(-1,99999999)+0.000000000001
			weight = LUMINOSITY/numOfEvents
			#print "file=" +  fname + " key=" + name + " numOfEvents=" + str(numOfEvents) + " weight=" + str(weight)
			if name != "HT":
				print "scaling hist=" + name + " weight=" + str(weight)
				h_.Scale(weight)
			h.Add(h_)
	
		fnew.cd()
		h.Write()
		fhists0.cd()
	fnew.Close()

def getCompoundTypeFiles(cType):
	rootFiles = []
	for type in COMPOUND_TYPES[cType]:
		rootFiles.extend(glob(BG_OUTPOUT_TYPE_SUM + "/*" + type + "*.root"))
	return rootFiles


# Add the histograms
if hadd or all:
	print "Adding histograms."
	fileList = glob(BG_SINGLE_OUTPUT + "/Summer16*");
	for f in fileList : 
		filename = os.path.basename(f).split(".")[1]
		types = filename.split("_")
		type = types[0]
		if type not in bgTypes:
			bgTypes[type] = {}
		if type == "DYJetsToLL":
			bgTypes[type][types[2]] = True
		else:
			bgTypes[type][types[1]] = True

	print bgTypes 

	for bgType in bgTypes:
		for bgTypeRange in bgTypes[bgType]:
			command = None
			if bgType == "DYJetsToLL":
				command = "hadd -f " + BG_OUTPOUT_TYPE_SUM + "/" + bgType + "_" + bgTypeRange + ".root " + BG_SINGLE_OUTPUT + "/Summer16." + bgType + "_*" + bgTypeRange + "*.root"
			else:
				command = "hadd -f " + BG_OUTPOUT_TYPE_SUM + "/" + bgType + "_" + bgTypeRange + ".root " + BG_SINGLE_OUTPUT + "/Summer16." + bgType + "_" + bgTypeRange + "*.root"
			print "Perorming:", command 
			system(command)

if cp or all:

	print "Creating plots."

	bgTypes = {}
	fileList = glob(BG_OUTPOUT_TYPE_SUM + "/*")
	for f in fileList : 
		filename = os.path.basename(f).split(".")[0]
		types = filename.split("_")
		if types[0] not in bgTypes:
			bgTypes[types[0]] = {}
		bgTypes[types[0]][types[1]] = True

	print bgTypes

	for bgType in bgTypes:
		if existsInCoumpoundType(bgType):
			continue
		print "Summing type", bgType
		rootfiles = glob(BG_OUTPOUT_TYPE_SUM + "/*" + bgType + "*.root")
		createPlots(rootfiles, bgType)
	for cType in COMPOUND_TYPES:
		print "Creating compound type", cType
		rootFiles = getCompoundTypeFiles(cType)
		if len(rootFiles):
			createPlots(rootFiles, cType)
		
		
print "Stack " + str(stack)

if stack or all:
	print "Creating Stacks."
	rtstacks___ = TFile(BG_OUTPOUT_STACK + "/stacked_histograms.root",'recreate')
	rootfiles = utils.orderBgFiles(glob(BG_OUTPOUT_PROCESSED + "/*"))
	files = []
	for i,file in enumerate(rootfiles):
		files.append(TFile(rootfiles[i]))
		
	keys = files[0].GetListOfKeys()
	for key in keys:
		name = key.GetName()#histogram name
		print "Creating " + name
		hs = THStack(name,"");
		filename = os.path.basename(rootfiles[0]).split(".")[0]
		h = files[0].Get(name)
		h.SetDirectory(0)
		h.SetName(filename)
		hs.Add(h)
		for i, fname in enumerate(rootfiles[1:]):
			filename = os.path.basename(fname).split(".")[0]
			h = files[i+1].Get(name)
			h.SetDirectory(0)
			h.SetName(filename)
			hs.Add(h)
		rtstacks___.cd()
		hs.Write()
	rtstacks___.Close()
	for f in files:
		f.Close()
	
exit(0)
