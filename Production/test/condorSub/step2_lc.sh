#!/bin/bash

# check for incorrect pilot cert
vomsident=$(voms-proxy-info -identity)
echo $vomsident
if [[ $vomsident = *"cmsgli"* ]]; then
    # this is the exit code for "User is not authorized to write to destination site."
    exit 60322
fi

echo "========================="
echo printing os information:
uname -a
echo "========================="

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
#if [ -e "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.3/current/el6-x86_64/setup.sh" ]; then
if [ -e "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/current/el7-x86_64/setup.sh" ]; then
    #. /cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.3/current/el6-x86_64/setup.sh
    . /cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/current/el7-x86_64/setup.sh
fi      
export CMDSTR="gfal-copy"
export GFLAG=""

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CMSSW_BASE/src/stops/lib/classes

cd $CMSSW_BASE/src/stops/lib/classes
rm LeptonCollectionMapDict.cxx
rootcling -f LeptonCollectionMapDict.cxx -c LeptonCollectionMap.h LinkDef.h
rm LeptonCollectionMap_C.so
echo .L LeptonCollectionMap.C+ | root.exe -b

cd $CMSSW_BASE/src/stops/analysis/scripts/

if [[ ( "$CMSSITE" == "T1_US_FNAL" && "$USER" == "cmsgli" && "${OUTDIR}" == *"root://cmseos.fnal.gov/"* ) ]]; then
    export CMDSTR="gfal-copy"
    export GFLAG="-g"
    export GSIFTP_ENDPOINT="gsiftp://cmseos-gridftp.fnal.gov//eos/uscms/store/user/"
    export OUTDIR=${GSIFTP_ENDPOINT}${OUTDIR#root://cmseos.fnal.gov//store/user/}
fi

for f in ${ARGS[*]}; do
    echo "Processing " $f
    echo "Running ${CMDSTR} -n 1 $INDIR/$f ."
    (eval `scram unsetenv -sh`; ${CMDSTR} -n 1 $INDIR/$f .)
    #${CMDSTR} -n 1 $INDIR/$f .
    mkdir tmp
    echo "Running ./create_lepton_collection.py -i $f -o tmp/$f"
    ./create_lepton_collection.py -i $f -o tmp/$f
    EXIT_STATUS=$?
    if [[ $EXIT_STATUS -ne 0 ]]; then
        echo "exit code $EXIT_STATUS, skipping gfal-copy"
        rm $f
        rm -rf tmp
        continue
    fi
    echo "Running ${CMDSTR} -n 1 tmp/$f ${OUTDIR}/"
    (eval `scram unsetenv -sh`; ${CMDSTR} -f tmp/$f ${OUTDIR}/)
    #${CMDSTR} -f tmp/$f ${OUTDIR}/
    if [[ $? -ne 0 ]]; then
        echo "Deleting file because gfal-copy failed"
        echo gfal-rm ${OUTDIR}/$f
        (eval `scram unsetenv -sh`; gfal-rm ${OUTDIR}/$f)
    fi
    rm $f
    rm -rf tmp
done

exit 0