#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
from array import array
import argparse
import sys
import os

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Run TMVA.')
parser.add_argument('-i', '--input_dir', nargs=1, help='Input Directory', required=True)
args = parser.parse_args()


input_dir = args.input_dir[0]
######## END OF CMDLINE ARGUMENTS ########

gROOT.SetBatch(1)
#print "input_dir:", input_dir
bFileNames =  glob(input_dir + "/*");
#print bFileNames
origNumberOfEvents = 0
origWeightedNumberOfEvents = 0
count = 0
weightedCount = 0
for f in bFileNames:
    #print "going to open ", f
    rootFile = TFile(f, "read")
    #h = rootFile.Get("hHt")
    #oN = h.Integral(-1,99999999)+0.000000000001
    #origNumberOfEvents += oN
    t = rootFile.Get("tEvent")
    #t = rootFile.Get("TreeMaker2/PreSelection")
    c = t.GetEntries()
    print os.path.basename(f), c
    count += c
    #t.GetEntry(0)
    #weight = t.Weight
    #weightedCount += weight * c
    #origWeightedNumberOfEvents += oN * weight
    rootFile.Close()

#print "origNumberOfEvents", origNumberOfEvents
#print "origWeightedNumberOfEvents", origWeightedNumberOfEvents
print "count", count
print "weightedCount", weightedCount