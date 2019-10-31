#!/usr/bin/env python

from ROOT import *
from glob import glob
from math import *
from sys import exit
from array import array
import argparse
import sys
import numpy as np
import os

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes"))

from lib import utils
from lib import analysis_ntuples
from lib import analysis_tools

gSystem.Load('LumiSectMap_C')
from ROOT import LumiSectMap

gSystem.Load('LeptonCollectionMap_C')
from ROOT import LeptonCollectionMap
from ROOT import LeptonCollectionFilesMap
from ROOT import LeptonCollection


gROOT.SetBatch(1)

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Split tracks into signal and background trees.')
parser.add_argument('-i', '--input_file', nargs=1, help='Input Filename', required=True)
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
args = parser.parse_args()

input_file = None
output_file = None
if args.input_file:
    input_file = args.input_file[0]
if args.output_file:
    output_file = args.output_file[0]

######## END OF CMDLINE ARGUMENTS ########

def main():

    tracksVars = (
        {"name":"dxyVtx", "type":"D"},
        {"name":"dzVtx", "type":"D"},
        {"name":"chi2perNdof", "type":"D"},
        {"name":"trkMiniRelIso", "type":"D"},
        {"name":"trkRelIso", "type":"D"},
    )

    otherVars = (
        {"name":"track", "type2":'TLorentzVector'},
        {"name":"deltaEtaLL", "type":"D"},
        {"name":"deltaEtaLJ", "type":"D"},
        {"name":"deltaRLL", "type":"D"},
        {"name":"deltaRLJ", "type":"D"}	
    )

    vars = otherVars + tracksVars

    varsDict = {}
    for i,v in enumerate(vars):
        varsDict[v["name"]] = i

    utils.addMemToTreeVarsDef(vars)

    tSig = TTree('tEvent','tEvent')
    utils.barchTreeFromVarsDef(tSig, vars)
    tBg = TTree('tEvent','tEvent')
    utils.barchTreeFromVarsDef(tBg, vars)

    c = TChain('tEvent')
    print "Going to open the file"
    print input_file
    c.Add(input_file)

    nentries = c.GetEntries()
    print 'Analysing', nentries, "entries"
    afterAtLeastOneReco = 0
    notCorrect = 0
    noReco = 0
    clean = 0
    sigTrack = 0
    appEvents = 0
    for ientry in range(nentries):
        if ientry % 5000 == 0:
            print "Processing " + str(ientry)
        c.GetEntry(ientry)
        rightProcess = analysis_ntuples.isX1X2X1Process(c)
        if not rightProcess:
            print "No"
            notCorrect += 1
            continue
        #print "Size Reco="
        #print str(len(c.Electrons) + len(c.Muons))
        if c.Electrons.size() + c.Muons.size() < 1:
            #print "No reco"
            noReco += 1
            continue
        afterAtLeastOneReco += 1
        genZL, genNonZL = analysis_ntuples.classifyGenZLeptons(c)
        if genZL is None or len(genZL) == 0:
            #print "genZL is None"
            continue
        #if len(genNonZL) == 0:
            #print "genNonZL is None"
        if len(genZL) != 2:
            print "What:", len(genZL)
    
        ll = analysis_ntuples.leadingLepton(c)
        appEvent = False
        for ti in range(c.tracks.size()):
            if c.tracks_trkRelIso[ti] > 0.1:
                continue 
            if c.tracks_dxyVtx[ti] > 0.02:
                continue
            if c.tracks_dzVtx[ti] > 0.05:
                continue

            t = c.tracks[ti]
            elecMin = analysis_tools.minDeltaR(t, c.Electrons)
            muonMin = analysis_tools.minDeltaR(t, c.Muons)
            if (elecMin is not None and elecMin < 0.1) or (muonMin is not None and muonMin < 0.1):
                continue
            clean += 1
            minZ, minCanZ = analysis_ntuples.minDeltaRGenParticles(t, genZL, c)
            minNZ, minCanNZ = analysis_ntuples.minDeltaRGenParticles(t, genNonZL, c)
        
            #if minNZ is None:
            #	print "minNZ is None for " + str(genNonZL)
            
            min = None
            if minNZ is None or minZ < minNZ:
                min = minZ
            else:
                min = minNZ
        
            result = ""
        
            if min > 0.1:
                result = "MM"
            elif minNZ is None or minZ < minNZ:
                if c.tracks_charge[ti] * c.GenParticles_PdgId[minCanZ] < 0:
                    result = "Zl"
                    #print "Found!"
                else:
                    result = "MM"
            else:
                result = "MM"
        
            vars[varsDict["track"]]["var"] = t
            for j, v in enumerate(tracksVars):
                i = len(otherVars) + j
                vars[i]["var"][0] = eval("c.tracks_" + vars[i]["name"] + "[" + str(ti) + "]")
            if ll is not None:
                vars[varsDict["deltaEtaLL"]]["var"][0] = abs(t.Eta()-ll.Eta()) 
                vars[varsDict["deltaRLL"]]["var"][0] = abs(t.DeltaR(ll))
            else:
                vars[varsDict["deltaEtaLL"]]["var"][0] = -1 
                vars[varsDict["deltaRLL"]]["var"][0] = -1
            vars[varsDict["deltaEtaLJ"]]["var"][0] = abs(t.Eta() - c.LeadingJet.Eta())
            vars[varsDict["deltaRLJ"]]["var"][0] = abs(t.DeltaR(c.LeadingJet))
        
            tree = None
            if result == "Zl":
                tree = tSig
                sigTrack += 1
                appEvent = True
                #print "Pt=" + str(vars[varsDict["track"]]["var"].Pt())
            else:
                tree = tBg
        
            tree.SetBranchAddress('track', vars[varsDict["track"]]["var"])
            tree.Fill()
        if appEvent:
            appEvents += 1

    print "notCorrect=" + str(notCorrect)
    print "afterAtLeastOneReco=" + str(afterAtLeastOneReco)
    print "clean=" + str(clean)
    print "noReco=" + str(noReco)
    print "sigTrack=" + str(sigTrack)
    print "appEvents=" + str(appEvents)

    fnew = TFile(output_file + "_sig.root",'recreate')
    tSig.Write()
    fnew.Close()

    fnew = TFile(output_file + "_bg.root",'recreate')
    tBg.Write()
    fnew.Close()
        
main()
exit(0)



