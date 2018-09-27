#!/bin/bash

shopt -s nullglob
shopt -s expand_aliases

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

OLD_PWD=$PWD

# CMS ENV
cd $CMS_WD
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsenv

cd $OLD_PWD

/afs/desy.de/user/n/nissanuv/cms-tools/analysis/cut_optimisation/tmva/tmva.py $@

