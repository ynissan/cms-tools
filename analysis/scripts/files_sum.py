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

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import utils

parser = argparse.ArgumentParser(description='Sum histograms and trees.')
parser.add_argument('-hadd', '--hadd', dest='hadd', help='Add histogram', action='store_true')
parser.add_argument('-cp', '--create_plots', dest='cp', help='Create plots', action='store_true')
parser.add_argument('-a', '--all', dest='all', help='Perform all', action='store_true')
parser.add_argument('-s', '--stack', dest='stack', help='Perform stack', action='store_true')
parser.add_argument('-skim', '--skim', dest='skim', help='Work on skim', action='store_true')
parser.add_argument('-bg', '--background', dest='bg', help='Signal', action='store_true')
parser.add_argument('-sig', '--signal', dest='sig', help='Background', action='store_true')
args = parser.parse_args()

hadd = args.hadd
cp = args.cp
all = args.all
stack = args.stack
skim = args.skim
signal = args.sig
bg = args.bg

if (bg and signal) or not (bg or signal):
    signal = True
    bg = False

WORK_DIR = None
if bg:
    if skim:
        WORK_DIR = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim"
    else:
        WORK_DIR = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/hist"
else:
    if skim:
        WORK_DIR = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim"
    else:
        WORK_DIR = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/hist"

SINGLE_OUTPUT = WORK_DIR + "/single"
OUTPUT_SUM = WORK_DIR + "/sum"
OUTPOUT_TYPE_SUM = OUTPUT_SUM + "/type_sum"
OUTPOUT_PROCESSED = OUTPUT_SUM + "/processed"
OUTPOUT_STACK = OUTPUT_SUM + "/stack"

if not os.path.isdir(OUTPUT_SUM):
    os.mkdir(OUTPUT_SUM)

if not os.path.isdir(OUTPOUT_TYPE_SUM):
    os.mkdir(OUTPOUT_TYPE_SUM)

if not os.path.isdir(OUTPOUT_PROCESSED):
    os.mkdir(OUTPOUT_PROCESSED)

if not os.path.isdir(OUTPOUT_STACK):
    os.mkdir(OUTPOUT_STACK)

sumTypes = {}

def createPlots(rootfiles, outputFileName):

    print rootfiles

    fnew = TFile(OUTPOUT_PROCESSED + "/" + outputFileName +'.root','recreate')
    fhists0 = TFile(rootfiles[0])
    keys = fhists0.GetListOfKeys()
    HT = fhists0.Get("HT").Clone()
    for key in keys:
        name = key.GetName()#histogram name
        h = fhists0.Get(name).Clone()
        numOfEvents = HT.Integral(-1,99999999)+0.000000000001
        #print "numOfEvents=" + str(numOfEvents)
        weight = utils.LUMINOSITY/numOfEvents
        #print "weight=" + str(weight)
        #print "file=" +  rootfiles[0] + " key=" + name + " numOfEvents=" + str(numOfEvents) + " weight=" + str(weight)
        if name != "HT":
            #print "scaling hist=" + name + " weight=" + str(weight)
            h.Scale(weight)
        for fname in rootfiles[1:]:
            #print "******"
            f_ = TFile(fname)
            fhists0.cd()
            h_ = f_.Get(name).Clone()
            hHT_ = f_.Get("HT").Clone()
            numOfEvents = hHT_.Integral(-1,99999999)+0.000000000001
            weight = utils.LUMINOSITY/numOfEvents
            #print "file=" +  fname + " key=" + name + " numOfEvents=" + str(numOfEvents) + " weight=" + str(weight)
            if name != "HT":
                print "scaling hist=" + name + " weight=" + str(weight)
                h_.Scale(weight)
            h.Add(h_)

        fnew.cd()
        h.Write()
        fhists0.cd()
    fnew.Close()

def getCompoundTypeFiles(cType):
    rootFiles = []
    for type in utils.compoundTypes[cType]:
        rootFiles.extend(glob(OUTPOUT_TYPE_SUM + "/*" + type + "*.root"))
    return rootFiles


# Add the histograms
if hadd or all:
    print "Adding histograms."
    fileList = glob(SINGLE_OUTPUT + "/*");
    for f in fileList :
        filename = None
        if bg:
            filename = os.path.basename(f).split(".")[1]
        else:
            filename = os.path.basename(f).split(".")[0]
        types = filename.split("_")
        type = types[0]
        if type not in sumTypes:
            sumTypes[type] = {}
        if bg:
            if type == "DYJetsToLL":
                sumTypes[type][types[2]] = True
            elif type == "ST":
                sumTypes[type][types[1] + "_" + types[2]] = True
            else:
                sumTypes[type][types[1]] = True

    print sumTypes 
    #exit(0)
    for type in sumTypes:
        print type
        if bg:
            for typeRange in sumTypes[type]:
                command = None
                if type == "DYJetsToLL":
                    command = "hadd -f " + OUTPOUT_TYPE_SUM + "/" + type + "_" + typeRange + ".root " + SINGLE_OUTPUT + "/Summer16." + type + "_*" + typeRange + "*.root"
                else:
                    command = "hadd -f " + OUTPOUT_TYPE_SUM + "/" + type + "_" + typeRange + ".root " + SINGLE_OUTPUT + "/Summer16." + type + "_" + typeRange + "_*.root"
                print "Perorming:", command 
                system(command)
        else:
            command = "hadd -f " + OUTPOUT_TYPE_SUM + "/" + type + ".root " + SINGLE_OUTPUT + "/" + type + "_*.root"
            print "Perorming:", command 
            system(command)

if cp or all:
    print "Creating plots."

    sumTypes = {}
    fileList = glob(OUTPOUT_TYPE_SUM + "/*")
    for f in fileList : 
        filename = os.path.basename(f).split(".")[0]
        types = filename.split("_")
        if types[0] not in sumTypes:
            sumTypes[types[0]] = {}
        sumTypes[types[0]][types[1]] = True

    print sumTypes

    for type in sumTypes:
        if utils.existsInCoumpoundType(type):
            continue
        print "Summing type", type
        rootfiles = glob(OUTPOUT_TYPE_SUM + "/*" + type + "*.root")
        createPlots(rootfiles, type)
    for cType in utils.compoundTypes:
        print "Creating compound type", cType
        rootFiles = getCompoundTypeFiles(cType)
        if len(rootFiles):
            createPlots(rootFiles, cType)

print "Stack " + str(stack)

if stack or all:
    print "Creating Stacks."
    rtstacks___ = TFile(OUTPOUT_STACK + "/stacked_histograms.root",'recreate')
    rootfiles = utils.orderBgFiles(glob(OUTPOUT_PROCESSED + "/*"))
    files = []
    for i,file in enumerate(rootfiles):
        files.append(TFile(rootfiles[i]))
    
    keys = files[0].GetListOfKeys()
    for key in keys:
        name = key.GetName()#histogram name
        print "Creating " + name
        hs = THStack(name,"");
        filename = os.path.basename(rootfiles[0]).split(".")[0]
        h = files[0].Get(name)
        h.SetDirectory(0)
        h.SetName(filename)
        hs.Add(h)
        for i, fname in enumerate(rootfiles[1:]):
            filename = os.path.basename(fname).split(".")[0]
            h = files[i+1].Get(name)
            h.SetDirectory(0)
            h.SetName(filename)
            hs.Add(h)
        rtstacks___.cd()
        hs.Write()
    rtstacks___.Close()
    for f in files:
        f.Close()

exit(0)
