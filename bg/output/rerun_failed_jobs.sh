#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

for fullname in `cat ./failed_jobs`; do
	if [[ $fullname =~ "TTJets_TuneCUETP8M1" ]]
	then
		cmd="qsub -l h_vmem=2G -o $STD_OUTPUT/$(basename $fullname .root).output  -e $ERR_OUTPUT/$(basename $fullname .root).err $SCRIPTS_WD/run_bg_analysis_single.sh --madHTlt 600 -i $NEWEST_SIM_DIR/$fullname &"
    		echo -e "\nRunning command:\n$cmd"
    		eval $cmd
	elif [[ $fullname =~ "TTJets_HT" ]]
	then
		cmd="qsub -l h_vmem=2G -o $STD_OUTPUT/$(basename $fullname .root).output  -e $ERR_OUTPUT/$(basename $fullname .root).err $SCRIPTS_WD/run_bg_analysis_single.sh --madHTgt 600 -i $NEWEST_SIM_DIR/$fullname &"
    		echo -e "\nRunning command:\n$cmd"
    		eval $cmd
	else
		cmd="qsub -l h_vmem=2G -o $STD_OUTPUT/$(basename $fullname .root).output  -e $ERR_OUTPUT/$(basename $fullname .root).err $SCRIPTS_WD/run_bg_analysis_single.sh -i $NEWEST_SIM_DIR/$fullname &"
    		echo -e "\nRunning command:\n$cmd"
    		eval $cmd
	fi
done