#!/bin/bash

. "$CMSSW_BASE/src/stops/lib/def.sh"

shopt -s nullglob 

# necessary for running cmsenv
shopt -s expand_aliases

echo Nopa@2wd | voms-proxy-init -voms cms:/cms -valid 192:00
export X509_USER_PROXY=$(voms-proxy-info | grep path | cut -b 13-)

#check output directory
if [ ! -d "$SIG_AOD_OUTPUT_DIR" ]; then
  mkdir $SIG_AOD_OUTPUT_DIR
fi

if [ ! -d "$SIG_AOD_OUTPUT_DIR/single" ]; then
  mkdir "$SIG_AOD_OUTPUT_DIR/single"
fi

if [ ! -d "$SIG_AOD_OUTPUT_DIR/stdout" ]; then
  mkdir "$SIG_AOD_OUTPUT_DIR/stdout"
fi

if [ ! -d "$SIG_AOD_OUTPUT_DIR/stderr" ]; then
  mkdir "$SIG_AOD_OUTPUT_DIR/stderr"
fi

cd ~/CMSSW_9_4_11/src
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
cmsenv

timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"

cat << EOM > $output_file
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
priority = 0
getenv = True
EOM

for f in $SIG_CONFIG_OUTPUT_DIR/single/*; do
	echo "Will run:"
	filename=$(basename $f .py)
	cmd="$SIM_DIR/simulate/create_aod_single.sh cmsRun $f"
	echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = ${SIG_AOD_OUTPUT_DIR}/stderr/${filename}.err
output = $SIG_AOD_OUTPUT_DIR/stdout/${filename}.output
Queue
EOM
done

condor_submit $output_file
rm $output_file
        
