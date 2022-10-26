

non_iso_2l_factors = {
    '2016' : {
        "Electrons" : [0.214285716414,0.136330502203],
        "Muons" : [0.535714268684,0.0766580571496],
    },
    '2017' : {
        "Electrons" : [0.333333343267,0.2222222222222],
        "Muons" : [0.577319562435,0.0685120763638],
    },
    '2018' : {
        "Electrons" : [0.318181812763,0.138074664848],
        "Muons" : [0.50304877758,0.0480125382518],
    },
    "phase1" : {
        "Electrons" : [0.322580635548,0.117313876994],
        "Muons" : [0.530651330948,0.0394464132051],
    }
}

non_iso_1t_factors = {
    '2016' : {
        "Electrons" : [0.952606618404,0.0938907814687],
        "Muons" : [1.00821352005,0.0644787681262],
    },
    '2017' : {
        "Electrons" : [1.04964542389,0.123523932702],
        "Muons" : [0.953716695309,0.0511205737877],
    },
    '2018' : {
        "Electrons" : [1.04891300201,0.108074340765],
        "Muons" : [1.11734688282,0.0491334201941],
    },
}

sfs = {
    "tracks" : non_iso_1t_factors,
    "leptons" : non_iso_2l_factors
}

tautau_factors = {
    "2016" : {
        "Electrons" : [0.518392205238,0.411471282416],
        "Muons" : [1.19318771362,0.457118010794],
    },
    "2017" : {
        "Electrons" : [1.4467600584,0.838945836228],
        "Muons" : [0.552942574024,0.434856996417],
    },
    "2018" : {
        "Electrons" : [0.710534274578,0.549813163105],
        "Muons" : [0.093785084784,0.316509052096],
    },
}

tautau_windows = {
    "Muons" : [40,130],
    "Electrons" : [0,160]
}

binning = {
    "1t" : {
        "Electrons" : [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,1],
        "Muons" : [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,1]
    },
    "2l" : {
        #"Electrons" : [0,0.1,0.2,0.3,0.35,1],
        #"Muons" : [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,1]
        "Electrons" : [0,0.1,0.2,0.3,1],
        #"Muons" : [0,0.05,0.15,0.25,0.35,0.45,0.6,1]
        #new 
        "Muons" : [0,0.1,0.2,0.3,0.4,0.45,0.5,1]        
    }
}

luminosities = {
    '2016' : 35.7389543,
    '2017' : 41.14712197,
    '2018' : 58.090723828,
    "phase1" : 99.226209715
}

fast_sim_weights = {
    '2016' : "Weight * BranchingRatio * tEffhMetMhtRealXMht2016 * FastSimWeightPR31285To36122",
    '2017' : "Weight * BranchingRatio * tEffhMetMhtRealXMht2017",
    '2018' : "Weight * BranchingRatio * tEffhMetMhtRealXMht2018 * hemFailureVetoElectrons * hemFailureVetoJets * hemFailureVetoMuons",
    "phase1" : "Weight * BranchingRatio * (("+ "{:.2f}".format(luminosities["2017"] * 1000) +" * tEffhMetMhtRealXMht2017 + "+ "{:.2f}".format(luminosities["2018"] * 1000) +" * tEffhMetMhtRealXMht2018)/" + "{:.2f}".format((luminosities["2017"]+luminosities["2018"]) * 1000)  + ") * hemFailureVetoElectrons * hemFailureVetoJets * hemFailureVetoMuons"
}

full_sim_weights  = {
    '2016' : "Weight * BranchingRatio * tEffhMetMhtRealXMht2016",
    '2017' : "Weight * BranchingRatio * tEffhMetMhtRealXMht2017",
    '2018' : "Weight * BranchingRatio * tEffhMetMhtRealXMht2018 * hemFailureVetoElectrons * hemFailureVetoJets * hemFailureVetoMuons",
    "phase1" : "Weight * BranchingRatio * (("+ "{:.2f}".format(luminosities["2017"] * 1000) +" * tEffhMetMhtRealXMht2017 + "+ "{:.2f}".format(luminosities["2018"] * 1000) +" * tEffhMetMhtRealXMht2018)/" + "{:.2f}".format((luminosities["2017"]+luminosities["2018"]) * 1000)  + ") * hemFailureVetoElectrons * hemFailureVetoJets * hemFailureVetoMuons"
}

data_weights = {
    '2016' : "",
    '2017' : "",
    '2018' : "hemFailureVetoElectrons * hemFailureVetoJets * hemFailureVetoMuons * ",
    "phase1" : "hemFailureVetoElectrons * hemFailureVetoJets * hemFailureVetoMuons * "
}

dilepBDTString = {
    '2016' : "dilepBDTphase1",
    '2017' : "dilepBDT",
    '2018' : "dilepBDT",
    "phase1" : "dilepBDT",
}

jetIsos = {
    "Electrons": "CorrJetNoMultIso10Dr0.5",
    "Muons" : "CorrJetNoMultIso10Dr0.6"
}

