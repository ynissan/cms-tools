#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

for f in ZJetsToNuNu_HT-200To400.root WJetsToLNu_HT-200To400.root ZJetsToNuNu_HT-600To800.root ZJetsToNuNu_HT-400To600.root WJetsToLNu_HT-100To200.root WJetsToLNu_HT-1200To2500.root; do 
#for f in WJetsToLNu_HT-1200To2500.root; do 
	$SCRIPTS_WD/skim_split.py -i $SKIM_OUTPUT_DIR/sum/type_sum/$f > /tmp/${f}.output 
done