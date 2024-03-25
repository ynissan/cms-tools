#!/usr/bin/env python3.8

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import numpy as np
import os
import cppyy
import itertools
from datetime import datetime

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib/classes"))
from lib import analysis_ntuples
from lib import analysis_tools
from lib import utils
from lib import analysis_observables

parser = argparse.ArgumentParser(description='Sum signal files.')
parser.add_argument('-f', '--force', dest='force', help='Force Update', action='store_true')
parser.add_argument('-sam', '--sam', dest='sam', help='Sam Skims', action='store_true')
parser.add_argument('-nlp', '--no_lepton_selection', dest='no_lepton_selection', help='No Lepton Selection Skim', action='store_true')
parser.add_argument('-phase1', '--phase1', dest='phase1', help='Phase 1', action='store_true')
args = parser.parse_args()

force = args.force
sam = args.sam
no_lepton_selection = args.no_lepton_selection
phase1 = args.phase1

signal_dir = "/afs/desy.de/user/d/diepholq/nfs/x1x2x1/signal/skim/single"

if no_lepton_selection:
    signal_dir = "/afs/desy.de/user/d/diepholq/nfs/x1x2x1/signal/skim_nlp/single"
elif phase1:
    signal_dir = "/afs/desy.de/user/d/diepholq/nfs/x1x2x1/signal/skim_phase1/single"


def main():
    points = {}
    
    fileList = glob(signal_dir + "/*");

    for fileName in fileList:
        point = None
        if sam:
            point = "_".join(os.path.basename(fileName).split("_")[2:4])
        else:
            #Example: higgsino_Summer16_stopstop_600GeV_mChipm200GeV_dm1p0GeV_pu35_part6of25_RA2AnalysisTree.root
            point = "_".join(os.path.basename(fileName).split("_")[3:6])
        if points.get(point) is None:
            print("New Point", point)
            points[point] = 0
        
        f = TFile(fileName, "read")
        print("Summing", os.path.basename(fileName))
        h = f.Get("hHt")
        numOfEvents = h.Integral(-1,99999999)
        #print(os.path.basename(fileName), "numOfEvents", numOfEvents)
        points[point] += numOfEvents
        f.Close()
        
    print("\n\n\n")
    print(points)
    print("\n\n\n")
    
    for fileName in fileList:
        print("Weighting", os.path.basename(fileName))
        point = None
        if sam:
            point = "_".join(os.path.basename(fileName).split("_")[2:4])
        else:
            point = "_".join(os.path.basename(fileName).split("_")[3:6])
        f = TFile(fileName, "update")
        t = f.Get("tEvent")
        t.GetEntry(0)
        numOfEvents = points[point]
        print("numOfEvents:", numOfEvents)
        cs = t.CrossSection
        print("CrossSection:", cs)
        weight = cs/numOfEvents
        print("weight:", weight)

        var_Weight = np.zeros(1,dtype=float)
        var_Weight[0] = weight
        nentries = t.GetEntries();
        if t.GetBranchStatus("Weight"):
            if not force:
                print("This tree is already weighted! Skipping...")
            else:
                branch = t.GetBranch("Weight")
                branch.Reset()
                branch.SetAddress(var_Weight)
                for ientry in range(nentries):
                    branch.Fill()
                t.Write("tEvent",TObject.kOverwrite)
                print("Done")
            f.Close()
            continue

        newBranch = t.Branch("Weight",var_Weight,"Weight/D");
        for ientry in range(nentries):
            newBranch.Fill()
        print("Writing Tree")
        t.Write("tEvent",TObject.kOverwrite)
        print("Done")
        f.Close()
    
main()
exit(0)
