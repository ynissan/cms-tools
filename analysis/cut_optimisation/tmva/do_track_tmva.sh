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

for sig in $LEPTON_TRACK_SPLIT_DIR/*_sig.root; do
	filename=$(basename $sig _sig.root)
	dir = $LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva/${filename}
	mkdir $dir
	echo "Will run:"
	echo $CMS_TOOLS/analysis/cut_optimisation/tmva/run_track_on_grid.sh -i $sig -bg  $LEPTON_TRACK_SPLIT_DIR/${filename}_bg.root --no_norm --all -o $dir/${filename}.root
cat << EOM >> $output_file
arguments = $CMS_TOOLS/analysis/cut_optimisation/tmva/run_track_on_grid.sh -i $sig -bg  $LEPTON_TRACK_SPLIT_DIR/${filename}_bg.root --no_norm --all -o $dir/${filename}.root
error = ${dir}/${filename}.err
output = ${dir}/${filename}.output
Queue
EOM
done

condor_submit $output_file
rm $output_file