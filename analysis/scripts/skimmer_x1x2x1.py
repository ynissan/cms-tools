#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import numpy as np
import os

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes"))
from lib import analysis_ntuples
from lib import analysis_tools
from lib import utils

gSystem.Load('LumiSectMap_C')
from ROOT import LumiSectMap

gSystem.Load('LeptonCollectionMap_C')
from ROOT import LeptonCollectionMap
from ROOT import LeptonCollectionFilesMap
from ROOT import LeptonCollection

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Create skims for x1x2x1 process.')
parser.add_argument('-i', '--input_file', nargs=1, help='Input Filename', required=False)
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
parser.add_argument('-madHTgt', '--madHTgt', nargs=1, help='madHT lower bound', required=False)
parser.add_argument('-madHTlt', '--madHTlt', nargs=1, help='madHT uppper bound', required=False)

parser.add_argument('-s', '--signal', dest='signal', help='Signal', action='store_true')
parser.add_argument('-bg', '--background', dest='bg', help='Background', action='store_true')
parser.add_argument('-skim', '--skim', dest='skim', help='Skim', action='store_true')
parser.add_argument('-data', '--data', dest='data', help='Data', action='store_true')
parser.add_argument('-dy', '--dy', dest='dy', help='Drell-Yan', action='store_true')
parser.add_argument('-sam', '--sam', dest='sam', help='Sam Samples', action='store_true')
parser.add_argument('-nlp', '--no_lepton_selection', dest='no_lepton_selection', help='No Lepton Selection Skim', action='store_true')
parser.add_argument('-jpsi_muons', '--jpsi_muons', dest='jpsi_muons', help='JPSI Muons Skim', action='store_true')
parser.add_argument('-jpsi_electrons', '--jpsi_electrons', dest='jpsi_electrons', help='JPSI Electrons Skim', action='store_true')

args = parser.parse_args()

print args

madHTgt = None
madHTlt = None
if args.madHTgt:
    madHTgt = int(args.madHTgt[0])
    print "Got madHT lower bound of " + str(madHTgt)
if args.madHTlt:
    madHTlt = int(args.madHTlt[0])
    print "Got madHT upper bound of " + str(madHTlt)


signal = args.signal
bg = args.bg
data = args.data
dy = args.dy
sam = args.sam
no_lepton_selection = args.no_lepton_selection
jpsi_muons = args.jpsi_muons
jpsi_electrons = args.jpsi_electrons
jpsi = False

if dy:
    print "Got Drell-Yan"
    #exit(0)
if no_lepton_selection:
    print "NO LEPTON SELECTION!"

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
output_file = None
if args.output_file:
    output_file = args.output_file[0].strip()

if (bg and signal):
    signal = True
    bg = False

replace_lepton_collection = True
if signal:
    replace_lepton_collection = False
    
def getDyMuons(c):
    muons = [i for i in range(len(c.Muons)) if c.Muons[i].Pt() >= 15 and bool(c.Muons_mediumID[i]) and bool(c.Muons_passIso[i]) and abs(c.Muons[i].Eta()) <= 2.4]
    
    if len(muons) != 2:
        return None, None
        
    if c.Muons[muons[0]].Pt() < 30:
        return None, None
    
    if c.Muons_charge[muons[0]] * c.Muons_charge[muons[1]] > 0:
        return None, None
    
    invMass = (c.Muons[muons[0]] + c.Muons[muons[1]]).M()
    if not abs(invMass-91.19)<10: return None, None
    
    return muons, invMass

######## END OF CMDLINE ARGUMENTS ########

commonBranches = {
        "tEffhMetMhtRealXMet2016" :  "float",
        "tEffhMetMhtRealXMet2017" :  "float",
        "tEffhMetMhtRealXMet2018" :  "float",
    
        "tEffhMetMhtRealXMht2016" :  "float",
        "tEffhMetMhtRealXMht2017" :  "float",
        "tEffhMetMhtRealXMht2018" :  "float",
    
        "passedMhtMet6pack" :  "bool",
}

