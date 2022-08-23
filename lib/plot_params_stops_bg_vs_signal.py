import sys
import os
from ROOT import *
import copy 

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib"))

from plot_params_base import *
import plotutils

skim_dir = "/afs/desy.de/user/n/nissanuv/q_nfs/x1x2x1/signal/skim/sum/"

signals = [
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm0p6GeV_1.root",
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p0GeV_1.root",
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm200GeV_dm1p4GeV_1.root",
    skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm400GeV_dm1p4GeV_1.root",
]

signalNames = [
    "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 0.6 Gev",
    "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.0 Gev",
    "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.4 Gev",
    "m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 1.4 Gev",
]


common_histograms = [
    
    { "obs" : "MET", "minX" : 0, "maxX" : 800, "bins" : 30, "legendCoor" : {"x1" : .35, "y1" : .7, "x2" : .98, "y2" : .95}, "legendCol" : 3 },
    #{ "obs" : "MT2", "minX" : 0, "maxX" : 100, "bins" : 30 },
    { "obs" : "MHT", "minX" : 200, "maxX" : 500, "bins" : 30, "units" : "H_{T}^{Miss} [GeV]" , "legendCoor" : {"x1" : .35, "y1" : .65, "x2" : .98, "y2" : .95}, "legendCol" : 3  },
    { "obs" : "HT", "minX" : 0, "maxX" : 700, "bins" : 30 },
    #{ "obs" : "MetDHt", "minX" : 0, "maxX" : 700, "bins" : 30 },
    { "obs" : "leptonFlavour%%%", "minX" : 0, "maxX" : 2, "bins" : 2 },
    #{ "obs" : "int(genFlavour == \"Muons\")", "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["genFlavour"] },
    #{ "obs" : "int(genFlavour == \"Electrons\")", "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["genFlavour"] },
    
    { "obs" : "NJets", "minX" : 0, "maxX" : 7, "bins" : 7 , "legendCoor" : {"x1" : .35, "y1" : .75, "x2" : .98, "y2" : .95}},
    #{ "obs" : "BTagsLoose", "minX" : 0, "maxX" : 7, "bins" : 7 },
    #{ "obs" : "BTagsMedium", "minX" : 0, "maxX" : 7, "bins" : 7 },
    #{ "obs" : "BTagsDeepLoose", "minX" : 0, "maxX" : 7, "bins" : 7 },
    { "obs" : "BTagsDeepMedium", "minX" : 0, "maxX" : 7, "bins" : 7, "legendCoor" : {"x1" : 0.65, "y1" : .2, "x2" : .95, "y2" : .89}, "legendCol" : 1 },
    
    #{ "obs" : "LeadingJetQgLikelihood", "minX" : 0, "maxX" : 1, "bins" : 30 },
    { "obs" : "MinDeltaPhiMhtJets", "minX" : 0, "maxX" : 1.5, "bins" : 20, "units" : "Min\Delta_{}\phi(H_{T}^{Miss}, Jets)" },
    { "obs" : "MinDeltaPhiMetJets", "minX" : 0, "maxX" : 1.5, "bins" : 20, "units" : "Min\Delta_{}\phi(E_{T}^{Miss}, Jets)" },
    
    { "obs" : "LeadingJetPt", "minX" : 0, "maxX" : 800, "bins" : 30, "units" : "p_{T}(j_{1})" },
    { "obs" : "abs(LeadingJet.Eta())", "minX" : 0, "maxX" : 2.5, "bins" : 30, "usedObs" : ["LeadingJet"], "units" : "|\eta_{j_{1}}|" },
    #{ "obs" : "abs(LeadingJet.Eta())_2","formula" : "abs(LeadingJet.Eta())", "minX" : 0, "maxX" : 0.5, "bins" : 60, "usedObs" : ["LeadingJet"], "units" : "|\eta_{j_{1}}|" },
    #{ "obs" : "MaxCsv25", "minX" : 0, "maxX" : 1, "bins" : 30 },
    #{ "obs" : "MaxDeepCsv25", "minX" : 0, "maxX" : 1, "bins" : 30 },
    #{ "obs" : "LeadingJetMinDeltaRElectrons", "minX" : 0, "maxX" : 5, "bins" : 30 },
    { "obs" : "LeadingJetMinDeltaRMuons", "minX" : 0, "maxX" : 5, "bins" : 30 },
    { "obs" : 'int(vetoElectronsPassIso)', "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["vetoElectronsPassIso"]},
    #{ "obs" : 'int(vetoElectronsCorrJetIso10)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoElectronsMediumID)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoElectronsTightID)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoElectrons)', "minX" : 0, "maxX" : 2, "bins" : 2},
    { "obs" : 'int(vetoMuonsPassIso)', "minX" : 0, "maxX" : 2, "bins" : 2, "usedObs" : ["vetoMuonsPassIso"]},
    { "obs" : "event_num", "formula" : "1", "units" : "Number of Events", "minX" : 0, "maxX" : 1, "bins" : 1},
    #{ "obs" : 'int(vetoMuonsCorrJetIso10)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoMuonoMediumID)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoMuonsTightID)', "minX" : 0, "maxX" : 2, "bins" : 2},
    #{ "obs" : 'int(vetoMuons)', "minX" : 0, "maxX" : 2, "bins" : 2},

]

two_leps_histograms = [
    
    #HIST E
    { "obs" : "invMass%%%", "minX" : 0, "maxX" : 12, "bins" : 20, "blind" : [4,None],"units" : "M_{ll} [GeV]", "linearYspace" : 1.5, "legendCoor" : {"x1" : .35, "y1" : .65, "x2" : .98, "y2" : .95}, "legendCol" : 3  },
#     { "obs" : "invMass%%%", "minX" : 0, "maxX" : 12, "bins" : 20, "units" : "M_{ll} [GeV]", "linearYspace" : 1.5, "legendCoor" : {"x1" : .35, "y1" : .65, "x2" : .98, "y2" : .95}, "legendCol" : 3  },
    
    
    
    { "obs" : "deltaPhi%%%", "minX" : 0, "maxX" : 3.2, "bins" : 30 },
    { "obs" : "deltaEta%%%", "minX" : 0, "maxX" : 4, "bins" : 30, "units" : "\Delta_{}\eta" },
    { "obs" : "deltaR%%%", "minX" : 0, "maxX" : 4, "bins" : 30, "units" : "\Delta_{}R_{ll}", "linearYspace" : 1.5 },
    { "obs" : "dilepHt%%%", "minX" : 200, "maxX" : 400, "bins" : 30 },
   
    { "obs" : "nmtautau%%%", "minX" : 0, "maxX" : 200, "bins" : 30 },
    
    { "obs" : "mth1%%%", "minX" : 0, "maxX" : 100, "bins" : 30, "units" : "m_{T}(l_{1}) [GeV]", "linearYspace" : 1.5 },
    { "obs" : "mth2%%%", "minX" : 0, "maxX" : 200, "bins" : 30, "units" : "m_{T}(l_{2}) [GeV]", "linearYspace" : 1.5},
    
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


class stops_bg_vs_signal(BaseParams):
    signal_dir = signals
    signal_names = signalNames
    bg_dir = "/nfs/dust/cms/user/diepholq/x1x2x1/bg/skim/sum/type_sum"

    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio",
    }
    
    calculatedLumi = {
        'MET' : utils.LUMINOSITY/1000.0,
    }
    
    plot_bg = True
    plot_data = False
    plot_signal = True
    
    
    
    plot_overflow = True
    plot_error = True
    plot_significance = True
    
    histograms_defs = []
    cuts = []
    
    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_bg_vs_signal.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    
   #  histograms_defs = [
#         { "obs" : "MET", "minX" : 0, "maxX" : 800, "bins" : 30 },
#         #{ "obs" : "MET2", "formula" : "MET", "minX" : 0, "maxX" : 600, "bins" : 80, "condition" : "HT < 600" },
#         { "obs" : "MHT", "minX" : 200, "maxX" : 500, "bins" : 30, "units" : "H_{T}^{Miss} [GeV]" },
#         { "obs" : "HT", "minX" : 0, "maxX" : 700, "bins" : 30 },
#         { "obs" : "invMass%%%", "minX" : 0, "maxX" : 12, "bins" : 20 ,"units" : "M_{ll} [GeV]", "linearYspace" : 1.5 },
#     ]
    
    histograms_defs = copy.deepcopy(common_histograms + two_leps_histograms)
    
    cuts = [
    {"name":"none", "title": "MET > 140 && MinDeltaPhiMhtJets > 0.4", "condition" : "MET > 140 && MinDeltaPhiMhtJets > 0.4", "baseline" : " leptonFlavour%%% == \"Muons\" && sameSign%%% == 0", "sc" : "1"}, 

	{"name":"step1", "title": "MET > 140 && MinDeltaPhiMhtJets > 0.4 && leptons%%%[0].Pt() < 7 && leptons%%%[1].Pt() < 7", "condition" : "MET > 140 && BTagsDeepMedium > 0 && MinDeltaPhiMhtJets > 0.4", "baseline" : "twoLeptons%%% == 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0", "sc" : "1"},
        
	{"name":"step3", "title": "MET > 140 && BTagsDeepMedium > 1 && MinDeltaPhiMhtJets > 0.4", "condition" : "MET > 140 && BTagsDeepMedium > 1 && MinDeltaPhiMhtJets > 0.4", "baseline" : "twoLeptons%%% == 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0", "sc" : "1"},

    ]
    
    legend_coordinates = {"x1" : .35, "y1" : .40, "x2" : .95, "y2" : .89}
    #legend_coordinates = {"x1" : 0.65, "y1" : .2, "x2" : .95, "y2" : .89}
    legend_columns = 2
    legend_border = 0
    
    y_title_offset = 1.3
    y_title = "Events"
    
    jetIsoStr = "NoIso"
    injectJetIsoToCuts(cuts, jetIsoStr)
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)
    





