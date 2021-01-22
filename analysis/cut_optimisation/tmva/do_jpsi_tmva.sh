#!/bin/bash

. "$CMSSW_BASE/src/cms-tools/lib/def.sh"

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



if [ ! -d "$SPLIT_JPSI_MASTER_OUTPUT_DIR/tmva" ]; then
    mkdir "$SPLIT_JPSI_MASTER_OUTPUT_DIR/tmva"
else
    rm -rf "$SPLIT_JPSI_MASTER_OUTPUT_DIR/tmva"
    mkdir "$SPLIT_JPSI_MASTER_OUTPUT_DIR/tmva"
fi

for group in "1"; do
    # value=${SIM_GROUP[$group]}
#     input=""
#     background=""
#     for pattern in $value; do
#         input="$input $LEPTON_TRACK_SPLIT_DIR/single/*$pattern*_sig.root"
#         background="$background $LEPTON_TRACK_SPLIT_DIR/single/*$pattern*_bg.root"
#     done
    
    
    #dir="$LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva/${group}"
    #mkdir $dir
    cmd="$CONDOR_WRAPPER $CUT_OPTIMISATION_SCRIPTS/jpsi_tmva.py -i $SPLIT_JPSI_MASTER_OUTPUT_DIR/single/*_sig.root -bg  $SPLIT_JPSI_MASTER_OUTPUT_DIR/single/*_bg.root --no_norm -o $SPLIT_JPSI_MASTER_OUTPUT_DIR/tmva/jpsi.root"
    echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = $SPLIT_JPSI_MASTER_OUTPUT_DIR/tmva/jpsi.err
output = $SPLIT_JPSI_MASTER_OUTPUT_DIR/tmva/jpsi.output
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

#condor_submit $output_file
rm $output_file