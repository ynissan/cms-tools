declare -A SIMS
SIMS=( ["dm13"]="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/pMSSM/pMSSM_MCMC1_38_870285_dm13_chi1pmchi20.root"\
       ["dm7"]="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/pMSSM/pMSSM_MCMC1_38_870285_dm7_m160.root",
       ["dm20"]="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/TChiZW/OfficialScan/TChiWZ_mNlsp150mLsp130.root")

#SIMS=(["dm7"]="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/pMSSM/pMSSM_MCMC1_38_870285_dm7_m160.root")
SIMS=(["dm051"]="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/M1M2Scan/ntuple_sidecar/higgsino_mu100_dm0.51Chi20Chipm.root")

# declare -A SIM_GROUP=(["low"]="dm2p dm3p dm4p"\
#            ["dm1"]="dm1p dm0p" \
#            ["dm5"]="dm5p" \
#            ["dm7"]="dm7p" \
#            ["dm9"]="dm9p" \
#            ["high"]="dm12p dm13p" \
#            ["all"]="dm1p dm0p dm2p dm3p dm4p" \
#            )

#declare -A SIM_GROUP=(["all"]="dm")

declare -A SIM_GROUP=(
           ["all"]="dm1p dm2p dm3p dm4p" \
           )

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$CMSSW_BASE/src/stops/lib/classes"

NEW_SIM_DIR="/pnfs/desy.de/cms/tier2/store/user/sbein/CommonNtuples"
NEWEST_SIM_DIR="/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/Production2016v2"
BG_NTUPLES="/pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/ProductionRun2v3*"
NEWESTEST_SIM_DIR="/nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/M1M2Scan/ntuple_sidecar/"
SIM_NTUPLES_DIR="/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu_2016Fast/ntuple_sidecarv3"
#SAM_SIM_NTUPLES_DIR="/pnfs/desy.de/cms/tier2/store/user/sbein/CommonSamples/RadiativeMu_2016Fast/ntuple_sidecar"
SAM_SIM_NTUPLES_DIR="/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu_2016Fast/ntuple_sidecar/"
SAM_NEW_SIM_NTUPLES_DIR="/pnfs/desy.de/cms/tier2/store/user/sbein/CommonSamples/RadiativeMu_2016Fast/ntuple_sidecar/"
DATA_NTUPLES_DIR="/pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/ProductionRun2v3*"
#2 jobs for this list (the full list)
BG_TYPES=(QCD TTJets_DiLept TTJets_SingleLeptFromTbar TTJets_SingleLeptFromT ST_t-channel_antitop_4f_inclusiveDecays ST_t-channel_top_4f_inclusiveDecays DYJetsToLL WJetsToLNu ZJetsToNuNu WZZ WWZ WW WZ ZZZ ZZ)

#BG_TYPES=(QCD)

# 10 jobs per file for this list
BG_TYPES=(QCD TTJets_SingleLeptFromTbar TTJets_SingleLeptFromT ST_t-channel_antitop_4f_inclusiveDecays ST_t-channel_top_4f_inclusiveDecays)
#continue with 8 of these
BG_TYPES=(DYJetsToLL WJetsToLNu ZJetsToNuNu WZZ WWZ WW WZ ZZZ ZZ)

#BG_TYPES=(ST_s-channel_4f_leptonDecays ST_tW_antitop_5f_inclusiveDecays ST_tW_top_5f_inclusiveDecays WGToLNuG ZGTo2LG)
#BG_TYPES=(ST_t-channel_antitop_4f_inclusiveDecays ST_t-channel_top_4f_inclusiveDecays DYJetsToLL  WZZ WWZ WW WZ ZZZ ZZ)

#BG_TYPES=(DYJetsToLL)
#BG_TYPES=(QCD TTJets_DiLept TTJets_SingleLeptFromTbar TTJets_SingleLeptFromT ST_t-channel_antitop_4f_inclusiveDecays ST_t-channel_top_4f_inclusiveDecays WJetsToLNu ZJetsToNuNu WZZ WWZ WW WZ ZZZ ZZ)

#BG_TYPES=(QCD)
#BG_TYPES=(TTJets_DiLept)

RARE=(WZZ WWZ ZZZ)
DiBoson=(WZ WW ZZ)

#BG_TYPES=(QCD)

