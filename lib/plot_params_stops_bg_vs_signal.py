import sys
import os
from ROOT import *
import copy 
from glob import glob

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib"))

from plot_params_base import *
import plotutils

skim_dir = "/afs/desy.de/user/d/diepholq/nfs/x1x2x1/signal/skim/sum/"

bgReTaggingOrderFull = {
    "resonances" : -3,
    "tautau" : -2,
    "other" : -1,
    "omega" : 0,
    "rho" : 1,
    "eta" : 2,
    "phi" : 3,
    "etaprime" : 4,
    "jpsi" : 5,
    "upsilon1" : 6,
    "upsilon2" : 7,
    "tc" : 8,
    "nbody" : 9,
    "scother" : 10,
    "fake" : 11,
    "jetty" : 12,
    "all" : 13
}

bgReTaggingNamesFull = {
    "resonances" : "resonances",
    "tautau" : "#tau#tau",
    "other" : "no information",
    "omega" : "#omega",
    "rho" : "#rho",
    "eta" : "#eta",
    "phi" : "#phi",
    "etaprime" : "#eta^{}'",
    "jpsi" : "J/#psi",
    "upsilon1" : "#Upsilon(1s)",
    "upsilon2" : "#Upsilon(2s)",
    "tc" : "no common parent",
    "nbody" : "n-body",
    "scother" : "other resonances",
    "fake" : "fake",
    "jetty" : "jetty",
    "all" : "bg"
}

bgReTagging = {
    "tautau" : "tautau%%%",
    "jetty" : "!tautau%%%"
}

signals = [
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm200GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm200GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm200GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm400GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm400GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm400GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_600GeV_mChipm115GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_600GeV_mChipm115GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_600GeV_mChipm115GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_600GeV_mChipm200GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_600GeV_mChipm200GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_600GeV_mChipm200GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_600GeV_mChipm400GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_600GeV_mChipm400GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_600GeV_mChipm400GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_700GeV_mChipm115GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_700GeV_mChipm115GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_700GeV_mChipm115GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_700GeV_mChipm200GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_700GeV_mChipm200GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_700GeV_mChipm200GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_700GeV_mChipm400GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_700GeV_mChipm400GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_700GeV_mChipm400GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_800GeV_mChipm115GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_800GeV_mChipm115GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_800GeV_mChipm115GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_800GeV_mChipm200GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_800GeV_mChipm200GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_800GeV_mChipm200GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_800GeV_mChipm400GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_800GeV_mChipm400GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_800GeV_mChipm400GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root"

]

# signalNames = [
#     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 0.6 Gev",
#     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.0 Gev",
#     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.4 Gev",
#     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 0.6 Gev",
#     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.0 Gev",
#     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.4 Gev",
#     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 0.6 Gev",
#     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 1.0 Gev",
#     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 1.4 Gev",
#     "m_{#tilde{t}} 600 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 0.6 Gev",
#     "m_{#tilde{t}} 600 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.0 Gev",
#     "m_{#tilde{t}} 600 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.4 Gev",
#     "m_{#tilde{t}} 600 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 0.6 Gev",
#     "m_{#tilde{t}} 600 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.0 Gev",
#     "m_{#tilde{t}} 600 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.4 Gev",
#     "m_{#tilde{t}} 600 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 0.6 Gev",
#     "m_{#tilde{t}} 600 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 1.0 Gev",
#     "m_{#tilde{t}} 600 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 1.4 Gev",
#     "m_{#tilde{t}} 700 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 0.6 Gev",
#     "m_{#tilde{t}} 700 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.0 Gev",
#     "m_{#tilde{t}} 700 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.4 Gev",
#     "m_{#tilde{t}} 700 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 0.6 Gev",
#     "m_{#tilde{t}} 700 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.0 Gev",
#     "m_{#tilde{t}} 700 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.4 Gev",
#     "m_{#tilde{t}} 700 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 0.6 Gev",
#     "m_{#tilde{t}} 700 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 1.0 Gev",
#     "m_{#tilde{t}} 700 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 1.4 Gev",
#     "m_{#tilde{t}} 800 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 0.6 Gev",
#     "m_{#tilde{t}} 800 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.0 Gev",
#     "m_{#tilde{t}} 800 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.4 Gev",
#     "m_{#tilde{t}} 800 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 0.6 Gev",
#     "m_{#tilde{t}} 800 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.0 Gev",
#     "m_{#tilde{t}} 800 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.4 Gev",
#     "m_{#tilde{t}} 800 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 0.6 Gev",
#     "m_{#tilde{t}} 800 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 1.0 Gev",
#     "m_{#tilde{t}} 800 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 1.4 Gev"
# ]


bdt_input_signal = [
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_600GeV_mChipm200GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root"
]
bdt_input_signal_name = [
    "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.4 GeV",
    
    "m_{#tilde{t}} 600 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.0 GeV",
]

unblinding_signal = [
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p4GeV_1.root",# pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_700GeV_mChipm115GeV_dm1p4GeV_1.root",# pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_600GeV_mChipm115GeV_dm1p0GeV_1.root",# pu35_part*of25_RA2AnalysisTree.root",
    skim_dir + "higgsino_Summer16_stopstop_800GeV_mChipm400GeV_dm0p6GeV_1.root",# pu35_part*of25_RA2AnalysisTree.root",
    
]

unblinding_signal_names = [
    "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.4 Gev",
    "m_{#tilde{t}} 700 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.4 Gev",
    "m_{#tilde{t}} 600 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.0 Gev",
    "m_{#tilde{t}} 800 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 0.6 Gev",
]


signals = [
#      skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm400GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root",
#      skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root",
     skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p4GeV_1.root",
     skim_dir + "higgsino_Summer16_stopstop_600GeV_mChipm200GeV_dm1p0GeV_1.root",
]

signalNames = [
    "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.4 Gev",
    "m_{#tilde{t}} 600 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.0 Gev"
]
# signals = glob("/nfs/dust/cms/user/diepholq/x1x2x1/signal/skim/single/higgsino_Summer16_stopstop_800GeV_mChipm400GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root")

