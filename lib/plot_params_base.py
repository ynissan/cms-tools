import sys
import os

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib"))

import crystal_ball_params
import utils
import plotutils

low_3_signals = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt_all/single/higgsino_mu100_dm1p92Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt_all/single/higgsino_mu100_dm3p28Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt_all/single/higgsino_mu100_dm4p30Chi20Chipm.root",
              #"/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1/signal/skim_dilepton_signal_bdt_all/single/higgsino_mu100_dm9p73Chi20Chipm.root"
              ]

calculatedLumi = {
        'MET' : 35.350177774,
        'SingleMuon' : 22.143021976
}

signals = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/slim/higgsino_mu100_dm1p13Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/slim/higgsino_mu100_dm1p47Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/slim/higgsino_mu100_dm1p92Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/slim/higgsino_mu100_dm3p28Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/slim/higgsino_mu100_dm4p30Chi20Chipm.root"
              ]

signalNames = [
    "\Delta_{}M 1.13 Gev",
    "\Delta_{}M 1.47 Gev",
    "\Delta_{}M 1.9 Gev",
    "\Delta_{}M 3.2 Gev",
    "\Delta_{}M 4.3 Gev",
]

def injectJetIsoToCuts(cuts, jetIso):
    for cut in cuts:
        if cut.get("condition") is not None:
            cut["condition"] = cut["condition"].replace("%%%", jetIso)
        if cut.get("baseline") is not None:
            cut["baseline"] = cut["baseline"].replace("%%%", jetIso)
        if cut.get("sc") is not None:
            cut["sc"] = cut["sc"].replace("%%%", jetIso)
        
def injectJetIsoToHistograms(hists, jetIso):
    for hist in hists:
        hist["obs"] = hist["obs"].replace("%%%", jetIso)
        if hist.get("formula") is not None:
            hist["formula"] = hist["formula"].replace("%%%", jetIso)
        if hist.get("usedObs") is not None:
            for i in range(len(hist["usedObs"])):
                hist["usedObs"][i] = hist["usedObs"][i].replace("%%%", jetIso)
        if hist.get("sc_obs") is not None:
            hist["sc_obs"] = hist["sc_obs"].replace("%%%", jetIso)
        if hist.get("condition") is not None:
            hist["condition"] = hist["condition"].replace("%%%", jetIso)

def injectJetIsoToList(obsList, jetIso):
    for i in range(len(obsList)):
        obsList[i] = obsList[i].replace("%%%", jetIso)

def injectJetIsoToMapValues(obsMap, jetIso):
    for k in obsMap:
        obsMap[k] = obsMap[k].replace("%%%", jetIso)

# histogram params:
# 
# object - for the purpose of retagging
# condition - adds a specific condition to the histogram
# baseline - adds a specific condition to the histogram (for not sc)
# sc - adds a specific condition to the histogram for sc
# obs - either the name of the histogram of the formula
# sc_obs - that's the obs for same-charge CR
# formula - in case we want to override the obs with a specific formula (for naming two histograms differently)
# sc_formula - formula for same-charge CR
# bins - bins num
# customBins - replaces the bins, minX, minY with custom binning array of low edges (plus one higher one)
# minX, maxX - for x axis
# minY, maxY, binsY - for y axis
# 2D - boolean for 2D
# plotStr - replaces the "hist" string when drawing the histogram
# units - x axis title
# legendCoor - legend coordinates
# legendCol - legend columns number
# labelText - work in progress or other text next to CMS
# cmsLocation - where to put the CMS label
# showLumi - bool
# linearYspace - how much space to leave for legend
# linear_log_space - how much space to leave for legend in log scale... this name makes no sense
# blind - blind a specific interval
# usedObs - used to tell which observables were in order to turn them on in the tree
# ratio1max - max value for ratio1
# ratio1min - min value for ratio2

