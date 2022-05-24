import sys
import os
import copy
import ROOT

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib"))

from plot_params_base import *
import plot_params_analysis_categories


class dilepton_muons_data_control_region(BaseParams):
    signal_dir = signals
    signal_names = signalNames
    bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim/sum/slim_sum/type_sum"
    data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim/slim_sum/"
    cuts = [
        {"name":"none", "title": "None", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && isoCr%%% == 0 && sameSign%%% == 0 && dilepBDT%%% < 0)", "baseline" : "", "sc" : ""},
        {"name":"njets", "title": "NJets > 1", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && isoCr%%% == 0 && sameSign%%% == 0 && dilepBDT%%% < 0 && NJets > 1)", "baseline" : "", "sc" : ""},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 200 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT%%% > 0.3 && isoCr%%% == 0)", "baseline" : "sameSign%%% == 0", "sc" : "sameSign%%% == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 200 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT%%% > 0.1 && (leptons%%%[1].Pt() <= 3.5 || deltaR%%% <= 0.3) && isoCr%%% == 0)", "baseline" : "sameSign%%% == 0", "sc" : "sameSign%%% == 1"},
    ]
    
    #(twoLeptons == 1 && (leptons[1].Pt() <= 3.5 || deltaR <= 0.3) && MHT >= 220 &&  MET >= 200 && invMass < 12  && invMass > 0.4 && !(invMass > 3 && invMass < 3.2) && !(invMass > 0.75 && invMass < 0.81) && dilepBDT > 0.1 && BTagsDeepMedium == 0 && vetoElectronsPassIsoTightID == 0 && vetoMuonsPassIsoPassIso == 0 && @leptons.size() == 2 && leptonFlavour == \"" + lep + "\" && sameSign == 0)", True)
    histograms_defs = []
    histograms_defs.extend(plot_params_analysis_categories.common_histograms)
    histograms_defs.extend(plot_params_analysis_categories.two_leps_histograms)
    #histograms_defs.extend(extra_study_obs)
    
    weightString = {
        #'MET' : "BranchingRatio * Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016 * puWeight",
        'MET' : "BranchingRatio * Weight * passedMhtMet6pack * tEffhMetMhtRealXMht2016",
        #'MET' : "BranchingRatio * Weight",
    }
    
    calculatedLumi = {
        #'MET' : 35.778598358,
        #'MET' : 135,

        'MET' : 35.712736198,

    }
    
    turnOnOnlyUsedObsInTree = False
    usedObs = ["BranchingRatio","Weight","passedMhtMet6pack","tEffhMetMhtRealXMht2016","puWeight","MinDeltaPhiMetJets","BTagsDeepMedium","twoLeptons%%%","MHT","MET","leptonFlavour%%%","invMass%%%","vetoElectronsPassIso","vetoMuonsPassIso","isoCr%%%","sameSign%%%", "leptons%%%", "deltaR%%%"]
    
    plot_sc = False
    plot_data = True
    plot_signal = False
    plot_overflow = True
    plot_ratio = True
    
    blind_data = False

    save_histrograms_to_file = True
    load_histrograms_from_file = True
    
    histrograms_file = "/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons_data_control_region.root" 
    #jetIsoStr = "CorrJetIso10.5Dr0.55"
    jetIsoStr = "NoIso"
    histrograms_file = BaseParams.histograms_root_files_dir + "/dilepton_muons_data_control_region.root"
    #"/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src/cms-tools/analysis/scripts/dilepton_muons" + jetIsoStr + ".root"
    #cuts = copy.deepcopy(dilepton_muons.cuts)
    injectJetIsoToCuts(cuts, jetIsoStr)
    #histograms_defs = copy.deepcopy(dilepton_muons.histograms_defs)
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)
    #usedObs = copy.deepcopy(dilepton_muons.usedObs)
    #print("before", usedObs)
    #injectJetIsoToList(usedObs, jetIsoStr)
    #print("after", usedObs)
    #exit(0)
    sig_line_width = 3
    plot_error = True

class dilepton_muons_data_control_region_iso_cr(dilepton_muons_data_control_region):
    cuts = [
        {"name":"none", "title": "Low BDT", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && isoCr%%% > 0 && sameSign%%% == 0 && dilepBDT%%% < 0)", "baseline" : "", "sc" : ""},
        {"name":"all", "title": "all", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && isoCr%%% > 0 && sameSign%%% == 0)", "baseline" : "", "sc" : ""},
        {"name":"njets", "title": "njets > 1", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 140 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && isoCr%%% > 0 && sameSign%%% == 0 && NJets > 1)", "baseline" : "", "sc" : ""},
        #{"name":"non-orth", "title": "Non Orth", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 200 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT%%% > 0.3 && isoCr%%% == 0)", "baseline" : "sameSign%%% == 0", "sc" : "sameSign%%% == 1"},
        #{"name":"orth", "title": "Orth", "condition" : "(MinDeltaPhiMetJets > 0.4 && BTagsDeepMedium == 0 && twoLeptons%%% == 1 && MHT >= 220 &&  MET >= 200 && leptonFlavour%%% == \"Muons\" && invMass%%% < 12  && invMass%%% > 0.4 && !(invMass%%% > 3 && invMass%%% < 3.2) && !(invMass%%% > 0.75 && invMass%%% < 0.81) && vetoElectronsPassIso == 0 && vetoMuonsPassIso == 0 && dilepBDT%%% > 0.1 && (leptons%%%[1].Pt() <= 3.5 || deltaR%%% <= 0.3) && isoCr%%% == 0)", "baseline" : "sameSign%%% == 0", "sc" : "sameSign%%% == 1"},
    ]
    jetIsoStr = "CorrJetIso10.5Dr0.55"
    #jetIsoStr = "NoIso"
    injectJetIsoToCuts(cuts, jetIsoStr)
    histograms_defs = []
    histograms_defs.extend(plot_params_analysis_categories.common_histograms)
    histograms_defs.extend(plot_params_analysis_categories.two_leps_histograms)
    injectJetIsoToHistograms(histograms_defs, jetIsoStr)
    normalise = True
    