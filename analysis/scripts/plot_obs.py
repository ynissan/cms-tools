#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import os
import re
from datetime import datetime
import math

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes"))
import utils
import analysis_ntuples

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

gSystem.Load('LumiSectMap_C')
from ROOT import LumiSectMap

#lumi = 5746.370
#weight = lumi / utils.LUMINOSITY

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Plot skims for x1x2x1 process with BDTs.')
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
parser.add_argument('-s', '--single', dest='single', help='Single', action='store_true')
parser.add_argument('-c', '--cut', nargs=1, help='Cut', required=False)
parser.add_argument('-obs', '--obs', nargs=1, help='Obs', required=False)
args = parser.parse_args()

output_file = None

#signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/old_leptons_x1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu100_dm7p39Chi20Chipm.root"
# signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/old_leptons_x1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu100_dm3p28Chi20Chipm.root"
# bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/old_leptons_x1x2x1/bg/skim_dilepton_signal_bdt/low/single"
# data_dir = "/afs/desy.de/user/n/nissanuv/nfs/old_leptons_x1x2x1/data/skim_dilepton_signal_bdt/low/single"

signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu115_dm1p13Chi20Chipm.root"
#signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu100_dm2p51Chi20Chipm.root"

#signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu100_dm3p28Chi20Chipm.root"
#signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu100_dm12p84Chi20Chipm.root"
bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1/bg/skim_dilepton_signal_bdt/dm1/single"
data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_dilepton_signal_bdt/dm7/single"

#bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dilepton_signal_bdt/dm0/single"
#signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu100_dm0p86Chi20Chipm.root"

#bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1/bg/skim_dilepton_signal_bdt/dm7/single"
#signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu100_dm7p39Chi20Chipm.root"
#signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu100_dm7p39Chi20Chipm.root"

#Z peak
#bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_z/sum/type_sum"
#data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_z/sum"

#SC
#signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt_sc/single/higgsino_mu100_dm7p39Chi20Chipm.root"
#bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dilepton_signal_bdt_sc/dm7/single"
#data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_dilepton_signal_bdt_sc/dm7/single"


plot_data = False
plot_signal = True
plot_ratio = True
plot_rand = False
plot_fast = True
plot_title = True
plot_overflow = True
plot_significance = False

if not plot_data:
    plot_ratio = False

if args.output_file:
    output_file = args.output_file[0]
else:
    output_file = "obs.pdf"
    
plot_single = args.single

req_cut = None
req_obs = None
if plot_single:
    print "Printing Single Plot"
    if args.cut is None:
        print "Must provide cut with single option."
        exit(0)
    if args.obs is None:
        print "Must provide obs with single option."
        exit(0)
    req_cut = args.cut[0]
    req_obs = args.obs[0]

######## END OF CMDLINE ARGUMENTS ########

def trackBDT(c):
    return c.trackBDT >= 0.2

def univBDT(c):
    return c.univBDT >= 0
    
def dilepBDT(c):
    return c.dilepBDT >= 0.4

def custom_cool(c):
    return c.dilepBDT >= 0.1 and c.univBDT >= 0 and c.tracks_dzVtx[0] <= 0.2 and c.tracks_dxyVtx[0] < 0.2 and c.tracks[0].Pt() < 15 and c.tracks[0].Pt() > 3 and abs(c.tracks[0].Eta()) < 2.4

def dilep_skim(c):
    return c.dilepBDT >= -0.3 and c.univBDT >= -0.4 and c.tracks[0].Pt() >= 3 and c.tracks[0].Pt() < 15 and c.tracks_dzVtx[0] < 0.1 and c.tracks_dxyVtx[0] < 0.1 and abs(c.tracks[0].Eta()) <= 2.4
    
def custom(c):
    return c.Met > 200 and c.dilepBDT >= 0.1 and c.univBDT >= 0 and c.tracks_dzVtx[0] <= 0.03 and c.tracks_dxyVtx[0] <= 0.03 and c.tracks[0].Pt() < 10 and c.tracks[0].Pt() > 3 and abs(c.tracks[0].Eta()) < 2.4 and c.dileptonPt <= 35 and c.pt3 >= 100

def custom_dpg(c):
    return c.Met > 200 and c.trackBDT >= 0.1 and c.dilepBDT >= 0.1 and c.univBDT >= 0 and c.tracks_dzVtx[0] <= 0.03 and c.tracks_dxyVtx[0] <= 0.03 and c.tracks[0].Pt() < 10 and c.tracks[0].Pt() > 5 and abs(c.tracks[0].Eta()) < 2.4 and c.dileptonPt <= 35  and c.pt3 >= 100

def step2(c):
    return c.Met > 200 and c.tracks[0].Pt() < 10 and c.tracks_dzVtx[0] <= 0.01 and c.tracks_dxyVtx[0] <= 0.01 and c.univBDT >= 0.1 and c.pt3 >= 225 and c.dilepBDT >= 0.15 and c.trackBDT >= 0.1 and abs(c.tracks[0].Eta()) < 1.8 and c.tracks[0].Pt() > 5

def step(c):
    return c.Met > 200 and c.trackBDT >= 0.1 and c.dilepBDT >= 0.15 and c.univBDT >= 0.1 and c.tracks_dzVtx[0] <= 0.03 and c.tracks_dxyVtx[0] <= 0.03 and c.tracks[0].Pt() < 10 and c.tracks[0].Pt() > 5 and abs(c.tracks[0].Eta()) < 2.4 and c.dileptonPt <= 35 and c.pt3 >= 100

