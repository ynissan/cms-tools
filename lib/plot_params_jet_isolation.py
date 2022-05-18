import sys
import os

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))

import crystal_ball_params
import utils

from plot_params_base import *
from plot_params_bg import *
from plot_params_jpsi import *
from plot_params_leptons import *

calculatedLumi = {
        'MET' : 35.350177774,
        'SingleMuon' : 22.143021976
}

bgReTagging = {
    "tautau" : "tautau",
    "sc" : "sc * (!tautau)",
    "tc" : "tc * (!tautau)",
    "rf" : "rf",
    "ff" : "ff"
}

bgReTaggingOrder = {
    "tautau" : 0,
    "sc" : 2,
    "tc" : 3,
    "rf" : 4,
    "ff" : 1
}

bgReTagging = {
    #"tautau" : "tautau",
    "tc" : "tc * (!tautau)",
    #"fake" : "(rf || ff)",
}

bgReTaggingOrder = {
    "tautau" : 0,
    "rr" : 1,
    "tc" : 3,
    "fake" : 2
}

# bgReTagging = {
#     "tcmuons" : "tc * (!tautau)",
#     "tctautau" : "tc * tautau",
#     "other" : "other * (!tautau) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)",
#     "tautau" : "tautau * (!tc) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)",
#     "omega" : "omega",
#     "rho" : "rho_0",
#     "eta" : "eta",
#     "phi" : "phi",
#     "etaprime" : "eta_prime",
#     "jpsi" : "j_psi",
#     "upsilon1" : "upsilon_1",
#     "upsilon2" : "upsilon_2",
#     #"tc" : "tc",
#     "nbody" : "n_body",
#     "sc" : "sc * (!tautau) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)"
# 
#     # "tautau" : "tautau",
# #     "n_body" : "n_body",
# #     
# #     "sc" : "sc * (!tautau)"
# }
# 
bgReTagging = {
    #"tcmuons" : "tc * (!tautau)",
    #"tctautau" : "tc * tautau",
#    "other" : "other * (!tautau) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)",
    #"tautau" : "tautau * (!tc) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)",
    "omega" : "omega",
    "rho" : "rho_0",
    "eta" : "eta",
    "phi" : "phi",
    "etaprime" : "eta_prime",
    "jpsi" : "j_psi",
    "upsilon1" : "upsilon_1",
    "upsilon2" : "upsilon_2",
    #"tc" : "tc",
    "nbody" : "n_body",
    "scother" : "sc * (!tautau) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)"

    # "tautau" : "tautau",
#     "n_body" : "n_body",
#     
#     "sc" : "sc * (!tautau)"
}

bgReTaggingOrder = {
#    "tcmuons" : -4,
#    "tctautau" : -3,
#    "tautau" : -2,
    "other" : -1,
    "omega" : 0,
    "rho" : 1,
    "eta" : 2,
    "phi" : 3,
    "etaprime" : 4,
    "jpsi" : 5,
    "upsilon1" : 6,
    "upsilon2" : 7,
    #"tc" : 8,
    "nbody" : 9,
    "scother" : 10


    # "tautau" : 0,
#     "sc" : 1,
}

bgReTagging = {
    "tautau" : "tautau",
    "sc" : "sc * (!tautau)",
    "tc_btag_veto" : "(BTagsDeepMedium == 0) * (tc || other) * (!tautau) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)",
    "tc_2_btags" : "(BTagsDeepMedium == 2) * (tc || other) * (!tautau) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)",
    "fake" : "(rf || ff)",
    "other_sc": "other * (!tautau) * (omega || rho_0 || eta || phi || eta_prime || j_psi || upsilon_1 || upsilon_2)",
    "other_no_sc" : "other * (!tautau) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)",
    "n_body" : "n_body * (!tautau)"
}

bgReTaggingOrder = {
    "tc_btag_veto" : 0, 
    "tc_2_btags" : 1
}

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

bgReTaggingOrderFull = {
#    "tcmuons" : -4,
#    "tctautau" : -3,
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


    # "tautau" : 0,
#     "sc" : 1,
}

bgReTaggingJPsi = {
    "tc" : "tc && !tautau",
    "tautau" : "tautau",
    "other" : "other && (!tautau) && (!omega) && (!rho_0) && (!eta) && (!phi) && (!eta_prime) && (!j_psi) && (!upsilon_1) && (!upsilon_2)",
    "jpsi" : "j_psi",
    "nbody" : "n_body && (!tautau)",
    "scother" : "sc && (!tautau) && (!omega) && (!rho_0) && (!eta) && (!phi) && (!eta_prime) && (!j_psi) && (!upsilon_1) && (!upsilon_2)",
    "fake" : "rf || ff",
}

histograms_defsss = [
    #Z PEAK
#     { "obs" : "invMass", "minX" : 91.19 - 10.0, "maxX" : 91.19 + 10.0, "bins" : 30 },
#     { "obs" : "Met", "minX" : 0, "maxX" : 200, "bins" : 200 },
#     { "obs" : "Mht", "minX" : 0, "maxX" : 200, "bins" : 200 },
#     { "obs" : "Ht", "minX" : 0, "maxX" : 200, "bins" : 200 },    
#     { "obs" : "Mt2", "minX" : 0, "maxX" : 100, "bins" : 200 },
#     { "obs" : "Muons[0].Pt()", "minX" : 0, "maxX" : 300, "bins" : 300 },
#     { "obs" : "NJets", "minX" : 0, "maxX" : 7, "bins" : 7 },
    
    
    #DY
    #{ "obs" : "DYMuonsInvMass", "minX" : 0, "maxX" : 150, "bins" : 30, "units" : "GeV" },
    #{ "obs" : "DYMuons[0].Pt()", "minX" : 30, "maxX" : 100, "bins" : 30 },
    #{ "obs" : "DYMuons[1].Pt()", "minX" : 15, "maxX" : 100, "bins" : 30 },
    
    #NORMAL
    { "obs" : "invMass", "units" : "M_{ll}", "minX" : 0.1, "maxX" : 13, "bins" : 30 },
    { "obs" : 'int(leptonFlavour == "Muons")', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30 },
    { "obs" : "dilepBDT", "units" : "BDT output", "minX" : 0.1, "maxX" : 0.8, "bins" : 30 },
    { "obs" : "Electrons.Pt()", "minX" : 0, "maxX" : 50, "bins" : 50 },
    { "obs" : "Muons.Pt()", "minX" : 0, "maxX" : 50, "bins" : 50 },

     
     { "obs" : 'int(vetoElectronsPassIso)', "minX" : 0, "maxX" : 2, "bins" : 2},
     { "obs" : 'int(vetoElectronsPassJetIso)', "minX" : 0, "maxX" : 2, "bins" : 2},
     { "obs" : 'int(vetoElectronsMediumID)', "minX" : 0, "maxX" : 2, "bins" : 2},
     { "obs" : 'int(vetoElectronsTightID)', "minX" : 0, "maxX" : 2, "bins" : 2},
     
     { "obs" : 'int(vetoMuonsPassIso)', "minX" : 0, "maxX" : 2, "bins" : 2},
     { "obs" : 'int(vetoMuonsPassJetIso)', "minX" : 0, "maxX" : 2, "bins" : 2},
     { "obs" : 'int(vetoMuonsMediumID)', "minX" : 0, "maxX" : 2, "bins" : 2},
     { "obs" : 'int(vetoMuonsTightID)', "minX" : 0, "maxX" : 2, "bins" : 2},


     #{ "obs" : "abs(leptonParentPdgId)", "minX" : 0, "maxX" : 30, "bins" : 30 },
     #{ "obs" : "abs(trackParentPdgId)", "minX" : 0, "maxX" : 30, "bins" : 30 },
#     
    
    #DILEPTON
    
    
    #{ "obs" : "mw", "minX" : 0, "maxX" : 150, "bins" : 50, "func" : mw },
    #{ "obs" : "invMass2", "minX" : 0, "maxX" : 15, "bins" : 90, "func" : mw2 },   
]

