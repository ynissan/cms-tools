#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import os
import re
from datetime import datetime

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes"))
import utils

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

gSystem.Load('LumiSectMap_C')
from ROOT import LumiSectMap

#lumi = 5746.370
#weight = lumi / utils.LUMINOSITY

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Calculate Luminosity.')
parser.add_argument('-i', '--input_dir', nargs=1, help='Input Directory', required=True)
args = parser.parse_args()

input_dir = None

if args.input_dir:
    input_dir = args.input_dir[0]

lumi = utils.get_lumi_from_bril('~/tmp_json_1613859532.json', 'ynissan')
    #os.remove(tmpJsonFile)
print "Luminosity=", lumi
exit(0)

lumiSecs = LumiSectMap()

data_files = glob(input_dir + "/*")
    
for f in data_files: 
    print f
    rootFile = TFile(f)
    if rootFile.GetListOfKeys().Contains("lumiSecs"):
        lumis = rootFile.Get('lumiSecs')
        col = TList()
        col.Add(lumis)
        lumiSecs.Merge(col)
    else:
        print "Bad file", f
        os.remove(f)
    rootFile.Close()

lumi = utils.calculateLumiFromLumiSecs(lumiSecs)
print "Luminosity=", lumi