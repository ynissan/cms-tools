#!/bin/bash

# check for incorrect pilot cert
vomsident=$(voms-proxy-info -identity)
echo $vomsident
if [[ $vomsident = *"cmsgli"* ]]; then
    # this is the exit code for "User is not authorized to write to destination site."
    exit 60322
fi

echo "Args before getopts: $@"

export JOBNAME=""
export PROCESS=""
export OUTDIR=""
export REDIR=""
export OPTIND=1
while [[ $OPTIND -lt $# ]]; do
    # getopts in silent mode, don't exit on errors
    getopts ":j:p:o:m:" opt || status=$?
    case "$opt" in
        j) export JOBNAME=$OPTARG
        ;;
        p) export PROCESS=$OPTARG
        ;;
        o) export OUTDIR=$OPTARG
        ;;
        m) export MODE=$OPTARG
        ;;
        # keep going if getopts had an error
        \? | :) OPTIND=$((OPTIND+1))
        ;;
    esac
done

echo "parameter set:"
echo "OUTDIR:     $OUTDIR"
echo "JOBNAME:    $JOBNAME"
echo "PROCESS:    $PROCESS"
echo "MODE:       $MODE"
echo ""

# run CMSSW
ARGS_FILE=$(cat args_${JOBNAME}_${PROCESS}.txt)
ARGS=($ARGS_FILE)

echo "ARGS FROM FILE: " ${ARGS[*]}

# check for incorrect pilot cert
vomsident=$(voms-proxy-info -identity)
echo $vomsident
if [[ $vomsident = *"cmsgli"* ]]; then
    # this is the exit code for "User is not authorized to write to destination site."
    rm *.root
    echo "exit code 60322, skipping file copy"
    exit 60322
fi

if [[ "$MODE" == "def" ]]; then
    echo Runnning: cmsDriver.py ${ARGS[0]} --datamix PreMix --conditions auto:run2_mc --pileup_input dbs:/RelValFS_PREMIXUP15_PU25/CMSSW_9_4_11_cand2-PU25ns_94X_mcRun2_asymptotic_v3_FastSim-v1/GEN-SIM-DIGI-RAW --fast --era Run2_2016 --eventcontent AODSIM --relval 100000,1000 -s GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2:pdigi_valid,DATAMIX,L1,DIGI2RAW,L1Reco,RECO --datatier AODSIM --beamspot Realistic50ns13TeVCollision --python_filename=${ARGS[1]} --fileout ${ARGS[2]} --no_exec -n 5 --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput
    cmsDriver.py ${ARGS[0]} --datamix PreMix --conditions auto:run2_mc --pileup_input dbs:/RelValFS_PREMIXUP15_PU25/CMSSW_9_4_11_cand2-PU25ns_94X_mcRun2_asymptotic_v3_FastSim-v1/GEN-SIM-DIGI-RAW --fast --era Run2_2016 --eventcontent AODSIM --relval 100000,1000 -s GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2:pdigi_valid,DATAMIX,L1,DIGI2RAW,L1Reco,RECO --datatier AODSIM --beamspot Realistic50ns13TeVCollision --python_filename=${ARGS[1]} --fileout ${ARGS[2]} --no_exec -n 5 --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput
elif [[ "$MODE" == "aod" ]]; then
    COPY_CMD="gfal-copy ${ARGS[0]} ."
    echo "Running: $COPY_CMD"
    $COPY_CMD
    export basename_name=$(basename ${ARGS[0]})
    cmd="cmsRun  $basename_name"
    echo "Running: $cmd"
    $cmd
fi

CMSEXIT=$?

echo "Exit Status: $CMSEXIT"

if [[ $CMSEXIT -ne 0 ]]; then
        rm $2
        echo "exit code $CMSEXIT, skipping gfal-copy"
        exit $CMSEXIT
fi

if [[ "$MODE" == "def" ]]; then
cat << EOM >> ${ARGS[1]}
from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randSvc.populate()
EOM
fi

# copy output to eos
echo "prepare gfal tools"
if [ -e "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.3/current/el6-x86_64/setup.sh" ]; then
    . /cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.3/current/el6-x86_64/setup.sh
fi      
export CMDSTR="gfal-copy"
export GFLAG=""
if [[ ( "$CMSSITE" == "T1_US_FNAL" && "$USER" == "cmsgli" && "${OUTDIR}" == *"root://cmseos.fnal.gov/"* ) ]]; then
    export CMDSTR="gfal-copy"
    export GFLAG="-g"
    export GSIFTP_ENDPOINT="gsiftp://cmseos-gridftp.fnal.gov//eos/uscms/store/user/"
    export OUTDIR=${GSIFTP_ENDPOINT}${OUTDIR#root://cmseos.fnal.gov//store/user/}
fi
echo "$CMDSTR output for condor"

if [[ "$MODE" == "def" ]]; then
    echo Running: ${CMDSTR} -n 1 ${ARGS[1]} ${OUTDIR}/
    ${CMDSTR} -n 1 ${ARGS[1]} ${OUTDIR}/
    rm ${ARGS[1]}
elif [[ "$MODE" == "aod" ]]; then
    echo Running: ${CMDSTR} -n 1 $basename_name ${OUTDIR}/
    ${CMDSTR} -n 1 $basename_name ${OUTDIR}/
    rm $basename_name
fi

echo "END OF SCRIPT"