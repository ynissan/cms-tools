#!/bin/bash

. "$CMSSW_BASE/src/stops/lib/def.sh"

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
EOM

if [ ! -d condor_output ] ; then
    mkdir condor_output
fi

for file in $1/*; do
    if [ ! -f $file ]; then
        echo "Skipping $file..."
        continue
    fi
    cmd="$CONDOR_WRAPPER $SCRIPTS_WD/skimmer_x1x2x1_create_jet_iso.py -i $file"
    echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = ${PWD}/condor_output/$(basename $file .root).err
output = ${PWD}/condor_output/$(basename $file .root).output
Queue
EOM
done

condor_submit $output_file
#echo $output_file
rm $output_file
