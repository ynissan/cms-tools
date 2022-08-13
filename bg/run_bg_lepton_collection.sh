#!/bin/bash

. "$CMSSW_BASE/src/cms-tools/lib/def.sh"

shopt -s nullglob 

SCRIPT_PATH=$LC_SCRIPT_PATH
OUTPUT_DIR=$LC_OUTPUT_DIR

STD_OUTPUT="${OUTPUT_DIR}/stdoutput"
ERR_OUTPUT="${OUTPUT_DIR}/stderr"
FILE_OUTPUT="${OUTPUT_DIR}/single"

echo "std output: $STD_OUTPUT"
echo "err output: $ERR_OUTPUT"
echo "file output: $FILE_OUTPUT"

#check output directory
if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir $OUTPUT_DIR
fi

#check output directory
if [ ! -d "$STD_OUTPUT" ]; then
  mkdir $STD_OUTPUT
fi

if [ ! -d "$FILE_OUTPUT" ]; then
  mkdir $FILE_OUTPUT
fi

if [ ! -d "$ERR_OUTPUT" ]; then
  mkdir $ERR_OUTPUT
fi

LC_INTPUT="/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/LeptonCollection/"

files=()

timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"

cat << EOM > $output_file
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
priority = 0
request_memory = 16 GB
EOM

PREFIX="Summer16"
PREFIX="Fall17"

for type in ${BG_TYPES_17[@]}; do 
    echo "Checking type $type"
    if [ "$type" = "DYJetsToLL" ]; then
        files=("${files[@]}" ${LC_INTPUT}/${PREFIX}*.${type}_M-50_*)
        files=("${files[@]}" ${LC_INTPUT}/${PREFIX}*.DYJetsToLL_M-5to50*)
    elif [ "$type" = "ZJetsToNuNu" ]; then
        files=("${files[@]}" ${LC_INTPUT}/${PREFIX}*.${type}_HT*)
    elif [ "$type" = "TTJets" ]; then
        files=("${files[@]}" ${LC_INTPUT}/${PREFIX}*.${type}_TuneCUETP8M1*)
    else
        files=("${files[@]}" ${LC_INTPUT}/${PREFIX}*.${type}_*)
    fi
done

# madHtFilesGt600=()
# madHtFilesLt600=()
# for type in ${MAD_HT_SPLIT_TYPES[@]}; do 
#     madHtFilesGt600=("${madHtFilesGt600[@]}" ${BG_NTUPLES}/Summer16*${type}*_HT-*)
#     madHtFilesLt600=("${madHtFilesLt600[@]}" ${BG_NTUPLES}/Summer16*${type}_TuneCUETP8M1*)
# done



file_limit=0
i=0
count=0
input_files=""
files_per_job=1
index=0
name=""

for fullname in "${files[@]}"; do
    name=$(basename $fullname)
    #echo "Checking $FILE_OUTPUT/$name"
    skip=0
    for ef in ${FILE_EXCLUDE_LIST[@]}; do
        if [[ $name == *"$ef"* ]]; then
            #echo "Skipping file $name"
            skip=1
        fi
    done
    
    if [[ $skip == 1 ]]; then
        #echo "Really skipping"
        continue
    fi
    
    if [ -f "$FILE_OUTPUT/$name" ]; then
        #echo "$name exist. Skipping..."
        continue
    fi
    input_files="$input_files $fullname"
    ((count+=1))
    if [ $(($count % $files_per_job)) == 0 ]; then
        ((index+=1)) 
        echo $CONDOR_WRAPPER $LC_SCRIPT_PATH -i $input_files -o ${FILE_OUTPUT}
cat << EOM >> $output_file
arguments = $CONDOR_WRAPPER $LC_SCRIPT_PATH -i $input_files -o ${FILE_OUTPUT}
error = $ERR_OUTPUT/$(basename $fullname .root).err
output = $STD_OUTPUT/$(basename $fullname .root).output
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
    echo $CONDOR_WRAPPER $LC_SCRIPT_PATH  -i $input_files -o ${FILE_OUTPUT}
cat << EOM >> $output_file
arguments = $CONDOR_WRAPPER $LC_SCRIPT_PATH  -i $input_files -o ${FILE_OUTPUT}
error = $ERR_OUTPUT/$(basename $fullname .root).err
output = $STD_OUTPUT/$(basename $fullname .root).output
Queue
EOM
fi

echo SUBMITTING JOBS....

condor_submit $output_file
rm $output_file