def main():
    
    import os
    from lib import utils
    
    if jpsi:
        utils.defaultJetIsoSetting = "NoIso"
    
    triggerFileName = os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/susy-trig-plots.root")
    print "Opening trigger file: " + triggerFileName
    
    triggerFile = TFile(triggerFileName, "read")
    
    tEffhMetMhtRealXMet2016 = analysis_ntuples.getTrigEffGraph(triggerFile, 'tEffhMetMhtRealXMet;1')
    tEffhMetMhtRealXMet2017 = analysis_ntuples.getTrigEffGraph(triggerFile, 'tEffhMetMhtRealXMet;2')
    tEffhMetMhtRealXMet2018 = analysis_ntuples.getTrigEffGraph(triggerFile, 'tEffhMetMhtRealXMet;3')
    
    tEffhMetMhtRealXMht2016 = analysis_ntuples.getTrigEffGraph(triggerFile, 'tEffhMetMhtRealXMht;1')
    tEffhMetMhtRealXMht2017 = analysis_ntuples.getTrigEffGraph(triggerFile, 'tEffhMetMhtRealXMht;2')
    tEffhMetMhtRealXMht2018 = analysis_ntuples.getTrigEffGraph(triggerFile, 'tEffhMetMhtRealXMht;3')
    
    triggerFile.Close()
    
    var_RunNum = np.zeros(1,dtype=int)
    var_LumiBlockNum = np.zeros(1,dtype=int)
    var_EvtNum = np.zeros(1,dtype=long)
    
    var_Met = np.zeros(1,dtype=float)
    var_METPhi = np.zeros(1,dtype=float)
    var_CrossSection = np.zeros(1,dtype=float)
    var_BranchingRatio = np.zeros(1,dtype=float)
    var_NJets = np.zeros(1,dtype=int)
    var_BTagsLoose = np.zeros(1,dtype=int)
    var_BTagsMedium = np.zeros(1,dtype=int)
    var_BTagsDeepLoose = np.zeros(1,dtype=int)
    var_BTagsDeepMedium = np.zeros(1,dtype=int)
    var_Ht = np.zeros(1,dtype=float)
    var_MHTPhi = np.zeros(1,dtype=float)
    var_madHT = np.zeros(1,dtype=float)
    var_Mht = np.zeros(1,dtype=float)
    var_MetDHt = np.zeros(1,dtype=float)
    var_Mt2 = np.zeros(1,dtype=float)
    
    var_vetoElectronsPassIso = np.zeros(1,dtype=bool)
    var_vetoElectronsMediumID = np.zeros(1,dtype=bool)
    var_vetoElectronsTightID = np.zeros(1,dtype=bool)
    
    var_vetoMuonsPassIso = np.zeros(1,dtype=bool)
    var_vetoMuonsMediumID = np.zeros(1,dtype=bool)
    var_vetoMuonsTightID = np.zeros(1,dtype=bool)
    
    var_DYMuons = ROOT.std.vector(TLorentzVector)()
    var_DYMuonsSum = TLorentzVector()
    var_DYMuonsInvMass = np.zeros(1,dtype=float)
    var_DYMuons_charge = ROOT.std.vector(int)()
    var_DYMuons_mediumID = ROOT.std.vector(bool)()
    var_DYMuons_passIso = ROOT.std.vector(bool)()
    var_DYMuons_tightID = ROOT.std.vector(bool)()
    var_DYMuons_MiniIso = ROOT.std.vector(double)()
    var_DYMuons_MT2Activity = ROOT.std.vector(double)()
    var_DYMuons_MTW = ROOT.std.vector(double)()
    
    var_Electrons_isZ = ROOT.std.vector(bool)()
    var_Muons_isZ = ROOT.std.vector(bool)()
    
    var_GenParticles = ROOT.std.vector(TLorentzVector)()
    var_GenParticles_ParentId = ROOT.std.vector(int)()
    var_GenParticles_ParentIdx = ROOT.std.vector(int)()
    var_GenParticles_PdgId = ROOT.std.vector(int)()
    var_GenParticles_Status = ROOT.std.vector(int)()
    var_LeadingJetPt = np.zeros(1,dtype=float)
    var_NL = np.zeros(1,dtype=int)
    var_NLGen = np.zeros(1,dtype=int)
    var_NLGenZ = np.zeros(1,dtype=int)
    var_puWeight = np.zeros(1,dtype=float)

    var_Jets = ROOT.std.vector(TLorentzVector)()
    var_Jets_bDiscriminatorCSV = ROOT.std.vector(double)()
    var_Jets_bJetTagDeepCSVBvsAll = ROOT.std.vector(double)()
    var_Jets_electronEnergyFraction = ROOT.std.vector(double)()
    var_Jets_muonEnergyFraction = ROOT.std.vector(double)()
    var_Jets_muonMultiplicity = ROOT.std.vector(int)()
    var_Jets_multiplicity = ROOT.std.vector(int)()
    var_Jets_electronMultiplicity = ROOT.std.vector(int)()
    var_Jets_muonCorrected = ROOT.std.vector(TLorentzVector)()
    var_Jets_electronCorrected = ROOT.std.vector(TLorentzVector)()
    
    var_LeadingJetPartonFlavor = np.zeros(1,dtype=int)
    var_LeadingJetQgLikelihood = np.zeros(1,dtype=float)
    var_LeadingJetMinDeltaRMuons = np.zeros(1,dtype=float)
    var_LeadingJetMinDeltaRElectrons = np.zeros(1,dtype=float)
    
    var_MinDeltaPhiMetJets = np.zeros(1,dtype=float)
    var_MinDeltaPhiMhtJets = np.zeros(1,dtype=float)
    
    var_MinCsv30 = np.zeros(1,dtype=float)
    var_MinCsv25 = np.zeros(1,dtype=float)
    var_MaxCsv30 = np.zeros(1,dtype=float)
    var_MaxCsv25 = np.zeros(1,dtype=float)
    
    var_MinDeepCsv30 = np.zeros(1,dtype=float)
    var_MinDeepCsv25 = np.zeros(1,dtype=float)
    var_MaxDeepCsv30 = np.zeros(1,dtype=float)
    var_MaxDeepCsv25 = np.zeros(1,dtype=float)
    #### TRACKS ####
    trackObs = {}
    
    for tracksOb in analysis_ntuples.tracksObs:
        trackObs[tracksOb] = ROOT.std.vector(eval(analysis_ntuples.tracksObs[tracksOb]))()
    
    pionsObs = {}
    for pionsOb in analysis_ntuples.pionsObs:
        pionsObs[pionsOb] = ROOT.std.vector(eval(analysis_ntuples.pionsObs[pionsOb]))()
        
    photonObs = {}
    for photonOb in analysis_ntuples.photonObs:
        photonObs[photonOb] = ROOT.std.vector(eval(analysis_ntuples.photonObs[photonOb]))()
    
    ### LEPTONS ###
    
    electronsObs = {}
    for electronsOb in analysis_ntuples.electronsObs:
        electronsObs[electronsOb] = ROOT.std.vector(eval(analysis_ntuples.electronsObs[electronsOb]))()

    electronsCalcObs = {}
    for electronsCalcOb in analysis_ntuples.electronsCalcObs:
        electronsCalcObs[electronsCalcOb] = ROOT.std.vector(eval(analysis_ntuples.electronsCalcObs[electronsCalcOb]))()

    muonsObs = {}
    for muonsOb in analysis_ntuples.muonsObs:
        muonsObs[muonsOb] = ROOT.std.vector(eval(analysis_ntuples.muonsObs[muonsOb]))()

    muonsCalcObs = {}
    for muonsCalcOb in analysis_ntuples.muonsCalcObs:
        muonsCalcObs[muonsCalcOb] = ROOT.std.vector(eval(analysis_ntuples.muonsCalcObs[muonsCalcOb]))()
        
    var_genFlavour      = ROOT.std.string()
    
    var_category = np.zeros(1,dtype=bool)
    
    leptonsCorrJetVars = {}
    
    for lep in ["Muons", "Electrons"]:
        for CorrJetObs in utils.leptonIsolationList:
            ptRanges = [""]
            if CorrJetObs == "CorrJetIso":
                ptRanges = utils.leptonCorrJetIsoPtRange
            for ptRange in ptRanges:
                leptonsCorrJetVars[lep + "_pass" + CorrJetObs + str(ptRange)] = ROOT.std.vector(eval(utils.leptonsCorrJetVecList[CorrJetObs]))()
                
    print leptonsCorrJetVars
    
    # DILEPTON OBSERVABLES
    
    dileptonVars = {}
    
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
                    for vecObs in utils.dileptonObservablesVecList:
                        dileptonVars[vecObs + postfix] = ROOT.std.vector(eval(utils.dileptonObservablesVecList[vecObs]))()
                    for stringObs in utils.dileptonObservablesStringList:
                        dileptonVars[stringObs + postfix] = ROOT.std.string("")
                    for DTypeObs in utils.dileptonObservablesDTypesList:
                        dileptonVars[DTypeObs + postfix] = np.zeros(1,dtype=utils.dileptonObservablesDTypesList[DTypeObs])

    print dileptonVars
       
    var_LeadingJet = TLorentzVector()
        
    # TRIGGER
    var_triggerNames     = ROOT.std.vector(ROOT.std.string)()
    var_triggerPass      = ROOT.std.vector(int)()
    var_triggerPrescales = ROOT.std.vector(int)()
    var_triggerVersion   = ROOT.std.vector(int)()

    tEvent = TTree('tEvent','tEvent')
    
    tEvent.Branch('RunNum', var_RunNum,'RunNum/I')
    tEvent.Branch('LumiBlockNum', var_LumiBlockNum,'LumiBlockNum/I')
    tEvent.Branch('EvtNum', var_EvtNum,'EvtNum/L')
    
    tEvent.Branch('Met', var_Met,'Met/D')
    tEvent.Branch('METPhi', var_METPhi,'METPhi/D')
    tEvent.Branch('CrossSection', var_CrossSection,'CrossSection/D')
    tEvent.Branch('BranchingRatio', var_BranchingRatio,'BranchingRatio/D')
    tEvent.Branch('NJets', var_NJets,'NJets/I')
    tEvent.Branch('BTagsLoose', var_BTagsLoose,'BTagsLoose/I')
    tEvent.Branch('BTagsMedium', var_BTagsMedium,'BTagsMedium/I')
    tEvent.Branch('BTagsDeepLoose', var_BTagsDeepLoose,'BTagsDeepLoose/I')
    tEvent.Branch('BTagsDeepMedium', var_BTagsDeepMedium,'BTagsDeepMedium/I')
    
    tEvent.Branch('NL', var_NL,'NL/I')
    tEvent.Branch('NLGen', var_NLGen,'NLGen/I')
    tEvent.Branch('NLGenZ', var_NLGenZ,'NLGenZ/I')
    tEvent.Branch('Ht', var_Ht,'Ht/D')
    tEvent.Branch('madHT', var_madHT,'madHT/D')
    tEvent.Branch('Mht', var_Mht,'Mht/D')
    tEvent.Branch('MHTPhi', var_MHTPhi,'MHTPhi/D')
    tEvent.Branch('MetDHt', var_MetDHt,'MetDHt/D')
    #tEvent.Branch('MetDHt2', var_MetDHt2,'MetDHt2/D')
    tEvent.Branch('Mt2', var_Mt2,'Mt2/D')
    tEvent.Branch('puWeight', var_puWeight,'puWeight/D')
    
    
    
    tEvent.Branch('vetoElectronsPassIso', var_vetoElectronsPassIso,'vetoElectronsPassIso/O')
    #tEvent.Branch('vetoElectronsPassJetIso', var_vetoElectronsPassJetIso,'vetoElectronsPassJetIso/O')
    tEvent.Branch('vetoElectronsMediumID', var_vetoElectronsMediumID,'vetoElectronsMediumID/O')
    tEvent.Branch('vetoElectronsTightID', var_vetoElectronsTightID,'vetoElectronsTightID/O')
    
    tEvent.Branch('vetoMuonsPassIso', var_vetoMuonsPassIso,'vetoMuonsPassIso/O')
    #tEvent.Branch('vetoMuonsPassJetIso', var_vetoMuonsPassJetIso,'vetoMuonsPassJetIso/O')
    tEvent.Branch('vetoMuonsMediumID', var_vetoMuonsMediumID,'vetoMuonsMediumID/O')
    tEvent.Branch('vetoMuonsTightID', var_vetoMuonsTightID,'vetoMuonsTightID/O')
    
    if signal:
        tEvent.Branch('Electrons_isZ', 'std::vector<bool>', var_Electrons_isZ)
        tEvent.Branch('Muons_isZ', 'std::vector<bool>', var_Muons_isZ)
        tEvent.Branch('genFlavour', 'std::string', var_genFlavour)
    if dy:
        tEvent.Branch('DYMuons', 'std::vector<TLorentzVector>', var_DYMuons)
        tEvent.Branch('DYMuons_charge', 'std::vector<int>', var_DYMuons_charge)
        tEvent.Branch('DYMuons_mediumID', 'std::vector<bool>', var_DYMuons_mediumID)
        tEvent.Branch('DYMuons_passIso', 'std::vector<bool>', var_DYMuons_passIso)
        tEvent.Branch('DYMuons_tightID', 'std::vector<bool>', var_DYMuons_tightID)
        tEvent.Branch('DYMuons_MiniIso', 'std::vector<double>', var_DYMuons_MiniIso)
        tEvent.Branch('DYMuons_MT2Activity', 'std::vector<double>', var_DYMuons_MT2Activity)
        tEvent.Branch('DYMuons_MTW', 'std::vector<double>', var_DYMuons_MTW)
        tEvent.Branch('DYMuonsSum', 'TLorentzVector', var_DYMuonsSum)
        tEvent.Branch('DYMuonsInvMass', var_DYMuonsInvMass,'DYMuonsInvMass/D')
    
    tEvent.Branch('GenParticles', 'std::vector<TLorentzVector>', var_GenParticles)
    tEvent.Branch('GenParticles_ParentId', 'std::vector<int>', var_GenParticles_ParentId)
    tEvent.Branch('GenParticles_ParentIdx', 'std::vector<int>', var_GenParticles_ParentIdx)
    tEvent.Branch('GenParticles_PdgId', 'std::vector<int>', var_GenParticles_PdgId)
    tEvent.Branch('GenParticles_Status', 'std::vector<int>', var_GenParticles_Status)

    tEvent.Branch('Jets', 'std::vector<TLorentzVector>', var_Jets)
    tEvent.Branch('Jets_bDiscriminatorCSV', 'std::vector<double>', var_Jets_bDiscriminatorCSV)
    tEvent.Branch('Jets_bJetTagDeepCSVBvsAll', 'std::vector<double>', var_Jets_bJetTagDeepCSVBvsAll)
    
    tEvent.Branch('Jets_electronEnergyFraction', 'std::vector<double>', var_Jets_electronEnergyFraction)
    tEvent.Branch('Jets_muonEnergyFraction', 'std::vector<double>', var_Jets_muonEnergyFraction)
    
    tEvent.Branch('Jets_muonMultiplicity', 'std::vector<int>', var_Jets_muonMultiplicity)
    tEvent.Branch('Jets_multiplicity', 'std::vector<int>', var_Jets_multiplicity)
    tEvent.Branch('Jets_electronMultiplicity', 'std::vector<int>', var_Jets_electronMultiplicity)
    
    tEvent.Branch('Jets_muonCorrected', 'std::vector<TLorentzVector>', var_Jets_muonCorrected)
    tEvent.Branch('Jets_electronCorrected', 'std::vector<TLorentzVector>', var_Jets_electronCorrected)

    tEvent.Branch('LeadingJetPartonFlavor', var_LeadingJetPartonFlavor,'LeadingJetPartonFlavor/I')
    tEvent.Branch('LeadingJetQgLikelihood', var_LeadingJetQgLikelihood,'LeadingJetQgLikelihood/D')
    tEvent.Branch('LeadingJetMinDeltaRMuons', var_LeadingJetMinDeltaRMuons,'LeadingJetMinDeltaRMuons/D')
    tEvent.Branch('LeadingJetMinDeltaRElectrons', var_LeadingJetMinDeltaRElectrons,'LeadingJetMinDeltaRElectrons/D')
    
    tEvent.Branch('MinDeltaPhiMetJets', var_MinDeltaPhiMetJets,'MinDeltaPhiMetJets/D')
    tEvent.Branch('MinDeltaPhiMhtJets', var_MinDeltaPhiMhtJets,'MinDeltaPhiMhtJets/D')
    tEvent.Branch('LeadingJetPt', var_LeadingJetPt,'LeadingJetPt/D')
      
    for lep in ["Muons", "Electrons"]:
        for CorrJetObs in utils.leptonIsolationList:
            ptRanges = [""]
            if CorrJetObs == "CorrJetIso":
                 ptRanges = utils.leptonCorrJetIsoPtRange
            for ptRange in ptRanges:
                print "tEvent.Branch(" + lep + "_pass" + CorrJetObs + str(ptRange), 'std::vector<' + str(utils.leptonsCorrJetVecList[CorrJetObs]) + '>', leptonsCorrJetVars[lep + "_pass" + CorrJetObs + str(ptRange)], ")"
                tEvent.Branch(lep + "_pass" +  CorrJetObs + str(ptRange), 'std::vector<' + utils.leptonsCorrJetVecList[CorrJetObs] + '>', leptonsCorrJetVars[lep + "_pass" + CorrJetObs + str(ptRange)])
            
    ###### Tracks #######
    
    for tracksOb in analysis_ntuples.tracksObs:
        tEvent.Branch(tracksOb, 'std::vector<' + analysis_ntuples.tracksObs[tracksOb] + '>', trackObs[tracksOb])
    
    for pionsOb in analysis_ntuples.pionsObs:
        tEvent.Branch(pionsOb, 'std::vector<' + analysis_ntuples.pionsObs[pionsOb] + '>', pionsObs[pionsOb])
        
    for photonOb in analysis_ntuples.photonObs:
        tEvent.Branch(photonOb, 'std::vector<' + analysis_ntuples.photonObs[photonOb] + '>', photonObs[photonOb])
    
    for electronsOb in analysis_ntuples.electronsObs:
        tEvent.Branch(electronsOb, 'std::vector<' + analysis_ntuples.electronsObs[electronsOb] + '>', electronsObs[electronsOb])
    
    for electronsCalcOb in analysis_ntuples.electronsCalcObs:
        tEvent.Branch(electronsCalcOb, 'std::vector<' + analysis_ntuples.electronsCalcObs[electronsCalcOb] + '>', electronsCalcObs[electronsCalcOb])
    
    for muonsOb in analysis_ntuples.muonsObs:
        tEvent.Branch(muonsOb, 'std::vector<' + analysis_ntuples.muonsObs[muonsOb] + '>', muonsObs[muonsOb])
    
    for muonsCalcOb in analysis_ntuples.muonsCalcObs:
        tEvent.Branch(muonsCalcOb, 'std::vector<' + analysis_ntuples.muonsCalcObs[muonsCalcOb] + '>', muonsCalcObs[muonsCalcOb])

    tEvent.Branch('LeadingJet', 'TLorentzVector', var_LeadingJet)
    
    tEvent.Branch('MinCsv30', var_MinCsv30,'MinCsv30/D')
    tEvent.Branch('MinCsv25', var_MinCsv25,'MinCsv25/D')
    tEvent.Branch('MaxCsv30', var_MaxCsv30,'MaxCsv30/D')
    tEvent.Branch('MaxCsv25', var_MaxCsv25,'MaxCsv25/D')
    
    tEvent.Branch('MinDeepCsv30', var_MinDeepCsv30,'MinDeepCsv30/D')
    tEvent.Branch('MinDeepCsv25', var_MinDeepCsv25,'MinDeepCsv25/D')
    tEvent.Branch('MaxDeepCsv30', var_MaxDeepCsv30,'MaxDeepCsv30/D')
    tEvent.Branch('MaxDeepCsv25', var_MaxDeepCsv25,'MaxDeepCsv25/D')
    
    tEvent.Branch('category', var_category,'vetoMuonsTightID/O')
    
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
                    for vecObs in utils.dileptonObservablesVecList:
                        print "tEvent.Branch(" + vecObs + postfix, 'std::vector<' + utils.dileptonObservablesVecList[vecObs] + '>', dileptonVars[vecObs + postfix], ")"
                        tEvent.Branch(vecObs + postfix, 'std::vector<' + utils.dileptonObservablesVecList[vecObs] + '>', dileptonVars[vecObs + postfix])
                    for stringObs in utils.dileptonObservablesStringList:
                        print "tEvent.Branch(" + stringObs + postfix, 'std::string', dileptonVars[stringObs + postfix],")"
                        tEvent.Branch(stringObs + postfix, 'std::string', dileptonVars[stringObs + postfix])
                    for DTypeObs in utils.dileptonObservablesDTypesList:
                        print "tEvent.Branch(" + DTypeObs + postfix, dileptonVars[DTypeObs + postfix],DTypeObs + postfix + "/" + utils.typeTranslation[utils.dileptonObservablesDTypesList[DTypeObs]], ")"
                        tEvent.Branch(DTypeObs + postfix, dileptonVars[DTypeObs + postfix],DTypeObs + postfix + "/" + utils.typeTranslation[utils.dileptonObservablesDTypesList[DTypeObs]])
                        
    if not signal:
        tEvent.Branch('TriggerNames', 'std::vector<string>', var_triggerNames)
        tEvent.Branch('TriggerPass', 'std::vector<int>', var_triggerPass)
        tEvent.Branch('TriggerPrescales', 'std::vector<int>', var_triggerPrescales)
        tEvent.Branch('TriggerVersion', 'std::vector<int>', var_triggerVersion)
    
    vars = {}
    
    for commonBranche in commonBranches:
        vars[commonBranche] = np.zeros(1,dtype=commonBranches[commonBranche])
        tEvent.Branch(commonBranche, vars[commonBranche], commonBranche + "/" + utils.typeTranslation[commonBranches[commonBranche]])
    
    chain = TChain('TreeMaker2/PreSelection')
    print "Opening", input_file
    chain.Add(input_file)
    c = chain.CloneTree()
    chain = None
    print "Creating " + output_file
    fnew = TFile(output_file,'recreate')
    print "Created."

    hHt = TH1F('hHt','hHt',100,0,3000)
    hHtWeighted = TH1F('hHtWeighted','hHtWeighted',100,0,3000)
    hHtAfterMadHt = TH1F('hHtAfterMadHt','hHtAfterMadHt',100,0,3000)
    hHt.Sumw2()
    
    lumiSecs = LumiSectMap()
    
    nentries = c.GetEntries()
    print 'Analysing', nentries, "entries"

    count = 0
    afterPreselection = 0
    afterMET = 0
    afterNj = 0
    afterLeptons = 0
    nLMap = {}
    nLGenMap = {}
    nLGenMapZ = {}
    baseFileName = os.path.basename(input_file)
    crossSection = 1
    if signal:
        if sam:
            chiM = os.path.basename(input_file).split("_")[2]
            print "Got chiM=" + chiM
            crossSection = utils.samCrossSections.get(chiM)
            print "Cross Section is", crossSection
        else:
            filename = (os.path.basename(input_file).split("Chi20Chipm")[0]).replace("p", ".")
            crossSection = utils.getCrossSection(filename)
        if crossSection is None:
            if utils.crossSections.get(filename) is not None:
                crossSection = utils.crossSections.get(filename)
            else:
                crossSection = 1.21547
    elif bg and "DYJetsToLL_M-5to50_" in input_file:
        fileBasename = os.path.basename(input_file).split(".root")[0].split("RunIISummer16MiniAODv3.")[1].split("_TuneCUETP8M1")[0]
        print "Checking DY CS for", fileBasename
        crossSection = utils.dyCrossSections.get(fileBasename)
        print "Got cs", crossSection
    
    currLeptonCollectionMap = None
    currLeptonCollectionFileMapFile = None
    
    print "Starting Loop"
    for ientry in range(nentries):
        if ientry % 1000 == 0:
            print "Processing " + str(ientry)
        c.GetEntry(ientry)

        ### MADHT ###
        rightProcess = True
    
        if signal and not sam:
            rightProcess = analysis_ntuples.isX1X2X1Process(c)
        elif bg:
            if "DYJetsToLL_M-5to50_" not in input_file:
                crossSection = c.CrossSection
            rightProcess = utils.madHtCheck(baseFileName, c.madHT)
        elif data:
            lumiSecs.insert(c.RunNum, c.LumiBlockNum)

        hHt.Fill(c.HT)
        #print "crossSection=" + str(crossSection)
        hHtWeighted.Fill(c.HT, crossSection)

        if not rightProcess:
            continue
            
        count += 1
        if not data:
            hHtAfterMadHt.Fill(c.madHT)
        
        nL = c.Electrons.size() + c.Muons.size()
        nT = c.tracks.size()
    
        #### GEN LEVEL STUFF ####
        nLGen = 0
        nLGenZ = 0
        nX20 = 0
        branching_ratio = 1
        if not data:
            partSize = c.GenParticles.size()
            for ipart in range(partSize):
                if c.GenParticles_Status[ipart] == 1 and (abs(c.GenParticles_PdgId[ipart]) == 11 or abs(c.GenParticles_PdgId[ipart]) == 13):
                    nLGen += 1
                    if c.GenParticles_ParentId[ipart] == 1000023 or c.GenParticles_ParentId[ipart] == 23:
                        nLGenZ += 1
                if abs(c.GenParticles_PdgId[ipart]) == 1000023:
                    nX20 += 1
                
            
            if nLMap.get(nL) is not None:
                nLMap[nL] += 1
            else:
                nLMap[nL] = 1
            if nLGenMap.get(nLGen) is not None:
                nLGenMap[nLGen] += 1
            else:
                nLGenMap[nLGen] = 1
            if nLGenMapZ.get(nLGenZ) is not None:
                nLGenMapZ[nLGenZ] += 1
            else:
                nLGenMapZ[nLGenZ] = 1
            
            if nX20 > 0:
                #print "nX20", nX20, "nLGenZ", nLGenZ
                if nX20 == 1 and nLGenZ == 2:
                    branching_ratio *= 0.2
                elif nX20 == 2 and nLGenZ == 4:
                    branching_ratio *= 0.04
                elif nX20 == 1 and nLGenZ == 0:
                    branching_ratio *= 1.8
                    #print "******", branching_ratio
                elif nX20 == 2 and nLGenZ == 0:
                    branching_ratio *= 3.24
                    
        #### END OF GEN LEVEL STUFF ####
        
        var_BranchingRatio[0] = branching_ratio
        # if branching_ratio == 1.8:
