#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob 

#---------- GET OPTIONS ------------
POSITIONAL=()
while [[ $# -gt 0 ]]
do
    key="$1"

    case $key in
        -skim|--skim)
        SKIM=true
        POSITIONAL+=("$1") # save it in an array for later
        shift # past argument
        ;;
        *)    # unknown option
        POSITIONAL+=("$1") # save it in an array for later
        shift # past argument
        ;;
    esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters
#---------- END OPTIONS ------------

SCRIPT_PATH=$ANALYZER_PATH
if [ -n "$SKIM" ]; then
    SCRIPT_PATH=$SKIMMER_PATH
    OUTPUT_DIR=$SKIM_OUTPUT_DIR
fi

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

files=()
for type in ${BG_TYPES[@]}; do 
    echo "Checking type $type"
    if [ "$type" = "DYJetsToLL" ]; then
        files=("${files[@]}" ${BG_NTUPLES}/Summer16.${type}_M-50_*)
        files=("${files[@]}" ${BG_NTUPLES}/RunIISummer16MiniAODv3.DYJetsToLL_M-5to50*)
    elif [ "$type" = "ZJetsToNuNu" ]; then
        files=("${files[@]}" ${BG_NTUPLES}/Summer16.${type}_HT*)
    elif [ "$type" = "TTJets" ]; then
        files=("${files[@]}" ${BG_NTUPLES}/Summer16.${type}_TuneCUETP8M1*)
    else
        files=("${files[@]}" ${BG_NTUPLES}/Summer16.${type}_*)
    fi
done

# madHtFilesGt600=()
# madHtFilesLt600=()
# for type in ${MAD_HT_SPLIT_TYPES[@]}; do 
#     madHtFilesGt600=("${madHtFilesGt600[@]}" ${BG_NTUPLES}/Summer16*${type}*_HT-*)
#     madHtFilesLt600=("${madHtFilesLt600[@]}" ${BG_NTUPLES}/Summer16*${type}_TuneCUETP8M1*)
# done

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
        echo $BG_SCRIPTS/run_bg_analysis_single.sh -i \"$input_files\" ${POSITIONAL[@]}
cat << EOM >> $output_file
arguments = $BG_SCRIPTS/run_bg_analysis_single.sh -i \"$input_files\" ${POSITIONAL[@]}
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
    echo $BG_SCRIPTS/run_bg_analysis_single.sh -i \"$input_files\" ${POSITIONAL[@]}
cat << EOM >> $output_file
arguments = $BG_SCRIPTS/run_bg_analysis_single.sh -i \"$input_files\" ${POSITIONAL[@]}
error = $ERR_OUTPUT/$(basename $fullname .root).err
output = $STD_OUTPUT/$(basename $fullname .root).output
Queue
EOM
fi

echo SUBMITTING JOBS....

condor_submit $output_file
rm $output_file