def step3(c):
    return c.Met > 200 and c.tracks[0].Pt() < 10 and c.tracks_dzVtx[0] <= 0.01 and c.tracks_dxyVtx[0] <= 0.01 and c.univBDT >= 0.1 and c.pt3 >= 225 and c.dilepBDT >= 0.15 and c.trackBDT >= 0.1 and abs(c.tracks[0].Eta()) < 1.8 and c.tracks[0].Pt() > 5 and c.deltaR <= 1

def step2_200_250(c):
    return step2(c) and c.Met < 250

def step2_250(c):
    return step2(c) and c.Met > 250

def invMass(c):
    return c.invMass < 30

def metMht(c):
    return c.Met > 200 and c.Mht > 100

def mw(c):
    if abs(c.leptonParentPdgId) == 15:
        gens = [i for i in range(c.GenParticles.size())]
        min, minCan = analysis_ntuples.minDeltaRGenParticles(c.lepton, gens, c)
        tauIdx = c.GenParticles_ParentIdx[minCan]
        wIdx = c.GenParticles_ParentIdx[tauIdx]
        if abs(c.GenParticles_PdgId[wIdx]) != 24:
            #print "Weird!"
            return 0
        else:
            #print "***Found W!"
            wChildrenPdgId = []
            wChildrenPdgIdx = []
            tauChildren = []
            #print "---"
            for i in range(c.GenParticles.size()):
                if c.GenParticles_ParentIdx[i] == wIdx:
                    #print c.GenParticles_Status[i]
                    wChildrenPdgId.append(c.GenParticles_PdgId[i])
                    wChildrenPdgIdx.append(i)
                if c.GenParticles_ParentIdx[i] == tauIdx:
                    tauChildren.append(c.GenParticles_PdgId[i])
            #print "wChildrenPdgId=", wChildrenPdgId
            #print "tauChildren=", tauChildren
            if len(wChildrenPdgIdx) == 2:
                return (c.GenParticles[wChildrenPdgIdx[0]] + c.GenParticles[wChildrenPdgIdx[1]]).M()
            return 0
    else:
        return 0

def mw2(c):
    return mw(c) < 60

#and c.dilepHt >= 250 and c.NJets <= 3 and c.mt1 <= 50

