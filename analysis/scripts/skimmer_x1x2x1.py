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
        "passedSingleMuPack" :  "bool",
        
        "passed2016BFilter" : "bool",
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
    
    flatObs = {}
    for flatOb in analysis_ntuples.commonFlatObs:
        flatObs[flatOb] = np.zeros(1,dtype=eval(analysis_ntuples.commonFlatObs[flatOb]))
    
    # commonFlatObs = {
#     "RunNum" : "int",
#     "LumiBlockNum" : "int",
#     "EvtNum" : "float",
#     "MET" : "float",
#     "METPhi" : "float",
#     "MT2" : "float",
#     "HT" : "float",
#     "MHT" : "float",
#     "MHTPhi" : "float",
# }
       
    commonCalcFlatObs = {}
    for commonCalcFlatOb in analysis_ntuples.commonCalcFlatObs:
        commonCalcFlatObs[commonCalcFlatOb] = np.zeros(1,dtype=eval(analysis_ntuples.commonCalcFlatObs[commonCalcFlatOb]))
    
   #  commonCalcFlatObs = {
#     "BranchingRatio" : "float",
#     "NJets" : "int",
#     "BTagsLoose" : "int",
#     "BTagsMedium" : "int",
#     "BTagsDeepLoose" : "int",
#     "BTagsDeepMedium" : "int",
#     "MetDHt" : "float",
#     "Mt2" : "float",
#     "NL" : "int",
# }

# bgFlatObs = {
#     "madHT" : "float",
#     "puWeight" : "float",
#     "CrossSection" : "float",
# }

    
   #  var_RunNum = np.zeros(1,dtype=int)
#     var_LumiBlockNum = np.zeros(1,dtype=int)
#     var_EvtNum = np.zeros(1,dtype=long)
#     
#     var_Met = np.zeros(1,dtype=float)
#     var_METPhi = np.zeros(1,dtype=float)
   # var_CrossSection = np.zeros(1,dtype=float)
    #var_BranchingRatio = np.zeros(1,dtype=float)
    
    #var_NJets = np.zeros(1,dtype=int)
    #var_BTagsLoose = np.zeros(1,dtype=int)
    #var_BTagsMedium = np.zeros(1,dtype=int)
    #var_BTagsDeepLoose = np.zeros(1,dtype=int)
    #var_BTagsDeepMedium = np.zeros(1,dtype=int)
    #var_Ht = np.zeros(1,dtype=float)
    #var_MHTPhi = np.zeros(1,dtype=float)
    #var_madHT = np.zeros(1,dtype=float)
    #var_Mht = np.zeros(1,dtype=float)
    #var_MetDHt = np.zeros(1,dtype=float)
    #var_Mt2 = np.zeros(1,dtype=float)
    
    # vetosFlatObs = {
#     "vetoElectronsPassIso" : "bool",
#     "vetoElectronsMediumID" : "bool",
#     "vetoElectronsTightID" : "bool",
#     "vetoMuonsMediumID" : "bool",
#     "vetoMuonsTightID" : "bool",
# }

    vetosFlatObs = {}
    for vetosFlatOb in analysis_ntuples.vetosFlatObs:
        vetosFlatObs[vetosFlatOb] = np.zeros(1,dtype=eval(analysis_ntuples.vetosFlatObs[vetosFlatOb]))
    
    
    # var_vetoElectronsPassIso = np.zeros(1,dtype=bool)
#     var_vetoElectronsMediumID = np.zeros(1,dtype=bool)
#     var_vetoElectronsTightID = np.zeros(1,dtype=bool)
#     
#     var_vetoMuonsPassIso = np.zeros(1,dtype=bool)
#     var_vetoMuonsMediumID = np.zeros(1,dtype=bool)
#     var_vetoMuonsTightID = np.zeros(1,dtype=bool)
#     
#     var_DYMuons = ROOT.std.vector(TLorentzVector)()
#     var_DYMuonsSum = TLorentzVector()
#     var_DYMuonsInvMass = np.zeros(1,dtype=float)
#     var_DYMuons_charge = ROOT.std.vector(int)()
#     var_DYMuons_mediumID = ROOT.std.vector(bool)()
#     var_DYMuons_passIso = ROOT.std.vector(bool)()
#     var_DYMuons_tightID = ROOT.std.vector(bool)()
#     var_DYMuons_MiniIso = ROOT.std.vector(double)()
#     var_DYMuons_MT2Activity = ROOT.std.vector(double)()
#     var_DYMuons_MTW = ROOT.std.vector(double)()
    
    #var_Electrons_isZ = ROOT.std.vector(bool)()
    #var_Muons_isZ = ROOT.std.vector(bool)()
    
#     var_GenParticles = ROOT.std.vector(TLorentzVector)()
#     var_GenParticles_ParentId = ROOT.std.vector(int)()
#     var_GenParticles_ParentIdx = ROOT.std.vector(int)()
#     var_GenParticles_PdgId = ROOT.std.vector(int)()
#     var_GenParticles_Status = ROOT.std.vector(int)()
    
    #var_LeadingJetPt = np.zeros(1,dtype=float)
    #var_NL = np.zeros(1,dtype=int)
    #var_NLGen = np.zeros(1,dtype=int)
    #var_NLGenZ = np.zeros(1,dtype=int)
    #var_puWeight = np.zeros(1,dtype=float)

     ### JETS ###
    
    jetsObs = {}
    for jetsOb in analysis_ntuples.jetsObs:
        jetsObs[jetsOb] = ROOT.std.vector(eval(analysis_ntuples.jetsObs[jetsOb]))()
    
    # jetsObs = {
#     "Jets" : "TLorentzVector",
#     "Jets_bDiscriminatorCSV" : "double",
#     "Jets_bJetTagDeepCSVBvsAll" : "double",
#     "Jets_electronEnergyFraction" : "double",
#     "Jets_muonEnergyFraction" : "double",
#     "Jets_muonMultiplicity" : "int",
#     "Jets_multiplicity" : "int",
#     "Jets_electronMultiplicity" : "int",
#     "Jets_partonFlavor" : "int",
#     "Jets_qgLikelihood" : "double"
# }

    # var_Jets = ROOT.std.vector(TLorentzVector)()
#     var_Jets_bDiscriminatorCSV = ROOT.std.vector(double)()
#     var_Jets_bJetTagDeepCSVBvsAll = ROOT.std.vector(double)()
#     var_Jets_electronEnergyFraction = ROOT.std.vector(double)()
#     var_Jets_muonEnergyFraction = ROOT.std.vector(double)()
#     var_Jets_muonMultiplicity = ROOT.std.vector(int)()
#     var_Jets_multiplicity = ROOT.std.vector(int)()
#     var_Jets_electronMultiplicity = ROOT.std.vector(int)()
#     

#     jetsCalcObs = {
#     "Jets_muonCorrected" : "TLorentzVector",
#     "Jets_electronCorrected" : "TLorentzVector",
# }
    #var_Jets_muonCorrected = ROOT.std.vector(TLorentzVector)()
    #var_Jets_electronCorrected = ROOT.std.vector(TLorentzVector)()
    
    jetsCalcObs = {}
    for jetsCalcOb in analysis_ntuples.jetsCalcObs:
        jetsCalcObs[jetsCalcOb] = ROOT.std.vector(eval(analysis_ntuples.jetsCalcObs[jetsCalcOb]))()
    
    # var_LeadingJetPartonFlavor = np.zeros(1,dtype=int)
