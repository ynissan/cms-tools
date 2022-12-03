#!/bin/bash

. "$CMSSW_BASE/src/cms-tools/lib/def.sh"

shopt -s nullglob
shopt -s expand_aliases

timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"

#---------- GET OPTIONS ------------
POSITIONAL=()
while [[ $# -gt 0 ]]
do
    key="$1"

    case $key in
        --phase1)
        PHASE1=true
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

cat << EOM > $output_file
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
priority = 0
+RequestRuntime = 86400
request_memory = 16 GB
EOM

SPLIT_DIR=$LEPTON_TRACK_SPLIT_DIR

SIM_GROUP_KEYS="${!SIM_GROUP[@]}"
echo "SIM_GROUP_KEYS $SIM_GROUP_KEYS"
if [ -n "$PHASE1" ]; then
    SPLIT_DIR=$LEPTON_TRACK_PHASE1_SPLIT_DIR
    SIM_GROUP_KEYS="${!SIM_GROUP_PHASE1[@]}"
fi

if [ ! -d "$SPLIT_DIR/cut_optimisation" ]; then
    mkdir "$SPLIT_DIR/cut_optimisation"
fi

if [ ! -d "$SPLIT_DIR/cut_optimisation/tmva" ]; then
    mkdir "$SPLIT_DIR/cut_optimisation/tmva"
else
    #rm -rf "$LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva"
    mkdir "$SPLIT_DIR/cut_optimisation/tmva"
fi

for group in $SIM_GROUP_KEYS; do
    echo "Running on group $group"
    value=""
    if [ -n "$PHASE1" ]; then
        value=${SIM_GROUP_PHASE1[$group]}
    else
        value=${SIM_GROUP[$group]}
    fi
    echo "Value is $value"
    input=""
    background=""
    for pattern in $value; do
        input="$input $SPLIT_DIR/single/*$pattern*_sig.root"
        background="$background $SPLIT_DIR/single/*$pattern*_bg.root"
    done
    for lep in Electrons Muons; do
        dir="$SPLIT_DIR/cut_optimisation/tmva/${lep}"
        mkdir $dir
        cmd="$CONDOR_WRAPPER $CUT_OPTIMISATION_SCRIPTS/track_tmva.py -i $input -bg  $background --no_norm -o $dir/${lep}.root -lep $lep"
        echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = ${dir}/${lep}.err
output = ${dir}/${lep}.output
Queue
EOM
    done
done

# for sig in $LEPTON_TRACK_SPLIT_DIR/single/*_sig.root; do
#     filename=$(basename $sig _sig.root)
#     dir="$LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva/${filename}"
#     mkdir $dir
#     echo "Will run:"
#     echo $CMS_TOOLS/analysis/cut_optimisation/tmva/run_track_on_grid.sh -i $sig -bg  $LEPTON_TRACK_SPLIT_DIR/single/${filename}_bg.root --no_norm -o $dir/${filename}.root
# cat << EOM >> $output_file
# arguments = $CMS_TOOLS/analysis/cut_optimisation/tmva/run_track_on_grid.sh -i $sig -bg  $LEPTON_TRACK_SPLIT_DIR/single/${filename}_bg.root --no_norm  -o $dir/${filename}.root
# error = ${dir}/${filename}.err
# output = ${dir}/${filename}.output
# Queue
# EOM
# done

condor_submit $output_file
rm $output_file