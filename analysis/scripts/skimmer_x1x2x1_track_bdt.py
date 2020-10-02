#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import numpy as np
import os
import xml.etree.ElementTree as ET
from math import *

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes"))
from lib import analysis_ntuples
from lib import analysis_tools
from lib import utils
from lib import cut_optimisation

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

gSystem.Load('LumiSectMap_C')
from ROOT import LumiSectMap

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Create skims for x1x2x1 process with BDTs.')
parser.add_argument('-i', '--input_file', nargs=1, help='Input Filename', required=True)
parser.add_argument('-tb', '--track_bdt', nargs=1, help='Track BDT Folder', required=True)

parser.add_argument('-s', '--signal', dest='signal', help='Signal', action='store_true')
parser.add_argument('-bg', '--background', dest='bg', help='Background', action='store_true')
parser.add_argument('-sc', '--same_charge', dest='sc', help='Same Charge', action='store_true')
parser.add_argument('-dy', '--dy', dest='dy', help='Drell-Yan', action='store_true')
parser.add_argument('-sam', '--sam', dest='sam', help='Sam Samples', action='store_true')
args = parser.parse_args()


signal = args.signal
bg = args.bg
sc = args.sc

print "SAME CHARGE=", sc

input_file = None
if args.input_file:
    input_file = args.input_file[0].strip()

if (bg and signal) or not (bg or signal):
    signal = True
    bg = False

track_bdt = None
if args.track_bdt:
    track_bdt = args.track_bdt[0]

######## END OF CMDLINE ARGUMENTS ########

exTrackVars = {}
track_bdt_vars_maps = {}
track_bdt_specs_maps = {}
track_bdt_readers = {}
branches = {}


def fillInNonTrackInfo(c, iso, cat, ptRange):
    for stringObs in utils.exclusiveTrackObservablesStringList:
        exTrackVars[stringObs + iso + str(ptRange) + cat] = ROOT.std.string("")
        #print "*"
        #print branches[stringObs + iso + str(ptRange) + cat]
        #print "**"
        #print exTrackVars[stringObs + iso + str(ptRange) + cat]
        #branches[stringObs + iso + str(ptRange) + cat].ResetAddress()
        c.SetBranchAddress(stringObs + iso + str(ptRange) + cat, exTrackVars[stringObs + iso + str(ptRange) + cat])
        #branches[stringObs + iso + str(ptRange) + cat].SetAddress(exTrackVars[stringObs + iso + str(ptRange) + cat])
        #print "**"
        branches[stringObs + iso + str(ptRange) + cat].Fill()
        #print "***"
    for DTypeObs in utils.commonObservablesDTypesList:
        exTrackVars["exTrack_" + DTypeObs + iso + str(ptRange) + cat][0] = -1
        #print "****"
        branches["exTrack_" + DTypeObs + iso + str(ptRange) + cat].Fill()
        #print "*****"
    for DTypeObs in utils.exclusiveTrackObservablesDTypesList:
        if DTypeObs == "exclusiveTrack":
            exTrackVars[DTypeObs + iso + str(ptRange) + cat][0] = 0
            #print "******"
        else:
            exTrackVars[DTypeObs + iso + str(ptRange) + cat][0] = -1
            #print "******"
        branches[DTypeObs + iso + str(ptRange) + cat].Fill()         
        #print "*******"
    for CTypeObs in utils.exclusiveTrackObservablesClassList:
        exTrackVars[CTypeObs + iso + str(ptRange) + cat] = eval(utils.exclusiveTrackObservablesClassList[CTypeObs])()
        #print "********"
        c.SetBranchAddress(CTypeObs + iso + str(ptRange) + cat, exTrackVars[CTypeObs + iso + str(ptRange) + cat])
        #branches[CTypeObs + iso + str(ptRange) + cat].SetAddress(exTrackVars[CTypeObs + iso + str(ptRange) + cat])
        #print "*********"
        branches[CTypeObs + iso + str(ptRange) + cat].Fill()
        #print "**********"