common_histograms = [
    { "obs" : "dileptonPt", "minX" : 0, "maxX" : 100, "bins" : 30 },
    { "obs" : "deltaPhi", "minX" : 0, "maxX" : 3.2, "bins" : 30 },
    { "obs" : "deltaEta", "minX" : 0, "maxX" : 4, "bins" : 30 },
    { "obs" : "deltaR", "minX" : 0, "maxX" : 4, "bins" : 30 },
    { "obs" : "pt3", "minX" : 0, "maxX" : 1000, "bins" : 30 },
    { "obs" : "Ht", "minX" : 0, "maxX" : 700, "bins" : 30 },
    { "obs" : "mtautau", "minX" : 0, "maxX" : 200, "bins" : 30 },
    { "obs" : "mt1", "minX" : 0, "maxX" : 200, "bins" : 30 },
    { "obs" : "mt2", "minX" : 0, "maxX" : 200, "bins" : 30 },
    { "obs" : "deltaEtaLeadingJetDilepton", "minX" : 0, "maxX" : 4, "bins" : 30 },
    { "obs" : "deltaPhiLeadingJetDilepton", "minX" : 0, "maxX" : 4, "bins" : 30 },
    { "obs" : "dilepHt", "minX" : 0, "maxX" : 400, "bins" : 30 },
    { "obs" : "NJets", "minX" : 0, "maxX" : 7, "bins" : 7 },
    { "obs" : "BTagsLoose", "minX" : 0, "maxX" : 7, "bins" : 7 },
    { "obs" : "BTagsMedium", "minX" : 0, "maxX" : 7, "bins" : 7 },
    { "obs" : "BTagsDeepLoose", "minX" : 0, "maxX" : 7, "bins" : 7 },
    { "obs" : "BTagsDeepMedium", "minX" : 0, "maxX" : 7, "bins" : 7 },
    { "obs" : "Met", "minX" : 0, "maxX" : 2000, "bins" : 30 },
    { "obs" : "Mht", "minX" : 0, "maxX" : 700, "bins" : 30 },
    { "obs" : "Ht", "minX" : 0, "maxX" : 700, "bins" : 30 },
    { "obs" : "LeadingJetQgLikelihood", "minX" : 0, "maxX" : 1, "bins" : 30 },
    { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 4, "bins" : 30 },
    { "obs" : "MinDeltaPhiMetJets", "minX" : 0, "maxX" : 4, "bins" : 30 },
    { "obs" : "Mt2", "minX" : 0, "maxX" : 100, "bins" : 30 },
    { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 800, "bins" : 30 },
    { "obs" : "abs(LeadingJet.Eta())", "minX" : 0, "maxX" : 4, "bins" : 30 },
    { "obs" : "MaxCsv25", "minX" : 0, "maxX" : 1, "bins" : 30 },
    { "obs" : "MaxDeepCsv25", "minX" : 0, "maxX" : 1, "bins" : 30 },
    { "obs" : "LeadingJetMinDeltaRElectrons", "minX" : 0, "maxX" : 5, "bins" : 30 },
    { "obs" : "LeadingJetMinDeltaRMuons", "minX" : 0, "maxX" : 5, "bins" : 30 },
]

two_leps_histograms = [
    { "obs" : "leptons[0].Pt()", "minX" : 2, "maxX" : 30, "bins" : 60 },
    { "obs" : "leptons[1].Pt()", "minX" : 2, "maxX" : 30, "bins" : 60 },
    { "obs" : "abs(leptons[0].Eta())", "minX" : 0, "maxX" : 3, "bins" : 60 },
    { "obs" : "abs(leptons[1].Eta())", "minX" : 0, "maxX" : 3, "bins" : 60 },
    { "obs" : "deltaPhiMetLepton1", "minX" : 0, "maxX" : 3.5, "bins" : 30 },
    { "obs" : "deltaPhiMetLepton2", "minX" : 0, "maxX" : 3.5, "bins" : 30 },
    { "obs" : "leptons_ParentPdgId[0]", "minX" : 0, "maxX" : 40, "bins" : 40 },
    { "obs" : "leptons_ParentPdgId[1]", "minX" : 0, "maxX" : 40, "bins" : 40 },
    
    { "obs" : "Electrons_minDeltaRJets[leptonsIdx[0]]", "minX" : 0, "maxX" : 1, "bins" : 60 },
    { "obs" : "Electrons_minDeltaRJets[leptonsIdx[1]]", "minX" : 0, "maxX" : 1, "bins" : 60 },
    
    { "obs" : "Muons_minDeltaRJets[leptonsIdx[0]]", "minX" : 0, "maxX" : 1, "bins" : 60 },
    { "obs" : "Muons_minDeltaRJets[leptonsIdx[1]]", "minX" : 0, "maxX" : 1, "bins" : 60 },
    
    { "obs" : "Electrons_deltaRLJ[leptonsIdx[0]]", "minX" : 0, "maxX" : 1, "bins" : 60 },
    { "obs" : "Electrons_deltaRLJ[leptonsIdx[1]]", "minX" : 0, "maxX" : 1, "bins" : 60 },
    
    { "obs" : "Muons_deltaRLJ[leptonsIdx[0]]", "minX" : 0, "maxX" : 1, "bins" : 60 },
    { "obs" : "Muons_deltaRLJ[leptonsIdx[1]]", "minX" : 0, "maxX" : 1, "bins" : 60 },
    
    { "obs" : "Electrons_deltaEtaLJ[leptonsIdx[0]]", "minX" : 0, "maxX" : 1, "bins" : 60 },
    { "obs" : "Electrons_deltaEtaLJ[leptonsIdx[1]]", "minX" : 0, "maxX" : 1, "bins" : 60 },
    
    { "obs" : "Muons_deltaEtaLJ[leptonsIdx[0]]", "minX" : 0, "maxX" : 1, "bins" : 60 },
    { "obs" : "Muons_deltaEtaLJ[leptonsIdx[1]]", "minX" : 0, "maxX" : 1, "bins" : 60 },

]

