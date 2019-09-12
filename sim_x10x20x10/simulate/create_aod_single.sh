#!/bin/bash

. "$CMSSW_BASE/src/cms-tools/lib/def.sh"

shopt -s nullglob

# necessary for running cmsenv
shopt -s expand_aliases

echo "HOME DIRECTORY IS $HOME"

# CMS ENV
cd ~/CMSSW_9_4_11/src
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

echo Nopa@2wd | voms-proxy-init -voms cms:/cms -valid 192:00
export X509_USER_PROXY=$(voms-proxy-info | grep path | cut -b 13-)

$@
