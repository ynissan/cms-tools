#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob
shopt -s expand_aliases


# CMS ENV
cd $CMS_WD
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"

OUTPUT_DIR=$SKIM_DATA_BDT_OUTPUT_DIR

echo $OUTPUT_DIR
#check output directory
if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir $OUTPUT_DIR
fi

cat << EOM > $output_file
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
priority = 0
EOM

for sim in $LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva/*; do
    echo $sim
    filename=$(basename $sim)
    echo $filename
    if [ ! -d "$OUTPUT_DIR/$filename" ]; then
      mkdir $OUTPUT_DIR/$filename
    fi

    #check output directory
    if [ ! -d "$OUTPUT_DIR/$filename/single" ]; then
      mkdir "$OUTPUT_DIR/$filename/single"
    fi

    if [ ! -d "$OUTPUT_DIR/$filename/stdout" ]; then
      mkdir "$OUTPUT_DIR/$filename/stdout" 
    fi

    if [ ! -d "$OUTPUT_DIR/$filename/stderr" ]; then
      mkdir "$OUTPUT_DIR/$filename/stderr"
    fi

    #for bg_file in $SKIM_OUTPUT_DIR/sum/type_sum/*ZJetsToNuNu_HT-100To200*; do
    for data_file in $SKIM_DATA_OUTPUT_DIR/sum/*; do
        echo "Will run:"
        data_file_name=$(basename $data_file .root)
        echo $SCRIPTS_WD/run_skim_signal_bdt_single.sh -i $data_file -o ${OUTPUT_DIR}/$filename/single/${data_file_name}.root -tb $LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva/$filename -ub $OUTPUT_WD/cut_optimisation/tmva/total_bdt
cat << EOM >> $output_file
arguments = $SCRIPTS_WD/run_skim_signal_bdt_single.sh -i $data_file -o ${OUTPUT_DIR}/$filename/single/${data_file_name}.root -tb $LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva/$filename -ub $OUTPUT_WD/cut_optimisation/tmva/total_bdt
error = ${OUTPUT_DIR}/$filename/stderr/${data_file_name}.err
output = ${OUTPUT_DIR}/$filename/stdout/${data_file_name}.output
Queue
EOM
    done
done

condor_submit $output_file
rm $output_file