#             print "YEY"
#         
        # if nX20 > 0:
#             if nX20 * 2 != nLGenZ:
#                 print "WTF", nX20, nLGenZ
        
        # nX20 = 0
#         nX10 = 0
#         nX1pm = 0
#         susy = 0
#         susy_map = {}
#         susy_status = {}
#         partSize = c.GenParticles.size()
#         for ipart in range(partSize):
#             
#             if abs(c.GenParticles_PdgId[ipart]) == 1000023:
#                 nX20 += 1
#             if abs(c.GenParticles_PdgId[ipart]) == 1000022:
#                 nX10 += 1
#             if abs(c.GenParticles_PdgId[ipart]) == 1000024:
#                 nX1pm += 1
#             if  analysis_tools.isSusy(abs(c.GenParticles_PdgId[ipart])):
#                 susy += 1
#                 if susy_map.get(abs(c.GenParticles_PdgId[ipart])) is not None:
#                     susy_map[abs(c.GenParticles_PdgId[ipart])] +=1
#                     susy_status[abs(c.GenParticles_PdgId[ipart])].append(abs(c.GenParticles_Status[ipart]))
#                 else:
#                     susy_map[abs(c.GenParticles_PdgId[ipart])] = 1
#                     susy_status[abs(c.GenParticles_PdgId[ipart])] = []
#                     susy_status[abs(c.GenParticles_PdgId[ipart])].append(abs(c.GenParticles_Status[ipart]))
#         print susy
#         print susy_map
#         print susy_status
        
        
        
        #continue
