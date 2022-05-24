#!/bin/bash

. "$CMSSW_BASE/src/stops/lib/def.sh"

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
    #filename=`echo $(basename $f) | awk -F"_" '{print $1"_"$2"_"$3"_miniAODSIM_"$5}'`
    filename=$(basename $f)
    #fileout=$SIG_MINIAOD_OUTPUT_DIR/single/${filename}
    fileout=$WORK_DIR/${filename}
    #echo $fileout
    if [ -f "$SIG_MINIAOD_OUTPUT_DIR/single/${filename}" ]; then
        echo "$SIG_MINIAOD_OUTPUT_DIR/single/${filename} exist. Skipping..."
        continue
    fi
    logfname=$(basename $filename .root)
    #echo logfname=$logfname
    echo "Will run:"
    cmd="$SIM_DIR/simulate/create_miniaod_single.sh $f $fileout"
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
        
