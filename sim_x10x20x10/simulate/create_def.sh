#!/bin/bash

. "$CMSSW_BASE/src/cms-tools/lib/def.sh"

shopt -s nullglob 

# necessary for running cmsenv
shopt -s expand_aliases

#check output directory
if [ ! -d "$SIG_CONFIG_OUTPUT_DIR" ]; then
  $MKDIR_CMD $SIG_CONFIG_OUTPUT_DIR
fi

if [ ! -d "$HOME/config" ]; then
  mkdir $HOME/config
fi

if [ ! -d "$HOME/config/stdout" ]; then
  mkdir $HOME/config/stdout
fi

if [ ! -d "$HOME/config/stderr" ]; then
  mkdir "$HOME/config/stderr"
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
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv
cd $OLDPWD

count=0

for f in ~/CMSSW_9_4_11/src/Configuration/Generator/python/higgsino*.py; do
    #for i in `seq 120`; do
    for i in 1; do
        ((count+=1))
        echo Running $count
        t=$(date +%N)
        filename=$(basename $f .py)
        configfilename=$(basename $filename _cff)_${t}.py
        #outfilename=$SIG_AOD_OUTPUT_DIR/single/$(basename $filename _cff)_AODSIM_n${t}.root
        outfilename=$WORK_DIR/$(basename $filename _cff)_AODSIM_n${t}.root
        echo "Will run:" #GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2:pdigi_valid,DATAMIX,L1,DIGI2RAW,L1Reco,RECO,VALIDATION
        #${SIG_CONFIG_OUTPUT_DIR}/single/$configfilename
        cmd="$SIM_DIR/simulate/create_def_single.sh $filename $WORK_DIR/$configfilename $outfilename"
        echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = $HOME/config/stderr/${configfilename}.err
output = $HOME/config/stdout/${configfilename}.output
Queue
EOM
done
done

condor_submit $output_file
rm $output_file
        
