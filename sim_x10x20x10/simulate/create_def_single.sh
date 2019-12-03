#!/bin/bash

. "$CMSSW_BASE/src/cms-tools/lib/def.sh"

shopt -s nullglob

# necessary for running cmsenv
shopt -s expand_aliases

# CMS ENV
cd ~/CMSSW_9_4_11/src
# . /etc/profile.d/modules.sh
# module use -a /afs/desy.de/group/cms/modulefiles/
# module load cmssw

export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

cmsenv

if [[ `hostname` == *".desy.de"* ]]; then
    echo Nopa@2wd | voms-proxy-init -voms cms:/cms -valid 192:00
    export X509_USER_PROXY=$(voms-proxy-info | grep path | cut -b 13-)
fi



#cmsDriver.py $1 --datamix PreMix --conditions auto:run2_mc --pileup_input dbs:/RelValFS_PREMIXUP15_PU25/CMSSW_9_4_11_cand2-PU25ns_94X_mcRun2_asymptotic_v3_FastSim-v1/GEN-SIM-DIGI-RAW --fast --era Run2_2016 --eventcontent AODSIM --relval 100000,1000 -s GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2:pdigi_valid,DATAMIX,L1,DIGI2RAW,L1Reco,RECO --datatier AODSIM --beamspot Realistic50ns13TeVCollision --python_filename=$2 --fileout $3 --no_exec -n 500 --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput
                                                                                
cmsDriver.py $1 --datamix PreMix --conditions auto:run2_mc --pileup_input dbs:/RelValFS_PREMIXUP15_PU25/CMSSW_9_3_0_pre5-PU25ns_93X_mcRun2_asymptotic_v0_FastSim-v1/GEN-SIM-DIGI-RAW  --fast --era Run2_2016 --eventcontent AODSIM --relval 100000,1000 -s GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2:pdigi_valid,DATAMIX,L1,DIGI2RAW,L1Reco,RECO --datatier AODSIM --beamspot Realistic50ns13TeVCollision --python_filename=$2 --fileout $3 --no_exec -n 500 --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput

cat << EOM >> $2
from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randSvc.populate()
EOM

echo Running: $COPY_CMD ${COPY_DEST_PREFIX}$2 $SIG_CONFIG_OUTPUT_DIR/single/

$COPY_CMD ${COPY_DEST_PREFIX}$2 $SIG_CONFIG_OUTPUT_DIR/single/
rm $2