# higgsino_Summer16_stopstop_800GeV_mChipm400GeV_dm1p0GeV_pu35_part14of25_RA2AnalysisTree.root
# signalNames = [
#     #  "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 0.6 Gev",
# #      "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.4 Gev",
#     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.0 Gev",
#     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.4 Gev",
#     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 1.4 Gev",
# #     "m_{#tilde{t}} 800 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 1.0 Gev",
# ]


common_histograms = [
    
    { "obs" : "MET", "minX" : 0, "maxX" : 800, "bins" : 30, "legendCoor" : {"x1" : .35, "y1" : .7, "x2" : .98, "y2" : .95}, "legendCol" : 3 },
    { "obs" : "dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT",  "bins" : 50},
    #{ "obs" : "MT2", "minX" : 0, "maxX" : 100, "bins" : 30 },
    { "obs" : "MHT", "minX" : 200, "maxX" : 500, "bins" : 30, "units" : "H_{T}^{Miss} [GeV]" , "legendCoor" : {"x1" : .35, "y1" : .65, "x2" : .98, "y2" : .95}, "legendCol" : 3  },
    { "obs" : "HT", "minX" : 0, "maxX" : 700, "bins" : 30 },
    #{ "obs" : "MetDHt", "minX" : 0, "maxX" : 700, "bins" : 30 },
    { "obs" : "leptonFlavour%%%", "minX" : 0, "maxX" : 2, "bins" : 2 },
    #{ "obs" : "int(genFlavour == \"Muons\")", "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["genFlavour"] },
    #{ "obs" : "int(genFlavour == \"Electrons\")", "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["genFlavour"] },
    
    { "obs" : "NJets", "minX" : 0, "maxX" : 7, "bins" : 7 , "legendCoor" : {"x1" : .35, "y1" : .75, "x2" : .98, "y2" : .95}},
    #{ "obs" : "BTagsLoose", "minX" : 0, "maxX" : 7, "bins" : 7 },
    #{ "obs" : "BTagsMedium", "minX" : 0, "maxX" : 7, "bins" : 7 },
    #{ "obs" : "BTagsDeepLoose", "minX" : 0, "maxX" : 7, "bins" : 7 },
    { "obs" : "BTagsDeepMedium", "minX" : 0, "maxX" : 7, "bins" : 7, "legendCoor" : {"x1" : 0.65, "y1" : .2, "x2" : .95, "y2" : .89}, "legendCol" : 1 },
    
    #{ "obs" : "LeadingJetQgLikelihood", "minX" : 0, "maxX" : 1, "bins" : 30 },
    { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 1.5, "bins" : 20, "units" : "Min\Delta_{}\phi(H_{T}^{Miss}, Jets)" },
    { "obs" : "MinDeltaPhiMetJets", "minX" : 0, "maxX" : 1.5, "bins" : 20, "units" : "Min\Delta_{}\phi(E_{T}^{Miss}, Jets)" },
    
    { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 800, "bins" : 30, "units" : "p_{T}(j_{1})" },
    { "obs" : "abs(LeadingJet.Eta())", "minX" : 0, "maxX" : 2.5, "bins" : 30, "usedObs" : ["LeadingJet"], "units" : "|\eta_{j_{1}}|" },
    #{ "obs" : "abs(LeadingJet.Eta())_2","formula" : "abs(LeadingJet.Eta())", "minX" : 0, "maxX" : 0.5, "bins" : 60, "usedObs" : ["LeadingJet"], "units" : "|\eta_{j_{1}}|" },
    #{ "obs" : "MaxCsv25", "minX" : 0, "maxX" : 1, "bins" : 30 },
    #{ "obs" : "MaxDeepCsv25", "minX" : 0, "maxX" : 1, "bins" : 30 },
    #{ "obs" : "LeadingJetMinDeltaRElectrons", "minX" : 0, "maxX" : 5, "bins" : 30 },
    { "obs" : "LeadingJetMinDeltaRMuons", "minX" : 0, "maxX" : 5, "bins" : 30 },
    { "obs" : 'int(vetoElectronsPassIso)', "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["vetoElectronsPassIso"]},
    #{ "obs" : 'int(vetoElectronsCorrJetIso10)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoElectronsMediumID)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoElectronsTightID)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoElectrons)', "minX" : 0, "maxX" : 2, "bins" : 2},
    { "obs" : 'int(vetoMuonsPassIso)', "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["vetoMuonsPassIso"]},
    { "obs" : "event_num", "formula" : "1", "units" : "Number of Events", "minX" : 0, "maxX" : 1, "bins" : 1},
    #{ "obs" : 'int(vetoMuonsCorrJetIso10)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoMuonoMediumID)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoMuonsTightID)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoMuons)', "minX" : 0, "maxX" : 2, "bins" : 2},

]

two_leps_histograms = [
    
    #HIST E
    { "obs" : "invMass%%%", "minX" : 0, "maxX" : 12, "bins" : 20, "blind" : [4,None],"units" : "M_{ll} [GeV]", "linearYspace" : 1.5, "legendCoor" : {"x1" : .35, "y1" : .65, "x2" : .98, "y2" : .95}, "legendCol" : 3  },
#     { "obs" : "invMass%%%", "minX" : 0, "maxX" : 12, "bins" : 20, "units" : "M_{ll} [GeV]", "linearYspace" : 1.5, "legendCoor" : {"x1" : .35, "y1" : .65, "x2" : .98, "y2" : .95}, "legendCol" : 3  },
    
    
    
    { "obs" : "deltaPhi%%%", "minX" : 0, "maxX" : 3.2, "bins" : 30 },
    { "obs" : "deltaEta%%%", "minX" : 0, "maxX" : 4, "bins" : 30, "units" : "\Delta_{}\eta" },
    { "obs" : "deltaR%%%", "minX" : 0, "maxX" : 4, "bins" : 30, "units" : "\Delta_{}R_{ll}", "linearYspace" : 1.5 },
    { "obs" : "dilepHt%%%", "minX" : 200, "maxX" : 400, "bins" : 30 },
   
    { "obs" : "nmtautau%%%", "minX" : 0, "maxX" : 200, "bins" : 30 },
    
    { "obs" : "mth1%%%", "minX" : 0, "maxX" : 100, "bins" : 30, "units" : "m_{T}(l_{1}) [GeV]", "linearYspace" : 1.5 },
    { "obs" : "mth2%%%", "minX" : 0, "maxX" : 200, "bins" : 30, "units" : "m_{T}(l_{2}) [GeV]", "linearYspace" : 1.5},
    
    { "obs" : "leptons%%%[0].Pt()", "minX" : 2, "maxX" : 15, "bins" : 30, "usedObs" : ["leptons%%%"], "units" : "p_{T}(l_{1}) [GeV]", "linearYspace" : 1.5 },
    { "obs" : "leptons%%%[1].Pt()", "minX" : 2, "maxX" : 15, "bins" : 30, "usedObs" : ["leptons%%%"], "units" : "p_{T}(l_{2}) [GeV]" },
    { "obs" : "abs(leptons%%%[0].Eta())", "minX" : 0, "maxX" : 2.4, "bins" : 30, "usedObs" : ["leptons%%%"] },
    { "obs" : "abs(leptons%%%[1].Eta())", "minX" : 0, "maxX" : 2.4, "bins" : 30, "usedObs" : ["leptons%%%"] },
    { "obs" : "deltaPhiMhtLepton1%%%", "minX" : 0, "maxX" : 3.5, "bins" : 30, "units" : "\Delta\phi(H_{T}^{Miss},l_{1})" },
    { "obs" : "deltaPhiMhtLepton2%%%", "minX" : 0, "maxX" : 3.5, "bins" : 30, "units" : "\Delta\phi(H_{T}^{Miss},l_{1})" },
    #{ "obs" : "leptons_ParentPdgId%%%[0]", "minX" : 0, "maxX" : 40, "bins" : 40, "usedObs" : ["leptons_ParentPdgId%%%"] },
    #{ "obs" : "leptons_ParentPdgId%%%[1]", "minX" : 0, "maxX" : 40, "bins" : 40, "usedObs" : ["leptons_ParentPdgId%%%"] },
    
    #{ "obs" : "deltaEtaLeadingJetDilepton%%%", "minX" : 0, "maxX" : 4, "bins" : 30 },
    #{ "obs" : "deltaPhiLeadingJetDilepton%%%", "minX" : 0, "maxX" : 4, "bins" : 30 },
    
    # { "obs" : "Electrons_minDeltaRJets[leptonsIdx%%%[0]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Electrons_minDeltaRJets"] },
#     { "obs" : "Electrons_minDeltaRJets[leptonsIdx%%%[1]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Electrons_minDeltaRJets"] },
#     
#     { "obs" : "Muons_minDeltaRJets[leptonsIdx%%%[0]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Muons_minDeltaRJets"] },
#     { "obs" : "Muons_minDeltaRJets[leptonsIdx%%%[1]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Muons_minDeltaRJets"] },
#     
#     { "obs" : "Electrons_deltaRLJ[leptonsIdx%%%[0]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Electrons_deltaRLJ"] },
#     { "obs" : "Electrons_deltaRLJ[leptonsIdx%%%[1]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Electrons_deltaRLJ"] },
#     
#     { "obs" : "Muons_deltaRLJ[leptonsIdx%%%[0]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Muons_deltaRLJ"] },
#     { "obs" : "Muons_deltaRLJ[leptonsIdx%%%[1]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Muons_deltaRLJ"] },
#     
#     { "obs" : "Electrons_deltaEtaLJ[leptonsIdx%%%[0]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Electrons_deltaEtaLJ"] },
#     { "obs" : "Electrons_deltaEtaLJ[leptonsIdx%%%[1]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Electrons_deltaEtaLJ"] },
#     
#     { "obs" : "Muons_deltaEtaLJ[leptonsIdx%%%[0]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Muons_deltaEtaLJ"] },
#     { "obs" : "Muons_deltaEtaLJ[leptonsIdx%%%[1]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Muons_deltaEtaLJ"] },

]

bdt_inputs_histograms = [                                                 #BDT Inputs 

    { "obs" : "custom_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT",  "bins" : 50, "customBins"  : [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.05,0.1,0.2,0.3,1]}, 
    { "obs" : "MHT", "minX" : 200, "maxX" : 500, "bins" : 30, "units" : "H_{T}^{Miss} [GeV]" , "legendCol" : 1  },
    { "obs" : "HT", "minX" : 0, "maxX" : 700, "bins" : 30 },
    { "obs" : "NJets", "minX" : 0, "maxX" : 7, "bins" : 7,"linear_log_space" : 100 },
    { "obs" : "BTagsDeepMedium", "minX" : 0, "maxX" : 7, "bins" : 7, "legendCol" : 1 },
    { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 1.5, "bins" : 20, "units" : "Min\Delta_{}\phi(H_{T}^{Miss}, Jets)","linear_log_space" : 100 },
    { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 800, "bins" : 30, "units" : "p_{T}(j_{1})"},
    { "obs" : "abs(LeadingJet.Eta())", "minX" : 0, "maxX" : 2.5, "bins" : 30, "usedObs" : ["LeadingJet"], "units" : "|\eta_{j_{1}}|" },
    { "obs" : "invMass%%%", "minX" : 0, "maxX" : 12, "bins" : 20, "blind" : [4,None],"units" : "M_{ll} [GeV]", "linearYspace" : 1.5  },
    { "obs" : "deltaPhi%%%", "minX" : 0, "maxX" : 3.2, "bins" : 30, "units": "\Delta\phi" },
    { "obs" : "deltaEta%%%", "minX" : 0, "maxX" : 4, "bins" : 30, "units" : "\Delta_{}\eta" },
    { "obs" : "deltaR%%%", "minX" : 0, "maxX" : 4, "bins" : 30, "units" : "\Delta_{}R_{ll}", "linearYspace" : 1.5 },
    { "obs" : "mth1%%%", "minX" : 0, "maxX" : 100, "bins" : 30, "units" : "m_{T}(l_{1}) [GeV]", "linearYspace" : 1.5 },
    { "obs" : "leptons%%%[0].Pt()", "minX" : 2, "maxX" : 15, "bins" : 30, "usedObs" : ["leptons%%%"], "units" : "p_{T}(l_{1}) [GeV]", "linearYspace" : 1.5 },
    { "obs" : "leptons%%%[1].Pt()", "minX" : 2, "maxX" : 15, "bins" : 30, "usedObs" : ["leptons%%%"], "units" : "p_{T}(l_{2}) [GeV]" },
    { "obs" : "abs(leptons%%%[0].Eta())", "minX" : 0, "maxX" : 2.4, "bins" : 30, "usedObs" : ["leptons%%%"], "units": "|\eta_{ll}|" },
    { "obs" : "deltaPhiMhtLepton1%%%", "minX" : 0, "maxX" : 3.5, "bins" : 30, "units" : "\Delta\phi(H_{T}^{Miss},l_{1})" },
    { "obs" : "deltaPhiMhtLepton2%%%", "minX" : 0, "maxX" : 3.5, "bins" : 30, "units" : "\Delta\phi(H_{T}^{Miss},l_{2})" },
    { "obs" : "dileptonPt%%%", "minX" : 0, "maxX" : 15, "bins" : 30, "units" : "dilepton p_{T}" },
    ] 

class stops_bg_vs_signal(BaseParams):
    signal_dir = signals
    signal_names = signalNames
    bg_dir = "/nfs/dust/cms/user/diepholq/x1x2x1/bg/skim/sum/type_sum"

    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio",
    }
    
    calculatedLumi = {
        'MET' : utils.LUMINOSITY/1000.0,
    }
    
    plot_bg = True
    plot_data = False
    plot_signal = True
    
    
    
    plot_overflow = True
    plot_error = True
    plot_significance = True
    
    histograms_defs = []
    cuts = []
    
    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_bg_vs_signal.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    
   #  histograms_defs = [
#         { "obs" : "MET", "minX" : 0, "maxX" : 800, "bins" : 30 },
#         #{ "obs" : "MET2", "formula" : "MET", "minX" : 0, "maxX" : 600, "bins" : 80, "condition" : "HT < 600" },
#         { "obs" : "MHT", "minX" : 200, "maxX" : 500, "bins" : 30, "units" : "H_{T}^{Miss} [GeV]" },
#         { "obs" : "HT", "minX" : 0, "maxX" : 700, "bins" : 30 },
#         { "obs" : "invMass%%%", "minX" : 0, "maxX" : 12, "bins" : 20 ,"units" : "M_{ll} [GeV]", "linearYspace" : 1.5 },
#     ]
    
    histograms_defs = copy.deepcopy(common_histograms + two_leps_histograms)
    
    cuts = [
    {"name":"none", "title": "MET > 140 && MinDeltaPhiMhtJets > 0.4", "condition" : "MET > 140 && MinDeltaPhiMhtJets > 0.4", "baseline" : " leptonFlavour%%% == \"Muons\" && sameSign%%% == 0", "sc" : "1"}, 

	{"name":"step1", "title": "MET > 140 && MinDeltaPhiMhtJets > 0.4 && leptons%%%[0].Pt() < 7 && leptons%%%[1].Pt() < 7", "condition" : "MET > 140 && BTagsDeepMedium > 0 && MinDeltaPhiMhtJets > 0.4", "baseline" : "twoLeptons%%% == 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0", "sc" : "1"},
        
	{"name":"step3", "title": "MET > 140 && BTagsDeepMedium > 1 && MinDeltaPhiMhtJets > 0.4", "condition" : "MET > 140 && BTagsDeepMedium > 1 && MinDeltaPhiMhtJets > 0.4", "baseline" : "twoLeptons%%% == 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0", "sc" : "1"},

    ]
    
    legend_coordinates = {"x1" : .35, "y1" : .40, "x2" : .95, "y2" : .89}
    #legend_coordinates = {"x1" : 0.65, "y1" : .2, "x2" : .95, "y2" : .89}
    legend_columns = 2
    legend_border = 0
    
    y_title_offset = 1.3
    y_title = "Events"
    
    jetIsoStr = "NoIso"
    injectJetIsoToCuts(cuts, jetIsoStr)
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)
    





