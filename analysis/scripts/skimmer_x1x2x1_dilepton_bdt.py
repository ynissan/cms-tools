#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import numpy as np
import os
import xml.etree.ElementTree as ET

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib/classes"))
from lib import analysis_ntuples
from lib import analysis_tools
from lib import utils
from lib import cut_optimisation
from lib import analysis_observables

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

gSystem.Load('LumiSectMap_C')
from ROOT import LumiSectMap

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Create skims for x1x2x1 process with BDTs.')
parser.add_argument('-i', '--input_file', nargs=1, help='Input Filename', required=True)
parser.add_argument('-bdt', '--bdt', nargs=1, help='Dilepton BDT Folder', required=True)

parser.add_argument('-s', '--signal', dest='signal', help='Signal', action='store_true')
parser.add_argument('-bg', '--background', dest='bg', help='Background', action='store_true')
parser.add_argument('-data', '--data', dest='data', help='Data', action='store_true')
parser.add_argument('-dy', '--dy', dest='dy', help='Drell-Yan', action='store_true')
parser.add_argument('-sc', '--same_charge', dest='sc', help='Same Charge', action='store_true')
parser.add_argument('-sam', '--sam', dest='sam', help='Sam Samples', action='store_true')
parser.add_argument('-jpsi_muons', '--jpsi_muons', dest='jpsi_muons', help='JPSI Muons Skim', action='store_true')
args = parser.parse_args()

print args

signal = args.signal
bg = args.bg
data = args.data

input_file = None
if args.input_file:
    input_file = args.input_file[0].strip()

bdt = None
if args.bdt:
    bdt = args.bdt[0]

jpsi_muons = args.jpsi_muons

jpsi = False

if jpsi_muons:
    jpsi = True
    print "Got JPSI"
    if jpsi_muons:
        print "MUONS"
    else:
        print "ELECTRONS"

######## END OF CMDLINE ARGUMENTS ########

vars = {}
bdt_vars_maps = {}
bdt_specs_maps = {}
bdt_readers = {}
branches = {}