histograms_defs = [
    #Z PEAK
#     { "obs" : "invMass", "minX" : 91.19 - 10.0, "maxX" : 91.19 + 10.0, "bins" : 30 },
#     { "obs" : "Met", "minX" : 0, "maxX" : 200, "bins" : 200 },
#     { "obs" : "Mht", "minX" : 0, "maxX" : 200, "bins" : 200 },
#     { "obs" : "Ht", "minX" : 0, "maxX" : 200, "bins" : 200 },    
#     { "obs" : "Mt2", "minX" : 0, "maxX" : 100, "bins" : 200 },
#     { "obs" : "Muons[0].Pt()", "minX" : 0, "maxX" : 300, "bins" : 300 },
#     { "obs" : "NJets", "minX" : 0, "maxX" : 7, "bins" : 7 },
    
    
    #NORMAL
    { "obs" : "invMass", "minX" : 0, "maxX" : 15, "bins" : 90, "units" : "GeV" },
    { "obs" : "dilepBDT", "minX" : -0.6, "maxX" : 0.6, "bins" : 30 },
    
    
    # { "obs" : "dileptonPt", "minX" : 0, "maxX" : 100, "bins" : 30 },
#     { "obs" : "deltaPhi", "minX" : 0, "maxX" : 3.2, "bins" : 30 },
#     { "obs" : "deltaEta", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "deltaR", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "pt3", "minX" : 230, "maxX" : 1000, "bins" : 30 },
#     { "obs" : "mtautau", "minX" : 0, "maxX" : 1000, "bins" : 30 },
#     { "obs" : "mtl", "minX" : 0, "maxX" : 200, "bins" : 30 },
#     { "obs" : "mtt", "minX" : 0, "maxX" : 200, "bins" : 30 },
#     { "obs" : "mt1", "minX" : 0, "maxX" : 200, "bins" : 30 },
#     { "obs" : "mt2", "minX" : 0, "maxX" : 200, "bins" : 30 },
#     { "obs" : "DeltaEtaLeadingJetDilepton", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "DeltaPhiLeadingJetDilepton", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "dilepHt", "minX" : 0, "maxX" : 400, "bins" : 30 },
#     { "obs" : "NJets", "minX" : 0, "maxX" : 7, "bins" : 7 },
#     { "obs" : "NTracks", "minX" : 0, "maxX" : 7, "bins" : 7 },
#     { "obs" : "Met", "minX" : 140, "maxX" : 700, "bins" : 30 },
#     { "obs" : "Mht", "minX" : 0, "maxX" : 700, "bins" : 30 },
#     { "obs" : "Ht", "minX" : 0, "maxX" : 700, "bins" : 30 },
#     { "obs" : "LeadingJetQgLikelihood", "minX" : 0, "maxX" : 1, "bins" : 30 },
#     { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "MinDeltaPhiMetJets", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "Mt2", "minX" : 0, "maxX" : 100, "bins" : 30 },
#     { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 800, "bins" : 30 },
#     { "obs" : "abs(LeadingJet.Eta())", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "MinCsv30", "minX" : 0, "maxX" : 1, "bins" : 30 },
#     { "obs" : "MinCsv25", "minX" : 0, "maxX" : 1, "bins" : 30 },
#     { "obs" : "MaxCsv30", "minX" : 0, "maxX" : 1, "bins" : 30 },
#     { "obs" : "MaxCsv25", "minX" : 0, "maxX" : 1, "bins" : 30 },
#     
#     #TRACK ONLY
#     { "obs" : "trackBDT", "minX" : 0, "maxX" : 0.7, "bins" : 30 },
#     { "obs" : "secondTrackBDT", "minX" : -1, "maxX" : 1, "bins" : 30 },
#     { "obs" : "abs(track.Eta())", "minX" : 0, "maxX" : 3, "bins" : 60 },
#     { "obs" : "abs(lepton.Eta())", "minX" : 0, "maxX" : 3, "bins" : 60 },
#     { "obs" : "track.Pt()", "minX" : 0, "maxX" : 30, "bins" : 60 },
#     { "obs" : "lepton.Pt()", "minX" : 2, "maxX" : 25, "bins" : 60 },
#     { "obs" : "secondTrack.Pt()", "minX" : 0, "maxX" : 30, "bins" : 60 },
#     { "obs" : "abs(secondTrack.Eta())", "minX" : 0, "maxX" : 3, "bins" : 60 },

     #{ "obs" : "abs(leptonParentPdgId)", "minX" : 0, "maxX" : 30, "bins" : 30 },
     #{ "obs" : "abs(trackParentPdgId)", "minX" : 0, "maxX" : 30, "bins" : 30 },
#     
    
    #DILEPTON
    
    #{ "obs" : "mw", "minX" : 0, "maxX" : 150, "bins" : 50, "func" : mw },
    #{ "obs" : "invMass2", "minX" : 0, "maxX" : 15, "bins" : 90, "func" : mw2 },
    
    
    
   #  { "obs" : "invMass", "minX" : 0, "maxX" : 2, "bins" : 90, "units" : "GeV" },
#     { "obs" : "dilepBDT", "minX" : -0.6, "maxX" : 0.6, "bins" : 30 },
#     { "obs" : "abs(leptons[0].Eta())", "minX" : 0, "maxX" : 3, "bins" : 60 },
#     { "obs" : "abs(leptons[1].Eta())", "minX" : 0, "maxX" : 3, "bins" : 60 },
#     { "obs" : "leptons[0].Pt()", "minX" : 0, "maxX" : 30, "bins" : 60 },
#     { "obs" : "leptons[1].Pt()", "minX" : 0, "maxX" : 30, "bins" : 60 },
#     { "obs" : "dileptonPt", "minX" : 0, "maxX" : 100, "bins" : 30 },
#     { "obs" : "deltaPhi", "minX" : 0, "maxX" : 3.2, "bins" : 30 },
#     { "obs" : "deltaEta", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "deltaR", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "pt3", "minX" : 230, "maxX" : 1000, "bins" : 30 },
#     { "obs" : "mtautau", "minX" : 0, "maxX" : 1000, "bins" : 30 },
#     { "obs" : "mt1", "minX" : 0, "maxX" : 200, "bins" : 30 },
#     { "obs" : "mt2", "minX" : 0, "maxX" : 200, "bins" : 30 },
#     { "obs" : "DeltaEtaLeadingJetDilepton", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "DeltaPhiLeadingJetDilepton", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "dilepHt", "minX" : 0, "maxX" : 400, "bins" : 30 },
#     { "obs" : "NJets", "minX" : 0, "maxX" : 7, "bins" : 7 },
#     { "obs" : "Met", "minX" : 140, "maxX" : 700, "bins" : 30 },
#     { "obs" : "Mht", "minX" : 100, "maxX" : 700, "bins" : 30 },
#     { "obs" : "Ht", "minX" : 0, "maxX" : 700, "bins" : 30 },
#     { "obs" : "LeadingJetQgLikelihood", "minX" : 0, "maxX" : 1, "bins" : 30 },
#     { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "MinDeltaPhiMetJets", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "Mt2", "minX" : 0, "maxX" : 100, "bins" : 30 },
#     { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 800, "bins" : 30 },
#     { "obs" : "abs(LeadingJet.Eta())", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "MinCsv30", "minX" : 0, "maxX" : 1, "bins" : 30 },
#     { "obs" : "MinCsv25", "minX" : 0, "maxX" : 1, "bins" : 30 },
#     { "obs" : "MaxCsv30", "minX" : 0, "maxX" : 1, "bins" : 30 },
#     { "obs" : "MaxCsv25", "minX" : 0, "maxX" : 1, "bins" : 30 },
#     { "obs" : "deltaPhiMetLepton1", "minX" : 0, "maxX" : 3.5, "bins" : 30 },
#     { "obs" : "deltaPhiMetLepton2", "minX" : 0, "maxX" : 3.5, "bins" : 30 },
    
    
    
]