class stops_bg_vs_signal_Iso(BaseParams):
    signal_dir = signals
#     signal_dir = bdt_input_signal
#     signal_names = bdt_input_signal_name
    signal_names = signalNames
    bg_dir = "/nfs/dust/cms/user/diepholq/x1x2x1/bg/skim/sum/type_sum"

    weightString = {
    'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * puWeight",
    }

    calculatedLumi = {
    'MET' : utils.LUMINOSITY/1000.0,
    }

    plot_bg = True
    plot_data = False
    plot_signal = True
    
    glob_signal = True

    no_weights = False

    plot_overflow = False
    plot_error = True
    plot_significance = True

    histograms_defs = []
    cuts = []

    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_bg_vs_signal_Iso.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = False 

    #  histograms_defs = [
    #         { "obs" : "MET", "minX" : 0, "maxX" : 800, "bins" : 30 },
    #         #{ "obs" : "MET2", "formula" : "MET", "minX" : 0, "maxX" : 600, "bins" : 80, "condition" : "HT < 600" },
    #         { "obs" : "MHT", "minX" : 200, "maxX" : 500, "bins" : 30, "units" : "H_{T}^{Miss} [GeV]" },
    #         { "obs" : "HT", "minX" : 0, "maxX" : 700, "bins" : 30 },
    #         { "obs" : "invMass%%%", "minX" : 0, "maxX" : 12, "bins" : 20 ,"units" : "M_{ll} [GeV]", "linearYspace" : 1.5 },
    #     ]

    #histograms_defs = copy.deepcopy(common_histograms + two_leps_histograms)
    histograms_defs = [
    { "obs" : "dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT",  "bins" : 50},
    { "obs" : "NSelectionMuons%%%", "minX" : -1, "maxX" : 1, "units" : "NMuons",  "bins" : 6, "minX" : 0, "maxX" : 6},
    { "obs" : "custom_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT",  "bins" : 50, "customBins"  : [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.05,0.1,0.2,0.3,1]},
    { "obs" : "BTagsDeepMedium", "minX" : 0, "maxX" : 7, "bins" : 7, "legendCoor" : {"x1" : 0.65, "y1" : .2, "x2" : .95, "y2" : .89}, "legendCol" : 1 },
    { "obs" : "NJets", "minX" : 0, "maxX" : 7, "bins" : 7 , "legendCoor" : {"x1" : .35, "y1" : .75, "x2" : .98, "y2" : .95}},
    ] #16
    cuts = [
    #{"name":"none", "title": "MET > 140 && MinDeltaPhiMhtJets > 0.4", "condition" : "MET > 140 && MinDeltaPhiMhtJets > 0.4 && twoLeptons%%% == 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0", "baseline" : "1", "sc" : "1"}, #sc?
#     {"name":"nmtautau", "title": "preselection baseline","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0 && dilepBDT%%% < -0.1 && (nmtautau%%% > 160 || nmtautau%%% < 0) && passesUniversalSelection == 1 && NJets > 1", "baseline" : "1", "sc" : "1"}  ,
#     {"name":"nmtautau", "title": "preselection baseline","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0 && (nmtautau%%% > 160 || nmtautau%%% < 0) && passesUniversalSelection == 1 && NJets > 1", "baseline" : "1", "sc" : "1"}  ,
#    {"name":"bdt", "title": "BDT","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 1 && leptonFlavour%%% == \"Muons\"  && sameSign%%% == 0", "baseline" : "1", "sc" : "1"},
    {"name":"finalcut", "title": "finalcut","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0 && (nmtautau%%% > 160 || nmtautau%%% < 0) && passesUniversalSelection == 1 && NJets > 1", "baseline" : "1", "sc" : "1"}  
    #{"name":"bjetsgreaterone", "title": "BTagsDeepMedium >= 2","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 2 && leptonFlavour%%% == \"Muons\"  && sameSign%%% == 0", "baseline" : "1", "sc" : "1"}
    ]

    legend_coordinates = {"x1" : .35, "y1" : .40, "x2" : .95, "y2" : .89}
    #legend_coordinates = {"x1" : 0.65, "y1" : .2, "x2" : .95, "y2" : .89}
    legend_columns = 2
    legend_border = 0

    y_title_offset = 1.3
    y_title = "Events"


    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
    injectJetIsoToCuts(cuts, jetIsoStr)
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)





