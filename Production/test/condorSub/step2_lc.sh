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
    getopts ":j:p:o:i:" opt || status=$?
    case "$opt" in
        j) export JOBNAME=$OPTARG
        ;;
        p) export PROCESS=$OPTARG
        ;;
        o) export OUTDIR=$OPTARG
        ;;
        i) export INDIR=$OPTARG
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
echo "INDIR:      $INDIR"
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

# copy output to eos
echo "prepare gfal tools"
if [ -e "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.3/current/el6-x86_64/setup.sh" ]; then
    . /cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.3/current/el6-x86_64/setup.sh
fi      
export CMDSTR="gfal-copy"
export GFLAG=""

for f in ${ARGS[*]}; do
    echo "Processing " $f
done

# if [[ "$MODE" == "def" ]]; then
#     cmd="cmsDriver.py ${ARGS[0]} --datamix PreMix --conditions auto:run2_mc --pileup_input dbs:/RelValFS_PREMIXUP15_PU25/CMSSW_9_4_11_cand2-PU25ns_94X_mcRun2_asymptotic_v3_FastSim-v1/GEN-SIM-DIGI-RAW --fast --era Run2_2016 --eventcontent AODSIM --relval 100000,1000 -s GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2:pdigi_valid,DATAMIX,L1,DIGI2RAW,L1Reco,RECO --datatier AODSIM --beamspot Realistic50ns13TeVCollision --python_filename=${ARGS[1]} --fileout ${ARGS[2]} --no_exec -n 5 --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput"
#     echo Runnning: $cmd
#     $cmd
# elif [[ "$MODE" == "aod" ]]; then
#     echo Running: ${CMDSTR} -n 1 ${ARGS[0]} .
#     ${CMDSTR} -n 1 ${ARGS[0]} .
#     export local_file=$(basename ${ARGS[0]})
#     cmd="cmsRun $local_file"
#     echo "Running: $cmd"
#     $cmd
# fi

CMSEXIT=$?

echo "Exit Status: $CMSEXIT"
exit 0

if [[ $CMSEXIT -ne 0 ]]; then
        if [[ "$MODE" == "aod" ]]; then
            rm $(basename ${ARGS[0]})
        fi
        echo "exit code $CMSEXIT, skipping gfal-copy"
        exit $CMSEXIT
fi

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
    move_file=$(basename ${ARGS[0]} .py)
    move_file=${move_file}_AOD.root
    echo Running: ${CMDSTR} -n 1 $move_file ${OUTDIR}/
    ${CMDSTR} -n 1 $move_file ${OUTDIR}/
    rm $move_file
    rm $local_file
fi

echo "END OF SCRIPT"