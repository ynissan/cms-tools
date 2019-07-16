#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

count=0
input_files=""
files_per_job=150
output_count=1
lastfile=""

mkdir $SKIM_DATA_OUTPUT_DIR/sum

for fullname in $SKIM_DATA_OUTPUT_DIR/single/*; do
    lastfile=$fullname
    input_files="$input_files $fullname"
    ((count+=1))
    if [ $(($count % $files_per_job)) == 0 ]; then
        output_name=`echo $(basename $fullname .root) | awk -F"METAOD_" "{print \\$1\"METAOD_${output_count}.root\"}"`
        ((output_count+=1))
        echo hadd -f $SKIM_DATA_OUTPUT_DIR/sum/$output_name $input_files
        hadd -f $SKIM_DATA_OUTPUT_DIR/sum/$output_name $input_files
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
    echo hadd -f $SKIM_DATA_OUTPUT_DIR/sum/$output_name $input_files
    hadd -f $SKIM_DATA_OUTPUT_DIR/sum/$output_name $input_files
    echo -e "\n\n\n\n\n\n\n"
    #echo rm $input_files
    #rm $input_files
    echo -e "\n\n\n\n\n\n\n"
    input_files=""
fi