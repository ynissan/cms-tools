#!/bin/bash

. "$CMSSW_BASE/src/stops/lib/def.sh"

shopt -s nullglob
shopt -s expand_aliases

#---------- GET OPTIONS ------------
POSITIONAL=()
while [[ $# -gt 0 ]]
do
    key="$1"
    case $key in
        --tl)
        TWO_LEPTONS=true
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


timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"


# if [ -n "$TWO_LEPTONS" ]; then
#     OUTPUT_DIR=$DILEPTON_TWO_LEPTONS_BDT_DIR
#     INPUT_SIG_DIR=$TWO_LEPTONS_SKIM_SIG_OUTPUT_DIR/sum
#     BG_INPUT=$TWO_LEPTONS_SKIM_OUTPUT_DIR/sum/type_sum
# else
#     OUTPUT_DIR=$DILEPTON_BDT_DIR
#     INPUT_SIG_DIR=$SKIM_SIG_BDT_OUTPUT_DIR
#     BG_INPUT=$SKIM_BG_SIG_BDT_OUTPUT_DIR
# fi

INPUT_DIR=$SKIM_SIG_OUTPUT_DIR/single
OUTPUT_DIR=$DILEPTON_BDT_DIR
BG_INPUT=$SKIM_OUTPUT_DIR/sum/type_sum

echo INPUT_DIR=$SKIM_SIG_OUTPUT_DIR/single
echo OUTPUT_DIR=$DILEPTON_BDT_DIR
echo BG_INPUT=$SKIM_OUTPUT_DIR/sum/type_sum

#check output directory
if [ ! -d "$OUTPUT_DIR" ]; then
    mkdir $OUTPUT_DIR
fi

#priority = 0
#+RequestRuntime = 86400
#request_memory = 16 GB

cat << EOM > $output_file
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
+RequestRuntime = 86400
EOM

for group in "${!SIM_GROUP[@]}"; do
    # if [[ -z "$TWO_LEPTONS" && $group == "all" ]]; then
#         echo "Skipping ALL!!!!!"
#         continue
#     fi
    
    # if [[ $group != "all" ]]; then
#         continue
#     fi
    
    value=${SIM_GROUP[$group]}
    #echo value=$value
    input=""
    background=""
    for pattern in $value; do
        
        # if [ -n "$TWO_LEPTONS" ]; then
#             input="$input $INPUT_SIG_DIR/*$pattern*.root"
#         else
#             input="$input $INPUT_SIG_DIR/single/*$pattern*.root"
#         fi
        #echo input=$input
        input="$input $INPUT_DIR/*$pattern*.root"
    done
    for lepNum in exTrack reco; do
        for lep in Muons Electrons; do
            for iso in "${LEPTON_ISOLATION_LIST[@]}"; do
                for category in "${LEPTON_ISOLATION_CATEGORIES[@]}"; do
                    ptRanges=("")
                    drCuts=("")
                    #ptRanges[0]=""
                    if [[ $iso == "CorrJetIso" || $iso == "CorrJetNoMultIso" ]]; then
                        ptRanges=("${LEPTON_CORR_JET_ISO_RANGE[@]}")
                        drCuts=("${LEPTON_CORR_JET_ISO_DR_CUTS[@]}")
                    fi
                    for ptRange in "${ptRanges[@]}"; do
                        for drCut in  "${drCuts[@]}"; do
                            cuts=$ptRange
                            if [ ! -z "$ptRange" ]; then
                                cuts=${ptRange}Dr${drCut}
                            fi
                            
                            echo ${lepNum}${lep}${iso}${category}${cuts}
                            dir="$OUTPUT_DIR/${lepNum}${lep}${iso}${category}${cuts}"
                            if [ ! -d $dir ]; then
                                mkdir $dir
                            fi
                            cmd="$CONDOR_WRAPPER $CUT_OPTIMISATION_SCRIPTS/dilepton_tmva.py -i $input -bg $BG_INPUT -o $dir/${lepNum}${lep}${iso}${category}${cuts}.root -lepNum $lepNum -lep $lep -iso $iso -ptRange $cuts -cat $category"
                            #echo "$dir/dataset/weights/TMVAClassification_${lepNum}${lep}${iso}${category}${ptRange}.xml"
                            #exit 0
                            if [ -f "$dir/dataset/weights/TMVAClassification_${lepNum}${lep}${iso}${category}${cuts}.weights.xml" ]; then 
                                echo "file $dir/dataset/weights/TMVAClassification_${lepNum}${lep}${iso}${category}${cuts}.weights.xml exists. Skipping..."
                                continue
                            fi
                            echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = ${dir}/${lepNum}${lep}${iso}${category}${cuts}.err
output = ${dir}/${lepNum}${lep}${iso}${category}${cuts}.output
log = ${dir}/${lepNum}${lep}${iso}${category}${cuts}.log
Queue
EOM
                        done
                    done
                done
            done
        done
    done
done
#     dir="$OUTPUT_DIR/${group}"
#     mkdir $dir
    #echo "Will run:"
    # if [ -n "$TWO_LEPTONS" ]; then
#         cmd="$CONDOR_WRAPPER $CUT_OPTIMISATION_SCRIPTS/dilepton_tmva.py -i $input -bg  $BG_INPUT -o $dir/${group}.root  --tl"
#     else
#         cmd="$CONDOR_WRAPPER $CUT_OPTIMISATION_SCRIPTS/dilepton_tmva.py -i $input -bg  $BG_INPUT/${group}/single -o $dir/${group}.root"
#     fi
#     cmd="$CONDOR_WRAPPER $CUT_OPTIMISATION_SCRIPTS/dilepton_tmva.py -i $input -bg  $BG_INPUT -o $dir/${group}.root"
#     echo $cmd
# cat << EOM >> $output_file
# arguments = $cmd
# error = ${dir}/${group}.err
# output = ${dir}/${group}.output
# Queue
# EOM
#     echo error = ${dir}/${group}.err
#     echo output = ${dir}/${group}.output
# done

# RUN ALL CATEGORY - only for track+lepton

# if [[ -z "$TWO_LEPTONS" ]]; then
#     echo -e "\n\n\nRunning ALL category!!!!!\n\n\n"
#     group=all
#     value=${SIM_GROUP[$group]}
#     input=""
#     background=""
#     for pattern in $value; do        
#         input="$input ${INPUT_SIG_DIR}_all/single/*.root"
#     done
#     dir="$OUTPUT_DIR/${group}"
#     mkdir $dir
#     echo "Will run:"
#     cmd="$CONDOR_WRAPPER $CUT_OPTIMISATION_SCRIPTS/dilepton_tmva.py -i $input -bg  $BG_INPUT/${group}/single -o $dir/${group}.root"
#     echo $cmd
# cat << EOM >> $output_file
# arguments = $cmd
# error = ${dir}/${group}.err
# output = ${dir}/${group}.output
# Queue
# EOM
# fi

condor_submit $output_file
echo $output_file
rm $output_file