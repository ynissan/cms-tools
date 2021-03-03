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

class BaseParams:
    signal_dir = None
    signal_names = None
    bg_dir = None
    data_dir = None
    sc_bg_dir = None
    sc_data_dir = None
    calculatedLumi = {}
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        'SingleMuon' : "1"
    }
    bgReTagging = {}
    bgReTaggingOrder = {}
    plot_kind = "MET"
    plot_bg = True
    plot_signal = True
    plot_rand = False
    plot_fast = True
    plot_title = True
    plot_overflow = True
    plot_significance = False
    plot_error = False
    plot_sc = False
    plot_data = False
    plot_ratio = False
    plot_point = False
    plot_efficiency = False
    create_canvas = False
    plot_custom_ratio = False
    #customRatios = [  [["DiBoson"],["TTJets"]],  [["WJetsToLNu"],["ZJetsToNuNu"]]  ]
    customRatios = [  [["tc_btag_veto"],["tc_2_btags"]]  ]
    choose_bg_files = False
    choose_bg_files_list = ["TTJets"]
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
    no_weights = False
    fit_inv_mass_jpsi = False
    fit_inv_mass_obs_jpsi = ""
    fit_inv_mass_cut_jpsi = "none"
    fit_inv_mass_jpsi_func = "gauss"
    fit_inv_mass_jpsi_func_bg = False
    fit_inv_mass_jpsi_bg_func = "linear"
    
    save_histrograms_to_file = False
    load_histrograms_from_file = False
    histrograms_file = ""
    
    bg_retag = False
    
    
    
    

