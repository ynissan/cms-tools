#!/bin/bash

. "$CMSSW_BASE/src/cms-tools/bg/def.sh"

shopt -s nullglob

# necessary for running cmsenv
shopt -s expand_aliases

# CMS ENV
cd ~/CMSSW_9_4_11/src
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

cd $CMSSW_BASE/src/TreeMaker/Production/test

echo PWD = $PWD

$@
