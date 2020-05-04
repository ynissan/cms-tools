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
        --tl)
        TWO_LEPTONS=true
        POSITIONAL+=("$1")
        shift
        ;;
        --sam)
        SAM=true
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

if [ -n "$TWO_LEPTONS" ]; then
    if [ -n "$SAM" ]; then
        OUTPUT_DIR=$SKIM_SAM_TWO_LEPTONS_SIG_DILEPTON_BDT_OUTPUT_DIR
        INPUT_DIR=$TWO_LEPTONS_SAM_SKIM_SIG_OUTPUT_DIR/sum
    else
        OUTPUT_DIR=$SKIM_TWO_LEPTONS_SIG_DILEPTON_BDT_OUTPUT_DIR
        INPUT_DIR=$TWO_LEPTONS_SKIM_SIG_OUTPUT_DIR/sum
    fi
    BDT_DIR=$TWO_LEPTONS_OUTPUT_WD/cut_optimisation/tmva/dilepton_bdt
else
    if [ -n "$SAM" ]; then
        OUTPUT_DIR=$SKIM_SAM_SIG_DILEPTON_BDT_OUTPUT_DIR
        INPUT_DIR=$SKIM_SAM_SIG_BDT_OUTPUT_DIR/single
    else
        OUTPUT_DIR=$SKIM_SIG_DILEPTON_BDT_OUTPUT_DIR
        INPUT_DIR=$SKIM_SIG_BDT_OUTPUT_DIR/single
    fi
    BDT_DIR=$OUTPUT_WD/cut_optimisation/tmva/dilepton_bdt
fi

if [ -n "$SC" ]; then
    echo "GOT SC"
    echo "HERE: $@"
    OUTPUT_DIR=$SKIM_SIG_DILEPTON_BDT_SC_OUTPUT_DIR
    INPUT_DIR=$SKIM_SIG_BDT_SC_OUTPUT_DIR
fi

if [ -z "$SAM" ]; then
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

if [ -z "$SAM" ]; then
    for sim in ${INPUT_DIR}/*; do
        filename=`echo $(basename $sim .root) | awk -F"_" '{print $1"_"$2"_"$3}'`
        echo $filename
        tb=$filename
        for group in "${!SIM_GROUP[@]}"; do
            if [[ $group == "all" ]]; then
                echo "Skipping ALL!!!!!"
                continue
            fi
            echo checking group $group
            value=${SIM_GROUP[$group]}
            found=false
            for pattern in $value; do
                echo checking pattern $pattern
                if [[ $filename == *"$pattern"* ]]; then
                    echo Found!
                    tb=$group
                    found=true
                    break
                fi
            done
            if [[ "$found" = "true" ]]; then
                break
            fi
        done
        cmd="$CONDOR_WRAPPER $SCRIPTS_WD/skimmer_x1x2x1_dilepton_bdt.py -i $sim -o ${OUTPUT_DIR}/single/${filename}.root -bdt $BDT_DIR/$tb $@"
        echo "Will run:"
        echo $cmd
    cat << EOM >> $output_file
arguments = $cmd
error = ${OUTPUT_DIR}/stderr/${filename}.err
output = ${OUTPUT_DIR}/stdout/${filename}.output
Queue
EOM
    done
fi
## ALL GROUP

echo -e "\n\nRUNNING ALL GROUP\n\n"

OUTPUT_DIR=${SKIM_SIG_DILEPTON_BDT_OUTPUT_DIR}_all
INPUT_DIR=${SKIM_SIG_BDT_OUTPUT_DIR}_all/single

if [ -n "$TWO_LEPTONS" ]; then
    if [ -n "$SAM" ]; then
        OUTPUT_DIR=${SKIM_SAM_TWO_LEPTONS_SIG_DILEPTON_BDT_OUTPUT_DIR}_all
        INPUT_DIR=$TWO_LEPTONS_SAM_SKIM_SIG_OUTPUT_DIR/sum
    else
        OUTPUT_DIR=${SKIM_TWO_LEPTONS_SIG_DILEPTON_BDT_OUTPUT_DIR}_all
        INPUT_DIR=$TWO_LEPTONS_SKIM_SIG_OUTPUT_DIR/sum
    fi
else
    if [ -n "$SAM" ]; then
        OUTPUT_DIR=${SKIM_SAM_SIG_DILEPTON_BDT_OUTPUT_DIR}_all
        INPUT_DIR=${SKIM_SAM_SIG_BDT_OUTPUT_DIR}_all/single
    else
        OUTPUT_DIR=${SKIM_SIG_DILEPTON_BDT_OUTPUT_DIR}_all
        INPUT_DIR=${SKIM_SIG_BDT_OUTPUT_DIR}_all/single
    fi
fi

#OUTPUT_DIR="$OUTPUT_WD/signal/skim_signal_bdt_tighter"

if [ -n "$SC" ]; then
    echo "GOT SC"
    echo "HERE: $@"
    OUTPUT_DIR=${SKIM_SIG_DILEPTON_BDT_SC_OUTPUT_DIR}_all
    INPUT_DIR=${SKIM_SIG_BDT_OUTPUT_DIR}_all/single
fi

#check output directory
if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir $OUTPUT_DIR
else
   rm -rf $OUTPUT_DIR
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

for sim in ${INPUT_DIR}/*; do
    filename=`echo $(basename $sim .root) | awk -F"_" '{print $1"_"$2"_"$3}'`
    echo $filename
    tb=all
    cmd="$CONDOR_WRAPPER $SCRIPTS_WD/skimmer_x1x2x1_dilepton_bdt.py -i $sim -o ${OUTPUT_DIR}/single/${filename}.root -bdt $BDT_DIR/$tb $@"
    echo "Will run:"
    echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = ${OUTPUT_DIR}/stderr/${filename}.err
output = ${OUTPUT_DIR}/stdout/${filename}.output
Queue
EOM
done

condor_submit $output_file
rm $output_file
