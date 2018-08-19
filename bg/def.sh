declare -A SIMS
SIMS=( ["dm13"]="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/pMSSM/pMSSM_MCMC1_38_870285_dm13_chi1pmchi20.root"\
       ["dm7"]="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/pMSSM/pMSSM_MCMC1_38_870285_dm7_m160.root",
       ["dm20"]="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/TChiZW/OfficialScan/TChiWZ_mNlsp150mLsp130.root")

SIM_DIR="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_SM"
NEW_SIM_DIR="/pnfs/desy.de/cms/tier2/store/user/sbein/CommonNtuples"
NEWEST_SIM_DIR="/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/Production2016v1"
BG_TYPES=(QCD DYJetsToLL WJetsToLNu ZJetsToNuNu WZZ WWZ WW WZ ZZZ ZZ TTWJetsToLNu)
#BG_TYPES=(WJetsToLNu)
RARE=(WZZ WWZ ZZZ)
DiBoson=(WZ WW ZZ)
MAD_HT_SPLIT_TYPES=(TTJets)
#MAD_HT_SPLIT_TYPES=()
WORK_DIR="/tmp"
CMS_WD="/afs/desy.de/user/n/nissanuv/CMSSW_9_2_7_patch1/src"
CMS_TOOLS="/afs/desy.de/user/n/nissanuv/cms-tools"
SIM_DIR="$CMS_TOOLS/sim_x10x20x10"
SCRIPTS_WD="$CMS_TOOLS/analysis/scripts"
ANALYZER_PATH="$SCRIPTS_WD/analyzer_x1x2x1.py"
SKIMMER_PATH="$SCRIPTS_WD/skimmer_x1x2x1.py"
CLONE_SCRIPT="$SCRIPTS_WD/clone_tree_split.py"
CLONE_SINGLE="$SIM_DIR/clone_sim_file_single.sh"
OUTPUT_WD="/afs/desy.de/user/n/nissanuv/xxl/af-cms/x1x2x1"
OUTPUT_DIR="$OUTPUT_WD/bg/hist"
SKIM_OUTPUT_DIR="$OUTPUT_WD/bg/skim"
SKIM_SIG_OUTPUT_DIR="$OUTPUT_WD/signal/skim"
SIG_DUP_OUTPUT_DIR="$OUTPUT_WD/signal/dup"