import sys
import os

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))

from plot_params_base import *

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
    #"tautau" : "tautau",
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
    "other" : "other",
    "omega" : "#omega",
    "rho" : "#rho",
    "eta" : "#eta",
    "phi" : "#phi",
    "etaprime" : "#eta^{}'",
    "jpsi" : "J/#psi",
    "upsilon1" : "#Upsilon(1s)",
    "upsilon2" : "#Upsilon(2s)",
    "tc" : "unrelated",
    "nbody" : "n-body",
    "scother" : "other (unknown)",
    "fake" : "fake"
}

class zoo_all(BaseParams):
    
    weightString = {
        'MET' : "1",
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
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12 && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]
    
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0.1, "maxX" : 12, "bins" : 100, "blind" : [4,None] },
    ]
    
    bg_retag = True
    
    bgReTagging = bgReTaggingFull
    bgReTaggingOrder = bgReTaggingOrderFull
    bgReTaggingNames = bgReTaggingNamesFull

class test_class(zoo_all):
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0.1, "maxX" : 2, "bins" : 100, "blind" : [4,None] },
    ]
    bgReTagging = bgReTaggingResonances

class zoo(zoo_all):
    bgReTagging = bgReTaggingResonances

class zoo_all_electrons(zoo_all):
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Electrons\" && invMass < 12 && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]

class zoo_electrons(zoo_all_electrons):
    bgReTagging = bgReTaggingResonances

# zoo removal
#invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81)

class dilepton_muons_bg(BaseParams):
    signal_dir = signals
    signal_names = signalNames
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim/sum/"
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]
    
    #(twoLeptons == 1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && BTagsDeepMedium == 0 && vetoElectronsTightID == 0 && vetoMuonsPassIso == 0 && @leptons.size() == 2 && leptonFlavour == \"" + lep + "\" && sameSign == 0)", True)
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 30, "blind" : [4,None], "customBins"  : [0,2,3.0,3.2,4,6,10,12] },#, "scale" : "width"
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30, "blind" : [None,0.1], "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
    ]
    
    
    weightString = {
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
    }
    
    calculatedLumi = {
        'MET' : 35.778598358,
    }
    
    plot_sc = True
    plot_data = False
    plot_overflow = False
    plot_ratio = True
    
    blind_data = True
    
    save_histrograms_to_file = True
    load_histrograms_from_file = True    
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg.root"

class dilepton_muons_bg_scale(dilepton_muons_bg):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_scale.root"
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 30, "blind" : [4,None], "customBins"  : [0,2,3.0,3.2,4,6,10,12], "scale" : "width"},
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30, "blind" : [None,0.1], "customBins"  : [-1,-0.4,0,0.1,0.2,1], "scale" : "width" },
    ]
    y_title = "Events / GeV"

class dilepton_muons_bg_fine(dilepton_muons_bg):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_fine.root"
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 30, "blind" : [4,None]},# "customBins"  : [0,2,3.05,3.15,4,6,10,12] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
    ]

class dilepton_muons_bg_basic_ratios(dilepton_muons_bg_scale):
    plot_sc = False
    save_histrograms_to_file = True
    load_histrograms_from_file = True    
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_basic_ratios.root"
    
    plot_custom_ratio = 2
    customRatios = [  [["WJetsToLNu"],["TTJets"]],  [["WJetsToLNu"],["ZJetsToNuNu"]]  ]


class dilepton_muons_bg_retag_ratios(dilepton_muons_bg):
    plot_sc = False
    save_histrograms_to_file = True
    load_histrograms_from_file = True    
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_retag_ratios.root"
    
    bg_retag = True
    
    bgReTagging = bgReTaggingCollected
    bgReTaggingOrder = bgReTaggingOrderFull
    bgReTaggingNames = bgReTaggingNamesFull
    
    plot_custom_ratio = 2
    customRatios = [  [["fake"],["tc"]],  [["fake"],["tautau"]]  ]
    
class dilepton_muons_bg_basic_ratios_subtract_same_charge(dilepton_muons_bg_basic_ratios):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_basic_ratios_subtract_same_charge.root"
    subtract_same_charge = True
    save_histrograms_to_file = True
    load_histrograms_from_file = True
    
    # histograms_defs = [
#         { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 30, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
#         { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
#     ]

class dilepton_muons_bg_basic_ratios_subtract_same_charge_fine_bins(dilepton_muons_bg_basic_ratios_subtract_same_charge):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_basic_ratios_subtract_same_charge_fine_bins.root"
    subtract_same_charge = True
    save_histrograms_to_file = True
    load_histrograms_from_file = True
    
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 30, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
    ]    

class dilepton_muons_bg_basic_ratios_subtract_same_charge_normalised(dilepton_muons_bg_basic_ratios_subtract_same_charge):
    normalise = False
    normalise_each_bg = True
    normalise_integral_positive_only = True
    subtract_same_charge = True
    choose_bg_categories = False
    choose_bg_categories_list = ["WJetsToLNu"]
    no_weights = False
    plot_signal = False
    load_histrograms_from_file = True
    plot_custom_ratio = 0
    plot_ratio = False
    