cuts = [#{"name":"none", "title": "No Cuts", "condition" : "1"},
#Z PEAK
#        {"name":"metb", "title": "Met<20", "condition" : "Met < 20"},
#        {"name":"mets", "title": "Met>20", "condition" : "Met > 20"},

#NORMAL 
          {"name":"MET", "title": "MET", "condition" : "Met >= 250 && invMass < 30"},
          {"name":"dilepBDT", "title": "dilepBDT", "condition" : "Met >= 200 && dilepBDT > 0.4 && invMass < 30"}
#          {"name":"deltaR", "title": "deltaR", "condition" : "Met >= 250 && deltaR < 0.9"},
#          {"name":"dm7", "title": "dm7", "condition" : "Met >= 250 && invMass < 30 && dilepBDT > -0.2 && abs(track.Eta()) < 1.5 && abs(lepton.Eta()) < 2 && track.Pt() < 10 && dilepBDT > 0 && univBDT > 0 && univBDT < 0.5 && secondTrack.Pt() < 5 && lepton.Pt() > 4 && lepton.Pt() < 20 && trackBDT > -0.2 && trackBDT < 0.3 && LeadingJetPt > 200 && tracks_dxyVtx[0] < 0.01 && tracks_dzVtx[0] < 0.015 && secondTrackBDT == -1 && deltaEta < 1.5 && mtl < 60"},
#          {"name":"leptons", "title": "leptons", "condition" : "lepton.Pt() > 4 && trackBDT > -0.3 && trackBDT < 0.4 && dilepBDT > -0.1 && lepton.Pt() < 20 && mtl < 60"},
#         {"name":"step", "title": "step", "condition" : "tracks_trackQualityHighPurity[0] && invMass < 30 && dilepBDT >= -0.3 && univBDT >= -0.4 && tracks[0].Pt() >= 3 && tracks[0].Pt() < 15 && tracks_dzVtx[0] < 0.1 && tracks_dxyVtx[0] < 0.1 && abs(tracks[0].Eta()) <= 2.4 && trackBDT > 0.1 && @tracks.size() == 1"},
#          {"name":"step2", "title": "step2", "condition" : "Met > 250 && tracks[0].Pt() < 10 && tracks_dzVtx[0] <= 0.01 && tracks_dxyVtx[0] <= 0.01 && univBDT >= 0.1 && pt3 >= 225 && dilepBDT >= 0.15 && trackBDT >= 0.1 && abs(tracks[0].Eta()) < 1.8 && tracks[0].Pt() > 5"},
#          {"name":"step3", "title": "step3", "condition" : "Met > 200 && tracks[0].Pt() < 10 && tracks_dzVtx[0] <= 0.01 && tracks_dxyVtx[0] <= 0.01 && univBDT >= 0.1 && pt3 >= 225 && dilepBDT >= 0.4 && trackBDT >= 0.1 && abs(tracks[0].Eta()) < 1.8 && tracks[0].Pt() > 5"},
#          {"name":"custom", "title": "custom", "condition" : "Met > 200 && dilepBDT >= 0.1 && univBDT >= 0 && tracks_dzVtx[0] <= 0.03 && tracks_dxyVtx[0] <= 0.03 && tracks[0].Pt() < 10 && tracks[0].Pt() > 3 && abs(tracks[0].Eta()) < 2.4 && dileptonPt <= 35 && pt3 >= 100"},
#          {"name":"custom_dpg", "title": "custom_dpg", "condition" : "Met > 200 && trackBDT >= 0.1 && dilepBDT >= 0.1 && univBDT >= 0 && tracks_dzVtx[0] <= 0.03 && tracks_dxyVtx[0] <= 0.03 && tracks[0].Pt() < 10 && tracks[0].Pt() > 5 && abs(tracks[0].Eta()) < 2.4 && dileptonPt <= 35  && pt3 >= 100"}


# STUDY PRESELECTION
         # {"name":"none", "title": "No Cuts", "condition" : "invMass < 30"},
#          {"name":"dilepBDT", "title": "dilepBDT", "condition" : "dilepBDT > 0 && invMass < 30"},
#          {"name":"dilepBDT2", "title": "dilepBDT2", "condition" : "dilepBDT > 0.2 && invMass < 30 && trackBDT > 0.2"},
#          {"name":"dm2", "title": "dm2", "condition" : "dilepBDT > 0.176 && invMass < 30"},
#          {"name":"dm3", "title": "dm3", "condition" : "dilepBDT > 0.31 && invMass < 30 && trackBDT > 0.22 && track.Pt() < 9 && abs(track.Eta()) < 1.4"},
         #secondTrackBDT == -1 &&
         #{"name":"trackBDT", "title": "trackBDT", "condition" : "trackBDT >= 0 && MaxCsv25 < 0.7"},

#DILEPTON
        #{"name":"none", "title": "No Cuts", "condition" : "invMass < 30"},
        #{"name":"dilepBDT", "title": "dilepBDT", "condition" : "dilepBDT > 0 && invMass < 30", "funcs" : [dilepBDT, invMass, mw2]},
        #{"name":"dilepBDT2", "title": "dilepBDT2", "condition" : "dilepBDT > 0.2 && invMass < 30"},
        #{"name":"dilepBDT3", "title": "dilepBDT3", "condition" : "dilepBDT > 0.3 && invMass < 30"},
        #{"name":"dilepBDT4", "title": "dilepBDT4", "condition" : "dilepBDT > 0.4 && invMass < 30"},

#         {"name":"dilepBdt2", "title": "dilepBdt2", "condition" : "dilepBDT >= 0"},
#         {"name":"dilepBdt3", "title": "dilepBdt3", "condition" : "dilepBDT >= 0.2"},
#         {"name":"dilepBdt3", "title": "dilepBdt4", "condition" : "dilepBDT >= 0.3"},
#         
#         
#         {"name":"univBDT", "title": "univBDT", "condition" : "univBDT >= -0.2"},
#         {"name":"univBDT2", "title": "univBDT2", "condition" : "univBDT >= 0"},
#         {"name":"univBDT3", "title": "univBDT3", "condition" : "univBDT >= 0.2"},
#         {"name":"univBDT4", "title": "univBDT4", "condition" : "univBDT >= 0.3"},
#         {"name":"univBDT5", "title": "univBDT5", "condition" : "univBDT >= 0.5 && univBDT <= 0.6"},
#         
#         
#         {"name":"trackBDT", "title": "trackBDT", "condition" : "trackBDT >= -0.2"},
#         {"name":"trackBDT2", "title": "trackBDT2", "condition" : "trackBDT >= 0"},
#         {"name":"trackBDT3", "title": "trackBDT3", "condition" : "trackBDT >= 0.1"},
#         {"name":"trackBDT4", "title": "trackBDT4", "condition" : "trackBDT >= 0.1 && trackBDT < 0.3"},
        
        #{"name":"dilep_skim_no_pt", "title": "dilep_skim_no_pt", "condition" : "invMass < 30 && dilepBDT >= -0.3 && univBDT >= -0.4 && tracks_dzVtx[0] < 0.1 && tracks_dxyVtx[0] < 0.1 && abs(tracks[0].Eta()) <= 2.4"},     
        # {"name":"dilep_skim", "title": "dilep_skim", "condition" : "tracks_trackQualityHighPurity[0] && invMass < 30 && dilepBDT >= -0.3 && univBDT >= -0.4 && tracks[0].Pt() >= 3 && tracks[0].Pt() < 15 && tracks_dzVtx[0] < 0.1 && tracks_dxyVtx[0] < 0.1 && abs(tracks[0].Eta()) <= 2.4"},
#         {"name":"dilep_skim_track_bdt", "title": "dilep_skim_track_bdt", "condition" : "tracks_trackQualityHighPurity[0] && invMass < 30 && dilepBDT >= -0.3 && univBDT >= -0.4 && tracks[0].Pt() >= 3 && tracks[0].Pt() < 15 && tracks_dzVtx[0] < 0.1 && tracks_dxyVtx[0] < 0.1 && abs(tracks[0].Eta()) <= 2.4 && trackBDT > 0.1 && @tracks.size() == 1"},

#        {"name":"metMht", "title": "MET > 200, Mht > 100", "funcs" : [metMht]},
#         {"name":"trackBDT", "title": "trackBDT >= 0.2", "funcs":[trackBDT]},
#         {"name":"univBDT", "title": "univBDT >= 0", "funcs":[univBDT]},
#         {"name":"dilepBDT", "title": "dilepBDT >= 0.1", "funcs":[dilepBDT]}
#        {"name":"custom", "title": "No Cuts", "funcs" : [custom, dilep_skim]},
#         {"name":"custom_dpg", "title": "No Cuts", "funcs" : [custom_dpg, dilep_skim]},
#         {"name":"step", "title": "No Cuts", "funcs" : [step]},
#         {"name":"step2", "title": "No Cuts", "funcs" : [step2]},
#         {"name":"step2_200_250", "title": "No Cuts", "funcs" : [step2_200_250]},
#         {"name":"step2_250", "title": "No Cuts", "funcs" : [step2_250]},
#         {"name":"step3", "title": "No Cuts", "funcs" : [step3]},
        ]

