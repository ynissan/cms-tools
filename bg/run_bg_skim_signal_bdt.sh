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
        --jpsi_muons)
        JPSI_MUONS=true
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

#OUTPUT_DIR=$SKIM_BG_SIG_BDT_OUTPUT_DIR
INPUT_DIR=$SKIM_OUTPUT_DIR

if [ -n "$SC" ]; then
    echo "GOT SC"
    echo "HERE: $@"
    #OUTPUT_DIR=$SKIM_BG_SIG_BDT_SC_OUTPUT_DIR
elif [ -n "$DRELL_YAN" ]; then
    echo "GOT DY"
    echo "HERE: $@"
    #OUTPUT_DIR=$SKIM_DY_BG_SIG_BDT_OUTPUT_DIR
    INPUT_DIR=$DY_SKIM_OUTPUT_DIR
elif [ -n "$JPSI_MUONS" ]; then
    INPUT_DIR=$JPSI_MUONS_SKIM_OUTPUT_DIR
fi

#echo OUTPUT_DIR=$OUTPUT_DIR
echo INPUT_DIR=$INPUT_DIR

timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"

# echo $OUTPUT_DIR
# #check output directory
# if [ ! -d "$OUTPUT_DIR" ]; then
#   mkdir $OUTPUT_DIR
# else
#   #rm -rf $OUTPUT_DIR
#   mkdir $OUTPUT_DIR
# fi

cat << EOM > $output_file
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
request_memory = 16 GB
+RequestRuntime = 86400
EOM

