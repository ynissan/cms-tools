#!/cvmfs/cms.cern.ch/slc6_amd64_gcc530/cms/cmssw-patch/CMSSW_8_0_5_patch1/external/slc6_amd64_gcc530/bin/python2.7

from ROOT import *
from math import *
from sys import exit
import numpy as np
import os
import argparse

parser = argparse.ArgumentParser(description='Create histograms for x1x2x1 process.')
parser.add_argument('-i', '--input_file', nargs=1, help='Input Filename', required=True)
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=True)

args = parser.parse_args()

input_file = None
if args.input_file:
	input_file = args.input_file[0]
output_file = None
if args.output_file:
	output_file = args.output_file[0]
	