class bdt_check(stops_bg_vs_signal_Iso):
    signal_dir = ["/afs/desy.de/user/n/nissanuv/q_nfs/x1x2x1/signal/skim/single/higgsino_Summer16_stopstop*dm[01]p*"]
    signal_names = ["Signal"]
    histograms_defs = [{ "obs" : "dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT",  "bins" : 50}]
    #higgsino_Summer16_stopstop_800GeV_mChipm400GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree
    #"dm0p dm1p"
    cuts =[ {"name":"none", "title": "BDT", "condition" : "twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 1 && leptonFlavour%%% == \"Muons\"  && sameSign%%% == 0", "baseline" : "1", "sc" : "1"}]
    plot_bg = False
    
    histrograms_file = BaseParams.histograms_root_files_dir + "/bdt_check.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    
    no_weights = True
    
    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
    injectJetIsoToCuts(cuts, jetIsoStr)
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)


class bg_retag(stops_bg_vs_signal_Iso):
    plot_signal = True
    bg_retag = True
    bgReTagging = copy.deepcopy(bgReTagging)
    bgReTaggingOrder = bgReTaggingOrderFull
    bgReTaggingNames = bgReTaggingNamesFull
    histrograms_file = BaseParams.histograms_root_files_dir + "/bg_retag.root"
    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
    injectJetIsoToMapValues(bgReTagging, jetIsoStr)


