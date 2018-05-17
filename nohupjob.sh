#!/bin/bash

for i in {12..15}
do
echo "######################### BEGIN NEW RUN ######################"
cmsRun StealthSqSq_test_cff_GEN_SIM_RECOBEFMIX_DIGI_L1_DIGI2RAW_L1Reco_RECO_EI_HLT.py
mv simData10.root simData$i.root
done