two_leps_cuts = [
        #{"name":"invMass_Muons", "title": "invMass - Muons", "condition" : "Met >= 200 && invMass < 12  && invMass > 0.4 && leptonFlavour == \"Muons\""},
        #{"name":"invMass_Electrons", "title": "invMass - Electrons", "condition" : "Met >= 200 && invMass < 12  && invMass > 0.4 && leptonFlavour == \"Electrons\""},
        
        #{"name":"real", "title": "real", "condition" : "Met >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && !(invMass > 0.95 && invMass < 1.06)"},
        
        #{"name":"dilepBDT", "title": "dilepBDT", "condition" : "Met >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && !(invMass > 0.95 && invMass < 1.06) && dilepBDT > 0.1"},
        #{"name":"noBDT", "title": "noBDT", "condition" : "BTagsDeepMedium == 0 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && Mht >= 220 &&  Met >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81)"},
        #{"name":"orthSOS", "title": "orthSOS", "condition" : "BTagsDeepMedium == 0 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && Mht >= 220 &&  Met >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1"},
        
        #{"name":"noBVeto_Electrons", "title": "noBVeto - Electrons", "condition" : "(leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && Mht >= 220 &&  Met >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && vetoElectronsTightID == 0 && vetoMuonsPassJetIso == 0 && leptonFlavour == \"Electrons\""},
        #{"name":"noBVeto_Muons", "title": "noBVeto - Muons", "condition" : "(leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && Mht >= 220 &&  Met >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && vetoElectronsTightID == 0 && vetoMuonsPassJetIso == 0 && leptonFlavour == \"Muons\""},
        
        
        #{"name":"orthSOS-no_veto_Electrons", "title": "orthSOS no lepton veto - Electrons", "condition" : "BTagsDeepMedium == 0 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && Mht >= 220 &&  Met >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && leptonFlavour == \"Electrons\""},
        #{"name":"orthSOS-no_veto_Muons", "title": "orthSOS no lepton veto - Muons", "condition" : "BTagsDeepMedium == 0 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && Mht >= 220 &&  Met >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && leptonFlavour == \"Muons\""},
        
        
        {"name":"orthSOS-veto_Electrons", "title": "orthSOS lepton veto - Electrons", "condition" : "vetoElectronsTightID == 0 && vetoMuonsPassIso == 0 && BTagsDeepMedium == 0 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && Mht >= 220 &&  Met >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && leptonFlavour == \"Electrons\""},
        {"name":"orthSOS-veto_Muons", "title": "orthSOS lepton veto - Muons", "condition" : "vetoElectronsTightID == 0 && vetoMuonsPassIso == 0 && BTagsDeepMedium == 0 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && Mht >= 220 &&  Met >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && leptonFlavour == \"Muons\""},
        
        {"name":"veto_Electrons", "title": "lepton veto - Electrons", "condition" : "vetoElectronsTightID == 0 && vetoMuonsPassIso == 0 && BTagsDeepMedium == 0 && Mht >= 220 &&  Met >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && leptonFlavour == \"Electrons\""},
        {"name":"veto_Muons", "title": "lepton veto - Muons", "condition" : "vetoElectronsTightID == 0 && vetoMuonsPassIso == 0 && BTagsDeepMedium == 0 && Mht >= 220 &&  Met >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && leptonFlavour == \"Muons\""},
        
        
        #{"name":"tc", "title": "tc", "condition" : 'Met >= 200 && invMass < 30 && leptonFlavour == "Muons" && tc * (!tautau)'},
        #{"name":"tautau", "title": "tautau", "condition" : '(Met >= 200 && invMass < 30 && leptonFlavour == "Muons") * (tautau)'},
        #{"name":"scother", "title": "scother", "condition" : 'Met >= 200 && invMass < 30 && leptonFlavour == "Muons" && sc * (!tautau) * (!omega) * (!rho_0) * (!eta) * (!phi) * (!eta_prime) * (!j_psi) * (!upsilon_1) * (!upsilon_2)'},
        
        # {"name":"dilepBDT", "title": "dilepBDT", "condition" : 'Met >= 200 && invMass < 30 && leptonFlavour == "Muons" && dilepBDT > 0.2'},
#         {"name":"lowMet", "title": "lowMet", "condition" : 'Met <= 200 && invMass < 30 && leptonFlavour == "Muons"'},
#         {"name":"lowMetBDT", "title": "lowMetBDT", "condition" : 'Met <= 200 && invMass < 30 && leptonFlavour == "Muons" && dilepBDT > 0'},
        
        
        # {"name":"parent_100-250", "title": "parent 100-250", "condition" : "Met >= 200 && invMass < 30 && leptons_ParentPdgId[0] > 100 && leptons_ParentPdgId[0] < 250"},
#         {"name":"parent_300-350", "title": "parent 300-350", "condition" : "Met >= 200 && invMass < 30 && leptons_ParentPdgId[0] > 300 && leptons_ParentPdgId[0] < 350"},
#         {"name":"parent_400-450", "title": "parent 400-450", "condition" : "Met >= 200 && invMass < 30 && leptons_ParentPdgId[0] > 400 && leptons_ParentPdgId[0] < 450"},
#          {"name":"parent_500-600", "title": "parent 500-600", "condition" : "Met >= 200 && invMass < 30 && leptons_ParentPdgId[0] > 500 && leptons_ParentPdgId[0] < 600"},
#          {"name":"parent_600", "title": "parent >600", "condition" : "Met >= 200 && invMass < 30 && leptons_ParentPdgId[0] > 600"},
#         
]

