import sys
import os

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))

import utils

from plot_params_base import *

signals = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm0p86Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm1p92Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm3p28Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm9p73Chi20Chipm.root"
              ]

signalNames = [
    "\Delta_{}M 0.8 GeV",
    "\Delta_{}M 1.9 GeV",
    "\Delta_{}M 3.2 GeV",
    "\Delta_{}M 9.7 GeV",
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
        #{"obs" : "Pt tracks_trackJetIso", "formula" : "tracks.Pt()", "bins" : 50, "minX" : 1.9, "maxX" : 10, "object" : "t", "condition" :  "tracks_passCorrJetIso10 == 1" },
        {"obs" : "abs(tracks.Eta())", "bins" : 50, "minX" : 0, "maxX" : 3, "object" : "t" },
        #{"obs" : "Pt tracks_trackJetIso", "formula" : "tracks.Pt()", "bins" : 50, "minX" : 1.9, "maxX" : 20, "object" : "t", "condition" :  "tracks_passCorrJetIso5 == 1" },
        
        # {"obs" : "tracks_matchedCaloEnergy", "bins" : 50, "minX" : 0, "maxX" : 50, "object" : "t" },
#         {"obs" : "tracks_nMissingOuterHits", "bins" : 13, "minX" : 0, "maxX" : 13, "object" : "t" },
#         {"obs" : "tracks_nMissingMiddleHits", "bins" : 3, "minX" : 0, "maxX" : 3, "object" : "t" },
#         {"obs" : "tracks_chi2perNdof", "bins" : 50, "minX" : 0, "maxX" : 20, "object" : "t" },
#         {"obs" : "tracks_trackerLayersWithMeasurement", "bins" : 19, "minX" : 0, "maxX" : 19, "object" : "t" },
#         {"obs" : "tracks_trackQualityGoodIterative", "bins" : 2, "minX" : 0, "maxX" : 2, "object" : "t" },
#         {"obs" : "tracks_trkRelIso", "bins" : 50, "minX" : 0, "maxX" : 0.2, "object" : "t" },
#         {"obs" : "tracks_trkMiniRelIso", "bins" : 50, "minX" : 0, "maxX" : 0.0002, "object" : "t" },
#         {"obs" : "tracks_nValidPixelHits", "bins" : 8, "minX" : 0, "maxX" : 8, "object" : "t" },
#         {"obs" : "tracks_nValidTrackerHits", "bins" : 40, "minX" : 0, "maxX" : 40, "object" : "t" },
#         {"obs" : "tracks_trackJetIso", "bins" : 50, "minX" : 0, "maxX" : 2, "object" : "t" },
#         {"obs" : "tracks_passPFCandVeto", "bins" : 2, "minX" : 0, "maxX" : 2, "object" : "t" },
#         {"obs" : "tracks_dxyVtx", "bins" : 50, "minX" : 0, "maxX" : 0.1, "object" : "t" },
#         {"obs" : "tracks_dzVtx", "bins" : 50, "minX" : 0, "maxX" : 0.1, "object" : "t" },
#         {"obs" : "tracks_pixelLayersWithMeasurement", "bins" : 5, "minX" : 0, "maxX" : 5, "object" : "t" },
#         {"obs" : "tracks_minDrLepton", "bins" : 50, "minX" : 0, "maxX" : 10, "object" : "t" },
#         {"obs" : "tracks_deltaRLJ", "bins" : 50, "minX" : 0, "maxX" : 5, "object" : "t" },
#         {"obs" : "tracks_correctedMinDeltaRJets", "bins" : 50, "minX" : 0, "maxX" : 1, "object" : "t" },
#         {"obs" : "tracks_minDeltaRJets", "bins" : 50, "minX" : 0, "maxX" : 1, "object" : "t" },
#         {"obs" : "tracks_deltaEtaLJ", "bins" : 50, "minX" : 0, "maxX" : 1, "object" : "t" },
#         {"obs" : "tracks_matchedCaloEnergyJets", "bins" : 50, "minX" : 0, "maxX" : 3, "object" : "t" },
#         {"obs" : "tracks_nMissingOuterHits", "bins" : 14, "minX" : 0, "maxX" : 14, "object" : "t" },
#         {"obs" : "tracks_matchedCaloEnergy", "bins" : 50, "minX" : 0, "maxX" : 100, "object" : "t" },
        
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

signalsGen = [
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm0p86Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm1p92Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm3p28Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_nlp/sum/higgsino_mu100_dm9p73Chi20Chipm.root"
              ]

class signal_muons(BaseParams):
    signal_dir = signalsGen
    signal_names = signalNames
    cuts = [
        {"name":"none", "title": "No Cuts", "condition" : "genFlavour == \"Muons\""},
    ]
    histograms_defs = [
        { "obs" : "Muons_pt", "formula" : "Muons.Pt()", "units" : "p_{T} [GeV]", "minX" : 2, "maxX" : 25, "bins" : 60, "condition" :  "Muons_isZ == 1", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        { "obs" : "Muons_Eta", "formula" : "abs(Muons.Eta())", "units" : "|\eta|", "minX" : 0, "maxX" : 2.4, "bins" : 60, "condition" :  "Muons_isZ == 1", "linearYspace" : 1.8, "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        { "obs" : "deltaRNoIso", "units" : "#Delta_{}R", "minX" : 0, "maxX" : 3.5, "bins" : 60, "condition" :  "twoLeptonsNoIso == 1 && leptonFlavour == \"Muons\" && Muons_isZ[leptonsIdxNoIso[0]] == 1 &&  Muons_isZ[leptonsIdxNoIso[1]] == 1 ", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        
        { "obs" : "Muons_pt_barrel", "formula" : "Muons.Pt()", "units" : "Barrel p_{T} [GeV]", "minX" : 2, "maxX" : 10, "bins" : 60, "condition" :  "Muons_isZ == 1 && abs(Muons.Eta()) < 1.2", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1, "linearYspace" : 1.2 },
        { "obs" : "Muons_pt_endcape", "formula" : "Muons.Pt()", "units" : "Endcaps p_{T} [GeV]", "minX" : 2, "maxX" : 10, "bins" : 60, "condition" :  "Muons_isZ == 1 && abs(Muons.Eta()) >= 1.2 && abs(Muons.Eta()) <= 2.4", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1},#, "linearYspace" : 1.2 },
        
    ]
    
    weightString = {
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        'SingleMuon' : "1"
    }
    
    plot_bg = False
    plot_data = False
    plot_overflow = False
    show_lumi = True
    label_text = plotutils.StampStr.SIM

class signal_muons_gen(BaseParams):
    signal_dir = signalsGen
    signal_names = signalNames
    cuts = [
        {"name":"none", "title": "No Cuts", "condition" : "genFlavour == \"Muons\""},
    ]
    histograms_defs = [
        { "obs" : "Muons_pt", "formula" : "GenParticles.Pt()", "units" : "Gen p_{T} [GeV]", "minX" : 2, "maxX" : 25, "bins" : 60, "condition" :  "GenParticles.Pt() < 25 && abs(GenParticles_PdgId) == 13 && GenParticles.Pt() > 2", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        { "obs" : "Muons_Eta", "formula" : "abs(GenParticles.Eta())", "units" : "Gen |\eta|", "minX" : 0, "maxX" : 2.4, "bins" : 60, "condition" :  "GenParticles.Pt() < 25 && abs(GenParticles_PdgId) == 13 && GenParticles.Pt() > 2", "linearYspace" : 1.8, "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        { "obs" : "gen_deltaR", "units" : "Gen #Delta_{}R", "minX" : 0, "maxX" : 3.5, "bins" : 60, "condition" :  "GenParticles[genLeptonsIdx[0]].Pt() < 10 && GenParticles[genLeptonsIdx[1]].Pt() < 10", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        
        { "obs" : "Muons_pt_barrel", "formula" : "GenParticles.Pt()", "units" : "Gen Barrel p_{T} [GeV]", "minX" : 2, "maxX" : 10, "bins" : 60, "condition" :  "GenParticles.Pt() < 25 && abs(GenParticles_PdgId) == 13 && GenParticles.Pt() > 2 && abs(GenParticles.Eta()) < 1.2", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        { "obs" : "Muons_pt_endcape", "formula" : "GenParticles.Pt()", "units" : "Gen Endcaps p_{T} [GeV]", "minX" : 2, "maxX" : 10, "bins" : 60, "condition" :  "GenParticles.Pt() < 25  && abs(GenParticles_PdgId) == 13 && GenParticles.Pt() > 2 && abs(GenParticles.Eta()) >= 1.2 && abs(GenParticles.Eta()) <= 2.4", "legendCoor" : {"x1" : .60, "y1" : .60, "x2" : .89, "y2" : .89}, "legendCol" : 1 },
        
    ]
    
    weightString = {
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        'SingleMuon' : "1"
    }
    
    plot_bg = False
    plot_data = False
    plot_overflow = False
    show_lumi = True
    label_text = plotutils.StampStr.SIM