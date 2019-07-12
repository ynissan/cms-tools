#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob

# necessary for running cmsenv
shopt -s expand_aliases

# CMS ENV
cd $CMS_WD
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/afs/desy.de/user/n/nissanuv/cms-tools/lib/classes

$SCRIPTS_WD/skimmer_x1x2x1_univ_bdt_track_bdt.py $@

