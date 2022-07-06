import sys
import os
from ROOT import *

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))

from plot_params_base import *
import plotutils

bgReTaggingFull = {
    "tc" : "tc * (!tautau)",
    "tautau" : "tautau",
    "other" : "other * (!tautau) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)",
    "omega" : "omega",
    "rho" : "rho_0",
    "eta" : "eta",
    "phi" : "phi",
    "etaprime" : "eta_prime",
    "jpsi" : "j_psi",
    "upsilon1" : "upsilon_1",
    "upsilon2" : "upsilon_2",
    "nbody" : "n_body * (!tautau)",
    "scother" : "sc * (!tautau) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)",
    "fake" : "(rf || ff)",
}

bgReTaggingCollected = {
    "tc" : "tc * (!tautau)",
    "tautau" : "tautau",
    "other" : "other * (!tautau) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)",
    "resonances" : "(sc || omega || rho_0 || eta || phi || eta_prime || j_psi || upsilon_1 || upsilon_2)",
    "nbody" : "n_body * (!tautau)",
    "fake" : "(rf || ff)",
}

bgReTaggingCollectedNoTauTau = {
    "tc" : "tc * (!tautau)",
    "other" : "other * (!tautau) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)",
    "resonances" : "(sc || omega || rho_0 || eta || phi || eta_prime || j_psi || upsilon_1 || upsilon_2)",
    "nbody" : "n_body * (!tautau)",
    "fake" : "(rf || ff)",
}


bgReTaggingResonances = {
    #"tc" : "tc * (!tautau)",
    #"tautau" : "tautau",
    #"other" : "other * (!tautau) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)",
    "omega" : "omega",
    "rho" : "rho_0",
    "eta" : "eta",
    "phi" : "phi",
    "etaprime" : "eta_prime",
    "jpsi" : "j_psi",
    "upsilon1" : "upsilon_1",
    "upsilon2" : "upsilon_2",
    "nbody" : "n_body * (!tautau)",
    "scother" : "sc * (!tautau) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)",
    #"fake" : "(rf || ff)",
}

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
    "fake" : 11
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
    "fake" : "fake"
}

# invMass veto
# invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81)

# FULL ZOO

class full_zoo(BaseParams):
    
    weightString = {
        'MET' : "Weight",
    }
    
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
    plot_signal = False
    
    plot_log_x = True
    plot_real_log_x = True
    plot_overflow = False
    
    # calculatedLumi = {
#         'MET' : 135.778598358,
#     }
    
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        {"name":"bdt", "title": "BDT>0.1", "condition" : "(dilepBDT > 0.1 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]
    
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0.1, "maxX" : 12, "bins" : 100, "blind" : [4,None] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1] },
    ]
    
    bg_retag = True
    
    bgReTagging = bgReTaggingFull
    bgReTaggingOrder = bgReTaggingOrderFull
    bgReTaggingNames = bgReTaggingNamesFull
    plot_error = True

class sm_zoo(full_zoo):
    bg_retag = False

class zoo_all_even_bins(full_zoo):
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]

class test_class(full_zoo):
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0.1, "maxX" : 2, "bins" : 100, "blind" : [4,None] },
    ]
    bgReTagging = bgReTaggingResonances

class zoo(full_zoo):
    bgReTagging = bgReTaggingResonances

class zoo_all_electrons(full_zoo):
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Electrons\" && invMass < 12 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]

class zoo_electrons(zoo_all_electrons):
    bgReTagging = bgReTaggingResonances
    
class zoo_all_low_met(full_zoo):
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && BTagsDeepMedium == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]
class zoo_all_low_met_all(full_zoo):
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && invMass < 12  && BTagsDeepMedium == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]


# zoo removal
#invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81)