class stops_bg_vs_signal_Iso(BaseParams):
    signal_dir = signals
    signal_names = signalNames
    bg_dir = "/nfs/dust/cms/user/diepholq/x1x2x1/bg/skim/sum/type_sum"

    weightString = {
    'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016 * Weight * BranchingRatio",
    }

    calculatedLumi = {
    'MET' : utils.LUMINOSITY/1000.0,
    }

    plot_bg = True
    plot_data = False
    plot_signal = True

    no_weights = True

    plot_overflow = True
    plot_error = True
    plot_significance = True

    histograms_defs = []
    cuts = []

    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_bg_vs_signal_Iso.root"
    save_histrograms_to_file = True
    load_histrograms_from_file = False

    #  histograms_defs = [
    #         { "obs" : "MET", "minX" : 0, "maxX" : 800, "bins" : 30 },
    #         #{ "obs" : "MET2", "formula" : "MET", "minX" : 0, "maxX" : 600, "bins" : 80, "condition" : "HT < 600" },
    #         { "obs" : "MHT", "minX" : 200, "maxX" : 500, "bins" : 30, "units" : "H_{T}^{Miss} [GeV]" },
    #         { "obs" : "HT", "minX" : 0, "maxX" : 700, "bins" : 30 },
    #         { "obs" : "invMass%%%", "minX" : 0, "maxX" : 12, "bins" : 20 ,"units" : "M_{ll} [GeV]", "linearYspace" : 1.5 },
    #     ]

    histograms_defs = copy.deepcopy(common_histograms + two_leps_histograms)

    cuts = [
    {"name":"none", "title": "MET > 140 && MinDeltaPhiMhtJets > 0.4", "condition" : "MET > 140 && MinDeltaPhiMhtJets > 0.4", "baseline" : "twoLeptons%%% == 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0", "sc" : "1"}, #sc?

    #{"name":"step1", "title": "MET > 140 && MinDeltaPhiMhtJets > 0.4 && leptons%%%[0].Pt() < 7 && leptons%%%[1].Pt() < 7", "condition" : "MET > 140 && BTagsDeepMedium > 0 && MinDeltaPhiMhtJets > 0.4", "baseline" : "twoLeptons%%% == 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0", "sc" : "1"},

    #{"name":"step3", "title": "MET > 140 && BTagsDeepMedium > 1 && MinDeltaPhiMhtJets > 0.4", "condition" : "MET > 140 && BTagsDeepMedium > 1 && MinDeltaPhiMhtJets > 0.4", "baseline" : "twoLeptons%%% == 1 && leptonFlavour%%% == \"Muons\" && sameSign%%% == 0", "sc" : "1"},

    ]

    legend_coordinates = {"x1" : .35, "y1" : .40, "x2" : .95, "y2" : .89}
    #legend_coordinates = {"x1" : 0.65, "y1" : .2, "x2" : .95, "y2" : .89}
    legend_columns = 2
    legend_border = 0

    y_title_offset = 1.3
    y_title = "Events"


    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
    injectJetIsoToCuts(cuts, jetIsoStr)
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)



