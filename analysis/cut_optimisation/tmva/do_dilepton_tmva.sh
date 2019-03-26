#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob
shopt -s expand_aliases

timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"

#check output directory
if [ ! -d "$DILEPTON_BDT_DIR" ]; then
    mkdir $DILEPTON_BDT_DIR
else
    rm -rf $DILEPTON_BDT_DIR
    mkdir $DILEPTON_BDT_DIR
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
        input="$input $SKIM_SIG_BDT_OUTPUT_DIR/single/*$pattern*.root"
    done
    dir="$DILEPTON_BDT_DIR/${group}"
    mkdir $dir
    echo "Will run:"
    echo $CMS_TOOLS/analysis/cut_optimisation/tmva/run_dilepton_on_grid.sh -i $input -bg  $SKIM_BG_SIG_BDT_OUTPUT_DIR/${group}/single --no_norm -o $dir/${group}.root
cat << EOM >> $output_file
arguments = $CMS_TOOLS/analysis/cut_optimisation/tmva/run_dilepton_on_grid.sh -i $input -bg  $SKIM_BG_SIG_BDT_OUTPUT_DIR/${group}/single --no_norm -o $dir/${group}.root
error = ${dir}/${group}.err
output = ${dir}/${group}.output
Queue
EOM
done

condor_submit $output_file
rm $output_file