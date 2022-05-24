#!/bin/bash

shopt -s nullglob

# necessary for running cmsenv
shopt -s expand_aliases

# CMS ENV
cd ~/CMSSW_10_1_0/src

export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

cmsenv

. "$CMSSW_BASE/src/stops/lib/def.sh"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$CMSSW_BASE/src/stops/lib/classes"


for f in ST_t-channel_antitop.root ST_t-channel_top.root TTJets_SingleLeptFromT_TuneCUETP8M1.root TTJets_DiLept_TuneCUETP8M1.root TTJets_SingleLeptFromTbar_TuneCUETP8M1.root WJetsToLNu_HT-1200To2500_TuneCUETP8M1.root WJetsToLNu_HT-200To400_TuneCUETP8M1.root WJetsToLNu_HT-400To600_TuneCUETP8M1.root WJetsToLNu_HT-600To800_TuneCUETP8M1.root WJetsToLNu_HT-800To1200_TuneCUETP8M1.root ZJetsToNuNu_HT-100To200_13TeV-madgraph.root ZJetsToNuNu_HT-200To400_13TeV-madgraph.root ZJetsToNuNu_HT-400To600_13TeV-madgraph.root ZJetsToNuNu_HT-600To800_13TeV-madgraph.root ZJetsToNuNu_HT-800To1200_13TeV-madgraph.root; do
    if [ -f "$NLP_SKIM_OUTPUT_DIR/sum/type_sum/$f" ]; then
        echo "$f exists."
        echo $SCRIPTS_WD/skim_split.py -i $NLP_SKIM_OUTPUT_DIR/sum/type_sum/$f | tee /tmp/$f 
        $SCRIPTS_WD/skim_split.py -i $NLP_SKIM_OUTPUT_DIR/sum/type_sum/$f | tee /tmp/$f 
    else 
        echo "$f does not exist. Skipping."
    fi
done