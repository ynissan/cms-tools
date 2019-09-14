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
    getopts ":j:p:o:" opt || status=$?
    case "$opt" in
        j) export JOBNAME=$OPTARG
        ;;
        p) export PROCESS=$OPTARG
        ;;
        o) export OUTDIR=$OPTARG
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
echo ""

# run CMSSW
ARGS=$(cat args_${JOBNAME}_${PROCESS}.txt)

echo "ARGS FROM FILE: $ARGS"

# check for incorrect pilot cert
vomsident = $(voms-proxy-info -identity)
echo $vomsident
if [[ $vomsident = *"cmsgli"* ]]; then
    # this is the exit code for "User is not authorized to write to destination site."
    rm *.root
    echo "exit code 60322, skipping file copy"	
    exit 60322
fi

# cp "$CMSSW_BASE/src/TreeMaker/Production/test/job_main_loop.py" .
# chmod +x job_main_loop.py
# ./job_main_loop.py --outpath=$OUTDIR --arguments="$ARGS"
# CMSSWSTATUS=$?
# if [[ $CMSSWSTATUS -ne 0 ]]; then
#     echo "error $CMSSWSTATUS"
#     exit CMSSWSTATUS
# fi

rm *.root