#MAD_HT_SPLIT_TYPES=(TTJets)
MAD_HT_SPLIT_TYPES=()

# LEPTON_ISOLATION_LIST=(JetIso CorrJetIso NonJetIso)
# LEPTON_ISOLATION_CATEGORIES=("" LowPt LowPtTight)
# LEPTON_CORR_JET_ISO_RANGE=(0 1 5 10 15)

LEPTON_ISOLATION_LIST=(NoIso CorrJetIso CorrJetNoMultIso JetIso)
LEPTON_ISOLATION_CATEGORIES=("")
LEPTON_CORR_JET_ISO_RANGE=(0 1 5 6 7 8 9 10 10.5 11 11.5 12 12.5 13 15 20)
LEPTON_CORR_JET_ISO_DR_CUTS=(0.4 0.45 0.5 0.55 0.6)

FILE_EXCLUDE_LIST=(-100to20_ -10to200_ -200to40_ -20to400_ -40to600_ -600to80_ -20To400_ -400To60_ -40To600_ HT100to1500_ HT1500to200_ HT200toInf_ -200toInf_ -80to1200_ -200To40_ -250toInf_ -1200to250_ -800to120_ -120to2500_ 1000to150_ -60ToInf_ 400to60_ 100To20_ HT150to2000_ HT200to30_ HT1000to150_ Run218 Run217 Run216 genMET)
WORK_DIR="/tmp"
CMS_WD="$CMSSW_BASE/src"
stops="$CMS_WD/stops"
SIM_DIR="$stops/sim_x10x20x10"
SCRIPTS_WD="$stops/analysis/scripts"
CUT_OPTIMISATION_SCRIPTS="$stops/analysis/cut_optimisation/tmva"
CONDOR_WRAPPER="$SCRIPTS_WD/condor_wrapper.sh"
LEPTON_TRACK_DIR="$stops/analysis/lepton_track"
BG_SCRIPTS="$stops/bg/scripts"
ANALYZER_PATH="$SCRIPTS_WD/analyzer_x1x2x1.py"
#SKIMMER_PATH="$SCRIPTS_WD/skimmer_x1x2x1.py"
SKIMMER_PATH="$SCRIPTS_WD/skimmer_x1x2x1.py"
JPSI_SKIMMER_PATH="$SCRIPTS_WD/skimmer_x1x2x1_jpsi.py"
MINI_SKIMMER_PATH="$SCRIPTS_WD/mini_skimmer_x1x2x1.py"
SELECTION_SKIMMER_PATH="$SCRIPTS_WD/skimmer_selection.py"
LC_SCRIPT_PATH="$SCRIPTS_WD/merge_lepton_collection.py"
CLONE_SCRIPT="$SCRIPTS_WD/clone_tree_split.py"
CLONE_SINGLE="$SIM_DIR/clone_sim_file_single.sh"
CS_SINGLE="$SIM_DIR/calculate_cross_section_single.sh"

OUTPUT_WD="/nfs/dust/cms/user/diepholq/x1x2x1"
TWO_LEPTONS_OUTPUT_WD="/nfs/dust/cms/user/nissanuv/2lx1x2x1"
DY_OUTPUT_WD="/nfs/dust/cms/user/nissanuv/dy_x1x2x1"

