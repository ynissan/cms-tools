#!/bin/bash

# check for incorrect pilot cert
vomsident=$(voms-proxy-info -identity)
echo $vomsident
if [[ $vomsident = *"cmsgli"* ]]; then
	# this is the exit code for "User is not authorized to write to destination site."
	exit 60322
fi

export JOBNAME=""
export PROCESS=""
export OUTDIR=""
export REDIR=""
export OPTIND=1
while [[ $OPTIND -lt $# ]]; do
	# getopts in silent mode, don't exit on errors
	getopts ":j:p:o:x:" opt || status=$?
	case "$opt" in
		j) export JOBNAME=$OPTARG
		;;
		p) export PROCESS=$OPTARG
		;;
		o) export OUTDIR=$OPTARG
		;;
		x) export REDIR=$OPTARG
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
echo "REDIR:      $REDIR"
echo ""


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

if [[ ( "$CMSSITE" == "T1_US_FNAL" && "$USER" == "cmsgli" && "${OUTDIR}" == *"root://cmseos.fnal.gov/"* ) ]]; then
    export CMDSTR="gfal-copy"
    export GFLAG="-g"
    export GSIFTP_ENDPOINT="gsiftp://cmseos-gridftp.fnal.gov//eos/uscms/store/user/"
    export OUTDIR=${GSIFTP_ENDPOINT}${OUTDIR#root://cmseos.fnal.gov//store/user/}
fi


export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CMSSW_BASE/src/stops/lib/classes
cd $CMSSW_BASE/src/stops/lib/classes
rm LumiSectMap_C.so
echo .L LumiSectMap.C+ | root.exe -b
cd $CMSSW_BASE/src/stops/analysis/scripts/

FILE="Summer16.QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1AOD_60000-A8B482FE-C9B0-E611-9FD1-A0000420FE80_RA2AnalysisTree.root"

echo ${CMDSTR} -n 1 srm://dcache-se-cms.desy.de/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/ProductionRun2v3/$FILE .
${CMDSTR} -n 1 srm://dcache-se-cms.desy.de/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/ProductionRun2v3/$FILE .

echo "Running locally"
echo $CMSSW_BASE/src/stops/analysis/scripts/skimmer_x1x2x1.py -i $FILE -o tmp.root -bg
$CMSSW_BASE/src/stops/analysis/scripts/skimmer_x1x2x1.py -i $FILE -o tmp.root -bg
echo "EXIT STATUS: $?"

echo "Running remotely"
echo $CMSSW_BASE/src/stops/analysis/scripts/skimmer_x1x2x1.py -i root://dcache-cms-xrootd.desy.de//pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/ProductionRun2v3/$FILE -o tmp.root -bg
$CMSSW_BASE/src/stops/analysis/scripts/skimmer_x1x2x1.py -i root://dcache-cms-xrootd.desy.de//pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/ProductionRun2v3/$FILE -o tmp.root -bg
echo "EXIT STATUS: $?"



EXITCODE=$?
