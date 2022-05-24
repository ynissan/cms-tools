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


for f in TTJets_SingleLeptFromT_TuneCUETP8M1.root TTJets_DiLept_TuneCUETP8M1.root TTJets_SingleLeptFromTbar_TuneCUETP8M1.root; do
    echo $SCRIPTS_WD/skim_split.py -i $TWO_LEPTONS_SKIM_OUTPUT_DIR/sum/type_sum/$f | tee /tmp/$f 
    $SCRIPTS_WD/skim_split.py -i $TWO_LEPTONS_SKIM_OUTPUT_DIR/sum/type_sum/$f | tee /tmp/$f 
done