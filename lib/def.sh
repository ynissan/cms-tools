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
BG_NTUPLES="/pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/ProductionRun2v[34]"
NEWESTEST_SIM_DIR="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/M1M2Scan/ntuple_sidecar/"
SIM_NTUPLES_DIR="/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/ntuples_sum"
DATA_NTUPLES_DIR="/pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/ProductionRun2v[34]"
BG_TYPES=(QCD TTJets_DiLept TTJets_SingleLeptFromTbar TTJets_SingleLeptFromT ST_t-channel_antitop_4f_inclusiveDecays ST_t-channel_top_4f_inclusiveDecays DYJetsToLL WJetsToLNu ZJetsToNuNu WZZ WWZ WW WZ ZZZ ZZ TTWJetsToLNu)
RARE=(WZZ WWZ ZZZ)
DiBoson=(WZ WW ZZ)
#MAD_HT_SPLIT_TYPES=(TTJets)
MAD_HT_SPLIT_TYPES=()
FILE_EXCLUDE_LIST=(-100to20_ -10to200_ -200to40_ -20to400_ -40to600_ -600to80_ -20To400_ -400To60_ -40To600_ HT100to1500_ HT1500to200_ HT200toInf_ -200toInf_ -80to1200_ -200To40_ -250toInf_ -1200to250_ -800to120_ -120to2500_ 1000to150_ -60ToInf_ 400to60_ 100To20_ HT150to2000_ HT200to30_ HT1000to150_ Run218 Run217 Run216)
WORK_DIR="/tmp"
CMS_WD="$CMSSW_BASE/src"
CMS_TOOLS="$CMS_WD/cms-tools"
SIM_DIR="$CMS_TOOLS/sim_x10x20x10"
SCRIPTS_WD="$CMS_TOOLS/analysis/scripts"
LEPTON_TRACK_DIR="$CMS_TOOLS/analysis/lepton_track"
BG_SCRIPTS="$CMS_TOOLS/bg/scripts"
ANALYZER_PATH="$SCRIPTS_WD/analyzer_x1x2x1.py"
SKIMMER_PATH="$SCRIPTS_WD/skimmer_x1x2x1.py"
CLONE_SCRIPT="$SCRIPTS_WD/clone_tree_split.py"
CLONE_SINGLE="$SIM_DIR/clone_sim_file_single.sh"
CS_SINGLE="$SIM_DIR/calculate_cross_section_single.sh"

#OUTPUT_WD="/afs/desy.de/user/n/nissanuv/work/x1x2x1"

DATA_DIR="$CMS_TOOLS/data"
BG_DIR="$CMS_TOOLS/bg"
BG_HIST_DIR="$OUTPUT_WD/bg/hist"
SKIM_OUTPUT_DIR="$OUTPUT_WD/bg/skim"
SKIM_SIG_OUTPUT_DIR="$OUTPUT_WD/signal/skim"
SKIM_DATA_OUTPUT_DIR="$OUTPUT_WD/data/skim"
CS_SIG_OUTPUT_DIR="$OUTPUT_WD/signal/cs"
SKIM_SIG_BDT_OUTPUT_DIR="$OUTPUT_WD/signal/skim_signal_bdt"
SKIM_DATA_BDT_OUTPUT_DIR="$OUTPUT_WD/data/skim_signal_bdt"
SKIM_BG_SIG_BDT_OUTPUT_DIR="$OUTPUT_WD/bg/skim_signal_bdt"
SKIM_SIG_DILEPTON_BDT_OUTPUT_DIR="$OUTPUT_WD/signal/skim_dilepton_signal_bdt"
SKIM_BG_SIG_DILEPTON_BDT_OUTPUT_DIR="$OUTPUT_WD/bg/skim_dilepton_signal_bdt"
SKIM_DATA_SIG_DILEPTON_BDT_OUTPUT_DIR="$OUTPUT_WD/data/skim_dilepton_signal_bdt"

SKIM_SIG_BDT_SC_OUTPUT_DIR="$OUTPUT_WD/signal/skim_signal_bdt_sc"
SKIM_DATA_BDT_SC_OUTPUT_DIR="$OUTPUT_WD/data/skim_signal_bdt_sc"
SKIM_BG_SIG_BDT_SC_OUTPUT_DIR="$OUTPUT_WD/bg/skim_signal_bdt_sc"
SKIM_SIG_DILEPTON_BDT_SC_OUTPUT_DIR="$OUTPUT_WD/signal/skim_dilepton_signal_bdt_sc"
SKIM_BG_SIG_DILEPTON_BDT_SC_OUTPUT_DIR="$OUTPUT_WD/bg/skim_dilepton_signal_bdt_sc"
SKIM_DATA_SIG_DILEPTON_BDT_SC_OUTPUT_DIR="$OUTPUT_WD/data/skim_dilepton_signal_bdt_sc"

SIG_DUP_OUTPUT_DIR="$OUTPUT_WD/signal/dup"
LEPTON_TRACK_SPLIT_DIR="$OUTPUT_WD/signal/lepton_track"
RGS_DIR="/afs/desy.de/user/n/nissanuv/cms-tools/analysis/cut_optimisation/rgs"
RESUMMINO_BIN="/afs/desy.de/user/n/nissanuv/local/bin/resummino"
DILEPTON_BDT_DIR="$OUTPUT_WD/cut_optimisation/tmva/dilepton_bdt"

if [[ `hostname` == *".desy.de"* ]]; then
    MKDIR_CMD=mkdir
    COPY_CMD=cp
    echo "COPY_CMD=$COPY_CMD"
    COPY_DEST_PREFIX=""
    OUTPUT_WD="/afs/desy.de/user/n/nissanuv/nfs/x1x2x1"
    SIG_CONFIG_OUTPUT_DIR="$OUTPUT_WD/signal/config"
    SIG_AOD_OUTPUT_DIR="$OUTPUT_WD/signal/aod"
    SIG_MINIAOD_OUTPUT_DIR="$OUTPUT_WD/signal/miniaod"
    SIG_NTUPLES_OUTPUT_DIR="$OUTPUT_WD/signal/ntuples"
else
    MKDIR_CMD=gfal-mkdir
    COPY_CMD=gfal-copy
    COPY_DEST_PREFIX="file://"
    OUTPUT_WD="srm://dcache-se-cms.desy.de/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub"
    SIG_CONFIG_OUTPUT_DIR="$OUTPUT_WD/signal/config"
    SIG_AOD_OUTPUT_DIR="$OUTPUT_WD/signal/aod"
    SIG_MINIAOD_OUTPUT_DIR="$OUTPUT_WD/signal/miniaod"
    SIG_NTUPLES_OUTPUT_DIR="$OUTPUT_WD/signal/ntuples"
fi