#     var_LeadingJetQgLikelihood = np.zeros(1,dtype=float)
#     var_LeadingJetMinDeltaRMuons = np.zeros(1,dtype=float)
#     var_LeadingJetMinDeltaRElectrons = np.zeros(1,dtype=float)
#     
#     var_MinDeltaPhiMetJets = np.zeros(1,dtype=float)
#     var_MinDeltaPhiMhtJets = np.zeros(1,dtype=float)
#     
#     var_MinCsv30 = np.zeros(1,dtype=float)
#     var_MinCsv25 = np.zeros(1,dtype=float)
#     var_MaxCsv30 = np.zeros(1,dtype=float)
#     var_MaxCsv25 = np.zeros(1,dtype=float)
#     
#     var_MinDeepCsv30 = np.zeros(1,dtype=float)
#     var_MinDeepCsv25 = np.zeros(1,dtype=float)
#     var_MaxDeepCsv30 = np.zeros(1,dtype=float)
#     var_MaxDeepCsv25 = np.zeros(1,dtype=float)

    #### TRACKS ####
    tracksObs = {}
    
    for tracksOb in analysis_ntuples.tracksObs:
        tracksObs[tracksOb] = ROOT.std.vector(eval(analysis_ntuples.tracksObs[tracksOb]))()
        
    tracksCalcObs = {}
    for tracksCalcOb in analysis_ntuples.tracksCalcObs:
        tracksCalcObs[tracksCalcOb] = ROOT.std.vector(eval(analysis_ntuples.tracksCalcObs[tracksCalcOb]))()
    
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
    
    ### GEN PARTICLES ###

    genParticlesObs = {}
    for genParticlesOb in analysis_ntuples.genParticlesObs:
        genParticlesObs[genParticlesOb] = ROOT.std.vector(eval(analysis_ntuples.genParticlesObs[genParticlesOb]))()
    
#     genParticlesObs = {
#     "GenParticles" : "TLorentzVector",
#     "GenParticles_ParentId" : "int",
#     "GenParticles_ParentIdx" : "int",
#     "GenParticles_PdgId" : "int",
#     "GenParticles_Status" : "int",
# }
    
    commonObservablesStringObs = {}
    for commonObservablesStringOb in analysis_ntuples.commonObservablesStringList:
        commonObservablesStringObs[commonObservablesStringOb] = ROOT.std.string()
    
    genVecObs = {}
    for genVecOb in utils.genObservablesVecList:
        genVecObs[genVecOb] = ROOT.std.vector(eval(utils.genObservablesVecList[genVecOb]))()
    
    genCalcObs = {}
    for DTypeOb in utils.commonObservablesDTypesList:
        genCalcObs[DTypeOb] = np.zeros(1,dtype=utils.commonObservablesDTypesList[DTypeOb])
    
    #var_category = np.zeros(1,dtype=bool)
    
    leptonsCorrJetVars = {}
    
    for lep in ["Muons", "Electrons", "tracks"]:
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
    
    ### TRIGGER ###
    
    triggerObs = {}
    for triggerOb in analysis_ntuples.triggerObs:
        triggerObs[triggerOb] = ROOT.std.vector(eval(analysis_ntuples.triggerObs[triggerOb]))()

    tEvent = TTree('tEvent','tEvent')
    
    
    
#     tEvent.Branch('RunNum', var_RunNum,'RunNum/I')
#     tEvent.Branch('LumiBlockNum', var_LumiBlockNum,'LumiBlockNum/I')
#     tEvent.Branch('EvtNum', var_EvtNum,'EvtNum/L')
#     
#     
#     tEvent.Branch('Met', var_Met,'Met/D')
#     tEvent.Branch('METPhi', var_METPhi,'METPhi/D')
#     tEvent.Branch('CrossSection', var_CrossSection,'CrossSection/D')
#     tEvent.Branch('BranchingRatio', var_BranchingRatio,'BranchingRatio/D')
#     tEvent.Branch('NJets', var_NJets,'NJets/I')
#     tEvent.Branch('BTagsLoose', var_BTagsLoose,'BTagsLoose/I')
#     tEvent.Branch('BTagsMedium', var_BTagsMedium,'BTagsMedium/I')
#     tEvent.Branch('BTagsDeepLoose', var_BTagsDeepLoose,'BTagsDeepLoose/I')
#     tEvent.Branch('BTagsDeepMedium', var_BTagsDeepMedium,'BTagsDeepMedium/I')
#     
#     tEvent.Branch('NL', var_NL,'NL/I')
#     tEvent.Branch('NLGen', var_NLGen,'NLGen/I')
#     tEvent.Branch('NLGenZ', var_NLGenZ,'NLGenZ/I')
#     tEvent.Branch('Ht', var_Ht,'Ht/D')
#     tEvent.Branch('madHT', var_madHT,'madHT/D')
#     tEvent.Branch('Mht', var_Mht,'Mht/D')
#     tEvent.Branch('MHTPhi', var_MHTPhi,'MHTPhi/D')
#     tEvent.Branch('MetDHt', var_MetDHt,'MetDHt/D')
#     #tEvent.Branch('MetDHt2', var_MetDHt2,'MetDHt2/D')
#     tEvent.Branch('Mt2', var_Mt2,'Mt2/D')
#     tEvent.Branch('puWeight', var_puWeight,'puWeight/D')
#     
#     
#     
#     tEvent.Branch('vetoElectronsPassIso', var_vetoElectronsPassIso,'vetoElectronsPassIso/O')
#     #tEvent.Branch('vetoElectronsPassJetIso', var_vetoElectronsPassJetIso,'vetoElectronsPassJetIso/O')
#     tEvent.Branch('vetoElectronsMediumID', var_vetoElectronsMediumID,'vetoElectronsMediumID/O')
#     tEvent.Branch('vetoElectronsTightID', var_vetoElectronsTightID,'vetoElectronsTightID/O')
#     
#     tEvent.Branch('vetoMuonsPassIso', var_vetoMuonsPassIso,'vetoMuonsPassIso/O')
#     #tEvent.Branch('vetoMuonsPassJetIso', var_vetoMuonsPassJetIso,'vetoMuonsPassJetIso/O')
#     tEvent.Branch('vetoMuonsMediumID', var_vetoMuonsMediumID,'vetoMuonsMediumID/O')
#     tEvent.Branch('vetoMuonsTightID', var_vetoMuonsTightID,'vetoMuonsTightID/O')
#     
#     if signal:
#         tEvent.Branch('Electrons_isZ', 'std::vector<bool>', var_Electrons_isZ)
#         tEvent.Branch('Muons_isZ', 'std::vector<bool>', var_Muons_isZ)
#         tEvent.Branch('genFlavour', 'std::string', var_genFlavour)
    # if dy:
#         tEvent.Branch('DYMuons', 'std::vector<TLorentzVector>', var_DYMuons)
#         tEvent.Branch('DYMuons_charge', 'std::vector<int>', var_DYMuons_charge)
#         tEvent.Branch('DYMuons_mediumID', 'std::vector<bool>', var_DYMuons_mediumID)
#         tEvent.Branch('DYMuons_passIso', 'std::vector<bool>', var_DYMuons_passIso)
#         tEvent.Branch('DYMuons_tightID', 'std::vector<bool>', var_DYMuons_tightID)
#         tEvent.Branch('DYMuons_MiniIso', 'std::vector<double>', var_DYMuons_MiniIso)
#         tEvent.Branch('DYMuons_MT2Activity', 'std::vector<double>', var_DYMuons_MT2Activity)
#         tEvent.Branch('DYMuons_MTW', 'std::vector<double>', var_DYMuons_MTW)
#         tEvent.Branch('DYMuonsSum', 'TLorentzVector', var_DYMuonsSum)
#         tEvent.Branch('DYMuonsInvMass', var_DYMuonsInvMass,'DYMuonsInvMass/D')
    