class all_bg(bg_retag):
   #  histograms_defs = [
#     { "obs" : "custom_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT",  "bins" : 50, "customBins"  : [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.05,0.1,0.2,0.3,1]},
#     ]
    histograms_defs = [
      { "obs" : "custom_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT",  "bins" : 50, "customBins"  : [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.05,0.1,0.2,0.3,1]}
      ]
    signal_dir = signals

    signal_names = signalNames
#     histograms_defs = bdt_inputs_histograms
#     signal_dir = bdt_input_signal
#     signal_names = bdt_input_signal_name 
    plot_signal = True
    plot_bg = True
    
    bgReTagging = {                               #uncomment for all bg in blue
    "all" : "1"
    }
    
    weightString = {
    'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * puWeight",
    }

    # bgReTaggingFactors = {                #without pu
#         "all" : [0.781,0.06],
#     }

    # bgReTaggingFactors = {                  #with pu
#         "all" : [1.024,0.080],
#     }


    # bgReTagging = copy.deepcopy(bgReTagging)        #uncomment for split in jetty and tau
#     bgReTaggingOrder = bgReTaggingOrderFull
#      bgReTaggingNames = bgReTaggingNamesFull
    plot_overflow = False
    cuts = [
    #{"name":"none", "title": "MET > 140 && MinDeltaPhiMhtJets > 0.4", "condition" : "MET > 140 && MinDeltaPhiMhtJets > 0.4 && twoLeptons%%% == 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0", "baseline" : "1", "sc" : "1"}, #sc?

   #  {"name":"final_preselection_without_tautau", "title": "final preselection without tautau","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && leptonFlavour%%% == \"Muons\"  && sameSign%%% == 0 && BTagsDeepMedium >= 1 && passesUniversalSelection == 1 && NJets > 1 && dilepBDT%%% < -0.1 ", "baseline" : "1", "sc" : "1"},
    {"name":"final_preselection", "title": "final preselection","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && leptonFlavour%%% == \"Muons\"  && sameSign%%% == 0 && BTagsDeepMedium >= 1 && (nmtautau%%% > 160 || nmtautau%%% < 0) && passesUniversalSelection == 1 && NJets > 1", "baseline" : "1", "sc" : "1"}
#     {"name":"directly post bdt", "title": "BDT","condition" : "MHT > 200 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && leptonFlavour%%% == \"Muons\"  && sameSign%%% == 0 && BTagsDeepMedium >= 1", "baseline" : "1", "sc" : "1"}
    ]
    legend_coordinates = {"x1" : .50, "y1" : .7, "x2" : .90, "y2" : .95}                #x1: .40
    # legend_coordinates = {"x1" : .80, "y1" : .8, "x2" : .90, "y2" : .95}                   #for jetty tau
    legend_columns = 1
    
    histrograms_file = BaseParams.histograms_root_files_dir + "/bg_retag_bdt_inputs.root"
    load_histrograms_from_file = False
    save_histrograms_to_file = False
    
    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)
    injectJetIsoToMapValues(bgReTagging, jetIsoStr)
    injectJetIsoToCuts(cuts, jetIsoStr)




