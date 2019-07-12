#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import numpy as np
import os

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools/lib/classes")
from lib import analysis_ntuples
from lib import analysis_tools
from lib import utils

gSystem.Load('LumiSectMap_C')
from ROOT import LumiSectMap

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Create skims for x1x2x1 process.')
parser.add_argument('-i', '--input_file', nargs=1, help='Input Filename', required=False)
args = parser.parse_args()

print args

input_file = None
if args.input_file:
    input_file = args.input_file[0]
    
def main():
    iFile = TFile(input_file)
    #hHt = iFile.Get('hHt')
    lumiSecs = iFile.Get('lumiSecs')
    print lumiSecs
    lumiMap = lumiSecs.getMap()
    for k, v in lumiMap:
        for a in v: 
            print "Key: " + str(k) + " Val: " + str(a)
main()
