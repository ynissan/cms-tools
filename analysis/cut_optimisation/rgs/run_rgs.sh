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
	    -i)
	    OUTPUT_DIR=`readlink -f $2`
	    POSITIONAL+=("$1") # save it in an array for later
	    POSITIONAL+=("$2") # save it in an array for later
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
if [ ! -d "$OUTPUT_DIR/single" ]; then
  mkdir "$OUTPUT_DIR/single"
fi

if [ ! -d "$OUTPUT_DIR/sstdout" ]; then
  mkdir "$OUTPUT_DIR/sstdout"
fi

if [ ! -d "$OUTPUT_DIR/sstderr" ]; then
  mkdir "$OUTPUT_DIR/sstderr"
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
arguments = $RGS_DIR/run_on_grid.sh -s $SKIM_SIG_OUTPUT_DIR/sum/type_sum/total.root -i $OUTPUT_DIR -c /afs/desy.de/user/n/nissanuv/work/x1x2x1/bg_sig.root
error = ${OUTPUT_DIR}/sstderr/signal.err
output = ${OUTPUT_DIR}/sstdout/signal.output
Queue
EOM

for bg_file in ${SKIM_OUTPUT_DIR}/sum/type_sum/*; do
	filename=$(basename $bg_file .root)
	echo "Will run:"
	echo $RGS_DIR/run_on_grid.sh -i $OUTPUT_DIR -c /afs/desy.de/user/n/nissanuv/work/x1x2x1/bg_sig.root -f $bg_file
cat << EOM >> $output_file
arguments = $RGS_DIR/run_on_grid.sh -i $OUTPUT_DIR -c /afs/desy.de/user/n/nissanuv/work/x1x2x1/bg_sig.root -f $bg_file
error = ${OUTPUT_DIR}/sstderr/${filename}.err
output = ${OUTPUT_DIR}/sstdout/${filename}.output
Queue
EOM
done

condor_submit $output_file
rm $output_file


