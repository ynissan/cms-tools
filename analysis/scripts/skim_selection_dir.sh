#!/bin/bash

echo START
uptime

dir=/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_dy/tmp

for i in $dir/*; do
    echo ./skimmer_selection.py -i $i -o $dir/slim_$(basename $i)
    ./skimmer_selection.py -i $i -o $dir/slim_$(basename $i)
    echo mv $dir/slim_$(basename $i) $i
    mv $dir/slim_$(basename $i) $i
    echo ""
    echo ""
    echo ""
done

echo END
uptime