class stops_datacontrolregion(stops_bg_vs_signal_Iso):
    data_dir = "/afs/desy.de/user/d/diepholq/nfs/x1x2x1/data/skim/sum/"
    
    histograms_defs = [

    { "obs" : "custom_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT",  "bins" : 50, "customBins"  : [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.05,0.1,0.2,0.3,1]},
#     { "obs" : "MET", "minX" : 0, "maxX" : 800, "bins" : 30, "legendCoor" : {"x1" : .35, "y1" : .7, "x2" : .98, "y2" : .95}, "legendCol" : 3 },
#     { "obs" : "dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT",  "bins" : 50},
# 
    { "obs" : "MHT", "minX" : 200, "maxX" : 500, "bins" : 30, "units" : "H_{T}^{Miss} [GeV]" , "legendCoor" : {"x1" : .35, "y1" : .65, "x2" : .98, "y2" : .95}, "legendCol" : 3  },
    { "obs" : "HT", "minX" : 0, "maxX" : 700, "bins" : 30 },
# 
#     { "obs" : "leptonFlavour%%%", "minX" : 0, "maxX" : 2, "bins" : 2 },
# 
    { "obs" : "NJets", "minX" : 0, "maxX" : 7, "bins" : 7 , "legendCoor" : {"x1" : .35, "y1" : .75, "x2" : .98, "y2" : .95}},
# 
    { "obs" : "BTagsDeepMedium", "minX" : 0, "maxX" : 7, "bins" : 7, "legendCoor" : {"x1" : 0.65, "y1" : .2, "x2" : .95, "y2" : .89}, "legendCol" : 1 },
# 
    { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 1.5, "bins" : 20, "units" : "Min\Delta_{}\phi(H_{T}^{Miss}, Jets)" },
#     { "obs" : "MinDeltaPhiMetJets", "minX" : 0, "maxX" : 1.5, "bins" : 20, "units" : "Min\Delta_{}\phi(E_{T}^{Miss}, Jets)" },
#     
    { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 800, "bins" : 30, "units" : "p_{T}(j_{1})" },
    { "obs" : "abs(LeadingJet.Eta())", "minX" : 0, "maxX" : 2.5, "bins" : 30, "usedObs" : ["LeadingJet"], "units" : "|\eta_{j_{1}}|" },
# 
#     { "obs" : "LeadingJetMinDeltaRMuons", "minX" : 0, "maxX" : 5, "bins" : 30 },
#     { "obs" : 'int(vetoElectronsPassIso)', "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["vetoElectronsPassIso"]},
# 
#     { "obs" : 'int(vetoMuonsPassIso)', "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["vetoMuonsPassIso"]},
    { "obs" : "invMass%%%", "minX" : 0, "maxX" : 12, "bins" : 20, "blind" : [4,None],"units" : "M_{ll} [GeV]", "linearYspace" : 1.5, "legendCoor" : {"x1" : .35, "y1" : .65, "x2" : .98, "y2" : .95}, "legendCol" : 3  },
    { "obs" : "deltaPhi%%%", "minX" : 0, "maxX" : 3.2, "bins" : 30 },
    { "obs" : "deltaEta%%%", "minX" : 0, "maxX" : 4, "bins" : 30, "units" : "\Delta_{}\eta" },
    { "obs" : "deltaR%%%", "minX" : 0, "maxX" : 4, "bins" : 30, "units" : "\Delta_{}R_{ll}", "linearYspace" : 1.5 },
#     { "obs" : "dilepHt%%%", "minX" : 200, "maxX" : 400, "bins" : 30 },
#    
#     { "obs" : "nmtautau%%%", "minX" : 0, "maxX" : 200, "bins" : 30 },
#     
    { "obs" : "mth1%%%", "minX" : 0, "maxX" : 100, "bins" : 30, "units" : "m_{T}(l_{1}) [GeV]", "linearYspace" : 1.5 },
#     { "obs" : "mth2%%%", "minX" : 0, "maxX" : 200, "bins" : 30, "units" : "m_{T}(l_{2}) [GeV]", "linearYspace" : 1.5},
#     
    { "obs" : "leptons%%%[0].Pt()", "minX" : 2, "maxX" : 15, "bins" : 30, "usedObs" : ["leptons%%%"], "units" : "p_{T}(l_{1}) [GeV]", "linearYspace" : 1.5 },
    { "obs" : "leptons%%%[1].Pt()", "minX" : 2, "maxX" : 15, "bins" : 30, "usedObs" : ["leptons%%%"], "units" : "p_{T}(l_{2}) [GeV]" },
    { "obs" : "abs(leptons%%%[0].Eta())", "minX" : 0, "maxX" : 2.4, "bins" : 30, "usedObs" : ["leptons%%%"] },
#     { "obs" : "abs(leptons%%%[1].Eta())", "minX" : 0, "maxX" : 2.4, "bins" : 30, "usedObs" : ["leptons%%%"] },
    { "obs" : "deltaPhiMhtLepton1%%%", "minX" : 0, "maxX" : 3.5, "bins" : 30, "units" : "\Delta\phi(H_{T}^{Miss},l_{1})" },
    { "obs" : "deltaPhiMhtLepton2%%%", "minX" : 0, "maxX" : 3.5, "bins" : 30, "units" : "\Delta\phi(H_{T}^{Miss},l_{2})" },
    { "obs" : "dileptonPt%%%", "minX" : 0, "maxX" : 15, "bins" : 30, "units" : "dilepton p_{T}" },
    ] #16 custom bins
    
    cuts = [
    #{"name":"bdt", "title": "Baseline","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 1 && leptonFlavour%%% == \"Muons\"  && sameSign%%% == 0 && dilepBDT%%% < -0.1 && passesUniversalSelection == 1", "baseline" : "1", "sc" : "1"},  
    {"name":"nmtautau", "title": "(nmtautau%%% > 160 || nmtautau%%% < 0)","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0 && dilepBDT%%% < -0.1 && (nmtautau%%% > 160 || nmtautau%%% < 0) && passesUniversalSelection == 1 && NJets > 1", "baseline" : "1", "sc" : "1"}  
    ]

    calculatedLumi = {
#         'MET' : 36.007270741,
#         'MET' : 3000.007270741,
        'MET' : 36.052169110,
    }
       
    weightString = {
        'MET' : "BranchingRatio * Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
#        'MET' : "BranchingRatio * Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        #'MET' : "BranchingRatio * Weight",
    }
    # bgReTagging = copy.deepcopy(bgReTagging)        
