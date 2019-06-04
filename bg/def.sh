declare -A SIMS
SIMS=( ["dm13"]="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/pMSSM/pMSSM_MCMC1_38_870285_dm13_chi1pmchi20.root"\
       ["dm7"]="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/pMSSM/pMSSM_MCMC1_38_870285_dm7_m160.root",
       ["dm20"]="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/TChiZW/OfficialScan/TChiWZ_mNlsp150mLsp130.root")

#SIMS=(["dm7"]="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/pMSSM/pMSSM_MCMC1_38_870285_dm7_m160.root")
SIMS=(["dm051"]="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/M1M2Scan/ntuple_sidecar/higgsino_mu100_dm0.51Chi20Chipm.root")

declare -A SIM_GROUP=(["low"]="dm2p dm3p dm4p"\
           ["dm5"]="dm5p" \
           ["dm7"]="dm7p" \
           ["dm9"]="dm9p" \
           ["high"]="dm12p dm13p")

NEW_SIM_DIR="/pnfs/desy.de/cms/tier2/store/user/sbein/CommonNtuples"
NEWEST_SIM_DIR="/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/Production2016v2"
BG_NTUPLES="/pnfs/desy.de/cms/tier2/store/user/vormwald/NtupleHub/ProductionRun2v3"
NEWESTEST_SIM_DIR="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/M1M2Scan/ntuple_sidecar/"
SIM_NTUPLES_DIR="/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/ntuples_sum"
DATA_NTUPLES_DIR="/pnfs/desy.de/cms/tier2/store/user/jarieger/NtupleHub/ProductionRun2v3"
BG_TYPES=(TTJets_DiLept TTJets_SingleLeptFromTbar TTJets_SingleLeptFromT ST_t-channel_antitop_4f_inclusiveDecays ST_t-channel_top_4f_inclusiveDecays DYJetsToLL WJetsToLNu ZJetsToNuNu WZZ WWZ WW WZ ZZZ ZZ TTWJetsToLNu)
#BG_TYPES=(QCD)
RARE=(WZZ WWZ ZZZ)
DiBoson=(WZ WW ZZ)
#MAD_HT_SPLIT_TYPES=(TTJets)
MAD_HT_SPLIT_TYPES=()
WORK_DIR="/tmp"
CMS_WD="/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src"
CMS_TOOLS="/afs/desy.de/user/n/nissanuv/cms-tools"
SIM_DIR="$CMS_TOOLS/sim_x10x20x10"
SCRIPTS_WD="$CMS_TOOLS/analysis/scripts"
LEPTON_TRACK_DIR="$CMS_TOOLS/analysis/lepton_track"
BG_SCRIPTS="$CMS_TOOLS/bg/scripts"
ANALYZER_PATH="$SCRIPTS_WD/analyzer_x1x2x1.py"
SKIMMER_PATH="$SCRIPTS_WD/skimmer_x1x2x1.py"
CLONE_SCRIPT="$SCRIPTS_WD/clone_tree_split.py"
CLONE_SINGLE="$SIM_DIR/clone_sim_file_single.sh"
CS_SINGLE="$SIM_DIR/calculate_cross_section_single.sh"
OUTPUT_WD="/afs/desy.de/user/n/nissanuv/nfs/x1x2x1"
DATA_DIR="$CMS_TOOLS/data"
BG_HIST_DIR="$OUTPUT_WD/bg/hist"
SKIM_OUTPUT_DIR="$OUTPUT_WD/bg/skim"
SKIM_SIG_OUTPUT_DIR="$OUTPUT_WD/signal/skim"
SKIM_DATA_OUTPUT_DIR="$OUTPUT_WD/data/skim"
CS_SIG_OUTPUT_DIR="$OUTPUT_WD/signal/cs"
SIG_CONFIG_OUTPUT_DIR="$OUTPUT_WD/signal/config"
SIG_AOD_OUTPUT_DIR="$OUTPUT_WD/signal/aod"
SIG_MINIAOD_OUTPUT_DIR="$OUTPUT_WD/signal/miniaod"
SIG_NTUPLES_OUTPUT_DIR="$OUTPUT_WD/signal/ntuples"
SKIM_SIG_BDT_OUTPUT_DIR="$OUTPUT_WD/signal/skim_signal_bdt"
SKIM_DATA_BDT_OUTPUT_DIR="$OUTPUT_WD/data/skim_signal_bdt"
SKIM_SIG_DILEPTON_BDT_OUTPUT_DIR="$OUTPUT_WD/signal/skim_dilepton_signal_bdt"
SKIM_BG_SIG_BDT_OUTPUT_DIR="$OUTPUT_WD/bg/skim_signal_bdt"
SKIM_BG_SIG_DILEPTON_BDT_OUTPUT_DIR="$OUTPUT_WD/bg/skim_dilepton_signal_bdt"
SKIM_DATA_SIG_DILEPTON_BDT_OUTPUT_DIR="$OUTPUT_WD/data/skim_dilepton_signal_bdt"
SIG_DUP_OUTPUT_DIR="$OUTPUT_WD/signal/dup"
LEPTON_TRACK_SPLIT_DIR="$OUTPUT_WD/signal/lepton_track"
RGS_DIR="/afs/desy.de/user/n/nissanuv/cms-tools/analysis/cut_optimisation/rgs"
RESUMMINO_BIN="/afs/desy.de/user/n/nissanuv/local/bin/resummino"
DILEPTON_BDT_DIR="$OUTPUT_WD/cut_optimisation/tmva/dilepton_bdt"