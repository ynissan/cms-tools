import sys
import os
from ROOT import *

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))

import utils

from plot_params_base import *

class signal_phase1_l1_prefire_dm1p759GeV(BaseParams):
    histrograms_file = BaseParams.histograms_root_files_dir + "/signal_phase1_l1_prefire_dm1p759GeV.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    signal_dir = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_phase1/slim_sum/mChipm100GeV_dm1p759GeV_1.root",
              ]
    
    signal_names = [
    "\Delta_{}M 1.75 Gev",
    ]
    
    plot_bg = False
    plot_data = False
    plot_overflow = False
    object_retag = False
    glob_signal = False
    plot_error = True
    
    sig_line_width = 1

    legend_coordinates = {"x1" : .65, "y1" : .60, "x2" : .98, "y2" : .95}
    legend_columns = 1
    legend_border = 0
    
    plot_sc = False
    
    plot_ratio = True
    plot_custom_ratio = 1
    customRatios = [  [["prefireWeight"],["base"]] ]  
    customRatiosNames = [  ["pW","base"]  ]
    ratio_style_numerator_hist = True
    stamp_ratio_integral = True
    
    label_text = plotutils.StampStr.SIM
    
    jetIso = "CorrJetNoMultIso10Dr0.6"
    
    cuts = [
        {"name":"none", "title": "None", "condition" : "(MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && isoCr%%% == 0)"},
    ]
    injectJetIsoToCuts(cuts, jetIso)

    histograms_defs = [     
        { "obs" : "fine_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "bins" : 40, "units" : "BDT", "legendCol" : 1, "legendCoor" : {"x1" : .15, "y1" : .70, "x2" : .65, "y2" : .79}, "object" : "s"},
        { "obs" : "signal_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : 0, "maxX" : 1, "bins" : 40, "units" : "BDT", "legendCol" : 1, "legendCoor" : {"x1" : .15, "y1" : .70, "x2" : .65, "y2" : .79}, "object" : "s"}
    ]
    injectJetIsoToHistograms(histograms_defs, jetIso)
    
    weightString = {
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * BranchingRatio * passesUniversalSelection",
    }
    
    use_calculated_lumi_weight = True
    no_weights = False
    show_lumi = True
    
    object_retag = True

    object_retag_map = {
        "s" : [ 
                {"base" : "1"},
                {"prefireWeight" : "1"},
            ],
    }
    
    object_retag_labels = {
         "s" : {
            "base" : "\Delta_{}M^{\pm} 1.75 Gev",
            "prefireWeight" : "prefireWeight"
            },
    }
    
    object_retag_weights = {
         "prefireWeight" :  "prefireWeight"
    }
    
    colorPalette = [
         { "name" : "blue", "fillColor" : kBlue, "lineColor" : kBlue, "fillStyle" : 0},
         { "name" : "red", "fillColor" : kRed, "lineColor" : kRed, "fillStyle" : 0 },
    ]

    
class signal_phase1_l1_prefire_dm2p259GeV(signal_phase1_l1_prefire_dm1p759GeV):
    histrograms_file = BaseParams.histograms_root_files_dir + "/signal_phase1_l1_prefire_dm2p259GeV.root"
    signal_dir = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_phase1/slim_sum/mChipm100GeV_dm2p259GeV_1.root",
              ]
    object_retag_labels = {
         "s" : {
            "base" : "\Delta_{}M^{\pm} 2.26 Gev",
            "prefireWeight" : "prefireWeight"
            },
    }  
    
class signal_phase1_l1_prefire_dm0p559GeV(signal_phase1_l1_prefire_dm1p759GeV):
    histrograms_file = BaseParams.histograms_root_files_dir + "/signal_phase1_l1_prefire_dm0p559GeV.root"
    signal_dir = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_phase1/slim_sum/mChipm100GeV_dm0p559GeV_1.root",
              ]
    object_retag_labels = {
         "s" : {
            "base" : "\Delta_{}M^{\pm} 0.55 Gev",
            "prefireWeight" : "prefireWeight"
            },
    }