class signal_muons(BaseParams):
    signal_dir = signals
    signal_names = signalNames
    cuts = [
        {"name":"none", "title": "No Cuts", "condition" : "1"},
    ]
    histograms_defs = [
        { "obs" : "Muons_pt", "formula" : "Muons.Pt()", "units" : "P_{t}", "minX" : 2, "maxX" : 25, "bins" : 60, "condition" :  "Muons_isZ == 1", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        { "obs" : "Muons_Eta", "formula" : "abs(Muons.Eta())", "units" : "|\eta|", "minX" : 0, "maxX" : 2.4, "bins" : 60, "condition" :  "Muons_isZ == 1", "linearYspace" : 1.8, "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        { "obs" : "deltaRCorrJetIso10", "units" : "#Delta_{}R", "minX" : 0, "maxX" : 3.5, "bins" : 60, "condition" :  "twoLeptonsCorrJetIso10 == 1 && leptonFlavour == \"Muons\" && Muons_isZ[leptonsIdxCorrJetIso10[0]] == 1 &&  Muons_isZ[leptonsIdxCorrJetIso10[1]] == 1 ", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        
        { "obs" : "Muons_pt_barrel", "formula" : "Muons.Pt()", "units" : "barrel p_{T}", "minX" : 2, "maxX" : 10, "bins" : 60, "condition" :  "Muons_isZ == 1 && abs(Muons.Eta()) < 1.2", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        { "obs" : "Muons_pt_endcape", "formula" : "Muons.Pt()", "units" : "endcaps p_{T}", "minX" : 2, "maxX" : 10, "bins" : 60, "condition" :  "Muons_isZ == 1 && abs(Muons.Eta()) >= 1.2 && abs(Muons.Eta()) <= 2.4", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        
    ]
    
    weightString = {
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        'SingleMuon' : "1"
    }
    
    plot_bg = False
    plot_data = False
    plot_overflow = False
    
signalsGen = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm0p86Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm1p92Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm3p28Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm9p73Chi20Chipm.root"
              ]

class signal_muons_gen(BaseParams):
    signal_dir = signalsGen
    signal_names = signalNames
    cuts = [
        {"name":"none", "title": "No Cuts", "condition" : "1"},
    ]
    histograms_defs = [
        { "obs" : "Muons_pt", "formula" : "GenParticles.Pt()", "units" : "P_{t}", "minX" : 2, "maxX" : 25, "bins" : 60, "condition" :  "GenParticles.Pt() < 20 && abs(GenParticles_PdgId) == 13 && GenParticles.Pt() > 2", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        { "obs" : "Muons_Eta", "formula" : "abs(GenParticles.Eta())", "units" : "|\eta|", "minX" : 0, "maxX" : 2.4, "bins" : 60, "condition" :  "GenParticles.Pt() < 20 && abs(GenParticles_PdgId) == 13 && GenParticles.Pt() > 2", "linearYspace" : 1.8, "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        #{ "obs" : "deltaRCorrJetIso10", "units" : "#Delta_{}R", "minX" : 0, "maxX" : 3.5, "bins" : 60, "condition" :  "twoLeptonsCorrJetIso10 == 1 && leptonFlavour == \"Muons\" && Muons_isZ[leptonsIdxCorrJetIso10[0]] == 1 &&  Muons_isZ[leptonsIdxCorrJetIso10[1]] == 1 ", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        
        { "obs" : "Muons_pt_barrel", "formula" : "GenParticles.Pt()", "units" : "barrel p_{T}", "minX" : 2, "maxX" : 10, "bins" : 60, "condition" :  "GenParticles.Pt() < 20 && abs(GenParticles_PdgId) == 13 && GenParticles.Pt() > 2 && abs(GenParticles.Eta()) < 1.2", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        { "obs" : "Muons_pt_endcape", "formula" : "GenParticles.Pt()", "units" : "endcaps p_{T}", "minX" : 2, "maxX" : 10, "bins" : 60, "condition" :  "GenParticles.Pt() < 20 && abs(GenParticles_PdgId) == 13 && GenParticles.Pt() > 2 && abs(GenParticles.Eta()) >= 1.2 && abs(GenParticles.Eta()) <= 2.4", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        
    ]
    
    weightString = {
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        'SingleMuon' : "1"
    }
    
    plot_bg = False
    plot_data = False
    plot_overflow = False
    


#{"name":"none", "title": "No Cuts", "condition" : "exclusiveTrack == 1 && Ht > 200 && passedSingleMuPack == 1 && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 10 && track.Pt() < 25 && Muons[0].Pt() < 100"},

class jpsi_muons(BaseParams):
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_muons_jpsi_track/sum/type_sum"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_muons_jpsi_track/sum"
    plot_kind = "SingleMuon"
    plot_signal = False
    plot_data = True
    plot_ratio = True
    blind_data = False
    plot_overflow = True
    calculatedLumi = {
        'SingleMuonReco' : 15.473761772,
        'SingleMuon' : 22.944792027,
    }
    # histograms_defs = [
#         { "obs" : "invMass", "units" : "M_{ll}", "minX" : 2.5, "maxX" : 3.5, "bins" : 60 },
#         { "obs" : "Muons[0].Pt()", "minX" : 24, "maxX" : 50, "bins" : 50 },
#         { "obs" : "leptons.Pt()", "minX" : 2, "maxX" : 15, "bins" : 50, "condition" :  "leptons.Pt() > 2.5" },
#         { "obs" : "leptons.Eta()", "minX" : 0, "maxX" : 2.4, "bins" : 50 },
#         { "obs" : "abs(leptons.Phi())", "minX" : 0, "maxX" : 3.2, "bins" : 50 },
#         
#     ] + common_histograms
    
    histograms_defs = [
        { "obs" : "invMass", "units" : "M_{ll}", "minX" : 2.5, "maxX" : 3.5, "bins" : 60 },
        { "obs" : "leptons.Pt()", "units" : "Muon P_{t}", "minX" : 2, "maxX" : 24, "bins" : 60 },
        { "obs" : "abs(leptons.Phi())",  "units" : "Muon \phi", "minX" : 0, "maxX" : 3.2, "bins" : 50 },
        { "obs" : "abs(leptons.Eta())", "units" : "Muon \eta", "minX" : 0, "maxX" : 2.4, "bins" : 50 },
        { "obs" : "tracks[Muons_ti[leptonsIdx]].Pt()", "units" : "Track P_{t}", "minX" : 2, "maxX" : 24, "bins" : 60, "condition" :  "Muons_ti[leptonsIdx] > -1" },
        { "obs" : "abs(tracks[Muons_ti[leptonsIdx]].Phi())",  "units" : "Track \phi", "minX" : 0, "maxX" : 3.2, "bins" : 50, "condition" :  "Muons_ti[leptonsIdx] > -1" },
        { "obs" : "tracks[Muons_ti[leptonsIdx]].Eta()", "units" : "Track \eta", "minX" : 0, "maxX" : 2.4, "bins" : 50, "condition" :  "Muons_ti[leptonsIdx] > -1" },
        { "obs" : "tracks_dxyVtx[Muons_ti[leptonsIdx]]", "units" : "dxy", "minX" : 0, "maxX" : 0.2, "bins" : 50, "condition" :  "Muons_ti[leptonsIdx] > -1" },
        { "obs" : "tracks_dzVtx[Muons_ti[leptonsIdx]]", "units" : "dz", "minX" : 0, "maxX" : 0.5, "bins" : 50, "condition" :  "Muons_ti[leptonsIdx] > -1" },
        { "obs" : "tracks_trkMiniRelIso[Muons_ti[leptonsIdx]]", "units" : "MiniRelIso", "minX" : 0, "maxX" : 0.2, "bins" : 50, "condition" :  "Muons_ti[leptonsIdx] > -1" },
        { "obs" : "tracks_trkRelIso[Muons_ti[leptonsIdx]]", "units" : "RelIso", "minX" : 0, "maxX" : 0.2, "bins" : 50, "condition" :  "Muons_ti[leptonsIdx] > -1" },
        { "obs" : "Muons[0].Pt()", "units" : "P_{t}(\mu_{1})", "minX" : 24, "maxX" : 100, "bins" : 60 },
        { "obs" : "Met", "units" : "Met", "minX" : 0, "maxX" : 250, "bins" : 50 },
        { "obs" : "Ht", "units" : "Ht", "minX" : 0, "maxX" : 1000, "bins" : 100 },
        { "obs" : "madHT", "units" : "madHT", "minX" : 0, "maxX" : 400, "bins" : 100 },
        { "obs" : "BTagsMedium", "units" : "BTagsMedium", "minX" : 0, "maxX" : 5, "bins" : 5 },
        { "obs" : "NJets", "units" : "NJets", "minX" : 0, "maxX" : 5, "bins" : 5 },
        { "obs" : "Muons_tightID[leptonsIdx]", "units" : "tightId", "minX" : 0, "maxX" : 2, "bins" : 2 },
        
    ]
    
    # histograms_defs = [
#          { "obs" : "Ht", "units" : "Ht", "minX" : 0, "maxX" : 1000, "bins" : 100 },
#          { "obs" : "madHT", "units" : "madHT", "minX" : 0, "maxX" : 400, "bins" : 100 },
#          { "obs" : "NJets", "units" : "NJets", "minX" : 0, "maxX" : 5, "bins" : 5 },
#     ]
    
    cuts = [
        {"name":"none", "title": "No Cuts", "condition" : "twoLeptons == 1 && passedSingleMuPack == 1"},
        #{"name":"track_match", "title": "Track Match", "condition" : "Muons_ti[leptonsIdx] > -1 && twoLeptons == 1 && passedSingleMuPack == 1"},
        {"name":"jpsi", "title": "jpsi", "condition" : "twoLeptons == 1 && invMass > 3.04 && invMass < 3.18 && passedSingleMuPack == 1"},
    ]
    
    #bgReTagging = bgReTaggingJPsi
    #bgReTaggingOrder = bgReTaggingOrderFull
    
    bgReTagging = {
        "jpsi" : "leptonParentPdgId == 443 || trackParentPdgId == 443",
        "other" : "!(leptonParentPdgId == 443 || trackParentPdgId == 443)",
    }

    bgReTaggingOrder = {
        "jpsi" : 0,
        "other" : 1
    }

class jpsi_muons_ex_track(jpsi_muons):
    histograms_defs = [
        { "obs" : "exTrack_invMass", "units" : "M_{ll}", "minX" : 2.5, "maxX" : 3.5, "bins" : 60 },
        { "obs" : "lepton.Pt()", "units" : "Muon P_{t}", "minX" : 2, "maxX" : 24, "bins" : 60 },
        { "obs" : "abs(lepton.Phi())",  "units" : "Muon \phi", "minX" : 0, "maxX" : 3.2, "bins" : 50 },
        { "obs" : "abs(lepton.Eta())", "units" : "Muon \eta", "minX" : 0, "maxX" : 2.4, "bins" : 50 },
        { "obs" : "track.Pt()", "units" : "Track P_{t}", "minX" : 2, "maxX" : 24, "bins" : 60 },
        #{ "obs" : "abs(track.Phi())",  "units" : "Track \phi", "minX" : 0, "maxX" : 3.2, "bins" : 50 },
        { "obs" : "abs( track.Eta() )", "units" : "Track \eta", "minX" : 0, "maxX" : 2.4, "bins" : 50 },
        { "obs" : "abs(track.Eta())", "units" : "Matched Track \eta", "minX" : 0, "maxX" : 2.4, "bins" : 50, "condition" :  "tracks_mi[ti] > -1" },
        #{ "obs" : "tracks_dxyVtx[ti]", "units" : "dxy", "minX" : 0, "maxX" : 0.2, "bins" : 50 },
        #{ "obs" : "tracks_dzVtx[ti]", "units" : "dz", "minX" : 0, "maxX" : 0.5, "bins" : 50 },
        #{ "obs" : "tracks_trkMiniRelIso[ti]", "units" : "MiniRelIso", "minX" : 0, "maxX" : 0.2, "bins" : 50 },
        #{ "obs" : "tracks_trkRelIso[ti]", "units" : "RelIso", "minX" : 0, "maxX" : 0.2, "bins" : 50},
        { "obs" : "Muons[0].Pt()", "units" : "P_{t}(\mu_{1})", "minX" : 24, "maxX" : 300, "bins" : 100 },
        { "obs" : "Met", "units" : "Met", "minX" : 0, "maxX" : 250, "bins" : 50 },
        { "obs" : "Ht", "units" : "Ht", "minX" : 0, "maxX" : 1000, "bins" : 100 },
        #{ "obs" : "madHT", "units" : "madHT", "minX" : 0, "maxX" : 400, "bins" : 100 },
        #{ "obs" : "BTagsMedium", "units" : "BTagsMedium", "minX" : 0, "maxX" : 5, "bins" : 5 },
        #{ "obs" : "NJets", "units" : "NJets", "minX" : 0, "maxX" : 5, "bins" : 5 },
        { "obs" : "Muons_tightID[leptonIdx]", "units" : "tightId", "minX" : 0, "maxX" : 2, "bins" : 2 },
        { "obs" : "exTrack_deltaEta", "units" : "\Delta\eta", "minX" : 0, "maxX" : 3, "bins" : 30 },
        { "obs" : "exTrack_deltaR", "units" : "\Delta{R}", "minX" : 0, "maxX" : 3, "bins" : 30 },
        
        #{ "obs" : "tracks_dxyVtx[Muons_ti[leptonIdx]]", "units" : "\mu dxy", "minX" : 0, "maxX" : 0.2, "bins" : 30, "condition" :  "Muons_ti[leptonIdx] > -1" },
        #{ "obs" : "tracks_dzVtx[Muons_ti[leptonIdx]]", "units" : "\mudz", "minX" : 0, "maxX" : 0.2, "bins" : 30, "condition" :  "Muons_ti[leptonIdx] > -1" },
        
    ]
    
    cuts = [
        #{"name":"none", "title": "No Cuts", "condition" : "exclusiveTrack == 1 && Muons_tightID[leptonIdx] == 1 && track.Pt() < 10 && lepton.Pt() > 10 && track.Pt() < 24 && Ht > 200 && passedSingleMuPack == 1"},
        #{"name":"jpsi", "title": "jpsi", "condition" : "exclusiveTrack == 1 && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 10 && track.Pt() < 24 && Ht > 200 && exclusiveTrack == 1 && exTrack_invMass > 3.04 && exTrack_invMass < 3.18 && passedSingleMuPack == 1"},
        
        #{"name":"none", "title": "No Cuts", "condition" : "exclusiveTrack == 1 && passedSingleMuPack == 1 && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 8 && track.Pt() < 25 && exTrack_deltaR < 0.7 && tracks_mi[ti] > -1"},
        
        #{"name":"jpsi", "title": "jpsi", "condition" : "exclusiveTrack == 1 &&  passedSingleMuPack == 1  && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 8 && track.Pt() < 25 && exTrack_invMass > 3.00 && exTrack_invMass < 3.2 && exTrack_deltaR < 0.7"},
        
        # {"name":"jpsi_2_3_barrel", "title": "jpsi pt 2-3 Barrel", "condition" : "exclusiveTrack == 1 &&  passedSingleMuPack == 1 && lepton.Pt() > 4 && track.Pt() < 25 && abs(track.Eta()) < 1.2 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3"},
#         {"name":"jpsi_2_3_endcups", "title": "jpsi pt 2-3 Endcaps", "condition" : "exclusiveTrack == 1 &&  passedSingleMuPack == 1 && lepton.Pt() > 4 && track.Pt() < 25 && abs(track.Eta()) >= 1.2 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3"},
#         
#         {"name":"jpsi_2_3_ht", "title": "jpsi pt 2-3 Ht > 100", "condition" : "Ht > 100 && exclusiveTrack == 1 &&  passedSingleMuPack == 1 && lepton.Pt() > 4 && track.Pt() < 25 && abs(track.Eta()) >= 1.2 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3"},
#         {"name":"jpsi_2_3_m0", "title": "jpsi pt 2-3 M0 > 100", "condition" : "Ht < 600 && Ht > 100 && exclusiveTrack == 1 &&  passedSingleMuPack == 1 && lepton.Pt() > 6 && track.Pt() < 25 && abs(track.Eta()) >= 1.2 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3 && Muons[0].Pt() < 100"},
#         
#         {"name":"jpsi_2_3_ht_barrel", "title": "jpsi pt 2-3 Ht > 100 barrel", "condition" : "Ht > 100 && exclusiveTrack == 1 &&  passedSingleMuPack == 1 && lepton.Pt() > 4 && track.Pt() < 25 && abs(track.Eta()) < 1.2 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3"},
#         {"name":"jpsi_2_3_m0_barrel", "title": "jpsi pt 2-3 M0 > 100 barrel", "condition" : "Ht < 600 && Ht > 100 && exclusiveTrack == 1 &&  passedSingleMuPack == 1 && lepton.Pt() > 6 && track.Pt() < 25 && abs(track.Eta()) < 1.2 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3 && Muons[0].Pt() < 100"},
#         
        {"name":"jpsi_2_3_ht_m0", "title": "jpsi pt 2-3 Ht > 100 M0 > 100", "condition" : "Ht > 100 && exclusiveTrack == 1 &&  passedSingleMuPack == 1 && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 4 && track.Pt() < 25 && abs(track.Eta()) >= 1.2 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3.5 && Muons[0].Pt() < 100 && exTrack_deltaR <= 1 && abs(lepton.Eta()) > 0.6"},
        
        
        #{"name":"jpsi_2_3", "title": "jpsi pt 2-3", "condition" : "exclusiveTrack == 1 &&  passedSingleMuPack == 1  && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 8 && track.Pt() < 25 && exTrack_invMass > 3.00 && exTrack_invMass < 3.2 && exTrack_deltaR < 0.7 && abs(track.Eta()) < 2.4 && tracks_mi[ti] > -1 && Muons_mediumID[tracks_mi[ti]] == 1 && track.Pt() >= 2 && track.Pt() <= 3"},
        #{"name":"jpsi_3_5_0_12", "title": "jpsi pt 3-5 eta 0-1.2", "condition" : "exclusiveTrack == 1 &&  passedSingleMuPack == 1  && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 8 && track.Pt() < 25 && exTrack_invMass > 3.00 && exTrack_invMass < 3.2 && exTrack_deltaR < 0.7 && abs(track.Eta()) < 2.4 && tracks_mi[ti] > -1 && Muons_mediumID[tracks_mi[ti]] == 1 && track.Pt() >= 3 && track.Pt() <= 5 && abs(track.Eta()) <= 1.2"},
        #{"name":"jpsi_3_5_12_24", "title": "jpsi pt 3-5 eta 1.2-2.4", "condition" : "exclusiveTrack == 1 &&  passedSingleMuPack == 1  && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 8 && track.Pt() < 25 && exTrack_invMass > 3.00 && exTrack_invMass < 3.2 && exTrack_deltaR < 0.7 && abs(track.Eta()) < 2.4 && tracks_mi[ti] > -1 && Muons_mediumID[tracks_mi[ti]] == 1 && track.Pt() >= 3 && track.Pt() <= 5 && abs(track.Eta()) >= 1.2 && abs(track.Eta()) <= 2.4"},
    ]
    
    
    bgReTagging = {
        "jpsi" : "leptonParentPdgId == 443 || trackParentPdgId == 443",
        "other" : "!(leptonParentPdgId == 443 || trackParentPdgId == 443)",
    }

    bgReTaggingOrder = {
        "jpsi" : 0,
        "other" : 1
    }

class jpsi_muons_ex_track_new(jpsi_muons):
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_master/sum/type_sum"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_master/sum"
    
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        'SingleMuon' : "puWeight"
    }
    
    calculatedLumi = {
        'SingleMuonReco' : 15.473761772,
        'SingleMuon' : 0.001,
    }
    
    histograms_defs = [
        { "obs" : "invMass", "units" : "M_{ll}", "minX" : 2.5, "maxX" : 3.5, "bins" : 60 },
        #{ "obs" : "BDT", "units" : "BDT", "minX" : -1, "maxX" : 1, "bins" : 60 },
        #{ "obs" : "BtagsDeepMedium", "units" : "BtagsDeepMedium", "minX" : 0, "maxX" : 5, "bins" : 5 },
        
        
        
        
        { "obs" : "Muons[tagMuon].Pt()", "units" : "Muon P_{t}", "minX" : 2, "maxX" : 24, "bins" : 60 },
#         { "obs" : "abs(Muons[tagMuon].Phi())",  "units" : "Muon \phi", "minX" : 0, "maxX" : 3.2, "bins" : 50 },
#         { "obs" : "abs(Muons[tagMuon].Eta())", "units" : "Muon \eta", "minX" : 0, "maxX" : 2.4, "bins" : 50 },
#         { "obs" : "tracks[probeTrack].Pt()", "units" : "Track P_{t}", "minX" : 2, "maxX" : 24, "bins" : 60 },
# 
#         { "obs" : "abs( tracks[probeTrack].Eta() )", "units" : "Track \eta", "minX" : 0, "maxX" : 2.4, "bins" : 50 },
#         { "obs" : "abs(tracks[probeTrack].Eta())", "units" : "Matched Track \eta", "minX" : 0, "maxX" : 2.4, "bins" : 50, "condition" :  "tracks_mi[probeTrack] > -1" },
        #{ "obs" : "tracks_dxyVtx[ti]", "units" : "dxy", "minX" : 0, "maxX" : 0.2, "bins" : 50 },
        #{ "obs" : "tracks_dzVtx[ti]", "units" : "dz", "minX" : 0, "maxX" : 0.5, "bins" : 50 },
        #{ "obs" : "tracks_trkMiniRelIso[ti]", "units" : "MiniRelIso", "minX" : 0, "maxX" : 0.2, "bins" : 50 },
        #{ "obs" : "tracks_trkRelIso[ti]", "units" : "RelIso", "minX" : 0, "maxX" : 0.2, "bins" : 50},
        #{ "obs" : "Muons[0].Pt()", "units" : "P_{t}(\mu_{1})", "minX" : 24, "maxX" : 300, "bins" : 100 },
        #{ "obs" : "Met", "units" : "Met", "minX" : 0, "maxX" : 250, "bins" : 50 },
        #{ "obs" : "Ht", "units" : "Ht", "minX" : 0, "maxX" : 1000, "bins" : 100 },
        #{ "obs" : "madHT", "units" : "madHT", "minX" : 0, "maxX" : 400, "bins" : 100 },
        #{ "obs" : "BTagsMedium", "units" : "BTagsMedium", "minX" : 0, "maxX" : 5, "bins" : 5 },
        #{ "obs" : "NJets", "units" : "NJets", "minX" : 0, "maxX" : 5, "bins" : 5 },
        # { "obs" : "Muons_tightID[tagMuon]", "units" : "tightId", "minX" : 0, "maxX" : 2, "bins" : 2 },
#         { "obs" : "deltaEta", "units" : "\Delta\eta", "minX" : 0, "maxX" : 3, "bins" : 30 },
         { "obs" : "deltaR", "units" : "\Delta{R}", "minX" : 0, "maxX" : 3, "bins" : 30 },
#         { "obs" : "dileptonPt", "units" : "\Delta{R}", "minX" : 0, "maxX" : 50, "bins" : 50 },
        
        
        #{ "obs" : "tracks_dxyVtx[Muons_ti[leptonIdx]]", "units" : "\mu dxy", "minX" : 0, "maxX" : 0.2, "bins" : 30, "condition" :  "Muons_ti[leptonIdx] > -1" },
        #{ "obs" : "tracks_dzVtx[Muons_ti[leptonIdx]]", "units" : "\mudz", "minX" : 0, "maxX" : 0.2, "bins" : 30, "condition" :  "Muons_ti[leptonIdx] > -1" },
        
    ]
    
    cuts = [
        #{"name":"none", "title": "No Cuts", "condition" : "exclusiveTrack == 1 && Muons_tightID[leptonIdx] == 1 && track.Pt() < 10 && lepton.Pt() > 10 && track.Pt() < 24 && Ht > 200 && passedSingleMuPack == 1"},
        #{"name":"none", "title": "No Cuts", "condition" : "tracks[probeTrack].Pt() >= 2 && tracks[probeTrack].Pt() < 3 && abs(tracks[probeTrack].Eta()) >= 1.2 && abs(tracks[probeTrack].Eta()) < 2.4"},
        {"name":"none", "title": "None", "condition" : "tracks[probeTrack].Pt() >= 2 && tracks[probeTrack].Pt() <= 20"},
        #{"name":"BtagsDeepMedium", "title": "BtagsDeepMedium", "condition" : "(BtagsDeepMedium >= 1 && BDT > -0.1 && tracks[probeTrack].Pt() >= 2 && tracks[probeTrack].Pt() < 3 && abs(tracks[probeTrack].Eta()) >= 1.2 && abs(tracks[probeTrack].Eta()) < 2.4)"},
        #{"name":"bdt0", "title": "BDT > 0", "condition" : "tracks[probeTrack].Pt() >= 2 && BDT > 0 && tracks[probeTrack].Pt() < 3 && abs(tracks[probeTrack].Eta()) >= 1.2 && abs(tracks[probeTrack].Eta()) < 2.4"},
        #{"name":"bdt1", "title": "BDT > 0.1", "condition" : "tracks[probeTrack].Pt() >= 2 &&  BDT > 0.1 && tracks[probeTrack].Pt() < 3 && abs(tracks[probeTrack].Eta()) >= 1.2 && abs(tracks[probeTrack].Eta()) < 2.4"},
        #{"name":"bdt2", "title": "BDT > 0.2", "condition" : "tracks[probeTrack].Pt() >= 2 &&  BDT > 0.2 && tracks[probeTrack].Pt() < 3 && abs(tracks[probeTrack].Eta()) >= 1.2 && abs(tracks[probeTrack].Eta()) < 2.4"},
        #{"name":"bdt3", "title": "BDT > 0.3", "condition" : "tracks[probeTrack].Pt() >= 2 &&  BDT > 0.3 && tracks[probeTrack].Pt() < 3 && abs(tracks[probeTrack].Eta()) >= 1.2 && abs(tracks[probeTrack].Eta()) < 2.4"},
        
        
        #{"name":"bdt2", "title": "BDT > 0.2", "condition" : "BDT > 0.2 && tracks[probeTrack].Pt() < 3.5 && abs(tracks[probeTrack].Eta()) >= 1.2 && abs(tracks[probeTrack].Eta()) < 2.4"},
        #{"name":"jpsi", "title": "jpsi", "condition" : "exclusiveTrack == 1 && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 10 && track.Pt() < 24 && Ht > 200 && exclusiveTrack == 1 && exTrack_invMass > 3.04 && exTrack_invMass < 3.18 && passedSingleMuPack == 1"},
        
        #{"name":"none", "title": "No Cuts", "condition" : "exclusiveTrack == 1 && passedSingleMuPack == 1 && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 8 && track.Pt() < 25 && exTrack_deltaR < 0.7 && tracks_mi[ti] > -1"},
        
        #{"name":"jpsi", "title": "jpsi", "condition" : "exclusiveTrack == 1 &&  passedSingleMuPack == 1  && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 8 && track.Pt() < 25 && exTrack_invMass > 3.00 && exTrack_invMass < 3.2 && exTrack_deltaR < 0.7"},
        
        # {"name":"jpsi_2_3_barrel", "title": "jpsi pt 2-3 Barrel", "condition" : "exclusiveTrack == 1 &&  passedSingleMuPack == 1 && lepton.Pt() > 4 && track.Pt() < 25 && abs(track.Eta()) < 1.2 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3"},
#         {"name":"jpsi_2_3_endcups", "title": "jpsi pt 2-3 Endcaps", "condition" : "exclusiveTrack == 1 &&  passedSingleMuPack == 1 && lepton.Pt() > 4 && track.Pt() < 25 && abs(track.Eta()) >= 1.2 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3"},
#         
#         {"name":"jpsi_2_3_ht", "title": "jpsi pt 2-3 Ht > 100", "condition" : "Ht > 100 && exclusiveTrack == 1 &&  passedSingleMuPack == 1 && lepton.Pt() > 4 && track.Pt() < 25 && abs(track.Eta()) >= 1.2 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3"},
#         {"name":"jpsi_2_3_m0", "title": "jpsi pt 2-3 M0 > 100", "condition" : "Ht < 600 && Ht > 100 && exclusiveTrack == 1 &&  passedSingleMuPack == 1 && lepton.Pt() > 6 && track.Pt() < 25 && abs(track.Eta()) >= 1.2 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3 && Muons[0].Pt() < 100"},
#         
#         {"name":"jpsi_2_3_ht_barrel", "title": "jpsi pt 2-3 Ht > 100 barrel", "condition" : "Ht > 100 && exclusiveTrack == 1 &&  passedSingleMuPack == 1 && lepton.Pt() > 4 && track.Pt() < 25 && abs(track.Eta()) < 1.2 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3"},
#         {"name":"jpsi_2_3_m0_barrel", "title": "jpsi pt 2-3 M0 > 100 barrel", "condition" : "Ht < 600 && Ht > 100 && exclusiveTrack == 1 &&  passedSingleMuPack == 1 && lepton.Pt() > 6 && track.Pt() < 25 && abs(track.Eta()) < 1.2 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3 && Muons[0].Pt() < 100"},
#         
        #{"name":"jpsi_2_3_ht_m0", "title": "jpsi pt 2-3 Ht > 100 M0 > 100", "condition" : "Ht > 100 && exclusiveTrack == 1 &&  passedSingleMuPack == 1 && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 4 && track.Pt() < 25 && abs(track.Eta()) >= 1.2 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3.5 && Muons[0].Pt() < 100 && exTrack_deltaR <= 1 && abs(lepton.Eta()) > 0.6"},
        
        
        #{"name":"jpsi_2_3", "title": "jpsi pt 2-3", "condition" : "exclusiveTrack == 1 &&  passedSingleMuPack == 1  && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 8 && track.Pt() < 25 && exTrack_invMass > 3.00 && exTrack_invMass < 3.2 && exTrack_deltaR < 0.7 && abs(track.Eta()) < 2.4 && tracks_mi[ti] > -1 && Muons_mediumID[tracks_mi[ti]] == 1 && track.Pt() >= 2 && track.Pt() <= 3"},
        #{"name":"jpsi_3_5_0_12", "title": "jpsi pt 3-5 eta 0-1.2", "condition" : "exclusiveTrack == 1 &&  passedSingleMuPack == 1  && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 8 && track.Pt() < 25 && exTrack_invMass > 3.00 && exTrack_invMass < 3.2 && exTrack_deltaR < 0.7 && abs(track.Eta()) < 2.4 && tracks_mi[ti] > -1 && Muons_mediumID[tracks_mi[ti]] == 1 && track.Pt() >= 3 && track.Pt() <= 5 && abs(track.Eta()) <= 1.2"},
        #{"name":"jpsi_3_5_12_24", "title": "jpsi pt 3-5 eta 1.2-2.4", "condition" : "exclusiveTrack == 1 &&  passedSingleMuPack == 1  && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 8 && track.Pt() < 25 && exTrack_invMass > 3.00 && exTrack_invMass < 3.2 && exTrack_deltaR < 0.7 && abs(track.Eta()) < 2.4 && tracks_mi[ti] > -1 && Muons_mediumID[tracks_mi[ti]] == 1 && track.Pt() >= 3 && track.Pt() <= 5 && abs(track.Eta()) >= 1.2 && abs(track.Eta()) <= 2.4"},
    ]
    
    
    bgReTagging = {
        "jpsi" : "tagJpsi == 1 && probeJpsi == 1",
        "other" : "!(tagJpsi == 1 && probeJpsi == 1)",
    }

    bgReTaggingOrder = {
        "jpsi" : 0,
        "other" : 1
    }
    
    plot_data = False
    plot_ratio = False
    normalise = False
    no_weights = False
    plot_overflow = False
    bg_retag = True

class jpsi_muons_ex_track_new_data(jpsi_muons_ex_track_new):
    plot_data = True
    plot_bg = False
    



# fSignalOnlyModel.SetParameter(0, 3.27)
# fSignalOnlyModel.SetParLimits(0, 1, 30)
# 
# fSignalOnlyModel.SetParameter(1, 4.57)
# fSignalOnlyModel.SetParLimits(1, 0, 100)
# #fSignalOnlyModel.SetParameter(0, 0)
# fSignalOnlyModel.SetParameter(2, 0.043)
# fSignalOnlyModel.SetParLimits(2, 0.005, 0.1)
# 
# fSignalOnlyModel.SetParameter(4, 70)


crystalBallInitialConditions = {

    "id_invMass_2_3_1.2_2.4" : {
        "pars" :
            [
                3.42383,
                0.057,
                0.043,
                3.096916,
                66.7
            ],
        "limits" :
            [
                [1, 10],
                [0, 10],
                [0.005, 0.1],
                [3.09, 3.1],
                [60,70]
            ]
    },
    
    "invMass_2_3_1.2_2.4" : {
        "pars" :
            [
                3.4,
                0,
                0.046,
                3.096916,
                70
            ],
        "limits" :
            [
                [1, 10],
                [0, 10],
                [0.02, 0.07],
                [3.09, 3.1],
                [60,200]
            ]
    },
    
    "id_invMass_3_4_0_1.2" : {
        "pars" :
            [
                1,
                1,
                0.026,
                3.096916,
                73
            ],
        "limits" :
            [
                [0, 10],
                [0, 10],
                [0.01, 0.07],
                [3.09, 3.1],
                [50,100]
            ]
    },
    
    "invMass_3_4_0_1.2" : {
        "pars" :
            [
                1.8,
                2.9,
                0.03,
                3.096916,
                160
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.01, 0.08],
                [3.09, 3.1],
                [140,180]
            ]
    },
    
    "id_invMass_3_4_1.2_2.4" : {
        "pars" :
            [
                5,
                1000,
                0.038,
                3.096916,
                67
            ],
        "limits" :
            [
                [0, 10000],
                [0, 100000],
                [0.01, 0.07],
                [3.09, 3.15],
                [50,85]
            ]
    },
    
    "invMass_3_4_1.2_2.4" : {
        "pars" :
            [
                1000,
                1000,
                0.03,
                3.096916,
                60
            ],
        "limits" :
            [
                [0, 10000],
                [0, 1000000],
                [0.01, 0.08],
                [3.09, 3.105],
                [50,180]
            ]
    },
    
    # "invMass_3_4_1.2_2.4" : {
#         "pars" :
#             [
#                 1.8,
#                 2.9,
#                 0.03,
#                 3.096916,
#                 60
#             ],
#         "limits" :
#             [
#                 [0, 10000],
#                 [0, 100000],
#                 [0.01, 0.08],
#                 [3.09, 3.1],
#                 [50,180]
#             ]
#     },
    
    "id_invMass_4_5_0_1.2" : {
        "pars" :
            [
                1,
                1,
                0.026,
                3.096916,
                101
            ],
        "limits" :
            [
                [0, 10],
                [0, 10],
                [0.01, 0.07],
                [3.09, 3.1],
                [80,250]
            ]
    },
    
 
    "invMass_4_5_0_1.2" : {
        "pars" :
            [
                1,
                1,
                0.019,
                3.096916,
                145
            ],
        "limits" :
            [
                [0, 10],
                [0, 10],
                [0.01, 0.04],
                [3.09, 3.1],
                [50,350]
            ]
    },
    
    "id_invMass_3_5_0_1.2" : {
        "pars" :
            [
                1,
                1,
                0.026,
                3.096916,
                168
            ],
        "limits" :
            [
                [0, 10],
                [0, 10],
                [0.01, 0.07],
                [3.09, 3.1],
                [100,250]
            ]
    },
    
 
    "invMass_3_5_0_1.2" : {
        "pars" :
            [
                2.05,
                1,
                0.019,
                3.096916,
                300
            ],
        "limits" :
            [
                [0, 5],
                [0, 5],
                [0.01, 0.04],
                [3.09, 3.1],
                [250,350]
            ]
    },

    # "id_invMass_3_5_0_1.2" : {
#         "pars" :
#             [
#                 1.51,
#                 3.43,
#                 0.039,
#                 3.096916,
#                 122
#             ],
#         "limits" :
#             [
#                 [0, 10],
#                 [0, 10],
#                 [0.01, 0.05],
#                 [3.09, 3.1],
#                 [100,150]
#             ]
#     },
    
    "id_invMass_3_5_1.2_2.4" : {
        "pars" :
            [
                1,
                2,
                0.039,
                3.096916,
                122
            ],
        "limits" :
            [
                [1, 6],
                [1, 15],
                [0.01, 0.04],
                [3.09, 3.1],
                [121,125]
            ]
    },

    
    "invMass_3_5_1.2_2.4" : {
        "pars" :
            [
                1.62,
                1.88,
                0.039,
                3.096916,
                130
            ],
        "limits" :
            [
                [0, 2],
                [0, 2],
                [0.01, 0.05],
                [3.09, 3.1],
                [120,135]
            ]
    },
    
    "id_invMass_4_5_1.2_2.4" : {
        "pars" :
            [
                1,
                2,
                0.039,
                3.096916,
                60
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.01, 0.04],
                [3.09, 3.1],
                [20,100]
            ]
    },

    
    "invMass_4_5_1.2_2.4" : {
        "pars" :
            [
                1,
                1,
                0.039,
                3.096916,
                58
            ],
        "limits" :
            [
                [0, 10000],
                [0, 10000],
                [0.01, 0.05],
                [3.085, 3.105],
                [20,80]
            ]
    },
    
    "id_invMass_5_10_0_1.2" : {
        "pars" :
            [
                1.42,
                3.01,
                0.024,
                3.096916,
                321
            ],
        "limits" :
            [
                [0, 2],
                [1, 100000],
                [0.01, 0.04],
                [3.09, 3.1],
                [300,350]
            ]
    },
    
    "invMass_5_10_0_1.2" : {
        "pars" :
            [
                1,
                2.9,
                0.024,
                3.096916,
                350
            ],
        "limits" :
            [
                [1, 5],
                [1, 5],
                [0.01, 0.04],
                [3.09, 3.1],
                [300,390]
            ]
    },
    
    "id_invMass_5_10_1.2_2.4" : {
        "pars" :
            [
                1.7,
                10,
                0.049,
                3.096916,
                138
            ],
        "limits" :
            [
                [0, 2],
                [0, 10000],
                [0.01, 0.05],
                [3.09, 3.1],
                [100,150]
            ]
    },
  
    "invMass_5_10_1.2_2.4" : {
        "pars" :
            [
                1,
                50,
                0.039,
                3.096916,
                148
            ],
        "limits" :
            [
                [0, 10],
                [0, 10000],
                [0.01, 0.05],
                [3.09, 3.1],
                [140,160]
            ]
    },

    "id_invMass_10_25_0_1.2" : {
        "pars" :
            [
                3.13,
                0.034,
                0.0305,
                3.096916,
                362
            ],
        "limits" :
            [
                [0, 10],
                [0, 100],
                [0.01, 0.05],
                [3.09, 3.1],
                [300,400]
            ]
    },
    
    "invMass_10_25_0_1.2" : {
        "pars" :
            [
                1,
                0,
                0.028,
                3.096916,
                365
            ],
        "limits" :
            [
                [1, 10],
                [0, 10],
                [0.01, 0.04],
                [3.09, 3.1],
                [350,400]
            ]
    },
    
    "id_invMass_10_25_1.2_2.4" : {
        "pars" :
            [
                3.15,
                4,
                0.028,
                3.096916,
                200
            ],
        "limits" :
            [
                [1, 5],
                [0, 10],
                [0.01, 0.06],
                [3.09, 3.1],
                [150,250]
            ]
    },


    "invMass_10_25_1.2_2.4" : {
        "pars" :
            [
                2.07,
                2.69,
                0.052,
                3.096916,
                189
            ],
        "limits" :
            [
                [1, 5],
                [0, 10],
                [0.01, 0.06],
                [3.09, 3.1],
                [150,195]
            ]
    },
    
}

crystalBallInitialConditionsGranularData = {
    
    "default" : {
         "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },

    "id_invMass_2_3_1.2_2.4" : {
        "pars" :
            [
                1.2,
                6,
                0.0476,
                3.096916,
                100
            ],
        "limits" :
            [
                [0, 5],
                [0, 10000],
                [0.02, 0.09],
                [3.09, 3.1],
                [70,120]
            ],
        "ignore" : False
    },
    
    "iso_invMass_2_3_1.2_2.4" : {
        "pars" :
            [
                5,
                6,
                0.0476,
                3.096916,
                50
            ],
        "limits" :
            [
                [0, 5],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [40,120]
            ],
        "ignore" : False
    },
    
    "invMass_2_3_1.2_2.4" : {
        "pars" :
            [
                6.07,
                5.606,
                0.046,
                3.096916,
                500
            ],
        "limits" :
            [
                [1, 10],
                [0, 10],
                [0.02, 0.09],
                [3.09, 3.1],
                [100,600]
            ],
        "ignore" : False
    },
    
    "id_invMass_3_4_0_1.2" : {
         "pars" :
            [
                1.2,
                10000000,
                0.025,
                3.096916,
                75.4
            ],
        "limits" :
            [
                [1, 10],
                [10000000, 100000000],
                [0.02, 0.06],
                [3.09, 3.1],
                [70,90]
            ],
        "ignore" : False
    },
    
    "iso_invMass_3_4_0_1.2" : {
         "pars" :
            [
                5,
                6,
                0.0476,
                3.096916,
                62
            ],
        "limits" :
            [
                [0, 5],
                [0, 1000],
                [0.02, 0.09],
                [3.09, 3.1],
                [50,100]
            ],
        "ignore" : False
    },
    
    "invMass_3_4_0_1.2" : {
        "pars" :
            [
                10,
                0,
                0.027,
                3.096916,
                218
            ],
        "limits" :
            [
                [5, 500],
                [0, 500],
                [0.01, 0.04],
                [3.09, 3.1],
                [200,250]
            ]
    },
    
    "id_invMass_3_4_1.2_2.4" : {
         "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                65
            ],
        "limits" :
            [
                [0, 100],
                [0, 10000],
                [0.02, 0.09],
                [3.09, 3.1],
                [60,70]
            ],
    },
    
    "iso_invMass_3_4_1.2_2.4" : {
         "pars" :
            [
                0,
                0,
                0.03,
                3.096916,
                55
            ],
        "limits" :
            [
                [0, 5],
                [0, 5],
                [0.02, 0.09],
                [3.09, 3.1],
                [40,70]
            ],
    },
    
    "invMass_3_4_1.2_2.4" : {
        "pars" :
            [
                1,
                5,
                0.055,
                3.096916,
                77
            ],
        "limits" :
            [
                [0, 1000],
                [-100, 1000],
                [0.02, 0.09],
                [3.09, 3.098],
                [50,200]
            ],
    },
    
    "id_invMass_4_5_0_1.2" : {
         "pars" :
            [
                10,
                10,
                0.055,
                3.096916,
                99
            ],
        "limits" :
            [
                [0, 1000],
                [0, 1000],
                [0.02, 0.09],
                [3.09, 3.1],
                [50,120]
            ],
    },
    
    "iso_invMass_4_5_0_1.2" : {
         "pars" :
            [
                0.1,
                15,
                0.055,
                3.096916,
                83
            ],
        "limits" :
            [
                [0.1, 100],
                [10, 100],
                [0.01, 0.09],
                [3.09, 3.1],
                [70,90]
            ],
    },
    
    "invMass_4_5_0_1.2" : {
        "pars" :
            [
                10,
                20,
                0.055,
                3.096916,
                115
            ],
        "limits" :
            [
                [1, 100],
                [5, 100],
                [0.015, 0.09],
                [3.09, 3.2],
                [100,150]
            ],
    },
    
    #CURRLINE
    
    "id_invMass_4_5_1.2_2.4" : {
        "pars" :
            [
                50,
                50,
                0.055,
                3.096916,
                53
            ],
        "limits" :
            [
                [10, 500],
                [10, 1000],
                [0.02, 0.09],
                [3.09, 3.1],
                [50,65]
            ],
    },
    
    "iso_invMass_4_5_1.2_2.4" : {
        "pars" :
            [
                0,
                15,
                0.055,
                3.096916,
                39
            ],
        "limits" :
            [
                [0, 10],
                [5, 20],
                [0.02, 0.09],
                [3.09, 3.2],
                [30,50]
            ],
    },

    
    "invMass_4_5_1.2_2.4" : {
        "pars" :
            [
                5,
                10,
                0.05,
                3.096916,
                67
            ],
        "limits" :
            [
                [0.1, 100],
                [0.1, 100],
                [0.02, 0.09],
                [3.09, 3.2],
                [40,100]
            ],
    },
    
    "id_invMass_5_10_0_1.2" : {
        "pars" :
            [
                7,
                80,
                0.055,
                3.096916,
                224
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [100,300]
            ],
    },
    
    "iso_invMass_5_10_0_1.2" : {
        "pars" :
            [
                4.3,
                81,
                0.055,
                3.096916,
                140
            ],
        "limits" :
            [
                [0, 10],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [130,150]
            ],
    },

    "invMass_5_10_0_1.2" : {
        "pars" :
            [
                0.5,
                8.1,
                0.055,
                3.096916,
                244
            ],
        "limits" :
            [
                [0, 1],
                [5, 10],
                [0.02, 0.09],
                [3.09, 3.1],
                [200,300]
            ],
    },
    
    "id_invMass_5_10_1.2_2.4" : {
        "pars" :
            [
                1,
                1000,
                0.055,
                3.096916,
                108
            ],
        "limits" :
            [
                [1, 100],
                [100, 10000],
                [0.02, 0.09],
                [3.09, 3.1],
                [90,120]
            ],
    },
    
    "iso_invMass_5_10_1.2_2.4" : {
        "pars" :
            [
                46,
                200,
                0.055,
                3.096916,
                62
            ],
        "limits" :
            [
                [1, 100],
                [150, 300],
                [0.02, 0.09],
                [3.09, 3.1],
                [50,70]
            ],
    },
  
    "invMass_5_10_1.2_2.4" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },

    "id_invMass_10_20_0_1.2" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "iso_invMass_10_20_0_1.2" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "invMass_10_20_0_1.2" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
#CURRLINE
    
    "default" : {
         "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "id_invMass_10_20_1.2_2.4" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "iso_invMass_10_20_1.2_2.4" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },

    "invMass_10_20_1.2_2.4" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
}

crystalBallInitialConditionsGranularBg = {
    
    "default" : {
         "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },

    "id_invMass_2_3_1.2_2.4" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "iso_invMass_2_3_1.2_2.4" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "invMass_2_3_1.2_2.4" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "id_invMass_3_4_0_1.2" : {
         "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                60
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [50,70]
            ],
    },
    
    "iso_invMass_3_4_0_1.2" : {
         "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "invMass_3_4_0_1.2" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                122
            ],
        "limits" :
            [
                [0, 100],
                [1, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [120,140]
            ],
    },
    
    "id_invMass_3_4_1.2_2.4" : {
         "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "iso_invMass_3_4_1.2_2.4" : {
         "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "invMass_3_4_1.2_2.4" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
        #HERE
    
    "id_invMass_4_5_0_1.2" : {
         "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "iso_invMass_4_5_0_1.2" : {
         "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "invMass_4_5_0_1.2" : {
        "pars" :
            [
                1,
                3,
                0.055,
                3.096916,
                100
            ],
        "limits" :
            [
                [0, 100],
                [1, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [50,150]
            ],
    },
    
    #CURRLINE
    
    "id_invMass_4_5_1.2_2.4" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                45
            ],
        "limits" :
            [
                [1, 100],
                [1, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [30,50]
            ],
    },
    
    "iso_invMass_4_5_1.2_2.4" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },

    
    "invMass_4_5_1.2_2.4" : {
        "pars" :
            [
                5,
                8,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [1, 100],
                [2, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "id_invMass_5_10_0_1.2" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                295
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [200,350]
            ],
    },
    
    "iso_invMass_5_10_0_1.2" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },

    "invMass_5_10_0_1.2" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                300
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [250,400]
            ],
    },
    
    "id_invMass_5_10_1.2_2.4" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                120
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [100,150]
            ],
    },
    
    "iso_invMass_5_10_1.2_2.4" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
  
    "invMass_5_10_1.2_2.4" : {
        "pars" :
            [
                5,
                50,
                0.055,
                3.096916,
                124
            ],
        "limits" :
            [
                [0, 100],
                [10, 100000],
                [0.02, 0.09],
                [3.09, 3.1],
                [100,130]
            ],
    },

    "id_invMass_10_20_0_1.2" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "iso_invMass_10_20_0_1.2" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "invMass_10_20_0_1.2" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
#CURRLINE
    
    "default" : {
         "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },
    
    "id_invMass_10_20_1.2_2.4" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                100
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [50,150]
            ],
    },
    
    "iso_invMass_10_20_1.2_2.4" : {
        "pars" :
            [
                5,
                5,
                0.055,
                3.096916,
                500
            ],
        "limits" :
            [
                [0, 100],
                [0, 100],
                [0.02, 0.09],
                [3.09, 3.1],
                [0,10000]
            ],
    },

    "invMass_10_20_1.2_2.4" : {
        "pars" :
            [
                5,
                6,
                0.055,
                3.096916,
                100
            ],
        "limits" :
            [
                [1, 10],
                [5, 10],
                [0.02, 0.09],
                [3.09, 3.1],
                [50,150]
            ],
    },
    
}

