#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
#module load root6
cd /afs/desy.de/user/n/nissanuv/CMSSW_8_0_30/src
cmsenv

$CLONE_SCRIPT $@
        
