#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob 

# necessary for running cmsenv
shopt -s expand_aliases

#check output directory
if [ ! -d "$SIG_CONFIG_OUTPUT_DIR" ]; then
  mkdir $SIG_CONFIG_OUTPUT_DIR
fi

if [ ! -d "$SIG_CONFIG_OUTPUT_DIR/single" ]; then
  mkdir "$SIG_CONFIG_OUTPUT_DIR/single"
fi

if [ ! -d "$SIG_CONFIG_OUTPUT_DIR/stdout" ]; then
  mkdir "$SIG_CONFIG_OUTPUT_DIR/stdout"
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
cd ~/CMSSW_8_0_5_patch1/src
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv
cd $OLDPWD

for f in ~/CMSSW_8_0_5_patch1/src/Configuration/Generator/python/higgsino*.py; do
	for i in `seq 20`; do
		t=$(date +%N)
		filename=$(basename $f .py)
		configfilename=$(basename $filename _cff)_${t}.py
		outfilename=$SIG_AOD_OUTPUT_DIR/single/$(basename $filename _cff)_AODSIM_n${t}.root
		echo "Will run:"
		cmd="$SIM_DIR/simulate/create_def_single.sh cmsDriver.py $filename --conditions auto:run2_mc --fast --era Run2_2016 --eventcontent AODSIM --relval 100000,1000 -s GEN,SIM,RECOBEFMIX,DIGI:pdigi_valid,L1,DIGI2RAW,L1Reco,RECO,EI,HLT:@relval25ns --datatier AODSIM --beamspot Realistic50ns13TeVCollision --python_filename=${SIG_CONFIG_OUTPUT_DIR}/single/$configfilename --fileout $outfilename --no_exec -n 5000"
		echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = ${CS_SIG_OUTPUT_DIR}/stderr/${filename}.err
output = $SIG_CONFIG_OUTPUT_DIR/stdout/${filename}.output
Queue
EOM
done
done

condor_submit $output_file
rm $output_file
        
