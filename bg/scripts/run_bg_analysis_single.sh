#!/bin/bash

echo $0 $@

shopt -s nullglob

# necessary for running cmsenv
shopt -s expand_aliases

# CMS ENV
cd ~/CMSSW_10_1_0/src

export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

cmsenv

. "$CMSSW_BASE/src/cms-tools/lib/def.sh"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$CMSSW_BASE/src/cms-tools/lib/classes"

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
        INPUT_FILES="$2"
        shift # past argument
        shift # past value
        ;;
        -h|--help)
        print_help
        exit 0
        ;;
        -skim|--skim)
        SKIM=true
        shift # past argument
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

echo "EXTRA PARAMS: ${POSITIONAL[@]}"

if [ -z "$INPUT_FILES" ]; then
    print_help
    exit 0
fi

SCRIPT_PATH=$ANALYZER_PATH
if [ -n "$SKIM" ]; then
    echo "GOT SKIM"
    SCRIPT_PATH=$SKIMMER_PATH
    OUTPUT_DIR=$SKIM_OUTPUT_DIR
fi

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

    timestamp=$(date +%Y%m%d_%H%M%S%N)

    output_file="${WORK_DIR}/${timestamp}/$(basename $INPUT_FILE)"
    command="$SCRIPT_PATH -i ${INPUT_FILE} -o $output_file -bg ${POSITIONAL[@]}"

    echo "Running command: $command"

    if [ -n "$SIMULATION" ]; then
        echo "IN SIMULATION: NOT RUNNING COMMANDS"
    fi

    if [ -z "$SIMULATION" ]; then
        mkdir $timestamp
        $command
        EXIT_STATUS=$?
        if [[ $EXIT_STATUS -ne 0 ]]; then
            echo "exit code $EXIT_STATUS, skipping copy"
            rm -rf $timestamp
            continue
        else
            mv $output_file "${FILE_OUTPUT}/"
            rm -rf $timestamp
        fi
    fi
done

exit 0