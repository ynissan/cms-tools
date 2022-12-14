import sys
import os

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))

from plot_params_base import *

signals = [
              #"/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm0p86Chi20Chipm.root",
              "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm1p92Chi20Chipm.root",
              #"/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm3p28Chi20Chipm.root",
              #"/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum/higgsino_mu100_dm9p73Chi20Chipm.root"
              ]

signalNames = [
    #"\Delta_{}M 0.8Gev",
    #"\Delta_{}M 1.9Gev",
    #"\Delta_{}M 3.2Gev",
    "\Delta_{}M 9.7Gev",
]

class track_bdt_electron(BaseParams):
    
    signal_dir = signals
    signal_names = signalNames
    #bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/type_sum"
    plot_bg = False
    plot_data = False
    plot_overflow = True
    object_retag = True
    
    sig_line_width = 1
    
    histograms_defs = [
        {"obs" : "tracks.Pt()", "units" : "p_{T} [GeV]", "bins" : 50, "minX" : 1.9, "maxX" : 10, "object" : "t" },
        #{"obs" : "Pt tracks_trackJetIso", "formula" : "tracks.Pt()", "bins" : 50, "minX" : 1.9, "maxX" : 10, "object" : "t", "condition" :  "tracks_passCorrJetIso10 == 1" },
        {"obs" : "abs(tracks.Eta())", "units" : "#eta", "bins" : 50, "minX" : 0, "maxX" : 3, "object" : "t" },
        
        {"obs" : "exTrack_invMass", "units" : "M_{ll} [GeV]", "bins" : 50, "minX" : 0, "maxX" : 30 },
        {"obs" : "exTrack_invMass", "units" : "M_{ll} [GeV]", "bins" : 50, "minX" : 0, "maxX" : 30, "object" : "o" },
        
        
        {"obs" : "trackBDT", "units" : "BDT Score", "bins" : 50, "minX" : -1, "maxX" : 1, "object" : "o" },
        #{"obs" : "trackBDT", "units" : "BDT Score", "bins" : 50, "minX" : -1, "maxX" : 1, "object" : "o" },
        
        { "obs" : "int(genFlavour == \"Muons\")", "units" : "Gen Muon", "minX" : 0, "maxX" : 2, "bins" : 2 },
        { "obs" : "int(genFlavour == \"Electrons\")", "units" : "Gen Electrons", "minX" : 0, "maxX" : 2, "bins" : 2 },
        #{"obs" : "secondTrackBDT", "units" : "Second BDT Score", "bins" : 50, "minX" : -1, "maxX" : 1, "object" : "o" },
        
        
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
                {"Fake" : "tracks_isZ == 0"},
                {"Exclusive" : "tracks_isZ == 1 && tracks_mi == -1 && tracks_ei == -1"},
                {"Reconstructed" : "tracks_isZ == 1 && (tracks_mi != -1 || tracks_ei != -1)"},
                ],

                
        "o" : [ {"Fake" : "tracks_isZ[ti] == 0"},
                {"Exclusive" : "tracks_isZ[ti] == 1 && tracks_mi[ti] == -1 && tracks_ei[ti] == -1"},
                {"Reconstructed" : "tracks_isZ[ti] == 1 && (tracks_mi[ti] != -1 || tracks_ei[ti] != -1)"},
                #{"Muon Reconstructed" : "tracks_isZ[ti] == 1 && tracks_mi[ti] != -1"},
                #{"Same" : "tracks_isZ[ti] == 1 && tracks_mi[ti] == leptonIdx"},
                ],
    }
    
    legend_coordinates = {"x1" : .20, "y1" : .60, "x2" : .89, "y2" : .89}
    legend_columns = 2
    legend_border = 0
    
    weightString = {
        'MET' : "Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016",
    }
    
    calculatedLumi = {
        'MET' : utils.LUMINOSITY/1000.0,
    }
    

    save_histrograms_to_file = True
    load_histrograms_from_file = False    
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/track_bdt_electron.root"

    
    cuts = [
        {"name":"none", "title": "None", "condition" : "(exclusiveTrack == 1 && MHT >= 220 &&  MET >= 200 && exTrack_invMass < 10 && BTagsDeepMedium == 0 && exclusiveTrackLeptonFlavour == \"Electrons\" )"},
        {"name":"bdt", "title": "BDT > 0", "condition" : "(exclusiveTrack == 1 && MHT >= 220 &&  MET >= 200 && exTrack_invMass < 10 && BTagsDeepMedium == 0 && exclusiveTrackLeptonFlavour == \"Electrons\" &&  trackBDT > 0)"}
    ]
    #histograms_defs = []
    #histograms_defs.extend(common_histograms)
    #histograms_defs.extend(ex_track_histograms)
    #histograms_defs.extend(extra_study_obs)
    

