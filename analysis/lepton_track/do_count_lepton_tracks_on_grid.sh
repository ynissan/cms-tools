#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob
shopt -s expand_aliases

#---------- GET OPTIONS ------------
POSITIONAL=()
while [[ $# -gt 0 ]]
do
	key="$1"

	case $key in
	    -o)
	    OUTPUT_DIR=`readlink -f $2`
	    shift # past argument
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

if [ -z "$OUTPUT_DIR" ]; then
	echo "Must provide output dir."
	exit 0
fi

#check output directory
if [ ! -d "$OUTPUT_DIR" ]; then
	echo "Must provide output dir."
	exit 0
fi

#check output directory

if [ ! -d "$OUTPUT_DIR/stdout" ]; then
  mkdir "$OUTPUT_DIR/stdout"
fi

if [ ! -d "$OUTPUT_DIR/stderr" ]; then
  mkdir "$OUTPUT_DIR/stderr"
fi

echo "output dir:" $OUTPUT_DIR

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

for f in /afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/single/*; do
	filename=$(basename $f .root)
	echo "Will run:"
	echo $LEPTON_TRACK_DIR/count_lepton_tracks_single.sh -i $f -o  $OUTPUT_DIR/${filename}.pdf $@
cat << EOM >> $output_file
arguments = $LEPTON_TRACK_DIR/count_lepton_tracks_single.sh -i $f -o  $OUTPUT_DIR/${filename}.pdf $@
error = ${OUTPUT_DIR}/stderr/${filename}.err
output = ${OUTPUT_DIR}/stdout/${filename}.output
Queue
EOM
done

condor_submit $output_file
rm $output_file


