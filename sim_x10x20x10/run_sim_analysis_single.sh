#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

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
cd $CMS_WD
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/afs/desy.de/user/n/nissanuv/cms-tools/lib/classes

SCRIPT_PATH=$ANALYZER_PATH
if [ -n "$SKIM" ]; then
	echo "GOT SKIM"
	SCRIPT_PATH=$SKIMMER_PATH
fi

$SCRIPT_PATH ${POSITIONAL[@]}

