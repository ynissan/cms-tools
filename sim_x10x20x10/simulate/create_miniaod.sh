#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob 

#check output directory
if [ ! -d "$SIG_MINIAOD_OUTPUT_DIR" ]; then
  mkdir $SIG_MINIAOD_OUTPUT_DIR
fi

if [ ! -d "$SIG_MINIAOD_OUTPUT_DIR/single" ]; then
  mkdir "$SIG_MINIAOD_OUTPUT_DIR/single"
fi

if [ ! -d "$SIG_MINIAOD_OUTPUT_DIR/stdout" ]; then
  mkdir "$SIG_MINIAOD_OUTPUT_DIR/stdout"
fi

if [ ! -d "$SIG_MINIAOD_OUTPUT_DIR/stderr" ]; then
  mkdir "$SIG_MINIAOD_OUTPUT_DIR/stderr"
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

for f in $SIG_AOD_OUTPUT_DIR/single/*; do
    filename=`echo $(basename $f) | awk -F"_" '{print $1"_"$2"_"$3"_miniAODSIM_"$5}'`
    fileout=$SIG_MINIAOD_OUTPUT_DIR/single/${filename}
    #echo $fileout
    if [ -f "$fileout" ]; then
        echo "$fileout exist. Skipping..."
        continue
    fi
    logfname=$(basename $filename .root)
    #echo logfname=$logfname
    echo "Will run:"
    cmd="$SIM_DIR/simulate/create_miniaod_single.sh cmsDriver.py step3 --conditions auto:run2_mc --fast --eventcontent MINIAODSIM --runUnscheduled --filein file:$f -s PAT --datatier MINIAODSIM --era Run2_2016 --mc --fileout $fileout -n 500"
    echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = ${SIG_MINIAOD_OUTPUT_DIR}/stderr/${logfname}.err
output = ${SIG_MINIAOD_OUTPUT_DIR}/stdout/${logfname}.output
Queue
EOM
done

condor_submit $output_file
rm $output_file
        