class dilepton_muons_bg(BaseParams):
    signal_dir = signals
    signal_names = signalNames
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim/sum/"
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        {"name":"no-tautau", "title": "No tautau", "condition" : "(!tautau && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        {"name":"bdt", "title": "BDT>0.1", "condition" : "(dilepBDT > 0.1 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        {"name":"bdt-no-tautau", "title": "BDT>0.1 && No tautau", "condition" : "(!tautau && dilepBDT > 0.1 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]
    
    #(twoLeptons == 1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && BTagsDeepMedium == 0 && vetoElectronsPassIsoTightID == 0 && vetoMuonsPassIsoPassIso == 0 && @leptons.size() == 2 && leptonFlavour == \"" + lep + "\" && sameSign == 0)", True)
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]},# "customBins"  : [0,2,3.0,3.2,4,6,10,12] },#, "scale" : "width"
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
    ]
    
    weightString = {
        'MET' : "Weight"# * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
    }
    
    #calculatedLumi = {
    #    'MET' : 35.778598358,
    #}
    
    plot_sc = True
    plot_data = False
    plot_overflow = False
    plot_ratio = True
    plot_signal = False
    
    blind_data = True
    
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg.root"

class dilepton_muons_bg_scale(dilepton_muons_bg):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_scale.root"
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None], "customBins"  : [0,2,3.0,3.2,4,6,10,12], "scale" : "width"},
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1], "customBins"  : [-1,-0.4,0,0.1,0.2,1], "scale" : "width" },
    ]
    y_title = "Events / GeV"

class dilepton_muons_bg_coarse(dilepton_muons_bg):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_fine.root"
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]},# "customBins"  : [0,2,3.05,3.15,4,6,10,12] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
    ]

class dilepton_muons_bg_coarse_retag(dilepton_muons_bg_coarse):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_coarse_retag.root"
    bg_retag = True
    
    bgReTagging = bgReTaggingFull
    bgReTaggingOrder = bgReTaggingOrderFull
    bgReTaggingNames = bgReTaggingNamesFull

class track_muon_sc_comparison(BaseParams):
    histrograms_file = BaseParams.histograms_root_files_dir + "/track_muon_sc_comparison.root"
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
    save_histrograms_to_file = True
    load_histrograms_from_file = True 
    
    cuts = [
        {"name":"none", "title": "None", "condition" : "(MinDeltaPhiMetJets > 0.4 && MHT >= 220 &&  MET >= 140 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "exclusiveTrack%%% == 1 && trackBDT%%% > 0 && exTrack_invMass%%% < 12 && exclusiveTrackLeptonFlavour%%% == \"Muons\"", "sc" : "sc_exclusiveTrack%%% == 1 && sc_trackBDT%%% > 0 && sc_exTrack_invMass%%% < 12 && sc_exclusiveTrackLeptonFlavour%%% == \"Muons\"" },
        #{"name":"sr", "title": "sr", "condition" : "(MHT >= 220 &&  MET >= 200 && BTagsDeepMedium == 0 )", "baseline" : "exclusiveTrack == 1 && trackBDT > 0 && exTrack_invMass < 30 && exclusiveTrackLeptonFlavour == \"Muons\" && exTrack_dilepBDT > 0.1", "sc" : "sc_exclusiveTrack == 1 && sc_trackBDT > 0 && sc_exTrack_invMass < 30 && sc_exclusiveTrackLeptonFlavour == \"Muons\"" }
    ]
    injectJetIsoToCuts(cuts, "CorrJetIso10Dr0.6")
    
    histograms_defs = [
        { "obs" : "exTrack_dilepBDT%%%", "units" : "BDT", "minX" : -1, "maxX" : 1, "bins" : 30, "blind" : [None,0.1], "sc_obs" : "sc_exTrack_dilepBDT%%%", "linearYspace" : 1.5},
    ]
    
    injectJetIsoToHistograms(histograms_defs, "CorrJetIso10Dr0.6")  
    
    weightString = {
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight * BranchingRatio",
    }
    
    plot_data = False
    plot_sc = True
    plot_ratio = True
    plot_signal = False
    sc_color = kOrange + 1
    label_text = plotutils.StampStr.SIMWIP

