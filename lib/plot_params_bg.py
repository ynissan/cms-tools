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

bgReTaggingCollectedNoTauTauCorrJetIso = {
    "tc" : "tcCorrJetIso15 * (!tautauCorrJetIso15)",
    #"tautau" : "tautau",
    "other" : "otherCorrJetIso15 * (!tautauCorrJetIso15) * (!omegaCorrJetIso15) * (!rho_0CorrJetIso15) * (!etaCorrJetIso15) * (!phiCorrJetIso15) * (!eta_primeCorrJetIso15) * (!j_psiCorrJetIso15) * (!upsilon_1CorrJetIso15) * (!upsilon_2CorrJetIso15)",
    "resonances" : "(scCorrJetIso15 || omegaCorrJetIso15 || rho_0CorrJetIso15 || etaCorrJetIso15 || phiCorrJetIso15 || eta_primeCorrJetIso15 || j_psiCorrJetIso15 || upsilon_1CorrJetIso15 || upsilon_2CorrJetIso15)",
    "nbody" : "n_bodyCorrJetIso15 * (!tautauCorrJetIso15)",
    "fake" : "(rfCorrJetIso15 || ffCorrJetIso15)",
}

bgReTaggingCollectedNoTauTauCorrJetIso15_04 = {
    "tc" : "tcCorrJetIso15Dr0.4 * (!tautauCorrJetIso15Dr0.4)",
    #"tautau" : "tautau",
    "other" : "otherCorrJetIso15Dr0.4 * (!tautauCorrJetIso15Dr0.4) * (!omegaCorrJetIso15Dr0.4) * (!rho_0CorrJetIso15Dr0.4) * (!etaCorrJetIso15Dr0.4) * (!phiCorrJetIso15Dr0.4) * (!eta_primeCorrJetIso15Dr0.4) * (!j_psiCorrJetIso15Dr0.4) * (!upsilon_1CorrJetIso15Dr0.4) * (!upsilon_2CorrJetIso15Dr0.4)",
    "resonances" : "(scCorrJetIso15Dr0.4 || omegaCorrJetIso15Dr0.4 || rho_0CorrJetIso15Dr0.4 || etaCorrJetIso15Dr0.4 || phiCorrJetIso15Dr0.4 || eta_primeCorrJetIso15Dr0.4 || j_psiCorrJetIso15Dr0.4 || upsilon_1CorrJetIso15Dr0.4 || upsilon_2CorrJetIso15Dr0.4)",
    "nbody" : "n_bodyCorrJetIso15Dr0.4 * (!tautauCorrJetIso15Dr0.4)",
    "fake" : "(rfCorrJetIso15Dr0.4 || ffCorrJetIso15Dr0.4)",
}

bgReTaggingCollectedCorrJetIso15 = {
    "tc" : "tcCorrJetIso15 * (!tautauCorrJetIso15)",
    "tautau" : "tautauCorrJetIso15",
    "other" : "otherCorrJetIso15 * (!tautauCorrJetIso15) * (!omegaCorrJetIso15) * (!rho_0CorrJetIso15) * (!etaCorrJetIso15) * (!phiCorrJetIso15) * (!eta_primeCorrJetIso15) * (!j_psiCorrJetIso15) * (!upsilon_1CorrJetIso15) * (!upsilon_2CorrJetIso15)",
    "resonances" : "(scCorrJetIso15 || omegaCorrJetIso15 || rho_0CorrJetIso15 || etaCorrJetIso15 || phiCorrJetIso15 || eta_primeCorrJetIso15 || j_psiCorrJetIso15 || upsilon_1CorrJetIso15 || upsilon_2CorrJetIso15)",
    "nbody" : "n_bodyCorrJetIso15 * (!tautauCorrJetIso15)",
    "fake" : "(rfCorrJetIso15 || ffCorrJetIso15)",
}

bgReTaggingCollectedNoTauTauCorrJetIso10 = {
    "tc" : "tcCorrJetIso10 * (!tautauCorrJetIso10)",
    #"tautau" : "tautau",
    "other" : "otherCorrJetIso10 * (!tautauCorrJetIso10) * (!omegaCorrJetIso10) * (!rho_0CorrJetIso10) * (!etaCorrJetIso10) * (!phiCorrJetIso10) * (!eta_primeCorrJetIso10) * (!j_psiCorrJetIso10) * (!upsilon_1CorrJetIso10) * (!upsilon_2CorrJetIso10)",
    "resonances" : "(scCorrJetIso10 || omegaCorrJetIso10 || rho_0CorrJetIso10 || etaCorrJetIso10 || phiCorrJetIso10 || eta_primeCorrJetIso10 || j_psiCorrJetIso10 || upsilon_1CorrJetIso10 || upsilon_2CorrJetIso10)",
    "nbody" : "n_bodyCorrJetIso10 * (!tautauCorrJetIso10)",
    "fake" : "(rfCorrJetIso10 || ffCorrJetIso10)",
}