def main():
    
    if jpsi:
        utils.defaultJetIsoSetting = "NoIso"
    
    iFile = TFile(input_file, "update")
    #hHt = iFile.Get('hHt')
    tree = iFile.Get('tEvent')
    nentries = tree.GetEntries()
    
    # CREATE VARS, BRANCHES, AND BDT READERS
              
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
                    
                    if iso + str(ptRange) + cat == utils.defaultJetIsoSetting:
                        postfixi = [iso + cuts + cat, ""]
                
                    for postfix in postfixi:
                
                        for DTypeObs in analysis_observables.commonPostBdtObservablesDTypesList:
                            for prefix in ["", "exTrack_"]:
                                sameChargeOptions = [False, True] if prefix == "exTrack_" else [False]
                            
                                for sameCharge in sameChargeOptions:
                            
                                    sc_prefix = "sc_" if sameCharge else ""
                            
                                    vars[sc_prefix + prefix + DTypeObs + postfix] = np.zeros(1,dtype=analysis_observables.commonPostBdtObservablesDTypesList[DTypeObs])
                                    if tree.GetBranchStatus(sc_prefix + prefix + DTypeObs + postfix):
                                        print "Reseting branch", sc_prefix + prefix + DTypeObs + postfix
                                        branches[sc_prefix + prefix + DTypeObs + postfix] = tree.GetBranch(sc_prefix + prefix + DTypeObs + postfix)
                                        branches[sc_prefix + prefix + DTypeObs + postfix].Reset()
                                        tree.SetBranchAddress(sc_prefix + prefix + DTypeObs + postfix, vars[sc_prefix + prefix + DTypeObs + postfix])
                                    else:
                                        print "Branching", sc_prefix + prefix + DTypeObs + postfix
                                        branches[sc_prefix + prefix + DTypeObs + postfix] = tree.Branch(sc_prefix + prefix + DTypeObs + postfix, vars[sc_prefix + prefix + DTypeObs + postfix], sc_prefix + prefix + DTypeObs + postfix + "/" + utils.typeTranslation[analysis_observables.commonPostBdtObservablesDTypesList[DTypeObs]])
                                        tree.SetBranchAddress(sc_prefix + prefix + DTypeObs + postfix, vars[sc_prefix + prefix + DTypeObs + postfix])
                                
                        for DTypeObs in analysis_observables.exclusiveTrackPostBdtObservablesDTypesList:
                        
                            for sameCharge in [False, True]:
                                sc_prefix = "sc_" if sameCharge else ""
                            
                                vars[sc_prefix + DTypeObs + postfix] = np.zeros(1,dtype=analysis_observables.exclusiveTrackPostBdtObservablesDTypesList[DTypeObs])
                                if tree.GetBranchStatus(sc_prefix + DTypeObs + postfix):
                                    print "Reseting branch", sc_prefix + DTypeObs + postfix
                                    branches[sc_prefix + DTypeObs + postfix] = tree.GetBranch(sc_prefix + DTypeObs + postfix)
                                    branches[sc_prefix + DTypeObs + postfix].Reset()
                                    tree.SetBranchAddress(sc_prefix + DTypeObs + postfix, vars[sc_prefix + DTypeObs + postfix])
                                else:
                                    print "Branching", sc_prefix + DTypeObs + postfix
                                    branches[sc_prefix + DTypeObs + postfix] = tree.Branch(sc_prefix + DTypeObs + postfix, vars[sc_prefix + DTypeObs + postfix], sc_prefix + DTypeObs + postfix + "/" + utils.typeTranslation[analysis_observables.exclusiveTrackPostBdtObservablesDTypesList[DTypeObs]])
                                    tree.SetBranchAddress(sc_prefix + DTypeObs + postfix, vars[sc_prefix + DTypeObs + postfix])
                
                    if not jpsi:    
                        for prefix in ["reco", "exTrack"]:
                            for lep in ["Muons", "Electrons"]:
                                dirname = prefix + lep + iso + cat + cuts
                                name = prefix + lep + iso + cuts + cat
                                bdt_weights = bdt + "/" + dirname + "/dataset/weights/TMVAClassification_" + name + ".weights.xml"
                                bdt_vars = cut_optimisation.getVariablesFromXMLWeightsFile(bdt_weights)
                                bdt_vars_map = cut_optimisation.getVariablesMemMap(bdt_vars)
                                bdt_specs = cut_optimisation.getSpecSpectatorFromXMLWeightsFile(bdt_weights)
                                bdt_specs_map = cut_optimisation.getSpectatorsMemMap(bdt_specs)
                                bdt_reader = cut_optimisation.prepareReader(bdt_weights, bdt_vars, bdt_vars_map, bdt_specs, bdt_specs_map)

                                bdt_vars_maps[prefix + lep + iso + cuts + cat] = bdt_vars_map
                                bdt_specs_maps[prefix + lep + iso + cuts + cat] = bdt_specs_map
                                bdt_readers[prefix + lep + iso + cuts + cat] = bdt_reader

    print 'Analysing', nentries, "entries"
    
    iFile.cd()

    for ientry in range(nentries):
        if ientry % 1000 == 0:
            print "Processing " + str(ientry) + " out of " + str(nentries)
        tree.GetEntry(ientry)
        
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
                    
                        if iso + str(ptRange) + cat == utils.defaultJetIsoSetting:
                            postfixi = [iso + cuts + cat, ""]
                
                        for postfix in postfixi:
                            for prefix in ["reco", "exTrack"]:
                                prefixVars = ""
                            
                                if prefix == "exTrack":
                                    prefixVars = "exTrack_"
                            
                                sameChargeOptions = [False, True] if prefix == "exTrack" else [False]
                            
                                for sameCharge in sameChargeOptions:
                            
                                    sc_prefix = "sc_" if sameCharge else ""
                            
                                    eventPassed = False
                                    leptonFlavour = ""
                                    if prefix == "reco":
                                        #if eval("tree.twoLeptons"  + postfix) == 1 and tree.BTagsDeepMedium == 0 and eval("tree.leptons"  + postfix).size() == 2:
                                        
                                        if getattr(tree, "twoLeptons"  + postfix) == 1 and getattr(tree, "leptons"  + postfix).size() == 2:
                                            eventPassed = True
                                            leptonFlavour = getattr(tree, "leptonFlavour"  + postfix)
                                    # Before
                                    #elif eval("tree." + sc_prefix + "exclusiveTrack"  + postfix) == 1 and tree.BTagsDeepMedium == 0 and eval("tree." + sc_prefix + "trackBDT"  + postfix) >= 0:
                                    # Making new version without trackBDT precut
                                    elif getattr(tree, sc_prefix + "exclusiveTrack"  + postfix) == 1 and tree.BTagsDeepMedium == 0:
                                        eventPassed = True
                                        leptonFlavour = getattr(tree, sc_prefix + "exclusiveTrackLeptonFlavour"  + postfix)
                                    if not jpsi and eventPassed:
                                        leptonFlavour = str(leptonFlavour)
                                        name = prefix + leptonFlavour + postfix
                                        #print bdt_vars_maps[prefix + postfix]
                                        #print name, eval("tree.twoLeptons"  + postfix), eval("tree.exclusiveTrack"  + postfix)
                                        for k, v in bdt_vars_maps[prefix + leptonFlavour + iso + cuts + cat].items():
                                            #print k, v
                                            try:
                                                if k in analysis_observables.dileptonBDTeventObservables:
                                                    if k == "LeadingJet.Eta()":
                                                        v[0] = eval("tree.LeadingJet.Eta()")
                                                    else:
                                                        #print "getattr(tree, k)", k
                                                        v[0] = getattr(tree, k)
                                                else:
                                                    #print k, " not in analysis_observables.dileptonBDTeventObservables"
                                                    #print "eval", "tree." + sc_prefix  + k
                                                    #print "getattr(tree, sc_prefix + k)", sc_prefix + k
                                                    if "[" in k:
                                                        #print "Special stuff"
                                                        (basenameK, postfixK) = k.split("[")
                                                        #print basenameK, postfixK
                                                        branch = getattr(tree, sc_prefix + basenameK)
                                                        #print "branch", branch
                                                        #print "Going to eval", "branch[" + postfixK
                                                        v[0] = eval("branch[" + postfixK)
                                                        #print "After", v[0]
                                                    elif "()" in k:
                                                        #print "Special stuff"
                                                        (basenameK, postfixK) = k.rsplit(".", 1)
                                                        #print basenameK, postfixK
                                                        branch = getattr(tree, sc_prefix + basenameK)
                                                        #print "branch", branch
                                                        #print "Going to eval", "branch." + postfixK
                                                        v[0] = eval("branch." + postfixK)
                                                        #print "After", v[0]
                                                    else:
                                                        v[0] = getattr(tree, sc_prefix + k)
                                                
                                            except Exception as e:
                                                print "exception", e
                                                print ientry, k, name, getattr(tree, "twoLeptons"  + iso + cuts + cat), getattr(tree, "exclusiveTrack"  + iso + cuts + cat)
                                                print "ERROR!!! GIVING UP..."
                                                exit(0)
                                        for k, v in bdt_specs_maps[prefix + leptonFlavour + iso + cuts + cat].items():
                                            if data and k == "Weight":
                                                v[0] = 1
                                            else:
                                                v[0] = getattr(tree, k)
                                     
                                        vars[sc_prefix + prefixVars + "dilepBDT" + postfix][0] = bdt_readers[prefix + leptonFlavour+ iso + cuts + cat].EvaluateMVA("BDT")
                                        #if sc_prefix == "sc_" and postfix == "" and prefixVars == "exTrack_":
                                        #    print "Getting BDT score", sc_prefix + prefixVars + "dilepBDT" + postfix, vars[sc_prefix + prefixVars + "dilepBDT" + postfix][0]
                                            #print bdt_vars_maps
                                    else:
                                        vars[sc_prefix + prefixVars + "dilepBDT" + postfix][0] = -1

                                    if signal and getattr(tree, sc_prefix + "exclusiveTrack"  + postfix) == 1:
                                        gens = [i for i in range(tree.GenParticles.size())]
                                        min, minCan = analysis_ntuples.minDeltaRGenParticles(getattr(tree, sc_prefix + "lepton" + postfix), gens, tree.GenParticles)
                                        #print min, minCan
                                        pdgId = tree.GenParticles_ParentId[minCan]
                                        if minCan is None or min > 0.05:
                                         #   print "BAD GEN LEPTON!!!"
                                            pdgId = 0
                                        #else:
                                        #    print "GOOD LEPTON ", pdgId
                                        vars[sc_prefix + "leptonParentPdgId" + postfix][0] = pdgId
                                        min, minCan = analysis_ntuples.minDeltaRGenParticles(getattr(tree, sc_prefix + "track"+ postfix), gens, tree.GenParticles)
                                        pdgId = tree.GenParticles_ParentId[minCan]
                                        if min > 0.05:
                                            #print "BAD GEN TRACK!!!"
                                            pdgId = 0
                                        #else:
                                        #    print "GOOD TRACK ", pdgId
                                        vars[sc_prefix + "trackParentPdgId" + postfix][0] = pdgId
                                    else:
                                        vars[sc_prefix + "leptonParentPdgId" + postfix][0] = -1
                                        vars[sc_prefix + "trackParentPdgId" + postfix][0] = -1
                            
                            for DTypeObs in analysis_observables.commonPostBdtObservablesDTypesList:
                                for prefix in ["", "exTrack_"]:
                                    sameChargeOptions = [False, True] if prefix == "exTrack_" else [False]
                            
                                    for sameCharge in sameChargeOptions:
                                        sc_prefix = "sc_" if sameCharge else ""
                                        branches[sc_prefix + prefix + DTypeObs + postfix].Fill()
                        
                            for DTypeObs in analysis_observables.exclusiveTrackPostBdtObservablesDTypesList:
                                for sameCharge in [False, True]:
                                    sc_prefix = "sc_" if sameCharge else ""
                                    branches[sc_prefix + DTypeObs + postfix].Fill()
            
    tree.Write("tEvent",TObject.kOverwrite)
        
    print "DONE SKIMMING"
    iFile.Close()

main()