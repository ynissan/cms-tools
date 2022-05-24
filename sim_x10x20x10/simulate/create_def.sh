#!/bin/bash

. "$CMSSW_BASE/src/stops/lib/def.sh"

shopt -s nullglob 

# necessary for running cmsenv
shopt -s expand_aliases

# echo Nopa@2wd | voms-proxy-init -voms cms:/cms -valid 192:00
# export X509_USER_PROXY=$(voms-proxy-info | grep path | cut -b 13-)

#check output directory
if [ ! -d "$SIG_CONFIG_OUTPUT_DIR" ]; then
    echo Running: $MKDIR_CMD $SIG_CONFIG_OUTPUT_DIR
    $MKDIR_CMD $SIG_CONFIG_OUTPUT_DIR
fi

if [ ! -d "$SIG_CONFIG_OUTPUT_DIR/single" ]; then
  mkdir $SIG_CONFIG_OUTPUT_DIR/single
fi

if [ ! -d "$SIG_CONFIG_OUTPUT_DIR/stdout" ]; then
  mkdir $SIG_CONFIG_OUTPUT_DIR/stdout
fi

if [ ! -d "$SIG_CONFIG_OUTPUT_DIR/stderr" ]; then
  mkdir "$SIG_CONFIG_OUTPUT_DIR/stderr"
fi

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

# CMS ENV
cd ~/CMSSW_9_4_11/src 
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
cmsenv
cd $OLDPWD

count=0

for f in ~/CMSSW_10_1_0/src/Configuration/Generator/python/higgsino*.py; do
    for i in `seq 150`; do
    #for i in 1; do
        ((count+=1))
        echo Running $count
        t=$(date +%N)
        filename=$(basename $f .py)
        configfilename=$(basename $filename _cff)_${t}.py
        #outfilename=$SIG_AOD_OUTPUT_DIR/single/$(basename $filename _cff)_AODSIM_n${t}.root
        outfilename=$WORK_DIR/$(basename $filename _cff)_${t}.root
        echo "Will run:" #GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2:pdigi_valid,DATAMIX,L1,DIGI2RAW,L1Reco,RECO,VALIDATION
        #${SIG_CONFIG_OUTPUT_DIR}/single/$configfilename
        cmd="$SIM_DIR/simulate/create_def_single.sh $filename $WORK_DIR/$configfilename $outfilename"
        echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = $SIG_CONFIG_OUTPUT_DIR/stderr/${configfilename}.err
output = $SIG_CONFIG_OUTPUT_DIR/stdout/${configfilename}.output
Queue
EOM
done
done

condor_submit $output_file
rm $output_file
        
