#!/bin/bash

. "$CMSSW_BASE/src/cms-tools/lib/def.sh"

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
         --sc)
        SAME_SIGN=true
        POSITIONAL+=("$1")
        shift
        ;;
        --tl)
        TWO_LEPTONS=true
        POSITIONAL+=("$1")
        shift
        ;;
        --jpsi_muons)
        JPSI_MUONS=true
        POSITIONAL+=("$1")
        shift
        ;;
        --dy)
        DY=true
        POSITIONAL+=("$1")
        shift
        ;;
        -nlp)
        NLP=true
        POSITIONAL+=("$1")
        shift
        ;;
        --master)
        MASTER=true
        POSITIONAL+=("$1")
        shift
        ;;
        --jpsi_single_electron)
        JPSI_SINGLE_ELECTRON=true
        POSITIONAL+=("$1")
        shift
        ;;
        --z_peak)
        Z_PEAK=true
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

SCRIPT_PATH=$ANALYZER_PATH
if [ -n "$SKIM" ]; then
    SCRIPT_PATH=$SKIMMER_PATH
    if [ -n "$MASTER" ]; then
        SCRIPT_PATH=$JPSI_SKIMMER_PATH
        OUTPUT_DIR=$SKIM_MASTER_OUTPUT_DIR
    elif [ -n "$Z_PEAK" ]; then
        SCRIPT_PATH=$JPSI_SKIMMER_PATH
        OUTPUT_DIR=$SKIM_Z_PEAK_OUTPUT_DIR
    elif [ -n "JPSI_SINGLE_ELECTRON" ]; then
        SCRIPT_PATH=$JPSI_SKIMMER_PATH
        OUTPUT_DIR=$SKIM_JPSI_SINGLE_ELECTRON_OUTPUT_DIR
    elif [ -n "$TWO_LEPTONS" ]; then
        if [ -n "$SAME_SIGN" ]; then
            OUTPUT_DIR=$TWO_LEPTONS_SAME_SIGN_SKIM_OUTPUT_DIR
        else
            OUTPUT_DIR=$TWO_LEPTONS_SKIM_OUTPUT_DIR
        fi
    elif [ -n "$DY" ]; then
        OUTPUT_DIR=$DY_SKIM_OUTPUT_DIR
    elif [ -n "$JPSI_MUONS" ]; then
        OUTPUT_DIR=$JPSI_MUONS_SKIM_OUTPUT_DIR
    else
        OUTPUT_DIR=$SKIM_OUTPUT_DIR
    fi
    if [ -n "$NLP" ]; then
        OUTPUT_DIR=$NLP_SKIM_OUTPUT_DIR
    fi
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



madHtFilesGt600=()
madHtFilesLt600=()
for type in ${MAD_HT_SPLIT_TYPES[@]}; do 
    madHtFilesGt600=("${madHtFilesGt600[@]}" ${BG_NTUPLES}/Summer16*${type}*_HT-*)
    madHtFilesLt600=("${madHtFilesLt600[@]}" ${BG_NTUPLES}/Summer16*${type}_TuneCUETP8M1*)
done

# echo ${MAD_HT_SPLIT_TYPES[@]}
# echo ${madHtFilesGt600[@]}
# echo ${madHtFilesLt600[@]}
# exit

#files=()

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
files_per_job=8

for type in reg madHtFilesGt600 madHtFilesLt600; do

    i=0
    count=0
    input_files=""
    
    echo "In loop running $type"
    
    extra_params=""
    list="${files[@]}"
    
    if [ "$type" = "madHtFilesGt600" ]; then
        echo "Running now type madHtFilesGt600"
        extra_params="-madHTgt 600"
        list="${madHtFilesGt600[@]}"
    elif [ "$type" = "madHtFilesLt600" ]; then
        echo "Running now type madHtFilesLt600"
        extra_params="-madHTlt 600"
        list="${madHtFilesLt600[@]}"
    fi
    
    echo "extra_params $extra_params"
    #echo $list
    
    for fullname in $list; do
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
            echo "$name exist. Skipping..."
            continue
        fi
        input_files="$input_files $fullname"
        ((count+=1))
        if [ $(($count % $files_per_job)) == 0 ]; then
            cmd="$BG_SCRIPTS/run_bg_analysis_single.sh -i \"$input_files\" $extra_params ${POSITIONAL[@]}"
            echo $cmd
cat << EOM >> $output_file
arguments = $BG_SCRIPTS/run_bg_analysis_single.sh -i \"$input_files\" $extra_params ${POSITIONAL[@]}
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
        cmd="$BG_SCRIPTS/run_bg_analysis_single.sh -i \"$input_files\" $extra_params ${POSITIONAL[@]}"
        echo $cmd
cat << EOM >> $output_file
arguments = $BG_SCRIPTS/run_bg_analysis_single.sh -i \"$input_files\" $extra_params ${POSITIONAL[@]}
error = $ERR_OUTPUT/$(basename $fullname .root).err
output = $STD_OUTPUT/$(basename $fullname .root).output
Queue
EOM
    fi
done

echo SUBMITTING JOBS....

condor_submit $output_file
rm $output_file