class signal_phase1_l1_prefire_pool(signal_phase1_l1_prefire_dm1p759GeV):
    histrograms_file = BaseParams.histograms_root_files_dir + "/signal_phase1_l1_prefire_pool.root"
    signal_dir = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_phase1/sum/mChipm*GeV_dm[012]p*GeV*.root",
              ]
    glob_signal = True
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    object_retag_labels = {
         "s" : {
            "base" : "base",
            "prefireWeight" : "prefireWeight"
            },
    }   

########### HEM FAILURE ##################


class signal_phase1_hem_failure_dm1p759GeV(signal_phase1_l1_prefire_dm1p759GeV):
    histrograms_file = BaseParams.histograms_root_files_dir + "/signal_phase1_l1_prefire_dm1p759GeV.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = True
    
    signal_dir = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_phase1/sum/mChipm100GeV_dm1p759GeV_1.root",
              ]
    
    histograms_defs = [     
        { "obs" : "electrons_fine_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "bins" : 40, "units" : "BDT", "legendCol" : 1, "legendCoor" : {"x1" : .15, "y1" : .70, "x2" : .65, "y2" : .79}, "object" : "e"},
        { "obs" : "electrons_signal_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : 0, "maxX" : 1, "bins" : 40, "units" : "BDT", "legendCol" : 1, "legendCoor" : {"x1" : .15, "y1" : .70, "x2" : .65, "y2" : .79}, "object" : "e"},
        
        { "obs" : "muons_fine_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "bins" : 40, "units" : "BDT", "legendCol" : 1, "legendCoor" : {"x1" : .15, "y1" : .70, "x2" : .65, "y2" : .79}, "object" : "m"},
        { "obs" : "muons_signal_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : 0, "maxX" : 1, "bins" : 40, "units" : "BDT", "legendCol" : 1, "legendCoor" : {"x1" : .15, "y1" : .70, "x2" : .65, "y2" : .79}, "object" : "m"},
        
        { "obs" : "jets_fine_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "bins" : 40, "units" : "BDT", "legendCol" : 1, "legendCoor" : {"x1" : .15, "y1" : .70, "x2" : .65, "y2" : .79}, "object" : "j"},
        { "obs" : "jets_signal_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : 0, "maxX" : 1, "bins" : 40, "units" : "BDT", "legendCol" : 1, "legendCoor" : {"x1" : .15, "y1" : .70, "x2" : .65, "y2" : .79}, "object" : "j"},
        
        { "obs" : "tracks_fine_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "bins" : 40, "units" : "BDT", "legendCol" : 1, "legendCoor" : {"x1" : .15, "y1" : .70, "x2" : .65, "y2" : .79}, "object" : "t"},
        { "obs" : "tracks_signal_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : 0, "maxX" : 1, "bins" : 40, "units" : "BDT", "legendCol" : 1, "legendCoor" : {"x1" : .15, "y1" : .70, "x2" : .65, "y2" : .79}, "object" : "t"},
        
        { "obs" : "ejets_fine_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "bins" : 40, "units" : "BDT", "legendCol" : 1, "legendCoor" : {"x1" : .15, "y1" : .70, "x2" : .65, "y2" : .79}, "object" : "ej"},
        { "obs" : "ejets_signal_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : 0, "maxX" : 1, "bins" : 40, "units" : "BDT", "legendCol" : 1, "legendCoor" : {"x1" : .15, "y1" : .70, "x2" : .65, "y2" : .79}, "object" : "ej"},
        
    ]
    jetIso = "CorrJetNoMultIso10Dr0.6"
    injectJetIsoToHistograms(histograms_defs, jetIso)

    object_retag_weights = {}
    
    object_retag_map = {
        "e" : [ 
                {"base" : "1"},
                {"hem" : "hemFailureVetoElectrons == 1"},
            ],
        "j" : [ 
                {"base" : "1"},
                {"hem" : "hemFailureVetoJets == 1"},
            ],
        "m" : [ 
                {"base" : "1"},
                {"hem" : "hemFailureVetoMuons == 1"},
            ],
        "t" : [ 
                {"base" : "1"},
                {"hem" : "hemFailureVetoTracks == 1"},
            ],
        "ej" : [ 
                {"base" : "1"},
                {"hem" : "hemFailureVetoElectrons == 1 && hemFailureVetoJets == 1"},
            ],
    }
    
    
    object_retag_labels = {

         "e" : {
                "base" : "\Delta_{}M^{\pm} 1.75 Gev",
                "hem" : "hemFailureVetoElectrons",
            },
        "j" : { 
                "base" : "\Delta_{}M^{\pm} 1.75 Gev",
                "hem" : "hemFailureVetoJets",
            },
        "m" : { 
                "base" : "\Delta_{}M^{\pm} 1.75 Gev",
                "hem" : "hemFailureVetoMuons",
            },
        "t" : { 
                "base" : "\Delta_{}M^{\pm} 1.75 Gev",
                "hem" : "hemFailureVetoTracks",
            },
        "ej" : {
                "base" : "\Delta_{}M^{\pm} 1.75 Gev",
                "hem" : "hemFailureVetoElectrons and Jets",
            },
        
    } 
    
    customRatios = [  [["hem"],["base"]] ]  
    customRatiosNames = [  ["hem-veto","base"]  ]

class signal_phase1_hem_failure_dm2p259GeV(signal_phase1_hem_failure_dm1p759GeV):
    histrograms_file = BaseParams.histograms_root_files_dir + "/signal_phase1_l1_prefire_dm2p259GeV.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    
    signal_dir = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_phase1/sum/mChipm100GeV_dm2p259GeV_1.root",
              ]
              
    object_retag_labels = {

         "e" : {
                "base" : "\Delta_{}M^{\pm} 2.25 Gev",
                "hem" : "hemFailureVetoElectrons",
            },
        "j" : { 
                "base" : "\Delta_{}M^{\pm} 2.25 Gev",
                "hem" : "hemFailureVetoJets",
            },
        "m" : { 
                "base" : "\Delta_{}M^{\pm} 2.25 Gev",
                "hem" : "hemFailureVetoMuons",
            },
        "t" : { 
                "base" : "\Delta_{}M^{\pm} 2.25 Gev",
                "hem" : "hemFailureVetoTracks",
            },
        "ej" : {
                "base" : "\Delta_{}M^{\pm} 2.25 Gev",
                "hem" : "hemFailureVetoElectrons and Jets",
            },
        
    }

class signal_phase1_hem_failure_dm0p559GeV(signal_phase1_hem_failure_dm1p759GeV):
    histrograms_file = BaseParams.histograms_root_files_dir + "/signal_phase1_l1_prefire_dm0p559GeV.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    
    signal_dir = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_phase1/sum/mChipm100GeV_dm0p559GeV_1.root",
              ]
              
    object_retag_labels = {

         "e" : {
                "base" : "\Delta_{}M^{\pm} 0.55 Gev",
                "hem" : "hemFailureVetoElectrons",
            },
        "j" : { 
                "base" : "\Delta_{}M^{\pm} 0.55 Gev",
                "hem" : "hemFailureVetoJets",
            },
        "m" : { 
                "base" : "\Delta_{}M^{\pm} 0.55 Gev",
                "hem" : "hemFailureVetoMuons",
            },
        "t" : { 
                "base" : "\Delta_{}M^{\pm} 0.55 Gev",
                "hem" : "hemFailureVetoTracks",
            },
        "ej" : {
                "base" : "\Delta_{}M^{\pm} 0.55 Gev",
                "hem" : "hemFailureVetoElectrons and Jets",
            },
        
    } 

class signal_phase1_hem_failure_pool(signal_phase1_hem_failure_dm1p759GeV):
    histrograms_file = BaseParams.histograms_root_files_dir + "/signal_phase1_hem_failure_pool.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    
    signal_dir = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_phase1/sum/mChipm*GeV_dm[012]p*GeV*.root",
              ]
    
    glob_signal = True
              
    object_retag_labels = {

         "e" : {
                "base" : "base",
                "hem" : "hemFailureVetoElectrons",
            },
        "j" : { 
                "base" : "base",
                "hem" : "hemFailureVetoJets",
            },
        "m" : { 
                "base" : "base",
                "hem" : "hemFailureVetoMuons",
            },
        "t" : { 
                "base" : "base",
                "hem" : "hemFailureVetoTracks",
            },
        "ej" : {
                "base" : "base",
                "hem" : "hemFailureVetoElectrons and Jets",
            },
        
    }