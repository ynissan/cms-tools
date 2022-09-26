import sys
import os
import copy

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))

import utils

from plot_params_base import *
#import plot_params_analysis_categories

common_histograms = [
    
    { "obs" : "MET", "minX" : 0, "maxX" : 800, "bins" : 60, "units" : "E_{T}^{Miss} [GeV]", "linearYspace" : 1.3 },
    #{ "obs" : "MT2", "minX" : 0, "maxX" : 100, "bins" : 30 },
    { "obs" : "MHT", "minX" : 0, "maxX" : 500, "bins" : 60, "units" : "H_{T}^{Miss} [GeV]", "linearYspace" : 1.3 },
    { "obs" : "HT", "minX" : 0, "maxX" : 700, "bins" : 60, "linearYspace" : 1.3 },
    #{ "obs" : "MetDHt", "minX" : 0, "maxX" : 700, "bins" : 30 },
    #{ "obs" : "leptonFlavour%%%", "minX" : 0, "maxX" : 2, "bins" : 2 },
    #{ "obs" : "int(genFlavour == \"Muons\")", "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["genFlavour"] },
    #{ "obs" : "int(genFlavour == \"Electrons\")", "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["genFlavour"] },
    
    { "obs" : "NJets", "minX" : 0, "maxX" : 7, "bins" : 7, "linearYspace" : 1.3 },
    #{ "obs" : "BTagsLoose", "minX" : 0, "maxX" : 7, "bins" : 7 },
    #{ "obs" : "BTagsMedium", "minX" : 0, "maxX" : 7, "bins" : 7 },
    #{ "obs" : "BTagsDeepLoose", "minX" : 0, "maxX" : 7, "bins" : 7 },
    { "obs" : "BTagsDeepMedium", "minX" : 0, "maxX" : 7, "bins" : 7, "linearYspace" : 1.3 },
    
    #{ "obs" : "LeadingJetQgLikelihood", "minX" : 0, "maxX" : 1, "bins" : 30 },
    { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 3.2, "bins" : 60, "units" : "Min\Delta_{}\phi(H_{T}^{Miss}, Jets)" },
    { "obs" : "MinDeltaPhiMetJets", "minX" : 0, "maxX" : 3.2, "bins" : 60, "units" : "Min\Delta_{}\phi(E_{T}^{Miss}, Jets)" },
    
    { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 800, "bins" : 60, "units" : "p_{T}(j_{1})", "linearYspace" : 1.3  },
    { "obs" : "abs(LeadingJet.Eta())", "minX" : 0, "maxX" : 2.5, "bins" : 100, "usedObs" : ["LeadingJet"], "units" : "|\eta_{j_{1}}|" },
    #{ "obs" : "MaxCsv25", "minX" : 0, "maxX" : 1, "bins" : 30 },
    #{ "obs" : "MaxDeepCsv25", "minX" : 0, "maxX" : 1, "bins" : 30 },
    #{ "obs" : "LeadingJetMinDeltaRElectrons", "minX" : 0, "maxX" : 5, "bins" : 30 },
    #{ "obs" : "LeadingJetMinDeltaRMuons", "minX" : 0, "maxX" : 5, "bins" : 30 },
    { "obs" : 'int(vetoElectronsPassIso)', "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["vetoElectronsPassIso"]},
    #{ "obs" : 'int(vetoElectronsCorrJetIso10)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoElectronsMediumID)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoElectronsTightID)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoElectrons)', "minX" : 0, "maxX" : 2, "bins" : 2},
    { "obs" : 'int(vetoMuonsPassIso)', "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["vetoMuonsPassIso"]},
    #{ "obs" : 'int(vetoMuonsCorrJetIso10)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoMuonoMediumID)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoMuonsTightID)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoMuons)', "minX" : 0, "maxX" : 2, "bins" : 2},

]

two_leps_histograms = [
    
    { "obs" : "invMass%%%_coarse", "formula" : "invMass%%%","minX" : 0, "maxX" : 13, "bins" : 6, "blind" : [4,None],"units" : "M_{ll} [GeV]" },
    { "obs" : "invMass%%%", "minX" : 0, "maxX" : 12, "bins" : 20, "blind" : [4,None],"units" : "M_{ll} [GeV]", "linearYspace" : 1.5 },
    { "obs" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "bins" : 60, "blind" : [None,0.1],"units" : "BDT" },
    { "obs" : "custom_dilepBDT%%%", "formula" : "dilepBDT%%%", "minX" : -1, "maxX" : 1, "bins" : 60, "blind" : [None,0.1],"units" : "BDT", "customBins"  : [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,1] },
    { "obs" : "dileptonPt%%%", "minX" : 0, "maxX" : 30, "bins" : 30, "units" : "p_{T}(ll) [GeV]" },
    #{ "obs" : "deltaPhi%%%", "minX" : 0, "maxX" : 3.2, "bins" : 30 },
    { "obs" : "deltaEta%%%", "minX" : 0, "maxX" : 4, "bins" : 30, "units" : "\Delta_{}\eta" },
    { "obs" : "deltaR%%%", "minX" : 0, "maxX" : 4, "bins" : 30, "units" : "\Delta_{}R_{ll}", "linearYspace" : 1.5 },
    { "obs" : "dilepHt%%%", "minX" : 200, "maxX" : 400, "bins" : 30 },
    #{ "obs" : "pt3%%%", "minX" : 0, "maxX" : 1000, "bins" : 30 },
    #{ "obs" : "mtautau%%%", "minX" : 0, "maxX" : 200, "bins" : 30 },
    
    { "obs" : "mt1%%%", "minX" : 0, "maxX" : 100, "bins" : 30, "units" : "m_{T}(l_{1}) [GeV]", "linearYspace" : 1.5 },
    #{ "obs" : "mt2%%%", "minX" : 0, "maxX" : 200, "bins" : 30 },
    
    { "obs" : "leptons%%%[0].Pt()", "minX" : 2, "maxX" : 15, "bins" : 30, "usedObs" : ["leptons%%%"], "units" : "p_{T}(l_{1}) [GeV]", "linearYspace" : 1.5 },
    { "obs" : "leptons%%%[1].Pt()", "minX" : 2, "maxX" : 15, "bins" : 30, "usedObs" : ["leptons%%%"], "units" : "p_{T}(l_{2}) [GeV]" },
    { "obs" : "abs(leptons%%%[0].Eta())", "minX" : 0, "maxX" : 2.4, "bins" : 30, "usedObs" : ["leptons%%%"] },
    { "obs" : "abs(leptons%%%[1].Eta())", "minX" : 0, "maxX" : 2.4, "bins" : 30, "usedObs" : ["leptons%%%"] },
    { "obs" : "deltaPhiMetLepton1%%%", "minX" : 0, "maxX" : 3.5, "bins" : 30, "units" : "\Delta\phi(H_{T}^{Miss},l_{1})" },
    { "obs" : "deltaPhiMetLepton2%%%", "minX" : 0, "maxX" : 3.5, "bins" : 30, "units" : "\Delta\phi(H_{T}^{Miss},l_{1})" },
    #{ "obs" : "leptons_ParentPdgId%%%[0]", "minX" : 0, "maxX" : 40, "bins" : 40, "usedObs" : ["leptons_ParentPdgId%%%"] },
    #{ "obs" : "leptons_ParentPdgId%%%[1]", "minX" : 0, "maxX" : 40, "bins" : 40, "usedObs" : ["leptons_ParentPdgId%%%"] },
    
    #{ "obs" : "deltaEtaLeadingJetDilepton%%%", "minX" : 0, "maxX" : 4, "bins" : 30 },
    #{ "obs" : "deltaPhiLeadingJetDilepton%%%", "minX" : 0, "maxX" : 4, "bins" : 30 },
    
    # { "obs" : "Electrons_minDeltaRJets[leptonsIdx%%%[0]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Electrons_minDeltaRJets"] },
#     { "obs" : "Electrons_minDeltaRJets[leptonsIdx%%%[1]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Electrons_minDeltaRJets"] },
#     
#     { "obs" : "Muons_minDeltaRJets[leptonsIdx%%%[0]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Muons_minDeltaRJets"] },
#     { "obs" : "Muons_minDeltaRJets[leptonsIdx%%%[1]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Muons_minDeltaRJets"] },
#     
#     { "obs" : "Electrons_deltaRLJ[leptonsIdx%%%[0]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Electrons_deltaRLJ"] },
#     { "obs" : "Electrons_deltaRLJ[leptonsIdx%%%[1]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Electrons_deltaRLJ"] },
#     
#     { "obs" : "Muons_deltaRLJ[leptonsIdx%%%[0]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Muons_deltaRLJ"] },
#     { "obs" : "Muons_deltaRLJ[leptonsIdx%%%[1]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Muons_deltaRLJ"] },
#     
#     { "obs" : "Electrons_deltaEtaLJ[leptonsIdx%%%[0]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Electrons_deltaEtaLJ"] },
#     { "obs" : "Electrons_deltaEtaLJ[leptonsIdx%%%[1]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Electrons_deltaEtaLJ"] },
#     
#     { "obs" : "Muons_deltaEtaLJ[leptonsIdx%%%[0]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Muons_deltaEtaLJ"] },
#     { "obs" : "Muons_deltaEtaLJ[leptonsIdx%%%[1]]", "minX" : 0, "maxX" : 1, "bins" : 60, "usedObs" : ["leptonsIdx%%%", "Muons_deltaEtaLJ"] },

]


signals = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm0p86Chi20Chipm*.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm1p13Chi20Chipm*.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm1p92Chi20Chipm*.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm3p28Chi20Chipm*.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm4p30Chi20Chipm*.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm5p63Chi20Chipm*.root"
              
              ]

signalsNlp = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm0p86Chi20Chipm*.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm1p13Chi20Chipm*.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm1p92Chi20Chipm*.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm3p28Chi20Chipm*.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm4p30Chi20Chipm*.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm5p63Chi20Chipm*.root"
              
              ]