# We don't really need to scan this category - because we use the 2 Muons category to decide this one out.
class track_muon_sc_comparison_scan_muons(BaseParams):
    histrograms_file = BaseParams.histograms_root_files_dir + "/track_muon_sc_comparison_scan_muons.root"
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
    save_histrograms_to_file = True
    load_histrograms_from_file = True 
    
    # cuts = [
#         {"name":"none", "title": "None", "condition" : "(MinDeltaPhiMetJets > 0.4 && MHT >= 220 &&  MET >= 140 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "exclusiveTrack%%% == 1 && trackBDT%%% > 0 && exTrack_invMass%%% < 12 && exclusiveTrackLeptonFlavour%%% == \"Muons\"", "sc" : "sc_exclusiveTrack%%% == 1 && sc_trackBDT%%% > 0 && sc_exTrack_invMass%%% < 12 && sc_exclusiveTrackLeptonFlavour%%% == \"Muons\"" },
#         #{"name":"sr", "title": "sr", "condition" : "(MHT >= 220 &&  MET >= 200 && BTagsDeepMedium == 0 )", "baseline" : "exclusiveTrack == 1 && trackBDT > 0 && exTrack_invMass < 30 && exclusiveTrackLeptonFlavour == \"Muons\" && exTrack_dilepBDT > 0.1", "sc" : "sc_exclusiveTrack == 1 && sc_trackBDT > 0 && sc_exTrack_invMass < 30 && sc_exclusiveTrackLeptonFlavour == \"Muons\"" }
#     ]
#     injectJetIsoToCuts(cuts, "CorrJetIso10.5Dr0.55")
#     
#     histograms_defs = [
#         { "obs" : "exTrack_dilepBDT%%%", "units" : "BDT", "minX" : -1, "maxX" : 1, "bins" : 30, "blind" : [None,0.1], "sc_obs" : "sc_exTrack_dilepBDT%%%", "linearYspace" : 1.5},
#     ]
#     
#     injectJetIsoToHistograms(histograms_defs, "CorrJetIso10.5Dr0.55")  
    
    weightString = {
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * BranchingRatio",
    }
    
    plot_data = False
    plot_sc = True
    plot_ratio = True
    plot_signal = False
    sc_color = kOrange + 1
    label_text = plotutils.StampStr.SIMWIP
    
    
    cuts = [
        {"name":"none", "title": "None", "condition" : "1", "baseline" : "1", "sc" : "1"},
        #{"name":"bdt", "title": "BDT > 0.35", "condition" : "(dilepBDT%%% > 0.35 &&  MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 200 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && !tautau%%%)", "baseline" : "isoCr%%% == 0", "sc" : "isoCr%%% >= 1"},
    ]
    histograms_defs = [
    
    ]
    
    for iso in utils.leptonIsolationList:
        for cat in utils.leptonIsolationCategories:
            ptRanges = [""]
            drCuts = [""]
            #if iso == "CorrJetIso":
            if iso == "CorrJetNoMultIso":
                ptRanges = utils.leptonCorrJetIsoPtRange
                drCuts = utils.leptonCorrJetIsoDrCuts
            else:
                continue
            for ptRange in ptRanges:
                for drCut in drCuts:
                    jetIso = ""
                    if len(str(ptRange)) > 0:
                        jetIso = iso + str(ptRange) + "Dr" + str(drCut) + cat
                    else:
                        continue
                    #for obs in ["invMass", "dilepBDT"]:
                    for obs in ["dilepBDT", "dilepBDT_fine", "dilepBDT_custom"]:
                    #for obs in ["dilepBDT_fine"]:
                        #{ "obs" : "invMassCorrJetIso15Dr0.4", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]}
                        hist_def = { "obs" : obs + "%%%", "formula" : "exTrack_dilepBDT%%%" if "dilepBDT" in obs else (obs + "%%%"), "sc_obs" : "sc_exTrack_dilepBDT%%%", "linearYspace" : 1.5, "minX" : 0 if obs == "invMass" else -1, "maxX" : 13 if obs == "invMass" else 1, "bins" : 40 if obs == "dilepBDT_fine" else 20, "blind" : [None, 0], "customBins"  : [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,1] if obs == "dilepBDT_custom" else None,  "condition" : "(MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && MHT >= 220 &&  MET >= 140 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "exclusiveTrack%%% == 1 && trackBDT%%% > 0 && exTrack_invMass%%% < 12 && exclusiveTrackLeptonFlavour%%% == \"Muons\"", "sc" : "sc_exclusiveTrack%%% == 1 && sc_trackBDT%%% > 0 && sc_exTrack_invMass%%% < 12 && sc_exclusiveTrackLeptonFlavour%%% == \"Muons\""}
                        #print(hist_def["obs"],jetIso)
                        #print(hist_def["obs"].replace("%%%", jetIso))
                        #print(hist_def["obs"])
                        hist_def["obs"] = hist_def["obs"].replace("%%%", jetIso)
                        hist_def["formula"] = hist_def["formula"].replace("%%%", jetIso)
                        #print(hist_def["obs"])
                        #exit(0)
                        hist_def["condition"] = hist_def["condition"].replace("%%%", jetIso)
                        hist_def["baseline"] = hist_def["baseline"].replace("%%%", jetIso)
                        hist_def["sc"] = hist_def["sc"].replace("%%%", jetIso)
                        histograms_defs.append(hist_def)


