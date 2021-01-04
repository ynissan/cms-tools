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
parser.add_argument('-jpsi_muons', '--jpsi_muons', dest='jpsi_muons', help='JPSI Muons Skim', action='store_true')
parser.add_argument('-jpsi_electrons', '--jpsi_electrons', dest='jpsi_electrons', help='JPSI Electrons Skim', action='store_true')
args = parser.parse_args()


signal = args.signal
bg = args.bg
sc = args.sc

jpsi_muons = args.jpsi_muons

if args.sam:
    signal = True

print "SAME CHARGE=", sc

if jpsi_muons or jpsi_electrons:
    jpsi = True
    print "Got JPSI"
    if jpsi_muons:
        print "MUONS"
    else:
        print "ELECTRONS"

input_file = None
if args.input_file:
    input_file = args.input_file[0].strip()

# if (bg and signal) or not (bg or signal):
#     signal = True
#     bg = False

track_bdt = None
if args.track_bdt:
    track_bdt = args.track_bdt[0]

######## END OF CMDLINE ARGUMENTS ########

exTrackVars = {}
track_bdt_vars_maps = {}
track_bdt_specs_maps = {}
track_bdt_readers = {}
branches = {}


def fillInNonTrackInfo(c, postfix):
    for stringObs in utils.exclusiveTrackObservablesStringList:
        exTrackVars[stringObs + postfix] = ROOT.std.string("")
        #print "*"
        #print branches[stringObs + postfix]
        #print "**"
        #print exTrackVars[stringObs + postfix]
        #branches[stringObs + postfix].ResetAddress()
        c.SetBranchAddress(stringObs + postfix, exTrackVars[stringObs + postfix])
        #branches[stringObs + postfix].SetAddress(exTrackVars[stringObs + postfix])
        #print "**"
        branches[stringObs + postfix].Fill()
        #print "***"
    for DTypeObs in utils.commonObservablesDTypesList:
        exTrackVars["exTrack_" + DTypeObs + postfix][0] = -1
        #print "****"
        branches["exTrack_" + DTypeObs + postfix].Fill()
        #print "*****"
    for DTypeObs in utils.exclusiveTrackObservablesDTypesList:
        if DTypeObs == "exclusiveTrack" or DTypeObs == "trackZ":
            exTrackVars[DTypeObs + postfix][0] = 0
            #print "******"
        else:
            exTrackVars[DTypeObs + postfix][0] = -1
            #print "******"
        branches[DTypeObs + postfix].Fill()         
        #print "*******"
    for CTypeObs in utils.exclusiveTrackObservablesClassList:
        exTrackVars[CTypeObs + postfix] = eval(utils.exclusiveTrackObservablesClassList[CTypeObs])()
        #print "********"
        c.SetBranchAddress(CTypeObs + postfix, exTrackVars[CTypeObs + postfix])
        #branches[CTypeObs + postfix].SetAddress(exTrackVars[CTypeObs + postfix])
        #print "*********"
        branches[CTypeObs + postfix].Fill()
        #print "**********"

