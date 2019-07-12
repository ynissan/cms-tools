#!/bin/bash

# CONSTS
. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

# necessary for running cmsenv
shopt -s expand_aliases

# CMS ENV
cd /afs/desy.de/user/n/nissanuv/treemaker/CMSSW_9_4_11/src
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

test_dir=/afs/desy.de/user/n/nissanuv/treemaker/CMSSW_9_4_11/src/TreeMaker/Production/test
cd $test_dir

echo Nopa@2wd | voms-proxy-init -voms cms:/cms -valid 192:00
export X509_USER_PROXY=$(voms-proxy-info | grep path | cut -b 13-)
export DICTLIST=RunIISummer16MiniAODv3_dyjets_yuval-AOD

sample_name=$1
counter=$2
outfile=$3

#workdir=${test_dir}/${sample_name}_${outfile}
#mkdir workdir
#cd workdir
#Summer16MiniAODv3

cmsRun $test_dir/runMakeTreeFromMiniAOD_cfg.py outfile=$outfile inputFilesConfig=RunIISummer16MiniAODv3.${sample_name}-AOD nstart=$counter nfiles=1 scenario=Summer16MiniAODv3 numevents=1 reportfreq=100
./get_miniAOD_filenames.py --infile="$(cat info_aodfilenames)"
cmsRun $test_dir/runMakeTreeFromMiniAOD_cfg.py outfile=$outfile inputFilesConfig=RunIISummer16MiniAODv3.${sample_name}-AOD nstart=$counter nfiles=1 scenario=Summer16MiniAODv3 numevents=1 reportfreq=100

exit 0