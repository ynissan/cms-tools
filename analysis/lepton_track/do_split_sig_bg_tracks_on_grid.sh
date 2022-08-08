#!/bin/bash

. "$CMSSW_BASE/src/cms-tools/lib/def.sh"

#---------- GET OPTIONS ------------
POSITIONAL=()
while [[ $# -gt 0 ]]
do
    key="$1"

    case $key in
        --jpsi)
        JPSI=true
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

INPUT_DIR=$SKIM_SIG_OUTPUT_DIR/sum
OUTPUT_DIR=$LEPTON_TRACK_SPLIT_DIR
COMMAND=$LEPTON_TRACK_DIR/split_sig_bg_tracks.py

if [ -n "$JPSI" ]; then
    INPUT_DIR=$SKIM_MASTER_OUTPUT_DIR/sum/type_sum
    OUTPUT_DIR=$SPLIT_JPSI_MASTER_OUTPUT_DIR
    COMMAND=$LEPTON_TRACK_DIR/split_jpsi_events.py
fi

echo "output dir:" $OUTPUT_DIR

#check output directory

if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir "$OUTPUT_DIR"
fi

if [ ! -d "$OUTPUT_DIR/stdout" ]; then
  mkdir "$OUTPUT_DIR/stdout"
fi

if [ ! -d "$OUTPUT_DIR/stderr" ]; then
  mkdir "$OUTPUT_DIR/stderr"
fi

if [ ! -d "$OUTPUT_DIR/single" ]; then
  mkdir "$OUTPUT_DIR/single"
fi

timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"

cat << EOM > $output_file
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
request_memory = 16 GB
EOM

for f in $INPUT_DIR/*; do
    filename=$(basename $f .root)
    if [[ $filename == *"dm13p"* || $filename == *"dm12p"* || $filename == *"dm9p"* || $filename == *"dm7p"* || $filename == *"dm5p"* ]]; then
        echo $filename contains large dm... Skipping...
        continue
    fi
    if [ -f $OUTPUT_DIR/single/${filename}_sig.root ] && [ -f $OUTPUT_DIR/single/${filename}_bg.root ]; then
        echo "$name exist. Skipping..."
        continue
    fi
    echo "Will run:"
    cmd="$CONDOR_WRAPPER $COMMAND -i $f -o  $OUTPUT_DIR/single/${filename}"
    echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = ${OUTPUT_DIR}/stderr/${filename}.err
output = ${OUTPUT_DIR}/stdout/${filename}.output
Queue
EOM
done

condor_submit $output_file
rm $output_file