ex_track_histograms = [
    #     #TRACK ONLY
    { "obs" : "trackBDT", "minX" : -0.7, "maxX" : 0.7, "bins" : 30 },
    { "obs" : "secondTrackBDT", "minX" : -1, "maxX" : 1, "bins" : 30 },
    { "obs" : "abs(track.Eta())", "minX" : 0, "maxX" : 3, "bins" : 60 },
    { "obs" : "abs(lepton.Eta())", "minX" : 0, "maxX" : 3, "bins" : 60 },
    { "obs" : "track.Pt()", "minX" : 0, "maxX" : 30, "bins" : 60 },
    { "obs" : "lepton.Pt()", "minX" : 2, "maxX" : 25, "bins" : 60 },
    { "obs" : "secondTrack.Pt()", "minX" : 0, "maxX" : 30, "bins" : 60 },
    { "obs" : "abs(secondTrack.Eta())", "minX" : 0, "maxX" : 3, "bins" : 60 },
    { "obs" : "abs(track.Phi())", "minX" : 0, "maxX" : 6, "bins" : 60 },
    { "obs" : "abs(lepton.Phi())", "minX" : 0, "maxX" : 6, "bins" : 60 },
    { "obs" : "mtl", "minX" : 0, "maxX" : 200, "bins" : 30 },
    { "obs" : "mtt", "minX" : 0, "maxX" : 200, "bins" : 30 },
    { "obs" : "NTracks", "minX" : 0, "maxX" : 7, "bins" : 7 },
]

ex_track_cuts = [
        {"name":"dilepBDT", "title": "dilepBDT", "condition" : "secondTrack.Pt() < 12 && lepton.Pt() < 18 && track.Pt() < 15 && abs(lepton.Eta()) < 2.4 && deltaEta < 2.5 && mt1 < 120 && dilepHt > 130 && deltaR > 0.25 &&  deltaR < 3 && dilepBDT > 0.1 && Met >= 200 && invMass < 30 && dileptonPt < 30"},
]

signals = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm0p86Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm1p92Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm3p28Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm9p73Chi20Chipm.root"
              ]

signalNames = [
    "\Delta_{}M 0.8Gev",
    "\Delta_{}M 1.9Gev",
    "\Delta_{}M 3.2Gev",
    "\Delta_{}M 9.7Gev",
]


