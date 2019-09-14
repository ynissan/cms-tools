#!/bin/bash

. "$CMSSW_BASE/src/cms-tools/lib/def.sh"

shopt -s nullglob

# necessary for running cmsenv
shopt -s expand_aliases

# CMS ENV
cd ~/CMSSW_9_4_11/src
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

cd $CMSSW_BASE/src/TreeMaker/Production/test

echo PWD = $PWD

cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=Summer16MiniAODv3Fastsig dataset=file:$1 outfile=$2 numevents=500

exit_code=$?
echo Output Code: $exit_code

if [ "$exit_code" -eq "0" ]
then
    echo Running: $COPY_CMD ${COPY_DEST_PREFIX}$2 $SIG_NTUPLES_OUTPUT_DIR/single/
    $COPY_CMD ${COPY_DEST_PREFIX}$2 $SIG_NTUPLES_OUTPUT_DIR/single/
fi

rm $2_RA2AnalysisTree.root