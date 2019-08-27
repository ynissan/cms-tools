#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob 

# necessary for running cmsenv
shopt -s expand_aliases

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
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
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
+RequestRuntime = 86400
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
        
