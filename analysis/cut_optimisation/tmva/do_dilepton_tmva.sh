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


timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"


if [ -n "$TWO_LEPTONS" ]; then
    OUTPUT_DIR=$DILEPTON_TWO_LEPTONS_BDT_DIR
    INPUT_SIG_DIR=$TWO_LEPTONS_SKIM_SIG_OUTPUT_DIR/sum
    BG_INPUT=$TWO_LEPTONS_SKIM_OUTPUT_DIR/sum/type_sum
else
    OUTPUT_DIR=$DILEPTON_BDT_DIR
    INPUT_SIG_DIR=$SKIM_SIG_BDT_OUTPUT_DIR
    BG_INPUT=$SKIM_BG_SIG_BDT_OUTPUT_DIR
fi

#check output directory
if [ ! -d "$OUTPUT_DIR" ]; then
    mkdir $OUTPUT_DIR
else
    rm -rf $OUTPUT_DIR
    mkdir $OUTPUT_DIR
fi

cat << EOM > $output_file
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
priority = 0
+RequestRuntime = 86400
EOM

for group in "${!SIM_GROUP[@]}"; do
    value=${SIM_GROUP[$group]}
    input=""
    background=""
    for pattern in $value; do
        if [ -n "$TWO_LEPTONS" ]; then
            input="$input $INPUT_SIG_DIR/*$pattern*.root"
        else
            input="$input $INPUT_SIG_DIR/single/*$pattern*.root"
        fi
    done
    dir="$OUTPUT_DIR/${group}"
    mkdir $dir
    echo "Will run:"
    if [ -n "$TWO_LEPTONS" ]; then
        cmd="$CONDOR_WRAPPER $CUT_OPTIMISATION_SCRIPTS/dilepton_tmva.py -i $input -bg  $BG_INPUT --no_norm -o $dir/${group}.root  --tl"
    else
        cmd="$CONDOR_WRAPPER $CUT_OPTIMISATION_SCRIPTS/dilepton_tmva.py -i $input -bg  $BG_INPUT/${group}/single --no_norm -o $dir/${group}.root"
    fi
    echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = ${dir}/${group}.err
output = ${dir}/${group}.output
Queue
EOM
done

condor_submit $output_file
rm $output_file