bgReTaggingCollectedCorrJetIso10 = {
    "tc" : "tcCorrJetIso10 * (!tautauCorrJetIso10)",
    "tautau" : "tautauCorrJetIso10",
    "other" : "otherCorrJetIso10 * (!tautauCorrJetIso10) * (!omegaCorrJetIso10) * (!rho_0CorrJetIso10) * (!etaCorrJetIso10) * (!phiCorrJetIso10) * (!eta_primeCorrJetIso10) * (!j_psiCorrJetIso10) * (!upsilon_1CorrJetIso10) * (!upsilon_2CorrJetIso10)",
    "resonances" : "(scCorrJetIso10 || omegaCorrJetIso10 || rho_0CorrJetIso10 || etaCorrJetIso10 || phiCorrJetIso10 || eta_primeCorrJetIso10 || j_psiCorrJetIso10 || upsilon_1CorrJetIso10 || upsilon_2CorrJetIso10)",
    "nbody" : "n_bodyCorrJetIso10 * (!tautauCorrJetIso10)",
    "fake" : "(rfCorrJetIso10 || ffCorrJetIso10)",
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

class dilepton_muons_bg_basic_ratios(dilepton_muons_bg_scale):
    plot_sc = False
    save_histrograms_to_file = True
    load_histrograms_from_file = False    
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_basic_ratios.root"
    
    plot_custom_ratio = 2
    customRatios = [  [["WJetsToLNu"],["TTJets"]],  [["WJetsToLNu"],["ZJetsToNuNu"]]  ]


class dilepton_muons_bg_retag_ratios(dilepton_muons_bg):
    plot_sc = False
    save_histrograms_to_file = True
    load_histrograms_from_file = False    
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_retag_ratios.root"
    
    bg_retag = True
    
    bgReTagging = bgReTaggingCollected
    bgReTaggingOrder = bgReTaggingOrderFull
    bgReTaggingNames = bgReTaggingNamesFull
    
    plot_custom_ratio = 2
    customRatios = [  [["fake"],["tc"]],  [["fake"],["tautau"]]  ]
    
class dilepton_muons_bg_basic_ratios_subtract_same_charge(dilepton_muons_bg_basic_ratios):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_basic_ratios_subtract_same_charge.root"
    subtract_same_charge = True
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    
    # histograms_defs = [
#         { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
#         { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
#     ]

class dilepton_muons_bg_basic_ratios_subtract_same_charge_fine_bins(dilepton_muons_bg_basic_ratios_subtract_same_charge):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_basic_ratios_subtract_same_charge_fine_bins.root"
    subtract_same_charge = True
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
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
    load_histrograms_from_file = False
    plot_custom_ratio = 0
    plot_ratio = False
    
class dilepton_muons_bg_basic_ratios_subtract_same_charge_normalised_unweighted(dilepton_muons_bg_basic_ratios_subtract_same_charge_normalised):
    no_weights = True
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_basic_ratios_subtract_same_charge_normalised_unweighted.root"
    
class dilepton_muons_bg_btags(dilepton_muons_bg):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_btags.root"
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium > 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        {"name":"two", "title": "BTags == 2", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 2 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]
    plot_sc = False
    plot_ratio = False
    plot_signal = False
    

class dilepton_muons_bg_btags_ratio(dilepton_muons_bg):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_btags_ratio.root"
    bg_retag = True
    
    save_histrograms_to_file = True
    load_histrograms_from_file = False 
    
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
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && !(invMass > 3 && invMass < 3.2) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        {"name":"no-tautau", "title": "No tautau", "condition" : "(!tautau && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && !(invMass > 3 && invMass < 3.2) && invMass < 12  && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        {"name":"bdt", "title": "BDT>0.1", "condition" : "(dilepBDT > 0.1 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && !(invMass > 3 && invMass < 3.2) && invMass < 12 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        {"name":"bdt-no-tautau", "title": "BDT>0.1 && No tautau", "condition" : "(!tautau && dilepBDT > 0.1 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && !(invMass > 3 && invMass < 3.2) && invMass < 12 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
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
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
    ] 
    

class dilepton_muons_bg_btags_ratio_sc_subtracted(dilepton_muons_bg_btags_ratio):
    subtract_same_charge = True
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_btags_ratio_sc_subtracted.root"

class dilepton_muons_bg_btags_ratio_sc_subtracted_normalised(dilepton_muons_bg_btags_ratio_sc_subtracted):
    normalise_each_bg = True
    normalise_integral_positive_only = True

class dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse(dilepton_muons_bg_btags_ratio_sc_subtracted_normalised):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse.root"
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None], "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1], "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
    ]

class dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse_with_resonances(dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse_with_resonances.root"
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None], "customBins"  : [0,2,3.0,3.2,4,6,10,12] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1], "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
    ]
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]

class dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_no_weights(dilepton_muons_bg_btags_ratio_sc_subtracted_normalised):
    weightString = {
        'MET' : "1",
    }
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_no_weights.root"
class dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse_no_weights(dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse_with_resonances):
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
    }
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_btags_ratio_sc_subtracted_normalised_coarse_no_weights.root"