#         if nX20>1:
#             print "MORE THAN 1!"
#         if nX20<1:
#             print "LESS THAN 1!", nX1pm, nX10
#         if  nX1pm !=1:
#             print "nX1pm not 1", nX1pm, nX10
#         if nX1pm == 0 and nX20 == 0 and nX10 == 0:
#             print "ALL 0!"
#         print "============"
#         continue
    
        var_NLGen[0] = nLGen
        var_NLGenZ[0] = nLGenZ
    
        #### PRECUTS ###
        if not signal:
            if not analysis_ntuples.passed2016BTrigger(c, data): continue
        
        MET = c.MET
        METPhi = c.METPhi
        MHT = c.MHT
        HT = c.HT
        MHTPhi = c.MHTPhi
        
        jets = c.Jets
        jets_bDiscriminatorCSV = c.Jets_bDiscriminatorCSV
        jets_bJetTagDeepCSVBvsAll = c.Jets_bJetTagDeepCSVBvsAll
        jets_electronEnergyFraction = c.Jets_electronEnergyFraction
        jets_muonEnergyFraction = c.Jets_muonEnergyFraction
        
        jets_muonMultiplicity = c.Jets_muonMultiplicity
        jets_multiplicity = c.Jets_multiplicity
        jets_electronMultiplicity = c.Jets_electronMultiplicity
        
        
        jets_partonFlavor = c.Jets_partonFlavor
        jets_qgLikelihood = c.Jets_qgLikelihood
        
        for tracksOb in analysis_ntuples.tracksObs:
            trackObs[tracksOb] = getattr(c, tracksOb)
        
        for pionsOb in analysis_ntuples.pionsObs:
            pionsObs[pionsOb] = getattr(c, pionsOb)
        
        for photonOb in analysis_ntuples.photonObs:
            photonObs[photonOb] = getattr(c, photonOb)
        
        muons = []
        if dy:
           
            muons, invMass = getDyMuons(c)
            if muons is None:
                continue
            
            metVec = TLorentzVector()
            metVec.SetPtEtaPhiE(MET,0,METPhi,MET)
            
            metVec += c.Muons[muons[0]]
            metVec += c.Muons[muons[1]]
            
            MET = abs(metVec.Pt())
            
            if MET > 3000:
                print "HERE WE GO!!!"
                print "c.MET=", c.MET, "metVec=", metVec.Pt(), "MET=", MET
                print "c.Muons[muons[0]].Pt()=", c.Muons[muons[0]].Pt(), "c.Muons[muons[1]].Pt()=", c.Muons[muons[1]].Pt()
                print "-------"
            
            METPhi = metVec.Phi()
            
            jetsHt = [i for i in range(len(c.Jets)) if c.Jets[i].Pt() >= 30 and abs(c.Jets[i].Eta()) <= 2.4 and abs(c.Muons[muons[0]].DeltaR(c.Jets[i])) > 0.1 and abs(c.Muons[muons[1]].DeltaR(c.Jets[i])) > 0.1]
            jetsMht = [i for i in range(len(c.Jets)) if c.Jets[i].Pt() >= 30 and abs(c.Jets[i].Eta()) <= 5 and abs(c.Muons[muons[0]].DeltaR(c.Jets[i])) > 0.1 and abs(c.Muons[muons[1]].DeltaR(c.Jets[i])) > 0.1]
            
            #print "jetsHt=", jetsHt
            #print "jetsMht=", jetsMht
            
            HT = 0
            for i in jetsHt:
                HT += c.Jets[i].Pt()
            MhtVec = TLorentzVector()
            metVec.SetPtEtaPhiE(0,0,0,0)
            for i in jetsMht:
                MhtVec -= c.Jets[i]
            MHT = MhtVec.Pt()
            MHTPhi = MhtVec.Phi()
            
            jets = ROOT.std.vector(TLorentzVector)()
            jets_bDiscriminatorCSV = ROOT.std.vector(double)()
            jets_bJetTagDeepCSVBvsAll = ROOT.std.vector(double)()
            
            jets_electronEnergyFraction = ROOT.std.vector(double)()
            jets_muonEnergyFraction = ROOT.std.vector(double)()
            
            jets_muonMultiplicity = ROOT.std.vector(int)()
            jets_multiplicity = ROOT.std.vector(int)()
            jets_electronMultiplicity = ROOT.std.vector(int)()
            
            jets_partonFlavor = ROOT.std.vector(int)()
            jets_qgLikelihood = ROOT.std.vector(double)()
            
            for i in range(c.Jets.size()):
                if abs(c.Muons[muons[0]].DeltaR(c.Jets[i])) > 0.1 and abs(c.Muons[muons[1]].DeltaR(c.Jets[i])) > 0.1:
                    jets.push_back(c.Jets[i])
                    jets_bDiscriminatorCSV.push_back(c.Jets_bDiscriminatorCSV[i])
                    jets_bJetTagDeepCSVBvsAll.push_back(c.Jets_bJetTagDeepCSVBvsAll[i])
                    jets_electronEnergyFraction.push_back(c.Jets_electronEnergyFraction[i])
                    jets_muonEnergyFraction.push_back(c.Jets_muonEnergyFraction[i])
                    jets_partonFlavor.push_back(c.Jets_partonFlavor[i])
                    jets_qgLikelihood.push_back(c.Jets_qgLikelihood[i])
                    jets_muonMultiplicity.push_back(c.Jets_muonMultiplicity[i])
                    jets_multiplicity.push_back(c.Jets_multiplicity[i])
                    jets_electronMultiplicity.push_back(c.Jets_electronMultiplicity[i])
            
            for tracksOb in analysis_ntuples.tracksObs:
                trackObs[tracksOb] = ROOT.std.vector(eval(analysis_ntuples.tracksObs[tracksOb]))()
            
            for i in range(c.tracks.size()):
                if abs(c.Muons[muons[0]].DeltaR(c.tracks[i])) > 0.01 and abs(c.Muons[muons[1]].DeltaR(c.tracks[i])) > 0.01:
                    for tracksOb in analysis_ntuples.tracksObs:
                        #print tracksOb, trackObs[tracksOb], getattr(c, tracksOb)[i]
                        if analysis_ntuples.tracksObs[tracksOb] == "bool":
                            trackObs[tracksOb].push_back(bool(getattr(c, tracksOb)[i]))
                        else:
                            trackObs[tracksOb].push_back(getattr(c, tracksOb)[i])
        
        nj, btagsLoose, ljet = analysis_ntuples.eventNumberOfJets25Pt2_4Eta_Loose(jets, jets_bDiscriminatorCSV)
        nj, btagsMedium, ljet = analysis_ntuples.eventNumberOfJets25Pt2_4Eta_Medium(jets, jets_bDiscriminatorCSV)
        nj, btagsDeepLoose, ljet = analysis_ntuples.eventNumberOfJets25Pt2_4Eta_DeepLoose(jets, jets_bJetTagDeepCSVBvsAll)
        nj, btagsDeepMedium, ljet = analysis_ntuples.eventNumberOfJets25Pt2_4Eta_DeepMedium(jets, jets_bJetTagDeepCSVBvsAll)
        
        if ljet is None:
            #print "No ljet:",ljet 
            continue
            
        if no_lepton_selection and btagsDeepMedium > 0:
            continue
        
        afterNj += 1
        
        #if not duoLepton: continue
        var_MinDeltaPhiMetJets[0] = analysis_ntuples.eventMinDeltaPhiMetJets25Pt2_4Eta(jets, MET, METPhi)
        var_MinDeltaPhiMhtJets[0] = analysis_ntuples.eventMinDeltaPhiMhtJets25Pt2_4Eta(jets, MHT, MHTPhi)
        if not dy and not jpsi:
            if var_MinDeltaPhiMetJets[0] < 0.4: continue
            if MHT < 100: continue
            if MET < 120: continue
        #Keep 2 b-tags for two-leptons
        # if two_leptons:
#             if btags > 2: continue
#         else:
#             if btags > 0: continue
                
        ## END PRECUTS##
        
        afterMET += 1
        #if btags > 0: continue
        
        #if nj < 1: continue
        
        #nj, btags, ljet = analysis_ntuples.numberOfJets25Pt2_4Eta_Loose(c)
        
        var_RunNum[0] = c.RunNum
        var_LumiBlockNum[0] = c.LumiBlockNum
        var_EvtNum[0] = c.EvtNum

        var_Met[0] = MET
        var_METPhi[0] = METPhi
        var_Mht[0] = MHT
        var_MHTPhi[0] = MHTPhi
        var_Ht[0] = HT
        var_Mt2[0] = c.MT2
        var_CrossSection[0] = crossSection
        var_NJets[0] = nj
        var_BTagsLoose[0] = btagsLoose
        var_BTagsMedium[0] = btagsMedium
        var_BTagsDeepLoose[0] = btagsDeepLoose
        var_BTagsDeepMedium[0] = btagsDeepMedium
        
        var_LeadingJetPt[0] = jets[ljet].Pt()
        var_LeadingJet = jets[ljet]

        var_MinCsv30[0], var_MaxCsv30[0] = analysis_ntuples.minMaxCsv(jets, jets_bDiscriminatorCSV, 30)
        var_MinCsv25[0], var_MaxCsv25[0] = analysis_ntuples.minMaxCsv(jets, jets_bDiscriminatorCSV, 25)
        
        var_MinDeepCsv30[0], var_MaxDeepCsv30[0] = analysis_ntuples.minMaxCsv(jets, jets_bJetTagDeepCSVBvsAll, 30)
        var_MinDeepCsv25[0], var_MaxDeepCsv25[0] = analysis_ntuples.minMaxCsv(jets, jets_bJetTagDeepCSVBvsAll, 25)
        
        #if var_MaxCsv25[0] > 0.7:
        #    continue
        
        afterPreselection += 1
        
        if not data:
            var_puWeight[0] = c.puWeight
            var_madHT[0] = c.madHT
        else:
            var_puWeight[0] = 1
            var_madHT[0] = 1
        
        takeLeptonsFrom = None
        
        if replace_lepton_collection:
            if currLeptonCollectionMap is None or not currLeptonCollectionMap.contains(c.RunNum, c.LumiBlockNum, c.EvtNum):
                print "NEED NEW LEPTON COLLECTION..."
                if currLeptonCollectionMap is not None:
                    currLeptonCollectionMap.Delete()
                    currLeptonCollectionMap = None
                currLeptonCollection = None
                currLeptonCollectionFileMapFile = utils.getLeptonCollectionFileMapFile(baseFileName)
                if currLeptonCollectionFileMapFile is None:
                    print "FATAL: could not open LeptonCollectionFileMapFile"
                    exit(1)
                print "currLeptonCollectionFileMapFile", currLeptonCollectionFileMapFile
                currLeptonCollectionFileMap = utils.getLeptonCollectionFileMap(currLeptonCollectionFileMapFile, c.RunNum, c.LumiBlockNum, c.EvtNum)
                print "Got currLeptonCollectionFileMap"
                if currLeptonCollectionFileMap is None:
                    print "FATAL: could not find file map. continuing..."
                    exit(1) 
                currLeptonCollectionFileName = currLeptonCollectionFileMap.get(c.RunNum, c.LumiBlockNum, c.EvtNum)
                currLeptonCollectionFileMap.Delete()
                currLeptonCollectionFileMap = None
                print "currLeptonCollectionFileName=", currLeptonCollectionFileName
                
                currLeptonCollectionMap = utils.getLeptonCollection(currLeptonCollectionFileName)
                print "currLeptonCollectionMap=", currLeptonCollectionMap
                currLeptonCollectionFileMapFile.Close()
            
            if currLeptonCollectionMap is None:
                print "FATAL: could not find lepton map for ",c.RunNum, c.LumiBlockNum, c.EvtNum, " continuing..."
                exit(1)
            
            takeLeptonsFrom = currLeptonCollectionMap.get(c.RunNum, c.LumiBlockNum, c.EvtNum)
        else:
            takeLeptonsFrom = c
            # takeLeptonsFrom["Electrons"] = c.Electrons
