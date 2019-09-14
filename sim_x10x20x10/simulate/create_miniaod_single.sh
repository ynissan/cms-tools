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

echo Nopa@2wd | voms-proxy-init -voms cms:/cms -valid 192:00
export X509_USER_PROXY=$(voms-proxy-info | grep path | cut -b 13-)

cmsDriver.py step3 --conditions auto:run2_mc --fast --eventcontent MINIAODSIM --runUnscheduled --filein file:$1 -s PAT --datatier MINIAODSIM --era Run2_2016 --mc --fileout $2 -n 500

exit_code=$?
echo Output Code: $exit_code

if [ "$exit_code" -eq "0" ]
then
    echo Running: $COPY_CMD ${COPY_DEST_PREFIX}$2 $SIG_MINIAOD_OUTPUT_DIR/single/
    $COPY_CMD ${COPY_DEST_PREFIX}$2 $SIG_MINIAOD_OUTPUT_DIR/single/
fi

rm $2