class dilepton_muons_bg_basic_ratios_subtract_same_charge_normalised_unweighted(dilepton_muons_bg_basic_ratios_subtract_same_charge_normalised):
    no_weights = True
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_basic_ratios_subtract_same_charge_normalised_unweighted.root"
    
class dilepton_muons_bg_btags(dilepton_muons_bg):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_btags.root"
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium > 0 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        {"name":"two", "title": "BTags == 2", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 2 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]
    plot_sc = False
    plot_ratio = False
    plot_signal = False
    

class dilepton_muons_bg_btags_ratio(dilepton_muons_bg):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_btags_ratio.root"
    bg_retag = True
    
    save_histrograms_to_file = True
    load_histrograms_from_file = True 
    
    bgReTagging = {
        "veto" : "(BTagsDeepMedium == 0)",
        "btags" : "(BTagsDeepMedium > 0)",
        "btags2" : "(BTagsDeepMedium == 2)",
    }
    
    bgReTaggingOrder = {
        "veto" : 0,
        "btags" : 1,
        "btags2" : 2,
    }
    bgReTaggingNames = {
        "veto" : "veto",
        "btags" : "BTagsDeepMedium > 0",
        "btags2" : "BTagsDeepMedium == 2",
    }
    
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]
    
    
    plot_custom_ratio = 2
    customRatios = [  [["veto"],["btags"]],  [["veto"],["btags2"]]  ]
    
    plot_signal = False
    plot_sc = False
    plot_data = False
    plot_overflow = False
    plot_ratio = True
    
    blind_data = True
    subtract_same_charge = False
    nostack = True
    
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 30, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
    ] 
    

class dilepton_muons_bg_btags_ratio_sc_subtracted(dilepton_muons_bg_btags_ratio):
    subtract_same_charge = True
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_btags_ratio_sc_subtracted.root"

class dilepton_muons_bg_btags_ratio_sc_subtracted_normalised(dilepton_muons_bg_btags_ratio_sc_subtracted):
    normalise_each_bg = True
    normalise_integral_positive_only = True

class dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse(dilepton_muons_bg_btags_ratio_sc_subtracted_normalised):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse.root"
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 30, "blind" : [4,None], "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30, "blind" : [None,0.1], "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
    ]

class dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse_with_resonances(dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse_with_resonances.root"
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 30, "blind" : [4,None], "customBins"  : [0,2,3.0,3.2,4,6,10,12] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30, "blind" : [None,0.1], "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
    ]
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 0.75 && invMass < 0.81) && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]

class dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_no_weights(dilepton_muons_bg_btags_ratio_sc_subtracted_normalised):
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
    }
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_no_weights.root"
class dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse_no_weights(dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse_with_resonances):
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
    }
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse_no_weights.root"

class dilepton_muons_bg_cleaned_z(dilepton_muons_bg_btags):
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dy/sum/type_sum"

    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_cleaned_z.root"
    cuts = [
        {"name":"none", "title": "None", "condition" : "(DYMuonsInvMass > 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"two", "title": "BTags == 2", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 2 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]
    plot_sc = False
    plot_ratio = False
    plot_signal = False

class dilepton_muons_bg_cleaned_w(dilepton_muons_bg_cleaned_z):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_cleaned_w.root"
    cuts = [
        {"name":"none", "title": "None", "condition" : "(DYMuonsInvMass < 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"two", "title": "BTags == 2", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 2 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]

class dilepton_muons_bg_cleaned_ratio(dilepton_muons_bg):
    # histograms_defs = [
#         { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 30, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
#         { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
#     ]
    save_histrograms_to_file = True
    load_histrograms_from_file = True 
    plot_signal = False
    plot_sc = False
    plot_data = False
    plot_overflow = False
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_cleaned_ratio.root"
    plot_custom_types = ["cleaned-z", "cleaned-w"]
    custom_types_dir = ["/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dy/sum/type_sum", "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dy/sum/type_sum"]
    custom_types_label = ["cleaned Z", "cleaned W"]
    custom_types_conditions = ["DYMuonsInvMass > 0", "DYMuonsInvMass < 0"]
    custom_types_common_files = True
    plot_custom_ratio = 2
    customRatios = [  [["bg"],["cleaned-z"]],  [["bg"],["cleaned-w"]]  ]
    
    weightString = {
        'SingleMuon' : "Weight * passedSingleMuPack * puWeight",
    }
    calculatedLumi = {
        'SingleMuon' : 35.000022662,
    }
    plot_kind = "SingleMuon"

class dilepton_muons_bg_cleaned_ratio_sc_subtracted(dilepton_muons_bg_cleaned_ratio):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_cleaned_ratio_sc_subtracted.root"
    subtract_same_charge = True
    
    
    
class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised(dilepton_muons_bg_cleaned_ratio_sc_subtracted):
    normalise = True
    normalise_integral_positive_only = True

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_retag(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_retag.root"
    
    bg_retag = True
    
    bgReTagging = bgReTaggingCollected
    bgReTaggingOrder = bgReTaggingOrderFull
    bgReTaggingNames = bgReTaggingNamesFull
    
    plot_error = True

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_retag_no_weights(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_retag):
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
    }
    calculatedLumi = {
        'MET' : 0.001,
    }
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_retag_no_weights.root"


class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_no_weights(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised):
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
    }
    calculatedLumi = {
        'MET' : 0.001,
    }
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_no_weights.root"

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse.root"
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 30, "blind" : [4,None], "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30, "blind" : [None,0.1], "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
    ]

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag.root"
    
    bg_retag = True
    
    bgReTagging = bgReTaggingCollected
    bgReTaggingOrder = bgReTaggingOrderFull
    bgReTaggingNames = bgReTaggingNamesFull
    
    plot_error = True

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag):
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
    }
    calculatedLumi = {
        'MET' : 0.001,
    }
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights.root"

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights):
    bgReTagging = bgReTaggingCollectedNoTauTau

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau_dy(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau):
    choose_bg_files = True
    choose_bg_files_list = ["DYJetsToLL"]
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau_dy.root"

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau_zj(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau):
    choose_bg_files = True
    choose_bg_files_list = ["ZJetsToNuNu"]
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau_zj.root"

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_fine_retag_no_weights_no_tautau_zj(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau_zj):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau_zj_fine.root"
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 30, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
    ]

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_no_weights(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse):
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
    }
    calculatedLumi = {
        'MET' : 0.001,
    }
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_no_weights.root"