signalNames = [
    "\Delta_{}m 0.8 GeV",
    "\Delta_{}m 1.1 GeV",
    "\Delta_{}m 1.9 GeV",
    "\Delta_{}m 3.2 GeV",
    "\Delta_{}m 4.3 GeV",
    "\Delta_{}m 5.6 GeV",
]

class signal_production_comparison_muons(BaseParams):
    
    plot_signal = True
    plot_bg = False
    plot_data = False
    plot_error = True
    
    #sig_line_width = 3
    
    jetIsoStr = "NoIso"
    jetIsoStr = "CorrJetNoMultIso10Dr0.6"
    
    histrograms_file = BaseParams.histograms_root_files_dir + "/signal_production_comparison_muons" + jetIsoStr + ".root"
    
    turnOnOnlyUsedObsInTree = True
    
    save_histrograms_to_file = True
    load_histrograms_from_file = False   
    
    signal_dir = [
        "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/slim_sum/higgsino_mu115_dm4p31Chi20Chipm_1.root",
        "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_sam/sum/mChipm115GeV_dm2p27GeV_1.root",
    ]
    
    signal_names = [
        "\mu 115 \Delta_{}m 4.31 Gev [UV]",
        "\mu 115 \Delta_{}m 4.54 Gev [Sam]",
    ]
    
    weightString = {
        'MET' : "BranchingRatio * Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016",
    }
    
    calculatedLumi = {
        'MET' : 135,
    }
    
    cuts = [
        {"name":"none", "title": "None", "condition" : "(MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && isoCr%%% == 0)", "baseline" : "sameSign%%% == 0", "sc" : "sameSign%%% == 1"},
        {"name":"non-orth", "title": "Non Orth", "condition" : "(MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT%%% > 0.3 && isoCr%%% == 0)", "baseline" : "sameSign%%% == 0", "sc" : "sameSign%%% == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT%%% > 0.1 && (leptons%%%[1].Pt() <= 3.5 || deltaR%%% <= 0.3) && isoCr%%% == 0)", "baseline" : "sameSign%%% == 0", "sc" : "sameSign%%% == 1"},
    ]
    injectJetIsoToCuts(cuts, jetIsoStr)
    histograms_defs = []
    histograms_defs.extend(copy.deepcopy(common_histograms))
    histograms_defs.extend(copy.deepcopy(two_leps_histograms))
    #histograms_defs = copy.deepcopy(dilepton_muons.histograms_defs)
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)
    usedObs = usedObs = ["BranchingRatio","Weight","passedMhtMet6pack","tEffhMetMhtRealXMht2016","puWeight","MinDeltaPhiMhtJets","BTagsDeepMedium","twoLeptons%%%","MHT","MET","leptonFlavour%%%","invMass%%%","vetoElectronsPassIso","vetoMuonsPassIso","isoCr%%%","sameSign%%%", "leptons%%%", "deltaR%%%"]
    injectJetIsoToList(usedObs, jetIsoStr)
    print("usedObs", usedObs)
    #exit(0)