# crystalBallInitialConditionsData = {
# 
#     "id_invMass_2_3_1.2_2.4" : {
#         "pars" :
#             [
#                 5,
#                 6,
#                 0.0476,
#                 3.096916,
#                 7800
#             ],
#         "limits" :
#             [
#                 [0, 5],
#                 [0, 100],
#                 [0.02, 0.09],
#                 [3.09, 3.1],
#                 [7000,8500]
#             ],
#         "ignore" : False
#     },
#     
#     "invMass_2_3_1.2_2.4" : {
#         "pars" :
#             [
#                 6.07,
#                 5.606,
#                 0.046,
#                 3.096916,
#                 20000
#             ],
#         "limits" :
#             [
#                 [1, 10],
#                 [0, 10],
#                 [0.02, 0.09],
#                 [3.09, 3.1],
#                 [10000,50000]
#             ],
#         "ignore" : False
#     },
#     
#     "id_invMass_3_5_0_1.2" : {
#          "pars" :
#             [
#                 5,
#                 6,
#                 0.0476,
#                 3.096916,
#                 8000
#             ],
#         "limits" :
#             [
#                 [0, 5],
#                 [0, 1000],
#                 [0.02, 0.09],
#                 [3.09, 3.1],
#                 [7000,8500]
#             ],
#         "ignore" : False
#     },
#     
#     "invMass_3_5_0_1.2" : {
#         "pars" :
#             [
#                 1.7,
#                 0.8,
#                 0.027,
#                 3.096916,
#                 17000
#             ],
#         "limits" :
#             [
#                 [0, 5],
#                 [0, 5],
#                 [0.01, 0.04],
#                 [3.09, 3.1],
#                 [10000,20000]
#             ]
#     },
#     
#     # HERE
#     
#     "id_invMass_3_4_0_1.2" : {
#          "pars" :
#             [
#                 5,
#                 6,
#                 0.0476,
#                 3.096916,
#                 8000
#             ],
#         "limits" :
#             [
#                 [0, 5],
#                 [0, 1000],
#                 [0.02, 0.09],
#                 [3.09, 3.1],
#                 [5500,8500]
#             ],
#         "ignore" : False
#     },
#     
#     "invMass_3_4_0_1.2" : {
#         "pars" :
#             [
#                 10,
#                 0,
#                 0.027,
#                 3.096916,
#                 14000
#             ],
#         "limits" :
#             [
#                 [5, 500],
#                 [0, 500],
#                 [0.01, 0.04],
#                 [3.09, 3.1],
#                 [10000,16000]
#             ]
#     },
#     
#     # HERE
#     
#     
#     
#     "id_invMass_4_5_0_1.2" : {
#          "pars" :
#             [
#                 0,
#                 0,
#                 0.0476,
#                 3.096916,
#                 1500
#             ],
#         "limits" :
#             [
#                 [0, 5],
#                 [0, 5],
#                 [0.02, 0.09],
#                 [3.09, 3.105],
#                 [1000,2000]
#             ],
#         "ignore" : False
#     },
#     
#     "invMass_4_5_0_1.2" : {
#         "pars" :
#             [
#                 10,
#                 10,
#                 0.027,
#                 3.096916,
#                 1658
#             ],
#         "limits" :
#             [
#                 [0, 20],
#                 [0, 20],
#                 [0.01, 0.04],
#                 [3.09, 3.15],
#                 [1500,1700]
#             ]
#     },
#     
#     
#     "id_invMass_3_5_1.2_2.4" : {
#         "pars" :
#             [
#                 1.6,
#                 0,
#                 0.047,
#                 3.096916,
#                 6754
#             ],
#         "limits" :
#             [
#                 [0, 5],
#                 [0, 10000],
#                 [0.02, 0.09],
#                 [3.09, 3.1],
#                 [6000,7000]
#             ],
#         "ignore" : False
#     },
# 
#     
#     "invMass_3_5_1.2_2.4" : {
#         "pars" :
#             [
#                 500,
#                 0.8,
#                 0.027,
#                 3.096916,
#                 8000
#             ],
#         "limits" :
#             [
#                 [2, 1000],
#                 [0, 100],
#                 [0.01, 0.07],
#                 [3.09, 3.1],
#                 [7000,8500]
#             ]
#     },
#     
#     # HERE
#     
#     "id_invMass_3_4_1.2_2.4" : {
#         "pars" :
#             [
#                 1,
#                 0,
#                 0.047,
#                 3.096916,
#                 5000
#             ],
#         "limits" :
#             [
#                 [0, 5],
#                 [0, 10000],
#                 [0.02, 0.09],
#                 [3.09, 3.1],
#                 [4000,7000]
#             ],
#         "ignore" : False
#     },
# 
#     
#     "invMass_3_4_1.2_2.4" : {
#         "pars" :
#             [
#                 500,
#                 0.8,
#                 0.027,
#                 3.096916,
#                 7000
#             ],
#         "limits" :
#             [
#                 [0, 1000],
#                 [0, 100],
#                 [0.01, 0.07],
#                 [3.09, 3.1],
#                 [5000,8500]
#             ]
#     },
#     
#     "id_invMass_4_5_1.2_2.4" : {
#         "pars" :
#             [
#                 800,
#                 10,
#                 0.045,
#                 3.096916,
#                 740
#             ],
#         "limits" :
#             [
#                 [500, 1000],
#                 [0, 100],
#                 [0.02, 0.09],
#                 [3.09, 3.11],
#                 [600,850]
#             ],
#         "ignore" : False
#     },
# 
#     
#     "invMass_4_5_1.2_2.4" : {
#         "pars" :
#             [
#                 0,
#                 0,
#                 0.027,
#                 3.096916,
#                 1000
#             ],
#         "limits" :
#             [
#                 [0, 1000],
#                 [0, 10000],
#                 [0.01, 0.07],
#                 [3.09, 3.15],
#                 [500,2000]
#             ]
#     },
#     
#     "id_invMass_5_10_0_1.2" : {
#         "pars" :
#             [
#                 1.6,
#                 0,
#                 0.047,
#                 3.096916,
#                 1800
#             ],
#         "limits" :
#             [
#                 [0, 5],
#                 [0, 10000],
#                 [0.01, 0.09],
#                 [3.09, 3.1],
#                 [1000,2000]
#             ],
#         "ignore" : False
#     },
# 
#     "invMass_5_10_0_1.2" : {
#         "pars" :
#             [
#                 0,
#                 0.8,
#                 0.027,
#                 3.096916,
#                 1785
#             ],
#         "limits" :
#             [
#                 [0, 1000],
#                 [0, 100],
#                 [0.01, 0.07],
#                 [3.09, 3.1],
#                 [1000,5000]
#             ]
#     },
#     
#     "id_invMass_5_10_1.2_2.4" : {
#         "pars" :
#             [
#                 2,
#                 1000,
#                 0.05,
#                 3.096916,
#                 1478
#             ],
#         "limits" :
#             [
#                 [0, 20000],
#                 [0, 10000],
#                 [0.01, 0.07],
#                 [3.09, 3.1],
#                 [1200,1700]
#             ],
#         "ignore" : False
#     },
#   
#     "invMass_5_10_1.2_2.4" : {
#         "pars" :
#             [
#                 5,
#                 1,
#                 0.027,
#                 3.096916,
#                 1600
#             ],
#         "limits" :
#             [
#                 [0, 10000],
#                 [0, 50000],
#                 [0.01, 0.07],
#                 [3.09, 3.1],
#                 [1000,2000]
#             ]
#     },
# 
#     "id_invMass_10_25_0_1.2" : {
#         "pars" :
#             [
#                 0,
#                 0,
#                 0.05,
#                 3.096916,
#                 4800
#             ],
#         "limits" :
#             [
#                 [0, 200],
#                 [0, 100],
#                 [0.01, 0.07],
#                 [3.09, 3.1],
#                 [1000,10000]
#             ],
#         "ignore" : False
#     },
#     
#     "invMass_10_25_0_1.2" : {
#         "pars" :
#             [
#                 1.2,
#                 1,
#                 0.027,
#                 3.096916,
#                 3839
#             ],
#         "limits" :
#             [
#                 [0, 100],
#                 [0, 100],
#                 [0.01, 0.07],
#                 [3.09, 3.1],
#                 [3500,4000]
#             ]
#     },
#     
#     "id_invMass_10_25_1.2_2.4" : {
#         "pars" :
#             [
#                 1.4,
#                 5000,
#                 0.05,
#                 3.096916,
#                 2100
#             ],
#         "limits" :
#             [
#                 [0, 2],
#                 [500, 10000],
#                 [0.01, 0.07],
#                 [3.09, 3.1],
#                 [1000,3000]
#             ],
#         "ignore" : False
#     },
# 
# 
#     "invMass_10_25_1.2_2.4" : {
#         "pars" :
#             [
#                 1,
#                 1000,
#                 0.027,
#                 3.096916,
#                 2100
#             ],
#         "limits" :
#             [
#                 [0, 10],
#                 [0, 50000000],
#                 [0.01, 0.07],
#                 [3.09, 3.1],
#                 [2000,5000]
#             ]
#     },
#     
# }


