#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob 

# necessary for running cmsenv
shopt -s expand_aliases

#check output directory
if [ ! -d "$SIG_NTUPLES_OUTPUT_DIR" ]; then
  mkdir $SIG_NTUPLES_OUTPUT_DIR
fi

if [ ! -d "$SIG_NTUPLES_OUTPUT_DIR/single" ]; then
  mkdir "$SIG_NTUPLES_OUTPUT_DIR/single"
fi

if [ ! -d "$SIG_NTUPLES_OUTPUT_DIR/stdout" ]; then
  mkdir "$SIG_NTUPLES_OUTPUT_DIR/stdout"
fi

if [ ! -d "$SIG_NTUPLES_OUTPUT_DIR/stderr" ]; then
  mkdir "$SIG_NTUPLES_OUTPUT_DIR/stderr"
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
EOM

for f in $SIG_MINIAOD_OUTPUT_DIR/single/*; do
	echo "Will run:"
	filename=`echo $(basename $f) | awk -F"_" '{print $1"_"$2"_"$3"_"$5}'`
	logfname=$(basename $filename .root)
	echo logfname=$logfname
	cmd="$SIM_DIR/simulate/create_ntuples_single.sh cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=Summer16MiniAODv3Fastsig dataset=file:$f outfile=$SIG_NTUPLES_OUTPUT_DIR/single/${logfname} numevents=500"
	echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = ${SIG_NTUPLES_OUTPUT_DIR}/stderr/${logfname}.err
output = ${SIG_NTUPLES_OUTPUT_DIR}/stdout/${logfname}.output
Queue
EOM
done

condor_submit $output_file
rm $output_file
        
