import sys
import os

from ROOT import *

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))

import crystal_ball_params
import utils

from plot_params_base import *

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
        { "obs" : "tracks[probeTrack].Pt()", "units" : "Probe Muon P_{t}", "minX" : 2, "maxX" : 24, "bins" : 60 },
        { "obs" : "high_tracks[probeTrack].Pt()", "formula" : "tracks[probeTrack].Pt()", "units" : "Probe Muon P_{t} high delta R", "minX" : 2, "maxX" : 24, "bins" : 60,  "condition" :  "deltaR > 0.5"},
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
        {"name":"none", "title": "None", "condition" : "Muons[tagMuon].Pt() < 20 && tracks[probeTrack].Pt() >= 2 && tracks[probeTrack].Pt() <= 20"},
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
    
    bgReTaggingNames = {
        "jpsi" : "J/#psi",
        "other" : "Continuum"
    }
    
    
    plot_data = False
    plot_ratio = False
    normalise = False
    no_weights = False
    plot_overflow = False
    bg_retag = True

class jpsi_muons_fit_bg(jpsi_muons_ex_track_new):
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
       

class jpsi_muons_fit_bg_tag_pt(jpsi_muons_fit_bg):

    crystalBallInitialConditions = crystal_ball_params.crystalBallInitialConditionsTagPtBg
    
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
            
            histograms_defs.append({ "obs" : "id_" + obsBaseName, "formula" : "invMass", "units" : "M_{ll} Id Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks_mi[probeTrack] > -1 && Muons_mediumID[tracks_mi[probeTrack]] == 1 && tracks[probeTrack].Pt() >= " + str(pt1) + " && tracks[probeTrack].Pt() <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2) })#&& tracks_trkRelIso[ti] < 0.1 #track.Pt() <= 10 && 
            #histograms_defs.append({ "obs" : "reco_" + obsBaseName, "formula" : "invMass", "units" : "M_{ll} Reco Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks_mi[probeTrack] > -1 && tracks[probeTrack].Pt() >= " + str(pt1) + " && tracks[probeTrack].Pt() <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2) })#&& tracks_trkRelIso[ti] < 0.1 #track.Pt() <= 10 && 
            histograms_defs.append({ "obs" : "iso_" + obsBaseName, "formula" : "invMass", "units" : "M_{ll} Iso Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks_mi[probeTrack] > -1 && Muons_mediumID[tracks_mi[probeTrack]] == 1 && tracks[probeTrack].Pt() >= " + str(pt1) + " && tracks[probeTrack].Pt() <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2)  + " && Muons_passCorrJetIso10[tracks_mi[probeTrack]] == 1" })
            histograms_defs.append({ "obs" : obsBaseName, "formula" : "invMass", "units" : "M_{ll} Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks[probeTrack].Pt() >= " + str(pt1) + " && tracks[probeTrack].Pt() <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2) })
            


class jpsi_muons_fit_data_tag_pt(jpsi_muons_fit_bg_tag_pt):
    plot_bg = False
    plot_data = True
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/invMassDataGranularHists.root"
    fit_inv_mass_jpsi_func_bg = False
    weightString = {
        'MET' : "passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        'SingleMuon' : "passedSingleMuPack"
    }
    
    crystalBallInitialConditions = crystal_ball_params.crystalBallInitialConditionsTagPtData
    
    fit_inv_mass_jpsi_func = "crystalBall"
    #fit_inv_mass_jpsi_func = "crystalBall"
    #fit_inv_mass_jpsi_func = "lorentzian"
    #fit_inv_mass_jpsi_func = "doubleGaussian"
    #fit_inv_mass_jpsi_func = "gauss"
    
    #fit_inv_mass_jpsi_func = "doubleGaussian"

class jpsi_muons_fit_data_delta_r(jpsi_muons_fit_data_tag_pt):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/invMassDataDeltaRHistsNoTagCut.root"
    
    histograms_defs = []
    
    eta_ranges = [0,1.2,2.4]
    delta_r_ranges = [0,0.3,0.5,1.5]
    
    crystalBallInitialConditions = crystal_ball_params.crystalBallInitialConditionsDeltaR
    
    cuts = [
        {"name":"none", "title": "No Cuts", "condition" : "1"},
    ]
    
    fit_inv_mass_cut_jpsi = "none"
    
    for pti in range(len(delta_r_ranges)):
        if pti == len(delta_r_ranges) - 1:
            continue
        pt1 = delta_r_ranges[pti]
        pt2 = delta_r_ranges[pti+1]
       
        for etai in range(len(eta_ranges)):
            if etai == len(eta_ranges) - 1:
                continue
            eta1 = eta_ranges[etai]
            eta2 = eta_ranges[etai+1]
            
            obsBaseName = "invMass_"+str(pt1)+"_"+str(pt2)+"_"+str(eta1)+"_"+str(eta2)
            
            #if "invMass_2_3_0_1.2" in obsBaseName:
            #    continue
                
            
            #if "invMass_2_3_1.2_2.4" != obsBaseName:
            #    continue
            
            #if "invMass_3_4_0_1.2" != obsBaseName:
            #    continue
            
            #if "invMass_10_20_1.2_2.4" != obsBaseName:
            #    continue
            
            # didn't have base condition before
            baseCondition = "tracks[probeTrack].Pt() < 20 && "
            if eta1 == 0:
                baseCondition += "tracks[probeTrack].Pt() > 3 && "
            histograms_defs.append({ "obs" : "id_" + obsBaseName, "formula" : "invMass", "units" : "m_{\mu^{+}\mu^{-}} [GeV] Id \Delta_{}R \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "linearYspace" : 1.8, "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": baseCondition + "tracks_mi[probeTrack] > -1 && Muons_mediumID[tracks_mi[probeTrack]] == 1 && deltaR >= " + str(pt1) + " && deltaR <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2) })#&& tracks_trkRelIso[ti] < 0.1 #track.Pt() <= 10 && 
            #histograms_defs.append({ "obs" : "reco_" + obsBaseName, "formula" : "invMass", "units" : "M_{ll} Reco Pt \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": "tracks_mi[probeTrack] > -1 && tracks[probeTrack].Pt() >= " + str(pt1) + " && tracks[probeTrack].Pt() <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2) })#&& tracks_trkRelIso[ti] < 0.1 #track.Pt() <= 10 && 
            #histograms_defs.append({ "obs" : "iso_" + obsBaseName, "formula" : "invMass", "units" : "M_{ll} Iso \Delta_{}R \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": baseCondition + "tracks_mi[probeTrack] > -1 && Muons_mediumID[tracks_mi[probeTrack]] == 1 && deltaR >= " + str(pt1) + " && deltaR <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2)  + " && Muons_passCorrJetIso10[tracks_mi[probeTrack]] == 1" })
            histograms_defs.append({ "obs" : obsBaseName, "formula" : "invMass", "units" : "m_{\mu^{+}\mu^{-}} [GeV] \Delta_{}R \in [" + str(pt1) + ", " + str(pt2) + "], \eta \in [" + str(eta1) + ", " + str(eta2) + "]", "linearYspace" : 1.8, "minX" : 2.5, "maxX" : 3.5, "bins" : 60, "condition": baseCondition + "deltaR >= " + str(pt1) + " && deltaR <= " + str(pt2) + " && abs(tracks[probeTrack].Eta()) >= " + str(eta1) + " && abs(tracks[probeTrack].Eta()) <= " + str(eta2) })
   
    
class jpsi_muons_fit_bg_delta_r(jpsi_muons_fit_data_delta_r):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/invMassBgDeltaRHistsNoTagCut.root"
    fit_inv_mass_jpsi_func_bg = True
    plot_bg = True
    plot_data = False
    
    weightString = {
        'SingleMuon' : "puWeight"
    }
    
    calculatedLumi = {
        'SingleMuonReco' : 0.001,
        'SingleMuon' : 0.001,
    }
    crystalBallInitialConditions = crystal_ball_params.crystalBallInitialConditionsBgDeltaR

class jpsi_muons_fit_data_delta_r_high_tag_pt(jpsi_muons_fit_data_delta_r):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/invMassDataDeltaRHistsHighTagPt.root"
    crystalBallInitialConditions = crystal_ball_params.crystalBallInitialConditionsDeltaRHighTagPt
    
    cuts = [
        {"name":"tag_muon", "title": "Tag Muon > 25 GeV", "condition" : "Muons[tagMuon].Pt() > 25"},
    ]
    
    fit_inv_mass_cut_jpsi = "tag_muon"
    
class jpsi_muons_fit_bg_delta_r_high_tag_pt(jpsi_muons_fit_data_delta_r_high_tag_pt):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/invMassBgDeltaRHistsHighTagPt.root"
    fit_inv_mass_jpsi_func_bg = True
    plot_bg = True
    plot_data = False
    
    weightString = {
        'SingleMuon' : "puWeight"
    }
    
    calculatedLumi = {
        'SingleMuonReco' : 0.001,
        'SingleMuon' : 0.001,
    }
    crystalBallInitialConditions = crystal_ball_params.crystalBallInitialConditionsBgDeltaRHighTagPt

class jpsi_muons_fit_bg_delta_r_single_electron(jpsi_muons_fit_bg_delta_r_high_tag_pt):
    histrograms_file = BaseParams.histograms_root_files_dir + "/invMassBgDeltaRHistsSingleElectron.root"
    crystalBallInitialConditions = crystal_ball_params.crystalBallInitialConditionsBgDeltaRSingleElectron
    cuts = [
        {"name":"none", "title": "None", "condition" : "1"},
    ]
    
    weightString = {
        'SingleElectron' : "puWeight"
    }
    
    fit_inv_mass_cut_jpsi = "none"
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_jpsi_single_electron/sum/type_sum"
    calculatedLumi = {
        'SingleElectron' : 36.0,
    }
    plot_kind = "SingleElectron"
    use_calculated_lumi_weight = False
    
    save_histrograms_to_file = True
    load_histrograms_from_file = True
    
    colorPalette = [
        { "name" : "yellow", "fillColor" : kYellow-4, "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 5,  "markerStyle" : kOpenCircle},
        { "name" : "lightgreen", "fillColor" : kGreen-6, "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    ]
    
    legend_coordinates = {"x1" : .4, "y1" : .65, "x2" : .89, "y2" : .89}
    show_lumi = False
    y_title = "Tracks"
    

class jpsi_muons_fit_data_delta_r_single_electron(jpsi_muons_fit_data_delta_r_high_tag_pt):
    histrograms_file = BaseParams.histograms_root_files_dir + "/invMassDataDeltaRHistsSingleElectron.root"
    crystalBallInitialConditions = crystal_ball_params.crystalBallInitialConditionsDataDeltaRSingleElectron
    
    cuts = [
        {"name":"none", "title": "None", "condition" : "passedSingleElectronPack == 1"},
    ]
    
    fit_inv_mass_cut_jpsi = "none"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_jpsi_single_electron/sum"
    
    weightString = {
        'SingleElectron' : "passedSingleElectronPack"
    }
    
    calculatedLumi = {
        #This was actually calculated!!!
        'SingleElectron' : 36.0,
    }
    plot_kind = "SingleElectron"
    use_calculated_lumi_weight = False
    
    save_histrograms_to_file = True
    load_histrograms_from_file = True
    
    show_lumi = True
    
    y_title = "Tracks"
    
    legend_coordinates = {"x1" : .4, "y1" : .65, "x2" : .89, "y2" : .89}
    label_text = plotutils.StampStr.PRE
    

class jpsi_muons_fit_data_delta_r_single_electron_no_trigger(jpsi_muons_fit_data_delta_r_single_electron):
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/invMassDataDeltaRHistsSingleElectronNoTrigger.root"
    weightString = {
        'SingleElectron' : "1"
    }
    cuts = [
        {"name":"none", "title": "None", "condition" : "1"},
    ]