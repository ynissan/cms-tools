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

i=1

for f in TTJets_DiLept_TuneCUETP8M1.root TTJets_SingleLeptFromT_TuneCUETP8M1.root TTJets_SingleLeptFromTbar_TuneCUETP8M1.root; do
    if [ ! -f "$DY_SKIM_OUTPUT_DIR/sum/type_sum/$f" ]; then
        echo "$DY_SKIM_OUTPUT_DIR/sum/type_sum/$f does not exist. Skipping..."
        continue
    fi
    firstfile=$(basename $f .root)_1.root
    if [ -f "$DY_SKIM_OUTPUT_DIR/sum/type_sum/$firstfile" ]; then
        echo "$DY_SKIM_OUTPUT_DIR/sum/type_sum/$firstfile exists. Skipping..."
        continue
    fi
    echo $SCRIPTS_WD/skim_split.py -i $DY_SKIM_OUTPUT_DIR/sum/type_sum/$f
    nohup $SCRIPTS_WD/skim_split.py -i $DY_SKIM_OUTPUT_DIR/sum/type_sum/$f | tee ./nohupout_$i &
    
    ((i+=1)) 
done