class dimuon_background_estimation_non_isolated_and_tautau(BaseParams):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dimuon_background_estimation_non_isolated_and_tautau.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim/slim_sum/"
    
    plot_error = True
    plot_data = False
    plot_data_for_bg_estimation = True
    
    plot_signal = True
    blind_data = False
    bg_retag = True
    
    jetIsoStr = ""
    
    jetIso = "CorrJetIso10.5Dr0.55"
    
    cuts = [
        {"name":"none", "title": "None", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0)"},
        {"name":"orth", "title": "orth", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && sameSign%%% == 0 && (leptons%%%[1].Pt() <= 3.5 || deltaR%%% <= 0.3))"},
    ]
    injectJetIsoToCuts(cuts, jetIso)

    histograms_defs = [     
        { "obs" : "dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "units" : "BDT", "customBins"  : [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,1], "legendCol" : 1, "legendCoor" : {"x1" : .72, "y1" : .60, "x2" : .99, "y2" : .89}},
        { "obs" : "fine_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "bins" : 40, "units" : "BDT", "legendCol" : 1, "legendCoor" : {"x1" : .72, "y1" : .60, "x2" : .99, "y2" : .89}}
    ]
    injectJetIsoToHistograms(histograms_defs, jetIso)
    
    weightString = {
        #'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight * BranchingRatio",
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * BranchingRatio",
    }
    
    calculatedLumi = {
        'MET' : 35.712736198,
    }
    
    bgReTagging = {
        "tautau" : "tautau%%% && isoCr%%% == 0",
        "non-iso" : "isoCr%%% >= 1"
    }
    
    injectJetIsoToMapValues(bgReTagging, jetIso)
    
    bgReTaggingUseSources = True
    
    bgReTaggingOrder = {
        "tautau" : 1,
        "non-iso" : 2
    }
    bgReTaggingNames = {
        "tautau" : "#tau#tau",
        "non-iso" : "non-isolated"
    }
    bgReTaggingSources = {
        "tautau" : "bg",
        "non-iso" : "data"
    }
    
    bgReTaggingFactors = {
        "tautau" : [0.792, 0.631],
        "non-iso" : [0.876, 0.0868]
    }
    
    colorPalette = [
        { "name" : "yellow", "fillColor" : TColor.GetColor("#ffd700"), "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 5,  "markerStyle" : kOpenCircle},
        { "name" : "blue", "fillColor" : TColor.GetColor("#0057b7"), "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    ]
    