integralRange = {
    'dm2p51' : [0,3],
    'dm7p39' : [0,8],
    'dm1p13' : [0,1.8]
}

calculatedLumi = {
    'MET' : 31.118664841
}



def styleHist(hist):
    hist.GetYaxis().SetTitleSize(10);
    hist.GetYaxis().SetTitleFont(43);
    hist.GetYaxis().SetTitleOffset(2.5);
    hist.GetYaxis().SetLabelFont(43); 
    hist.GetYaxis().SetLabelSize(10);

    hist.GetXaxis().SetTitleSize(10);
    hist.GetXaxis().SetTitleFont(43);
    hist.GetXaxis().SetTitleOffset(7.5);
    hist.GetXaxis().SetLabelFont(43); 
    hist.GetXaxis().SetLabelSize(10);

def createPlots(rootfiles, type, histograms, weight=1):
    print "Processing "
    print rootfiles
    lumiSecs = LumiSectMap()
    
    for f in rootfiles:
        print f
        rootFile = TFile(f)
        c = rootFile.Get('tEvent')
        if type == "data":
            lumis = rootFile.Get('lumiSecs')
            col = TList()
            col.Add(lumis)
            lumiSecs.Merge(col)
        nentries = c.GetEntries()
        print 'Analysing', nentries, "entries"
        for ientry in range(nentries):
            if ientry % 10000 == 0:
                print "Processing " + str(ientry)
            c.GetEntry(ientry)
            
            for cut in cuts:
                passed = True
                if cut.get("funcs") is not None:
                    for func in cut["funcs"]:
                        passed = func(c)
                        if not passed:
                            break
                if not passed:
                    continue
                
                for hist_def in histograms_defs:
                    histName =  cut["name"] + "_" + hist_def["obs"] + "_" + type
                    hist = histograms[histName]
                    if type != "data":
                        #print "Weight=", c.Weight
                        #print "weight=", weight
                        if hist_def.get("func") is not None:
                            hist.Fill(hist_def["func"](c), c.Weight * weight)
                        else:
                            hist.Fill(eval('c.' + hist_def["obs"]), c.Weight * weight)
                    else:
                        hist.Fill(eval('c.' + hist_def["obs"]), 1)
        rootFile.Close()
    
    if type == "data":
        if calculatedLumi.get('MET') is not None:
            print "Found lumi=" + str(calculatedLumi['MET'])
            return calculatedLumi['MET']
        else:
            return utils.calculateLumiFromLumiSecs(lumiSecs)
        #return 3.939170474
        #return 35.574589421
        #return 35.493718415
        #return 27.360953311
        return 27.677964176


