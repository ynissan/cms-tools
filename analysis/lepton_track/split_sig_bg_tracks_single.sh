#!/bin/bash

shopt -s nullglob
shopt -s expand_aliases

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

# CMS ENV
cd $CMS_WD
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/afs/desy.de/user/n/nissanuv/cms-tools/lib/classes

/afs/desy.de/user/n/nissanuv/cms-tools/analysis/lepton_track/split_sig_bg_tracks.py $@