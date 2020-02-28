#!/bin/bash

. "$CMSSW_BASE/src/cms-tools/lib/def.sh"

shopt -s nullglob
shopt -s expand_aliases

#---------- GET OPTIONS ------------
POSITIONAL=()
while [[ $# -gt 0 ]]
do
    key="$1"

    case $key in
        --tl)
        TWO_LEPTONS=true
        POSITIONAL+=("$1")
        shift
        ;;
        *)    # unknown option
        POSITIONAL+=("$1") # save it in an array for later
        shift # past argument
        ;;
    esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters
#---------- END OPTIONS ------------

OUTPUT_DIR=$SKIM_DATA_OUTPUT_DIR/sum
INPUT_DIR=$SKIM_DATA_OUTPUT_DIR/single
if [ -n "$TWO_LEPTONS" ]; then
        OUTPUT_DIR=$TWO_LEPTONS_SKIM_DATA_OUTPUT_DIR/sum
        INPUT_DIR=$TWO_LEPTONS_SKIM_DATA_OUTPUT_DIR/single
fi


count=0
input_files=""
files_per_job=300
output_count=1
lastfile=""

mkdir $OUTPUT_DIR

for fullname in $INPUT_DIR/*; do
    lastfile=$fullname
    input_files="$input_files $fullname"
    ((count+=1))
    if [ $(($count % $files_per_job)) == 0 ]; then
        output_name=`echo $(basename $fullname .root) | awk -F"METAOD_" "{print \\$1\"METAOD_${output_count}.root\"}"`
        ((output_count+=1))
        echo hadd -f $OUTPUT_DIR/$output_name $input_files
        hadd -f $OUTPUT_DIR/$output_name $input_files
        echo -e "\n\n\n\n\n\n\n"
        #echo rm $input_files
        #rm $input_files
        echo -e "\n\n\n\n\n\n\n"
        input_files=""
    fi
done

if [ $(($count % $files_per_job)) != 0 ]; then
    output_name=`echo $(basename $lastfile .root) | awk -F"METAOD_" "{print \\$1\"METAOD_${output_count}.root\"}"`
    ((output_count+=1))
    echo hadd -f $OUTPUT_DIR/$output_name $input_files
    hadd -f $OUTPUT_DIR/$output_name $input_files
    echo -e "\n\n\n\n\n\n\n"
    #echo rm $input_files
    #rm $input_files
    echo -e "\n\n\n\n\n\n\n"
    input_files=""
fi