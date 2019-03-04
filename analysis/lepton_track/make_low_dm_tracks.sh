#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

OUTPUT_DIR="$LEPTON_TRACK_SPLIT_DIR/single"

if [ ! -d "$OUTPUT_DIR/low" ]; then
    mkdir "$OUTPUT_DIR/low"
fi

echo "Will run:"
cmd="hadd -f $OUTPUT_DIR/higgsino_low_dm_sig.root $OUTPUT_DIR/*dm4p*_sig.root $OUTPUT_DIR/*dm3p*_sig.root $OUTPUT_DIR/*dm2p*_sig.root"
echo $cmd

$cmd

echo "Will run:"
cmd="hadd -f $OUTPUT_DIR/higgsino_low_dm_bg.root $OUTPUT_DIR/*dm4p*_bg.root $OUTPUT_DIR/*dm3p*_bg.root $OUTPUT_DIR/*dm2p*_bg.root"
echo $cmd

$cmd

echo "Will run:"
cmd="mv $OUTPUT_DIR/*dm4p*_sig.root $OUTPUT_DIR/*dm3p*_sig.root $OUTPUT_DIR/*dm2p*_sig.root $OUTPUT_DIR/low/"
echo $cmd

$cmd

echo "Will run:"
cmd="mv $OUTPUT_DIR/*dm4p*_bg.root $OUTPUT_DIR/*dm3p*_bg.root $OUTPUT_DIR/*dm2p*_bg.root $OUTPUT_DIR/low/"
echo $cmd

$cmd