#             takeLeptonsFrom["Electrons_charge"] = c.Electrons_charge
#             takeLeptonsFrom["Electrons_mediumID"] = c.Electrons_mediumID
#             takeLeptonsFrom["Electrons_passIso"] = c.Electrons_passIso
#             takeLeptonsFrom["Electrons_tightID"] = c.Electrons_tightID
#             takeLeptonsFrom["Electrons_EnergyCorr"] = c.Electrons_EnergyCorr
#             takeLeptonsFrom["Electrons_MiniIso"] = c.Electrons_MiniIso
#             takeLeptonsFrom["Electrons_MT2Activity"] = c.Electrons_MT2Activity
#             takeLeptonsFrom["Electrons_MTW"] = c.Electrons_MTW
#             takeLeptonsFrom["Electrons_TrkEnergyCorr"] = c.Electrons_TrkEnergyCorr
#         
#             takeLeptonsFrom["Muons"] = c.Muons
#             takeLeptonsFrom["Muons_charge"] = c.Muons_charge
#             takeLeptonsFrom["Muons_mediumID"] = c.Muons_mediumID
#             takeLeptonsFrom["Muons_passIso"] = c.Muons_passIso
#             takeLeptonsFrom["Muons_tightID"] = c.Muons_tightID
#             takeLeptonsFrom["Muons_MiniIso"] = c.Muons_MiniIso
#             takeLeptonsFrom["Muons_MT2Activity"] = c.Muons_MT2Activity
#             takeLeptonsFrom["Muons_MTW"] = c.Muons_MTW
             
        if dy:
            #print "muons=", muons
            muons, invMass = getDyMuons(takeLeptonsFrom)
            if muons is None:
                print "WHAT IS GOING ON?"
            
            var_DYMuons = ROOT.std.vector(TLorentzVector)()
            var_DYMuons_charge = ROOT.std.vector(int)()
            var_DYMuons_mediumID = ROOT.std.vector(bool)()
            var_DYMuons_passIso = ROOT.std.vector(bool)()
            var_DYMuons_tightID = ROOT.std.vector(bool)()
            var_DYMuons_MiniIso = ROOT.std.vector(double)()
            var_DYMuons_MT2Activity = ROOT.std.vector(double)()
            var_DYMuons_MTW = ROOT.std.vector(double)()
            
            var_DYMuons.push_back(takeLeptonsFrom.Muons[muons[0]])
            var_DYMuons.push_back(takeLeptonsFrom.Muons[muons[1]])
            
            var_DYMuonsSum = takeLeptonsFrom.Muons[muons[0]] + takeLeptonsFrom.Muons[muons[1]]
            var_DYMuonsInvMass[0] = var_DYMuonsSum.M()
            
            var_DYMuons_charge.push_back(takeLeptonsFrom.Muons_charge[muons[0]])
            var_DYMuons_charge.push_back(takeLeptonsFrom.Muons_charge[muons[1]])
            
            var_DYMuons_mediumID.push_back(bool(takeLeptonsFrom.Muons_mediumID[muons[0]]))
            var_DYMuons_mediumID.push_back(bool(takeLeptonsFrom.Muons_mediumID[muons[1]]))
            
            var_DYMuons_passIso.push_back(bool(takeLeptonsFrom.Muons_passIso[muons[0]]))
            var_DYMuons_passIso.push_back(bool(takeLeptonsFrom.Muons_passIso[muons[1]]))
            
            var_DYMuons_tightID.push_back(bool(takeLeptonsFrom.Muons_tightID[muons[0]]))
            var_DYMuons_tightID.push_back(bool(takeLeptonsFrom.Muons_tightID[muons[1]]))
            
            var_DYMuons_MiniIso.push_back(takeLeptonsFrom.Muons_MiniIso[muons[0]])
            var_DYMuons_MiniIso.push_back(takeLeptonsFrom.Muons_MiniIso[muons[1]])
            
            var_DYMuons_MT2Activity.push_back(takeLeptonsFrom.Muons_MT2Activity[muons[0]])
            var_DYMuons_MT2Activity.push_back(takeLeptonsFrom.Muons_MT2Activity[muons[1]])
            
            var_DYMuons_MTW.push_back(takeLeptonsFrom.Muons_MTW[muons[0]])
            var_DYMuons_MTW.push_back(takeLeptonsFrom.Muons_MTW[muons[1]])
            
            for muonsOb in analysis_ntuples.muonsObs:
                muonsObs[muonsOb] = ROOT.std.vector(eval(analysis_ntuples.muonsObs[muonsOb]))()
            
            for i in range(takeLeptonsFrom.Muons.size()):
                if i != muons[0] and i != muons[1]:
                    for muonsOb in analysis_ntuples.muonsObs:
                        if analysis_ntuples.muonsObs[muonsOb] == "bool":
                            muonsObs[muonsOb].push_back(bool(getattr(takeLeptonsFrom, muonsOb)[i]))
                        else:
                            muonsObs[muonsOb].push_back(getattr(takeLeptonsFrom, muonsOb)[i])
        
        for electronsOb in analysis_ntuples.electronsObs:
            electronsObs[electronsOb] = getattr(takeLeptonsFrom, electronsOb)
        
        if not dy:
            for muonsOb in analysis_ntuples.muonsObs:
                muonsObs[muonsOb] = getattr(takeLeptonsFrom, muonsOb)
        
        
        var_Jets = jets
        var_Jets_bDiscriminatorCSV = jets_bDiscriminatorCSV
        var_Jets_bJetTagDeepCSVBvsAll = jets_bJetTagDeepCSVBvsAll
        var_Jets_electronEnergyFraction = jets_electronEnergyFraction
        var_Jets_muonEnergyFraction = jets_muonEnergyFraction
        
        
        var_Jets_muonMultiplicity = jets_muonMultiplicity
        var_Jets_multiplicity = jets_multiplicity
        var_Jets_electronMultiplicity = jets_electronMultiplicity
        
        
        var_NL[0] = nL
        
        if data:
            var_GenParticles = ROOT.std.vector(TLorentzVector)()
            var_GenParticles_ParentId = ROOT.std.vector(int)()
            var_GenParticles_ParentIdx = ROOT.std.vector(int)()
            var_GenParticles_PdgId = ROOT.std.vector(int)()
            var_GenParticles_Status = ROOT.std.vector(int)()
        else:
            var_GenParticles = c.GenParticles
            var_GenParticles_ParentId = c.GenParticles_ParentId
            var_GenParticles_ParentIdx = c.GenParticles_ParentIdx
            var_GenParticles_PdgId = c.GenParticles_PdgId
            var_GenParticles_Status = c.GenParticles_Status
        
        if not signal:
            var_triggerNames = c.TriggerNames
            var_triggerPass = c.TriggerPass
            var_triggerPrescales = c.TriggerPrescales
            var_triggerVersion = c.TriggerVersion
        
        for electronsCalcOb in analysis_ntuples.electronsCalcObs:
            electronsCalcObs[electronsCalcOb] = ROOT.std.vector(eval(analysis_ntuples.electronsCalcObs[electronsCalcOb]))()
        
        for muonsCalcOb in analysis_ntuples.muonsCalcObs:
            muonsCalcObs[muonsCalcOb] = ROOT.std.vector(eval(analysis_ntuples.muonsCalcObs[muonsCalcOb]))()
        
        for i in range(electronsObs["Electrons"].size()):
            electronsCalcObs["Electrons_deltaRLJ"].push_back(electronsObs["Electrons"][i].DeltaR(var_LeadingJet))
            electronsCalcObs["Electrons_deltaPhiLJ"].push_back(abs(electronsObs["Electrons"][i].DeltaPhi(var_LeadingJet)))
            electronsCalcObs["Electrons_deltaEtaLJ"].push_back(abs(electronsObs["Electrons"][i].Eta() - var_LeadingJet.Eta()))
            min, minCan = analysis_ntuples.minDeltaLepLeps(electronsObs["Electrons"][i], trackObs["tracks"])
            if min is None or min > 0.01 or trackObs["tracks_charge"][minCan] * electronsObs["Electrons_charge"][i] < 0:
                electronsCalcObs["Electrons_ti"].push_back(-1)
            else:
                electronsCalcObs["Electrons_ti"].push_back(minCan)
            
        for i in range(muonsObs["Muons"].size()):
            muonsCalcObs["Muons_deltaRLJ"].push_back(muonsObs["Muons"][i].DeltaR(var_LeadingJet))
            muonsCalcObs["Muons_deltaPhiLJ"].push_back(abs(muonsObs["Muons"][i].DeltaPhi(var_LeadingJet)))
            muonsCalcObs["Muons_deltaEtaLJ"].push_back(abs(muonsObs["Muons"][i].Eta() - var_LeadingJet.Eta()))
            min, minCan = analysis_ntuples.minDeltaLepLeps(muonsObs["Muons"][i], trackObs["tracks"])
            if min is None or min > 0.01 or trackObs["tracks_charge"][minCan] * muonsObs["Muons_charge"][i] < 0:
                muonsCalcObs["Muons_ti"].push_back(-1)
            else:
                muonsCalcObs["Muons_ti"].push_back(minCan)
        
        if not data:
            genElectrons = [ var_GenParticles[i] for i in range(var_GenParticles.size()) if abs(var_GenParticles_PdgId[i]) == 11 ]
            genElectronsIdx = [ i for i in range(var_GenParticles.size()) if abs(var_GenParticles_PdgId[i]) == 11 ]
            genMuons = [ var_GenParticles[i] for i in range(var_GenParticles.size()) if abs(var_GenParticles_PdgId[i]) == 13]
            genMuonsIdx = [ i for i in range(var_GenParticles.size()) if abs(var_GenParticles_PdgId[i]) == 13]
            for i in range(electronsObs["Electrons"].size()):
                signedGenElectrons = [ genElectrons[j] for j in range(len(genElectrons)) if var_GenParticles_PdgId[genElectronsIdx[j]] == -11 *  electronsObs["Electrons_charge"][i] ]
                min, minCan = analysis_ntuples.minDeltaLepLeps(electronsObs["Electrons"][i], signedGenElectrons)
                if min is None or min > 0.01:
                    electronsCalcObs["Electrons_matchGen"].push_back(False)
                else:
                    electronsCalcObs["Electrons_matchGen"].push_back(True)
            for i in range(muonsObs["Muons"].size()):
                signedGenMuons = [ genMuons[j] for j in range(len(genMuons)) if var_GenParticles_PdgId[genMuonsIdx[j]] == -13 *  muonsObs["Muons_charge"][i] ]
                min, minCan = analysis_ntuples.minDeltaLepLeps(muonsObs["Muons"][i], signedGenMuons)
                if min is None or min > 0.01:
                    muonsCalcObs["Muons_matchGen"].push_back(False)
                else:
                    muonsCalcObs["Muons_matchGen"].push_back(True)
        
        for lep in ["Muons", "Electrons"]:
            for CorrJetObs in utils.leptonIsolationList:
                if CorrJetObs == "CorrJetIso":
                    for ptRange in utils.leptonCorrJetIsoPtRange:
                        leptonsCorrJetVars[lep + "_pass" + CorrJetObs + str(ptRange)] = ROOT.std.vector(eval(utils.leptonsCorrJetVecList[CorrJetObs]))()
                else:
                    leptonsCorrJetVars[lep + "_pass" + CorrJetObs] = ROOT.std.vector(eval(utils.leptonsCorrJetVecList[CorrJetObs]))()
        
        isoJets = {"electron" : {"obs" : "Electrons"}, "muon" : {"obs" : "Muons"}}
        for lepIso in utils.leptonIsolationList:
            for lep in isoJets:
                if lepIso == "CorrJetIso":
                    continue
                #elif lepIso == "JetIso":
                #    isoJets[lep][lepIso] =  [var_Jets[j] for j in range(len(var_Jets)) if var_Jets[j].Pt() > 25 and (var_Jets_multiplicity[j] >=10 or eval("var_Jets_" + lep + "EnergyFraction")[j] <= (0.3 if lep == "electron" else 0.1))]
                elif lepIso == "NonJetIso":
                    isoJets[lep][lepIso] = [ var_Jets[j] for j in range(len(var_Jets)) ]# if var_Jets[j].Pt() > 25 ]
        
        for lep in isoJets:

            leptonsVecName = isoJets[lep]["obs"]
            leptonsVec = eval(leptonsVecName.lower() + "Obs")[leptonsVecName]
            
            for i in range(leptonsVec.size()):
                leptonsCorrJetVars[isoJets[lep]["obs"] + "_passNoIso"].push_back(True)
                min, minCan = analysis_ntuples.minDeltaLepLeps(leptonsVec[i], var_Jets)
                if min is None:
                    eval(leptonsVecName.lower() + "CalcObs")[leptonsVecName  + "_minDeltaRJets"].push_back(-1)
                    eval(leptonsVecName.lower() + "CalcObs")[leptonsVecName  + "_closestJet"].push_back(-1)
                    #leptonsCorrJetVars[isoJets[lep]["obs"] + "_passJetIso"].push_back(True)
                    leptonsCorrJetVars[isoJets[lep]["obs"] + "_passNonJetIso"].push_back(True)
                else:
                    eval(leptonsVecName.lower() + "CalcObs")[leptonsVecName  + "_minDeltaRJets"].push_back(min)
                    eval(leptonsVecName.lower() + "CalcObs")[leptonsVecName  + "_closestJet"].push_back(minCan)
        
                    # min, minCan = analysis_ntuples.minDeltaLepLeps(leptonsVec[i], isoJets[lep]["JetIso"])