def main():
    
    if jpsi:
        utils.defaultJetIsoSetting = "NoIso"
    
    file = TFile(input_file, "update")
    
    c = file.Get("tEvent")
    nentries = c.GetEntries()
    
    # CREATE VARS, BRANCHES, AND BDT READERS
    
    for iso in utils.leptonIsolationList:
        for cat in utils.leptonIsolationCategories:
            ptRanges = [""]
            if iso == "CorrJetIso":
                ptRanges = utils.leptonCorrJetIsoPtRange
            for ptRange in ptRanges:
            
                postfixi = [iso + str(ptRange) + cat]
                    
                if iso + str(ptRange) + cat == utils.defaultJetIsoSetting:
                    postfixi = [iso + str(ptRange) + cat, ""]
                
                for postfix in postfixi:
                    for stringObs in utils.exclusiveTrackObservablesStringList:
                        exTrackVars[stringObs + postfix] = ROOT.std.string("")
                        if c.GetBranchStatus(stringObs + postfix):
                            print "Reseting branch", stringObs + postfix
                            branches[stringObs + postfix] = c.GetBranch(stringObs + postfix)
                            branches[stringObs + postfix].Reset()
                            c.SetBranchAddress(stringObs + postfix, exTrackVars[stringObs + postfix])
                        else:
                            print "Branching", stringObs + postfix
                            branches[stringObs + postfix] = c.Branch(stringObs + postfix, 'std::string', exTrackVars[stringObs + postfix])
                            c.SetBranchAddress(stringObs + postfix, exTrackVars[stringObs + postfix])
                    for DTypeObs in utils.commonObservablesDTypesList:
                        exTrackVars["exTrack_" + DTypeObs + postfix] = np.zeros(1,dtype=utils.commonObservablesDTypesList[DTypeObs])
                        if c.GetBranchStatus("exTrack_" + DTypeObs + postfix):
                            print "Reseting branch", "exTrack_" + DTypeObs + postfix
                            branches["exTrack_" + DTypeObs + postfix] = c.GetBranch("exTrack_" + DTypeObs + postfix)
                            branches["exTrack_" + DTypeObs + postfix].Reset()
                            c.SetBranchAddress("exTrack_" + DTypeObs + postfix, exTrackVars["exTrack_" + DTypeObs + postfix])
                            #branches["exTrack_" + DTypeObs + postfix].SetAddress(exTrackVars["exTrack_" + DTypeObs + postfix])
                        else:
                            print "Branching", "exTrack_" + DTypeObs + postfix
                            branches["exTrack_" + DTypeObs + postfix] = c.Branch("exTrack_" + DTypeObs + postfix, exTrackVars[stringObs + postfix], "exTrack_" + DTypeObs + postfix + "/" + utils.typeTranslation[utils.commonObservablesDTypesList[DTypeObs]])
                            c.SetBranchAddress("exTrack_" + DTypeObs + postfix, exTrackVars["exTrack_" + DTypeObs + postfix])
                    for DTypeObs in utils.exclusiveTrackObservablesDTypesList:
                        exTrackVars[DTypeObs + postfix] = np.zeros(1,dtype=utils.exclusiveTrackObservablesDTypesList[DTypeObs])
                        if c.GetBranchStatus(DTypeObs + postfix):
                            print "Reseting branch", DTypeObs + postfix
                            branches[DTypeObs + postfix] = c.GetBranch(DTypeObs + postfix)
                            branches[DTypeObs + postfix].Reset()
                            c.SetBranchAddress(DTypeObs + postfix, exTrackVars[DTypeObs + postfix])
                            #branches[DTypeObs + postfix].SetAddress(exTrackVars[DTypeObs + postfix])
                        else:
                            print "Branching", DTypeObs + postfix
                            branches[DTypeObs + postfix] = c.Branch(DTypeObs + postfix, exTrackVars[DTypeObs + postfix], DTypeObs + postfix + "/" + utils.typeTranslation[utils.exclusiveTrackObservablesDTypesList[DTypeObs]])
                            c.SetBranchAddress(DTypeObs + postfix, exTrackVars[DTypeObs + postfix])
                    for CTypeObs in utils.exclusiveTrackObservablesClassList:
                        exTrackVars[CTypeObs + postfix] = eval(utils.exclusiveTrackObservablesClassList[CTypeObs])()
                        if c.GetBranchStatus(CTypeObs + postfix):
                            print "Reseting branch", CTypeObs + postfix
                            branches[CTypeObs + postfix] = c.GetBranch(CTypeObs + postfix)
                            branches[CTypeObs + postfix].Reset()
                            c.SetBranchAddress(CTypeObs + postfix, exTrackVars[CTypeObs + postfix])
                        else:
                            print "Branching", CTypeObs + postfix
                            branches[CTypeObs + postfix] = c.Branch(CTypeObs + postfix, utils.exclusiveTrackObservablesClassList[CTypeObs], exTrackVars[CTypeObs + postfix])
                            c.SetBranchAddress(CTypeObs + postfix, exTrackVars[CTypeObs + postfix])
                if not jpsi:
                    for lep in ["Muons", "Electrons"]:
                        track_bdt_weights = track_bdt + "/dataset/weights/TMVAClassification_" + lep + iso + str(ptRange) + cat + ".weights.xml"
                        track_bdt_vars = cut_optimisation.getVariablesFromXMLWeightsFile(track_bdt_weights)
                        track_bdt_vars_map = cut_optimisation.getVariablesMemMap(track_bdt_vars)
                        track_bdt_specs = cut_optimisation.getSpecSpectatorFromXMLWeightsFile(track_bdt_weights)
                        track_bdt_specs_map = cut_optimisation.getSpectatorsMemMap(track_bdt_specs)
                        track_bdt_reader = cut_optimisation.prepareReader(track_bdt_weights, track_bdt_vars, track_bdt_vars_map, track_bdt_specs, track_bdt_specs_map)

                        track_bdt_vars_maps[lep + iso + str(ptRange) + cat] = track_bdt_vars_map
                        track_bdt_specs_maps[lep + iso + str(ptRange) + cat] = track_bdt_specs_map
                        track_bdt_readers[lep + iso + str(ptRange) + cat] = track_bdt_reader

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
        #continue
        
        genZL, genNonZL = None, None
        if signal:
            genZL, genNonZL = analysis_ntuples.classifyGenZLeptons(c)
        
        for iso in utils.leptonIsolationList:
            for cat in utils.leptonIsolationCategories:
                ptRanges = [""]
                if iso == "CorrJetIso":
                    ptRanges = utils.leptonCorrJetIsoPtRange
                for ptRange in ptRanges:
                    
                    postfixi = [iso + str(ptRange) + cat]
                    
                    if iso + str(ptRange) + cat == utils.defaultJetIsoSetting:
                        postfixi = [iso + str(ptRange) + cat, ""]
                    
                    for postfix in postfixi:
                
                        exTrackVars["exclusiveTrack" + postfix][0] = 0
                        exTrackVars["trackZ" + postfix][0] = 0
                        
                        ll, lepIdx, leptonCharge, leptonFlavour, t, ti = None, None, None, None, None, None
                        
                        if jpsi:
                            ll, lepIdx, t, ti = analysis_ntuples.getSingleJPsiLeptonAfterSelection(24, 24, c.Muons, getattr(c, "Muons_pass" + iso + str(ptRange)), c.Muons_mediumID, c.Muons_charge, c.tracks, c.tracks_charge, utils.leptonIsolationCategories[cat]["muonPt"], utils.leptonIsolationCategories[cat]["lowPtTightMuons"], c.Muons_tightID, c.Muons_passIso)
                        else:
                            ll, lepIdx, leptonCharge, leptonFlavour = analysis_ntuples.getSingleLeptonAfterSelection(c.Electrons, getattr(c, "Electrons_pass" + iso + str(ptRange)), c.Electrons_deltaRLJ, c.Electrons_charge, c.Muons, getattr(c, "Muons_pass" + iso + str(ptRange)), c.Muons_mediumID, c.Muons_deltaRLJ, c.Muons_charge, utils.leptonIsolationCategories[cat]["muonPt"], utils.leptonIsolationCategories[cat]["lowPtTightMuons"], c.Muons_tightID)
        
                        if ll is None:
                            # NOT TWO TRACKS
                            #print "**** BEFORE FILL ***" 
                            fillInNonTrackInfo(c, postfix)
                            #print "**** AFTER FILL ***"
                            continue
                        
                        if jpsi:
                            leptonFlavour = "Muons"
                            leptonCharge = c.Muons_charge[lepIdx]
                        
                        if leptonCharge == 0:
                            print "WHAT?! leptonCharge=0"
                        
                        exTrackVars["lepton_charge" + postfix][0] = leptonCharge
                        exTrackVars["exclusiveTrackLeptonFlavour" + postfix] = ROOT.std.string(leptonFlavour)
    
                        afterMonoLepton += 1
                    
                        exTrackVars["secondTrackBDT" + postfix][0] = -1
        
                        metvec = TLorentzVector()
                        metvec.SetPtEtaPhiE(c.Met, 0, c.METPhi, c.Met)
                        
                        highestOppositeTrackScore = None
                        secondTrackScore = None
                        secondTrack = None
                        oppositeChargeTrack = None
                        ntracks = 0
                        
                        if not jpsi:
                            for ti in range(c.tracks.size()):
                                t = c.tracks[ti]
                                if t.Pt() > 10:
                                    continue
                                if t.Eta() > 2.4:
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
                        
                                track_bdt_vars_maps[leptonFlavour + iso + str(ptRange) + cat]["deltaEtaLJ"][0] = abs(t.Eta() - c.LeadingJet.Eta())
                                track_bdt_vars_maps[leptonFlavour + iso + str(ptRange) + cat]["deltaRLJ"][0] = abs(t.DeltaR(c.LeadingJet))
                                track_bdt_vars_maps[leptonFlavour + iso + str(ptRange) + cat]["track.Phi()"][0] = t.Phi()
                                track_bdt_vars_maps[leptonFlavour + iso + str(ptRange) + cat]["track.Pt()"][0] = t.Pt()
                                track_bdt_vars_maps[leptonFlavour + iso + str(ptRange) + cat]["track.Eta()"][0] = t.Eta()
            
            
                                track_bdt_vars_maps[leptonFlavour + iso + str(ptRange) + cat]["deltaEtaLL"][0] = abs(t.Eta()-ll.Eta()) 
                                track_bdt_vars_maps[leptonFlavour + iso + str(ptRange) + cat]["deltaRLL"][0] = abs(t.DeltaR(ll))
                                track_bdt_vars_maps[leptonFlavour + iso + str(ptRange) + cat]["mtt"][0] = analysis_tools.MT2(c.Met, c.METPhi, t)
                                #track_bdt_vars_map["deltaRMet"][0] = abs(t.DeltaR(metvec))
                                track_bdt_vars_maps[leptonFlavour + iso + str(ptRange) + cat]["deltaPhiMet"][0] = abs(t.DeltaPhi(metvec))
            
                                track_bdt_vars_maps[leptonFlavour + iso + str(ptRange) + cat]["lepton.Eta()"][0] = ll.Eta()
                                track_bdt_vars_maps[leptonFlavour + iso + str(ptRange) + cat]["lepton.Phi()"][0] = ll.Phi()
                                track_bdt_vars_maps[leptonFlavour + iso + str(ptRange) + cat]["lepton.Pt()"][0] = ll.Pt()
                                track_bdt_vars_maps[leptonFlavour + iso + str(ptRange) + cat]["invMass"][0] = (t + ll).M()
            
            
                                for trackVar in ['dxyVtx', 'dzVtx','trkMiniRelIso', 'trkRelIso']:
                                    val = eval("c.tracks_" + trackVar + "[" + str(ti) + "]")
                                    if val == 0:
                                        val = 0.000000000000001
                                    track_bdt_vars_maps[leptonFlavour + iso + str(ptRange) + cat]["log(" + trackVar + ")"][0] = log(val)
            
                                track_tmva_value = track_bdt_readers[leptonFlavour + iso + str(ptRange) + cat].EvaluateMVA("BDT")
            
                                if  highestOppositeTrackScore is None or highestOppositeTrackScore < track_tmva_value:
                                    if highestOppositeTrackScore is not None:
                                        secondTrackScore = highestOppositeTrackScore
                                        exTrackVars["secondTrackBDT" + postfix][0] = exTrackVars["trackBDT" + postfix][0]
                                        secondTrack = oppositeChargeTrack
                                    highestOppositeTrackScore = track_tmva_value
                                    exTrackVars["trackBDT" + postfix][0] = track_tmva_value
                                    oppositeChargeTrack = ti
                        else:
                            highestOppositeTrackScore = 1
                            secondTrackScore = 1
                            secondTrack = None
                            oppositeChargeTrack = ti
                            ntracks = 0
                            
                            
                        if highestOppositeTrackScore is None:
                            fillInNonTrackInfo(c, postfix)
                            #print "2"
                            continue
                        #print "REAL ONE"
                        afterAtLeastOneTrack += 1
                        afterMonoTrack += 1
                    
                        exTrackVars["exclusiveTrack" + postfix][0] = 1
                    
                        exTrackVars["ti" + postfix][0] = oppositeChargeTrack
                        if secondTrack is not None:
                            exTrackVars["sti" + postfix][0] = secondTrack
                        else:
                            exTrackVars["sti" + postfix][0] = -1
                        if signal:
                            if genZL is None:
                                exTrackVars["trackZ" + postfix][0] = 0
                            else:
                                l = c.tracks[oppositeChargeTrack]
                                minZ, minCanZ = analysis_ntuples.minDeltaRGenParticles(l, genZL, c.GenParticles)
                                minNZ, minCanNZ = analysis_ntuples.minDeltaRGenParticles(l, genNonZL, c.GenParticles)
                                min = 0
                                if minNZ is None or minZ < minNZ:
                                    min = minZ
                                else:
                                    min = minNZ
                            
                                if min < 0.01 and (minNZ is None or minZ < minNZ):
                                    if c.tracks_charge[ti] * c.GenParticles_PdgId[minCanZ] < 0 and (abs(c.GenParticles_PdgId[minCanZ]) == 11 or abs(c.GenParticles_PdgId[minCanZ]) == 13):
                                        exTrackVars["trackZ" + postfix][0] = 1
        
                        l1 = None
                        l2 = None
                        if ll.Pt() > c.tracks[oppositeChargeTrack].Pt():
                            l1 = ll
                            l2 = c.tracks[oppositeChargeTrack]
                        else:
                            l1 = c.tracks[oppositeChargeTrack]
                            l2 = ll
                    
                        exTrackVars["l1" + postfix] = l1
                        exTrackVars["l2" + postfix] = l2
                        exTrackVars["lepton" + postfix] = ll
                        exTrackVars["track" + postfix] = c.tracks[oppositeChargeTrack]
                        exTrackVars["leptonIdx" + postfix][0] = lepIdx
                    
                        if secondTrack is not None:
                            exTrackVars["secondTrack" + postfix] = c.tracks[secondTrack]
                        else:
                            exTrackVars["secondTrack" + postfix] = TLorentzVector()
                        
                        
                        
                        exTrackVars["exTrack_invMass" + postfix][0] = (l1 + l2).M()
                        exTrackVars["exTrack_dileptonPt" + postfix][0] = abs((l1 + l2).Pt())
                        exTrackVars["exTrack_deltaPhi" + postfix][0] =  abs(l1.DeltaPhi(l2))
                        exTrackVars["exTrack_deltaEta" + postfix][0] = abs(l1.Eta() - l2.Eta())
                        exTrackVars["exTrack_deltaR" + postfix][0] = abs(l1.DeltaR(l2))
                        exTrackVars["NTracks" + postfix][0] = ntracks

                        exTrackVars["exTrack_pt3" + postfix][0] = analysis_tools.pt3(l1.Pt(),l1.Phi(),l2.Pt(),l2.Phi(),c.Met,c.METPhi)

                        pt = TLorentzVector()
                        pt.SetPtEtaPhiE(c.Met,0,c.METPhi,c.Met)

                        exTrackVars["exTrack_mt1" + postfix][0] = analysis_tools.MT2(c.Met, c.METPhi, l1)
                        exTrackVars["exTrack_mt2" + postfix][0] = analysis_tools.MT2(c.Met, c.METPhi, l2)

                        exTrackVars["mtt" + postfix][0] = analysis_tools.MT2(c.Met, c.METPhi, c.tracks[oppositeChargeTrack])
                        exTrackVars["mtl" + postfix][0] = analysis_tools.MT2(c.Met, c.METPhi, ll)
                        
                        exTrackVars["exTrack_mtautau" + postfix][0] = analysis_tools.Mtautau(pt, l1, l2)
                    
                        exTrackVars["exTrack_deltaEtaLeadingJetDilepton" + postfix][0] = abs((l1 + l2).Eta() - c.LeadingJet.Eta())
                        exTrackVars["exTrack_deltaPhiLeadingJetDilepton" + postfix][0] = abs((l1 + l2).DeltaPhi(c.LeadingJet))
                    
                        exTrackVars["exTrack_dilepHt" + postfix][0] = analysis_ntuples.htJet25Leps(c.Jets, [l1,l2])
                    
                        exTrackVars["deltaRMetTrack" + postfix][0] = abs(c.tracks[oppositeChargeTrack].DeltaR(pt))
                        exTrackVars["deltaPhiMetTrack" + postfix][0] = abs(c.tracks[oppositeChargeTrack].DeltaPhi(pt))
                        exTrackVars["deltaRMetLepton" + postfix][0] = abs(ll.DeltaR(pt))
                        exTrackVars["deltaPhiMetLepton" + postfix][0] = abs(ll.DeltaPhi(pt))
                        #print "HERE!!!"
                        for stringObs in utils.exclusiveTrackObservablesStringList:
                            c.SetBranchAddress(stringObs + postfix, exTrackVars[stringObs + postfix])
                            #branches[stringObs + postfix].SetAddress(exTrackVars[stringObs + postfix])
                            branches[stringObs + postfix].Fill()
                        for DTypeObs in utils.commonObservablesDTypesList:
                            branches["exTrack_" + DTypeObs + postfix].Fill()
                        for DTypeObs in utils.exclusiveTrackObservablesDTypesList:
                            branches[DTypeObs + postfix].Fill()         
                        for CTypeObs in utils.exclusiveTrackObservablesClassList:
                            c.SetBranchAddress(CTypeObs + postfix, exTrackVars[CTypeObs + postfix])
                            #branches[CTypeObs + postfix].SetAddress(exTrackVars[CTypeObs + postfix])
                            branches[CTypeObs + postfix].Fill()
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