class dilepton_muons_bg_cleaned_z(dilepton_muons_bg_btags):
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dy/sum/type_sum"

    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_cleaned_z.root"
    cuts = [
        {"name":"none", "title": "None", "condition" : "(DYMuonsInvMass > 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"two", "title": "BTags == 2", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 2 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]
    plot_sc = False
    plot_ratio = False
    plot_signal = False

class dilepton_muons_bg_cleaned_w(dilepton_muons_bg_cleaned_z):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_cleaned_w.root"
    cuts = [
        {"name":"none", "title": "None", "condition" : "(DYMuonsInvMass < 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"two", "title": "BTags == 2", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 2 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]

class dilepton_muons_bg_cleaned_ratio(dilepton_muons_bg):
    # histograms_defs = [
#         { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
#         { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
#     ]
    save_histrograms_to_file = True
    load_histrograms_from_file = False 
    plot_signal = False
    plot_sc = False
    plot_data = False
    plot_overflow = False
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_cleaned_ratio.root"
    plot_custom_types = ["cleaned-z", "cleaned-w"]
    custom_types_dir = ["/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dy/sum/type_sum", "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dy/sum/type_sum"]
    custom_types_label = ["cleaned Z", "cleaned W"]
    custom_types_conditions = ["DYMuonsInvMass > 0", "DYMuonsInvMass < 0"]
    custom_types_common_files = True
    plot_custom_ratio = 2
    customRatios = [  [["bg"],["cleaned-z"]],  [["bg"],["cleaned-w"]]  ]
    
    weightString = {
        'SingleMuon' : "Weight"# * passedSingleMuPack * puWeight",
    }
    #calculatedLumi = {
    #    'SingleMuon' : 35.000022662,
    #}
    plot_kind = "SingleMuon"

#dilepton_muons_bg_isocr dilepton_muons_bg_isocr_notautau dilepton_muons_bg_isocr_res dilepton_muons_bg_isocr_tc dilepton_muons_bg_isocr_tautau dilepton_muons_bg_isocr_other dilepton_muons_bg_isocr_nbody dilepton_muons_bg_isocr_fake

class dilepton_muons_bg_isocr(dilepton_muons_bg_btags_ratio):
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr.root"
    
    bg_retag = True
    
    save_histrograms_to_file = True
    load_histrograms_from_file = False 
    
    # bgReTagging = {
#         "veto" : "(isoCr == 0)",
#         "isoCr" : "(isoCr >= 1)",
#     }
#     
#     bgReTaggingOrder = {
#         "veto" : 0,
#         "isoCr" : 1,
#     }
#     bgReTaggingNames = {
#         "veto" : "veto",
#         "isoCr" : "Jet Iso #Delta_{}R CR",
#     }
    
    bgReTagging = bgReTaggingCollected
    bgReTaggingOrder = bgReTaggingOrderFull
    bgReTaggingNames = bgReTaggingNamesFull
    
    cuts = [
        #{"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1"},
        #{"name":"isocr1", "title": "isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr == 1"},
        {"name":"mindr01", "title": "MinDr >= 0.1 && isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr == 1 && isoCrMinDr >= 0.1"},
        {"name":"mindr02", "title": "MinDr >= 0.2 && isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr == 1 && isoCrMinDr >= 0.2"},
        #{"name": "bdt", "title": "bdt >= 0.1", "condition" : "(dilepBDT >= 0.1 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1"},
        #{"name":"no-tautau", "title": "No tautau", "condition" : "(!tautau && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && !(invMass > 3 && invMass < 3.2) && invMass < 12  && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"bdt", "title": "BDT>0.1", "condition" : "(dilepBDT > 0.1 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && !(invMass > 3 && invMass < 3.2) && invMass < 12 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"bdt-no-tautau", "title": "BDT>0.1 && No tautau", "condition" : "(!tautau && dilepBDT > 0.1 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && !(invMass > 3 && invMass < 3.2) && invMass < 12 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        
        #{"name":"low-met", "title": "Low Met", "condition" : "(twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]
    
    
    plot_custom_ratio = 0
    #customRatios = [  [["veto"],["isoCr"]]  ]
    
    plot_signal = False
    plot_sc = True
    plot_data = False
    plot_overflow = False
    plot_ratio = True
    
    blind_data = True
    subtract_same_charge = False
    nostack = False
    
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        #{ "obs" : "isoCrMinDr", "minX" : 0, "maxX" : 0.4, "bins" : 8},
        { "obs" : "deltaR", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "dilepHt", "minX" : 200, "maxX" : 800, "bins" : 8},
        { "obs" : "dileptonPt", "minX" : 0, "maxX" : 30, "bins" : 8},
        { "obs" : "MHT", "minX" : 220, "maxX" : 800, "bins" : 8},
        { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "leptons[0].Pt()", "minX" : 0, "maxX" : 20, "bins" : 8},
        { "obs" : "deltaPhiMetLepton1", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "mt1", "minX" : 0, "maxX" : 200, "bins" : 8},
        { "obs" : "leptons[0].Eta()", "minX" : -2.4, "maxX" : 2.4, "bins" : 8},
        { "obs" : "NJets", "minX" : 0, "maxX" : 6, "bins" : 6},
        { "obs" : "deltaPhiMetLepton2", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 500, "bins" : 8},
        { "obs" : "LeadingJet.Eta()", "minX" : -2.4, "maxX" : 2.4, "bins" : 8},
        { "obs" : "deltaEta", "minX" : 0, "maxX" : 5, "bins" : 8},
        { "obs" : "HT", "minX" : 0, "maxX" : 500, "bins" : 8},
        { "obs" : "leptons[0].Phi()", "minX" : 0, "maxX" : 3.5, "bins" : 8},
    ]
    
    normalise = True
    normalise_each_bg = False
    plot_error = True
    sc_label = "Jet Iso #Delta_{}R CR"
    sc_ratio_label = "cr"

class dilepton_muons_bg_isocr_min_dr(dilepton_muons_bg_isocr):
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_min_dr.root"
    
    histograms_defs = [
        { "obs" : "isoCrMinDr", "minX" : 0, "maxX" : 0.4, "bins" : 8}
    ]
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr >= 1", "sc" : "sameSign == 0 && isoCr >= 1"},
    ]
    plot_sc = False
    plot_ratio = False
    normalise = False

class dilepton_muons_bg_isocr_notautau(dilepton_muons_bg_isocr):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_notautau.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    bgReTagging = bgReTaggingCollectedNoTauTau
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
        {"name":"isocr1", "title": "isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr == 1  && !tautau"},
        {"name":"mindr01", "title": "MinDr >= 0.1 && isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr == 1 && !tautau && isoCrMinDr >= 0.1"},
        {"name":"mindr02", "title": "MinDr >= 0.2 && isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr == 1 && !tautau && isoCrMinDr >= 0.2"},
        {"name":"isocr011", "title": "MinDr >= 0.1 && isoCr >= 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau && isoCrMinDr >= 0.1"},
        {"name":"isocr02", "title": "MinDr >= 0.2 && isoCr >= 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau && isoCrMinDr >= 0.2"},
        #{"name":"nj", "title": "NJ >= 2", "condition" : "(NJets >= 2 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
        #{"name": "bdt", "title": "bdt >= 0.1", "condition" : "(dilepBDT >= 0.1 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
        
        #{"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
    ]

class dilepton_muons_bg_isocr_notautau_corrjetiso(dilepton_muons_bg_isocr_notautau):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_notautau_corrjetiso.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    bgReTagging = bgReTaggingCollectedNoTauTauCorrJetIso
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_0.4/sum/type_sum"
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 >= 1 && !tautauCorrJetIso15"},
        {"name":"isocr1", "title": "isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 1 && !tautauCorrJetIso15"},
        {"name":"mindr01", "title": "MinDr >= 0.1 && isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 1 && !tautauCorrJetIso15 && isoCrMinDrCorrJetIso15 >= 0.1"},
        {"name":"mindr02", "title": "MinDr >= 0.2 && isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 1 && !tautauCorrJetIso15 && isoCrMinDrCorrJetIso15 >= 0.2"},
        {"name":"isocr011", "title": "MinDr >= 0.1 && isoCr >= 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 >= 1 && !tautauCorrJetIso15 && isoCrMinDrCorrJetIso15 >= 0.1"},
        {"name":"isocr02", "title": "MinDr >= 0.2 && isoCr >= 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 >= 1 && !tautauCorrJetIso15 && isoCrMinDrCorrJetIso15 >= 0.2"},
        #{"name":"nj", "title": "NJ >= 2", "condition" : "(NJets >= 2 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
        #{"name": "bdt", "title": "bdt >= 0.1", "condition" : "(dilepBDT >= 0.1 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
        
        #{"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
    ]
    
    histograms_defs = [
        { "obs" : "invMassCorrJetIso15", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDTCorrJetIso15", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        { "obs" : "isoCrMinDrCorrJetIso15", "minX" : 0, "maxX" : 0.4, "bins" : 8},
        { "obs" : "deltaRCorrJetIso15", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "dilepHtCorrJetIso15", "minX" : 200, "maxX" : 800, "bins" : 8},
        { "obs" : "dileptonPtCorrJetIso15", "minX" : 0, "maxX" : 30, "bins" : 8},
        { "obs" : "MHT", "minX" : 220, "maxX" : 800, "bins" : 8},
        { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "leptonsCorrJetIso15[0].Pt()", "minX" : 0, "maxX" : 20, "bins" : 8},
        { "obs" : "deltaPhiMetLepton1CorrJetIso15", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "mt1CorrJetIso15", "minX" : 0, "maxX" : 200, "bins" : 8},
        { "obs" : "leptonsCorrJetIso15[0].Eta()", "minX" : -2.4, "maxX" : 2.4, "bins" : 8},
        { "obs" : "NJets", "minX" : 0, "maxX" : 6, "bins" : 6},
        { "obs" : "deltaPhiMetLepton2CorrJetIso15", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 500, "bins" : 8},
        { "obs" : "LeadingJet.Eta()", "minX" : -2.4, "maxX" : 2.4, "bins" : 8},
        { "obs" : "deltaEtaCorrJetIso15", "minX" : 0, "maxX" : 5, "bins" : 8},
        { "obs" : "HT", "minX" : 0, "maxX" : 500, "bins" : 8},
        { "obs" : "leptonsCorrJetIso15[0].Phi()", "minX" : 0, "maxX" : 3.5, "bins" : 8},
    ]


class dilepton_muons_bg_isocr_notautau_corrjetiso_15_04(dilepton_muons_bg_isocr_notautau_corrjetiso):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_notautau_corrjetiso_15_04.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    bgReTagging = bgReTaggingCollectedNoTauTauCorrJetIso15_04
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
    cuts = [
        {"name":"none", "title": "None", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15Dr0.4 == 1 && MHT >= 220 &&  MET >= 200 && leptonFlavourCorrJetIso15Dr0.4 == \"Muons\" && invMassCorrJetIso15Dr0.4 < 12  && invMassCorrJetIso15Dr0.4 > 0.4 && !(invMassCorrJetIso15Dr0.4 > 3 && invMassCorrJetIso15Dr0.4 < 3.2) && !(invMassCorrJetIso15Dr0.4 > 0.75 && invMassCorrJetIso15Dr0.4 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15Dr0.4 == 0 && isoCrCorrJetIso15Dr0.4 == 0 && !tautauCorrJetIso15Dr0.4", "sc" : "sameSignCorrJetIso15Dr0.4 == 0 && isoCrCorrJetIso15Dr0.4 >= 1 && !tautauCorrJetIso15Dr0.4"},
    ]
    
    histograms_defs = [
        { "obs" : "invMassCorrJetIso15Dr0.4", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDTCorrJetIso15Dr0.4", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        { "obs" : "isoCrMinDrCorrJetIso15Dr0.4", "minX" : 0, "maxX" : 0.4, "bins" : 8},
        { "obs" : "deltaRCorrJetIso15Dr0.4", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "dilepHtCorrJetIso15Dr0.4", "minX" : 200, "maxX" : 800, "bins" : 8},
        { "obs" : "dileptonPtCorrJetIso15Dr0.4", "minX" : 0, "maxX" : 30, "bins" : 8},
        { "obs" : "MHT", "minX" : 220, "maxX" : 800, "bins" : 8},
        { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "leptonsCorrJetIso15Dr0.4[0].Pt()", "minX" : 0, "maxX" : 20, "bins" : 8},
        { "obs" : "deltaPhiMetLepton1CorrJetIso15Dr0.4", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "mt1CorrJetIso15Dr0.4", "minX" : 0, "maxX" : 200, "bins" : 8},
        { "obs" : "leptonsCorrJetIso15Dr0.4[0].Eta()", "minX" : -2.4, "maxX" : 2.4, "bins" : 8},
        { "obs" : "NJets", "minX" : 0, "maxX" : 6, "bins" : 6},
        { "obs" : "deltaPhiMetLepton2CorrJetIso15Dr0.4", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 500, "bins" : 8},
        { "obs" : "LeadingJet.Eta()", "minX" : -2.4, "maxX" : 2.4, "bins" : 8},
        { "obs" : "deltaEtaCorrJetIso15Dr0.4", "minX" : 0, "maxX" : 5, "bins" : 8},
        { "obs" : "HT", "minX" : 0, "maxX" : 500, "bins" : 8},
        { "obs" : "leptonsCorrJetIso15Dr0.4[0].Phi()", "minX" : 0, "maxX" : 3.5, "bins" : 8},
    ]


class dilepton_muons_bg_isocr_notautau_corrjetiso_no_norm(dilepton_muons_bg_isocr_notautau_corrjetiso):
    load_histrograms_from_file = True
    normalise = False

class dilepton_muons_bg_isocr_inclusive_corrjetiso(dilepton_muons_bg_isocr_notautau_corrjetiso):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_inclusive_corrjetiso.root"
    bgReTagging = bgReTaggingCollectedCorrJetIso15
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 >= 1"},
        #{"name":"isocr1", "title": "isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 1"},
        #{"name":"mindr01", "title": "MinDr >= 0.1 && isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 1 && isoCrMinDrCorrJetIso15 >= 0.1"},
        #{"name":"mindr02", "title": "MinDr >= 0.2 && isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 1 && isoCrMinDrCorrJetIso15 >= 0.2"},
        #{"name":"isocr011", "title": "MinDr >= 0.1 && isoCr >= 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 >= 1 && isoCrMinDrCorrJetIso15 >= 0.1"},
        #{"name":"isocr02", "title": "MinDr >= 0.2 && isoCr >= 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 >= 1 && isoCrMinDrCorrJetIso15 >= 0.2"},
        #{"name":"nj", "title": "NJ >= 2", "condition" : "(NJets >= 2 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
        #{"name": "bdt", "title": "bdt >= 0.1", "condition" : "(dilepBDT >= 0.1 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
        
        #{"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
    ]

class dilepton_muons_bg_isocr_inclusive_corrjetiso_no_norm(dilepton_muons_bg_isocr_inclusive_corrjetiso):
    normalise = False
    load_histrograms_from_file = True

class dilepton_muons_bg_isocr_tautau_corrjetiso15(dilepton_muons_bg_isocr_inclusive_corrjetiso):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_tautau_corrjetiso15.root"
    choose_bg_categories_list = ["tautau"]
    choose_bg_categories = True
    cuts = [
        #{"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["tautau"]},
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 >= 1 && " + dilepton_muons_bg_isocr_inclusive_corrjetiso.bgReTagging["tautau"] + " == 1"},
    ]

class dilepton_muons_bg_isocr_tautau_corrjetiso15_no_norm(dilepton_muons_bg_isocr_tautau_corrjetiso15):
    normalise = False
    load_histrograms_from_file = True

class dilepton_muons_bg_isocr_notautau_corrjetiso_15_0_6(dilepton_muons_bg_isocr_notautau_corrjetiso):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_notautau_corrjetiso_15_0_6.root"
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"

class dilepton_muons_bg_isocr_notautau_corrjetiso_15_0_6_no_norm(dilepton_muons_bg_isocr_notautau_corrjetiso_15_0_6):
    normalise = False
    load_histrograms_from_file = True

class dilepton_muons_bg_isocr_notautau_corrjetiso_10(dilepton_muons_bg_isocr_notautau_corrjetiso):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_notautau_corrjetiso_10.root"
    bgReTagging = bgReTaggingCollectedNoTauTauCorrJetIso10
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso10 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso10.size() == 2 && leptonFlavourCorrJetIso10 == \"Muons\" && invMassCorrJetIso10 < 12  && invMassCorrJetIso10 > 0.4 && !(invMassCorrJetIso10 > 3 && invMassCorrJetIso10 < 3.2) && !(invMassCorrJetIso10 > 0.75 && invMassCorrJetIso10 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso10 == 0 && isoCrCorrJetIso10 == 0 && !tautauCorrJetIso10", "sc" : "sameSignCorrJetIso10 == 0 && isoCrCorrJetIso10 >= 1 && !tautauCorrJetIso10"},
        {"name":"isocr1", "title": "isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso10 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso10.size() == 2 && leptonFlavourCorrJetIso10 == \"Muons\" && invMassCorrJetIso10 < 12  && invMassCorrJetIso10 > 0.4 && !(invMassCorrJetIso10 > 3 && invMassCorrJetIso10 < 3.2) && !(invMassCorrJetIso10 > 0.75 && invMassCorrJetIso10 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso10 == 0 && isoCrCorrJetIso10 == 0 && !tautauCorrJetIso10", "sc" : "sameSignCorrJetIso10 == 0 && isoCrCorrJetIso10 == 1 && !tautauCorrJetIso10"},
        {"name":"mindr01", "title": "MinDr >= 0.1 && isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso10 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso10.size() == 2 && leptonFlavourCorrJetIso10 == \"Muons\" && invMassCorrJetIso10 < 12  && invMassCorrJetIso10 > 0.4 && !(invMassCorrJetIso10 > 3 && invMassCorrJetIso10 < 3.2) && !(invMassCorrJetIso10 > 0.75 && invMassCorrJetIso10 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso10 == 0 && isoCrCorrJetIso10 == 0 && !tautauCorrJetIso10", "sc" : "sameSignCorrJetIso10 == 0 && isoCrCorrJetIso10 == 1 && !tautauCorrJetIso10 && isoCrMinDrCorrJetIso10 >= 0.1"},
        {"name":"mindr02", "title": "MinDr >= 0.2 && isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso10 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso10.size() == 2 && leptonFlavourCorrJetIso10 == \"Muons\" && invMassCorrJetIso10 < 12  && invMassCorrJetIso10 > 0.4 && !(invMassCorrJetIso10 > 3 && invMassCorrJetIso10 < 3.2) && !(invMassCorrJetIso10 > 0.75 && invMassCorrJetIso10 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso10 == 0 && isoCrCorrJetIso10 == 0 && !tautauCorrJetIso10", "sc" : "sameSignCorrJetIso10 == 0 && isoCrCorrJetIso10 == 1 && !tautauCorrJetIso10 && isoCrMinDrCorrJetIso10 >= 0.2"},
        {"name":"isocr011", "title": "MinDr >= 0.1 && isoCr >= 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso10 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso10.size() == 2 && leptonFlavourCorrJetIso10 == \"Muons\" && invMassCorrJetIso10 < 12  && invMassCorrJetIso10 > 0.4 && !(invMassCorrJetIso10 > 3 && invMassCorrJetIso10 < 3.2) && !(invMassCorrJetIso10 > 0.75 && invMassCorrJetIso10 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso10 == 0 && isoCrCorrJetIso10 == 0 && !tautauCorrJetIso10", "sc" : "sameSignCorrJetIso10 == 0 && isoCrCorrJetIso10 >= 1 && !tautauCorrJetIso10 && isoCrMinDrCorrJetIso10 >= 0.1"},
        {"name":"isocr02", "title": "MinDr >= 0.2 && isoCr >= 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso10 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso10.size() == 2 && leptonFlavourCorrJetIso10 == \"Muons\" && invMassCorrJetIso10 < 12  && invMassCorrJetIso10 > 0.4 && !(invMassCorrJetIso10 > 3 && invMassCorrJetIso10 < 3.2) && !(invMassCorrJetIso10 > 0.75 && invMassCorrJetIso10 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso10 == 0 && isoCrCorrJetIso10 == 0 && !tautauCorrJetIso10", "sc" : "sameSignCorrJetIso10 == 0 && isoCrCorrJetIso10 >= 1 && !tautauCorrJetIso10 && isoCrMinDrCorrJetIso10 >= 0.2"},
        #{"name":"nj", "title": "NJ >= 2", "condition" : "(NJets >= 2 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
        #{"name": "bdt", "title": "bdt >= 0.1", "condition" : "(dilepBDT >= 0.1 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
        
        #{"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
    ]
    histograms_defs = [
        { "obs" : "invMassCorrJetIso10", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDTCorrJetIso10", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        { "obs" : "isoCrMinDrCorrJetIso10", "minX" : 0, "maxX" : 0.4, "bins" : 8},
        { "obs" : "deltaRCorrJetIso10", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "dilepHtCorrJetIso10", "minX" : 200, "maxX" : 800, "bins" : 8},
        { "obs" : "dileptonPtCorrJetIso10", "minX" : 0, "maxX" : 30, "bins" : 8},
        { "obs" : "MHT", "minX" : 220, "maxX" : 800, "bins" : 8},
        { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "leptonsCorrJetIso10[0].Pt()", "minX" : 0, "maxX" : 20, "bins" : 8},
        { "obs" : "deltaPhiMetLepton1CorrJetIso10", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "mt1CorrJetIso10", "minX" : 0, "maxX" : 200, "bins" : 8},
        { "obs" : "leptonsCorrJetIso10[0].Eta()", "minX" : -2.4, "maxX" : 2.4, "bins" : 8},
        { "obs" : "NJets", "minX" : 0, "maxX" : 6, "bins" : 6},
        { "obs" : "deltaPhiMetLepton2CorrJetIso10", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 500, "bins" : 8},
        { "obs" : "LeadingJet.Eta()", "minX" : -2.4, "maxX" : 2.4, "bins" : 8},
        { "obs" : "deltaEtaCorrJetIso10", "minX" : 0, "maxX" : 5, "bins" : 8},
        { "obs" : "HT", "minX" : 0, "maxX" : 500, "bins" : 8},
        { "obs" : "leptonsCorrJetIso10[0].Phi()", "minX" : 0, "maxX" : 3.5, "bins" : 8},
    ]

class dilepton_muons_bg_isocr_notautau_corrjetiso_10_no_norm(dilepton_muons_bg_isocr_notautau_corrjetiso_10):
    normalise = False
    load_histrograms_from_file = True

class dilepton_muons_bg_isocr_inclusive_corrjetiso_10(dilepton_muons_bg_isocr_notautau_corrjetiso_10):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_inclusive_corrjetiso_10.root"
    bgReTagging = bgReTaggingCollectedCorrJetIso10
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso10 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso10.size() == 2 && leptonFlavourCorrJetIso10 == \"Muons\" && invMassCorrJetIso10 < 12  && invMassCorrJetIso10 > 0.4 && !(invMassCorrJetIso10 > 3 && invMassCorrJetIso10 < 3.2) && !(invMassCorrJetIso10 > 0.75 && invMassCorrJetIso10 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso10 == 0 && isoCrCorrJetIso10 == 0", "sc" : "sameSignCorrJetIso10 == 0 && isoCrCorrJetIso10 >= 1"},
    ]

