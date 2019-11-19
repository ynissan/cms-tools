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
        -sc)
        SC=true
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

if [ -n "$SC" ]; then
    echo "GOT SC"
    echo "HERE: $@"
    OUTPUT_DIR=$SKIM_DATA_BDT_SC_OUTPUT_DIR
fi

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
        echo $CONDOR_WRAPPER $SCRIPTS_WD/skimmer_x1x2x1_univ_bdt_track_bdt.py -i $data_file -o ${OUTPUT_DIR}/$filename/single/${data_file_name}.root -tb $LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva/$filename -ub $OUTPUT_WD/cut_optimisation/tmva/total_bdt $@
cat << EOM >> $output_file
arguments = $CONDOR_WRAPPER $SCRIPTS_WD/skimmer_x1x2x1_univ_bdt_track_bdt.py -i $data_file -o ${OUTPUT_DIR}/$filename/single/${data_file_name}.root -tb $LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva/$filename -ub $OUTPUT_WD/cut_optimisation/tmva/total_bdt $@
error = ${OUTPUT_DIR}/$filename/stderr/${data_file_name}.err
output = ${OUTPUT_DIR}/$filename/stdout/${data_file_name}.output
Queue
EOM
    done
done

condor_submit $output_file
rm $output_file