class signal_common_distributions_fixed_mu(BaseParams):
    
    plot_signal = True
    plot_bg = False
    plot_data = False
    plot_error = True
    plot_overflow = True
    
    histrograms_file = BaseParams.histograms_root_files_dir + "/signal_common_distributions_fixed_mu.root"
    
    save_histrograms_to_file = True
    load_histrograms_from_file = True
    
    weightString = {
        'MET' : "BranchingRatio * Weight",
    }
    
    signal_dir = signalsNlp
    signal_names = signalNames
    glob_signal = True
    
    #histograms_defs = []
    #histograms_defs.extend(copy.deepcopy(common_histograms))
    
    histograms_defs = [
    
        { "obs" : "MET", "minX" : 0, "maxX" : 800, "bins" : 60, "units" : "E_{T}^{Miss} [GeV]", "linearYspace" : 1.3 },
        { "obs" : "MHT", "minX" : 0, "maxX" : 500, "bins" : 60, "units" : "H_{T}^{Miss} [GeV]", "linearYspace" : 1.3 },
        { "obs" : "HT", "minX" : 0, "maxX" : 700, "bins" : 60, "linearYspace" : 1.3, "units" : "H_{T} [GeV]" },
        { "obs" : "NJets", "minX" : 0, "maxX" : 7, "bins" : 7, "linearYspace" : 1.3, "units" : "Number of jets" },
        { "obs" : "BTagsDeepMedium", "minX" : 0, "maxX" : 7, "bins" : 7, "linearYspace" : 1.3, "units" : "Number of b-jets" },
        { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 3.2, "bins" : 60, "units" : "Min\Delta_{}\phi(H_{T}^{Miss}, Jets)" },
        { "obs" : "MinDeltaPhiMetJets", "minX" : 0, "maxX" : 3.2, "bins" : 60, "units" : "Min\Delta_{}\phi(E_{T}^{Miss}, Jets)" },
        { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 400, "bins" : 60, "units" : "p_{T}(j_{1}) [GeV]", "linearYspace" : 1.3  },
        #{ "obs" : "abs(LeadingJet.Eta())", "minX" : 0, "maxX" : 2.5, "bins" : 100, "usedObs" : ["LeadingJet"], "units" : "|\eta_{j_{1}}|" },
        #{ "obs" : 'int(vetoElectronsPassIso)', "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["vetoElectronsPassIso"]},
        #{ "obs" : 'int(vetoMuonsPassIso)', "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["vetoMuonsPassIso"]},

    ]
    
    y_title_offset = 1.2
    
    cuts = [
        {"name":"none", "title": "None", "condition" : "1"}
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT%%% > 0.3 && isoCr%%% == 0)", "baseline" : "sameSign%%% == 0", "sc" : "sameSign%%% == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(MinDeltaPhiMhtJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT%%% > 0.1 && (leptons%%%[1].Pt() <= 3.5 || deltaR%%% <= 0.3) && isoCr%%% == 0)", "baseline" : "sameSign%%% == 0", "sc" : "sameSign%%% == 1"},
    ]

class signal_common_distributions_fixed_dm(signal_common_distributions_fixed_mu):
    signal_dir = [
        "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm1p47Chi20Chipm*.root",
          "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu115_dm1p47Chi20Chipm*.root",
          "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu130_dm1p47Chi20Chipm*.root",
    ]
    signal_names = [
    "\Delta_{}m 1.47 GeV, \mu 100 GeV",
    "\Delta_{}m 1.47 GeV, \mu 115 GeV",
    "\Delta_{}m 1.47 GeV, \mu 130 GeV",
    ]
    
    histrograms_file = BaseParams.histograms_root_files_dir + "/signal_common_distributions_fixed_dm.root"
    
    save_histrograms_to_file = True
    load_histrograms_from_file = True