#     bgReTaggingOrder = bgReTaggingOrderFull
#     bgReTaggingNames = bgReTaggingNamesFull
    
    legend_coordinates = {"x1" : .6, "y1" : .6, "x2" : .8, "y2" : .9}
    legend_columns = 1

    plot_bg = True
    plot_data = True
    plot_signal = False
    blind_data = False
    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_control_region.root_smbg.root"
    load_histrograms_from_file = False
    save_histrograms_to_file = True
    

    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)
#     injectJetIsoToMapValues(bgReTagging, jetIsoStr)
    plot_ratio = True
    injectJetIsoToCuts(cuts, jetIsoStr)


class stops_datacontrolregion_transfer_factor(stops_datacontrolregion):
    weightString = {
        'MET' : "BranchingRatio * Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
    }
    cuts = [
    {"name":"nmtautau", "title": "(nmtautau%%% > 160 || nmtautau%%% < 0)","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0 && dilepBDT%%% < -0.2 && (nmtautau%%% > 160 || nmtautau%%% < 0) && passesUniversalSelection == 1 && NJets > 1", "baseline" : "1", "sc" : "1"}  
    ]
    histograms_defs = [    { "obs" : "custom_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT",  "bins" : 50, "customBins"  : [-1,-0.2], "linearYspace" : 1.4, "linear_log_space": 100 },
    ]
    
    legend_coordinates = {"x1" : .4, "y1" : .75, "x2" : .9, "y2" : .9}
    legend_columns = 3
    
    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_control_region_TransferFactor.root"
    load_histrograms_from_file = False
    save_histrograms_to_file = True
    
    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)
    injectJetIsoToCuts(cuts, jetIsoStr)
    
    
class stops_datacontrolregion_rescaled_with_pu(stops_datacontrolregion):
#     histograms_defs = bdt_inputs_histograms
    cuts = [
    #{"name":"bdt", "title": "Baseline","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 1 && leptonFlavour%%% == \"Muons\"  && sameSign%%% == 0 && dilepBDT%%% < -0.1 && passesUniversalSelection == 1", "baseline" : "1", "sc" : "1"},  
    {"name":"nmtautau", "title": "(nmtautau%%% > 160 || nmtautau%%% < 0)","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0 && dilepBDT%%% < -0.1 && (nmtautau%%% > 160 || nmtautau%%% < 0) && passesUniversalSelection == 1 && NJets > 1", "baseline" : "1", "sc" : "1"}  
    ]
    
    weightString = {
        'MET' : "BranchingRatio * Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
    }
    
    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_control_region_pu.root"
    bg_retag = True
    bgReTaggingOrder = bgReTaggingOrderFull
    bgReTaggingNames = bgReTaggingNamesFull

    
    legend_coordinates = {"x1" : .80, "y1" : .8, "x2" : .90, "y2" : .95}
    
    bgReTagging = {
        "all" : "1"
    }
    
    bgReTaggingFactors = {
        "all" : [1.037,0.080],
    }
    
    load_histrograms_from_file = False
    save_histrograms_to_file = True
    
    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
#     injectJetIsoToHistograms(histograms_defs, jetIsoStr)
    injectJetIsoToMapValues(bgReTagging, jetIsoStr)
    injectJetIsoToCuts(cuts, jetIsoStr)
    



class stops_same_sign_controlregion(stops_datacontrolregion):

    cuts = [
#     {"name":"nmtautau", "title": "(nmtautau%%% > 160 || nmtautau%%% < 0)","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 1 && NSelectionMuons%%% == 2 && (nmtautau%%% > 160 || nmtautau%%% < 0) && passesUniversalSelection == 1 && NJets > 1", "baseline" : "1", "sc" : "1"}
    {"name":"preselection_from_BT", "title": "preselection_from_BT","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 1 && NSelectionMuons%%% == 2 && passesUniversalSelection == 1 && NJets > 1", "baseline" : "1", "sc" : "1"}
    ]
    
    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_same_sign_control_region.root"
    load_histrograms_from_file = False
    save_histrograms_to_file = False
    
    bg_retag = True
    bgReTagging = {
    "all" : "1"
    }
    bgReTaggingOrder = bgReTaggingOrderFull
    bgReTaggingNames = bgReTaggingNamesFull

    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
