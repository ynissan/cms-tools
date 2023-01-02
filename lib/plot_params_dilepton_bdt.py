import sys
import os

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))

from plot_params_base import *

class dilepton_bdt_inputs_muons(BaseParams):
    
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_bdt_inputs_muons.root"
    
    save_histrograms_to_file = True
    load_histrograms_from_file = True 
    
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
        {"obs" : "abs_deltaPhiLL_", "units" : "|#Delta_{}\phi(t,l)|", "bins" : 50, "minX" : 0, "maxX" : 3.2 },
        {"obs" : "lepton.Pt__", "units" : "p_{T}(l) [GeV]", "bins" : 50, "minX" : 1.9, "maxX" : 10 },
        {"obs" : "deltaEtaLJ", "units" : "|#Delta_{}\eta(t,j_{1})|", "bins" : 50, "minX" : 0, "maxX" : 5 },
        {"obs" : "deltaPhiMht", "units" : "|#Delta_{}\phi(t,H_{T}^{Miss})|", "bins" : 50, "minX" : 0, "maxX" : 3.2, "linearYspace" : 1.6 },
        {"obs" : "abs_lepton.Eta___", "units" : "|\eta(l)|", "bins" : 50, "minX" : 0, "maxX" : 3, "linearYspace" : 1.6 },
        {"obs" : "abs_track.Eta___", "units" : "|\eta(t)|", "bins" : 50, "minX" : 0, "maxX" : 3, "linearYspace" : 1.6 },
        {"obs" : "deltaRLJ", "units" : "#Delta_{}R(l,j_{1})", "bins" : 50, "minX" : 0, "maxX" : 6.3 },
        #{"obs" : "track.Phi__", "units" : "\phi(t)", "bins" : 50, "minX" : -3.2, "maxX" : 3.2, "linearYspace" : 1.6 },
        #{"obs" : "lepton.Phi__", "units" : "\phi(l)", "bins" : 50, "minX" : -3.2, "maxX" : 3.2, "linearYspace" : 1.6 },
        #{"obs" : "mtt", "units" : "m_{T}(t) [GeV]", "bins" : 50, "minX" : 0, "maxX" : 200, "linearYspace" : 1.2 },
        {"obs" : "invMass", "units" : "M_{ll} [GeV]", "bins" : 50, "minX" : 0, "maxX" : 50, "linearYspace" : 1.2 },
        #{"obs" : "track.Pt__", "units" : "p_{T}(t) [GeV]", "bins" : 50, "minX" : 1.9, "maxX" : 10 },
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