class stops_bg_two_vs_three_muons_bg(stops_bg_vs_signal_Iso):
    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_bg_two_vs_three_muons_bg.root"
    plot_signal = False
    no_weights = True
    bg_retag = True
    
    save_histrograms_to_file = True
    load_histrograms_from_file = False 
    
    bgReTagging = {
        "2-muons" : "(leptonsIdx%%%[2] == -1)",
        "3-muons" : "(leptonsIdx%%%[2] >= 0)",
    }
    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
    injectJetIsoToMapValues(bgReTagging, jetIsoStr)
    
    bgReTaggingOrder = {
        "2-muons" : 0,
        "3-muons" : 1
    }
    bgReTaggingNames = {
        "2-muons" : "2 Muons",
        "3-muons" : "3 Muons"
    }
    
class stops_bg_two_vs_three_muons_signal(stops_bg_two_vs_three_muons_bg):
    histrograms_file = BaseParams.histograms_root_files_dir + "/stops_bg_two_vs_three_muons_signal.root"
    plot_signal = True
    plot_bg = False
    
    save_histrograms_to_file = True
    load_histrograms_from_file = False
    
    
    signal_dir = [
        #skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm0p6GeV_1.root",
        #skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p0GeV_1.root",
        skim_dir + "higgsino_Summer16_stopstop_700GeV_mChipm200GeV_dm1p4GeV_1.root",
        #skim_dir + "higgsino_Summer16_stopstop_500GeV_mChipm400GeV_dm1p4GeV_1.root",
    ]
    signal_names = [
    #"m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 0.6 Gev",
    #"m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 115GeV \Delta_{}m 1.0 Gev",
    "m_{#tilde{t}} 700 GeV m_{#tilde{#chi}^{#pm}_{1}} 200GeV \Delta_{}m 1.4 Gev",
    #"m_{#tilde{t}} 500 GeV m_{#tilde{#chi}^{#pm}_{1}} 400GeV \Delta_{}m 1.4 Gev",
]
    

    
    object_retag = True
    jetIsoStr = "CorrJetNoMultIso15Dr0.4"
    object_retag_map = {
        "l" : [ 
                { "2 Muons" : "(leptonsIdx%%%[2] == -1)".replace("%%%", jetIsoStr)},
                { "3 Muons" : "(leptonsIdx%%%[2] >= 0)".replace("%%%", jetIsoStr)}
                ],
    }
    
    no_weights = True
    
    #injectJetIsoToMapValues(object_retag_map["l"], jetIsoStr)
    
    
    for histDef in stops_bg_two_vs_three_muons_bg.histograms_defs:
        histDef["object"] = "l"
    