class lepton_selection(BaseParams):
    signal_dir = [
              #"/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm0p86Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm1p92Chi20Chipm.root",
              #"/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm3p28Chi20Chipm.root",
              #"/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm9p73Chi20Chipm.root"
              ]
    
    plot_bg = False
    plot_data = False
    plot_overflow = True
    object_retag = True
    
    sig_line_width = 1

    legend_coordinates = {"x1" : .75, "y1" : .75, "x2" : .89, "y2" : .89}
    legend_columns = 1
    legend_border = 1
    
    cuts = [
        {"name":"none", "title": "No Cuts", "condition" : "1", "object" : {"e" : "Electrons.Pt() < 20", "m" : "Muons.Pt() > 2 && Muons.Pt() < 20"  }},
        {"name":"no_iso", "title": "no_iso", "condition": "1", "object" : {"e" : "Electrons_deltaRLJ > 0.4 && Electrons.Pt() < 20", "m" : "Muons.Pt() < 20 && Muons.Pt() > 2 && Muons_deltaRLJ > 0.4 && Muons_mediumID == 1 "  }},
    ]
    
    histograms_defs = [
        {"obs" : "Electrons_pt", "formula" : "abs(Electrons.Pt())", "units" : "e p_{T}", "bins" : 60, "minX" : 5, "maxX" : 20, "object" : "e" },
        {"obs" : "Electrons_eta", "formula" : "abs(Electrons.Eta())", "units" : "|\eta|_{e}", "bins" : 50, "minX" : 0, "maxX" : 2.5, "object" : "e" },
        {"obs" : "Electrons_rlj", "formula" : "Electrons_deltaRLJ", "units" : "\Delta_{}R(j_{1}, e)", "bins" : 50, "minX" : 0, "maxX" : 5, "object" : "e" },
        
        { "obs" : "Electrons_pt_barrel", "formula" : "Electrons.Pt()", "units" : "barrel e p_{T}", "minX" : 5, "maxX" : 20, "bins" : 60, "object" : "e", "condition" : "abs(Electrons.Eta()) < 1.2" },
        { "obs" : "Electrons_pt_endcape", "formula" : "Electrons.Pt()", "units" : "endcaps e p_{T}", "minX" : 5, "maxX" : 20, "bins" : 60, "object" : "e", "condition" : "abs(Electrons.Eta()) >= 1.2 && abs(Electrons.Eta()) <= 2.4" },
        { "obs" : "Electrons_pt_barrel_medium", "formula" : "Electrons_mediumID", "units" : "barrel e mediumID", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "e", "condition" : "abs(Electrons.Eta()) < 1.2" },
        { "obs" : "Electrons_pt_endcape_medium", "formula" : "Electrons_mediumID", "units" : "endcaps e mediumID", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "e", "condition" : "abs(Electrons.Eta()) >= 1.2 && abs(Electrons.Eta()) <= 2.4" },
        
        { "obs" : "Electrons_iso", "formula" : "Electrons_passIso", "units" : "e passIso", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "e", "condition" : "1" },
        { "obs" : "Electrons_passCorrJetIso10", "formula" : "Electrons_passCorrJetIso10", "units" : "e passCorrJetIso10", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "e", "condition" : "1" },
        
        
        { "obs" : "Muons_pt", "formula" : "abs(Muons.Pt())", "units" : "\mu p_{T}", "minX" : 2, "maxX" : 25, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2" },
        { "obs" : "Muons_Eta", "formula" : "abs(Muons.Eta())", "units" : "|\eta|_{\mu}", "minX" : 0, "maxX" : 2.4, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Pt()) >= 2" },
        { "obs" : "Muons_pt_barrel", "formula" : "Muons.Pt()", "units" : "barrel p_{T}", "minX" : 2, "maxX" : 20, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) <= 0.9" },
        { "obs" : "Muons_pt_overlap", "formula" : "Muons.Pt()", "units" : "overlap p_{T}", "minX" : 2, "maxX" : 20, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) > 0.9 && abs(Muons.Eta()) <= 1.2" },
        { "obs" : "Muons_pt_endcape", "formula" : "Muons.Pt()", "units" : "endcaps p_{T}", "minX" : 2, "maxX" : 20, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) >= 1.2 && abs(Muons.Eta()) <= 2.4" },
        
        { "obs" : "Muons_rlj_barrel", "formula" : "Muons_deltaRLJ", "units" : "barrel \Delta_{}R(j_{1}, \mu)", "minX" : 0, "maxX" : 5, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) <= 0.9" },
        { "obs" : "Muons_rlj_overlap", "formula" : "Muons_deltaRLJ", "units" : "overlap \Delta_{}R(j_{1}, \mu)", "minX" : 0, "maxX" : 5, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) > 0.9 && abs(Muons.Eta()) <= 1.2" },
        { "obs" : "Muons_rlj_endcape", "formula" : "Muons_deltaRLJ", "units" : "endcaps \Delta_{}R(j_{1}, \mu)", "minX" : 0, "maxX" : 5, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) >= 1.2 && abs(Muons.Eta()) <= 2.4" },
        

        { "obs" : "Muons_pt_barrel_medium", "formula" : "Muons_mediumID", "units" : "barrel mediumID", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) <= 0.9" },
        { "obs" : "Muons_pt_overlap_medium", "formula" : "Muons_mediumID", "units" : "overlap mediumID", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) > 0.9 && abs(Muons.Eta()) <= 1.2" },
        { "obs" : "Muons_pt_endcape_medium", "formula" : "Muons_mediumID", "units" : "endcaps mediumID", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) >= 1.2 && abs(Muons.Eta()) <= 2.4" },
        
        { "obs" : "Muons_pt_barrel_jet_iso", "formula" : "Muons_passCorrJetIso10", "units" : "barrel \mu passCorrJetIso10", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) <= 0.9" },
        { "obs" : "Muons_pt_overlap_jet_iso", "formula" : "Muons_passCorrJetIso10", "units" : "overlap \mu passCorrJetIso10", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) > 0.9 && abs(Muons.Eta()) <= 1.2" },
        { "obs" : "Muons_pt_endcape_jet_iso", "formula" : "Muons_passCorrJetIso10", "units" : "endcaps \mu passCorrJetIso10", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) >= 1.2 && abs(Muons.Eta()) <= 2.4" },
        
        { "obs" : "Muons_pt_barrel_iso", "formula" : "Muons_passIso", "units" : "barrel \mu passIso", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) <= 0.9" },
        { "obs" : "Muons_pt_overlap_iso", "formula" : "Muons_passIso", "units" : "overlap \mu passIso", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) > 0.9 && abs(Muons.Eta()) <= 1.2" },
        { "obs" : "Muons_pt_endcape_iso", "formula" : "Muons_passIso", "units" : "endcaps \mu passIso", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) >= 1.2 && abs(Muons.Eta()) <= 2.4" },
        
    ]
    
    lepConds = {
        "e" : { "Zl" : "Electrons_matchGen == 1",
                "MM" : "Electrons_matchGen == 0"},
        "m" : { "Zl" : "Muons_matchGen == 1",
                "MM" : "Muons_matchGen == 0"},
    }

    object_retag_map = {
        "e" : [ 
                {"MM" : "Electrons_isZ == 0"},
                {"Zl" : "Electrons_isZ == 1"}],
        "m" : [ {"MM" : "Muons_isZ == 0"},
                {"Zl" : "Muons_isZ == 1"}],
    }
    
    weightString = {
        'MET' : "1",
        'SingleMuon' : "1"
    }
    
    calculatedLumi = {
        'MET' : 0.001,
        'SingleMuon' : 0.001,
    }

class track_selection(lepton_selection):
    cuts = [
        {"name":"none", "title": "No Cuts", "condition" : "tracks.Pt() < 10"},
        {"name":"dxyz", "title": "dxyz", "condition" : "tracks.Pt() < 10 && tracks_dxyVtx < 0.02 && tracks_dzVtx < 0.02"},
        
    ]
    
    histograms_defs = [
        {"obs" : "tracks.Pt()", "bins" : 50, "minX" : 1.9, "maxX" : 10, "object" : "t" },
        {"obs" : "Pt tracks_trackJetIso", "formula" : "tracks.Pt()", "bins" : 50, "minX" : 1.9, "maxX" : 10, "object" : "t", "condition" :  "tracks_passCorrJetIso5 == 1" },
        {"obs" : "abs(tracks.Eta())", "bins" : 50, "minX" : 0, "maxX" : 3, "object" : "t" },
        #{"obs" : "Pt tracks_trackJetIso", "formula" : "tracks.Pt()", "bins" : 50, "minX" : 1.9, "maxX" : 20, "object" : "t", "condition" :  "tracks_passCorrJetIso5 == 1" },
        
        {"obs" : "tracks_matchedCaloEnergy", "bins" : 50, "minX" : 0, "maxX" : 50, "object" : "t" },
        {"obs" : "tracks_nMissingOuterHits", "bins" : 13, "minX" : 0, "maxX" : 13, "object" : "t" },
        {"obs" : "tracks_nMissingMiddleHits", "bins" : 3, "minX" : 0, "maxX" : 3, "object" : "t" },
        {"obs" : "tracks_chi2perNdof", "bins" : 50, "minX" : 0, "maxX" : 20, "object" : "t" },
        {"obs" : "tracks_trackerLayersWithMeasurement", "bins" : 19, "minX" : 0, "maxX" : 19, "object" : "t" },
        {"obs" : "tracks_trackQualityGoodIterative", "bins" : 2, "minX" : 0, "maxX" : 2, "object" : "t" },
        {"obs" : "tracks_trkRelIso", "bins" : 50, "minX" : 0, "maxX" : 0.2, "object" : "t" },
        {"obs" : "tracks_trkMiniRelIso", "bins" : 50, "minX" : 0, "maxX" : 0.0002, "object" : "t" },
        {"obs" : "tracks_nValidPixelHits", "bins" : 8, "minX" : 0, "maxX" : 8, "object" : "t" },
        {"obs" : "tracks_nValidTrackerHits", "bins" : 40, "minX" : 0, "maxX" : 40, "object" : "t" },
        {"obs" : "tracks_trackJetIso", "bins" : 50, "minX" : 0, "maxX" : 2, "object" : "t" },
        {"obs" : "tracks_passPFCandVeto", "bins" : 2, "minX" : 0, "maxX" : 2, "object" : "t" },
        {"obs" : "tracks_dxyVtx", "bins" : 50, "minX" : 0, "maxX" : 0.1, "object" : "t" },
        {"obs" : "tracks_dzVtx", "bins" : 50, "minX" : 0, "maxX" : 0.1, "object" : "t" },
        {"obs" : "tracks_pixelLayersWithMeasurement", "bins" : 5, "minX" : 0, "maxX" : 5, "object" : "t" },
        {"obs" : "tracks_minDrLepton", "bins" : 50, "minX" : 0, "maxX" : 10, "object" : "t" },
        {"obs" : "tracks_deltaRLJ", "bins" : 50, "minX" : 0, "maxX" : 5, "object" : "t" },
        {"obs" : "tracks_correctedMinDeltaRJets", "bins" : 50, "minX" : 0, "maxX" : 1, "object" : "t" },
        {"obs" : "tracks_minDeltaRJets", "bins" : 50, "minX" : 0, "maxX" : 1, "object" : "t" },
        {"obs" : "tracks_deltaEtaLJ", "bins" : 50, "minX" : 0, "maxX" : 1, "object" : "t" },
        {"obs" : "tracks_matchedCaloEnergyJets", "bins" : 50, "minX" : 0, "maxX" : 3, "object" : "t" },
        {"obs" : "tracks_nMissingOuterHits", "bins" : 14, "minX" : 0, "maxX" : 14, "object" : "t" },
        {"obs" : "tracks_matchedCaloEnergy", "bins" : 50, "minX" : 0, "maxX" : 100, "object" : "t" },
        
    ]
    
    object_retag_map = {
        "t" : [ 
                {"MM" : "tracks_isZ == 0"},
                {"exZl" : "tracks_isZ == 1 && tracks_mi == -1 && tracks_ei == -1"},
                {"Zl" : "tracks_isZ == 1 && (tracks_mi != -1 || tracks_ei != -1)"},
                ],
        "m" : [ {"MM" : "Muons_isZ == 0"},
                {"Zl" : "Muons_isZ == 1"}],
    }
    
    legend_coordinates = {"x1" : .20, "y1" : .60, "x2" : .89, "y2" : .89}
    legend_columns = 2
    legend_border = 0

class jet_isolation_study(BaseParams):
    
    save_histrograms_to_file = True
    load_histrograms_from_file = True    
    
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/jetIsolationStudyHists.root"
    
    
    signal_dir = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm0p86Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm1p92Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm3p28Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm5p63Chi20Chipm.root"
              ]
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
    
    plot_bg = True
    plot_data = False
    plot_overflow = True
    object_retag = False
    
    #sig_line_width = 1

    #legend_coordinates = {"x1" : .75, "y1" : .75, "x2" : .89, "y2" : .89}
    #legend_columns = 1
    #legend_border = 1
    
    cuts = [
        {"name":"none", "title": "No Cuts", "condition" : "(MHT >= 220 &&  MET >= 200 && BTagsDeepMedium == 0)", "object" : {"e" : "1", "m" : "1"  }},
        #{"name":"no_iso", "title": "no_iso", "condition": "1", "object" : {"e" : "Electrons_deltaRLJ > 0.4 && Electrons.Pt() < 20", "m" : "Muons.Pt() < 20 && Muons.Pt() > 2 && Muons_deltaRLJ > 0.4 && Muons_mediumID == 1 "  }},
    ]

    
    histograms_defs_base = [
        { "obs" : "Muons_pt", "formula" : "abs(Muons.Pt())", "units" : "\mu p_{T}", "minX" : 2, "maxX" : 25, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2" },
        { "obs" : "Muons_Eta", "formula" : "abs(Muons.Eta())", "units" : "|\eta|_{\mu}", "minX" : 0, "maxX" : 2.4, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Pt()) >= 2" },
        { "obs" : "Muons_pt_barrel", "formula" : "Muons.Pt()", "units" : "barrel p_{T}", "minX" : 2, "maxX" : 20, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) <= 0.9" },
        { "obs" : "Muons_pt_overlap", "formula" : "Muons.Pt()", "units" : "overlap p_{T}", "minX" : 2, "maxX" : 20, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) > 0.9 && abs(Muons.Eta()) <= 1.2" },
        { "obs" : "Muons_pt_endcape", "formula" : "Muons.Pt()", "units" : "endcaps p_{T}", "minX" : 2, "maxX" : 20, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) >= 1.2 && abs(Muons.Eta()) <= 2.4" },
        
        { "obs" : "Muons_rlj_barrel", "formula" : "Muons_deltaRLJ", "units" : "barrel \Delta_{}R(j_{1}, \mu)", "minX" : 0, "maxX" : 5, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) <= 0.9" },
        { "obs" : "Muons_rlj_overlap", "formula" : "Muons_deltaRLJ", "units" : "overlap \Delta_{}R(j_{1}, \mu)", "minX" : 0, "maxX" : 5, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) > 0.9 && abs(Muons.Eta()) <= 1.2" },
        { "obs" : "Muons_rlj_endcape", "formula" : "Muons_deltaRLJ", "units" : "endcaps \Delta_{}R(j_{1}, \mu)", "minX" : 0, "maxX" : 5, "bins" : 60, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) >= 1.2 && abs(Muons.Eta()) <= 2.4" },
        
        { "obs" : "Muons_pt_barrel_medium", "formula" : "Muons_mediumID", "units" : "barrel mediumID", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) <= 0.9" },
        { "obs" : "Muons_pt_overlap_medium", "formula" : "Muons_mediumID", "units" : "overlap mediumID", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) > 0.9 && abs(Muons.Eta()) <= 1.2" },
        { "obs" : "Muons_pt_endcape_medium", "formula" : "Muons_mediumID", "units" : "endcaps mediumID", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) >= 1.2 && abs(Muons.Eta()) <= 2.4" },
        
        { "obs" : "Muons_pt_barrel_jet_iso", "formula" : "Muons_passCorrJetIso10", "units" : "barrel \mu passCorrJetIso10", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) <= 0.9" },
        { "obs" : "Muons_pt_overlap_jet_iso", "formula" : "Muons_passCorrJetIso10", "units" : "overlap \mu passCorrJetIso10", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) > 0.9 && abs(Muons.Eta()) <= 1.2" },
        { "obs" : "Muons_pt_endcape_jet_iso", "formula" : "Muons_passCorrJetIso10", "units" : "endcaps \mu passCorrJetIso10", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) >= 1.2 && abs(Muons.Eta()) <= 2.4" },
        
        { "obs" : "Muons_pt_barrel_iso", "formula" : "Muons_passIso", "units" : "barrel \mu passIso", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) <= 0.9" },
        { "obs" : "Muons_pt_overlap_iso", "formula" : "Muons_passIso", "units" : "overlap \mu passIso", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) > 0.9 && abs(Muons.Eta()) <= 1.2" },
        { "obs" : "Muons_pt_endcape_iso", "formula" : "Muons_passIso", "units" : "endcaps \mu passIso", "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : "Muons.Pt() >= 2 && abs(Muons.Eta()) >= 1.2 && abs(Muons.Eta()) <= 2.4" },
        
    ]
    
    histograms_defs = []
    
    isoStrs = []
    isoConds = {}
    
    for CorrJetObs in utils.leptonIsolationList:
            ptRanges = [""]
            if CorrJetObs == "CorrJetIso":
                 ptRanges = utils.leptonCorrJetIsoPtRange
            for ptRange in ptRanges:
                #isoStr = "_pass" + CorrJetObs + str(ptRange)
                isoStr = CorrJetObs + str(ptRange)
                isoStrs.append(isoStr)
                isoConds[isoStr] = "twoLeptons" + isoStr + " == 1 && leptonFlavour" + isoStr + " == \"Muons\" && sameSign" + isoStr + " == 0 && @leptons" + isoStr + ".size() == 2"
    
    
    for isoStr in isoStrs:
        histograms_defs.append({ "obs" : "leptons" + isoStr + ".Pt()", "units" : "\mu " + isoStr +  " p_{T}", "minX" : 2, "maxX" : 20, "bins" : 60, "object" : "m", "condition" : isoConds[isoStr] })
    for isoStr in isoStrs:
        histograms_defs.append({ "obs" : "leptons" + isoStr +"_pt_gt_20", "formula" : "Muons.Pt()", "units" : "\mu " + isoStr +  " p_{T}", "minX" : 20, "maxX" : 50, "bins" : 60, "object" : "m", "condition" : isoConds[isoStr] + " && Muons.Pt() >= 20 && Muons_pass" + isoStr + " == 1" })
    for isoStr in isoStrs:
        histograms_defs.append({ "obs" : "invMass" + isoStr, "units" : "M_{ll} " + isoStr, "minX" : 0, "maxX" : 10, "bins" : 60, "object" : "m", "condition" : isoConds[isoStr] + " && invMass" + isoStr + " < 10"})
    for isoStr in isoStrs:
        histograms_defs.append({ "obs" : "dilepBDT" + isoStr, "units" : "dilepton BDT " + isoStr , "minX" : -1, "maxX" : 1, "bins" : 60, "object" : "m", "condition" : isoConds[isoStr] })
    for isoStr in isoStrs:
        histograms_defs.append({ "obs" : "vetoMuons" + isoStr, "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "m", "condition" : isoConds[isoStr] })
    
    
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight",
    }
    
    calculatedLumi = {
        'MET' : utils.LUMINOSITY/1000.0,
        'SingleMuon' : 0.001,
    }
    
    #hist = utils.getHistogramFromTree(deltaM + "_2l_" + lep, c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio * (twoLeptons == 1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && BTagsDeepMedium == 0 && vetoElectronsTightID == 0 && vetoMuonsPassIso == 0 && @leptons.size() == 2 && leptonFlavour == \"" + lep + "\" && sameSign == 0)", True)
    #hist = utils.getHistogramFromTree(basename, c, "dilepBDT", 30, -0.6, 0.6, str(utils.LUMINOSITY) + "* passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * (twoLeptons == 1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && BTagsDeepMedium == 0 && vetoElectronsTightID == 0 && vetoMuonsPassIso == 0 && @leptons.size() == 2 && leptonFlavour == \"" + lep + "\" && sameSign == 0)", True)

class jet_isolation_study_electrons(jet_isolation_study):
    
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/jetIsolationStudyElectronsHists.root"
    
    histograms_defs = []
    
    isoStrs = []
    isoConds = {}
    
    for CorrJetObs in utils.leptonIsolationList:
            ptRanges = [""]
            if CorrJetObs == "CorrJetIso":
                 ptRanges = utils.leptonCorrJetIsoPtRange
            for ptRange in ptRanges:
                #isoStr = "_pass" + CorrJetObs + str(ptRange)
                isoStr = CorrJetObs + str(ptRange)
                isoStrs.append(isoStr)
                isoConds[isoStr] = "twoLeptons" + isoStr + " == 1 && leptonFlavour" + isoStr + " == \"Electrons\" && sameSign" + isoStr + " == 0 && @leptons" + isoStr + ".size() == 2"
    
    
    for isoStr in isoStrs:
        histograms_defs.append({ "obs" : "leptons" + isoStr + ".Pt()", "units" : "e " + isoStr +  " p_{T}", "minX" : 2, "maxX" : 20, "bins" : 60, "object" : "e", "condition" : isoConds[isoStr] })
    for isoStr in isoStrs:
        histograms_defs.append({ "obs" : "leptons" + isoStr +"_pt_gt_20", "formula" : "Electrons.Pt()", "units" : "\mu " + isoStr +  " p_{T}", "minX" : 20, "maxX" : 50, "bins" : 60, "object" : "e", "condition" : isoConds[isoStr] + " && Electrons.Pt() >= 20 && Electrons_pass" + isoStr + " == 1" })
    for isoStr in isoStrs:
        histograms_defs.append({ "obs" : "invMass" + isoStr, "units" : "M_{ll} " + isoStr, "minX" : 0, "maxX" : 10, "bins" : 60, "object" : "e", "condition" : isoConds[isoStr] + " && invMass" + isoStr + " < 10"})
    for isoStr in isoStrs:
        histograms_defs.append({ "obs" : "invMass_orth" + isoStr, "formula" : "invMass" + isoStr, "units" : "M_{ll} orth " + isoStr, "minX" : 0, "maxX" : 10, "bins" : 60, "object" : "e", "condition" : isoConds[isoStr] + " && invMass" + isoStr + " < 10 && (leptons" + isoStr + "[1].Pt() <= 3.5 || deltaR" + isoStr + " <= 0.3) "})
    for isoStr in isoStrs:
        histograms_defs.append({ "obs" : "invMass_orth_dilep" + isoStr, "formula" : "invMass" + isoStr, "units" : "M_{ll} orth dilep" + isoStr, "minX" : 0, "maxX" : 10, "bins" : 60, "object" : "e", "condition" : isoConds[isoStr] + " && invMass" + isoStr + " < 10 && dilepBDT" + isoStr + " > 0 && (leptons" + isoStr + "[1].Pt() <= 3.5 || deltaR" + isoStr + " <= 0.3) "})
    for isoStr in isoStrs:
        histograms_defs.append({ "obs" : "dilepBDT" + isoStr, "units" : "dilepton BDT " + isoStr , "minX" : -1, "maxX" : 1, "bins" : 60, "object" : "e", "condition" : isoConds[isoStr] })
    for isoStr in isoStrs:
        histograms_defs.append({ "obs" : "dilepBDT_orth" + isoStr, "formula" : "dilepBDT" + isoStr, "units" : "dilepton BDT orth " + isoStr , "minX" : -1, "maxX" : 1, "bins" : 60, "object" : "e", "condition" : isoConds[isoStr] + " && (leptons" + isoStr + "[1].Pt() <= 3.5 || deltaR" + isoStr + " <= 0.3) "})
    for isoStr in isoStrs:
        histograms_defs.append({ "obs" : "vetoElectrons" + isoStr, "minX" : 0, "maxX" : 2, "bins" : 2, "object" : "e", "condition" : isoConds[isoStr] })
   

class track_selection_bg(track_selection):
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
    #bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/bla"
    signal_dir = [
              #"/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm0p86Chi20Chipm.root",
              #"/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm1p92Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm3p28Chi20Chipm.root",
              #"/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm9p73Chi20Chipm.root"
              ]
    weightString = {
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        'SingleMuon' : "1"
    }
    calculatedLumi = {
        'MET' : utils.LUMINOSITY/1000.0,
        'SingleMuon' : 0.001,
    }
    plot_bg = True
    plot_signal = True
    plot_data = False
    plot_overflow = True
    object_retag = False

class data_jets_multiplicity_muons(BaseParams):
    save_histrograms_to_file = True
    load_histrograms_from_file = False    
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_11_3_1/src/cms-tools/analysis/scripts/data_jets_multiplicity_muons.root" 
    
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim/sum"
    plot_bg = False
    plot_data = True
    plot_signal = False
    cuts = [
        {"name":"none", "title": "None", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && isoCr%%% == 0 && sameSign%%% == 0 && dilepBDT%%% < 0)", "baseline" : "", "sc" : ""},
        #{"name":"njets", "title": "NJets > 1", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && isoCr%%% == 0 && sameSign%%% == 0 && dilepBDT%%% < 0 && && NJets > 1)", "baseline" : "", "sc" : ""},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 200 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT%%% > 0.3 && isoCr%%% == 0)", "baseline" : "sameSign%%% == 0", "sc" : "sameSign%%% == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 200 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT%%% > 0.1 && (leptons%%%[1].Pt() <= 3.5 || deltaR%%% <= 0.3) && isoCr%%% == 0)", "baseline" : "sameSign%%% == 0", "sc" : "sameSign%%% == 1"},
    ]
    histograms_defs = [                                                                                                                                                                                                                                                                                                                                                                         #{"x1" : .35, "y1" : .60, "x2" : .89, "y2" : .89}
        { "obs" : "Jets_multiplicity[Muons_closestJet]:Muons_minDeltaRJets", "units" : "Muons_minDeltaRJets", "minX" : 0, "maxX" : 0.5, "bins" : 20, "minY" : 0, "maxY" : 40, "binsY" : 20, "2D" : True, "plotStr" : "colz", "condition" : "Muons_mediumID == 1 && Muons_deltaRLJ > 0.4 && Muons_minDeltaRJets < 0.4 && Muons.Pt() > 2 && Muons.Pt() < 15", "legendCol" : 1, "legendCoor" : {"x1" : .7, "y1" : .70, "x2" : .89, "y2" : .89}},
    ]
    y_title = "Jets_multiplicity[Muons_closestJet]"
    #jetIsoStr = "CorrJetIso10.5Dr0.55"
    jetIsoStr = "NoIso"
    injectJetIsoToCuts(cuts, jetIsoStr)
    #histograms_defs = copy.deepcopy(dilepton_muons.histograms_defs)
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)
    calculatedLumi = {
        'MET' : 35.712736198,
    }
    

class bg_jets_multiplicity_muons(data_jets_multiplicity_muons):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_11_3_1/src/cms-tools/analysis/scripts/bg_jets_multiplicity_muons.root" 
    save_histrograms_to_file = True
    load_histrograms_from_file = False 
    plot_bg = True
    plot_data = False
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
    
    weightString = {
        #'MET' : "BranchingRatio * Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
        'MET' : "BranchingRatio * Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        #'MET' : "BranchingRatio * Weight",
    }
    #nostack = True
    solid_bg = True

signals = [
              #"/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/slim/higgsino_mu100_dm1p13Chi20Chipm.root",
              #"/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/slim/higgsino_mu100_dm1p47Chi20Chipm.root",
              #"/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/slim/higgsino_mu100_dm1p92Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm3p28Chi20Chipm.root",
              #"/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/slim/higgsino_mu100_dm4p30Chi20Chipm.root"
              ]

signalNames = [
    #"\Delta_{}M 1.13 Gev",
    #"\Delta_{}M 1.47 Gev",
    #"\Delta_{}M 1.9 Gev",
    "\Delta_{}M 3.2 Gev",
    #"\Delta_{}M 4.3 Gev",
]

class signal_jets_multiplicity_muons(bg_jets_multiplicity_muons):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_11_3_1/src/cms-tools/analysis/scripts/histograms_root_files/signal_jets_multiplicity_muons.root" 
    save_histrograms_to_file = True
    load_histrograms_from_file = False 
    plot_bg = False
    plot_data = False
    plot_signal = True
   
    signal_dir = signals
    signal_names = signalNames
   