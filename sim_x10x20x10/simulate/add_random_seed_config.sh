#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob 

for f in $SIG_CONFIG_OUTPUT_DIR/single/*; do
	cat << EOM >> $f
from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randSvc.populate()
EOM
done