def main():
    
    file = TFile(input_file, "update")
    
    c = file.Get("tEvent")
    nentries = c.GetEntriesFast()
    
    # CREATE VARS, BRANCHES, AND BDT READERS
    
    for iso in utils.leptonIsolationList:
        for cat in utils.leptonIsolationCategories:
            ptRanges = [""]
            if iso == "CorrJetIso":
                ptRanges = utils.leptonCorrJetIsoPtRange
            for ptRange in ptRanges:
                for stringObs in utils.exclusiveTrackObservablesStringList:
                    exTrackVars[stringObs + iso + str(ptRange) + cat] = ROOT.std.string("")
                    if c.GetBranchStatus(stringObs + iso + str(ptRange) + cat):
                        print "Reseting branch", stringObs + iso + str(ptRange) + cat
                        branches[stringObs + iso + str(ptRange) + cat] = c.GetBranch(stringObs + iso + str(ptRange) + cat)
                        branches[stringObs + iso + str(ptRange) + cat].Reset()
                        c.SetBranchAddress(stringObs + iso + str(ptRange) + cat, exTrackVars[stringObs + iso + str(ptRange) + cat])
                    else:
                        print "Branching", stringObs + iso + str(ptRange) + cat
                        branches[stringObs + iso + str(ptRange) + cat] = c.Branch(stringObs + iso + str(ptRange) + cat, 'std::string', exTrackVars[stringObs + iso + str(ptRange) + cat])
                        c.SetBranchAddress(stringObs + iso + str(ptRange) + cat, exTrackVars[stringObs + iso + str(ptRange) + cat])
                for DTypeObs in utils.commonObservablesDTypesList:
                    exTrackVars["exTrack_" + DTypeObs + iso + str(ptRange) + cat] = np.zeros(1,dtype=utils.commonObservablesDTypesList[DTypeObs])
                    if c.GetBranchStatus("exTrack_" + DTypeObs + iso + str(ptRange) + cat):
                        print "Reseting branch", "exTrack_" + DTypeObs + iso + str(ptRange) + cat
                        branches["exTrack_" + DTypeObs + iso + str(ptRange) + cat] = c.GetBranch("exTrack_" + DTypeObs + iso + str(ptRange) + cat)
                        branches["exTrack_" + DTypeObs + iso + str(ptRange) + cat].Reset()
                        c.SetBranchAddress("exTrack_" + DTypeObs + iso + str(ptRange) + cat, exTrackVars["exTrack_" + DTypeObs + iso + str(ptRange) + cat])
                        #branches["exTrack_" + DTypeObs + iso + str(ptRange) + cat].SetAddress(exTrackVars["exTrack_" + DTypeObs + iso + str(ptRange) + cat])
                    else:
                        print "Branching", "exTrack_" + DTypeObs + iso + str(ptRange) + cat
                        branches["exTrack_" + DTypeObs + iso + str(ptRange) + cat] = c.Branch("exTrack_" + DTypeObs + iso + str(ptRange) + cat, exTrackVars[stringObs + iso + str(ptRange) + cat], "exTrack_" + DTypeObs + iso + str(ptRange) + cat + "/" + utils.typeTranslation[utils.commonObservablesDTypesList[DTypeObs]])
                        c.SetBranchAddress("exTrack_" + DTypeObs + iso + str(ptRange) + cat, exTrackVars["exTrack_" + DTypeObs + iso + str(ptRange) + cat])
                for DTypeObs in utils.exclusiveTrackObservablesDTypesList:
                    exTrackVars[DTypeObs + iso + str(ptRange) + cat] = np.zeros(1,dtype=utils.exclusiveTrackObservablesDTypesList[DTypeObs])
                    if c.GetBranchStatus(DTypeObs + iso + str(ptRange) + cat):
                        print "Reseting branch", DTypeObs + iso + str(ptRange) + cat
                        branches[DTypeObs + iso + str(ptRange) + cat] = c.GetBranch(DTypeObs + iso + str(ptRange) + cat)
                        branches[DTypeObs + iso + str(ptRange) + cat].Reset()
                        c.SetBranchAddress(DTypeObs + iso + str(ptRange) + cat, exTrackVars[DTypeObs + iso + str(ptRange) + cat])
                        #branches[DTypeObs + iso + str(ptRange) + cat].SetAddress(exTrackVars[DTypeObs + iso + str(ptRange) + cat])
                    else:
                        print "Branching", DTypeObs + iso + str(ptRange) + cat
                        branches[DTypeObs + iso + str(ptRange) + cat] = c.Branch(DTypeObs + iso + str(ptRange) + cat, exTrackVars[DTypeObs + iso + str(ptRange) + cat], DTypeObs + iso + str(ptRange) + cat + "/" + utils.typeTranslation[utils.exclusiveTrackObservablesDTypesList[DTypeObs]])
                        c.SetBranchAddress(DTypeObs + iso + str(ptRange) + cat, exTrackVars[DTypeObs + iso + str(ptRange) + cat])
                for CTypeObs in utils.exclusiveTrackObservablesClassList:
                    exTrackVars[CTypeObs + iso + str(ptRange) + cat] = eval(utils.exclusiveTrackObservablesClassList[CTypeObs])()
                    if c.GetBranchStatus(CTypeObs + iso + str(ptRange) + cat):
                        print "Reseting branch", CTypeObs + iso + str(ptRange) + cat
                        branches[CTypeObs + iso + str(ptRange) + cat] = c.GetBranch(CTypeObs + iso + str(ptRange) + cat)
                        branches[CTypeObs + iso + str(ptRange) + cat].Reset()
                        c.SetBranchAddress(CTypeObs + iso + str(ptRange) + cat, exTrackVars[CTypeObs + iso + str(ptRange) + cat])
                    else:
                        print "Branching", CTypeObs + iso + str(ptRange) + cat
                        branches[CTypeObs + iso + str(ptRange) + cat] = c.Branch(CTypeObs + iso + str(ptRange) + cat, utils.exclusiveTrackObservablesClassList[CTypeObs], exTrackVars[CTypeObs + iso + str(ptRange) + cat])
                        c.SetBranchAddress(CTypeObs + iso + str(ptRange) + cat, exTrackVars[CTypeObs + iso + str(ptRange) + cat])
                    
                track_bdt_weights = track_bdt + "/dataset/weights/TMVAClassification_Muons" + iso + str(ptRange) + cat + ".weights.xml"
                track_bdt_vars = cut_optimisation.getVariablesFromXMLWeightsFile(track_bdt_weights)
                track_bdt_vars_map = cut_optimisation.getVariablesMemMap(track_bdt_vars)
                track_bdt_specs = cut_optimisation.getSpecSpectatorFromXMLWeightsFile(track_bdt_weights)
                track_bdt_specs_map = cut_optimisation.getSpectatorsMemMap(track_bdt_vars)
                track_bdt_reader = cut_optimisation.prepareReader(track_bdt_weights, track_bdt_vars, track_bdt_vars_map, track_bdt_specs, track_bdt_specs_map)

                track_bdt_vars_maps[iso + str(ptRange) + cat] = track_bdt_vars_map
                track_bdt_specs_maps[iso + str(ptRange) + cat] = track_bdt_specs_map
                track_bdt_readers[iso + str(ptRange) + cat] = track_bdt_reader

    print 'Analysing', nentries, "entries"

    afterMonoLepton = 0
    afterUniversalBdt = 0
    afterMonoTrack = 0
    afterAtLeastOneTrack = 0

    totalTracks = 0
    totalSurvivedTracks = 0
    eventsWithGreaterThanOneOppSignTracks = 0
    noSurvivingTracks = 0
    
    file.cd()
    
    for ientry in range(nentries):
        if ientry % 100 == 0:
            print "Processing " + str(ientry) + " out of " + str(nentries)
        c.GetEntry(ientry)
        
        for iso in utils.leptonIsolationList:
            for cat in utils.leptonIsolationCategories:
                ptRanges = [""]
                if iso == "CorrJetIso":
                    ptRanges = utils.leptonCorrJetIsoPtRange
                for ptRange in ptRanges:
                    exTrackVars["exclusiveTrack" + iso + str(ptRange) + cat][0] = 0
                    
                    ll, lepIdx, leptonCharge, leptonFlavour = analysis_ntuples.getSingleLeptonAfterSelection(c.Electrons, getattr(c, "Electrons_pass" + iso + str(ptRange)), c.Electrons_deltaRLJ, c.Electrons_charge, c.Muons, getattr(c, "Muons_pass" + iso + str(ptRange)), c.Muons_mediumID, c.Muons_deltaRLJ, c.Muons_charge, utils.leptonIsolationCategories[cat]["muonPt"], utils.leptonIsolationCategories[cat]["lowPtTightMuons"], c.Muons_tightID)
        
                    if ll is None:
                        # NOT TWO TRACKS
                        #print "**** BEFORE FILL ***" 
                        fillInNonTrackInfo(c, iso, cat, ptRange)
                        #print "**** AFTER FILL ***"
                        continue
                    
                    if leptonCharge == 0:
                        print "WHAT?! leptonCharge=0"
                    
                    exTrackVars["lepton_charge" + iso + str(ptRange) + cat][0] = leptonCharge
                    exTrackVars["exclusiveTrackLeptonFlavour" + iso + str(ptRange) + cat] = ROOT.std.string(leptonFlavour)
    
                    afterMonoLepton += 1
                    
                    exTrackVars["secondTrackBDT" + iso + str(ptRange) + cat][0] = -1
        
                    metvec = TLorentzVector()
                    metvec.SetPtEtaPhiE(c.Met, 0, c.METPhi, c.Met)
        
                    highestOppositeTrackScore = None
                    secondTrackScore = None
                    secondTrack = None
                    oppositeChargeTrack = None
                    ntracks = 0
                    for ti in range(c.tracks.size()):
                        t = c.tracks[ti]
                        if t.Pt() > 15:
                            continue
                        tcharge = c.tracks_charge[ti]
                        #Try lowering to 0!!
            
                        if c.tracks_trkRelIso[ti] > 0.1:
                            continue 
                        if c.tracks_dxyVtx[ti] > 0.02:
                            continue
                        if c.tracks_dzVtx[ti] > 0.05:
                            continue

                        if sc:
                            if tcharge * leptonCharge < 0:
                                continue
                        else:
                            if tcharge * leptonCharge > 0:
                                continue
            
                        totalTracks +=1
        
                        deltaRLL = abs(t.DeltaR(ll))
                        if deltaRLL < 0.01:
                            continue
                        ntracks += 1
      
                        track_bdt_vars_maps[iso + str(ptRange) + cat]["deltaEtaLJ"][0] = abs(t.Eta() - c.LeadingJet.Eta())
                        track_bdt_vars_maps[iso + str(ptRange) + cat]["deltaRLJ"][0] = abs(t.DeltaR(c.LeadingJet))
                        track_bdt_vars_maps[iso + str(ptRange) + cat]["track.Phi()"][0] = t.Phi()
                        track_bdt_vars_maps[iso + str(ptRange) + cat]["track.Pt()"][0] = t.Pt()
                        track_bdt_vars_maps[iso + str(ptRange) + cat]["track.Eta()"][0] = t.Eta()
            
            
                        track_bdt_vars_maps[iso + str(ptRange) + cat]["deltaEtaLL"][0] = abs(t.Eta()-ll.Eta()) 
                        track_bdt_vars_maps[iso + str(ptRange) + cat]["deltaRLL"][0] = abs(t.DeltaR(ll))
                        track_bdt_vars_maps[iso + str(ptRange) + cat]["mtt"][0] = analysis_tools.MT2(c.Met, c.METPhi, t)
                        #track_bdt_vars_map["deltaRMet"][0] = abs(t.DeltaR(metvec))
                        track_bdt_vars_maps[iso + str(ptRange) + cat]["deltaPhiMet"][0] = abs(t.DeltaPhi(metvec))
            
                        track_bdt_vars_maps[iso + str(ptRange) + cat]["lepton.Eta()"][0] = ll.Eta()
                        track_bdt_vars_maps[iso + str(ptRange) + cat]["lepton.Phi()"][0] = ll.Phi()
                        track_bdt_vars_maps[iso + str(ptRange) + cat]["lepton.Pt()"][0] = ll.Pt()
                        track_bdt_vars_maps[iso + str(ptRange) + cat]["invMass"][0] = (t + ll).M()
            
            
                        for trackVar in ['dxyVtx', 'dzVtx']:#, 'trkMiniRelIso', 'trkRelIso']:
                            track_bdt_vars_maps[iso + str(ptRange) + cat]["log(" + trackVar + ")"][0] = log(eval("c.tracks_" + trackVar + "[" + str(ti) + "]"))
            
                        track_tmva_value = track_bdt_readers[iso + str(ptRange) + cat].EvaluateMVA("BDT")
            
                        if  highestOppositeTrackScore is None or highestOppositeTrackScore < track_tmva_value:
                            if highestOppositeTrackScore is not None:
                                secondTrackScore = highestOppositeTrackScore
                                exTrackVars["secondTrackBDT" + iso + str(ptRange) + cat][0] = exTrackVars["trackBDT" + iso + str(ptRange) + cat][0]
                                secondTrack = oppositeChargeTrack
                            highestOppositeTrackScore = track_tmva_value
                            exTrackVars["trackBDT" + iso + str(ptRange) + cat][0] = track_tmva_value
                            oppositeChargeTrack = ti

        
                    if highestOppositeTrackScore is None or highestOppositeTrackScore<0:
                        fillInNonTrackInfo(c, iso, cat, ptRange)
                        #print "2"
                        continue
                    #print "REAL ONE"
                    afterAtLeastOneTrack += 1
                    afterMonoTrack += 1
                    
                    exTrackVars["exclusiveTrack" + iso + str(ptRange) + cat][0] = 1
                    
                    exTrackVars["ti" + iso + str(ptRange) + cat][0] = oppositeChargeTrack
                    if secondTrack is not None:
                        exTrackVars["sti" + iso + str(ptRange) + cat][0] = secondTrack
                    else:
                        exTrackVars["sti" + iso + str(ptRange) + cat][0] = -1
        
                    l1 = None
                    l2 = None
                    if ll.Pt() > c.tracks[oppositeChargeTrack].Pt():
                        l1 = ll
                        l2 = c.tracks[oppositeChargeTrack]
                    else:
                        l1 = c.tracks[oppositeChargeTrack]
                        l2 = ll
                    
                    exTrackVars["l1" + iso + str(ptRange) + cat] = l1
                    exTrackVars["l2" + iso + str(ptRange) + cat] = l2
                    exTrackVars["lepton" + iso + str(ptRange) + cat] = ll
                    exTrackVars["track" + iso + str(ptRange) + cat] = c.tracks[oppositeChargeTrack]
                    exTrackVars["leptonIdx" + iso + str(ptRange) + cat][0] = lepIdx
                    
                    if secondTrack is not None:
                        exTrackVars["secondTrack" + iso + str(ptRange) + cat] = c.tracks[secondTrack]
                    else:
                        exTrackVars["secondTrack" + iso + str(ptRange) + cat] = TLorentzVector()
                    
                    exTrackVars["exTrack_invMass" + iso + str(ptRange) + cat][0] = (l1 + l2).M()
                    exTrackVars["exTrack_dileptonPt" + iso + str(ptRange) + cat][0] = abs((l1 + l2).Pt())
                    exTrackVars["exTrack_deltaPhi" + iso + str(ptRange) + cat][0] =  abs(l1.DeltaPhi(l2))
                    exTrackVars["exTrack_deltaEta" + iso + str(ptRange) + cat][0] = abs(l1.Eta() - l2.Eta())
                    exTrackVars["exTrack_deltaR" + iso + str(ptRange) + cat][0] = abs(l1.DeltaR(l2))
                    exTrackVars["NTracks" + iso + str(ptRange) + cat][0] = ntracks

                    exTrackVars["exTrack_pt3" + iso + str(ptRange) + cat][0] = analysis_tools.pt3(l1.Pt(),l1.Phi(),l2.Pt(),l2.Phi(),c.Met,c.METPhi)

                    pt = TLorentzVector()
                    pt.SetPtEtaPhiE(c.Met,0,c.METPhi,c.Met)

                    exTrackVars["exTrack_mt1" + iso + str(ptRange) + cat][0] = analysis_tools.MT2(c.Met, c.METPhi, l1)
                    exTrackVars["exTrack_mt2" + iso + str(ptRange) + cat][0] = analysis_tools.MT2(c.Met, c.METPhi, l2)

                    exTrackVars["mtt" + iso + str(ptRange) + cat][0] = analysis_tools.MT2(c.Met, c.METPhi, c.tracks[oppositeChargeTrack])
                    exTrackVars["mtl" + iso + str(ptRange) + cat][0] = analysis_tools.MT2(c.Met, c.METPhi, ll)
                    
                    exTrackVars["exTrack_mtautau" + iso + str(ptRange) + cat][0] = analysis_tools.Mtautau(pt, l1, l2)
                    
                    exTrackVars["exTrack_deltaEtaLeadingJetDilepton" + iso + str(ptRange) + cat][0] = abs((l1 + l2).Eta() - c.LeadingJet.Eta())
                    exTrackVars["exTrack_deltaPhiLeadingJetDilepton" + iso + str(ptRange) + cat][0] = abs((l1 + l2).DeltaPhi(c.LeadingJet))
                    
                    exTrackVars["exTrack_dilepHt" + iso + str(ptRange) + cat][0] = analysis_ntuples.htJet25Leps(c.Jets, [l1,l2])
                    
                    exTrackVars["deltaRMetTrack" + iso + str(ptRange) + cat][0] = abs(c.tracks[oppositeChargeTrack].DeltaR(pt))
                    exTrackVars["deltaPhiMetTrack" + iso + str(ptRange) + cat][0] = abs(c.tracks[oppositeChargeTrack].DeltaPhi(pt))
                    exTrackVars["deltaRMetLepton" + iso + str(ptRange) + cat][0] = abs(ll.DeltaR(pt))
                    exTrackVars["deltaPhiMetLepton" + iso + str(ptRange) + cat][0] = abs(ll.DeltaPhi(pt))
                    #print "HERE!!!"
                    for stringObs in utils.exclusiveTrackObservablesStringList:
                        c.SetBranchAddress(stringObs + iso + str(ptRange) + cat, exTrackVars[stringObs + iso + str(ptRange) + cat])
                        #branches[stringObs + iso + str(ptRange) + cat].SetAddress(exTrackVars[stringObs + iso + str(ptRange) + cat])
                        branches[stringObs + iso + str(ptRange) + cat].Fill()
                    for DTypeObs in utils.commonObservablesDTypesList:
                        branches["exTrack_" + DTypeObs + iso + str(ptRange) + cat].Fill()
                    for DTypeObs in utils.exclusiveTrackObservablesDTypesList:
                        branches[DTypeObs + iso + str(ptRange) + cat].Fill()         
                    for CTypeObs in utils.exclusiveTrackObservablesClassList:
                        c.SetBranchAddress(CTypeObs + iso + str(ptRange) + cat, exTrackVars[CTypeObs + iso + str(ptRange) + cat])
                        #branches[CTypeObs + iso + str(ptRange) + cat].SetAddress(exTrackVars[CTypeObs + iso + str(ptRange) + cat])
                        branches[CTypeObs + iso + str(ptRange) + cat].Fill()
                    #print "AFTER!!!"

    c.Write("tEvent",TObject.kOverwrite)
    
    file.Close()

    print "nentries=" + str(nentries)
    print "totalTracks=" + str(totalTracks)
    print "totalSurvivedTracks=" + str(totalSurvivedTracks)
    print "eventsWithGreaterThanOneOppSignTracks=" + str(eventsWithGreaterThanOneOppSignTracks)
    print "noSurvivingTracks=" + str(noSurvivingTracks)
    print "afterAtLeastOneTrack=" + str(afterAtLeastOneTrack)
    print "afterMonoLepton=" + str(afterMonoLepton)
    print "afterUniversalBdt=" + str(afterUniversalBdt)
    print "afterMonoTrack=" + str(afterMonoTrack)

main()