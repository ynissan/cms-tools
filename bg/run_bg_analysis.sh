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
	if [ "$type" = "DYJetsToLL" ]; then
		files=("${files[@]}" ${NEWEST_SIM_DIR}/Summer16.${type}_M-50_HT-*)
	else
		files=("${files[@]}" ${NEWEST_SIM_DIR}/Summer16.${type}_*)
	fi
done

madHtFilesGt600=()
madHtFilesLt600=()
for type in ${MAD_HT_SPLIT_TYPES[@]}; do 
	madHtFilesGt600=("${madHtFilesGt600[@]}" ${NEWEST_SIM_DIR}/Summer16*${type}*_HT-*)
	madHtFilesLt600=("${madHtFilesLt600[@]}" ${NEWEST_SIM_DIR}/Summer16*${type}_TuneCUETP8M1*)
done

file_limit=0
i=0
count=0

for fullname in "${files[@]}"; do
	#cmd="qsub -cwd -l h_vmem=2G -o $STD_OUTPUT/$(basename $fullname .root).output  -e $ERR_OUTPUT/$(basename $fullname .root).err $SCRIPTS_WD/run_bg_analysis_single.sh -i $fullname &"
	#cmd="condor_qsub -o $STD_OUTPUT/$(basename $fullname .root).output  -e $ERR_OUTPUT/$(basename $fullname .root).err $SCRIPTS_WD/run_bg_analysis_single.sh -i $fullname &"
read -r -d '' CMD << EOM
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
arguments = $SCRIPTS_WD/run_bg_analysis_single.sh -i $fullname ${POSITIONAL[@]}
error = $ERR_OUTPUT/$(basename $fullname .root).err
output = $STD_OUTPUT/$(basename $fullname .root).output
notification = Never
priority = 0
Queue
EOM
    	echo -e "\nRunning cmd:\n$SCRIPTS_WD/run_bg_analysis_single.sh -i $fullname ${POSITIONAL[@]}"
    	#echo $fullname
    	echo "$CMD" | condor_submit &
	if [ $file_limit -gt 0 ]; then
		#check limit
		((i+=1)) 
		if [ $i -ge $file_limit ]; then
			break
		fi
	fi
	((count+=1))
	if ! ((count % 200)); then
		sleep 2
	fi
done

for fullname in "${madHtFilesGt600[@]}"; do

read -r -d '' CMD << EOM
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
arguments = $SCRIPTS_WD/run_bg_analysis_single.sh --madHTgt 600 -i $fullname ${POSITIONAL[@]}
error = $ERR_OUTPUT/$(basename $fullname .root).err
output = $STD_OUTPUT/$(basename $fullname .root).output
notification = Never
priority = 0
Queue
EOM

    	echo -e "\nRunning cmd:\n$SCRIPTS_WD/run_bg_analysis_single.sh --madHTgt 600 -i $fullname ${POSITIONAL[@]}"
    	#echo $fullname
    	echo "$CMD" | condor_submit &
    	if [ $file_limit -gt 0 ]; then
		#check limit
		((i+=1)) 
		if [ $i -ge $file_limit ]; then
			break
		fi
	fi
	((count+=1))
	if ! ((count % 200)); then
		sleep 2
	fi
done

for fullname in "${madHtFilesLt600[@]}"; do

read -r -d '' CMD << EOM
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
arguments = $SCRIPTS_WD/run_bg_analysis_single.sh --madHTlt 600 -i $fullname ${POSITIONAL[@]}
error = $ERR_OUTPUT/$(basename $fullname .root).err
output = $STD_OUTPUT/$(basename $fullname .root).output
notification = Never
priority = 0
Queue
EOM

    	echo -e "\nRunning cmd:\n$SCRIPTS_WD/run_bg_analysis_single.sh --madHTlt 600 -i $fullname ${POSITIONAL[@]}"
    	#echo $fullname
    	echo "$CMD" | condor_submit &
    	if [ $file_limit -gt 0 ]; then
		#check limit
		((i+=1)) 
		if [ $i -ge $file_limit ]; then
			break
		fi
	fi
	((count+=1))
	if ! ((count % 200)); then
		sleep 2
	fi
done