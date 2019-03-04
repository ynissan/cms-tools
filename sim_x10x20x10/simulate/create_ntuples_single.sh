#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob

# necessary for running cmsenv
shopt -s expand_aliases

# CMS ENV
cd /afs/desy.de/user/n/nissanuv/CMSSW_9_4_11/src
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

cd /afs/desy.de/user/n/nissanuv/CMSSW_9_4_11/src/TreeMaker/Production/test

echo PWD = $PWD

$@
