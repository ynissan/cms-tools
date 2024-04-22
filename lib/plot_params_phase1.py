import sys
import os
from ROOT import *
import copy 
from glob import glob
import utils

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib"))

from plot_params_base import *
import plotutils

skim_dir = "/afs/desy.de/user/d/diepholq/nfs/x1x2x1/signal/skim_phase1/sum/"


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
     skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p4GeV_1.root",
     skim_dir + "higgsino_Summer16_stopstop_600GeV_mChipm200GeV_dm1p0GeV_1.root",
]

signalNames = [
    "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.4 Gev",
    "m_{#tilde{t}} 600 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.0 Gev"
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
    { "obs" : "deltaPhiMhtLepton2%%%l", "minX" : 0, "maxX" : 3.5, "bins" : 30, "units" : "\Delta\phi(H_{T}^{Miss},l_{2})" },
    { "obs" : "dileptonPt%%%", "minX" : 0, "maxX" : 15, "bins" : 30, "units" : "dilepton p_{T}" },
    ] 

class stops_phase1_Iso(BaseParams):
    signal_dir = signals
    signal_names = signalNames
    bg_dir = "/afs/desy.de/user/d/diepholq/nfs/x1x2x1/bg/skim/sum/type_sum"

    weightString = {
    'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * puWeight",
    }

    calculatedLumi = {
    'MET' : utils.LUMINOSITY/1000.0,
    }

    plot_bg = True
    plot_data = False
    plot_signal = False
    
    glob_signal = True

    no_weights = False

    plot_overflow = False
    plot_error = True
    plot_significance = True

    histograms_defs = []
    cuts = []

    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_phase1_Iso.root"
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
    { "obs" : "MET", "minX" : 0, "maxX" : 800, "bins" : 30 },
    ]
    cuts = [
    {"name":"finalcut", "title": "finalcut","condition" : "MET > 140 && MHT > 220 && twoLeptons%%% == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium >= 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0 && (nmtautau%%% > 160 || nmtautau%%% < 0) && passesUniversalSelection == 1 && NJets > 1", "baseline" : "1", "sc" : "1"}
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


