#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import numpy as np
import os
import xml.etree.ElementTree as ET

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import analysis_ntuples
from lib import analysis_tools
from lib import utils
from lib import cut_optimisation

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Create skims for x1x2x1 process with BDTs.')
parser.add_argument('-i', '--input_file', nargs=1, help='Input Filename', required=True)
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=True)
parser.add_argument('-bdt', '--bdt', nargs=1, help='Dilepton BDT Folder', required=True)

parser.add_argument('-s', '--signal', dest='signal', help='Signal', action='store_true')
parser.add_argument('-bg', '--background', dest='bg', help='Background', action='store_true')
args = parser.parse_args()
	

signal = args.signal
bg = args.bg

input_file = None
if args.input_file:
	input_file = args.input_file[0]
output_file = None
if args.output_file:
	output_file = args.output_file[0]

if (bg and signal) or not (bg or signal):
	signal = True
	bg = False
	
univ_bdt = None
if args.bdt:
	univ_bdt = args.bdt[0]
	
######## END OF CMDLINE ARGUMENTS ########


def main():
	iFile = TFile(input_file)
	hHt = iFile.Get('hHt')
	c = iFile.Get('tEvent')
	
	tree = c.CloneTree(0)
	tree.SetDirectory(0)

	nentries = c.GetEntries()
	print 'Analysing', nentries, "entries"
	
	(univ_testBGHists, univ_trainBGHists, univ_testSignalHists, univ_trainSignalHists, univ_methods, univ_names) = cut_optimisation.get_bdt_hists([univ_bdt])
	univ_trainSignalHist, univ_trainBGHist, univ_testSignalHist, univ_testBGHist = univ_trainSignalHists[0], univ_trainBGHists[0], univ_testSignalHists[0], univ_testBGHists[0]
	univ_highestZ, univ_highestS, univ_highestB, univ_highestMVA, univ_ST, univ_BT = cut_optimisation.getHighestZ(univ_trainSignalHist, univ_trainBGHist, univ_testSignalHist, univ_testBGHist)
	
	univ_bdt_weights = univ_bdt + "/dataset/weights/TMVAClassification_BDT.weights.xml"
	univ_bdt_vars = cut_optimisation.getVariablesFromXMLWeightsFile(univ_bdt_weights)
	univ_bdt_vars_map = cut_optimisation.getVariablesMemMap(univ_bdt_vars)
	univ_bdt_reader = cut_optimisation.prepareReader(univ_bdt_weights, univ_bdt_vars, univ_bdt_vars_map)
	
	print "-------------------"
	
	print "univ_highestZ=" + str(univ_highestZ)
	print "univ_highestS=" + str(univ_highestS)
	print "univ_highestB=" + str(univ_highestB)
	print "univ_highestMVA=" + str(univ_highestMVA)
	print "univ_ST=" + str(univ_ST)
	print "univ_BT=" + str(univ_BT)
	
	print "-------------------"
	
	for ientry in range(nentries):
		if ientry % 1000 == 0:
			print "Processing " + str(ientry)
		c.GetEntry(ientry)
		
		for k, v in univ_bdt_vars_map.items():
			v[0] = eval("c." + k)
		univ_tmva_value = univ_bdt_reader.EvaluateMVA("BDT")
		if univ_tmva_value < univ_highestMVA:
			continue

		tree.Fill()
	
	if tree.GetEntries() != 0:
		fnew = TFile(output_file,'recreate')
		tree.Write()
		hHt.Write()
		fnew.Close()
	else:
		print "*** RESULT EMPTY"
	iFile.Close()

main()