class track_bdt_muon(track_bdt_electron):
    #
    cuts = [
        {"name":"none", "title": "None", "condition" : "(exclusiveTrack == 1 && MHT >= 220 &&  MET >= 200 && exTrack_invMass < 10 && BTagsDeepMedium == 0 && exclusiveTrackLeptonFlavour == \"Muons\" )"},
        {"name":"BDT", "title": "BDT > 0", "condition" : "(exclusiveTrack == 1 && MHT >= 220 &&  MET >= 200 && exTrack_invMass < 10 && BTagsDeepMedium == 0 && exclusiveTrackLeptonFlavour == \"Muons\"  &&  trackBDT > 0)"}
    ]
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/track_bdt_muon.root"


class track_bdt_inputs_muons(BaseParams):
    
    histrograms_file = BaseParams.histograms_root_files_dir + "/track_bdt_inputs_muons.root"
    
    save_histrograms_to_file = True
    load_histrograms_from_file = False 
    
    show_lumi = False
    use_calculated_lumi_weight = False
    use_bdt_file_as_input = True
    
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/lepton_track/cut_optimisation/tmva/Muons/Muons.root"
    
    plot_signal = False
    no_weights = True
    nostack = True
    y_title = "Tracks"
    y_title_offset = 1.2
    legend_columns = 1
    legend_coordinates = {"x1" : .6, "y1" : .60, "x2" : .95, "y2" : .89}
    
    plot_overflow = True
    
    colorPalette = plotutils.bdtColors
    
    label_text = plotutils.StampStr.SIM
    
    cuts = [
        {"name":"none", "title": "None", "condition" : "1" },
    ]
    
    histograms_defs = [
        {"obs" : "deltaRLL", "units" : "#Delta_{}R(t,l)", "bins" : 50, "minX" : 0, "maxX" : 6.3 },
        {"obs" : "deltaEtaLL", "units" : "|#Delta_{}\eta(t,l)|", "bins" : 50, "minX" : 0, "maxX" : 5 },
        {"obs" : "deltaEtaLJ", "units" : "|#Delta_{}\eta(t,j_{1})|", "bins" : 50, "minX" : 0, "maxX" : 5 },
        {"obs" : "deltaPhiMht", "units" : "|#Delta_{}\phi(t,H_{T}^{Miss})|", "bins" : 50, "minX" : 0, "maxX" : 3.2, "linearYspace" : 1.6 },
        {"obs" : "lepton.Eta__", "units" : "\eta(l)", "bins" : 50, "minX" : -3, "maxX" : 3, "linearYspace" : 1.6 },
        {"obs" : "track.Eta__", "units" : "\eta(t)", "bins" : 50, "minX" : -3, "maxX" : 3, "linearYspace" : 1.6 },
        {"obs" : "deltaRLJ", "units" : "#Delta_{}R(l,j_{1})", "bins" : 50, "minX" : 0, "maxX" : 6.3 },
        {"obs" : "track.Phi__", "units" : "\phi(t)", "bins" : 50, "minX" : -3.2, "maxX" : 3.2, "linearYspace" : 1.6 },
        {"obs" : "lepton.Phi__", "units" : "\phi(l)", "bins" : 50, "minX" : -3.2, "maxX" : 3.2, "linearYspace" : 1.6 },
        {"obs" : "mtt", "units" : "m_{T}(t) [GeV]", "bins" : 50, "minX" : 0, "maxX" : 200, "linearYspace" : 1.2 },
        {"obs" : "invMass", "units" : "M_{ll} [GeV]", "bins" : 50, "minX" : 0, "maxX" : 50, "linearYspace" : 1.2 },
        {"obs" : "track.Pt__", "units" : "p_{T} [GeV]", "bins" : 50, "minX" : 1.9, "maxX" : 10 },
    ]
    
    bg_retag = True
    
    bgReTagging = {
        "fake" : "classID == 1",
        "gen-matched" : "classID == 0",
    }
    
    bgReTaggingOrder = {
        "fake"  : 1,
        "gen-matched" : 2
    }
    bgReTaggingNames = {
        "fake" : "Fake",
        "gen-matched" : "Gen Matched"
    }