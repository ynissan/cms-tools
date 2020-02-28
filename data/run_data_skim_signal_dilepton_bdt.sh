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

# CMS ENV
cd $CMS_WD
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

OUTPUT_DIR=$SKIM_DATA_SIG_DILEPTON_BDT_OUTPUT_DIR
INPUT_DIR=$SKIM_DATA_BDT_OUTPUT_DIR
BDT_DIR=$OUTPUT_WD/cut_optimisation/tmva/dilepton_bdt
EXTRA_FLAGS=""

if [ -n "$SC" ]; then
    echo "GOT SC"
    echo "HERE: $@"
    OUTPUT_DIR=$SKIM_DATA_SIG_DILEPTON_BDT_SC_OUTPUT_DIR
    INPUT_DIR=$SKIM_DATA_BDT_SC_OUTPUT_DIR
elif [ -n "$TWO_LEPTONS" ]; then
    OUTPUT_DIR=$SKIM_TWO_LEPTONS_DATA_SIG_DILEPTON_BDT_OUTPUT_DIR
    INPUT_DIR=$TWO_LEPTONS_SKIM_DATA_OUTPUT_DIR/sum
    BDT_DIR=$TWO_LEPTONS_OUTPUT_WD/cut_optimisation/tmva/dilepton_bdt
    EXTRA_FLAGS="--tl"
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
for sim in $BDT_DIR/*; do    
    filename=`echo $(basename $sim)`
    echo $filename
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
    
    if [ -n "$TWO_LEPTONS" ]; then
        DATA_DIR=$INPUT_DIR
    else
        DATA_DIR=$INPUT_DIR/$tb/single
    fi

    for data_file in $DATA_DIR/*; do
        echo "Will run:"
        data_file_name=$(basename $data_file .root)
        cmd="$CONDOR_WRAPPER $SCRIPTS_WD/skimmer_x1x2x1_dilepton_bdt.py --data -i $data_file -o ${OUTPUT_DIR}/$tb/single/${data_file_name}.root -bdt $BDT_DIR/$tb $EXTRA_FLAGS"
        echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = ${OUTPUT_DIR}/$tb/stderr/${data_file_name}.err
output = ${OUTPUT_DIR}/$tb/stdout/${data_file_name}.output
Queue
EOM
    done
done

condor_submit $output_file
rm $output_file
