#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

for dir in $SKIM_BG_SIG_BDT_OUTPUT_DIR/*; do
	echo "Dir=$dir"
	$SCRIPTS_WD/weight_skims.py -i $dir/single/
done