#FILES=(WJetsToLNu_HT-600To800_TuneCUETP8M1_11.root TTJets_SingleLeptFromT_TuneCUETP8M1_16.root ST_t-channel_top_3.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_8.root)
#FILES=(TTJets_DiLept_TuneCUETP8M1_10.root TTJets_DiLept_TuneCUETP8M1_11.root TTJets_DiLept_TuneCUETP8M1_13.root TTJets_DiLept_TuneCUETP8M1_15.root TTJets_DiLept_TuneCUETP8M1_1.root TTJets_DiLept_TuneCUETP8M1_20.root TTJets_DiLept_TuneCUETP8M1_25.root TTJets_DiLept_TuneCUETP8M1_2.root TTJets_DiLept_TuneCUETP8M1_55.root TTJets_DiLept_TuneCUETP8M1_61.root TTJets_DiLept_TuneCUETP8M1_65.root TTJets_SingleLeptFromT_TuneCUETP8M1_10.root TTJets_SingleLeptFromT_TuneCUETP8M1_116.root TTJets_SingleLeptFromT_TuneCUETP8M1_18.root TTJets_SingleLeptFromT_TuneCUETP8M1_6.root TTJets_SingleLeptFromT_TuneCUETP8M1_76.root TTJets_SingleLeptFromT_TuneCUETP8M1_7.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_105.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_112.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_113.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_117.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_118.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_123.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_30.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_38.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_4.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_58.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_63.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_66.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_74.root TTJets_SingleLeptFromTbar_TuneCUETP8M1_96.root WJetsToLNu_HT-200To400_TuneCUETP8M1_28.root WJetsToLNu_HT-200To400_TuneCUETP8M1_32.root WJetsToLNu_HT-200To400_TuneCUETP8M1_56.root WJetsToLNu_HT-200To400_TuneCUETP8M1_7.root WJetsToLNu_HT-200To400_TuneCUETP8M1_8.root WJetsToLNu_HT-200To400_TuneCUETP8M1_9.root WJetsToLNu_HT-400To600_TuneCUETP8M1_13.root WJetsToLNu_HT-400To600_TuneCUETP8M1_17.root WJetsToLNu_HT-400To600_TuneCUETP8M1_21.root WJetsToLNu_HT-400To600_TuneCUETP8M1_25.root WJetsToLNu_HT-400To600_TuneCUETP8M1_26.root WJetsToLNu_HT-400To600_TuneCUETP8M1_2.root WJetsToLNu_HT-400To600_TuneCUETP8M1_9.root WJetsToLNu_HT-600To800_TuneCUETP8M1_14.root WJetsToLNu_HT-600To800_TuneCUETP8M1_15.root WJetsToLNu_HT-600To800_TuneCUETP8M1_16.root WJetsToLNu_HT-600To800_TuneCUETP8M1_1.root WJetsToLNu_HT-600To800_TuneCUETP8M1_21.root WJetsToLNu_HT-600To800_TuneCUETP8M1_22.root WJetsToLNu_HT-600To800_TuneCUETP8M1_23.root WJetsToLNu_HT-600To800_TuneCUETP8M1_24.root WJetsToLNu_HT-600To800_TuneCUETP8M1_25.root WJetsToLNu_HT-600To800_TuneCUETP8M1_26.root WJetsToLNu_HT-600To800_TuneCUETP8M1_27.root WJetsToLNu_HT-600To800_TuneCUETP8M1_28.root WJetsToLNu_HT-600To800_TuneCUETP8M1_29.root WJetsToLNu_HT-600To800_TuneCUETP8M1_30.root WJetsToLNu_HT-600To800_TuneCUETP8M1_31.root WJetsToLNu_HT-600To800_TuneCUETP8M1_32.root WJetsToLNu_HT-600To800_TuneCUETP8M1_33.root WJetsToLNu_HT-600To800_TuneCUETP8M1_34.root WJetsToLNu_HT-600To800_TuneCUETP8M1_35.root WJetsToLNu_HT-600To800_TuneCUETP8M1_36.root WJetsToLNu_HT-600To800_TuneCUETP8M1_37.root WJetsToLNu_HT-600To800_TuneCUETP8M1_39.root WJetsToLNu_HT-600To800_TuneCUETP8M1_3.root WJetsToLNu_HT-600To800_TuneCUETP8M1_41.root WJetsToLNu_HT-600To800_TuneCUETP8M1_43.root WJetsToLNu_HT-600To800_TuneCUETP8M1_45.root WJetsToLNu_HT-600To800_TuneCUETP8M1_46.root WJetsToLNu_HT-600To800_TuneCUETP8M1_47.root WJetsToLNu_HT-600To800_TuneCUETP8M1_50.root WJetsToLNu_HT-600To800_TuneCUETP8M1_51.root WJetsToLNu_HT-600To800_TuneCUETP8M1_52.root WJetsToLNu_HT-600To800_TuneCUETP8M1_53.root WJetsToLNu_HT-600To800_TuneCUETP8M1_54.root WJetsToLNu_HT-600To800_TuneCUETP8M1_55.root WJetsToLNu_HT-600To800_TuneCUETP8M1_56.root WJetsToLNu_HT-600To800_TuneCUETP8M1_57.root WJetsToLNu_HT-800To1200_TuneCUETP8M1_11.root WJetsToLNu_HT-800To1200_TuneCUETP8M1_12.root WJetsToLNu_HT-800To1200_TuneCUETP8M1_14.root WJetsToLNu_HT-800To1200_TuneCUETP8M1_15.root WJetsToLNu_HT-800To1200_TuneCUETP8M1_16.root WJetsToLNu_HT-800To1200_TuneCUETP8M1_17.root WJetsToLNu_HT-800To1200_TuneCUETP8M1_18.root WJetsToLNu_HT-800To1200_TuneCUETP8M1_19.root WJetsToLNu_HT-800To1200_TuneCUETP8M1_1.root WJetsToLNu_HT-800To1200_TuneCUETP8M1_23.root WJetsToLNu_HT-800To1200_TuneCUETP8M1_24.root WJetsToLNu_HT-800To1200_TuneCUETP8M1_25.root WJetsToLNu_HT-800To1200_TuneCUETP8M1_3.root ZJetsToNuNu_HT-400To600_13TeV-madgraph_9.root)
FILES=$INPUT_DIR/sum/type_sum/*


for sim in $LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva/*; do
    filename=$(basename $sim .root)

    # if [ ! -d "$OUTPUT_DIR/$filename" ]; then
#       mkdir $OUTPUT_DIR/$filename
#     fi
# 
#     #check output directory
#     if [ ! -d "$OUTPUT_DIR/$filename/single" ]; then
#       mkdir "$OUTPUT_DIR/$filename/single"
#     fi
# 
#     if [ ! -d "$OUTPUT_DIR/$filename/stdout" ]; then
#       mkdir "$OUTPUT_DIR/$filename/stdout" 
#     fi
# 
#     if [ ! -d "$OUTPUT_DIR/$filename/stderr" ]; then
#       mkdir "$OUTPUT_DIR/$filename/stderr"
#     fi

    #for bg_file in $SKIM_OUTPUT_DIR/sum/type_sum/*ZJetsToNuNu_HT-100To200*; do
    #for bg_file in $SKIM_OUTPUT_DIR/sum/type_sum/WW_TuneCUETP8M1*; do
    for bg_file_name in ${FILES[@]}; do
    #for bg_file in $INPUT_DIR/sum/type_sum/*; do
        #bg_file=$INPUT_DIR/sum/type_sum/$bg_file_name
        bg_file=$bg_file_name
        echo "Will run:"
        bg_file_name=$(basename $bg_file .root)
        out_file=${OUTPUT_DIR}/$filename/single/${bg_file_name}.root
        if [ -f "$out_file" ]; then
            echo "$out_file exist. Skipping..."
            continue
        fi
        #cmd="$CONDOR_WRAPPER $SCRIPTS_WD/skimmer_x1x2x1_univ_bdt_track_bdt.py -i $bg_file -o $out_file -tb $LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva/$filename -ub $OUTPUT_WD/cut_optimisation/tmva/total_bdt $@"
        cmd="$CONDOR_WRAPPER $SCRIPTS_WD/skimmer_x1x2x1_track_bdt.py -bg -i $bg_file -tb $LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva/$filename $@"
        echo $cmd
cat << EOM >> $output_file
arguments = $cmd
error = ${INPUT_DIR}/stderr/${bg_file_name}_track_bdt.err
output = ${INPUT_DIR}/stdoutput/${bg_file_name}_track_bdt.output
Queue
EOM
    done
done

condor_submit $output_file
rm $output_file