def createPlotsFast(rootfiles, type, histograms, weight=1):
    print "Processing "
    print rootfiles
    lumiSecs = LumiSectMap()
    
    for f in rootfiles:
        print f
        rootFile = TFile(f)
        c = rootFile.Get('tEvent')
        if type == "data":
            lumis = rootFile.Get('lumiSecs')
            col = TList()
            col.Add(lumis)
            lumiSecs.Merge(col)
        
        for cut in cuts:
            for hist_def in histograms_defs:
                histName =  cut["name"] + "_" + hist_def["obs"] + "_" + type
                #if type != "data" and type != "signal":
                #    hist = utils.getHistogramFromTree(histName, c, hist_def["obs"], hist_def["bins"], hist_def["minX"], hist_def["maxX"], "puWeight * (" + cut["condition"] + ")")
                #else:
                hist = utils.getHistogramFromTree(histName, c, hist_def["obs"], hist_def["bins"], hist_def["minX"], hist_def["maxX"], cut["condition"], plot_overflow)
                if hist is None:
                    continue
                hist.GetXaxis().SetTitle("")
                hist.SetTitle("")
                #hist.Sumw2()
                if type != "data":
                    c.GetEntry(0)
                    hist.Scale(c.Weight * weight)
                if histograms.get(histName) is None:
                    histograms[histName] = hist
                else:
                    histograms[histName].Add(hist)
        
        rootFile.Close()
    
    if type == "data":
        if calculatedLumi.get('MET') is not None:
            print "Found lumi=" + str(calculatedLumi['MET'])
            return calculatedLumi['MET']
        else:
            return utils.calculateLumiFromLumiSecs(lumiSecs)
        #Z PEAK
        #return 27.677786572
        #Norman
        return 35.579533154
        #return utils.calculateLumiFromLumiSecs(lumiSecs)

def createRandomHist(name):
    h = utils.UOFlowTH1F(name, "", 100, -5, 5)
    h.Sumw2()
    h.FillRandom("gaus")
    styleHist(h)
    return h
    
def createCRPads(pId, ratioPads):
    histCPad = TPad("pad" + str(pId),"pad" + str(pId),0,0.21,1,1)
    histRPad = TPad("rpad" + str(pId),"rpad" + str(pId),0,0,1,0.2);
    ratioPads[pId] = []
    ratioPads[pId].append(histCPad)
    ratioPads[pId].append(histRPad)
    histCPad.SetBottomMargin(0)
    histRPad.SetTopMargin(0.05)
    histRPad.SetBottomMargin(0.25)
    histRPad.Draw()
    histCPad.Draw()
    return histCPad, histRPad

def plotRatio(c1, pad, memory, dataHist, newBgHist, hist_def):
    pad.cd()
    pad.SetGridx()
    pad.SetGridy()
    rdataHist = dataHist.Clone()
    memory.append(rdataHist)
    rdataHist.Divide(utils.getStackSum(newBgHist))
    rdataHist.SetMinimum(0)
    rdataHist.SetMaximum(2)
    rdataHist.GetXaxis().SetTitle(hist_def["obs"])
    rdataHist.GetYaxis().SetTitle("Data / BG")
    styleHist(rdataHist)
    rdataHist.GetYaxis().SetNdivisions(505)
    rdataHist.Draw("p")
    line = TLine(rdataHist.GetXaxis().GetXmin(),1,rdataHist.GetXaxis().GetXmax(),1);
    line.SetLineColor(kRed);
    line.Draw("SAME");
    memory.append(line)
    c1.Modified()

