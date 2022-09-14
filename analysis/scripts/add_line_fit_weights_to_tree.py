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
parser.add_argument('-i', '--input_file', nargs=1, help='Input Directory', required=True)
parser.add_argument('-f', '--force', dest='force', help='Force Update', action='store_true')
#parser.add_argument('-data', '--data', dest='data', help='data', action='store_true')
#parser.add_argument('-sam', '--sam', dest='sam', help='Sam Samples', action='store_true')
args = parser.parse_args()

input_file = args.input_file[0]
force = args.force
#sam = args.sam
#data = args.data
######## END OF CMDLINE ARGUMENTS ########

# NO.   NAME      VALUE            ERROR          SIZE      DERIVATIVE 
#    1  p0           1.11418e+00   9.20848e-02   8.82279e-05  -2.51672e-11
#    2  p1           1.76377e-01   2.07421e-01   1.98733e-04   0.00000e+00

# NEW BINNING

#   NO.   NAME      VALUE            ERROR          SIZE      DERIVATIVE 
#    1  p0           1.11327e+00   9.24861e-02   9.61610e-05   4.61818e-11
#    2  p1           1.79169e-01   2.08616e-01   2.16905e-04  -1.02369e-11

def funcBackground(x,par):
    return par[0]+par[1]*x[0]

fLine = TF1('fLine', funcBackground, -1, 1, 2)
fLine.SetParameter(0, 1.114)
fLine.SetParameter(1, 0.176)

fLineSigmaM = TF1('fLineSigmaM', funcBackground, -1, 1, 2)
fLineSigmaM.SetParameter(0, 1.114)
fLineSigmaM.SetParameter(1, 0.383)

fLineSigmaB = TF1('fLineSigmaB', funcBackground, -1, 1, 2)
fLineSigmaB.SetParameter(0, 1.206)
fLineSigmaB.SetParameter(1, 0.176)

# print("fLine.Eval(0)", fLine.Eval(0))
# print("fLine.Eval(1)", fLine.Eval(1))
# print("fLine.Eval(2)", fLine.Eval(2))

newObservableStrs = ["muonsClosureLineFitWeight", "muonsClosureLineFitSigmaMWeight", "muonsClosureLineFitSigmaBWeight"]
wantedIso = "CorrJetNoMultIso10Dr0.6"

fileList = [input_file]

for filename in fileList:
    if os.path.isdir(filename): continue
    print "processing file " + filename
    f = TFile(filename, "update")
    
    t = f.Get("tEvent")
    
    shouldSkipTree = False
    rewriteTree = False
    
    for iso in utils.leptonIsolationList:
        for cat in utils.leptonIsolationCategories:
            ptRanges = [""]
            drCuts = [""]
            if iso in ["CorrJetIso", "CorrJetNoMultIso"]:
                ptRanges = utils.leptonCorrJetIsoPtRange
                drCuts = utils.leptonCorrJetIsoDrCuts
            for ptRange in ptRanges:
                for drCut in drCuts:
                    cuts = ""
                    if len(str(ptRange)) > 0:
                        cuts = str(ptRange) + "Dr" + str(drCut)
                    if (iso + cuts + cat) != wantedIso:
                        continue
                    postfixi = [iso + cuts + cat]
                    if iso + cuts + cat == utils.defaultJetIsoSetting:
                        postfixi = [iso + cuts + cat, ""]
                    for postfix in postfixi:
                        obsStr = newObservableStrs[0] + postfix
                        if t.GetBranchStatus(obsStr):
                            if not force:
                                print "Tree", filename ,"already has", obsStr, "! Skipping..."
                                shouldSkipTree = True
                            else:
                                rewriteTree = True
                            break
    
          
    if shouldSkipTree:
        f.Close()
        continue

    nentries = t.GetEntries();
    
    obsMem = {}
    branches = {}
    
    print 'Analysing', nentries, "entries"
    
    for ientry in range(nentries):
        if ientry % 1000 == 0:
            print "Processing " + str(ientry) + " out of " + str(nentries)
        t.GetEntry(ientry)
        
        for iso in utils.leptonIsolationList:
            for cat in utils.leptonIsolationCategories:
                ptRanges = [""]
                drCuts = [""]
                if iso in ["CorrJetIso", "CorrJetNoMultIso"]:
                    ptRanges = utils.leptonCorrJetIsoPtRange
                    drCuts = utils.leptonCorrJetIsoDrCuts
                for ptRange in ptRanges:
                    for drCut in drCuts:
                        cuts = ""
                        if len(str(ptRange)) > 0:
                            cuts = str(ptRange) + "Dr" + str(drCut)
                        postfixi = [iso + cuts + cat]
                        if (iso + cuts + cat) != wantedIso:
                            continue
                        if iso + cuts + cat == utils.defaultJetIsoSetting:
                            postfixi = [iso + cuts + cat, ""]
                        for postfix in postfixi:
                            
                            for newObservableStr in newObservableStrs:
                            
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

                                if getattr(t, "twoLeptons"  + postfix) == 1 and getattr(t, "leptons"  + postfix).size() == 2 and getattr(t, "leptonFlavour"  + postfix) == "Muons" and getattr(t, "isoCr"  + postfix) >= 1:
                                    #met = TLorentzVector()
                                    #met.SetPtEtaPhiE(t.MET,0,t.METPhi,t.MET)

                                    dilepBDT = getattr(t, "dilepBDT"  + postfix)
                                    if newObservableStr == "muonsClosureLineFitWeight":
                                        obsMem[obsStr][0] = fLine.Eval(dilepBDT)
                                    elif newObservableStr == "muonsClosureLineFitSigmaMWeight":
                                        #print "calculating for fLineSigmaM", dilepBDT, " by hand ", 1.114 + 0.383*dilepBDT, " eval ", fLineSigmaM.Eval(dilepBDT)
                                        obsMem[obsStr][0] = fLineSigmaM.Eval(dilepBDT)
                                    elif newObservableStr == "muonsClosureLineFitSigmaBWeight":
                                        obsMem[obsStr][0] = fLineSigmaB.Eval(dilepBDT)
                                else:
                                    obsMem[obsStr][0] = 1
                                    #print "NOT TWO LEPTONS", "twoLeptons"  + postfix, getattr(t, "twoLeptons"  + postfix), getattr(t, "leptons"  + postfix).size()
                                    #obsMem[obsStr][0] = -2
                                branches[obsStr].Fill()
   
    t.Write("tEvent",TObject.kOverwrite)
    print "Done"
    f.Close()


    
