#!/usr/bin/env python

from ROOT import *
from glob import glob
from math import *
from sys import exit
from array import array
from os import system
import argparse
import os
import sys

skim_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/single/"
output_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum"

SUM_SIZE = 30

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

files = glob(skim_dir + "/higgsino*");

points = {}

for f in files:
    point = "_".join(os.path.basename(f).split("_")[0:3])
    if points.get(point) is None:
        points[point] = 1
    else:
        points[point] += 1

print points

for point in points:
    point_files = glob(skim_dir + "/" + point + "*")
    print "point=" + point
    print "size=" + str(len(point_files))
    cmd = "hadd -f " + output_dir + "/" + point + ".root " + " ".join(point_files)
    print "Running cmd: " + cmd
    system(cmd)

