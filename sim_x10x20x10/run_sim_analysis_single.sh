#!/bin/bash

shopt -s nullglob

#---------- GET OPTIONS ------------
POSITIONAL=()
while [[ $# -gt 0 ]]
do
	key="$1"

	case $key in
	    -skim|--skim)
	    SKIM=true
	    shift # past argument
	    ;;
	    *)    # unknown option
	    POSITIONAL+=("$1") # save it in an array for later
	    shift # past argument
	    ;;
	esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters
#---------- END OPTIONS ------------

# necessary for running cmsenv
shopt -s expand_aliases

# CMS ENV
cd ~/CMSSW_11_3_1/src

export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

cmsenv

. "$CMSSW_BASE/src/stops/lib/def.sh"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$CMSSW_BASE/src/stops/lib/classes"

SCRIPT_PATH=$ANALYZER_PATH
if [ -n "$SKIM" ]; then
	echo "GOT SKIM"
	SCRIPT_PATH=$SKIMMER_PATH
fi

$SCRIPT_PATH ${POSITIONAL[@]}