#     tEvent.Branch('GenParticles', 'std::vector<TLorentzVector>', var_GenParticles)
#     tEvent.Branch('GenParticles_ParentId', 'std::vector<int>', var_GenParticles_ParentId)
#     tEvent.Branch('GenParticles_ParentIdx', 'std::vector<int>', var_GenParticles_ParentIdx)
#     tEvent.Branch('GenParticles_PdgId', 'std::vector<int>', var_GenParticles_PdgId)
#     tEvent.Branch('GenParticles_Status', 'std::vector<int>', var_GenParticles_Status)
# 
#     tEvent.Branch('Jets', 'std::vector<TLorentzVector>', var_Jets)
#     tEvent.Branch('Jets_bDiscriminatorCSV', 'std::vector<double>', var_Jets_bDiscriminatorCSV)
#     tEvent.Branch('Jets_bJetTagDeepCSVBvsAll', 'std::vector<double>', var_Jets_bJetTagDeepCSVBvsAll)
#     
#     tEvent.Branch('Jets_electronEnergyFraction', 'std::vector<double>', var_Jets_electronEnergyFraction)
#     tEvent.Branch('Jets_muonEnergyFraction', 'std::vector<double>', var_Jets_muonEnergyFraction)
#     
#     tEvent.Branch('Jets_muonMultiplicity', 'std::vector<int>', var_Jets_muonMultiplicity)
#     tEvent.Branch('Jets_multiplicity', 'std::vector<int>', var_Jets_multiplicity)
#     tEvent.Branch('Jets_electronMultiplicity', 'std::vector<int>', var_Jets_electronMultiplicity)
#     
#     tEvent.Branch('Jets_muonCorrected', 'std::vector<TLorentzVector>', var_Jets_muonCorrected)
#     tEvent.Branch('Jets_electronCorrected', 'std::vector<TLorentzVector>', var_Jets_electronCorrected)
# 
#     tEvent.Branch('LeadingJetPartonFlavor', var_LeadingJetPartonFlavor,'LeadingJetPartonFlavor/I')
#     tEvent.Branch('LeadingJetQgLikelihood', var_LeadingJetQgLikelihood,'LeadingJetQgLikelihood/D')
#     tEvent.Branch('LeadingJetMinDeltaRMuons', var_LeadingJetMinDeltaRMuons,'LeadingJetMinDeltaRMuons/D')
#     tEvent.Branch('LeadingJetMinDeltaRElectrons', var_LeadingJetMinDeltaRElectrons,'LeadingJetMinDeltaRElectrons/D')
#     
#     tEvent.Branch('MinDeltaPhiMetJets', var_MinDeltaPhiMetJets,'MinDeltaPhiMetJets/D')
#     tEvent.Branch('MinDeltaPhiMhtJets', var_MinDeltaPhiMhtJets,'MinDeltaPhiMhtJets/D')
#     tEvent.Branch('LeadingJetPt', var_LeadingJetPt,'LeadingJetPt/D')

    for flatOb in analysis_ntuples.commonFlatObs:
        print "tEvent.Branch(" + flatOb + "," +  "flatObs[flatOb]" + "," + flatOb + "/" + utils.typeTranslation[analysis_ntuples.commonFlatObs[flatOb]] + ")"
        tEvent.Branch(flatOb, flatObs[flatOb],flatOb + "/" + utils.typeTranslation[analysis_ntuples.commonFlatObs[flatOb]])
     
    for commonCalcFlatOb in analysis_ntuples.commonCalcFlatObs:
        print "tEvent.Branch(" + commonCalcFlatOb  + "," + "commonCalcFlatObs[commonCalcFlatOb]" + "," + commonCalcFlatOb + "/" + utils.typeTranslation[analysis_ntuples.commonCalcFlatObs[commonCalcFlatOb]] + ")"
        tEvent.Branch(commonCalcFlatOb, commonCalcFlatObs[commonCalcFlatOb],commonCalcFlatOb + "/" + utils.typeTranslation[analysis_ntuples.commonCalcFlatObs[commonCalcFlatOb]])
    
    for vetosFlatOb in analysis_ntuples.vetosFlatObs:
        tEvent.Branch(vetosFlatOb, vetosFlatObs[vetosFlatOb],vetosFlatOb + "/" + utils.typeTranslation[analysis_ntuples.vetosFlatObs[vetosFlatOb]])
    
    for jetsOb in analysis_ntuples.jetsObs:
        tEvent.Branch(jetsOb, 'std::vector<' + analysis_ntuples.jetsObs[jetsOb] + '>', jetsObs[jetsOb])
    
    for jetsCalcOb in analysis_ntuples.jetsCalcObs:
        tEvent.Branch(jetsCalcOb, 'std::vector<' + analysis_ntuples.jetsCalcObs[jetsCalcOb] + '>', jetsCalcObs[jetsCalcOb])
    
    if not data:
        for genParticlesOb in analysis_ntuples.genParticlesObs:
            tEvent.Branch(genParticlesOb, 'std::vector<' + analysis_ntuples.genParticlesObs[genParticlesOb] + '>', genParticlesObs[genParticlesOb])
        ## Signal Gen Stuff
        if signal:
            for genVecOb in utils.genObservablesVecList:
                tEvent.Branch(genVecOb, 'std::vector<' + utils.genObservablesVecList[genVecOb] + '>', genVecObs[genVecOb])
            
            for DTypeOb in utils.commonObservablesDTypesList:
                tEvent.Branch("gen_" + DTypeOb, genCalcObs[DTypeOb],"gen_" + DTypeOb + "/" + utils.typeTranslation[utils.commonObservablesDTypesList[DTypeOb]])
    
    for commonObservablesStringOb in analysis_ntuples.commonObservablesStringList:
        tEvent.Branch(commonObservablesStringOb, 'std::string', commonObservablesStringObs[commonObservablesStringOb])
    
    for lep in ["Muons", "Electrons", "tracks"]:
        for CorrJetObs in utils.leptonIsolationList:
            ptRanges = [""]
            if CorrJetObs == "CorrJetIso":
                 ptRanges = utils.leptonCorrJetIsoPtRange
            for ptRange in ptRanges:
                print "tEvent.Branch(" + lep + "_pass" + CorrJetObs + str(ptRange), 'std::vector<' + str(utils.leptonsCorrJetVecList[CorrJetObs]) + '>', leptonsCorrJetVars[lep + "_pass" + CorrJetObs + str(ptRange)], ")"
                tEvent.Branch(lep + "_pass" +  CorrJetObs + str(ptRange), 'std::vector<' + utils.leptonsCorrJetVecList[CorrJetObs] + '>', leptonsCorrJetVars[lep + "_pass" + CorrJetObs + str(ptRange)])
            
    ###### Tracks #######
    
    for tracksOb in analysis_ntuples.tracksObs:
        tEvent.Branch(tracksOb, 'std::vector<' + analysis_ntuples.tracksObs[tracksOb] + '>', tracksObs[tracksOb])
    
    for tracksCalcOb in analysis_ntuples.tracksCalcObs:
        tEvent.Branch(tracksCalcOb, 'std::vector<' + analysis_ntuples.tracksCalcObs[tracksCalcOb] + '>', tracksCalcObs[tracksCalcOb])
    
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
    
    # tEvent.Branch('MinCsv30', var_MinCsv30,'MinCsv30/D')
