#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob


# necessary for running cmsenv
shopt -s expand_aliases

# CMS ENV
cd $CMS_WD
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/afs/desy.de/user/n/nissanuv/cms-tools/lib/classes

SCRIPT_PATH=$SKIMMER_PATH

#---------- GET OPTIONS ------------
POSITIONAL=()
while [[ $# -gt 0 ]]
do
    key="$1"

    case $key in
        -i|--input)
        INPUT_FILES="$2"
        shift # past argument
        shift # past value
        ;;
        *)    # unknown option
        POSITIONAL+=("$1") # save it in an array for later
        shift # past argument
        ;;
    esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters
#---------- END OPTIONS ------------


OUTPUT_DIR=$SKIM_DATA_OUTPUT_DIR
FILE_OUTPUT="${OUTPUT_DIR}/single"

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

echo INTPUT_FILES=$INPUT_FILES

for INPUT_FILE in $INPUT_FILES; do

    #timestamp=$(date +%Y%m%d_%H%M%S%N)

    #output_file="${WORK_DIR}/${timestamp}/$(basename $INPUT_FILE)"
    output_file="${FILE_OUTPUT}/$(basename $INPUT_FILE)"
    command="$SCRIPT_PATH -i ${INPUT_FILE} -o $output_file  ${POSITIONAL[@]}"

    echo "Running command: $command"

    if [ -n "$SIMULATION" ]; then
        echo "IN SIMULATION: NOT RUNNING COMMANDS"
    fi

    if [ -z "$SIMULATION" ]; then
        #mkdir $timestamp
        eval $command
        #mv $output_file "${FILE_OUTPUT}/"
        #rm -rf $timestamp
    fi
done

