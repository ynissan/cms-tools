#!/bin/bash
# cms software setup
export SCRAM_ARCH=slc6_amd64_gcc530
echo "working directory"
	

tar xvf loot.tar

cd CMSSW_8_0_5_patch1/src/
eval `scramv1 runtime -sh`
cd ../../

cmsDriver.py SIGID_cff  --conditions auto:run2_mc --fast  --era Run2_2016 --eventcontent AODSIM --relval 100000,1000 -s GEN,SIM,RECOBEFMIX,DIGI:pdigi_valid,L1,DIGI2RAW,L1Reco,RECO,EI,HLT:@relval25ns --datatier AODSIM --beamspot Realistic50ns13TeVCollision --fileout SIGID_AODSIM_n0.root --no_exec -n NUMEVENTS 

echo "ls'ing"
ls
#,EI,HLT:@relval25ns

python StealthSusy/python/edit_config.py SIGID_cff_GEN_SIM_RECOBEFMIX_DIGI_L1_DIGI2RAW_L1Reco_RECO_EI_HLT.py 

cmsRun SIGID_cff_GEN_SIM_RECOBEFMIX_DIGI_L1_DIGI2RAW_L1Reco_RECO_EI_HLT.py

cmsDriver.py step3 --conditions auto:run2_mc --fast --eventcontent MINIAODSIM --runUnscheduled --filein file:SIGID_AODSIM_n0.root -s PAT --datatier MINIAODSIM --era Run2_25ns --mc --fileout SIGID_miniAODSIM_n0.root -n NUMEVENTS

xrdcp SIGID_miniAODSIM_n0.root root://cmseos.fnal.gov//store/user/sbein/StealthSusy/Production/miniaodsim/

rm *.py 
rm *.root

#try going back to scratch area before running code