def createAllHistograms(histograms, sumTypes):
    foundReqObs = False
    foundReqCut = False
    
    global cuts
    global histograms_defs
    global plot_title
    
    if plot_single:
        plot_title = False
        for obs in histograms_defs:
            if obs["obs"] == req_obs:
                foundReqObs = True
                histograms_defs = [obs]
                break
        if not foundReqObs:
            print "Could not find obs " + req_obs
            exit(0)
        for cut in cuts:
            if cut["name"] == req_cut:
                foundReqCut = True
                cuts = [cut]
                break
        if not foundReqCut:
            print "Could not find cut " + req_cut
            exit(0)
            
    if not plot_rand:
        c2 = TCanvas("c2")
        c2.cd()
    
        bg_files = glob(bg_dir + "/*")

        for f in bg_files: 
            filename = os.path.basename(f).split(".")[0]
            types = filename.split("_")
            type = None
            
            #if types[0] == "WJetsToLNu" or types[0] == "ZJetsToNuNu":
            #    continue
            
            if types[0] == "TTJets":
                type = "_".join(types[0:2])
            elif types[0] == "ST":
                type = "_".join(types[0:3])
            else:
                type = types[0]
            if type not in sumTypes:
                sumTypes[type] = {}
            #sumTypes[types[0]][types[1]] = True

        print sumTypes
        if not plot_fast:
            print "NOT PLOTTING FAST"
            for cut in cuts:
                    for hist_def in histograms_defs:
                        baseName = cut["name"] + "_" + hist_def["obs"]
                        sigName = baseName + "_signal"
                        dataName = baseName + "_data"
                        histograms[sigName] = utils.UOFlowTH1F(sigName, "", hist_def["bins"], hist_def["minX"], hist_def["maxX"])
                        histograms[dataName] = utils.UOFlowTH1F(dataName, "", hist_def["bins"], hist_def["minX"], hist_def["maxX"])
                        utils.formatHist(histograms[sigName], utils.signalCp[0], 0.8)
                        for type in sumTypes:
                            if utils.existsInCoumpoundType(type):
                                continue
                            bgName = baseName + "_" + type
                            histograms[bgName] = utils.UOFlowTH1F(bgName, "", hist_def["bins"], hist_def["minX"], hist_def["maxX"])
                        for type in utils.compoundTypes:
                            bgName = baseName + "_" + type
                            histograms[bgName] = utils.UOFlowTH1F(bgName, "", hist_def["bins"], hist_def["minX"], hist_def["maxX"])
    
        calculated_lumi = None
        weight=0
        if plot_data:
            dataFiles = glob(data_dir + "/*")
            if plot_fast:
                calculated_lumi = createPlotsFast(dataFiles, "data", histograms)
            else:
                calculated_lumi = createPlots(dataFiles, "data", histograms)
            print "Calculated Luminosity: ", calculated_lumi
            weight = calculated_lumi * 1000
        else:
            print "HERE"
            weight = utils.LUMINOSITY
    
        if plot_signal:
            if plot_fast:
                print "Plotting Signal Fast"
                createPlotsFast([signal_dir], "signal", histograms, weight)
            else:
                createPlots([signal_dir], "signal", histograms, weight)
        for type in sumTypes:
            if utils.existsInCoumpoundType(type):
                continue
            #if type == "ZJetsToNuNu" or type == "WJetsToLNu":
            #    continue
            print "Summing type", type
            rootfiles = glob(bg_dir + "/*" + type + "*.root")
            if plot_fast:
                createPlotsFast(rootfiles, type, histograms, weight)
            else:
                createPlots(rootfiles, type, histograms, weight)
    
        for cType in utils.compoundTypes:
            print "Creating compound type", cType
            rootFiles = []
            for type in utils.compoundTypes[cType]:
                print "Searching " + type
                if type not in sumTypes:
                    continue
                if "ST_" in type:
                    print "In ST***"
                    print "Globing " + bg_dir + "/" + type + ".root"
                    rootFiles.extend(glob(bg_dir + "/" + type + ".root"))
                else:
                    print "Globing " + bg_dir + "/" + type + "_*.root"
                    rootFiles.extend(glob(bg_dir + "/" + type + "_*.root"))
            if len(rootFiles):
                if plot_fast:
                    createPlotsFast(rootFiles, cType, histograms, weight)
                else:
                    createPlots(rootFiles, cType, histograms, weight)
            else:
                print "**Couldn't find file for " + cType

