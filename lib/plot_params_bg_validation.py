import sys
import os
import copy
import ROOT

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))

from plot_params_base import *

#######################################################################################################
############ SAME SIGN VALIDATION FOR CorrJetNoMultIso10_06 WITH/OUT LINE FITS AND WEIGHTS ############
#######################################################################################################

# here was dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass
class dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign(BaseParams):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_no_retag_CorrJetIso10_06_invmass_same_sign.root"
    
    cuts = [
        #"passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMhtJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && dilepBDT" + jetiso + " < 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && tautau" + jetiso + " == 0)"
        {"name":"none", "title": "None", "condition" : "(passedMhtMet6pack == 1 && passesUniversalSelection == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 1 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
        #{"name":"loose", "title": "loose", "condition" : "(MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
        #{"name":"mtautau", "title": "mtautau > 200", "condition" : "(mtautau%%% > 200 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
        #{"name":"nmtautau", "title": "nmtautau < 0 or nmtautau > 160", "condition" : "((nmtautau%%% < 0 || nmtautau%%% > 160) && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
        #{"name":"nmtautau_inside", "title": "0 < nmtautau < 160 && BDT < 0", "condition" : "((nmtautau%%% < 160 && nmtautau%%% > 0) && dilepBDT%%% < 0 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
    ]
    injectJetIsoToCuts(cuts, "CorrJetNoMultIso10Dr0.6")
    fit_linear_ratio_plot = False

class dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf(dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign):
    normalise = False
    
    transfer_factor = 0.539
    transfer_factor_error = 0.055
    transfer_factor_error = 0.0
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    calculatedLumi = {
        'MET' : 35.7389543,
    }
    fit_linear_ratio_plot = True

class dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights(dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights.root"
    weightString = {
        #'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight * BranchingRatio",
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * BranchingRatio * muonsClosureLineFitWeightCorrJetNoMultIso10Dr0.6",
    }

class dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sf_recalcualted(dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights):
    transfer_factor = 0.506

class dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_m(dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_m.root"
    weightString = {
        #'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight * BranchingRatio",
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * BranchingRatio * muonsClosureLineFitSigmaMWeightCorrJetNoMultIso10Dr0.6",
    }
    save_histrograms_to_file = True
    load_histrograms_from_file = True

class dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_m_sf_recalculated(dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_m):
    transfer_factor = 0.534

class dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_b(dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_b.root"
    weightString = {
        #'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight * BranchingRatio",
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * BranchingRatio * muonsClosureLineFitSigmaBWeightCorrJetNoMultIso10Dr0.6",
    }
    save_histrograms_to_file = True
    load_histrograms_from_file = True

class dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_b_sf_recalculated(dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_b):
    transfer_factor = 0.465

class dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sf_errors(dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights):
    transfer_factor_error = 0.055

class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign(dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign.root"
    plot_bg = False
    plot_data = True
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim/slim_sum"
    calculatedLumi = {
        'MET' : 35.7389543,
    }
    fit_linear_ratio_plot = False
    
class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf(dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign):
    normalise = False
    #0.602
    transfer_factor = 0.65
    transfer_factor_error = 0.102
    transfer_factor_error = 0.0
    fit_linear_ratio_plot = True
    load_histrograms_from_file = False

class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights(dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights.root"
    weightString = {
        #'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight * BranchingRatio",
        'MET' : "muonsClosureLineFitWeightCorrJetNoMultIso10Dr0.6",
    }
    applyWeightsToData = True
    save_histrograms_to_file = True
    load_histrograms_from_file = False

class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sf_recalculated(dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights):
    transfer_factor = 0.610

class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_m(dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_m.root"
    weightString = {
        #'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight * BranchingRatio",
        'MET' : "muonsClosureLineFitSigmaMWeightCorrJetNoMultIso10Dr0.6",
    }
    save_histrograms_to_file = True
    load_histrograms_from_file = True

class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_m_sf_recalculated(dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_m):
    transfer_factor = 0.645

class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_b(dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_b.root"
    weightString = {
        #'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight * BranchingRatio",
        'MET' : "muonsClosureLineFitSigmaBWeightCorrJetNoMultIso10Dr0.6",
    }
    save_histrograms_to_file = True
    load_histrograms_from_file = True

class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_b_sf_recalculated(dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sigma_b):
    transfer_factor = 0.562

class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights_sf_errors(dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf_line_weights):
    transfer_factor_error = 0.102
    



###########################################################################################################
############ SAME SIGN VALIDATION FOR CorrJetNoMultIso10_06 WITH/OUT LINE FITS AND WEIGHTS PHASE1 ############
###########################################################################################################


# It used to inherit from dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass
class dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_phase1(BaseParams):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_no_retag_CorrJetIso10_06_invmass_same_sign_phase1.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    cuts = [
        #"passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMhtJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && dilepBDT" + jetiso + " < 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && tautau" + jetiso + " == 0)"
        {"name":"none", "title": "None", "condition" : "(passedMhtMet6pack == 1 && passesUniversalSelection == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 1 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
        #{"name":"loose", "title": "loose", "condition" : "(MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
        #{"name":"mtautau", "title": "mtautau > 200", "condition" : "(mtautau%%% > 200 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
        #{"name":"nmtautau", "title": "nmtautau < 0 or nmtautau > 160", "condition" : "((nmtautau%%% < 0 || nmtautau%%% > 160) && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
        #{"name":"nmtautau_inside", "title": "0 < nmtautau < 160 && BDT < 0", "condition" : "((nmtautau%%% < 160 && nmtautau%%% > 0) && dilepBDT%%% < 0 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
    ]
    injectJetIsoToCuts(cuts, "CorrJetNoMultIso10Dr0.6")
    fit_linear_ratio_plot = False
    
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_phase1/sum/slim_sum/type_sum"
    
    weightString = {
        #'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight * BranchingRatio",
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2017 * BranchingRatio",
    }
    
    histograms_defs = [
        
        { "obs" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "bins" : 20, "units" : "BDT"},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        { "obs" : "closure_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT", "customBins"  : [-1,0,0.1,0.30,0.4,0.45,1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        { "obs" : "closure_less_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT", "customBins"  : [-1,0,0.1,0.30,0.4,1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        #{ "obs" : "closure_new_bin_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT", "customBins"  : [-1,0,0.1,0.2,0.3,0.4,0.5,1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        #{ "obs" : "closure_newer_bin_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT", "customBins"  : [-1,0,0.1,0.2,0.3,0.4,0.45,0.5,0.55,1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        #{ "obs" : "closure_newest_bin_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT", "customBins"  : [-1,0,0.1,0.2,0.3,0.4,0.45,0.5,1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        
        { "obs" : "fine_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "bins" : 60, "units" : "BDT"},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        #{ "obs" : "coarse_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1], "units" : "BDT"},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        #{ "obs" : "sideband_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 0, "bins" : 1, "blind" : [None,0.1], "units" : "BDT"},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        #'0.10', '0.30', '0.40', '0.45'
       { "obs" : "custom_dilepBDT%%%", "formula" : "dilepBDT%%%","minX" : -1, "maxX" : 1, "bins" : 6, "units" : "BDT", "customBins"  : [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.30,0.4,0.45,1] }, 
       { "obs" : "custom_less_dilepBDT%%%", "formula" : "dilepBDT%%%","minX" : -1, "maxX" : 1, "bins" : 6, "units" : "BDT", "customBins"  : [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.30,0.4,1] }, 
        #{ "obs" : "mtautau%%%", "linearYspace" : 1.5, "minX" : -300, "maxX" : 300, "bins" : 15},
        #{ "obs" : "nmtautau%%%", "linearYspace" : 1.5, "minX" : -300, "maxX" : 300, "bins" : 15},
        #{ "obs" : "coarse_nmtautau%%%", "formula" : "nmtautau%%%", "linearYspace" : 1.5, "minX" : 0, "maxX" : 160, "bins" : 15},
        #{ "obs" : "invMass%%%", "formula" : "invMass%%%", "minX" : 0, "maxX" : 12, "bins" : 6},
        
    ]
    injectJetIsoToHistograms(histograms_defs, "CorrJetNoMultIso10Dr0.6")
    normalise = False
    stamp_scale_factor = True
    transfer_factor = 0.81
    transfer_factor_error = 0


class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2017(dilepton_muons_bg_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_phase1):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2017.root"
    plot_bg = False
    plot_data = True
    save_histrograms_to_file = True
    load_histrograms_from_file = True
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_phase1/slim_2017"
    glob_data = False
    transfer_factor = 0.438
    transfer_factor_error = 0
    #calculatedLumi = {
    #    'MET' : 35.7389543,
    #}
    fit_linear_ratio_plot = False

class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2017F(dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2017):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2017F.root"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_phase1/slim_2017F"
    transfer_factor = 0.381
    transfer_factor_error = 0

class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2017F_prefire(dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2017):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2017F_prefire.root"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_phase1/slim_2017F"
    transfer_factor = 0.396
    transfer_factor_error = 0
    weightString = {
        #'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight * BranchingRatio",
        'MET' : "prefireWeight",
    }
    applyWeightsToData = True

class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2018A(dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2017):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2018A.root"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_phase1/slim_2018A"
    transfer_factor = 0.462
    transfer_factor_error = 0

class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2018CD(dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2017):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2018CD.root"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_phase1/slim_2018CD"
    transfer_factor = 0.498
    transfer_factor_error = 0

class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2018CD_hem_veto(dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2017):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_2018CD_hem_veto.root"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_phase1/slim_2018CD"
    transfer_factor = 0.490
    transfer_factor_error = 0
    cuts = [
        #"passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons" + jetiso + " == 1 "  + (orth_cond if orth else "") +  " && MinDeltaPhiMhtJets > 0.4 && MET >= 140 && MHT >= 220 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign" + jetiso + " == 0 && isoCr" + jetiso + (" >= 1" if isoCr else " == 0") + " && dilepBDT" + jetiso + " < 0 && leptonFlavour" + jetiso + " == \"" + lep + "\" && tautau" + jetiso + " == 0)"
        {"name":"none", "title": "None", "condition" : "(passedMhtMet6pack == 1 && passesUniversalSelection == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 1 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
        {"name":"hem_ej", "title": "HEM e+j", "condition" : "(hemFailureVetoJets == 1 && hemFailureVetoElectrons == 1 && passedMhtMet6pack == 1 && passesUniversalSelection == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 1 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
        {"name":"hem_ejm", "title": "HEM e+j+m", "condition" : "(hemFailureVetoMuons == 1 && hemFailureVetoJets == 1 && hemFailureVetoElectrons == 1 && passedMhtMet6pack == 1 && passesUniversalSelection == 1 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 1 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
        
        #{"name":"loose", "title": "loose", "condition" : "(MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
        #{"name":"mtautau", "title": "mtautau > 200", "condition" : "(mtautau%%% > 200 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
        #{"name":"nmtautau", "title": "nmtautau < 0 or nmtautau > 160", "condition" : "((nmtautau%%% < 0 || nmtautau%%% > 160) && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
        #{"name":"nmtautau_inside", "title": "0 < nmtautau < 160 && BDT < 0", "condition" : "((nmtautau%%% < 160 && nmtautau%%% > 0) && dilepBDT%%% < 0 && MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
    ]
    injectJetIsoToCuts(cuts, "CorrJetNoMultIso10Dr0.6")
    


class dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign_no_norm_sf(dilepton_muons_data_isocr_no_retag_CorrJetNoMultIso10_06_invmass_same_sign):
    normalise = False
    #0.602
    transfer_factor = 0.65
    transfer_factor_error = 0.102
    transfer_factor_error = 0.0
    fit_linear_ratio_plot = True
    load_histrograms_from_file = False