#     injectJetIsoToMapValues(bgReTagging, jetIsoStr)
    plot_ratio = True
    injectJetIsoToCuts(cuts, jetIsoStr)
    injectJetIsoToMapValues(bgReTagging, jetIsoStr)

class stops_same_sign_controlregion_TF(stops_same_sign_controlregion):

    histograms_defs = [
    { "obs" : "custom_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT",  "bins" : 50, "customBins"  : [-1,-0.2], "linearYspace" : 1.4, "linear_log_space": 100 },
    ]
    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_same_signcontrol_region_TF.root"
    load_histrograms_from_file = False
    save_histrograms_to_file = False
    
    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)


class stops_same_sign_controlregion_rescaled_with_TF(stops_same_sign_controlregion):
#     histograms_defs = [{ "obs" : "custom_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT",  "bins" : 50, "customBins"  : [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.05,0.1,0.2,0.3,1]}]
    histograms_defs = bdt_inputs_histograms
    #     histograms_defs = [
    #     { "obs" : "deltaPhiMhtLepton1%%%", "minX" : 0, "maxX" : 3.5, "bins" : 30, "units" : "\Delta\phi(H_{T}^{Miss},l_{1})" },
    #     { "obs" : "deltaPhiMhtLepton2%%%", "minX" : 0, "maxX" : 3.5, "bins" : 30, "units" : "\Delta\phi(H_{T}^{Miss},l_{2})" }
    #     ]
    legend_coordinates = {"x1" : .80, "y1" : .8, "x2" : .90, "y2" : .95}
    bgReTaggingFactors = {
        "all" : [1.038,0.08],
    }
    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_same_signcontrol_region_rescaled_with_TF.root"
    load_histrograms_from_file = False
    save_histrograms_to_file = False

#     fit_linear_ratio_plot = True
    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)

class stops_unblinding(stops_datacontrolregion):
    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_unblinding.root"
    load_histrograms_from_file = False
    save_histrograms_to_file = False
    
    signal_dir = unblinding_signal
    signal_names = unblinding_signal_names
    legend_coordinates = {"x1" : .57, "y1" : .5, "x2" : .90, "y2" : .95}
    
    histograms_defs = [{ "obs" : "custom_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT", "linear_log_space": 100,  "bins" : 50, "customBins"  : [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.05,0.1,0.2,0.3,1]}]
    
    cuts = [
    {"name":"unblinding", "title": "unblinding","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0 && (nmtautau%%% > 160 || nmtautau%%% < 0) && passesUniversalSelection == 1 && NJets > 1", "baseline" : "1", "sc" : "1"}  
    ]
    
    glob_signal = True
    plot_bg = True
    plot_data = True
    plot_signal = True
    bg_retag = True
    bgReTagging = {
        "all" : "1"
    }
    bgReTaggingFactors = {
        "all" : [1.037,0.080],
    }
    bgReTaggingOrder = bgReTaggingOrderFull
    bgReTaggingNames = bgReTaggingNamesFull
    
    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
    injectJetIsoToCuts(cuts, jetIsoStr)
    injectJetIsoToMapValues(bgReTagging, jetIsoStr)
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)
    
    
    
    
    
class stops_datacontrolregion_rescaled_without_pu(stops_datacontrolregion_rescaled_with_pu):

    weightString = {
        'MET' : "BranchingRatio * Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016",
    }
    
    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_control_region_nopu.root"
    load_histrograms_from_file = False
    save_histrograms_to_file = True
 
 
    bgReTaggingFactors = {
        "all" : [0.781,0.06],
    }
    
 
class stops_bg_two_vs_three_muons_bg(stops_bg_vs_signal_Iso):
    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_bg_two_vs_three_muons_bg.root"
    plot_signal = True
    no_weights = False
    bg_retag = True
    signal_dir = [
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm0p6GeV_1.root",
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p4GeV_1.root",
   # skim_dir + "higgsino_Summer16_stopstop_700GeV_mChipm200GeV_dm1p4GeV_1.root",  
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm400GeV_dm1p4GeV_1.root",
    ]
    signal_names = [
     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 0.6 Gev",
     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.4 Gev",
   #  "m_{#tilde{t}} 700 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.4 Gev",
     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 1.4 Gev",
]
    
    save_histrograms_to_file = True
    load_histrograms_from_file = False 
    
    bgReTagging = {
        "2-muons" : "(leptonsIdx%%%[2] == -1)",
        "3-muons" : "(leptonsIdx%%%[2] >= 0)",
    }
    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
    injectJetIsoToMapValues(bgReTagging, jetIsoStr)
    
    bgReTaggingOrder = {
        "2-muons" : 0,
        "3-muons" : 1
    }
    bgReTaggingNames = {
        "2-muons" : "2 Muons",
        "3-muons" : "3 Muons"
    }
    
class stops_bg_two_vs_three_muons_signal(stops_bg_two_vs_three_muons_bg):
    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_bg_two_vs_three_muons_signal.root"
    plot_signal = True
    plot_bg = False
    
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    
    
    signal_dir = [
 #        skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm0p6GeV_1.root",
         skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p4GeV_1.root",
 #       skim_dir + "higgsino_Summer16_stopstop_700GeV_mChipm200GeV_dm1p4GeV_1.root",  
#         skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm400GeV_dm1p4GeV_1.root",
    ]
    signal_names = [
#     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 0.6 Gev",
     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.4 Gev",
#    "m_{#tilde{t}} 700 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.4 Gev",
#     "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 1.4 Gev",
]
    

    
    object_retag = True
    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
    object_retag_map = {
        "l" : [ 
                { "2 Muons" : "(leptonsIdx%%%[2] == -1)".replace("%%%", jetIsoStr)},
                { "3 Muons" : "(leptonsIdx%%%[2] >= 0)".replace("%%%", jetIsoStr)}
                ],
    }
    
    no_weights = False
    
    #injectJetIsoToMapValues(object_retag_map["l"], jetIsoStr)
    
    
    for histDef in stops_bg_two_vs_three_muons_bg.histograms_defs:
        histDef["object"] = "l"
    