#     tEvent.Branch('MinCsv25', var_MinCsv25,'MinCsv25/D')
#     tEvent.Branch('MaxCsv30', var_MaxCsv30,'MaxCsv30/D')
#     tEvent.Branch('MaxCsv25', var_MaxCsv25,'MaxCsv25/D')
#     
#     tEvent.Branch('MinDeepCsv30', var_MinDeepCsv30,'MinDeepCsv30/D')
#     tEvent.Branch('MinDeepCsv25', var_MinDeepCsv25,'MinDeepCsv25/D')
#     tEvent.Branch('MaxDeepCsv30', var_MaxDeepCsv30,'MaxDeepCsv30/D')
#     tEvent.Branch('MaxDeepCsv25', var_MaxDeepCsv25,'MaxDeepCsv25/D')
#     
#     tEvent.Branch('category', var_category,'vetoMuonsTightID/O')
    
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
        for triggerOb in analysis_ntuples.triggerObs:
            tEvent.Branch(triggerOb, 'std::vector<' + analysis_ntuples.triggerObs[triggerOb] + '>', triggerObs[triggerOb])
    
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
        
        #var_BranchingRatio[0] = branching_ratio
        commonCalcFlatObs["BranchingRatio"][0] = branching_ratio
        commonCalcFlatObs["NLGen"][0] = nLGen
        commonCalcFlatObs["NLGenZ"][0] = nLGenZ
    
        #### PRECUTS ###
        if not signal:
            vars["passed2016BFilter"][0] = analysis_ntuples.passed2016BFilter(c, data)
        else:
            vars["passed2016BFilter"][0] = True
        
        for tracksOb in analysis_ntuples.tracksObs:
            tracksObs[tracksOb] = getattr(c, tracksOb)
        
        for pionsOb in analysis_ntuples.pionsObs:
            pionsObs[pionsOb] = getattr(c, pionsOb)
        
        for photonOb in analysis_ntuples.photonObs:
            photonObs[photonOb] = getattr(c, photonOb)
        
        for jetsOb in analysis_ntuples.jetsObs:
            jetsObs[jetsOb] = getattr(c, jetsOb)
        
        nj, btagsLoose, ljet = analysis_ntuples.eventNumberOfJets25Pt2_4Eta_Loose(c.Jets, c.Jets_bDiscriminatorCSV)
        nj, btagsMedium, ljet = analysis_ntuples.eventNumberOfJets25Pt2_4Eta_Medium(c.Jets, c.Jets_bDiscriminatorCSV)
        nj, btagsDeepLoose, ljet = analysis_ntuples.eventNumberOfJets25Pt2_4Eta_DeepLoose(c.Jets, c.Jets_bJetTagDeepCSVBvsAll)
        nj, btagsDeepMedium, ljet = analysis_ntuples.eventNumberOfJets25Pt2_4Eta_DeepMedium(c.Jets, c.Jets_bJetTagDeepCSVBvsAll)
        
        if ljet is None and not jpsi:
            #print "No ljet:",ljet 
            continue
            
        if no_lepton_selection and btagsDeepMedium > 0:
            continue
        
        afterNj += 1
        
        #if not duoLepton: continue
        commonCalcFlatObs["MinDeltaPhiMetJets"][0] = analysis_ntuples.eventMinDeltaPhiMetJets25Pt2_4Eta(c.Jets, c.MET, c.METPhi)
        commonCalcFlatObs["MinDeltaPhiMhtJets"][0] = analysis_ntuples.eventMinDeltaPhiMhtJets25Pt2_4Eta(c.Jets, c.MHT, c.MHTPhi)
        if not dy and not jpsi:
            if commonCalcFlatObs["MinDeltaPhiMetJets"][0] < 0.4: continue
            if c.MHT < 100: continue
            if c.MET < 120: continue
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
        
        for flatOb in flatObs:
            flatObs[flatOb][0] = getattr(c, flatOb)
    
    
        commonCalcFlatObs["CrossSection"][0] = crossSection
        commonCalcFlatObs["NJets"][0] = nj
        commonCalcFlatObs["BTagsLoose"][0] = btagsLoose
        commonCalcFlatObs["BTagsMedium"][0] = btagsMedium
        commonCalcFlatObs["BTagsDeepLoose"][0] = btagsDeepLoose
        commonCalcFlatObs["BTagsDeepMedium"][0] = btagsDeepMedium
        
        if ljet is None:
            commonCalcFlatObs["LeadingJetPt"][0] = -1
            var_LeadingJet = TLorentzVector()
        else:
            commonCalcFlatObs["LeadingJetPt"][0] = c.Jets[ljet].Pt()
            var_LeadingJet = c.Jets[ljet]

        commonCalcFlatObs["MinCsv30"][0], commonCalcFlatObs["MaxCsv30"][0] = analysis_ntuples.minMaxCsv(c.Jets, c.Jets_bDiscriminatorCSV, 30)
        commonCalcFlatObs["MinCsv25"][0], commonCalcFlatObs["MaxCsv25"][0] = analysis_ntuples.minMaxCsv(c.Jets, c.Jets_bDiscriminatorCSV, 25)
        
        commonCalcFlatObs["MinDeepCsv30"][0], commonCalcFlatObs["MaxDeepCsv30"][0] = analysis_ntuples.minMaxCsv(c.Jets, c.Jets_bJetTagDeepCSVBvsAll, 30)
        commonCalcFlatObs["MinDeepCsv25"][0], commonCalcFlatObs["MaxDeepCsv25"][0] = analysis_ntuples.minMaxCsv(c.Jets, c.Jets_bJetTagDeepCSVBvsAll, 25)
        
        #if var_MaxCsv25[0] > 0.7:
        #    continue
        
        afterPreselection += 1
        
        if not data:
            commonCalcFlatObs["puWeight"][0] = c.puWeight
            commonCalcFlatObs["madHT"][0] = c.madHT
        else:
            commonCalcFlatObs["puWeight"][0] = 1
            commonCalcFlatObs["madHT"][0] = 1
        
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

        for electronsOb in analysis_ntuples.electronsObs:
            electronsObs[electronsOb] = getattr(takeLeptonsFrom, electronsOb)
        
        if not dy:
            for muonsOb in analysis_ntuples.muonsObs:
                muonsObs[muonsOb] = getattr(takeLeptonsFrom, muonsOb)
        
        commonCalcFlatObs["NL"][0] = nL
        
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
        
        for tracksCalcOb in analysis_ntuples.tracksCalcObs:
            tracksCalcObs[tracksCalcOb] = ROOT.std.vector(eval(analysis_ntuples.tracksCalcObs[tracksCalcOb]))()
        
        for i in range(electronsObs["Electrons"].size()):
            electronsCalcObs["Electrons_deltaRLJ"].push_back(electronsObs["Electrons"][i].DeltaR(var_LeadingJet))
            electronsCalcObs["Electrons_deltaPhiLJ"].push_back(abs(electronsObs["Electrons"][i].DeltaPhi(var_LeadingJet)))
            electronsCalcObs["Electrons_deltaEtaLJ"].push_back(abs(electronsObs["Electrons"][i].Eta() - var_LeadingJet.Eta()))
            min, minCan = analysis_ntuples.minDeltaLepLeps(electronsObs["Electrons"][i], tracksObs["tracks"])
            if min is None or min > 0.01 or tracksObs["tracks_charge"][minCan] * electronsObs["Electrons_charge"][i] < 0:
                electronsCalcObs["Electrons_ti"].push_back(-1)
            else:
                electronsCalcObs["Electrons_ti"].push_back(minCan)
            
        for i in range(muonsObs["Muons"].size()):
            muonsCalcObs["Muons_deltaRLJ"].push_back(muonsObs["Muons"][i].DeltaR(var_LeadingJet))
            muonsCalcObs["Muons_deltaPhiLJ"].push_back(abs(muonsObs["Muons"][i].DeltaPhi(var_LeadingJet)))
            muonsCalcObs["Muons_deltaEtaLJ"].push_back(abs(muonsObs["Muons"][i].Eta() - var_LeadingJet.Eta()))
            min, minCan = analysis_ntuples.minDeltaLepLeps(muonsObs["Muons"][i], tracksObs["tracks"])
            if min is None or min > 0.01 or tracksObs["tracks_charge"][minCan] * muonsObs["Muons_charge"][i] < 0:
                muonsCalcObs["Muons_ti"].push_back(-1)
            else:
                muonsCalcObs["Muons_ti"].push_back(minCan)
        
        for i in range(tracksObs["tracks"].size()):
            tracksCalcObs["tracks_deltaRLJ"].push_back(tracksObs["tracks"][i].DeltaR(var_LeadingJet))
            tracksCalcObs["tracks_deltaPhiLJ"].push_back(abs(tracksObs["tracks"][i].DeltaPhi(var_LeadingJet)))
            tracksCalcObs["tracks_deltaEtaLJ"].push_back(abs(tracksObs["tracks"][i].Eta() - var_LeadingJet.Eta()))
        
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
            for i in range(tracksObs["tracks"].size()):
                signedGenElectrons = [ genElectrons[j] for j in range(len(genElectrons)) if var_GenParticles_PdgId[genElectronsIdx[j]] == -11 *  tracksObs["tracks_charge"][i] ]
                signedGenMuons = [ genMuons[j] for j in range(len(genMuons)) if var_GenParticles_PdgId[genMuonsIdx[j]] == -13 *  tracksObs["tracks_charge"][i] ]
                min, minCan = analysis_ntuples.minDeltaLepLeps(tracksObs["tracks"][i], signedGenMuons)
                if min is None or min > 0.01:
                    min, minCan = analysis_ntuples.minDeltaLepLeps(tracksObs["tracks"][i], signedGenElectrons)
                    if min is None or min > 0.01:
                        muonsCalcObs["Muons_matchGen"].push_back(False)
                    else:
                        muonsCalcObs["Muons_matchGen"].push_back(True)
                else:
                    muonsCalcObs["Muons_matchGen"].push_back(True)
        
        for lep in ["Muons", "Electrons", "tracks"]:
            for CorrJetObs in utils.leptonIsolationList:
                if CorrJetObs == "CorrJetIso":
                    for ptRange in utils.leptonCorrJetIsoPtRange:
                        leptonsCorrJetVars[lep + "_pass" + CorrJetObs + str(ptRange)] = ROOT.std.vector(eval(utils.leptonsCorrJetVecList[CorrJetObs]))()
                else:
                    leptonsCorrJetVars[lep + "_pass" + CorrJetObs] = ROOT.std.vector(eval(utils.leptonsCorrJetVecList[CorrJetObs]))()
        
        isoJets = {"electron" : {"obs" : "Electrons"}, "muon" : {"obs" : "Muons"}, "track" : {"obs" : "tracks"}}
        for lepIso in utils.leptonIsolationList:
            for lep in isoJets:
                if lepIso == "CorrJetIso":
                    continue
                #elif lepIso == "JetIso":
                #    isoJets[lep][lepIso] =  [var_Jets[j] for j in range(len(var_Jets)) if var_Jets[j].Pt() > 25 and (var_Jets_multiplicity[j] >=10 or eval("var_Jets_" + lep + "EnergyFraction")[j] <= (0.3 if lep == "electron" else 0.1))]
                elif lepIso == "NonJetIso":
                    isoJets[lep][lepIso] = [ c.Jets[j] for j in range(len(c.Jets)) ]# if var_Jets[j].Pt() > 25 ]
        
        for lep in isoJets:

            leptonsVecName = isoJets[lep]["obs"]
            leptonsVec = eval(leptonsVecName.lower() + "Obs")[leptonsVecName]
            
            for i in range(leptonsVec.size()):
                leptonsCorrJetVars[isoJets[lep]["obs"] + "_passNoIso"].push_back(True)
                min, minCan = analysis_ntuples.minDeltaLepLeps(leptonsVec[i], c.Jets)
                if min is None:
                    eval(leptonsVecName.lower() + "CalcObs")[leptonsVecName  + "_minDeltaRJets"].push_back(-1)
                    eval(leptonsVecName.lower() + "CalcObs")[leptonsVecName  + "_closestJet"].push_back(-1)
                    #leptonsCorrJetVars[isoJets[lep]["obs"] + "_passJetIso"].push_back(True)
                    #leptonsCorrJetVars[isoJets[lep]["obs"] + "_passNonJetIso"].push_back(True)
                else:
                    eval(leptonsVecName.lower() + "CalcObs")[leptonsVecName  + "_minDeltaRJets"].push_back(min)
                    eval(leptonsVecName.lower() + "CalcObs")[leptonsVecName  + "_closestJet"].push_back(minCan)
        
                    # min, minCan = analysis_ntuples.minDeltaLepLeps(leptonsVec[i], isoJets[lep]["JetIso"])