class dilepton_muons_bg_isocr_notautau_corrjetiso_10_0_6(dilepton_muons_bg_isocr_notautau_corrjetiso_10):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_notautau_corrjetiso_10_0_6.root"
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"

class dilepton_muons_bg_isocr_notautau_corrjetiso_mindr(dilepton_muons_bg_isocr_notautau_corrjetiso):
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 > 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 >= 1 && !tautauCorrJetIso15"},
    ]
    histograms_defs = [
        { "obs" : "isoCrMinDrCorrJetIso15", "minX" : 0, "maxX" : 0.4, "bins" : 8},
    ]
    plot_sc = False
    plot_ratio = False
    normalise = False

class dilepton_muons_bg_isocr_notautau_corrjetiso_10_0_6_no_norm(dilepton_muons_bg_isocr_notautau_corrjetiso_10_0_6):
    normalise = False
    load_histrograms_from_file = True

class dilepton_muons_bg_isocr_notautau_working_02_corrjetiso(dilepton_muons_bg_isocr):
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dr_0.2_working/sum/type_sum"
    bgReTagging = bgReTaggingCollectedNoTauTauCorrJetIso
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 >= 1 && !tautauCorrJetIso15"},
        {"name":"isocr1", "title": "isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 1 && !tautauCorrJetIso15"},
        #{"name":"isocr1", "title": "isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr == 1  && !tautau"},
        #{"name":"mindr01", "title": "MinDr >= 0.1 && isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr == 1 && isoCrMinDr >= 0.1"},
        #{"name":"mindr02", "title": "MinDr >= 0.2 && isoCr == 1", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr == 1 && isoCrMinDr >= 0.2"},
        
        #{"name":"isocr02", "title": "MinDr >= 0.1", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau && isoCrMinDr >= 0.1"},
        #{"name":"isocr02", "title": "MinDr >= 0.2", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau && isoCrMinDr >= 0.2"},
        #{"name":"nj", "title": "NJ >= 2", "condition" : "(NJets >= 2 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
        #{"name": "bdt", "title": "bdt >= 0.1", "condition" : "(dilepBDT >= 0.1 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
        
        #{"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && !tautau"},
    ]
    histograms_defs = [
        { "obs" : "invMassCorrJetIso15", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDTCorrJetIso15", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        #{ "obs" : "isoCrMinDr", "minX" : 0, "maxX" : 0.4, "bins" : 8},
        { "obs" : "deltaRCorrJetIso15", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "dilepHtCorrJetIso15", "minX" : 200, "maxX" : 800, "bins" : 8},
        { "obs" : "dileptonPtCorrJetIso15", "minX" : 0, "maxX" : 30, "bins" : 8},
        { "obs" : "MHT", "minX" : 220, "maxX" : 800, "bins" : 8},
        { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "leptonsCorrJetIso15[0].Pt()", "minX" : 0, "maxX" : 20, "bins" : 8},
        { "obs" : "deltaPhiMetLepton1CorrJetIso15", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "mt1CorrJetIso15", "minX" : 0, "maxX" : 200, "bins" : 8},
        { "obs" : "leptonsCorrJetIso15[0].Eta()", "minX" : -2.4, "maxX" : 2.4, "bins" : 8},
        { "obs" : "NJets", "minX" : 0, "maxX" : 6, "bins" : 6},
        { "obs" : "deltaPhiMetLepton2CorrJetIso15", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 500, "bins" : 8},
        { "obs" : "LeadingJet.Eta()", "minX" : -2.4, "maxX" : 2.4, "bins" : 8},
        { "obs" : "deltaEtaCorrJetIso15", "minX" : 0, "maxX" : 5, "bins" : 8},
        { "obs" : "HT", "minX" : 0, "maxX" : 500, "bins" : 8},
        { "obs" : "leptonsCorrJetIso15[0].Phi()", "minX" : 0, "maxX" : 3.5, "bins" : 8},
    ]

class dilepton_muons_bg_isocr_res(dilepton_muons_bg_isocr):
    choose_bg_categories = True
    choose_bg_files_for_sc = True
    choose_bg_categories_list = ["resonances"]
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["resonances"]},
        {"name":"isocr", "title": "MinDr >= 0.2", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && isoCrMinDr >= 0.2 && " + dilepton_muons_bg_isocr.bgReTagging["resonances"]},
        #{"name":"nj", "title": "NJ >= 2", "condition" : "(NJets >= 2 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["resonances"]},
        #{"name": "bdt", "title": "bdt >= 0.1", "condition" : "(dilepBDT >= 0.1 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["resonances"]},
    ]

