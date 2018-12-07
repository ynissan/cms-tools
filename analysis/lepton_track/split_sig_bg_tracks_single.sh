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

/afs/desy.de/user/n/nissanuv/cms-tools/analysis/lepton_track/split_sig_bg_tracks.py $@