#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

# necessary for running cmsenv
shopt -s expand_aliases

# CMS ENV
cd $CMS_WD
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
#cmsenv

module load root6

$ANALYZER_PATH $@