#                     if min is None or min > 0.4:
#                         leptonsCorrJetVars[isoJets[lep]["obs"] + "_passJetIso"].push_back(True)
#                     else:
#                         leptonsCorrJetVars[isoJets[lep]["obs"] + "_passJetIso"].push_back(False)
                    #min, minCan = analysis_ntuples.minDeltaLepLeps(leptonsVec[i], var_Jets)
                    if min is None or min > 0.4:
                        leptonsCorrJetVars[isoJets[lep]["obs"] + "_passNonJetIso"].push_back(True)
                    else:
                        leptonsCorrJetVars[isoJets[lep]["obs"] + "_passNonJetIso"].push_back(False)
        
        var_Jets_muonCorrected = ROOT.std.vector(TLorentzVector)(var_Jets)
        var_Jets_electronCorrected = ROOT.std.vector(TLorentzVector)(var_Jets)
        
        non_iso_jet_electrons = [ i for i in range(len(electronsObs["Electrons"])) if analysis_ntuples.electronPassesKinematicSelection(i, electronsObs["Electrons"], electronsCalcObs["Electrons_deltaRLJ"]) and electronsCalcObs["Electrons_minDeltaRJets"][i] >= 0 and electronsCalcObs["Electrons_minDeltaRJets"][i] < 0.4 ]
        non_iso_jet_muons = [ i for i in range(len(muonsObs["Muons"])) if analysis_ntuples.muonPassesLooseSelection(i, muonsObs["Muons"], muonsObs["Muons_mediumID"], muonsCalcObs["Muons_deltaRLJ"])and muonsCalcObs["Muons_minDeltaRJets"][i] >= 0 and muonsCalcObs["Muons_minDeltaRJets"][i] < 0.4 ]
        
        for i in non_iso_jet_electrons:
            for j in range(len(var_Jets_electronCorrected)):
                if var_Jets_electronCorrected[j].DeltaR(electronsObs["Electrons"][i]) < 0.4:
                    var_Jets_electronCorrected[j] -= electronsObs["Electrons"][i]
        for i in non_iso_jet_muons:
            for j in range(len(var_Jets_muonCorrected)):
                if var_Jets_muonCorrected[j].DeltaR(muonsObs["Muons"][i]) < 0.4:
                    var_Jets_muonCorrected[j] -= muonsObs["Muons"][i]
        
        for lepIso in utils.leptonIsolationList:
            for lep in isoJets:
                if lepIso != "CorrJetIso":
                    continue
                for ptRange in utils.leptonCorrJetIsoPtRange:
                    isoJets[lep][str(ptRange)] = [eval("var_Jets_" + lep + "Corrected")[j] for j in range(len(eval("var_Jets_" + lep + "Corrected"))) if var_Jets_multiplicity[j] >=10 or (eval("var_Jets_" + lep + "Corrected")[j].E() > 0 and eval("var_Jets_" + lep + "Corrected")[j].Pt() > ptRange)]
          
        for lep in isoJets:
             
            leptonsVecName = isoJets[lep]["obs"]
            leptonsVec = eval(leptonsVecName.lower() + "Obs")[leptonsVecName]
            
            for i in range(leptonsVec.size()):
                min, minCan = analysis_ntuples.minDeltaLepLeps(leptonsVec[i], eval("var_Jets_" + lep + "Corrected"))
                if min is None:
                    eval(leptonsVecName.lower() + "CalcObs")[leptonsVecName  +  "_correctedMinDeltaRJets"].push_back(-1)
                    eval(leptonsVecName.lower() + "CalcObs")[leptonsVecName  +  "_correctedClosestJet"].push_back(-1)
                    for ptRange in utils.leptonCorrJetIsoPtRange:
                        leptonsCorrJetVars[isoJets[lep]["obs"] + "_passCorrJetIso" + str(ptRange)].push_back(True)
                else:
                    eval(leptonsVecName.lower() + "CalcObs")[leptonsVecName  +  "_correctedMinDeltaRJets"].push_back(min)
                    eval(leptonsVecName.lower() + "CalcObs")[leptonsVecName  +  "_correctedClosestJet"].push_back(minCan)
                    
                    for ptRange in utils.leptonCorrJetIsoPtRange:
    
                        min, minCan = analysis_ntuples.minDeltaLepLeps(leptonsVec[i], isoJets[lep][str(ptRange)])
                        if min is None or min > 0.4:
                            leptonsCorrJetVars[isoJets[lep]["obs"] + "_passCorrJetIso" + str(ptRange)].push_back(True)
                        else:
                            leptonsCorrJetVars[isoJets[lep]["obs"] + "_passCorrJetIso" + str(ptRange)].push_back(False)
         
        for lep in ["Muons", "Electrons"]:
            for CorrJetObs in utils.leptonIsolationList:
                if CorrJetObs == "CorrJetIso":
                    for ptRange in utils.leptonCorrJetIsoPtRange:
                        tEvent.SetBranchAddress(lep + "_pass" + CorrJetObs + str(ptRange), leptonsCorrJetVars[lep + "_pass" + CorrJetObs + str(ptRange)])
                else:
                    #print lep + "_pass" + CorrJetObs, leptonsCorrJetVars[lep + "_pass" + CorrJetObs]
                    tEvent.SetBranchAddress(lep + "_pass" + CorrJetObs, leptonsCorrJetVars[lep + "_pass" + CorrJetObs])
        
        tight_electrons = [ electronsObs["Electrons"][i] for i in range(len(electronsObs["Electrons"])) if analysis_ntuples.electronPassesTightSelection(i, electronsObs["Electrons"], leptonsCorrJetVars["Electrons_passCorrJetIso10"], electronsCalcObs["Electrons_deltaRLJ"]) ]
        tight_muons = [ muonsObs["Muons"][i] for i in range(len(muonsObs["Muons"])) if analysis_ntuples.muonPassesTightSelection(i, muonsObs["Muons"], muonsObs["Muons_mediumID"], leptonsCorrJetVars["Muons_passCorrJetIso10"], muonsCalcObs["Muons_deltaRLJ"]) ]
        
        min, minCan = analysis_ntuples.minDeltaLepLeps(var_Jets[ljet], tight_electrons)
        if minCan is None:
            var_LeadingJetMinDeltaRElectrons[0] = -1
        else:
            var_LeadingJetMinDeltaRElectrons[0] = min
            
        min, minCan = analysis_ntuples.minDeltaLepLeps(var_Jets[ljet], tight_muons)
        if minCan is None:
            var_LeadingJetMinDeltaRMuons[0] = -1
        else:
            var_LeadingJetMinDeltaRMuons[0] = min
        
        for vecObs in utils.dileptonObservablesVecList:
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
                            dileptonVars[vecObs + postfix] = ROOT.std.vector(eval(utils.dileptonObservablesVecList[vecObs]))()
                            if postfix == utils.defaultJetIsoSetting:
                                dileptonVars[vecObs] = ROOT.std.vector(eval(utils.dileptonObservablesVecList[vecObs]))()
                            
        foundTwoLeptons = False
        foundSingleLepton = False
        
        var_category[0] = 0
            
        for iso in utils.leptonIsolationList:
            for cat in utils.leptonIsolationCategories:
                ptRanges = [""]
                if iso == "CorrJetIso":
                    ptRanges = utils.leptonCorrJetIsoPtRange

                for ptRange in ptRanges:
                    postfixi = [iso + str(ptRange) + cat]
                    
                    if iso + str(ptRange) + cat == utils.defaultJetIsoSetting:
                        postfixi = [iso + str(ptRange) + cat, ""]
                    
                    #print "default=", utils.defaultJetIsoSetting
                    #print iso + str(ptRange) + cat, postfixi
                    
                    for DTypeObs in utils.dileptonObservablesDTypesList:
                        for postfix in postfixi:
                            if utils.dileptonObservablesDTypesList[DTypeObs] == "bool":
                                dileptonVars[DTypeObs + postfix][0] = 0
                            else:
                                dileptonVars[DTypeObs + postfix][0] = -1
                    
                    leptonsNum = analysis_ntuples.countLeptonsAfterSelection(electronsObs["Electrons"], leptonsCorrJetVars["Electrons_pass" + iso + str(ptRange)], electronsCalcObs["Electrons_deltaRLJ"], electronsObs["Electrons_charge"], muonsObs["Muons"], leptonsCorrJetVars["Muons_pass" + iso + str(ptRange)], muonsObs["Muons_mediumID"], muonsCalcObs["Muons_deltaRLJ"], muonsObs["Muons_charge"], utils.leptonIsolationCategories[cat]["muonPt"], utils.leptonIsolationCategories[cat]["lowPtTightMuons"], muonsObs["Muons_tightID"])
                    for postfix in postfixi:
                        dileptonVars["NSelectionLeptons" + postfix][0] = leptonsNum
                    
                    leptons, leptonsIdx, leptonsCharge, leptonFlavour, same_sign = None, None, None, None, None
                    
                    if jpsi_muons:
                        leptonFlavour = "Muons"
                        same_sign = False
                        leptons, leptonsIdx, leptonsCharge = analysis_ntuples.getTwoJPsiLeptonsAfterSelection(24, 24, muonsObs["Muons"], leptonsCorrJetVars["Muons_pass" + iso + str(ptRange)], muonsObs["Muons_mediumID"], muonsObs["Muons_charge"], utils.leptonIsolationCategories[cat]["muonPt"], utils.leptonIsolationCategories[cat]["lowPtTightMuons"], muonsObs["Muons_tightID"], muonsObs["Muons_passIso"])
                        #print ientry
                        #print ientry, leptons, leptonsIdx, leptonsCharge
                    else:
                        leptons, leptonsIdx, leptonsCharge, leptonFlavour, same_sign = analysis_ntuples.getTwoLeptonsAfterSelection(electronsObs["Electrons"], leptonsCorrJetVars["Electrons_pass" + iso + str(ptRange)], electronsCalcObs["Electrons_deltaRLJ"], electronsObs["Electrons_charge"], muonsObs["Muons"], leptonsCorrJetVars["Muons_pass" + iso + str(ptRange)], muonsObs["Muons_mediumID"], muonsCalcObs["Muons_deltaRLJ"], muonsObs["Muons_charge"], utils.leptonIsolationCategories[cat]["muonPt"], utils.leptonIsolationCategories[cat]["lowPtTightMuons"], muonsObs["Muons_tightID"])
                    
                    if not jpsi_muons and leptons is None:
                        ll, leptonIdx, leptonCharge, leptonFlavour = analysis_ntuples.getSingleLeptonAfterSelection(electronsObs["Electrons"], leptonsCorrJetVars["Electrons_pass" + iso + str(ptRange)], electronsCalcObs["Electrons_deltaRLJ"], electronsObs["Electrons_charge"], muonsObs["Muons"], leptonsCorrJetVars["Muons_pass" + iso + str(ptRange)], muonsObs["Muons_mediumID"], muonsCalcObs["Muons_deltaRLJ"], muonsObs["Muons_charge"], utils.leptonIsolationCategories[cat]["muonPt"], utils.leptonIsolationCategories[cat]["lowPtTightMuons"], muonsObs["Muons_tightID"])
                
                        if ll is not None:
                            if nT > 0 and var_BTagsLoose[0] == 0 or var_BTagsMedium[0] == 0 or var_BTagsDeepLoose[0] == 0 or var_BTagsDeepMedium[0] == 0:
                                var_category[0] = 1
                                foundSingleLepton = True
                    if leptons is not None and (jpsi_muons or var_BTagsLoose[0] < 3 or var_BTagsMedium[0] < 3 or var_BTagsDeepLoose[0] < 3 or var_BTagsDeepMedium[0] < 3):
                    
                        #print var_BTagsLoose[0], var_BTagsMedium[0], var_BTagsDeepLoose[0], var_BTagsDeepMedium[0]
                    
                        foundTwoLeptons = True
                        #print "foundTwoLeptons!!!", ientry
                        #print ientry, leptons, leptonsIdx, leptonsCharge, leptonFlavour, same_sign
                        
                        pt = TLorentzVector()
                        pt.SetPtEtaPhiE(MET,0,METPhi,MET)
                        
                        for postfix in postfixi:
                        
                            #print ientry, postfix, leptons, leptonsIdx, leptonsCharge, leptonFlavour, same_sign
                        
                            dileptonVars["leptons" + postfix].push_back(leptons[0].Clone())
                            dileptonVars["leptons" + postfix].push_back(leptons[1].Clone())
                        
                            dileptonVars["leptonsIdx" + postfix].push_back(leptonsIdx[0])
                            dileptonVars["leptonsIdx" + postfix].push_back(leptonsIdx[1])
                        
                            dileptonVars["leptons_charge" + postfix].push_back(leptonsCharge[0])
                            dileptonVars["leptons_charge" + postfix].push_back(leptonsCharge[1])
                        
                            dileptonVars["leptonFlavour" + postfix] = ROOT.std.string(leptonFlavour)
                        
                            dileptonVars["twoLeptons" + postfix][0] = 1
                        
                            dileptonVars["sameSign" + postfix][0] = 1 if same_sign else 0
                        
                            dileptonVars["invMass" + postfix][0] =  (leptons[0] + leptons[1]).M()
                            dileptonVars["dileptonPt" + postfix][0] = abs((leptons[0] + leptons[1]).Pt())
                            dileptonVars["deltaPhi" + postfix][0] = abs(leptons[0].DeltaPhi(leptons[1]))
                            dileptonVars["deltaEta" + postfix][0] = abs(leptons[0].Eta() - leptons[1].Eta())
                            dileptonVars["deltaR" + postfix][0] = abs(leptons[0].DeltaR(leptons[1]))
                            dileptonVars["pt3" + postfix][0] = analysis_tools.pt3(leptons[0].Pt(),leptons[0].Phi(),leptons[1].Pt(),leptons[1].Phi(),MET,METPhi)
                            dileptonVars["mt1" + postfix][0] = analysis_tools.MT2(MET, METPhi, leptons[0])
                            dileptonVars["mt2" + postfix][0] = analysis_tools.MT2(MET, METPhi, leptons[1])
                            
                            #if leptons[0].Pt() < 1 or leptons[1].Pt() < 1:
                            #    print "FUCK!"
                            #    exit(0)
                            
                            #print postfix
                            #print ientry
                            dileptonVars["mtautau" + postfix][0] = analysis_tools.Mtautau(pt, leptons[0], leptons[1])
                            dileptonVars["deltaEtaLeadingJetDilepton" + postfix][0] = abs((leptons[0] + leptons[1]).Eta() - jets[ljet].Eta())
                            dileptonVars["deltaPhiLeadingJetDilepton" + postfix][0] = abs((leptons[0] + leptons[1]).DeltaPhi(jets[ljet]))
                            dileptonVars["dilepHt" + postfix][0] = analysis_ntuples.htJet25Leps(jets, leptons)
                            dileptonVars["deltaPhiMetLepton1" + postfix][0] = abs(leptons[0].DeltaPhi(pt))
                            dileptonVars["deltaPhiMetLepton2" + postfix][0] = abs(leptons[1].DeltaPhi(pt))
                            
                            
                            if not data:
                                gens = [i for i in range(var_GenParticles.size())]
                                lepCans = []
                                numRealLeptons = 0
        
                                for i in range(len(leptons)):
                                    lepton = leptons[i]
                                    min, minCan = analysis_ntuples.minDeltaRGenParticles(lepton, gens, var_GenParticles)
                                    pdgId = var_GenParticles_ParentId[minCan]
                                    if min > 0.01:
                                        #print "BAD GEN!!! ", min
                                        pdgId = 0
                                    else:
                                        if ((abs(var_GenParticles_PdgId[minCan]) == 13 and leptonFlavour == "Muons") or (abs(var_GenParticles_PdgId[minCan]) == 11 and leptonFlavour == "Electrons")) and leptonsCharge[i] * var_GenParticles_PdgId[minCan] < 0:
                                            numRealLeptons += 1
                                            lepCans.append(minCan)
                                        else:
                                            #print "BAD GEN MATCH! "
                                            pdgId = 0
                                        dileptonVars["leptons_ParentPdgId" + postfix].push_back(pdgId)

                                if bg:
                                    if numRealLeptons == 0:
                                        dileptonVars["ff" + postfix][0] = True
                                    elif numRealLeptons == 1:
                                        dileptonVars["rf" + postfix][0] = True
                                    else:
                                        dileptonVars["rr" + postfix][0] = True
                                        if abs(dileptonVars["leptons_ParentPdgId" + postfix][0]) == abs(dileptonVars["leptons_ParentPdgId" + postfix][1]) == 15:
                                            dileptonVars["tautau" + postfix][0] = True
                
                                        parentIdx = var_GenParticles_ParentIdx[lepCans[0]]
                                        parentIdx2 = var_GenParticles_ParentIdx[lepCans[1]]
                                        if parentIdx == -1 and parentIdx2 == -1:
                                            dileptonVars["other" + postfix][0] = True
                                            if abs(dileptonVars["leptons_ParentPdgId" + postfix][0]) == abs(dileptonVars["leptons_ParentPdgId" + postfix][1]) == 223:
                                                dileptonVars["omega" + postfix][0] = True
                                            elif abs(dileptonVars["leptons_ParentPdgId" + postfix][0]) == abs(dileptonVars["leptons_ParentPdgId" + postfix][1]) == 113:
                                                dileptonVars["rho_0" + postfix][0] = True
                                            elif abs(dileptonVars["leptons_ParentPdgId" + postfix][0]) == abs(dileptonVars["leptons_ParentPdgId" + postfix][1]) == 221:
                                                dileptonVars["eta" + postfix][0] = True
                                            elif abs(dileptonVars["leptons_ParentPdgId" + postfix][0]) == abs(dileptonVars["leptons_ParentPdgId" + postfix][1]) == 333:
                                                dileptonVars["phi" + postfix][0] = True
                                            elif abs(dileptonVars["leptons_ParentPdgId" + postfix][0]) == abs(dileptonVars["leptons_ParentPdgId" + postfix][1]) == 331:
                                                dileptonVars["eta_prime" + postfix][0] = True
                                            elif abs(dileptonVars["leptons_ParentPdgId" + postfix][0]) == abs(dileptonVars["leptons_ParentPdgId" + postfix][1]) == 443:
                                                dileptonVars["j_psi" + postfix][0] = True
                                            elif abs(dileptonVars["leptons_ParentPdgId" + postfix][0]) == abs(dileptonVars["leptons_ParentPdgId" + postfix][1]) == 553:
                                                dileptonVars["upsilon_1" + postfix][0] = True
                                            elif abs(dileptonVars["leptons_ParentPdgId" + postfix][0]) == abs(dileptonVars["leptons_ParentPdgId" + postfix][1]) == 100553:
                                                dileptonVars["upsilon_2" + postfix][0] = True
                                        else:
                                            if var_GenParticles_ParentIdx[lepCans[0]] == var_GenParticles_ParentIdx[lepCans[1]]:
                                                numOfParentChildren = 0
                                                for i in range(var_GenParticles.size()):
                                                    if var_GenParticles_Status[i] == 1 and var_GenParticles_ParentIdx[i] == parentIdx:
                                                        numOfParentChildren += 1
                                                #print "numOfParentChildren=", numOfParentChildren, "var_leptons_ParentPdgId[0]", var_leptons_ParentPdgId[0], "var_GenParticles_PdgId[parentIdx]", var_GenParticles_PdgId[parentIdx], "var_GenParticles_PdgId[parentIdx2]", var_GenParticles_PdgId[parentIdx2]
                                                #print lepCans
                                                if numOfParentChildren == 2:
                                                    dileptonVars["sc" + postfix][0] = True
                                                    if abs(var_GenParticles_PdgId[parentIdx]) == 223:
                                                        dileptonVars["omega" + postfix][0] = True
                                                    elif abs(var_GenParticles_PdgId[parentIdx]) == 113:
                                                        dileptonVars["rho_0" + postfix][0] = True
                                                    elif abs(var_GenParticles_PdgId[parentIdx]) == 221:
                                                        dileptonVars["eta" + postfix][0] = True
                                                    elif abs(var_GenParticles_PdgId[parentIdx]) == 333:
                                                        dileptonVars["phi" + postfix][0] = True
                                                    elif abs(var_GenParticles_PdgId[parentIdx]) == 331:
                                                        dileptonVars["eta_prime" + postfix][0] = True
                                                    elif abs(var_GenParticles_PdgId[parentIdx]) == 443:
                                                        dileptonVars["j_psi" + postfix][0] = True
                                                    elif abs(var_GenParticles_PdgId[parentIdx]) == 553:
                                                        dileptonVars["upsilon_1" + postfix][0] = True
                                                    elif abs(var_GenParticles_PdgId[parentIdx]) == 100553:
                                                        dileptonVars["upsilon_2" + postfix][0] = True
                                                else:
                                                    dileptonVars["n_body" + postfix][0] = True
                                            else:
                                                dileptonVars["tc" + postfix][0] = True
                            
                    for postfix in postfixi:
                        for vecObs in utils.dileptonObservablesVecList:
                            #print "tEvent.SetBranchAddress(" + vecObs + postfix +","+ str(dileptonVars[vecObs + postfix]) + ")"
                            tEvent.SetBranchAddress(vecObs + postfix, dileptonVars[vecObs + postfix])
                        for stringObs in utils.dileptonObservablesStringList:
                            #print "tEvent.SetBranchAddress(" + stringObs + postfix +","+ str(dileptonVars[stringObs + postfix]) + ")"
                            tEvent.SetBranchAddress(stringObs + postfix, dileptonVars[stringObs + postfix])
        
        if not no_lepton_selection and not foundTwoLeptons and not foundSingleLepton:
            continue

        afterLeptons += 1
        
        var_vetoElectronsPassIso[0] = 0 if len([ i for i in range(electronsObs["Electrons"].size()) if electronsObs["Electrons"][i].Pt() > 25 and  bool(electronsObs["Electrons_passIso"][i]) ]) == 0 else 1
        #var_vetoElectronsPassJetIso[0] = 0 if len([ i for i in range(len(var_Electrons)) if var_Electrons[i].Pt() > 25 and  bool(var_Electrons_passJetIso[i]) ]) == 0 else 1
        var_vetoElectronsMediumID[0] = 0 if len([ i for i in range(electronsObs["Electrons"].size()) if electronsObs["Electrons"][i].Pt() > 25 and  bool(electronsObs["Electrons_mediumID"][i]) ]) == 0 else 1
        var_vetoElectronsTightID[0] = 0 if len([ i for i in range(electronsObs["Electrons"].size()) if electronsObs["Electrons"][i].Pt() > 25 and  bool(electronsObs["Electrons_tightID"][i]) ]) == 0 else 1
        
        var_vetoMuonsPassIso[0] = 0 if len([ i for i in range(muonsObs["Muons"].size()) if muonsObs["Muons"][i].Pt() > 25 and  bool(muonsObs["Muons_passIso"][i]) ]) == 0 else 1
        #var_vetoMuonsPassJetIso[0] = 0 if len([ i for i in range(len(var_Muons)) if var_Muons[i].Pt() > 25 and  bool(var_Muons_passJetIso[i]) ]) == 0 else 1
        var_vetoMuonsMediumID[0] = 0 if len([ i for i in range(muonsObs["Muons"].size()) if muonsObs["Muons"][i].Pt() > 25 and  bool(muonsObs["Muons_mediumID"][i]) ]) == 0 else 1
        var_vetoMuonsTightID[0] = 0 if len([ i for i in range(muonsObs["Muons"].size()) if muonsObs["Muons"][i].Pt() > 25 and  bool(muonsObs["Muons_tightID"][i]) ]) == 0 else 1
        
        if dy:
            
            tEvent.SetBranchAddress('DYMuons', var_DYMuons)
            tEvent.SetBranchAddress('DYMuons_charge', var_DYMuons_charge)
            tEvent.SetBranchAddress('DYMuonsSum', var_DYMuonsSum)
            
            tEvent.SetBranchAddress('DYMuons_mediumID', var_DYMuons_mediumID)
            tEvent.SetBranchAddress('DYMuons_passIso', var_DYMuons_passIso)
            tEvent.SetBranchAddress('DYMuons_tightID', var_DYMuons_tightID)
        
            tEvent.SetBranchAddress('DYMuons_MiniIso', var_DYMuons_MiniIso)
            tEvent.SetBranchAddress('DYMuons_MT2Activity', var_DYMuons_MT2Activity)
            tEvent.SetBranchAddress('DYMuons_MTW', var_DYMuons_MTW)

        tEvent.SetBranchAddress('GenParticles', var_GenParticles)
        tEvent.SetBranchAddress('GenParticles_ParentId', var_GenParticles_ParentId)
        tEvent.SetBranchAddress('GenParticles_Status', var_GenParticles_Status)
        tEvent.SetBranchAddress('GenParticles_ParentIdx', var_GenParticles_ParentIdx)
        tEvent.SetBranchAddress('GenParticles_PdgId', var_GenParticles_PdgId)
        tEvent.SetBranchAddress('Jets', var_Jets)
        tEvent.SetBranchAddress('Jets_bDiscriminatorCSV', var_Jets_bDiscriminatorCSV)
        tEvent.SetBranchAddress('Jets_bJetTagDeepCSVBvsAll', var_Jets_bJetTagDeepCSVBvsAll)
        tEvent.SetBranchAddress('Jets_electronEnergyFraction', var_Jets_electronEnergyFraction)
        tEvent.SetBranchAddress('Jets_muonEnergyFraction', var_Jets_muonEnergyFraction)
        #tEvent.SetBranchAddress('Jets_minDeltaRElectrons', var_Jets_minDeltaRElectrons)
        #tEvent.SetBranchAddress('Jets_minDeltaRMuons', var_Jets_minDeltaRMuons)
        tEvent.SetBranchAddress('Jets_muonMultiplicity', var_Jets_muonMultiplicity)
        tEvent.SetBranchAddress('Jets_multiplicity', var_Jets_multiplicity)
        tEvent.SetBranchAddress('Jets_electronMultiplicity', var_Jets_electronMultiplicity)
        
        tEvent.SetBranchAddress('Jets_muonCorrected', var_Jets_muonCorrected)
        tEvent.SetBranchAddress('Jets_electronCorrected', var_Jets_electronCorrected)
        
        for tracksOb in analysis_ntuples.tracksObs:
            tEvent.SetBranchAddress(tracksOb, trackObs[tracksOb])
        
        for pionsOb in analysis_ntuples.pionsObs:
            tEvent.SetBranchAddress(pionsOb, pionsObs[pionsOb])
        
        for photonOb in analysis_ntuples.photonObs:
            tEvent.SetBranchAddress(photonOb, photonObs[photonOb])
        
        for electronsOb in analysis_ntuples.electronsObs:
            tEvent.SetBranchAddress(electronsOb, electronsObs[electronsOb])
        
        for electronsCalcOb in analysis_ntuples.electronsCalcObs:
            tEvent.SetBranchAddress(electronsCalcOb, electronsCalcObs[electronsCalcOb])
        
        for muonsOb in analysis_ntuples.muonsObs:
            tEvent.SetBranchAddress(muonsOb, muonsObs[muonsOb])
        
        for muonsCalcOb in analysis_ntuples.muonsCalcObs:
            tEvent.SetBranchAddress(muonsCalcOb, muonsCalcObs[muonsCalcOb])
        
        tEvent.SetBranchAddress('LeadingJet', var_LeadingJet)
        
        if signal:
            var_Electrons_isZ = ROOT.std.vector(bool)()
            var_Muons_isZ = ROOT.std.vector(bool)()
            
            genZL, genNonZL = analysis_ntuples.classifyGenZLeptons(c)
            
            if genZL is None:
                var_genFlavour = ROOT.std.string("")
                for i in range(electronsObs["Electrons"].size()):
                    var_Electrons_isZ.push_back(False)
                for i in range(muonsObs["Muons"].size()):
                    var_Muons_isZ.push_back(False)
            else:
                if abs(c.GenParticles_PdgId[genZL[0]]) == 11:
                    var_genFlavour = ROOT.std.string("Electrons")
                    for i in range(electronsObs["Electrons"].size()):
                        var_Electrons_isZ.push_back(analysis_ntuples.isLeptonMatchedGen(c.GenParticles, c.GenParticles_PdgId, genZL, genNonZL, i, electronsObs["Electrons"], electronsObs["Electrons_charge"], -11))
                    for i in range(muonsObs["Muons"].size()):
                        var_Muons_isZ.push_back(False)
                else:
                    var_genFlavour = ROOT.std.string("Muons")
                    for i in range(muonsObs["Muons"].size()):
                        var_Muons_isZ.push_back(analysis_ntuples.isLeptonMatchedGen(c.GenParticles, c.GenParticles_PdgId, genZL, genNonZL, i, muonsObs["Muons"], muonsObs["Muons_charge"], -13))
                    for i in range(electronsObs["Electrons"].size()):
                        var_Electrons_isZ.push_back(False)
                        
            tEvent.SetBranchAddress('genFlavour', var_genFlavour)
            tEvent.SetBranchAddress('Electrons_isZ', var_Electrons_isZ)
            tEvent.SetBranchAddress('Muons_isZ', var_Muons_isZ)
        
        if not signal:
            tEvent.SetBranchAddress('TriggerNames', var_triggerNames)
            tEvent.SetBranchAddress('TriggerPass', var_triggerPass)
            tEvent.SetBranchAddress('TriggerPrescales', var_triggerPrescales)
            tEvent.SetBranchAddress('TriggerVersion', var_triggerVersion)

            
        metDHt = 9999999
        if HT != 0:
            metDHt = MET / HT

        var_MetDHt[0] = metDHt
        var_LeadingJetPartonFlavor[0] = jets_partonFlavor[ljet]
        var_LeadingJetQgLikelihood[0] = jets_qgLikelihood[ljet]
        
        
        if not data:    
            vars["tEffhMetMhtRealXMet2016"][0] = tEffhMetMhtRealXMet2016.Eval(var_Met)
            vars["tEffhMetMhtRealXMet2017"][0] = tEffhMetMhtRealXMet2017.Eval(var_Met)
            vars["tEffhMetMhtRealXMet2018"][0] = tEffhMetMhtRealXMet2018.Eval(var_Met)
    
            vars["tEffhMetMhtRealXMht2016"][0] = tEffhMetMhtRealXMht2016.Eval(var_Mht)
            vars["tEffhMetMhtRealXMht2017"][0] = tEffhMetMhtRealXMht2017.Eval(var_Mht)
            vars["tEffhMetMhtRealXMht2018"][0] = tEffhMetMhtRealXMht2018.Eval(var_Mht)
            
            vars["passedMhtMet6pack"][0] = True
            
            #if tree.Met < 200:
            #    print "HERE:", var_tEffhMetMhtRealXMet2016[0]
        else:
            vars["tEffhMetMhtRealXMet2016"][0] = 1
            vars["tEffhMetMhtRealXMet2017"][0] = 1
            vars["tEffhMetMhtRealXMet2018"][0] = 1
    
            vars["tEffhMetMhtRealXMht2016"][0] = 1
            vars["tEffhMetMhtRealXMht2017"][0] = 1
            vars["tEffhMetMhtRealXMht2018"][0] = 1
            
            vars["passedMhtMet6pack"][0] = analysis_ntuples.passTrig(c, "MhtMet6pack")
    
        tEvent.Fill()

    fnew.cd()
    tEvent.Write()
    print 'just created', fnew.GetName()
    print "Total: " + str(nentries)
    print "Right Process: " + str(count)
    print "After MET: " + str(afterMET)
    print "After NJ: " + str(afterNj)
    print "After Preselection: " + str(afterPreselection)
    print "After Leptons: " + str(afterLeptons)
    print "nL:"
    print nLMap
    print "nLGen:"
    print nLGenMap
    print "nLGenZ:"
    print nLGenMapZ

    hHt.Write()
    hHtWeighted.Write()
    hHtAfterMadHt.Write()
    
    if data:
        lumiSecs.Write("lumiSecs") 
    
    fnew.Close()

main()
