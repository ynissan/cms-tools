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

for sim in "${!SIMS[@]}"; do
	echo "$sim - ${SIMS[$sim]}";
	echo "Will run:"
	echo $CLONE_SINGLE -i ${SIMS[$sim]} -o ${SIG_DUP_OUTPUT_DIR}/single/${sim}
read -r -d '' CMD << EOM
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
arguments = $CLONE_SINGLE -i ${SIMS[$sim]} -o ${SIG_DUP_OUTPUT_DIR}/single/${sim}
error = ${SIG_DUP_OUTPUT_DIR}/stderr/${sim}.err
output = ${SIG_DUP_OUTPUT_DIR}/stdout/${sim}.output
notification = Never
priority = 0
Queue
EOM

	echo "$CMD" | condor_submit &
done
        
