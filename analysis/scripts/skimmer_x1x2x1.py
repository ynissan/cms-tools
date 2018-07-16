#!/usr/bin/python

from ROOT import *
from glob import glob
from math import *
from sys import exit
from array import array
import argparse
import sys
import numpy as np

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import histograms
from lib import utils
from lib import cuts
from lib import analysis_ntuples
from lib import analysis_tools

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Create skims for x1x2x1 process.')
parser.add_argument('-i', '--input_file', nargs=1, help='Input Filename', required=False)
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
parser.add_argument('-madHTgt', '--madHTgt', nargs=1, help='madHT lower bound', required=False)
parser.add_argument('-madHTlt', '--madHTlt', nargs=1, help='madHT uppper bound', required=False)

parser.add_argument('-s', '--signal', dest='signal', help='Signal', action='store_true')
parser.add_argument('-bg', '--background', dest='bg', help='Background', action='store_true')
args = parser.parse_args()

madHTgt = None
madHTlt = None
if args.madHTgt:
	madHTgt = int(args.madHTgt[0])
	print "Got madHT lower bound of " + str(madHTgt)
if args.madHTlt:
	madHTlt = int(args.madHTlt[0])
	print "Got madHT upper bound of " + str(madHTlt)
	

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
	
######## END OF CMDLINE ARGUMENTS ########

fnew = TFile(output_file,'recreate')

hHt = TH1F('hHt','hHt',100,0,3000)
hHt.Sumw2()
#hHtWeighted = TH1F('hHtWeighted','hHtWeighted',100,0,3000).Sumw2()

var_Met = np.zeros(1,dtype=float)

tEvent = TTree('tEvent','tEvent')
tEvent.Branch('Met', var_Met,'Met/D')

c = TChain('TreeMaker2/PreSelection')
c.Add(input_file)

nentries = c.GetEntries()
print 'Analysing', nentries, "entries"

for ientry in range(nentries):
	c.GetEntry(ientry)
	var_Met[0] = c.MET
	hHt.Fill(c.madHT)
	tEvent.Fill()

fnew.cd()
tEvent.Write()
print 'just created', fnew.GetName()
hHt.Write()
#hHtWeighted.Write()
fnew.Close()