common_preselection = "passedMhtMet6pack && passesUniversalSelection && MinDeltaPhiMhtJets > 0.4 && MHT >= 220 &&  MET >= 140 && BTagsDeepMedium == 0 && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0"

two_leptons_condition = "twoLeptons%%% == 1 && leptonFlavour%%% == \"$$$\""
two_leptons_condition_zoo_removal  = "invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81)"
two_leptons_iso_condition = "isoCr%%% == 0"
two_leptons_iso_sb_condition = "isoCr%%% > 0"
two_leptons_same_sign = "sameSign%%% == 1"
two_leptons_opposite_sign = "sameSign%%% == 0"

### This should be for example dilepBDTCorrJetNoMultIso10Dr0.6 > 0 
two_leptons_bdt_sr = "***%%% > 0"
two_leptons_bdt_cr = "***%%% < 0"

sos_orth_condition = "(leptons%%%[1].Pt() <= 3.5 || deltaR%%% <= 0.3)"


exclusive_track_category =  "exclusiveTrack%%% == 1 && exTrack_invMass%%% < 12 && exclusiveTrackLeptonFlavour%%% ==\"$$$\" && trackBDT%%% > 0"
exclusive_track_category_sr = "exTrack_dilepBDT%%% > 0"
exclusive_track_category_cr = "exTrack_dilepBDT%%% < 0"

electrons_extra_exclusive_track_category = "exclusive_track_category%%% > 0.05"

sc_exclusive_track_category = "sc_exclusiveTrack%%% == 1 && sc_exTrack_invMass%%% < 12 && sc_exclusiveTrackLeptonFlavour%%% == \"$$$\" && sc_trackBDT%%% > 0 &&"
sc_exclusive_track_category_sr = "sc_exTrack_dilepBDT%%% > 0"
sc_exclusive_track_category_cr = "sc_exTrack_dilepBDT%%% < 0"

sc_electrons_extra_exclusive_track_category = "sc_exTrack_deltaR%%% > 0.05"

mtautau_veto = "(nmtautau%%% < ^^^ || nmtautau%%% > @@@)"
inside_mtautau_window = "nmtautau%%% > ^^^ && nmtautau%%% < @@@"

tautau_mc = "tautau%%%"
not_tautau_mc = "!tautau%%%"

###### PRE MADE LISTS ###### 


two_leptons_sr_conditions = [common_preselection, two_leptons_condition, two_leptons_condition_zoo_removal, two_leptons_iso_condition, two_leptons_opposite_sign, two_leptons_bdt_sr]
two_leptons_cr_conditions = [common_preselection, two_leptons_condition, two_leptons_condition_zoo_removal, two_leptons_iso_condition, two_leptons_opposite_sign, two_leptons_bdt_cr]

two_leptons_bdt_sr_iso_sb = [common_preselection, two_leptons_condition, two_leptons_condition_zoo_removal, two_leptons_iso_sb_condition, two_leptons_opposite_sign, two_leptons_bdt_sr]
two_leptons_bdt_sr_iso_sb_outside_mtautau_window = two_leptons_bdt_sr_iso_sb + [mtautau_veto]


two_leptons_sr_conditions_sos = two_leptons_sr_conditions + [sos_orth_condition]
two_leptons_cr_conditions_sos = two_leptons_cr_conditions + [sos_orth_condition]
two_leptons_cr_conditions_sos_not_tautau = two_leptons_cr_conditions_sos + [not_tautau_mc]

#### OUTSIDE MTAUTAU WINDOW #####

two_leptons_cr_conditions_outside_mtautau_window_basic = [common_preselection, two_leptons_condition, two_leptons_condition_zoo_removal, mtautau_veto, two_leptons_bdt_cr]
two_leptons_cr_conditions_outside_mtautau_window  = [common_preselection, two_leptons_condition, two_leptons_condition_zoo_removal, two_leptons_iso_condition, two_leptons_opposite_sign, two_leptons_bdt_cr, mtautau_veto]
# two_leptons_cr_conditions_outside_mtautau_window_sos = two_leptons_cr_conditions_outside_mtautau_window + [sos_orth_condition]
# two_leptons_cr_conditions_outside_mtautau_window_iso_sb = [common_preselection, two_leptons_condition, two_leptons_condition_zoo_removal, two_leptons_iso_sb_condition, two_leptons_opposite_sign, two_leptons_bdt_cr, mtautau_veto]
# two_leptons_cr_conditions_outside_mtautau_window_iso_sb_sos = two_leptons_cr_conditions_outside_mtautau_window_iso_sb + [sos_orth_condition]
# two_leptons_cr_conditions_outside_mtautau_window_same_sign = [common_preselection, two_leptons_condition, two_leptons_condition_zoo_removal, two_leptons_iso_condition, two_leptons_same_sign, two_leptons_bdt_cr, mtautau_veto]
# two_leptons_cr_conditions_outside_mtautau_window_same_sign_sos = two_leptons_cr_conditions_outside_mtautau_window_same_sign + [sos_orth_condition]
# two_leptons_cr_conditions_outside_mtautau_window_same_sign_iso_sb = [common_preselection, two_leptons_condition, two_leptons_condition_zoo_removal, two_leptons_iso_sb_condition, two_leptons_same_sign, two_leptons_bdt_cr, mtautau_veto]
# two_leptons_cr_conditions_outside_mtautau_window_same_sign_iso_sb_sos = two_leptons_cr_conditions_outside_mtautau_window_same_sign_iso_sb + [sos_orth_condition]

