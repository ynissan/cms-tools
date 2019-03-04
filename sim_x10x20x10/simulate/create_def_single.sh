#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob

# necessary for running cmsenv
shopt -s expand_aliases

# CMS ENV
cd ~/CMSSW_8_0_5_patch1/src
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

cd $SIG_CONFIG_OUTPUT_DIR/single

$@