class clean_dy_sim_data_comparison(BaseParams):

    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/clean_dy_sim_data_comparison.root"
    
    save_histrograms_to_file = True
    load_histrograms_from_file = True 
    
    # weightString = {
#         'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
#     }
    
    weightString = {
        'MET' : "Weight * passedSingleMuPack * puWeight",
    }
    
    calculatedLumi = {
        'MET' : 35.000022662,
    }
    
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dy/sum/type_sum"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_dy/sum"
    plot_signal = False
    plot_overflow = False
    plot_data = True
    plot_ratio = True
    
    # calculatedLumi = {
#         'MET' : 135.778598358,
#     }
    
    cuts = [
        #{"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12 && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        {"name":"none", "title": "None", "condition" : "DYMuonsInvMass > 1"},
        {"name":"high-met", "title": "high-met", "condition" : "DYMuonsInvMass > 1 && (MHT >= 220 &&  MET >= 200)"},
        {"name":"two-mu", "title": "two-mu", "condition" : "DYMuonsInvMass > 1 && (twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        {"name":"mumu", "title": "\mu\mu", "condition" : "DYMuonsInvMass > 1 && (twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12 && BTagsDeepMedium == 0 && vetoElectrons == 0 && vetoMuons == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"}
    ]
    #91.19
    
    #"DYMuonsInvMass" : "float"

    #"DYMuonsSum" : "TLorentzVector",

    histograms_defs = [
        { "obs" : "DYMuonsInvMass", "minX" : 81, "maxX" : 102, "bins" : 100 },
        { "obs" : "DYMuonsSum.Pt()", "minX" : 0, "maxX" : 200, "bins" : 100 },
        { "obs" : "MET", "minX" : 0, "maxX" : 1000, "bins" : 100 },
        { "obs" : "MHT", "minX" : 0, "maxX" : 1000, "bins" : 100 },
        { "obs" : "HT", "minX" : 0, "maxX" : 1000, "bins" : 100 },
        { "obs" : "DYMuons[0].Pt()", "minX" : 0, "maxX" : 300, "bins" : 100 },
        { "obs" : "DYMuons[1].Pt()", "minX" : 0, "maxX" : 300, "bins" : 100 },
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 30, "blind" : [4,None], "customBins"  : [0,2,2.8,3.2,4,6,10,12], "scale" : "width" },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30, "blind" : [None,0.1], "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        #{ "obs" : "MET:DYMuonsSum.Pt()", "minX" : 0, "maxX" : 500, "bins" : 100, "minY" : 0, "maxY" : 100, "binsY" : 100, "2D" : True, "plotStr" : "colz"},
    ]
    
    bg_retag = False
    
    bgReTagging = bgReTaggingFull
    bgReTaggingOrder = bgReTaggingOrderFull
    bgReTaggingNames = bgReTaggingNamesFull

class clean_dy_sim_data_comparison_correlation_sim(clean_dy_sim_data_comparison):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/clean_dy_sim_data_comparison_correlation_sim.root"
    histograms_defs = [
        { "obs" : "MET", "minX" : 0, "maxX" : 1000, "bins" : 100 },
        { "obs" : "MET:DYMuonsSum.Pt()", "minX" : 0, "maxX" : 200, "bins" : 100, "minY" : 0, "maxY" : 100, "binsY" : 100, "2D" : True, "plotStr" : "colz"},
    ]
    solid_bg = True
    plot_data = False