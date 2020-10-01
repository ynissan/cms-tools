#!/bin/bash

shopt -s nullglob

# necessary for running cmsenv
shopt -s expand_aliases

# CMS ENV
cd ~/CMSSW_10_1_0/src

export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

cmsenv

. "$CMSSW_BASE/src/cms-tools/lib/def.sh"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$CMSSW_BASE/src/cms-tools/lib/classes"

#for f in ZJetsToNuNu_HT-100To200.root ZJetsToNuNu_HT-200To400.root WJetsToLNu_HT-200To400.root ZJetsToNuNu_HT-600To800.root ZJetsToNuNu_HT-400To600.root WJetsToLNu_HT-100To200.root WJetsToLNu_HT-1200To2500.root; do 
#for f in WJetsToLNu_HT-200To400.root; do 
#for f in ZJetsToNuNu_HT-100To200.root ZJetsToNuNu_HT-200To400.root WJetsToLNu_HT-200To400.root ZJetsToNuNu_HT-600To800.root ZJetsToNuNu_HT-400To600.root WJetsToLNu_HT-100To200.root WJetsToLNu_HT-1200To2500.root; do 
#for f in WW_TuneCUETP8M1.root DYJetsToLL_M-50_HT-100to200.root DYJetsToLL_M-50_HT-200to400.root DYJetsToLL_M-50_HT-400to600.root DYJetsToLL_M-50_HT-600to800.root ST_t-channel_antitop.root TTJets_DiLept.root TTJets_SingleLeptFromT.root TTJets_SingleLeptFromTbar.root WJetsToLNu_HT-600To800.root ST_t-channel_top.root DYJetsToLL_M-50_HT-100to200.root DYJetsToLL_M-50_HT-200to400.root DYJetsToLL_M-50_HT-400to600.root DYJetsToLL_M-50_HT-600to800.root ST_t-channel_antitop.root TTJets_DiLept.root TTJets_SingleLeptFromT.root TTJets_SingleLeptFromTbar.root WJetsToLNu_HT-600To800.root ST_t-channel_top WJetsToLNu_HT-200To400.root ZJetsToNuNu_HT-100To200.root ZJetsToNuNu_HT-200To400.root ZJetsToNuNu_HT-600To800.root ZJetsToNuNu_HT-400To600.root WJetsToLNu_HT-100To200.root WJetsToLNu_HT-1200To2500.root; do 
#for f in WJetsToLNu_HT-200To400_TuneCUETP8M1.root WJetsToLNu_HT-600To800_TuneCUETP8M1.root; do
#for f in WJetsToLNu_HT-200To400_TuneCUETP8M1.root WJetsToLNu_HT-600To800_TuneCUETP8M1.root TTJets_DiLept_TuneCUETP8M1.root TTJets_SingleLeptFromT_TuneCUETP8M1.root TTJets_SingleLeptFromTbar_TuneCUETP8M1.root ST_t-channel_top.root ZJetsToNuNu_HT-100To200_13TeV-madgraph.root ZJetsToNuNu_HT-200To400_13TeV-madgraph.root ZJetsToNuNu_HT-400To600_13TeV-madgraph.root; do
i=1
for f in ST_t-channel_top.root TTJets_DiLept_TuneCUETP8M1.root TTJets_SingleLeptFromT_TuneCUETP8M1.root TTJets_SingleLeptFromTbar_TuneCUETP8M1.root WJetsToLNu_HT-1200To2500_TuneCUETP8M1.root WJetsToLNu_HT-200To400_TuneCUETP8M1.root WJetsToLNu_HT-400To600_TuneCUETP8M1.root WJetsToLNu_HT-600To800_TuneCUETP8M1.root WJetsToLNu_HT-800To1200_TuneCUETP8M1.root ZJetsToNuNu_HT-100To200_13TeV-madgraph.root ZJetsToNuNu_HT-200To400_13TeV-madgraph.root ZJetsToNuNu_HT-400To600_13TeV-madgraph.root; do
    if [ ! -f "$SKIM_OUTPUT_DIR/sum/type_sum/$f" ]; then
        echo "$SKIM_OUTPUT_DIR/sum/type_sum/$f does not exist. Skipping..."
        continue
    fi
    firstfile=$(basename $f .root)_1.root
    if [ -f "$SKIM_OUTPUT_DIR/sum/type_sum/$firstfile" ]; then
        echo "$SKIM_OUTPUT_DIR/sum/type_sum/$firstfile exists. Skipping..."
        continue
    fi
    echo $SCRIPTS_WD/skim_split.py -i $SKIM_OUTPUT_DIR/sum/type_sum/$f
    nohup $SCRIPTS_WD/skim_split.py -i $SKIM_OUTPUT_DIR/sum/type_sum/$f | tee ./nohupout_$i &
    
    ((i+=1)) 
done