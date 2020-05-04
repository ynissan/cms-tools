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
import argparse

parser = argparse.ArgumentParser(description='Create skims for x1x2x1 process.')
parser.add_argument('-tl', '--tl', dest='two_leptons', help='Two Leptons', action='store_true')
parser.add_argument('-sam', '--sam', dest='sam', help='Sam Skims', action='store_true')
args = parser.parse_args()

two_leptons = args.two_leptons
sam = args.sam

skim_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/single/"
output_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim/sum"

if sam:
    skim_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_sam/single/"
    output_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_sam/sum"

if two_leptons:
    skim_dir = "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1/signal/skim/single/"
    output_dir = "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1/signal/skim/sum"
    if sam:
        skim_dir = "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1/signal/skim_sam/single/"
        output_dir = "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1/signal/skim_sam/sum"

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

files = glob(skim_dir + "/*higgsino*");

points = {}

for f in files:
    point = None
    if sam:
        point = "_".join(os.path.basename(f).split("_")[2:4])
    else:
        point = "_".join(os.path.basename(f).split("_")[0:3])
    if points.get(point) is None:
        points[point] = 1
    else:
        points[point] += 1

print points

for point in points:
    point_files = glob(skim_dir + "/*" + point + "*")
    print "point=" + point
    print "size=" + str(len(point_files))
    cmd = "hadd -f " + output_dir + "/" + point + ".root " + " ".join(point_files)
    print "Running cmd: " + cmd
    system(cmd)