class dilepton_muons_bg_isocr_tc(dilepton_muons_bg_isocr_res):
    choose_bg_categories_list = ["tc"]
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["tc"]},
        {"name":"isocr", "title": "MinDr >= 0.2", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && isoCrMinDr >= 0.2 && " + dilepton_muons_bg_isocr.bgReTagging["tc"]},
        {"name":"nj", "title": "NJ >= 2", "condition" : "(NJets >= 2 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["tc"]},
        {"name": "bdt", "title": "bdt >= 0.1", "condition" : "(dilepBDT >= 0.1 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["tc"]},
    ]

class dilepton_muons_bg_isocr_tautau(dilepton_muons_bg_isocr_tc):
    choose_bg_categories_list = ["tautau"]
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["tautau"]},
        {"name":"isocr", "title": "MinDr >= 0.2", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && isoCrMinDr >= 0.2 && " + dilepton_muons_bg_isocr.bgReTagging["tautau"]},
        #{"name":"nj", "title": "NJ >= 2", "condition" : "(NJets >= 2 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["tautau"]},
        #{"name": "bdt", "title": "bdt >= 0.1", "condition" : "(dilepBDT >= 0.1 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["tautau"]},
    ]

class dilepton_muons_bg_isocr_other(dilepton_muons_bg_isocr_tc):
    choose_bg_categories_list = ["other"]
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["other"]},
        {"name":"isocr", "title": "MinDr >= 0.2", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && isoCrMinDr >= 0.2 && " + dilepton_muons_bg_isocr.bgReTagging["other"]},
        #{"name":"nj", "title": "NJ >= 2", "condition" : "(NJets >= 2 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["other"]},
        #{"name": "bdt", "title": "bdt >= 0.1", "condition" : "(dilepBDT >= 0.1 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["other"]},
    ]