DATA_DIR="$stops/data"
BG_DIR="$stops/bg"
BG_HIST_DIR="$OUTPUT_WD/bg/hist"
SKIM_OUTPUT_DIR="$OUTPUT_WD/bg/skim"
SKIM_MASTER_OUTPUT_DIR="$OUTPUT_WD/bg/skim_master"
SKIM_JPSI_SINGLE_ELECTRON_OUTPUT_DIR="$OUTPUT_WD/bg/skim_jpsi_single_electron"
SKIM_Z_PEAK_OUTPUT_DIR="$OUTPUT_WD/bg/skim_z"
TWO_LEPTONS_SKIM_OUTPUT_DIR="$TWO_LEPTONS_OUTPUT_WD/bg/skim"
NLP_SKIM_OUTPUT_DIR="$OUTPUT_WD/bg/skim_nlp"
JPSI_MUONS_SKIM_OUTPUT_DIR="$OUTPUT_WD/bg/skim_muons_jpsi"
TWO_LEPTONS_SAME_SIGN_SKIM_OUTPUT_DIR="$TWO_LEPTONS_OUTPUT_WD/bg/skim_sc"
DY_SKIM_OUTPUT_DIR="$OUTPUT_WD/bg/skim_dy"
LC_OUTPUT_DIR="$OUTPUT_WD/bg/lc"
LC_DATA_OUTPUT_DIR="$OUTPUT_WD/data/lc"
SKIM_SIG_OUTPUT_DIR="$OUTPUT_WD/signal/skim"
SKIM_SIG_SAM_OUTPUT_DIR="$OUTPUT_WD/signal/skim_sam"
SKIM_SIG_NLP_OUTPUT_DIR="$OUTPUT_WD/signal/skim_nlp"
TWO_LEPTONS_SKIM_SIG_OUTPUT_DIR="$TWO_LEPTONS_OUTPUT_WD/signal/skim"
TWO_LEPTONS_SAM_SKIM_SIG_OUTPUT_DIR="$TWO_LEPTONS_OUTPUT_WD/signal/skim_sam"
SKIM_DATA_OUTPUT_DIR="$OUTPUT_WD/data/skim"
TWO_LEPTONS_SKIM_DATA_OUTPUT_DIR="$TWO_LEPTONS_OUTPUT_WD/data/skim"
TWO_LEPTONS_SAME_SIGN_SKIM_DATA_OUTPUT_DIR="$TWO_LEPTONS_OUTPUT_WD/data/skim_sc"
DY_SKIM_DATA_OUTPUT_DIR="$OUTPUT_WD/data/skim_dy"
CS_SIG_OUTPUT_DIR="$OUTPUT_WD/signal/cs"
SKIM_SIG_BDT_OUTPUT_DIR="$OUTPUT_WD/signal/skim_signal_bdt"
SKIM_SAM_SIG_BDT_OUTPUT_DIR="$OUTPUT_WD/signal/skim_sam_signal_bdt"
SKIM_DATA_BDT_OUTPUT_DIR="$OUTPUT_WD/data/skim_signal_bdt"
SKIM_BG_SIG_BDT_OUTPUT_DIR="$OUTPUT_WD/bg/skim_signal_bdt"
SKIM_DY_BG_SIG_BDT_OUTPUT_DIR="$DY_OUTPUT_WD/bg/skim_signal_bdt"
SKIM_SIG_DILEPTON_BDT_OUTPUT_DIR="$OUTPUT_WD/signal/skim_dilepton_signal_bdt"
SKIM_SAM_SIG_DILEPTON_BDT_OUTPUT_DIR="$OUTPUT_WD/signal/skim_sam_dilepton_signal_bdt"
SKIM_TWO_LEPTONS_SIG_DILEPTON_BDT_OUTPUT_DIR="$TWO_LEPTONS_OUTPUT_WD/signal/skim_dilepton_signal_bdt"
SKIM_SAM_TWO_LEPTONS_SIG_DILEPTON_BDT_OUTPUT_DIR="$TWO_LEPTONS_OUTPUT_WD/signal/skim_sam_dilepton_signal_bdt"
SKIM_TWO_LEPTONS_BG_DILEPTON_BDT_OUTPUT_DIR="$TWO_LEPTONS_OUTPUT_WD/bg/skim_dilepton_signal_bdt"
SKIM_TWO_LEPTONS_BG_DILEPTON_BDT_SC_OUTPUT_DIR="$TWO_LEPTONS_OUTPUT_WD/bg/skim_dilepton_signal_bdt_sc"
SKIM_BG_SIG_DILEPTON_BDT_OUTPUT_DIR="$OUTPUT_WD/bg/skim_dilepton_signal_bdt"
SKIM_DATA_SIG_DILEPTON_BDT_OUTPUT_DIR="$OUTPUT_WD/data/skim_dilepton_signal_bdt"
SKIM_TWO_LEPTONS_DATA_SIG_DILEPTON_BDT_OUTPUT_DIR="$TWO_LEPTONS_OUTPUT_WD/data/skim_dilepton_signal_bdt"
SKIM_TWO_LEPTONS_DATA_SIG_DILEPTON_BDT_SC_OUTPUT_DIR="$TWO_LEPTONS_OUTPUT_WD/data/skim_dilepton_signal_bdt_sc"


