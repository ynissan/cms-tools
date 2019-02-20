#!/bin/bash

shopt -s nullglob
shopt -s expand_aliases

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

#---------- GET OPTIONS ------------
POSITIONAL=()
while [[ $# -gt 0 ]]
do
	key="$1"

	case $key in
	    -o)
	    OUTPUT_DIR=$(dirname $2)
	    POSITIONAL+=("$1") # save it in an array for later
	    POSITIONAL+=("$2") # save it in an array for later
	    shift # past argument
	    shift
	    ;;
	    *)    # unknown option
	    POSITIONAL+=("$1") # save it in an array for later
	    shift # past argument
	    ;;
	esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters
#---------- END OPTIONS ------------

# CMS ENV
cd $CMS_WD
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

echo "dir $OUTPUT_DIR"
cd $OUTPUT_DIR


echo "Running /afs/desy.de/user/n/nissanuv/cms-tools/analysis/cut_optimisation/tmva/dilepton_tmva.py $@"
/afs/desy.de/user/n/nissanuv/cms-tools/analysis/cut_optimisation/tmva/dilepton_tmva.py $@

