#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob 

#check output directory
if [ ! -d "$SIG_DUP_OUTPUT_DIR" ]; then
  mkdir $SIG_DUP_OUTPUT_DIR
fi

if [ ! -d "$SIG_DUP_OUTPUT_DIR/single" ]; then
  mkdir "$SIG_DUP_OUTPUT_DIR/single"
fi

if [ ! -d "$SIG_DUP_OUTPUT_DIR/stdout" ]; then
  mkdir "$SIG_DUP_OUTPUT_DIR/stdout"
fi

if [ ! -d "$SIG_DUP_OUTPUT_DIR/stderr" ]; then
  mkdir "$SIG_DUP_OUTPUT_DIR/stderr"
fi

module load root6

timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"

cat << EOM > $output_file
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
priority = 0
EOM

for sim in $NEWESTEST_SIM_DIR/*; do
	echo "$sim";
	echo "Will run:"
	echo $CLONE_SINGLE -i $sim -o ${SIG_DUP_OUTPUT_DIR}/single/`basename ${sim}`
cat << EOM >> $output_file
arguments = $CLONE_SINGLE -i $sim -o ${SIG_DUP_OUTPUT_DIR}/single/`basename ${sim}`
error = ${SIG_DUP_OUTPUT_DIR}/stderr/`basename ${sim}`.err
output = ${SIG_DUP_OUTPUT_DIR}/stdout/`basename ${sim}`.output
Queue
EOM
done

condor_submit $output_file
rm $output_file
        
