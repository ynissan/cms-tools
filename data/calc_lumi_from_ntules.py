#!/usr/bin/env python

from ROOT import *
from glob import glob
import sys
import os

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes"))
import utils

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

gSystem.Load('LumiSectMap_C')
from ROOT import LumiSectMap

####### CMDLINE ARGUMENTS #########

lumiSecs = LumiSectMap()

#data_files = glob("/pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/ProductionRun2v*/Run2016B*MET*")
#data_files = glob("/afs/desy.de/user/n/nissanuv/ntupleHub/SlimmedProduction/Run201[78]*MET*")
#data_files = glob("/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/tmp/*")
#data_files = glob("/afs/desy.de/user/n/nissanuv/ntupleHub/SlimmedProduction/Run2018D*MET*")
data_files = glob("/tmp/tmp.root")
print len(data_files), "Files"
i=0
    
for f in data_files:
    i+=1
    print "***"
    print i, "/", len(data_files)
    print "***"
    c = TChain('TreeMaker2/PreSelection')
    #c = TChain('tEvent')
    c.Add(f)
    
    nentries = c.GetEntries()
    print 'Analysing', nentries, "entries"
    
    for ientry in range(nentries):
        if ientry % 10000 == 0:
            print "Processing " + str(ientry)
        c.GetEntry(ientry)
        lumiSecs.insert(c.RunNum, c.LumiBlockNum)

lumi = utils.calculateLumiFromLumiSecs(lumiSecs)
print "Luminosity=", lumi