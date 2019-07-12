#!/bin/bash

# CONSTS
. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

# necessary for running cmsenv
shopt -s expand_aliases

# CMS ENV
cd /afs/desy.de/user/n/nissanuv/treemaker/CMSSW_9_4_11/src
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

OUTPUT_DIR="/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/.ntuples"

STD_OUTPUT="${OUTPUT_DIR}/stdout"
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

cd /afs/desy.de/user/n/nissanuv/treemaker/CMSSW_9_4_11/src/TreeMaker/Production/test

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

file_limit=1
i=0
count=0

for sample_name in DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8; do
    echo "Checking sample $sample_name"
    sample_file=`ls /afs/desy.de/user/n/nissanuv/treemaker/CMSSW_9_4_11/src/TreeMaker/Production/python/RunIISummer16MiniAODv3/${sample_name}*.py`
    echo "File is $sample_file"
    counter=1
    grep '/store/' $sample_file | while read -r line ; do
        echo "Processing $line"
        echo $counter
        /afs/desy.de/user/n/nissanuv/cms-tools/bg/simulate/simulate_bg_single.sh $sample_name $counter $FILE_OUTPUT/Summer16.${sample_name}_${counter}
cat << EOM >> $output_file
arguments = /afs/desy.de/user/n/nissanuv/cms-tools/bg/simulate/simulate_bg_single.sh $sample_name $counter $FILE_OUTPUT/Summer16.${sample_name}_${counter}
error = $ERR_OUTPUT/${sample_name}_${counter}.err
output = $STD_OUTPUT/${sample_name}_${counter}.output
Queue
EOM
        ((counter+=1))
        if [ $file_limit -gt 0 ]; then
            #check limit
            ((i+=1)) 
            if [ $i -ge $file_limit ]; then
               break
            fi
        fi
    done
    if [ $file_limit -gt 0 ]; then
        #check limit
        ((i+=1)) 
        if [ $i -ge $file_limit ]; then
           break
        fi
    fi
done

echo SUBMITTING JOBS....

#condor_submit $output_file
rm $output_file