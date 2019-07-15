#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

#for f in ZJetsToNuNu_HT-100To200.root ZJetsToNuNu_HT-200To400.root WJetsToLNu_HT-200To400.root ZJetsToNuNu_HT-600To800.root ZJetsToNuNu_HT-400To600.root WJetsToLNu_HT-100To200.root WJetsToLNu_HT-1200To2500.root; do 
#for f in WJetsToLNu_HT-200To400.root; do 
#for f in ZJetsToNuNu_HT-100To200.root ZJetsToNuNu_HT-200To400.root WJetsToLNu_HT-200To400.root ZJetsToNuNu_HT-600To800.root ZJetsToNuNu_HT-400To600.root WJetsToLNu_HT-100To200.root WJetsToLNu_HT-1200To2500.root; do 
for f in WW_TuneCUETP8M1.root DYJetsToLL_M-50_HT-100to200.root DYJetsToLL_M-50_HT-200to400.root DYJetsToLL_M-50_HT-400to600.root DYJetsToLL_M-50_HT-600to800.root ST_t-channel_antitop.root TTJets_DiLept.root TTJets_SingleLeptFromT.root TTJets_SingleLeptFromTbar.root WJetsToLNu_HT-600To800.root ST_t-channel_top.root DYJetsToLL_M-50_HT-100to200.root DYJetsToLL_M-50_HT-200to400.root DYJetsToLL_M-50_HT-400to600.root DYJetsToLL_M-50_HT-600to800.root ST_t-channel_antitop.root TTJets_DiLept.root TTJets_SingleLeptFromT.root TTJets_SingleLeptFromTbar.root WJetsToLNu_HT-600To800.root ST_t-channel_top WJetsToLNu_HT-200To400.root ZJetsToNuNu_HT-100To200.root ZJetsToNuNu_HT-200To400.root ZJetsToNuNu_HT-600To800.root ZJetsToNuNu_HT-400To600.root WJetsToLNu_HT-100To200.root WJetsToLNu_HT-1200To2500.root; do 
    $SCRIPTS_WD/skim_split.py -i $SKIM_OUTPUT_DIR/sum/type_sum/$f > /tmp/$f 
    break
done