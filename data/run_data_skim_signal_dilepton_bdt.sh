#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

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

OUTPUT_DIR=$SKIM_DATA_SIG_DILEPTON_BDT_OUTPUT_DIR
INPUT_DIR=$SKIM_DATA_BDT_OUTPUT_DIR

if [ -n "$SC" ]; then
    echo "GOT SC"
    echo "HERE: $@"
    OUTPUT_DIR=$SKIM_DATA_SIG_DILEPTON_BDT_SC_OUTPUT_DIR
    INPUT_DIR=$SKIM_DATA_BDT_SC_OUTPUT_DIR
fi

timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"

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

#for sim in $SKIM_BG_SIG_BDT_OUTPUT_DIR/*; do
for sim in $INPUT_DIR/*; do    
    filename=`echo $(basename $sim)`
    echo $filename
    echo here
    tb=$filename

    if [ ! -d "$OUTPUT_DIR/$tb" ]; then
      mkdir $OUTPUT_DIR/$tb
    fi

    #check output directory
    if [ ! -d "$OUTPUT_DIR/$tb/single" ]; then
      mkdir "$OUTPUT_DIR/$tb/single"
    fi

    if [ ! -d "$OUTPUT_DIR/$tb/stdout" ]; then
      mkdir "$OUTPUT_DIR/$tb/stdout" 
    fi

    if [ ! -d "$OUTPUT_DIR/$tb/stderr" ]; then
      mkdir "$OUTPUT_DIR/$tb/stderr"
    fi

    for data_file in $INPUT_DIR/$tb/single/*; do
        echo "Will run:"
        data_file_name=$(basename $data_file .root)
        echo $SCRIPTS_WD/run_skim_signal_dilepton_bdt_single.sh -i $data_file -o ${OUTPUT_DIR}/$tb/single/${data_file_name}.root -bdt $OUTPUT_WD/cut_optimisation/tmva/dilepton_bdt/$tb 
cat << EOM >> $output_file
arguments = $SCRIPTS_WD/run_skim_signal_dilepton_bdt_single.sh -i $data_file -o ${OUTPUT_DIR}/$tb/single/${data_file_name}.root -bdt $OUTPUT_WD/cut_optimisation/tmva/dilepton_bdt/$tb 
error = ${OUTPUT_DIR}/$tb/stderr/${data_file_name}.err
output = ${OUTPUT_DIR}/$tb/stdout/${data_file_name}.output
Queue
EOM
    done
done

condor_submit $output_file
rm $output_file
