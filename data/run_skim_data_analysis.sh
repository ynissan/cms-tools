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

file_limit=0
i=0
count=0
input_files=""
files_per_job=20

OUTPUT_DIR=$SKIM_DATA_OUTPUT_DIR
FILE_OUTPUT="${OUTPUT_DIR}/single"

#for fullname in ${DATA_NTUPLES_DIR}/Run2016*SingleMuon*; do
for fullname in ${DATA_NTUPLES_DIR}/Run2016*METAOD*; do
    name=$(basename $fullname)
    if [ -f "$FILE_OUTPUT/$name" ]; then
        #echo "$name exist. Skipping..."
        continue
    fi
    input_files="$input_files $fullname"
    ((count+=1))
    if [ $(($count % $files_per_job)) == 0 ]; then
        echo $DATA_DIR/run_skim_data_analysis_single.sh -i \"$input_files\" --data ${POSITIONAL[@]}
cat << EOM >> $output_file
arguments = $DATA_DIR/run_skim_data_analysis_single.sh -i \"$input_files\" --data ${POSITIONAL[@]}
error = ${OUTPUT_DIR}/stderr/$(basename $fullname .root).err
output = ${OUTPUT_DIR}/stdout/$(basename $fullname .root).output
Queue
EOM
    input_files=""
    fi
    
    if [ $file_limit -gt 0 ]; then
        #check limit
        ((i+=1)) 
        if [ $i -ge $file_limit ]; then
            break
        fi
    fi
done

if [ $(($count % $files_per_job)) != 0 ]; then
    echo $DATA_DIR/run_skim_data_analysis_single.sh -i \"$input_files\" --data ${POSITIONAL[@]}
cat << EOM >> $output_file
arguments = $DATA_DIR/run_skim_data_analysis_single.sh -i \"$input_files\" --data ${POSITIONAL[@]}
error = ${OUTPUT_DIR}/stderr/$(basename $fullname .root).err
output = ${OUTPUT_DIR}/stdout/$(basename $fullname .root).output
Queue
EOM
fi


#for sim in ${SIG_DUP_OUTPUT_DIR}/single/*; do
# for sim in ${DATA_NTUPLES_DIR}/Run2016*METAOD*; do
#     filename=$(basename $sim .root)
#     echo "Will run:"
#     echo $DATA_DIR/run_skim_data_analysis_single.sh -i $sim -o ${OUTPUT_DIR}/single/${filename}.root --data ${POSITIONAL[@]}
# cat << EOM >> $output_file
# arguments = $DATA_DIR/run_skim_data_analysis_single.sh -i $sim -o ${OUTPUT_DIR}/single/${filename}.root --data ${POSITIONAL[@]}
# error = ${OUTPUT_DIR}/stderr/${filename}.err
# output = ${OUTPUT_DIR}/stdout/${filename}.output
# Queue
# EOM
# done

condor_submit $output_file
#echo $output_file
rm $output_file
