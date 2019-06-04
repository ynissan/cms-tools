#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob
shopt -s expand_aliases

# CMS ENV
cd $CMS_WD
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

OUTPUT_DIR=$SKIM_DATA_OUTPUT_DIR

#check output directory
if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir $OUTPUT_DIR
fi

#check output directory
if [ ! -d "$OUTPUT_DIR/single" ]; then
  mkdir "$OUTPUT_DIR/single"
fi

if [ ! -d "$OUTPUT_DIR/stdout" ]; then
  mkdir "$OUTPUT_DIR/stdout"
fi

if [ ! -d "$OUTPUT_DIR/stderr" ]; then
  mkdir "$OUTPUT_DIR/stderr"
fi

timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"

cat << EOM > $output_file
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
priority = 0
EOM

#for sim in ${SIG_DUP_OUTPUT_DIR}/single/*; do
for sim in ${DATA_NTUPLES_DIR}/Run2016B*METAOD*; do
    filename=$(basename $sim .root)
    echo "Will run:"
    echo $DATA_DIR/run_skim_data_analysis_single.sh -i $sim -o ${OUTPUT_DIR}/single/${filename}.root --data ${POSITIONAL[@]}
cat << EOM >> $output_file
arguments = $DATA_DIR/run_skim_data_analysis_single.sh -i $sim -o ${OUTPUT_DIR}/single/${filename}.root --data ${POSITIONAL[@]}
error = ${OUTPUT_DIR}/stderr/${filename}.err
output = ${OUTPUT_DIR}/stdout/${filename}.output
Queue
EOM
done

condor_submit $output_file
rm $output_file
