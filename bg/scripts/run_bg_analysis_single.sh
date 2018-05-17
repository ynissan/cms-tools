#!/bin/bash

# CONSTS
. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

# necessary for running cmsenv
shopt -s expand_aliases

print_help() {
	echo "$0 -i input_file [-s|--simulation]"
	echo -e "\t-s simulation: will not run command"
} 


#---------- GET OPTIONS ------------
POSITIONAL=()
while [[ $# -gt 0 ]]
do
	key="$1"

	case $key in
	    -i|--input)
	    INPUT_FILE="$2"
	    shift # past argument
	    shift # past value
	    ;;
	    -h|--help)
	    print_help
	    exit 0
	    ;;
	    -s|--simulation)
	    SIMULATION=true
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

if [ -z "$INPUT_FILE" ]; then
	print_help
	exit 0
fi

echo "EXTRA PARAMS: ${POSITIONAL[@]}"

# CMS ENV
cd $CMS_WD
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

#check output directory
if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir $OUTPUT_DIR
fi

#check output directory
if [ ! -d "$FILE_OUTPUT" ]; then
  mkdir $FILE_OUTPUT
fi


# RUN ANALYSIS
cd $WORK_DIR
timestamp=$(date +%Y%m%d_%H%M%S%N)

output_file="${WORK_DIR}/${timestamp}/$(basename $INPUT_FILE)"
command="$ANALYZER_PATH -i ${INPUT_FILE} -o $output_file -bg ${POSITIONAL[@]}"

if [ -n "$SIMULATION" ]; then
	echo "IN SIMULATION: NOT RUNNING COMMANDS"
fi

echo "Running command: $command"

if [ -z "$SIMULATION" ]; then
	mkdir $timestamp
	eval $command
	mv $output_file "${FILE_OUTPUT}/"
	rm -rf $timestamp
fi

exit 0