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

OUTPUT_DIR=$SKIM_SIG_BDT_OUTPUT_DIR
#OUTPUT_DIR="$OUTPUT_WD/signal/skim_signal_bdt_tighter"

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

for sim in ${SKIM_SIG_OUTPUT_DIR}/single/*; do
	filename=$(basename $sim .root)
	echo "Will run:"
	echo $SCRIPTS_WD/run_skim_signal_bdt_single.sh -i $sim -o ${OUTPUT_DIR}/single/${filename}.root -tb $LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva/$filename  -ub $OUTPUT_WD/cut_optimisation/tmva/total_bdt_no_norm_full_skim_no_spectator_lj_eta_correct_weight
cat << EOM >> $output_file
arguments = $SCRIPTS_WD/run_skim_signal_bdt_single.sh -i $sim -o ${OUTPUT_DIR}/single/${filename}.root -tb $LEPTON_TRACK_SPLIT_DIR/cut_optimisation/tmva/$filename  -ub $OUTPUT_WD/cut_optimisation/tmva/total_bdt_no_norm_full_skim_no_spectator_lj_eta_correct_weight
error = ${OUTPUT_DIR}/stderr/${filename}.err
output = ${OUTPUT_DIR}/stdout/${filename}.output
Queue
EOM
done

#condor_submit $output_file
rm $output_file