#                     if min is None or min > 0.4:
#                         leptonsCorrJetVars[isoJets[lep]["obs"] + "_passJetIso"].push_back(True)
#                     else:
#                         leptonsCorrJetVars[isoJets[lep]["obs"] + "_passJetIso"].push_back(False)
                    #min, minCan = analysis_ntuples.minDeltaLepLeps(leptonsVec[i], var_Jets)
                    # if min is None or min > 0.4:
#                         leptonsCorrJetVars[isoJets[lep]["obs"] + "_passNonJetIso"].push_back(True)
#                     else:
#                         leptonsCorrJetVars[isoJets[lep]["obs"] + "_passNonJetIso"].push_back(False)
        
        jetsCalcObs["Jets_muonCorrected"] = ROOT.std.vector(TLorentzVector)(c.Jets)
        jetsCalcObs["Jets_electronCorrected"] = ROOT.std.vector(TLorentzVector)(c.Jets)
        jetsCalcObs["Jets_trackCorrected"] = ROOT.std.vector(TLorentzVector)(c.Jets)
        
        #non_iso_jet_electrons = [ i for i in range(len(electronsObs["Electrons"])) if analysis_ntuples.electronPassesKinematicSelection(i, electronsObs["Electrons"], electronsCalcObs["Electrons_deltaRLJ"]) and electronsCalcObs["Electrons_minDeltaRJets"][i] >= 0 and electronsCalcObs["Electrons_minDeltaRJets"][i] < 0.4 ]
        #non_iso_jet_muons = [ i for i in range(len(muonsObs["Muons"])) if analysis_ntuples.muonPassesLooseSelection(i, muonsObs["Muons"], muonsObs["Muons_mediumID"], muonsCalcObs["Muons_deltaRLJ"])and muonsCalcObs["Muons_minDeltaRJets"][i] >= 0 and muonsCalcObs["Muons_minDeltaRJets"][i] < 0.4 ]
        
        # changing this definition. We no longer ignore high-Pt leptons, and we no longer look at the leading jet
        non_iso_jet_electrons = [ i for i in range(len(electronsObs["Electrons"])) if electronsCalcObs["Electrons_minDeltaRJets"][i] >= 0 and electronsCalcObs["Electrons_minDeltaRJets"][i] < 0.4 ]
        non_iso_jet_muons = [ i for i in range(len(muonsObs["Muons"])) if analysis_ntuples.muonPassesJetIsoSelection(i, muonsObs["Muons"], muonsObs["Muons_mediumID"]) and muonsCalcObs["Muons_minDeltaRJets"][i] >= 0 and muonsCalcObs["Muons_minDeltaRJets"][i] < 0.4 ]
        non_iso_jet_tracks = [ i for i in range(len(c.tracks)) if abs(c.tracks[i].Eta()) < 2.4 and c.tracks_trkRelIso[i] < 0.1 and c.tracks_dxyVtx[i] < 0.02 and c.tracks_dzVtx[i] < 0.05 and tracksCalcObs["tracks_minDeltaRJets"][i] >= 0 and tracksCalcObs["tracks_minDeltaRJets"][i] < 0.4]
        
        for i in non_iso_jet_electrons:
            for j in range(jetsCalcObs["Jets_electronCorrected"].size()):
                if jetsCalcObs["Jets_electronCorrected"][j].DeltaR(electronsObs["Electrons"][i]) < 0.4:
                    jetsCalcObs["Jets_electronCorrected"][j] -= electronsObs["Electrons"][i]
        for i in non_iso_jet_muons:
            for j in range(jetsCalcObs["Jets_muonCorrected"].size()):
                if jetsCalcObs["Jets_muonCorrected"][j].DeltaR(muonsObs["Muons"][i]) < 0.4:
                    jetsCalcObs["Jets_muonCorrected"][j] -= muonsObs["Muons"][i]
        for i in non_iso_jet_tracks:
            for j in range(jetsCalcObs["Jets_trackCorrected"].size()):
                if jetsCalcObs["Jets_trackCorrected"][j].DeltaR(c.tracks[i]) < 0.4:
                    jetsCalcObs["Jets_trackCorrected"][j] -= c.tracks[i]
        
        for lepIso in utils.leptonIsolationList:
            for lep in isoJets:
                if lepIso != "CorrJetIso":
                    continue
                for ptRange in utils.leptonCorrJetIsoPtRange:
                    isoJets[lep][str(ptRange)] = [jetsCalcObs["Jets_" + lep + "Corrected"][j] for j in range(len(jetsCalcObs["Jets_" + lep + "Corrected"])) if c.Jets_multiplicity[j] >=10 or (jetsCalcObs["Jets_" + lep + "Corrected"][j].E() > 0 and jetsCalcObs["Jets_" + lep + "Corrected"][j].Pt() > ptRange)]
          
        for lep in isoJets:
             
            leptonsVecName = isoJets[lep]["obs"]
            leptonsVec = eval(leptonsVecName.lower() + "Obs")[leptonsVecName]
            
            for i in range(leptonsVec.size()):
                min, minCan = analysis_ntuples.minDeltaLepLeps(leptonsVec[i], jetsCalcObs["Jets_" + lep + "Corrected"])
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
         
        for lep in ["Muons", "Electrons", "tracks"]:
            for CorrJetObs in utils.leptonIsolationList:
                if CorrJetObs == "CorrJetIso":
                    for ptRange in utils.leptonCorrJetIsoPtRange:
                        tEvent.SetBranchAddress(lep + "_pass" + CorrJetObs + str(ptRange), leptonsCorrJetVars[lep + "_pass" + CorrJetObs + str(ptRange)])
                else:
                    #print lep + "_pass" + CorrJetObs, leptonsCorrJetVars[lep + "_pass" + CorrJetObs]
                    tEvent.SetBranchAddress(lep + "_pass" + CorrJetObs, leptonsCorrJetVars[lep + "_pass" + CorrJetObs])
        
        tight_electrons = [ electronsObs["Electrons"][i] for i in range(len(electronsObs["Electrons"])) if analysis_ntuples.electronPassesTightSelection(i, electronsObs["Electrons"], leptonsCorrJetVars["Electrons_passCorrJetIso10"], electronsCalcObs["Electrons_deltaRLJ"]) ]
        tight_muons = [ muonsObs["Muons"][i] for i in range(len(muonsObs["Muons"])) if analysis_ntuples.muonPassesTightSelection(i, muonsObs["Muons"], muonsObs["Muons_mediumID"], leptonsCorrJetVars["Muons_passCorrJetIso10"], muonsCalcObs["Muons_deltaRLJ"]) ]
        
        min, minCan = analysis_ntuples.minDeltaLepLeps(var_LeadingJet, tight_electrons)
        if minCan is None:
            commonCalcFlatObs["LeadingJetMinDeltaRElectrons"][0] = -1
        else:
            commonCalcFlatObs["LeadingJetMinDeltaRElectrons"][0] = min
            
        min, minCan = analysis_ntuples.minDeltaLepLeps(var_LeadingJet, tight_muons)
        if minCan is None:
            commonCalcFlatObs["LeadingJetMinDeltaRMuons"][0] = -1
        else:
            commonCalcFlatObs["LeadingJetMinDeltaRMuons"][0] = min
        
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
        
        commonCalcFlatObs["category"][0] = 0
            
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
                        
                        dileptonVars["vetoElectrons" + postfix][0] = 0 if len([ i for i in range(electronsObs["Electrons"].size()) if electronsObs["Electrons"][i].Pt() > 20 and bool(leptonsCorrJetVars["Electrons_pass" + iso + str(ptRange)][i]) ]) == 0 else 1
                        dileptonVars["vetoMuons" + postfix][0] = 0 if len([ i for i in range(muonsObs["Muons"].size()) if muonsObs["Muons"][i].Pt() > 20 and  bool(leptonsCorrJetVars["Muons_pass" + iso + str(ptRange)][i]) ]) == 0 else 1
                    
                    leptons, leptonsIdx, leptonsCharge, leptonFlavour, same_sign = None, None, None, None, None
                    
                    if jpsi_muons:
                        leptonFlavour = "Muons"
                        same_sign = False
                        leptons, leptonsIdx, leptonsCharge = analysis_ntuples.getTwoJPsiLeptonsAfterSelection(24, 24, muonsObs["Muons"], leptonsCorrJetVars["Muons_pass" + iso + str(ptRange)], muonsObs["Muons_mediumID"], muonsObs["Muons_charge"], utils.leptonIsolationCategories[cat]["muonPt"], utils.leptonIsolationCategories[cat]["lowPtTightMuons"], muonsObs["Muons_tightID"], muonsObs["Muons_passIso"])
                        #print ientry
                        #print ientry, leptons, leptonsIdx, leptonsCharge
                    else:
                        leptons, leptonsIdx, leptonsCharge, leptonFlavour, same_sign = analysis_ntuples.getTwoLeptonsAfterSelection(electronsObs["Electrons"], leptonsCorrJetVars["Electrons_pass" + iso + str(ptRange)], electronsCalcObs["Electrons_deltaRLJ"], electronsObs["Electrons_charge"], muonsObs["Muons"], leptonsCorrJetVars["Muons_pass" + iso + str(ptRange)], muonsObs["Muons_mediumID"], muonsCalcObs["Muons_deltaRLJ"], muonsObs["Muons_charge"], utils.leptonIsolationCategories[cat]["muonPt"], utils.leptonIsolationCategories[cat]["lowPtTightMuons"], muonsObs["Muons_tightID"])
                    
                    if leptons is None:
                        if jpsi_muons:
                            ll, leptonIdx, t, ti = analysis_ntuples.getSingleJPsiLeptonAfterSelection(24, 24, muonsObs["Muons"], leptonsCorrJetVars["Muons_pass" + iso + str(ptRange)], muonsObs["Muons_mediumID"], muonsObs["Muons_charge"], tracksObs["tracks"], tracksObs["tracks_charge"], utils.leptonIsolationCategories[cat]["muonPt"], utils.leptonIsolationCategories[cat]["lowPtTightMuons"], muonsObs["Muons_tightID"], muonsObs["Muons_passIso"])
                        else:
                            ll, leptonIdx, leptonCharge, leptonFlavour = analysis_ntuples.getSingleLeptonAfterSelection(electronsObs["Electrons"], leptonsCorrJetVars["Electrons_pass" + iso + str(ptRange)], electronsCalcObs["Electrons_deltaRLJ"], electronsObs["Electrons_charge"], muonsObs["Muons"], leptonsCorrJetVars["Muons_pass" + iso + str(ptRange)], muonsObs["Muons_mediumID"], muonsCalcObs["Muons_deltaRLJ"], muonsObs["Muons_charge"], utils.leptonIsolationCategories[cat]["muonPt"], utils.leptonIsolationCategories[cat]["lowPtTightMuons"], muonsObs["Muons_tightID"])
                
                        if ll is not None:
                            if nT > 0 and (jpsi_muons or commonCalcFlatObs["BTagsLoose"][0] == 0 or commonCalcFlatObs["BTagsMedium"][0] == 0 or commonCalcFlatObs["BTagsDeepLoose"][0] == 0 or commonCalcFlatObs["BTagsDeepMedium"][0] == 0):
                                commonCalcFlatObs["category"][0] = 1
                                foundSingleLepton = True
                    if leptons is not None and (jpsi_muons or commonCalcFlatObs["BTagsLoose"][0] < 3 or commonCalcFlatObs["BTagsMedium"][0] < 3 or commonCalcFlatObs["BTagsDeepLoose"][0] < 3 or commonCalcFlatObs["BTagsDeepMedium"][0] < 3):
                    
                        #print var_BTagsLoose[0], var_BTagsMedium[0], var_BTagsDeepLoose[0], var_BTagsDeepMedium[0]
                    
                        foundTwoLeptons = True
                        #print "foundTwoLeptons!!!", ientry
                        #print ientry, leptons, leptonsIdx, leptonsCharge, leptonFlavour, same_sign
                        
                        pt = TLorentzVector()
                        pt.SetPtEtaPhiE(c.MET,0,c.METPhi,c.MET)
                        
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
                            dileptonVars["pt3" + postfix][0] = analysis_tools.pt3(leptons[0].Pt(),leptons[0].Phi(),leptons[1].Pt(),leptons[1].Phi(),c.MET,c.METPhi)
                            dileptonVars["mt1" + postfix][0] = analysis_tools.MT2(c.MET, c.METPhi, leptons[0])
                            dileptonVars["mt2" + postfix][0] = analysis_tools.MT2(c.MET, c.METPhi, leptons[1])
                            
                            #if leptons[0].Pt() < 1 or leptons[1].Pt() < 1:
                            #    print "FUCK!"
                            #    exit(0)
                            
                            #print postfix
                            #print ientry
                            dileptonVars["mtautau" + postfix][0] = analysis_tools.Mtautau(pt, leptons[0], leptons[1])
                            dileptonVars["deltaEtaLeadingJetDilepton" + postfix][0] = abs((leptons[0] + leptons[1]).Eta() - var_LeadingJet.Eta())
                            dileptonVars["deltaPhiLeadingJetDilepton" + postfix][0] = abs((leptons[0] + leptons[1]).DeltaPhi(var_LeadingJet))
                            dileptonVars["dilepHt" + postfix][0] = analysis_ntuples.htJet25Leps(c.Jets, leptons)
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
        
        for i in range(len(tracksObs["tracks"])):
            t = tracksObs["tracks"][i]
            
            min, minCan = analysis_ntuples.minDeltaLepLeps(tracksObs["tracks"][i], electronsObs["Electrons"])
            if min is None or min > 0.01 or electronsObs["Electrons_charge"][minCan] * tracksObs["tracks_charge"][i] < 0:
                tracksCalcObs["tracks_ei"].push_back(-1)
            else:
                tracksCalcObs["tracks_ei"].push_back(minCan)
            
            min, minCan = analysis_ntuples.minDeltaLepLeps(tracksObs["tracks"][i], muonsObs["Muons"])
            if min is None or min > 0.01 or muonsObs["Muons_charge"][minCan] * tracksObs["tracks_charge"][i] < 0:
                tracksCalcObs["tracks_mi"].push_back(-1)
            else:
                tracksCalcObs["tracks_mi"].push_back(minCan)
        
        
        vetosFlatObs["vetoElectronsPassIso"][0] = 0 if len([ i for i in range(electronsObs["Electrons"].size()) if electronsObs["Electrons"][i].Pt() > 20 and  bool(electronsObs["Electrons_passIso"][i]) ]) == 0 else 1
        #var_vetoElectronsPassJetIso[0] = 0 if len([ i for i in range(len(var_Electrons)) if var_Electrons[i].Pt() > 25 and  bool(var_Electrons_passJetIso[i]) ]) == 0 else 1
        vetosFlatObs["vetoElectronsMediumID"][0] = 0 if len([ i for i in range(electronsObs["Electrons"].size()) if electronsObs["Electrons"][i].Pt() > 20 and  bool(electronsObs["Electrons_mediumID"][i]) ]) == 0 else 1
        vetosFlatObs["vetoElectronsTightID"][0] = 0 if len([ i for i in range(electronsObs["Electrons"].size()) if electronsObs["Electrons"][i].Pt() > 20 and  bool(electronsObs["Electrons_tightID"][i]) ]) == 0 else 1
        
        #vetosFlatObs["vetoElectronsJetIso"][0] = 0 if len([ i for i in range(electronsObs["Electrons"].size()) if electronsObs["Electrons"][i].Pt() > 25 and  bool(electronsObs["Electrons_tightID"][i]) ]) == 0 else 1
        
        vetosFlatObs["vetoMuonsPassIso"][0] = 0 if len([ i for i in range(muonsObs["Muons"].size()) if muonsObs["Muons"][i].Pt() > 20 and  bool(muonsObs["Muons_passIso"][i]) ]) == 0 else 1
        #var_vetoMuonsPassJetIso[0] = 0 if len([ i for i in range(len(var_Muons)) if var_Muons[i].Pt() > 25 and  bool(var_Muons_passJetIso[i]) ]) == 0 else 1
        vetosFlatObs["vetoMuonsMediumID"][0] = 0 if len([ i for i in range(muonsObs["Muons"].size()) if muonsObs["Muons"][i].Pt() > 20 and  bool(muonsObs["Muons_mediumID"][i]) ]) == 0 else 1
        vetosFlatObs["vetoMuonsTightID"][0] = 0 if len([ i for i in range(muonsObs["Muons"].size()) if muonsObs["Muons"][i].Pt() > 20 and  bool(muonsObs["Muons_tightID"][i]) ]) == 0 else 1
        
        # if dy:
#             
#             tEvent.SetBranchAddress('DYMuons', var_DYMuons)
#             tEvent.SetBranchAddress('DYMuons_charge', var_DYMuons_charge)
#             tEvent.SetBranchAddress('DYMuonsSum', var_DYMuonsSum)
#             
#             tEvent.SetBranchAddress('DYMuons_mediumID', var_DYMuons_mediumID)
#             tEvent.SetBranchAddress('DYMuons_passIso', var_DYMuons_passIso)
#             tEvent.SetBranchAddress('DYMuons_tightID', var_DYMuons_tightID)
#         
#             tEvent.SetBranchAddress('DYMuons_MiniIso', var_DYMuons_MiniIso)
#             tEvent.SetBranchAddress('DYMuons_MT2Activity', var_DYMuons_MT2Activity)
#             tEvent.SetBranchAddress('DYMuons_MTW', var_DYMuons_MTW)

        # tEvent.SetBranchAddress('GenParticles', var_GenParticles)
#         tEvent.SetBranchAddress('GenParticles_ParentId', var_GenParticles_ParentId)
#         tEvent.SetBranchAddress('GenParticles_Status', var_GenParticles_Status)
#         tEvent.SetBranchAddress('GenParticles_ParentIdx', var_GenParticles_ParentIdx)
#         tEvent.SetBranchAddress('GenParticles_PdgId', var_GenParticles_PdgId)
#         tEvent.SetBranchAddress('Jets', var_Jets)
#         tEvent.SetBranchAddress('Jets_bDiscriminatorCSV', var_Jets_bDiscriminatorCSV)
#         tEvent.SetBranchAddress('Jets_bJetTagDeepCSVBvsAll', var_Jets_bJetTagDeepCSVBvsAll)
#         tEvent.SetBranchAddress('Jets_electronEnergyFraction', var_Jets_electronEnergyFraction)
#         tEvent.SetBranchAddress('Jets_muonEnergyFraction', var_Jets_muonEnergyFraction)
#         #tEvent.SetBranchAddress('Jets_minDeltaRElectrons', var_Jets_minDeltaRElectrons)
#         #tEvent.SetBranchAddress('Jets_minDeltaRMuons', var_Jets_minDeltaRMuons)
#         tEvent.SetBranchAddress('Jets_muonMultiplicity', var_Jets_muonMultiplicity)
#         tEvent.SetBranchAddress('Jets_multiplicity', var_Jets_multiplicity)
#         tEvent.SetBranchAddress('Jets_electronMultiplicity', var_Jets_electronMultiplicity)
#         
#         tEvent.SetBranchAddress('Jets_muonCorrected', var_Jets_muonCorrected)
#         tEvent.SetBranchAddress('Jets_electronCorrected', var_Jets_electronCorrected)
        
        
        for jetsOb in analysis_ntuples.jetsObs:
            tEvent.SetBranchAddress(jetsOb, jetsObs[jetsOb])
        
        for jetsCalcOb in analysis_ntuples.jetsCalcObs:
            tEvent.SetBranchAddress(jetsCalcOb, jetsCalcObs[jetsCalcOb])
        
        
        if not data:
            for genParticlesOb in analysis_ntuples.genParticlesObs:
                genParticlesObs[genParticlesOb] = getattr(c, genParticlesOb)
            for genParticlesOb in analysis_ntuples.genParticlesObs:
                tEvent.SetBranchAddress(genParticlesOb, genParticlesObs[genParticlesOb])
    
        for commonObservablesStringOb in analysis_ntuples.commonObservablesStringList:
            tEvent.SetBranchAddress(commonObservablesStringOb, commonObservablesStringObs[commonObservablesStringOb])
   
        for tracksOb in analysis_ntuples.tracksObs:
            tEvent.SetBranchAddress(tracksOb, tracksObs[tracksOb])
        
        for tracksCalcOb in analysis_ntuples.tracksCalcObs:
            tEvent.SetBranchAddress(tracksCalcOb, tracksCalcObs[tracksCalcOb])
        
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
            electronsCalcObs["Electrons_isZ"] = ROOT.std.vector(bool)()
            muonsCalcObs["Muons_isZ"] = ROOT.std.vector(bool)()
            commonObservablesStringObs["genFlavour"] = ROOT.std.string("")
            
            genVecObs["genLeptonsIdx"] = ROOT.std.vector(int)()
            
            genZL, genNonZL = analysis_ntuples.classifyGenZLeptons(c)
            #print len(genZL)
            
            if genZL is None:
                commonObservablesStringObs["genFlavour"] = ROOT.std.string("")
                #print "****"
                #print commonObservablesStringObs["genFlavour"]
                for i in range(electronsObs["Electrons"].size()):
                    electronsCalcObs["Electrons_isZ"].push_back(False)
                for i in range(muonsObs["Muons"].size()):
                    muonsCalcObs["Muons_isZ"].push_back(False)
                for i in range(tracksObs["tracks"].size()):
                    tracksCalcObs["tracks_isZ"].push_back(False)
                
                for ob in genCalcObs:
                    genCalcObs[ob][0] = -1
            else:
                
                if  c.GenParticles[genZL[0]].Pt() > c.GenParticles[genZL[1]]:
                    genVecObs["genLeptonsIdx"].push_back(genZL[0])
                    genVecObs["genLeptonsIdx"].push_back(genZL[1])
                    g1 = c.GenParticles[genZL[0]]
                    g2 = c.GenParticles[genZL[1]]
                else:
                    genVecObs["genLeptonsIdx"].push_back(genZL[1])
                    genVecObs["genLeptonsIdx"].push_back(genZL[0])
                    g2 = c.GenParticles[genZL[0]]
                    g1 = c.GenParticles[genZL[1]]
                
                pt = TLorentzVector()
                pt.SetPtEtaPhiE(c.MET,0,c.METPhi,c.MET)
                
                genCalcObs["invMass"][0] = (g1 + g2).M()
                genCalcObs["dileptonPt"][0] = abs((g1 + g2).Pt())
                genCalcObs["deltaPhi"][0] = abs(g1.DeltaPhi(g2))
                genCalcObs["deltaEta"][0] = abs(g1.Eta() - g2.Eta())
                genCalcObs["deltaR"][0] = abs(g1.DeltaR(g2))
                genCalcObs["pt3"][0] = analysis_tools.pt3(g1.Pt(),g1.Phi(),g2.Pt(),g2.Phi(),c.MET,c.METPhi)
                genCalcObs["mt1"][0] = analysis_tools.MT2(c.MET, c.METPhi, g1)
                genCalcObs["mt2"][0] = analysis_tools.MT2(c.MET, c.METPhi, g2)
                genCalcObs["mtautau"][0] = analysis_tools.Mtautau(pt, g1, g2)
                genCalcObs["deltaEtaLeadingJetDilepton"][0] = abs((g1 + g2).Eta() - var_LeadingJet.Eta())
                genCalcObs["deltaPhiLeadingJetDilepton"][0] = abs((g1 + g2).DeltaPhi(var_LeadingJet))
                genCalcObs["dilepHt"][0] = analysis_ntuples.htJet25Leps(c.Jets, [g1,g2])
                #genCalcObs["deltaPhiMetLepton1"][0] = abs(g1.DeltaPhi(pt))
                #genCalcObs["deltaPhiMetLepton2"][0] = abs(g2.DeltaPhi(pt))
                
                if abs(c.GenParticles_PdgId[genZL[0]]) == 11:
                    commonObservablesStringObs["genFlavour"] = ROOT.std.string("Electrons")
                    for i in range(electronsObs["Electrons"].size()):
                        electronsCalcObs["Electrons_isZ"].push_back(analysis_ntuples.isLeptonMatchedGen(c.GenParticles, c.GenParticles_PdgId, genZL, genNonZL, i, electronsObs["Electrons"], electronsObs["Electrons_charge"], -11))
                    for i in range(muonsObs["Muons"].size()):
                        muonsCalcObs["Muons_isZ"].push_back(False)
                else:
                    commonObservablesStringObs["genFlavour"] = ROOT.std.string("Muons")
                    for i in range(muonsObs["Muons"].size()):
                        muonsCalcObs["Muons_isZ"].push_back(analysis_ntuples.isLeptonMatchedGen(c.GenParticles, c.GenParticles_PdgId, genZL, genNonZL, i, muonsObs["Muons"], muonsObs["Muons_charge"], -13))
                    for i in range(electronsObs["Electrons"].size()):
                        electronsCalcObs["Electrons_isZ"].push_back(False)
                for i in range(tracksObs["tracks"].size()):
                    tracksCalcObs["tracks_isZ"].push_back(analysis_ntuples.isLeptonMatchedGen(c.GenParticles, c.GenParticles_PdgId, genZL, genNonZL, i, tracksObs["tracks"], tracksObs["tracks_charge"], 0))
            
            tEvent.SetBranchAddress('genFlavour', commonObservablesStringObs["genFlavour"])
            tEvent.SetBranchAddress('Electrons_isZ', electronsCalcObs["Electrons_isZ"])
            tEvent.SetBranchAddress('Muons_isZ', muonsCalcObs["Muons_isZ"])
            
            for genVecOb in utils.genObservablesVecList:
                tEvent.SetBranchAddress(genVecOb, genVecObs[genVecOb])
        
        if not signal:
            for triggerOb in analysis_ntuples.triggerObs:
                tEvent.SetBranchAddress(triggerOb, triggerObs[triggerOb])
            
        metDHt = 9999999
        if c.HT != 0:
            metDHt = c.MET / c.HT
        
        commonCalcFlatObs["MetDHt"][0] = metDHt
        
        if not ljet:
            commonCalcFlatObs["LeadingJetPartonFlavor"][0] = -1
            commonCalcFlatObs["LeadingJetQgLikelihood"][0] = -1
        else:
            commonCalcFlatObs["LeadingJetPartonFlavor"][0] = c.Jets_partonFlavor[ljet]
            commonCalcFlatObs["LeadingJetQgLikelihood"][0] = c.Jets_qgLikelihood[ljet]
        
        
        if not data:    
            vars["tEffhMetMhtRealXMet2016"][0] = tEffhMetMhtRealXMet2016.Eval(c.MET)
            vars["tEffhMetMhtRealXMet2017"][0] = tEffhMetMhtRealXMet2017.Eval(c.MET)
            vars["tEffhMetMhtRealXMet2018"][0] = tEffhMetMhtRealXMet2018.Eval(c.MET)
    
            vars["tEffhMetMhtRealXMht2016"][0] = tEffhMetMhtRealXMht2016.Eval(c.MHT)
            vars["tEffhMetMhtRealXMht2017"][0] = tEffhMetMhtRealXMht2017.Eval(c.MHT)
            vars["tEffhMetMhtRealXMht2018"][0] = tEffhMetMhtRealXMht2018.Eval(c.MHT)
            
            vars["passedMhtMet6pack"][0] = True
            vars["passedSingleMuPack"][0] = True
            
            
            
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
            vars["passedSingleMuPack"][0] = analysis_ntuples.passTrig(c, "SingleMuon")
    
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
