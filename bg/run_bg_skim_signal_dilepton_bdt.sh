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
        -dy)
        DRELL_YAN=true
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

if [ -n "$DRELL_YAN" ]; then
    echo "GOT DY"
    echo "HERE: $@"
    INPUT_DIR=$SKIM_DY_BG_SIG_BDT_OUTPUT_DIR
else
    if [ -n "$SC" ]; then
        echo "GOT SC"
        echo "HERE: $@"
        INPUT_DIR=$SKIM_BG_SIG_BDT_SC_OUTPUT_DIR
    else
        INPUT_DIR=$SKIM_OUTPUT_DIR
    fi
fi

BDT_DIR=$OUTPUT_WD/cut_optimisation/tmva/dilepton_bdt

echo INPUT_DIR=$INPUT_DIR
echo BDT_DIR=$BDT_DIR

timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"

cat << EOM > $output_file
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
EOM

for bg_file in $INPUT_DIR/sum/type_sum/*; do
    cmd="$CONDOR_WRAPPER $SCRIPTS_WD/skimmer_x1x2x1_dilepton_bdt.py -i $bg_file -bdt $BDT_DIR -bg $@"
    echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = ${INPUT_DIR}/stderr/${bg_file_name}_dilepton.err
output = ${INPUT_DIR}/stdoutput/${bg_file_name}_dilepton.output
Queue
EOM
    
done

condor_submit $output_file
rm $output_file