SKIM_SIG_BDT_SC_OUTPUT_DIR="$OUTPUT_WD/signal/skim_signal_bdt_sc"
SKIM_DATA_BDT_SC_OUTPUT_DIR="$OUTPUT_WD/data/skim_signal_bdt_sc"
SKIM_DATA_BDT_DY_OUTPUT_DIR="$DY_OUTPUT_WD/data/skim_signal_bdt"
SKIM_BG_SIG_BDT_SC_OUTPUT_DIR="$OUTPUT_WD/bg/skim_signal_bdt_sc"
SKIM_SIG_DILEPTON_BDT_SC_OUTPUT_DIR="$OUTPUT_WD/signal/skim_dilepton_signal_bdt_sc"
SKIM_BG_SIG_DILEPTON_BDT_SC_OUTPUT_DIR="$OUTPUT_WD/bg/skim_dilepton_signal_bdt_sc"
SKIM_BG_SIG_DILEPTON_BDT_DY_OUTPUT_DIR="$DY_OUTPUT_WD/bg/skim_dilepton_signal_bdt"
SKIM_DATA_SIG_DILEPTON_BDT_SC_OUTPUT_DIR="$OUTPUT_WD/data/skim_dilepton_signal_bdt_sc"
SKIM_DATA_SIG_DILEPTON_BDT_DY_OUTPUT_DIR="$DY_OUTPUT_WD/data/skim_dilepton_signal_bdt"
SKIM_DATA_JPSI_MUONS_OUTPUT_DIR="$OUTPUT_WD/data/skim_muons_jpsi"
SKIM_DATA_MINI_OUTPUT_DIR="$OUTPUT_WD/data/skim_mini"
SKIM_DATA_MASTER_OUTPUT_DIR="$OUTPUT_WD/data/skim_master"
SKIM_DATA_JPSI_SINGLE_ELECTRON_OUTPUT_DIR="$OUTPUT_WD/data/skim_jpsi_single_electron"
SKIM_DATA_Z_PEAK_OUTPUT_DIR="$OUTPUT_WD/data/skim_z"

SIG_DUP_OUTPUT_DIR="$OUTPUT_WD/signal/dup"
LEPTON_TRACK_SPLIT_DIR="$OUTPUT_WD/signal/lepton_track"

SPLIT_JPSI_MASTER_OUTPUT_DIR="$SKIM_MASTER_OUTPUT_DIR/split"

RGS_DIR="/afs/desy.de/user/n/nissanuv/stops/analysis/cut_optimisation/rgs"
RESUMMINO_BIN="/afs/desy.de/user/n/nissanuv/local/bin/resummino"
DILEPTON_BDT_DIR="$OUTPUT_WD/cut_optimisation/tmva/dilepton_bdt"
DILEPTON_TWO_LEPTONS_BDT_DIR="$TWO_LEPTONS_OUTPUT_WD/cut_optimisation/tmva/dilepton_bdt"

if [[ `hostname` == *".desy.de"* ]]; then
    echo Running in DESY
    MKDIR_CMD=mkdir
    COPY_CMD=cp
    LS_CMD=ls
    COPY_DEST_PREFIX=""
    OUTPUT_WD="/nfs/dust/cms/user/diepholq/x1x2x1"
    SIG_CONFIG_OUTPUT_DIR="$OUTPUT_WD/signal/config"
    SIG_AOD_OUTPUT_DIR="$OUTPUT_WD/signal/aod"
    SIG_MINIAOD_OUTPUT_DIR="$OUTPUT_WD/signal/miniaod"
    SIG_NTUPLES_OUTPUT_DIR="$OUTPUT_WD/signal/ntuples"
else
    echo Running in cmslogin
    MKDIR_CMD=gfal-mkdir
    COPY_CMD=gfal-copy
    LS_CMD=gfal-ls
    COPY_DEST_PREFIX="file://"
    OUTPUT_WD="srm://dcache-se-cms.desy.de/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub"
    SIG_CONFIG_OUTPUT_DIR="$OUTPUT_WD/signal/config"
    SIG_AOD_OUTPUT_DIR="$OUTPUT_WD/signal/aod"
    SIG_MINIAOD_OUTPUT_DIR="$OUTPUT_WD/signal/miniaod"
    SIG_NTUPLES_OUTPUT_DIR="$OUTPUT_WD/signal/ntuples"
fi