class jpsi_muons_new_normalised_fit_bg(jpsi_muons_ex_track_new):
    fit_inv_mass_jpsi = True
    fit_inv_mass_obs_jpsi = "invMass"
    fit_inv_mass_cut_jpsi = "none"
    #fit_inv_mass_jpsi_func = "lorentzian"
    fit_inv_mass_jpsi_func = "doubleGaussian"
    
    #fit_inv_mass_jpsi_func = "gauss"
    
    #fit_inv_mass_jpsi_func = "crystalBall"
    
    #fit_inv_mass_jpsi_func = "crystalBall2"
    
    fit_inv_mass_jpsi_bg_func = "quad"
    fit_inv_mass_jpsi_func_bg = True
    plot_error = True
    nostack = False
    #solid_bg = True
    #plot_bg = False
    plot_ratio = False
    #pt_ranges = [2,3,4,5,10,25]
    pt_ranges = [2,3,5,10,25]
    eta_ranges = [0,1.2,2.4]
    plot_bg = True
    plot_data = False
    
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        'SingleMuon' : "puWeight"
    }
    #NEED TO DO SOMETHING ABOUT THE NORMALISATION OF THE LUMI!!!
    calculatedLumi = {
        'SingleMuonReco' : 0.001,
        'SingleMuon' : 22.944,
    }
    
    #calculatedLumi = {
    #    'SingleMuonReco' : 0.001,
    #    'SingleMuon' : 0.001,
    #}
    
    save_histrograms_to_file = True
    load_histrograms_from_file = True    
    
    create_canvas = False
    
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/invMassBgHists.root"
    
    #solid_bg = True
    
    histograms_defs = [
        #{ "obs" : "invMass", "units" : "M_{ll}", "minX" : 2.5, "maxX" : 3.5, "bins" : 60},
    ]
    
    cuts = [
        {"name":"none", "title": "No Cuts", "condition" : "1"},
    ]
        
    for pti in range(len(pt_ranges)):
        if pti == len(pt_ranges) - 1:
            continue
        pt1 = pt_ranges[pti]
        pt2 = pt_ranges[pti+1]
       
        for etai in range(len(eta_ranges)):
            if etai == len(eta_ranges) - 1:
                continue
            eta1 = eta_ranges[etai]
            eta2 = eta_ranges[etai+1]
            
            obsBaseName = "invMass_"+str(pt1)+"_"+str(pt2)+"_"+str(eta1)+"_"+str(eta2)
            
            #if "invMass_2_3_0_1.2" in obsBaseName:
            #    continue
                
            
            #if "invMass_4_5_1.2_2.4" != obsBaseName:
            #    continue
        
            histograms_defs.append({ "obs" : "id_" + obsBaseName, "formula" : "invMass", "units" : "M_{ll} Id Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks_mi[probeTrack] > -1 && Muons_mediumID[tracks_mi[probeTrack]] == 1 && tracks[probeTrack].Pt() >= " + str(pt1) + " && tracks[probeTrack].Pt() <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2) })#&& tracks_trkRelIso[ti] < 0.1 #track.Pt() <= 10 && 
            #histograms_defs.append({ "obs" : "reco_" + obsBaseName, "formula" : "invMass", "units" : "M_{ll} Reco Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks_mi[probeTrack] > -1 && tracks[probeTrack].Pt() >= " + str(pt1) + " && tracks[probeTrack].Pt() <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2) })#&& tracks_trkRelIso[ti] < 0.1 #track.Pt() <= 10 && 
            histograms_defs.append({ "obs" : obsBaseName, "formula" : "invMass", "units" : "M_{ll} Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks[probeTrack].Pt() >= " + str(pt1) + " && tracks[probeTrack].Pt() <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2) })
            

class jpsi_muons_new_normalised_fit_data(jpsi_muons_new_normalised_fit_bg):
    plot_bg = False
    plot_data = True
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/invMassDataHists.root"
    fit_inv_mass_jpsi_func_bg = False
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        'SingleMuon' : "passedSingleMuPack"
    }


class jpsi_muons_new_normalised_fit_bg_granular(jpsi_muons_new_normalised_fit_bg):

    crystalBallInitialConditions = crystalBallInitialConditionsGranularBg
    
    #fit_inv_mass_jpsi_func = "doubleGaussian"
    fit_inv_mass_jpsi_func = "crystalBall"
    
    calculatedLumi = {
        'SingleMuonReco' : 0.001,
        'SingleMuon' : 0.001,
    }

    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/invMassBgGranularHists.root"
    
    cuts = [
        #{"name":"none", "title": "No Cuts", "condition" : "1"},
        {"name":"tag_muon", "title": "Tag Muon < 20 GeV", "condition" : "Muons[tagMuon].Pt() < 20"},
    ]
    
    histograms_defs = [
        #{ "obs" : "invMass", "units" : "M_{ll}", "minX" : 2.5, "maxX" : 3.5, "bins" : 60},
    ]
    
    eta_ranges = [0,1.2,2.4]
    pt_ranges = [2,3,4,5,10,20,25]
    
    fit_inv_mass_cut_jpsi = "tag_muon"
    
    for pti in range(len(pt_ranges)):
        if pti == len(pt_ranges) - 1:
            continue
        pt1 = pt_ranges[pti]
        pt2 = pt_ranges[pti+1]
       
        for etai in range(len(eta_ranges)):
            if etai == len(eta_ranges) - 1:
                continue
            eta1 = eta_ranges[etai]
            eta2 = eta_ranges[etai+1]
            
            obsBaseName = "invMass_"+str(pt1)+"_"+str(pt2)+"_"+str(eta1)+"_"+str(eta2)
            
            if "invMass_2_3_0_1.2" in obsBaseName:
                continue
                
            
            #if "invMass_2_3_1.2_2.4" != obsBaseName:
            #    continue
            
            #if "invMass_3_4_0_1.2" != obsBaseName:
            #    continue
            
            #if "invMass_10_20_1.2_2.4" != obsBaseName:
            #    continue
        
            histograms_defs.append({ "obs" : "id_" + obsBaseName, "formula" : "invMass", "units" : "M_{ll} Id Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks_mi[probeTrack] > -1 && Muons_mediumID[tracks_mi[probeTrack]] == 1 && tracks[probeTrack].Pt() >= " + str(pt1) + " && tracks[probeTrack].Pt() <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2) })#&& tracks_trkRelIso[ti] < 0.1 #track.Pt() <= 10 && 
            #histograms_defs.append({ "obs" : "reco_" + obsBaseName, "formula" : "invMass", "units" : "M_{ll} Reco Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks_mi[probeTrack] > -1 && tracks[probeTrack].Pt() >= " + str(pt1) + " && tracks[probeTrack].Pt() <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2) })#&& tracks_trkRelIso[ti] < 0.1 #track.Pt() <= 10 && 
            histograms_defs.append({ "obs" : "iso_" + obsBaseName, "formula" : "invMass", "units" : "M_{ll} Iso Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks_mi[probeTrack] > -1 && Muons_mediumID[tracks_mi[probeTrack]] == 1 && tracks[probeTrack].Pt() >= " + str(pt1) + " && tracks[probeTrack].Pt() <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2)  + " && Muons_passCorrJetIso10[tracks_mi[probeTrack]] == 1" })
            histograms_defs.append({ "obs" : obsBaseName, "formula" : "invMass", "units" : "M_{ll} Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks[probeTrack].Pt() >= " + str(pt1) + " && tracks[probeTrack].Pt() <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2) })
            

class jpsi_muons_new_normalised_fit_data_granular(jpsi_muons_new_normalised_fit_bg_granular):
    plot_bg = False
    plot_data = True
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/invMassDataGranularHists.root"
    fit_inv_mass_jpsi_func_bg = False
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        'SingleMuon' : "passedSingleMuPack"
    }
    
    crystalBallInitialConditions = crystalBallInitialConditionsGranularData
    
    fit_inv_mass_jpsi_func = "crystalBall"
    #fit_inv_mass_jpsi_func = "crystalBall"
    #fit_inv_mass_jpsi_func = "lorentzian"
    #fit_inv_mass_jpsi_func = "doubleGaussian"
    #fit_inv_mass_jpsi_func = "gauss"
    
    #fit_inv_mass_jpsi_func = "doubleGaussian"
    

crystalBallInitialConditionsOrig = {

    "id_invMass_2_3_1.2_2.4" : {
        "pars" :
            [
                3.27,
                4.57,
                0.043,
                3.096916,
                70
            ],
        "limits" :
            [
                [1, 30],
                [0, 100],
                [0.005, 0.1],
                [3.09, 3.1],
                [0,100]
            ]
    },
    
}


class jpsi_muons_jpsi_shape_comp(jpsi_muons_new_normalised_fit_bg):
    save_histrograms_to_file = False
    load_histrograms_from_file = False
    histograms_defs = [
    ]
    
    cuts = [
        {"name":"none", "title": "No Cuts", "condition" : "1"},
    ]
    
    pt_ranges = [2,3,5,10,25]
    eta_ranges = [0,1.2,2.4]
    
    for pti in range(len(pt_ranges)):
        if pti == len(pt_ranges) - 1:
            continue
        pt1 = pt_ranges[pti]
        pt2 = pt_ranges[pti+1]
        
        for etai in range(len(eta_ranges)):
            if etai == len(eta_ranges) - 1:
                continue
            eta1 = eta_ranges[etai]
            eta2 = eta_ranges[etai+1]
            histograms_defs.append({ "obs" : "invMass_"+str(pt1)+"_"+str(pt2)+"_"+str(eta1)+"_"+str(eta2), "formula" : "invMass", "units" : "M_{ll} Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks[probeTrack].Pt() >= " + str(pt1) + " && tracks[probeTrack].Pt() <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2) })
    bgReTagging = {
        "jpsi" : "tagJpsi == 1 && probeJpsi == 1",
        "id" : "(tagJpsi == 1 && probeJpsi == 1) && tracks_mi[probeTrack] > -1 && Muons_mediumID[tracks_mi[probeTrack]] == 1",
    }

    bgReTaggingOrder = {
        "jpsi" : 0,
        "id" : 1
    }
    
    nostack = True
    fit_inv_mass_jpsi = False
    fit_inv_mass_jpsi_func_bg = False
    customRatios = [  [["id"],["jpsi"]]  ]
    plot_custom_ratio = True

class jpsi_muons_ex_track_normalised(jpsi_muons_ex_track):
    normalise = False
    no_weights = True
    plot_data = False
    plot_ratio = False

class jpsi_muons_ex_track_normalised_fit(jpsi_muons_ex_track_normalised):
    fit_inv_mass_jpsi = True
    fit_inv_mass_obs_jpsi = "invMass"
    fit_inv_mass_cut_jpsi = "none"
    fit_inv_mass_jpsi_func = "lorentzian"
    fit_inv_mass_jpsi_func_bg = False
    plot_error = True
    nostack = False
    #solid_bg = True
    #plot_bg = False
    plot_ratio = False
    pt_ranges = [2,3,5,10,25]
    eta_ranges = [0,1.2,2.4]
    plot_bg = False
    plot_data = True
    
    normalise = False
    no_weights = False
    
    histograms_defs = [
        { "obs" : "exTrack_invMass", "units" : "M_{ll}", "minX" : 2.5, "maxX" : 3.5, "bins" : 60},
    ]
    
    cuts = [
        #{"name":"none", "title": "No Cuts", "condition" : "exclusiveTrack == 1 && passedSingleMuPack == 1 && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 8 && track.Pt() < 25 && exTrack_deltaR < 0.7"},
        
        {"name":"none", "title": "Loose", "condition" : "exclusiveTrack == 1 && passedSingleMuPack == 1 && Muons_tightID[leptonIdx] == 1 && lepton.Pt() > 8 && track.Pt() < 25"},
        #
        #{"name":"none", "title": "Looser", "condition" : "exclusiveTrack == 1 && passedSingleMuPack == 1 && lepton.Pt() > 4 && track.Pt() < 25"},
        #{"name":"none", "title": "Ht", "condition" : "Ht > 100 && exclusiveTrack == 1 && passedSingleMuPack == 1 && lepton.Pt() > 4 && track.Pt() < 25"},
        
        #{"name":"none", "title": "Low", "condition" : "Ht < 600 && Ht > 100 && exclusiveTrack == 1 &&  passedSingleMuPack == 1 && lepton.Pt() > 6 && track.Pt() < 25 && abs(track.Eta()) < 2.4 && track.Pt() >= 2 && track.Pt() <= 3 && Muons[0].Pt() < 100"},
        
        
        
        
        
        #{"name":"none", "title": "No Cuts", "condition" : "Ht > 200 && exclusiveTrack == 1 && passedSingleMuPack == 1"},
        #{"name":"jpsi", "title": "jpsi", "condition" : "Ht > 200 && exclusiveTrack == 1 && exTrack_invMass > 3.04 && exTrack_invMass < 3.18 && passedSingleMuPack == 1"},
    ]
    for pti in range(len(pt_ranges)):
        if pti == len(pt_ranges) - 1:
            continue
        pt1 = pt_ranges[pti]
        pt2 = pt_ranges[pti+1]
        if False:#pt1 == 2:
            histograms_defs.append({ "obs" : "exTrack_invMass_"+str(pt1)+"_"+str(pt2), "formula" : "exTrack_invMass", "units" : "M_{ll} Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [1.2,2.4]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "track.Pt() >= " + str(pt1) + " && track.Pt() <= " + str(pt2) + " && abs(track.Eta()) >= 1.2  && abs(track.Eta()) <= 2.4" })
        else:
            for etai in range(len(eta_ranges)):
                if etai == len(eta_ranges) - 1:
                    continue
                eta1 = eta_ranges[etai]
                eta2 = eta_ranges[etai+1]
                histograms_defs.append({ "obs" : "exTrack_invMass_"+str(pt1)+"_"+str(pt2)+"_"+str(eta1)+"_"+str(eta2), "formula" : "exTrack_invMass", "units" : "M_{ll} Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "track.Pt() >= " + str(pt1) + " && track.Pt() <= " + str(pt2) + " && abs(track.Eta()) >= " + str(eta1) + " && abs(track.Eta()) <= " + str(eta2) })
    
    #histograms_defs.append({ "obs" : "cut_exTrack_invMass", "formula" : "exTrack_invMass", "units" : "M_{ll} Cut", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "abs(track.Eta()) < 2.4 && tracks_dxyVtx[ti] < 0.02 && tracks_dzVtx[ti] < 0.02"})# && tracks_trkRelIso[ti] < 0.1
    histograms_defs.append({ "obs" : "reco_exTrack_invMass", "formula" : "exTrack_invMass", "units" : "M_{ll} Reco", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks_mi[ti] > -1"})# && tracks_trkRelIso[ti] < 0.1
    histograms_defs.append({ "obs" : "id_exTrack_invMass", "formula" : "exTrack_invMass", "units" : "M_{ll} Id", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "abs(track.Eta()) < 2.4 && tracks_mi[ti] > -1 && Muons_mediumID[tracks_mi[ti]] == 1"})# && tracks_trkRelIso[ti] < 0.1
    
    
    for pti in range(len(pt_ranges)):
        if pti == len(pt_ranges) - 1:
            continue
        pt1 = pt_ranges[pti]
        pt2 = pt_ranges[pti+1]
        if False:#pt1 == 2:
            #histograms_defs.append({ "obs" : "cut_exTrack_invMass_"+str(pt1)+"_"+str(pt2), "formula" : "exTrack_invMass", "units" : "M_{ll} Cut Pt \in [" + str(pt1) + ", " + str(pt2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "abs(track.Eta()) < 2.4 && tracks_dxyVtx[ti] < 0.02 && tracks_dzVtx[ti] < 0.02 && track.Pt() >= " + str(pt1) + " && track.Pt() <= " + str(pt2)}) #&& tracks_trkRelIso[ti] < 0.1#track.Pt() <= 10 && 
            histograms_defs.append({ "obs" : "reco_exTrack_invMass_"+str(pt1)+"_"+str(pt2), "formula" : "exTrack_invMass", "units" : "M_{ll} Reco Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [1.2,2.4]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks_mi[ti] > -1 && track.Pt() >= " + str(pt1) + " && track.Pt() <= " + str(pt2) + " && abs(track.Eta()) >= 1.2  && abs(track.Eta()) <= 2.4"})
            histograms_defs.append({ "obs" : "id_exTrack_invMass_"+str(pt1)+"_"+str(pt2), "formula" : "exTrack_invMass", "units" : "M_{ll} Id Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [1.2,2.4]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "abs(track.Eta()) < 2.4 && tracks_mi[ti] > -1 && Muons_mediumID[tracks_mi[ti]] == 1 && track.Pt() >= " + str(pt1) + " && track.Pt() <= " + str(pt2) + " && abs(track.Eta()) >= 1.2  && abs(track.Eta()) <= 2.4"})
        else:
            for etai in range(len(eta_ranges)):
                if etai == len(eta_ranges) - 1:
                    continue
                eta1 = eta_ranges[etai]
                eta2 = eta_ranges[etai+1]
                #histograms_defs.append({ "obs" : "cut_exTrack_invMass_"+str(pt1)+"_"+str(pt2)+"_"+str(eta1)+"_"+str(eta2), "formula" : "exTrack_invMass", "units" : "M_{ll} Cut Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "abs(track.Eta()) < 2.4 && tracks_dxyVtx[ti] < 0.02 && tracks_dzVtx[ti] < 0.02 && track.Pt() >= " + str(pt1) + " && track.Pt() <= " + str(pt2) + " && abs(track.Eta()) >= " + str(eta1) + " && abs(track.Eta()) <= " + str(eta2) })#&& tracks_trkRelIso[ti] < 0.1 #track.Pt() <= 10 && 
                histograms_defs.append({ "obs" : "reco_exTrack_invMass_"+str(pt1)+"_"+str(pt2)+"_"+str(eta1)+"_"+str(eta2), "formula" : "exTrack_invMass", "units" : "M_{ll} Reco Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks_mi[ti] > -1 && track.Pt() >= " + str(pt1) + " && track.Pt() <= " + str(pt2) + " && abs(track.Eta()) >= " + str(eta1) + " && abs(track.Eta()) <= " + str(eta2) })#&& tracks_trkRelIso[ti] < 0.1 #track.Pt() <= 10 && 
                histograms_defs.append({ "obs" : "id_exTrack_invMass_"+str(pt1)+"_"+str(pt2)+"_"+str(eta1)+"_"+str(eta2), "formula" : "exTrack_invMass", "units" : "M_{ll} Id Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "abs(track.Eta()) < 2.4 && tracks_mi[ti] > -1 && Muons_mediumID[tracks_mi[ti]] == 1 && track.Pt() >= " + str(pt1) + " && track.Pt() <= " + str(pt2) + " && abs(track.Eta()) >= " + str(eta1) + " && abs(track.Eta()) <= " + str(eta2) })#&& tracks_trkRelIso[ti] < 0.1 #track.Pt() <= 10 && 
                
                

class jpsi_muons_ex_track_normalised_fit_bg(jpsi_muons_ex_track_normalised_fit):
    fit_inv_mass_jpsi_func_bg = True
    plot_data = False
    plot_bg = True

class jpsi_muons_normalised(jpsi_muons):
    normalise = True
    no_weights = True
    
class jpsi_muons_reco(jpsi_muons):
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_muons_jpsi_reco/sum/type_sum"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_muons_jpsi_reco_reco/sum"
    plot_kind = "SingleMuonReco"

class jpsi_muons_reco_normalised(jpsi_muons_reco):
    normalise = True
    no_weights = True
    
    
class jpsi_muons_n_plot(jpsi_muons):
    cuts = [
        #{"name":"none", "title": "No Cuts", "condition" : "1"},
        #{"name":"jpsi_invmass", "title": "jpsi", "condition" : "Muons_tightID[0] == 1 && Muons_passIso[0] == 1 && Muons[0].Pt() > 24 && Muons[0].Eta() < 2.4 && invMass > 3 && invMass < 3.2"},
        {"name":"jpsi", "title": "jpsi", "condition" : "invMass > 3.04 && invMass < 3.18"},
    ]
    
    #histograms_defs = [
        #{ "obs" : "invMass", "units" : "M_{ll}", "minX" : 3.04, "maxX" : 3.18, "bins" : 60 },
    #]
    histograms_defs = []
    for histdef in jpsi_muons.histograms_defs:
        histograms_defs.append(histdef)
    histograms_defs[0] = { "obs" : "invMass", "units" : "M_{ll}", "minX" : 3.04, "maxX" : 3.18, "bins" : 60 }
    bgReTagging = {
        "all" : "(Muons_ti[leptonsIdx] > -1 && tracks_trkRelIso[Muons_ti[leptonsIdx]] < 0.1 && tracks_dxyVtx[Muons_ti[leptonsIdx]] < 0.02 && tracks_dzVtx[Muons_ti[leptonsIdx]] < 0.05)",
        #"all" : "1",
        "trkRelIso" : "(Muons_ti[leptonsIdx] > -1 && tracks_dxyVtx[Muons_ti[leptonsIdx]] < 0.02 && tracks_dzVtx[Muons_ti[leptonsIdx]] < 0.05)",
        "dxy" : "(Muons_ti[leptonsIdx] > -1 && tracks_trkRelIso[Muons_ti[leptonsIdx]] < 0.1 && tracks_dzVtx[Muons_ti[leptonsIdx]] < 0.05)",
        "dz" : "(Muons_ti[leptonsIdx] > -1 && tracks_trkRelIso[Muons_ti[leptonsIdx]] < 0.1 && tracks_dxyVtx[Muons_ti[leptonsIdx]] < 0.02)",
        "none" : "(Muons_ti[leptonsIdx] > -1)"
    }
    
    bgReTaggingOrder = {
        "all" : 4,
        "trkRelIso" : 1,
        "dxy" : 2,
        "dz" : 3,
        "none" : 0
    }
    
    plot_data = False
    plot_ratio = False
    nostack = True
    customRatios = [  [["trkRelIso"],["all"]]  ]
    plot_custom_ratio = False
    plot_point = True
    plot_error = True
    plot_efficiency = True
    efficiencies = [ 
        {"name" : "trkRelIso", "numerator" : ["all"], "denominator": ["trkRelIso"] },
        {"name" : "dxy", "numerator" : ["all"], "denominator": ["dxy"] },
        {"name" : "dz", "numerator" : ["all"], "denominator": ["dz"] },
    ]
    
    # if c.tracks_trkRelIso[ti] > 0.1:
#                             continue 
#                         if c.tracks_dxyVtx[ti] > 0.02:
#                             continue
#                         if c.tracks_dzVtx[ti] > 0.05:
#                             continue 
    

class jpsi_muons_n_plot_normalised(jpsi_muons_n_plot):
    normalise = True
    no_weights = True

class jpsi_muons_fit_invmass(jpsi_muons):
    fit_inv_mass_jpsi = True
    fit_inv_mass_obs_jpsi = "invMass"
    fit_inv_mass_cut_jpsi = "none"
    #fit_inv_mass_jpsi_func = "lorentzian"
    fit_inv_mass_jpsi_func_bg = False
    plot_error = True
    nostack = False
    solid_bg = True
    
    histograms_defs = [
        { "obs" : "invMass", "units" : "M_{ll}", "minX" : 2.5, "maxX" : 3.5, "bins" : 60 },  
    ]
    
    # histograms_defs = [
#          { "obs" : "Ht", "units" : "Ht", "minX" : 0, "maxX" : 1000, "bins" : 100 },
#          { "obs" : "madHT", "units" : "madHT", "minX" : 0, "maxX" : 400, "bins" : 100 },
#          { "obs" : "NJets", "units" : "NJets", "minX" : 0, "maxX" : 5, "bins" : 5 },
#     ]
    
    cuts = [
        {"name":"none", "title": "No Cuts", "condition" : "twoLeptons == 1 && passedSingleMuPack == 1"},
        {"name":"jpsi", "title": "jpsi", "condition" : "twoLeptons == 1 && invMass > 3.04 && invMass < 3.18 && passedSingleMuPack == 1"},
    ]
    

class jpsi_muons_fit_invmass_ex_track(jpsi_muons_fit_invmass):
    cuts = [
        {"name":"none", "title": "No Cuts", "condition" : "twoLeptons == 1 && passedSingleMuPack == 1"},
        #{"name":"jpsi", "title": "jpsi", "condition" : "twoLeptons == 1 && invMass > 3.04 && invMass < 3.18 && passedSingleMuPack == 1"},
    ]

class jpsi_muons_fit_invmass_categories(jpsi_muons_fit_invmass):
    cuts = [
        {"name":"none", "title": "No Cuts", "condition" : "twoLeptons == 1 && passedSingleMuPack == 1"}
        #{"name":"jpsi", "title": "jpsi", "condition" : "twoLeptons == 1 && invMass > 3.04 && invMass < 3.18 && passedSingleMuPack == 1"},
    ]
    
    pt_ranges = [2,5,10,24]
    eta_ranges = [0,1.2,2.4]
    
    histograms_defs = [
        { "obs" : "invMass", "units" : "M_{ll}", "minX" : 2.5, "maxX" : 3.5, "bins" : 60 },
    ]
    
    for pti in range(len(pt_ranges)):
        if pti == len(pt_ranges) - 1:
            continue
        pt1 = pt_ranges[pti]
        pt2 = pt_ranges[pti+1]
        for etai in range(len(eta_ranges)):
            if etai == len(eta_ranges) - 1:
                continue
            eta1 = eta_ranges[etai]
            eta2 = eta_ranges[etai+1]
            histograms_defs.append({ "obs" : "invMass_"+str(pt1)+"_"+str(pt2)+"_"+str(eta1)+"_"+str(eta2), "formula" : "invMass", "units" : "M_{ll} Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "leptons[0].Pt() >= " + str(pt1) + " && leptons[0].Pt() <= " + str(pt2) + " && abs(leptons[0].Eta()) >= " + str(eta1) + " && abs(leptons[0].Eta()) <= " + str(eta2) })

class jpsi_muons_fit_invmass_categories_normalised(jpsi_muons_fit_invmass_categories):
    normalise = True
    no_weights = True

class jpsi_muons_fit_invmass_categories_normalised_bg(jpsi_muons_fit_invmass_categories_normalised):
    fit_inv_mass_jpsi_func_bg = True
    
default_params = jpsi_muons_fit_invmass




          #{"name":"MET2", "title": "MET >= 250", "condition" : "Met >= 250 && invMass < 30"},
          #{"name":"dilepBDT", "title": "dilepBDT", "condition" : "Met >= 125 && dilepBDT >= 0 && invMass < 30"},
          #{"name":"trackBDT", "title": "trackBDT", "condition" : "Met >= 125 && invMass < 30 && trackBDT >= 0.2"},
          #{"name":"rectangular_leptons", "title": "rectangular_leptons", "condition" : "Met >= 200 && invMass < 30 && deltaR <= 1.2  && leptons[0].Pt() < 15 && Ht >= 120 && leptons[1].Pt() <= 9 && deltaEta < 1 && mt1 <= 40 && mt2 <= 40 && dilepHt >= 170 && DeltaPhiLeadingJetDilepton >= 1.7"},
          #{"name":"rectangular_track", "title": "rectangular_track", "condition" : "Met >= 200 && invMass < 30 && lepton.Pt() < 15 && Mht >=140 && mtl <= 60 && deltaR <= 1.7 && MinDeltaPhiMhtJets >= 1 && DeltaEtaLeadingJetDilepton <= 2.2 && DeltaPhiLeadingJetDilepton >= 1.8 && deltaPhi <= 1.3 && deltaEta <= 1.2 && LeadingJetPt >= 100 && mtt <= 50 && mt1 <= 60 && mt2 <= 50 && Ht >= 140 &&  MinDeltaPhiMetJets >= 1.3 "},

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

# histograms_defs = [
#     { "obs" : 'int(twoLeptonsJetIso)', "minX" : 1, "maxX" : 2, "bins" : 1},
#     { "obs" : 'int(twoLeptonsJetIsoLowPt)', "minX" : 1, "maxX" : 2, "bins" : 1},
#     { "obs" : 'int(twoLeptonsJetIsoLowPtTight)', "minX" : 1, "maxX" : 2, "bins" : 1},
#     { "obs" : 'int(twoLeptonsCorrJetIso1)', "minX" : 1, "maxX" : 2, "bins" : 1},
#     { "obs" : 'int(twoLeptonsCorrJetIso1LowPt)', "minX" : 1, "maxX" : 2, "bins" : 1},
#     { "obs" : 'int(twoLeptonsCorrJetIso1LowPtTight)', "minX" : 1, "maxX" : 2, "bins" : 1},
#     { "obs" : 'int(twoLeptonsCorrJetIso5)', "minX" : 1, "maxX" : 2, "bins" : 1},
#     { "obs" : 'int(twoLeptonsCorrJetIso5LowPt)', "minX" : 1, "maxX" : 2, "bins" : 1},
#     { "obs" : 'int(twoLeptonsCorrJetIso5LowPtTight)', "minX" : 1, "maxX" : 2, "bins" : 1},
#     { "obs" : 'int(twoLeptonsCorrJetIso10)', "minX" : 1, "maxX" : 2, "bins" : 1},
#     { "obs" : 'int(twoLeptonsCorrJetIso10LowPt)', "minX" : 1, "maxX" : 2, "bins" : 1},
#     { "obs" : 'int(twoLeptonsCorrJetIso10LowPtTight)', "minX" : 1, "maxX" : 2, "bins" : 1},
#     { "obs" : 'int(twoLeptonsCorrJetIso15)', "minX" : 1, "maxX" : 2, "bins" : 1},
#     { "obs" : 'int(twoLeptonsCorrJetIso15LowPt)', "minX" : 1, "maxX" : 2, "bins" : 1},
#     { "obs" : 'int(twoLeptonsCorrJetIso15LowPtTight)', "minX" : 1, "maxX" : 2, "bins" : 1},
# 
# ]

# cuts = [ {"name":"none", "title": "No Cuts", "condition" : "1"},
#          #{"name":"MET", "title": "MET >= 150", "condition" : 'Met >= 150 && invMass < 12 && leptonFlavour == "Muons"'},
#          #{"name":"dileptonPt", "title": "dileptonPt", "condition" : "Met >= 200 && invMass < 30 && dileptonPt < 30"}        
# ]