class BaseParams:
    signal_dir = signals
    #signal_files = signals
    signal_names = signalNames
    bg_dir = None
    data_dir = None
    sc_bg_dir = None
    sc_data_dir = None
    
    # This is in fb-1
    calculatedLumi = {}
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        #'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight * BranchingRatio",
        'SingleMuon' : "1"
    }
    applyWeightsToData = False
    bgReTagging = {}
    bgReTaggingOrder = {}
    bgReTaggingNames = utils.bgReTaggingNames
    # turn on when some of the BG are coming from data
    bgReTaggingUseSources = False
    # sources should have keys taken from the retagging, and each value is a list with the sources which are either "bg" or "data"
    bgReTaggingSources = {}
    # for normalisation and transfer factors
    bgReTaggingFactors = {}
    
    plot_kind = "MET"
    plot_bg = True
    plot_data = False
    plot_data_for_bg_estimation = False
    plot_signal = True
    plot_rand = False
    plot_fast = True
    plot_title = True
    plot_overflow = True
    plot_significance = False
    plot_error = False
    plot_sc = False
    plot_ratio = False
    plot_reverse_ratio = False
    plot_point = False
    plot_efficiency = False
    plot_grid_x = False
    plot_grid_y = False
    plot_custom_ratio = False
    
    create_canvas = False
    
    glob_signal = False
    
    #customRatios = [  [["DiBoson"],["TTJets"]],  [["WJetsToLNu"],["ZJetsToNuNu"]]  ]
    customRatios = [  [["tc_btag_veto"],["tc_2_btags"]]  ]
    choose_bg_files = False
    choose_bg_files_list = ["TTJets"]
    # plot only specific subset of BG categories
    choose_bg_categories = False
    choose_bg_categories_list = []
    #choose_bg_files_list = ["WJetsToLNu"]
    choose_bg_files_for_sc = False
    ignore_bg_files = ["TT_TuneCUETP8M2T4_13TeV-powheg-pythia8.root", "TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root"]
    #ignore_bg_files = []
    blind_data = True
    plot_log_x = False
    plot_real_log_x = False
    nostack = False
    solid_bg = False
    logXplots = ["invMass"]
    histograms_defs = []
    cuts = []
    efficiencies = []
    normalise = False
    normalise_each_bg = False
    normalise_integral_positive_only = False
    no_weights = False
    
    fit_inv_mass_jpsi = False
    fit_inv_mass_obs_jpsi = ""
    fit_inv_mass_cut_jpsi = "none"
    fit_inv_mass_jpsi_func = "gauss"
    fit_inv_mass_jpsi_func_bg = False
    fit_inv_mass_jpsi_bg_func = "linear"
    
    fit_linear_ratio_plot = False
    
    save_histrograms_to_file = False
    load_histrograms_from_file = False
    histrograms_file = ""
    
    bg_retag = False
    
    object_retag = False
    object_retag_map = {}
    
    sig_line_width = 2

    legend_coordinates = {"x1" : .35, "y1" : .60, "x2" : .89, "y2" : .89}
    legend_columns = 2
    legend_border = 0
    
    y_title_offset = 1
    y_title = "Events"
    
    label_text = plotutils.StampStr.SIMWIP
    cms_location = plotutils.StampCoor.ABOVE_PLOT
    show_lumi = True
    
    use_calculated_lumi_weight = True
    
    subtract_same_charge = False
    
    sc_label = "same-sign"
    sc_ratio_label = "sc"
    sc_color = 6
    
    plot_custom_types = []
    # used for cleaned-z and cleaned-w. They have different files and conditions attached to them.
    custom_types_dir = []
    custom_types_label = []
    custom_types_conditions = []
    custom_types_common_files = False
    
    cms_tools_base_dir = os.path.expandvars("$CMSSW_BASE/src/stops")
    histograms_root_files_dir = cms_tools_base_dir + "/analysis/scripts/histograms_root_files"
    
    #used to turn on only wanted branches in the tree
    turnOnOnlyUsedObsInTree = False
    usedObs = []
    
    transfer_factor = -1
    transfer_factor_error = -1
    
    colorPalette = plotutils.defaultColorPalette
    