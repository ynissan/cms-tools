#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob
shopt -s expand_aliases

timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"

cat << EOM > $output_file
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
priority = 0
+RequestRuntime = 86400
EOM

if [ ! -d "$LEPTON_TRACK_SPLIT_DIR/cut_optimisation" ]; then
    mkdir "$LEPTON_TRACK_SPLIT_DIR/cut_optimisation"
fi

if [ ! -d "$LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva" ]; then
    mkdir "$LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva"
else
    #rm -rf "$LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva"
    mkdir "$LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva"
fi

for group in "${!SIM_GROUP[@]}"; do
    value=${SIM_GROUP[$group]}
    input=""
    background=""
    for pattern in $value; do
        input="$input $LEPTON_TRACK_SPLIT_DIR/single/*$pattern*_sig.root"
        background="$background $LEPTON_TRACK_SPLIT_DIR/single/*$pattern*_bg.root"
    done
    dir="$LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva/${group}"
    mkdir $dir
    echo $CMS_TOOLS/analysis/cut_optimisation/tmva/run_track_on_grid.sh -i $input -bg  $background --no_norm -o $dir/${group}.root
cat << EOM >> $output_file
arguments = $CMS_TOOLS/analysis/cut_optimisation/tmva/run_track_on_grid.sh -i $input -bg  $background --no_norm -o $dir/${group}.root
error = ${dir}/${group}.err
output = ${dir}/${group}.output
Queue
EOM
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