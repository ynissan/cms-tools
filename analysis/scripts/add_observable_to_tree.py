#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import numpy as np
import argparse
import sys
import os

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes"))
from lib import analysis_ntuples
from lib import analysis_tools
from lib import utils
from lib import analysis_observables

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Weight skims for x1x2x1 process.')
parser.add_argument('-i', '--input_dir', nargs=1, help='Input Directory', required=True)
parser.add_argument('-f', '--force', dest='force', help='Force Update', action='store_true')
#parser.add_argument('-data', '--data', dest='data', help='data', action='store_true')
#parser.add_argument('-sam', '--sam', dest='sam', help='Sam Samples', action='store_true')
args = parser.parse_args()

input_dir = args.input_dir[0]
force = args.force
#sam = args.sam
#data = args.data
######## END OF CMDLINE ARGUMENTS ########

newObservableStr = "nmtautau"

fileList = glob(input_dir + "/*");
for filename in fileList:
    if os.path.isdir(filename): continue
    print "processing file " + filename
    f = TFile(filename, "update")
    
    t = f.Get("tEvent")
    
    shouldSkipTree = False
    rewriteTree = False
    
#     for iso in utils.leptonIsolationList:
#         for cat in utils.leptonIsolationCategories:
#             ptRanges = [""]
#             drCuts = [""]
#             if iso == "CorrJetIso":
#                 ptRanges = utils.leptonCorrJetIsoPtRange
#                 drCuts = utils.leptonCorrJetIsoDrCuts
#             for ptRange in ptRanges:
#                 for drCut in drCuts:
#                     cuts = ""
#                     if len(str(ptRange)) > 0:
#                         cuts = str(ptRange) + "Dr" + str(drCut)
#             
#                     postfixi = [iso + cuts + cat]
#                 
#                     if iso + str(ptRange) + cat == utils.defaultJetIsoSetting:
#                         postfixi = [iso + cuts + cat, ""]
#             
#                     for postfix in postfixi:
#                         obsStr = newObservableStr + postfix
#                         if t.GetBranchStatus(obsStr):
#                             if not force:
#                                 print "Tree", filename ,"already has", obsStr, "! Skipping..."
#                                 shouldSkipTree = True
#                             else:
#                                 rewriteTree = True
#                             break
#     if shouldSkipTree:
#         f.Close()
#         continue
    
    
    nentries = t.GetEntries();
    
    obsMem = {}
    branches = {}
    
    print 'Analysing', nentries, "entries"
    
    for ientry in range(nentries):
        if ientry % 1000 == 0:
            print "Processing " + str(ientry) + " out of " + str(nentries)
        t.GetEntry(ientry)
        
        
        postfix = "CorrJetIso10.5Dr0.55"
        
        # for iso in utils.leptonIsolationList:
#             for cat in utils.leptonIsolationCategories:
#                 ptRanges = [""]
#                 drCuts = [""]
#                 if iso == "CorrJetIso":
#                     ptRanges = utils.leptonCorrJetIsoPtRange
#                     drCuts = utils.leptonCorrJetIsoDrCuts
#                 for ptRange in ptRanges:
#                     for drCut in drCuts:
#                         cuts = ""
#                         if len(str(ptRange)) > 0:
#                             cuts = str(ptRange) + "Dr" + str(drCut)
#                 
#                         postfixi = [iso + cuts + cat]
#                     
#                         if iso + str(ptRange) + cat == utils.defaultJetIsoSetting:
#                             postfixi = [iso + cuts + cat, ""]
#                 
#                         for postfix in postfixi:
#                             
        obsStr = newObservableStr + postfix
        if obsMem.get(obsStr) is None:
            obsMem[obsStr] = np.zeros(1,dtype=float)
            
            if t.GetBranchStatus(obsStr):
                print "Restting branch", obsStr
                branch = t.GetBranch(obsStr)
                branch.Reset()
                branch.SetAddress(obsMem[obsStr])
                branches[obsStr] = branch
            else:
                branch = t.Branch(obsStr,obsMem[obsStr],obsStr+"/D");
                branches[obsStr] = branch
        
        if getattr(t, "twoLeptons"  + postfix) == 1 and getattr(t, "leptons"  + postfix).size() == 2:
            met = TLorentzVector()
            met.SetPtEtaPhiE(t.MET,0,t.METPhi,t.MET)

            l1 = getattr(t, "leptons"  + postfix)[0]
            l2 = getattr(t, "leptons"  + postfix)[1]
            #Mtautau(pt, l1, l2)
            obsMem[obsStr][0] = analysis_tools.Mtautau2(met, l1, l2)
            #obsMem[obsStr][0] = analysis_tools.PreciseMtautau(t.MET, t.METPhi, getattr(t, "leptons"  + postfix)[0], getattr(t, "leptons"  + postfix)[1])
        else:
            #print "NOT TWO LEPTONS", "twoLeptons"  + postfix, getattr(t, "twoLeptons"  + postfix), getattr(t, "leptons"  + postfix).size()
            obsMem[obsStr][0] = -2
        branches[obsStr].Fill()
   
    t.Write("tEvent",TObject.kOverwrite)
    print "Done"
    f.Close()


    
