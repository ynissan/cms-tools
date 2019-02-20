#!/usr/bin/env python

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
	
WORK_DIR = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/single"
	
sumTypes = {}
totals = {}

def main():
	print "Going over skims."
	fileList = glob(WORK_DIR + "/*");
	for f in fileList :
		filename = os.path.basename(f).split(".")[1]
		types = filename.split("_")
		type = types[0]
		if type not in sumTypes:
			sumTypes[type] = {}

		if type == "DYJetsToLL":
			sumTypes[type][types[2]] = True
		else:
			sumTypes[type][types[1]] = True

	print sumTypes 
	emptyFiles = {}
	for type in sumTypes:
		print type
		if type not in totals:
			totals[type] = {}
		for typeRange in sumTypes[type]:
			print "-------------------------------"
			print "Summing " + type + "_" + typeRange
			files = None
			if type == "DYJetsToLL":
				files = WORK_DIR  + "/Summer16." + type + "_*" + typeRange + "*.root"
			else:
				files = WORK_DIR  + "/Summer16." + type + "_" + typeRange + "*.root"
			
			fileList = glob(files)
			total = 0
			for f in fileList:
				print "Checking file: " + f
				rootFile = TFile(f)
				HT = rootFile.Get("hHt").Clone()
				numOfEvents = HT.Integral(-1,99999999)+0.000000000001
				print "numOfEvents: " , numOfEvents
				total += numOfEvents
				t = rootFile.Get("tEvent")
				if t.GetEntries() == 0:
					print "Empty File: " + f
					emptyFiles[f] = True
			print "total: ", total
			totals[type][typeRange] = total
	print totals
	for type in sumTypes:
		print type
		if type not in totals:
			totals[type] = {}
		for typeRange in sumTypes[type]:
			print "-------------------------------"
			print "Summing " + type + "_" + typeRange
			files = None
			if type == "DYJetsToLL":
				files = WORK_DIR  + "/Summer16." + type + "_*" + typeRange + "*.root"
			else:
				files = WORK_DIR  + "/Summer16." + type + "_" + typeRange + "*.root"
			
			fileList = glob(files)
			for f in fileList:
				if emptyFiles.get(f) is not None:
					print "Skipping empty file ", f
					continue
				print "processing file " + f 
				rootFile = TFile(f, "update")
				t = rootFile.Get("tEvent")
				t.GetEntry(0)
				cs = t.CrossSection
				print "CrossSection:", cs
				numOfEvents = totals[type][typeRange]
				print "Total:", numOfEvents
				weight = (utils.LUMINOSITY * cs)/numOfEvents
				print "weight:", weight
				var_Weight = np.zeros(1,dtype=float)
				var_Weight[0] = weight
				nentries = t.GetEntries();
				if t.GetBranchStatus("Weight"):
					print "This tree is already weighted! Skipping..."
					rootFile.Close()
					continue
		
				newBranch = t.Branch("Weight",var_Weight,"Weight/D");
				for ientry in range(nentries):
					newBranch.Fill()
				print "Writing Tree"
				t.Write("tEvent",TObject.kOverwrite)
				print "Done"
				rootFile.Close()
	print "Empty Files:"
	print emptyFiles
	print "Deleting Empty files."
	for f in emptyFiles:
		print "Deleting ", f
		os.remove(f)

main()
exit(0)

