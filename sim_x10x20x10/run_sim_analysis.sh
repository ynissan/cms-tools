#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob

#---------- GET OPTIONS ------------
POSITIONAL=()
while [[ $# -gt 0 ]]
do
	key="$1"

	case $key in
	    -skim|--skim)
	    SKIM=true
	    POSITIONAL+=("$1") # save it in an array for later
	    shift # past argument
	    ;;
	    *)    # unknown option
	    POSITIONAL+=("$1") # save it in an array for later
	    shift # past argument
	    ;;
	esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters
#---------- END OPTIONS ------------

# CMS ENV
cd $CMS_WD
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

OUTPUT_DIR=$SIM_DIR
if [ -n "$SKIM" ]; then
	OUTPUT_DIR=$SKIM_SIG_OUTPUT_DIR	
fi

#check output directory
if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir $OUTPUT_DIR
fi

#check output directory
if [ ! -d "$OUTPUT_DIR/single" ]; then
  mkdir "$OUTPUT_DIR/single"
fi

if [ ! -d "$OUTPUT_DIR/stdout" ]; then
  mkdir "$OUTPUT_DIR/stdout"
fi

if [ ! -d "$OUTPUT_DIR/stderr" ]; then
  mkdir "$OUTPUT_DIR/stderr"
fi

for sim in "${!SIMS[@]}"; do
	echo "$sim - ${SIMS[$sim]}";
	INPUT_FILE=${SIMS[$sim]}
	if [ -n "$SKIM" ]; then
		INPUT_FILE=${SIG_DUP_OUTPUT_DIR}/single/${sim}.root
	fi
	echo "Will run:"
	echo $SIM_DIR/run_sim_analysis_single.sh -i $INPUT_FILE -o ${OUTPUT_DIR}/single/${sim}.root ${POSITIONAL[@]}
read -r -d '' CMD << EOM
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
arguments = $SIM_DIR/run_sim_analysis_single.sh -i $INPUT_FILE -o ${OUTPUT_DIR}/single/${sim}.root ${POSITIONAL[@]}
error = ${OUTPUT_DIR}/stderr/${sim}.err
output = ${OUTPUT_DIR}/stdout/${sim}.output
notification = Never
priority = 0
Queue
EOM

	echo "$CMD" | condor_submit &
done