two_leptons_bdt_cr_tautau_inside_mtautau_window = [common_preselection, two_leptons_condition, two_leptons_iso_condition, two_leptons_opposite_sign, two_leptons_bdt_cr, inside_mtautau_window, tautau_mc]
two_leptons_bdt_cr_tautau_inside_mtautau_window_sos = two_leptons_bdt_cr_tautau_inside_mtautau_window + [sos_orth_condition]

###### MC - NOT TAU TAU - INSIDE/OUTSIDE TAU-TAU WINDOW #########

two_leptons_sr_conditions_not_tautau = two_leptons_sr_conditions + [not_tautau_mc]
two_leptons_sr_conditions_sos_not_tautau = two_leptons_sr_conditions_not_tautau + [sos_orth_condition]

###### INSIDE ######
two_leptons_bdt_cr_not_tautau_inside_mtautau_window  = [common_preselection, two_leptons_condition, two_leptons_iso_condition, two_leptons_opposite_sign, two_leptons_bdt_cr, inside_mtautau_window, not_tautau_mc]
two_leptons_bdt_cr_not_tautau_inside_mtautau_window_sos = two_leptons_bdt_cr_not_tautau_inside_mtautau_window + [sos_orth_condition]
two_leptons_bdt_cr_not_tautau_inside_mtautau_window_iso_sb = [common_preselection, two_leptons_condition, two_leptons_iso_sb_condition, two_leptons_opposite_sign, two_leptons_bdt_cr, inside_mtautau_window, not_tautau_mc]
two_leptons_bdt_cr_not_tautau_inside_mtautau_window_iso_sb_sos = two_leptons_bdt_cr_not_tautau_inside_mtautau_window_iso_sb + [sos_orth_condition]
###### INSIDE INCLUSIVE #####
two_leptons_bdt_cr_inside_mtautau_window  = [common_preselection, two_leptons_condition, two_leptons_iso_condition, two_leptons_opposite_sign, two_leptons_bdt_cr, inside_mtautau_window]
two_leptons_bdt_cr_inside_mtautau_window_sos = two_leptons_bdt_cr_inside_mtautau_window + [sos_orth_condition]
two_leptons_bdt_cr_inside_mtautau_window_iso_sb = [common_preselection, two_leptons_condition, two_leptons_iso_sb_condition, two_leptons_opposite_sign, two_leptons_bdt_cr, inside_mtautau_window]
two_leptons_bdt_cr_inside_mtautau_window_iso_sb_sos = two_leptons_bdt_cr_inside_mtautau_window_iso_sb + [sos_orth_condition]

###### OUTSIDE ######
two_leptons_bdt_cr_not_tautau_outside_mtautau_window = two_leptons_cr_conditions_outside_mtautau_window + [not_tautau_mc]
two_leptons_bdt_cr_not_tautau_outside_mtautau_window_sos = two_leptons_bdt_cr_not_tautau_outside_mtautau_window + [sos_orth_condition]
two_leptons_bdt_cr_not_tautau_outside_mtautau_window_iso_sb = [common_preselection, two_leptons_condition, two_leptons_condition_zoo_removal, two_leptons_iso_sb_condition, two_leptons_opposite_sign, two_leptons_bdt_cr, mtautau_veto, not_tautau_mc]
two_leptons_bdt_cr_not_tautau_outside_mtautau_window_iso_sb_sos = two_leptons_bdt_cr_not_tautau_outside_mtautau_window_iso_sb + [sos_orth_condition]

def injectValues(toReplace, year, flavour):    
    return toReplace.replace("%%%", jetIsos[flavour]).replace("^^^", str(tautau_windows[flavour][0])).replace("@@@", str(tautau_windows[flavour][1])).replace("$$$", flavour).replace("***", dilepBDTString[year])

def getFastSimString(year, flavour, selections):
    return injectValues("{:.2f}".format(luminosities[year] * 1000) + " * " + fast_sim_weights[year] + " * (" + " && ".join(selections) + ")", year, flavour)

def getFullSimString(year, flavour, selections):
    return injectValues("{:.2f}".format(luminosities[year] * 1000) + " * " +full_sim_weights[year] + " * (" + " && ".join(selections) + ")", year, flavour)

def getDataString(year, flavour, selections):
    return injectValues(data_weights[year] + "(" + " && ".join(selections) + ")", year, flavour)


