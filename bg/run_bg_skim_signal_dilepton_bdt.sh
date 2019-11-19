#!/bin/bash

. "$CMSSW_BASE/src/cms-tools/lib/def.sh"

shopt -s nullglob
shopt -s expand_aliases

#---------- GET OPTIONS ------------
POSITIONAL=()
while [[ $# -gt 0 ]]
do
    key="$1"

    case $key in
        -sc)
        SC=true
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

# CMS ENV
cd $CMS_WD
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

OUTPUT_DIR=$SKIM_BG_SIG_DILEPTON_BDT_OUTPUT_DIR
INPUT_DIR=$SKIM_BG_SIG_BDT_OUTPUT_DIR

if [ -n "$SC" ]; then
    echo "GOT SC"
    echo "HERE: $@"
    OUTPUT_DIR=$SKIM_BG_SIG_DILEPTON_BDT_SC_OUTPUT_DIR
    INPUT_DIR=$SKIM_BG_SIG_BDT_SC_OUTPUT_DIR
fi

timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"

echo $OUTPUT_DIR
#check output directory
if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir $OUTPUT_DIR
else
   #rm -rf $OUTPUT_DIR
   mkdir $OUTPUT_DIR
fi

cat << EOM > $output_file
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
priority = 0
EOM

for sim in $INPUT_DIR/*; do
#for sim in /afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_signal_bdt/single/*; do    
    filename=`echo $(basename $sim )`
    echo $filename
    echo here
    tb=$filename

    if [ ! -d "$OUTPUT_DIR/$tb" ]; then
      mkdir $OUTPUT_DIR/$tb
    fi

    #check output directory
    if [ ! -d "$OUTPUT_DIR/$tb/single" ]; then
      mkdir "$OUTPUT_DIR/$tb/single"
    fi

    if [ ! -d "$OUTPUT_DIR/$tb/stdout" ]; then
      mkdir "$OUTPUT_DIR/$tb/stdout" 
    fi

    if [ ! -d "$OUTPUT_DIR/$tb/stderr" ]; then
      mkdir "$OUTPUT_DIR/$tb/stderr"
    fi

    for bg_file in $INPUT_DIR/$tb/single/*; do
    #for bg_file in $SKIM_BG_SIG_BDT_OUTPUT_DIR/$tb/single/WW_TuneCUETP8M1*; do
        echo "Will run:"
        echo "error=${OUTPUT_DIR}/$tb/stderr/${bg_file_name}.err" 
        bg_file_name=$(basename $bg_file .root)
        echo $CONDOR_WRAPPER $SCRIPTS_WD/skimmer_x1x2x1_dilepton_bdt.py -i $bg_file -o ${OUTPUT_DIR}/$tb/single/${bg_file_name}.root -bdt $OUTPUT_WD/cut_optimisation/tmva/dilepton_bdt/$tb 
cat << EOM >> $output_file
arguments = $CONDOR_WRAPPER $SCRIPTS_WD/skimmer_x1x2x1_dilepton_bdt.py -i $bg_file -o ${OUTPUT_DIR}/$tb/single/${bg_file_name}.root -bdt $OUTPUT_WD/cut_optimisation/tmva/dilepton_bdt/$tb 
error = ${OUTPUT_DIR}/$tb/stderr/${bg_file_name}.err
output = ${OUTPUT_DIR}/$tb/stdout/${bg_file_name}.output
Queue
EOM
    done
done

condor_submit $output_file
rm $output_file
