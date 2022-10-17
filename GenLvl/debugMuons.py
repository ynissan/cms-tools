#!/usr/bin/env python3.8
from ROOT import *
import sys
import os
from glob import glob
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib/classes"))
from lib import analysis_ntuples
import cppyy


#signal_file = glob("/afs/desy.de/user/d/diepholq/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_Summer16_stopstop_600GeV_mChipm200GeV_dm1p0GeV_1.root")
signal_file = glob("/afs/desy.de/user/d/diepholq/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_Summer16_stopstop_*GeV_mChipm*GeV_dm*GeV_*.root")
chain = TChain("tEvent")
for file in signal_file:
    chain.Add(file)

number_of_entries = chain.GetEntries()
print("number_of_entries",number_of_entries)

def minDeltaLepLeps(lep, leps):
    min, minCan = None, None
    for i, l in enumerate(leps):
        deltaR = abs(lep.DeltaR(l))
        if min is None or deltaR < min:
            min = deltaR
            minCan = i
    return min, minCan
    
    
def main():
    Gen4 = 0
    genmatchedPassedSelection = 0
    for ientry in range(number_of_entries):
        chain.GetEntry(ientry)
        if ientry % 1000 == 0:
            print("Processing " + str(ientry), "of", number_of_entries)
        ########### CUTS
        isobranch_reco = getattr(chain,"isoCrCorrJetIso15Dr0.4")
        samesignbranch_reco = getattr(chain,"sameSignCorrJetIso15Dr0.4")
        if chain.MHT > 200:
            continue
        if chain.MET > 140:
            continue
        if chain.MinDeltaPhiMhtJets < 0.4:
            continue
        if isobranch_reco != 0:
            continue
        if samesignbranch_reco != 0:
            continue
        ########### LOOP
        muonsisobranch = getattr(chain,"Muons_passCorrJetIso15Dr0.4")
        genmus = []
        genmatched = []
        genmatchedPassedSelectionList = []
        for idx in range(len(chain.GenParticles)):
            if abs(chain.GenParticles_PdgId[idx]) == 13: #status?
                genmus.append(chain.GenParticles[idx])
        if len(genmus) == 4:
            Gen4 += 1
            for i in range(4):
                mindRmu, minCanmu = minDeltaLepLeps(genmus[i],chain.Muons)
                if mindRmu is not None:
                    if mindRmu < 0.01:
                        if analysis_ntuples.muonPassesTightSelection(minCanmu,chain.Muons, chain.Muons_mediumID, muonsisobranch, chain.Muons_deltaRLJ, 2, False, None):
                            genmatchedPassedSelectionList.append(chain.Muons[minCanmu])
            if len(genmatchedPassedSelectionList) == 4:
                genmatchedPassedSelection += 1
                print("wuo o")
                print("EventNumber =", ientry)
                print("genmatchedPassedSelection",len(genmatchedPassedSelectionList))
                    

def nmuons():
    for ientry in range(number_of_entries):
        chain.GetEntry(ientry)
        muonsisobranch = getattr(chain,"Muons_passCorrJetIso15Dr0.4")
        
        if ientry % 100000 == 0:
            print("Processing " + str(ientry), "of", number_of_entries)
        nselectionmuonbranch = getattr(chain,"NSelectionMuonsCorrJetIso15Dr0.4")
        nselectionNoIsoBranch = getattr(chain,"NSelectionMuonsNoIso")
        if nselectionmuonbranch > 3:
            print("NSelectionMuonsCorrJetIso15Dr0.4:",nselectionmuonbranch)
            print("sameSignCorrJetIso15Dr0.4:       ",getattr(chain,"sameSignCorrJetIso15Dr0.4"))
            print("isoCrCorrJetIso15Dr0.4:          ",getattr(chain,"isoCrCorrJetIso15Dr0.4"))
            print("Medium ID:",chain.Muons_mediumID)
            print("Iso:      ",getattr(chain,"Muons_passCorrJetIso15Dr0.4"))
            print("MET:      ",chain.MET)
            print("MHT:      ",chain.MHT)
            for i in range(len(chain.Muons)):
                print(f"pT of muon {1+i}: {chain.Muons[i].Pt()}")
                print(f"muon {1+i} passes tight selection: {analysis_ntuples.muonPassesTightSelection(i,chain.Muons, chain.Muons_mediumID, muonsisobranch, chain.Muons_deltaRLJ, 2, False, None)}")


#main()
nmuons()
exit(0)
                    
                    
            
    