class dilepton_muons_bg_isocr_nbody(dilepton_muons_bg_isocr_tc):
    choose_bg_categories_list = ["nbody"]
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["nbody"]},
        {"name":"isocr", "title": "MinDr >= 0.2", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && isoCrMinDr >= 0.2 && " + dilepton_muons_bg_isocr.bgReTagging["nbody"]},
        #{"name":"nj", "title": "NJ >= 2", "condition" : "(NJets >= 2 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["nbody"]},
        #{"name": "bdt", "title": "bdt >= 0.1", "condition" : "(dilepBDT >= 0.1 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["nbody"]},
    ]

class dilepton_muons_bg_isocr_fake(dilepton_muons_bg_isocr_tc):
    choose_bg_categories_list = ["fake"]
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["fake"]},
        {"name":"isocr", "title": "MinDr >= 0.2", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0 && !tautau", "sc" : "sameSign == 0 && isoCr >= 1 && isoCrMinDr >= 0.2 && " + dilepton_muons_bg_isocr.bgReTagging["fake"]},
        #{"name":"nj", "title": "NJ >= 2", "condition" : "(NJets >= 2 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["fake"]},
        #{"name": "bdt", "title": "bdt >= 0.1", "condition" : "(dilepBDT >= 0.1 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && " + dilepton_muons_bg_isocr.bgReTagging["fake"]},
    ]