def main():
    print "Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    deltaM = utils.getDmFromFileName(signal_dir)
    print "deltaM=" + deltaM

    histograms = {}
    sumTypes = {}
    
    createAllHistograms(histograms, sumTypes)

    print "Plotting observable"

    c1 = TCanvas("c1", "c1", 800, 800)
    
    if plot_single:
        c1.SetBottomMargin(0.16)
        c1.SetLeftMargin(0.18)
    
    c1.cd()
    
    titlePad = None
    histPad = None
    t = None
    if plot_title:
        titlePad = TPad("titlePad", "",0.0,0.93,1.0,1.0)
        histPad = TPad("histPad", "",0.0,0.0,1.0,0.93)
        titlePad.Draw()
        t = TPaveText(0.0,0.93,1.0,1.0,"NB")
        t.SetFillStyle(0)
        t.SetLineColor(0)
        t.SetTextFont(40);
        t.AddText("No Cuts")
        t.Draw()
    else:
        histPad = c1
    
    histPad.Draw()
    if not plot_single:
        histPad.Divide(2,2)

    c1.Print(output_file+"[");

    plot_num = 0

    pId = 1
    needToDraw = False

    memory = []
    
    ratioPads = {}
    
    for cut in cuts:
        
        sigNum = 0
        bgNum = 0
        
        cutName = cut["name"]
        print "Cut " + cutName
        if plot_title:
            t.Clear()
            t.AddText(cut["title"])
            t.Draw()
            titlePad.Update()
        pId = 1
        for hist_def in histograms_defs:
            
            needToDraw = True
            pad = None
            if plot_single:
                pad = histPad.cd()
            else:
                pad = histPad.cd(pId)
            histCPad = None
            histRPad = None
            if plot_ratio:
                if ratioPads.get(pId) is None:
                    histCPad, histRPad = createCRPads(pId, ratioPads)
                else:
                    histCPad = ratioPads[pId][0]
                    histRPad = ratioPads[pId][1]
                pad = histCPad
                pad.cd()
            
            hs = THStack(str(plot_num),"")
            plot_num += 1
            memory.append(hs)
            types = [k for k in utils.bgOrder]
            types = sorted(types, key=lambda a: utils.bgOrder[a])
            typesInx = []
            i = 0
            foundBg = False
            for type in types:
                hname = cut["name"] + "_" + hist_def["obs"] + "_" + type
                if plot_rand:
                    histograms[hname] = createRandomHist(hname)
                if histograms.get(hname) is not None:
                    hs.Add(histograms[hname])
                    typesInx.append(i)
                    foundBg = True
                i += 1
            sigHistName = cut["name"] + "_" + hist_def["obs"] + "_signal"
            dataHistName = cut["name"] + "_" + hist_def["obs"] + "_data"
            if plot_rand:
                histograms[dataHistName] = createRandomHist(dataHistName)
            dataHist = None
            sigHist = None
            sigMax = 0
            if plot_signal: 
                sigHist = histograms[sigHistName]
                utils.formatHist(sigHist, utils.signalCp[0], 0.8)
                sigMax = sigHist.GetMaximum()
            maximum = sigMax
            if foundBg:
                bgMax = hs.GetMaximum()
                maximum = max(bgMax, sigMax)
            if plot_data:
                dataHist = histograms[dataHistName]
                dataHist.SetMinimum(0.01)
                dataHist.SetMarkerStyle(kFullCircle)
                dataHist.SetMarkerSize(0.5)
                dataMax = dataHist.GetMaximum()
                maximum = max(dataMax, maximum)
            
            if maximum == 0:
                maximum == 10
            
            legend = TLegend(.20,.60,.89,.89)
            legend.SetNColumns(2)
            legend.SetBorderSize(0)
            legend.SetFillStyle(0)
            newBgHist = None
            memory.append(legend)
            
            if foundBg:
                newBgHist = utils.styledStackFromStack(hs, memory, legend, "", typesInx, True)
                #newBgHist.SetFillColorAlpha(fillC, 0.35)
                newBgHist.SetMaximum(maximum*1000)
                newBgHist.SetMinimum(0.01)
                newBgHist.Draw("hist")
                
                if plot_single:
                    utils.histoStyler(newBgHist)
                if not plot_ratio:
                    if plot_single:
                        newBgHist.GetXaxis().SetTitle(hist_def["units"] if hist_def.get("unit") is not None else "#DeltaR(ll)")#hist_def["obs"])
                    else:
                        newBgHist.GetXaxis().SetTitle(hist_def["obs"])
                newBgHist.GetYaxis().SetTitle("Number of events")
                if plot_single:
                    newBgHist.GetYaxis().SetTitleOffset(1.15)

                #newBgHist.GetXaxis().SetLabelSize(0.055)
                c1.Modified()
            
            if plot_signal: 
                legend.AddEntry(sigHist, "signal", 'l')
            if foundBg and plot_signal:
                sigHist.SetMaximum(maximum)
            if plot_signal:
                sigHist.SetMinimum(0.01)
                sigHist.SetLineWidth(2)
            if foundBg and plot_signal:
                sigHist.Draw("HIST SAME")
            elif plot_signal:
                sigHist.Draw("HIST")
            
            if hist_def["obs"] == "invMass":
                binMin = sigHist.GetXaxis().FindBin(integralRange[deltaM][0])
                binMax = sigHist.GetXaxis().FindBin(integralRange[deltaM][1])
                sigNum = sigHist.Integral(binMin,binMax)
                bgNum = 0
                for h in newBgHist.GetHists():
                    bgNum += h.Integral(binMin,binMax)
                significance = sigNum / math.sqrt(bgNum)
                print "cutName ", cutName, " sigNum", sigNum, " bgNum", bgNum, " sig", significance
                if not plot_single and plot_significance:
                    pt = TPaveText(.60,.1,.95,.2, "NDC")
                    pt.SetFillColor(0)
                    pt.SetTextAlign(11)
                    pt.SetBorderSize(0)
                    memory.append(pt)
                    pt.AddText("sigNum=" + str(sigNum))
                    pt.AddText("bgNum=" + str(bgNum))
                    pt.AddText("sig=" + str(significance))
                    pt.Draw()
                
            
            if plot_data:
                dataHist.Draw("P SAME")
                legend.AddEntry(dataHist, "data", 'p')
            
            legend.Draw("SAME")
            pad.SetLogy()
            c1.Update()
            
            if plot_ratio:
                plotRatio(c1, histRPad, memory, dataHist, newBgHist, hist_def)
            
            if plot_single:
                utils.stamp_plot()
                break
            
            pId += 1

            if pId > 4:
                pId = 1
                c1.Print(output_file);
                needToDraw = False;
            
            linBgHist = newBgHist.Clone()
            memory.append(linBgHist)
            linBgHist.SetMaximum(maximum*1.1)
            linBgHist.SetMinimum(0)
            
            if plot_ratio:
                if ratioPads.get(pId) is None:
                    pad = histPad.cd(pId)
                    histCPad, histRPad = createCRPads(pId, ratioPads)
                else:
                    histCPad = ratioPads[pId][0]
                    histRPad = ratioPads[pId][1]
                pad = histCPad
                pad.cd()
            else:
                pad = histPad.cd(pId)
            
            pad.SetLogy(0)
            linBgHist.Draw("hist")
            if plot_signal:
                sigHist.Draw("HIST SAME")
            if plot_data:
                dataHist.Draw("P e SAME")
            legend.Draw("SAME")
            
            if plot_ratio:
                plotRatio(c1, histRPad, memory, dataHist, newBgHist, hist_def)
            
            pId += 1

            if pId > 4:
                pId = 1
                c1.Print(output_file);
                needToDraw = False;
            
        
        if needToDraw and not plot_single:
            for id in range(pId, 5):
                print "Clearing pad " + str(id)
                pad = histPad.cd(id)
                if plot_ratio:
                    ratioPads[pId][0].Clear()
                    ratioPads[pId][1].Clear()
                else:
                    pad.Clear()
        if needToDraw:
            c1.Print(output_file);
        
    c1.Print(output_file+"]");
    
    print "End: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    exit(0)

main()