#dilepton_muons_bg_isocr_sm dilepton_muons_bg_isocr_sm_wjets dilepton_muons_bg_isocr_sm_ttjets dilepton_muons_bg_isocr_sm_dy dilepton_muons_bg_isocr_sm_zjets dilepton_muons_bg_isocr_sm_rare dilepton_muons_bg_isocr_sm_diboson

class dilepton_muons_bg_isocr_sm(dilepton_muons_bg_isocr):
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_0.4/sum/type_sum"
    load_histrograms_from_file = False
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_sm.root"
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1"},
        {"name":"mindr", "title": "MinDr >= 0.2", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && isoCrMinDr >= 0.2"},
        #{"name":"nj", "title": "NJ >= 2", "condition" : "(NJets >= 2 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1"},
        #{"name": "bdt", "title": "bdt >= 0.1", "condition" : "(dilepBDT >= 0.1 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1"},
    ]
    plot_sc = True
    plot_custom_ratio = False
    customRatios = []
    plot_ratio = True
    normalise = True
    normalise_each_bg = False
    bg_retag = False
    nostack = False
    sc_label = "Jet Iso #Delta_{}R CR"
    sc_ratio_label = "cr"

class dilepton_muons_bg_isocr_sm_corrjetiso_15(dilepton_muons_bg_isocr_sm):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_sm_corrjetiso_15.root"
    cuts = [
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptonsCorrJetIso15 == 1 && MHT >= 220 &&  MET >= 200 && @leptonsCorrJetIso15.size() == 2 && leptonFlavourCorrJetIso15 == \"Muons\" && invMassCorrJetIso15 < 12  && invMassCorrJetIso15 > 0.4 && !(invMassCorrJetIso15 > 3 && invMassCorrJetIso15 < 3.2) && !(invMassCorrJetIso15 > 0.75 && invMassCorrJetIso15 < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 == 0 && !tautauCorrJetIso15", "sc" : "sameSignCorrJetIso15 == 0 && isoCrCorrJetIso15 >= 1 && !tautauCorrJetIso15"},
    ]
    histograms_defs = [
        { "obs" : "invMassCorrJetIso15", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDTCorrJetIso15", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        { "obs" : "isoCrMinDrCorrJetIso15", "minX" : 0, "maxX" : 0.4, "bins" : 8},
        { "obs" : "deltaRCorrJetIso15", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "dilepHtCorrJetIso15", "minX" : 200, "maxX" : 800, "bins" : 8},
        { "obs" : "dileptonPtCorrJetIso15", "minX" : 0, "maxX" : 30, "bins" : 8},
        { "obs" : "MHT", "minX" : 220, "maxX" : 800, "bins" : 8},
        { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "leptonsCorrJetIso15[0].Pt()", "minX" : 0, "maxX" : 20, "bins" : 8},
        { "obs" : "deltaPhiMetLepton1CorrJetIso15", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "mt1CorrJetIso15", "minX" : 0, "maxX" : 200, "bins" : 8},
        { "obs" : "leptonsCorrJetIso15[0].Eta()", "minX" : -2.4, "maxX" : 2.4, "bins" : 8},
        { "obs" : "NJets", "minX" : 0, "maxX" : 6, "bins" : 6},
        { "obs" : "deltaPhiMetLepton2CorrJetIso15", "minX" : 0, "maxX" : 3.5, "bins" : 8},
        { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 500, "bins" : 8},
        { "obs" : "LeadingJet.Eta()", "minX" : -2.4, "maxX" : 2.4, "bins" : 8},
        { "obs" : "deltaEtaCorrJetIso15", "minX" : 0, "maxX" : 5, "bins" : 8},
        { "obs" : "HT", "minX" : 0, "maxX" : 500, "bins" : 8},
        { "obs" : "leptonsCorrJetIso15[0].Phi()", "minX" : 0, "maxX" : 3.5, "bins" : 8},
    ]
    
class dilepton_muons_bg_isocr_sm_mindr(dilepton_muons_bg_isocr_sm):
    plot_sc = False
    plot_ratio = False
    cuts = [
        #{"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 0 && isoCr >= 1"},
        {"name":"none", "title": "None", "condition" : "(BTagsDeepMedium == 0 && MHT >= 220 &&  MET >= 200 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "", "sc" : "sameSign == 0 && isoCr >= 1"},
        #{"name":"mindr", "title": "MinDr >= 0.2", "condition" : "(BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1 && isoCrMinDr >= 0.2"},
        #{"name":"nj", "title": "NJ >= 2", "condition" : "(NJets >= 2 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1"},
        #{"name": "bdt", "title": "bdt >= 0.1", "condition" : "(dilepBDT >= 0.1 && BTagsDeepMedium == 0 && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0 && isoCr == 0", "sc" : "sameSign == 0 && isoCr >= 1"},
    ]
    histograms_defs = [
        { "obs" : "Muons_minDeltaRJets", "minX" : 0, "maxX" : 3, "bins" : 30, "blind" : [4,None], "condition" : "Muons_passCorrJetIso15 == 1 && Jets[Muons_closestJet].Pt() > 15 && Jets[Muons_closestJet].Pt() < 30"},# "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "Muons_minDeltaRJets_cr", "formula": "Muons_minDeltaRJets" ,"minX" : 0, "maxX" : 3, "bins" : 30, "blind" : [4,None], "condition" : "Muons_passCorrJetIso15 == 0 && Jets[Muons_closestJet].Pt() > 15 && Jets[Muons_closestJet].Pt() < 30"},# "customBins"  : [0,2,4,6,10,12] },
    ]
    normalise = False
    

class dilepton_muons_bg_isocr_sm_wjets(dilepton_muons_bg_isocr_sm):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_sm_wjets.root"
    choose_bg_files = True
    choose_bg_files_list = ["WJetsToLNu"]
    
class dilepton_muons_bg_isocr_sm_ttjets(dilepton_muons_bg_isocr_sm_wjets):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_sm_ttjets.root"
    choose_bg_files_list = ["TTJets"]
    
class dilepton_muons_bg_isocr_sm_dy(dilepton_muons_bg_isocr_sm_wjets):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_sm_dy.root"
    choose_bg_files_list = ["DYJetsToLL"]

class dilepton_muons_bg_isocr_sm_zjets(dilepton_muons_bg_isocr_sm_wjets):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_sm_zjets.root"
    choose_bg_files_list = ["ZJetsToNuNu"]

class dilepton_muons_bg_isocr_sm_rare(dilepton_muons_bg_isocr_sm_wjets):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_sm_rare.root"
    choose_bg_files_list = ["Rare"]

class dilepton_muons_bg_isocr_sm_diboson(dilepton_muons_bg_isocr_sm_wjets):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_isocr_sm_diboson.root"
    choose_bg_files_list = ["DiBoson"]

class dilepton_muons_bg_cleaned_ratio_sc_subtracted(dilepton_muons_bg_cleaned_ratio):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_cleaned_ratio_sc_subtracted.root"
    subtract_same_charge = True
    

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised(dilepton_muons_bg_cleaned_ratio_sc_subtracted):
    normalise = True
    normalise_integral_positive_only = True

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_retag(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_retag.root"
    
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
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_retag_no_weights.root"


class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_no_weights(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised):
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
    }
    calculatedLumi = {
        'MET' : 0.001,
    }
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_no_weights.root"

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse.root"
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None], "customBins"  : [0,2,3.0,3.2,4,6,10,12]},
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1], "customBins"  : [-1,-0.4,0,0.1,0.2,1]},
    ]

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag.root"
    
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
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights.root"

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights):
    bgReTagging = bgReTaggingCollectedNoTauTau

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau_dy(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau):
    choose_bg_files = True
    choose_bg_files_list = ["DYJetsToLL"]
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau_dy.root"

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau_zj(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau):
    choose_bg_files = True
    choose_bg_files_list = ["ZJetsToNuNu"]
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau_zj.root"

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_fine_retag_no_weights_no_tautau_zj(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau_zj):
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_retag_no_weights_no_tautau_zj_fine.root"
    histograms_defs = [
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None]},# "customBins"  : [0,2,4,6,10,12] },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1]},# "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
    ]

class dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_no_weights(dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse):
    weightString = {
        'SingleMuon' : "1",
    }
    calculatedLumi = {
        'SingleMuon' : 0.001,
    }
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_bg_cleaned_ratio_sc_subtracted_normalised_coarse_no_weights.root"
    cuts = [
        {"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        {"name":"no-tau-tau", "title": "no-tau-tau", "condition" : "((!tautau) && twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT > 0.1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3))", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
    ]

class clean_dy_sim_data_comparison(BaseParams):

    histrograms_file = BaseParams.histograms_root_files_dir + "/clean_dy_sim_data_comparison.root"
    
    save_histrograms_to_file = True
    load_histrograms_from_file = False 
    
    # weightString = {
#         'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
#     }
    
    weightString = {
        'SingleMuon' : "Weight * passedSingleMuPack * puWeight",
    }
    
    calculatedLumi = {
        'SingleMuon' : 35.000022662,
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
        #{"name":"none", "title": "None", "condition" : "(twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        {"name":"none", "title": "None", "condition" : "DYMuonsInvMass > 1"},
        {"name":"high-met", "title": "high-met", "condition" : "DYMuonsInvMass > 1 && (MHT >= 220 &&  MET >= 200)"},
        {"name":"two-mu", "title": "two-mu", "condition" : "DYMuonsInvMass > 1 && (twoLeptons == 1 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"},
        {"name":"mumu", "title": "\mu\mu", "condition" : "DYMuonsInvMass > 1 && (twoLeptons == 1 && MHT >= 220 &&  MET >= 200 && @leptons.size() == 2 && leptonFlavour == \"Muons\" && invMass < 12 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0)", "baseline" : "sameSign == 0", "sc" : "sameSign == 1"}
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
        { "obs" : "invMass", "minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None], "customBins"  : [0,2,2.8,3.2,4,6,10,12], "scale" : "width" },
        { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 6, "blind" : [None,0.1], "customBins"  : [-1,-0.4,0,0.1,0.2,1] },
        #{ "obs" : "MET:DYMuonsSum.Pt()", "minX" : 0, "maxX" : 500, "bins" : 100, "minY" : 0, "maxY" : 100, "binsY" : 100, "2D" : True, "plotStr" : "colz"},
    ]
    
    bg_retag = False
    
    bgReTagging = bgReTaggingFull
    bgReTaggingOrder = bgReTaggingOrderFull
    bgReTaggingNames = bgReTaggingNamesFull
    
    plot_kind = "SingleMuon"

class clean_dy_sim_bg(clean_dy_sim_data_comparison):
    histrograms_file = BaseParams.histograms_root_files_dir + "/clean_dy_sim_bg.root"
    histograms_defs = [
        { "obs" : "MET:DYMuonsSum.Pt()", "minX" : 0, "maxX" : 500, "bins" : 100, "minY" : 0, "maxY" : 500, "binsY" : 100, "2D" : True, "plotStr" : "colz"},
        { "obs" : "MET:OrigMET", "minX" : 0, "maxX" : 500, "bins" : 100, "minY" : 0, "maxY" : 500, "binsY" : 100, "2D" : True, "plotStr" : "colz"},
        { "obs" : "HT:OrigHT", "minX" : 0, "maxX" : 500, "bins" : 100, "minY" : 0, "maxY" : 500, "binsY" : 100, "2D" : True, "plotStr" : "colz"},
        { "obs" : "MHT:OrigMHT", "minX" : 0, "maxX" : 500, "bins" : 100, "minY" : 0, "maxY" : 500, "binsY" : 100, "2D" : True, "plotStr" : "colz"},
    ]
    solid_bg = True
    plot_data = False
    weightString = {
        'SingleMuon' : "1",
    }
    calculatedLumi = {
        'SingleMuon' : 0.001,
    }
    plot_kind = "SingleMuon"
    plot_ratio = False
    
    save_histrograms_to_file = True
    load_histrograms_from_file = False

class clean_dy_flat_obs(clean_dy_sim_bg):
    solid_bg = False
    histograms_defs = [
        { "obs" : "madHT", "minX" : 0, "maxX" : 1000, "bins" : 100 },
        { "obs" : "OrigMET", "minX" : 0, "maxX" : 1000, "bins" : 100 },
        { "obs" : "MET", "minX" : 0, "maxX" : 1000, "bins" : 100 },
        { "obs" : "OrigHT", "minX" : 0, "maxX" : 1000, "bins" : 100 },
        { "obs" : "HT", "minX" : 0, "maxX" : 1000, "bins" : 100 },
        { "obs" : "OrigMHT", "minX" : 0, "maxX" : 1000, "bins" : 100 },
        { "obs" : "MHT", "minX" : 0, "maxX" : 1000, "bins" : 100 },
    ]
    histrograms_file = BaseParams.histograms_root_files_dir + "/clean_dy_flat_obs.root"
    weightString = {
        'SingleMuon' : "Weight",
    }
    calculatedLumi = {
        'SingleMuon' : 36.00,
    }