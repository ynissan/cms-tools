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

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes"))
from lib import utils

parser = argparse.ArgumentParser(description='Sum histograms and trees.')
parser.add_argument('-hadd', '--hadd', dest='hadd', help='Add histogram', action='store_true')
parser.add_argument('-cp', '--create_plots', dest='cp', help='Create plots', action='store_true')
parser.add_argument('-a', '--all', dest='all', help='Perform all', action='store_true')
parser.add_argument('-s', '--stack', dest='stack', help='Perform stack', action='store_true')
parser.add_argument('-skim', '--skim', dest='skim', help='Work on skim', action='store_true')
parser.add_argument('-bg', '--background', dest='bg', help='Background', action='store_true')
parser.add_argument('-sig', '--signal', dest='sig', help='Signal', action='store_true')
parser.add_argument('-lp', '--lepton_collection', dest='lepton_collection', help='Lepton Collection', action='store_true')
parser.add_argument('-sn', '--signal_ntuples', dest='signal_ntuples', help='Signal Ntuples', action='store_true')
parser.add_argument('-dlc', '--data_lepton_collection', dest='data_lepton_collection', help='Data Lepton Collection', action='store_true')
parser.add_argument('-tl', '--tl', dest='two_leptons', help='Two Leptons', action='store_true')
parser.add_argument('-dy', '--dy', dest='drell_yan', help='Two Leptons', action='store_true')
parser.add_argument('-sc', '--sc', dest='sc', help='Same Charge', action='store_true')
parser.add_argument('-nlp', '--no_lepton_selection', dest='no_lepton_selection', help='No Lepton Selection Skim', action='store_true')
parser.add_argument('-jpsi_electrons', '--jpsi_electrons', dest='jpsi_electrons', help='JPSI Electrons Skim', action='store_true')
parser.add_argument('-jpsi_muons', '--jpsi_muons', dest='jpsi_muons', help='JPSI Muons Skim', action='store_true')
args = parser.parse_args()

hadd = args.hadd
cp = args.cp
all = args.all
stack = args.stack
skim = args.skim
signal = args.sig
bg = args.bg
lepton_collection = args.lepton_collection
signal_ntuples = args.signal_ntuples
data_lepton_collection = args.data_lepton_collection
two_leptons = args.two_leptons
drell_yan = args.drell_yan
sc = args.sc
no_lepton_selection = args.no_lepton_selection
jpsi_muons = args.jpsi_muons


if (bg and signal) or not (bg or signal):
    signal = True
    bg = False

WORK_DIR = None
if bg:
    if skim:
        WORK_DIR = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim"
        if lepton_collection:
            WORK_DIR = "/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/LeptonCollectionFilesMaps/"
        elif two_leptons:
            if sc:
                WORK_DIR = "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1/bg/skim_sc"
            else:
                WORK_DIR = "/afs/desy.de/user/n/nissanuv/nfs/2lx1x2x1/bg/skim"
        elif drell_yan:
            WORK_DIR = "/afs/desy.de/user/n/nissanuv/nfs/dy_x1x2x1/bg/skim"
        elif no_lepton_selection:
            WORK_DIR = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_nlp"
        elif jpsi_muons:
            WORK_DIR = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_muons_jpsi"
    else:
        WORK_DIR = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/hist"
else:
    if skim:
        WORK_DIR = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim"
        if lepton_collection:
            WORK_DIR = "/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/LeptonCollectionFilesMaps/"
    else:
        WORK_DIR = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/hist"
    

SINGLE_OUTPUT = WORK_DIR + "/single"
OUTPUT_SUM = WORK_DIR + "/sum"
OUTPOUT_TYPE_SUM = OUTPUT_SUM + "/type_sum"
OUTPOUT_PROCESSED = OUTPUT_SUM + "/processed"
OUTPOUT_STACK = OUTPUT_SUM + "/stack"

if lepton_collection:
    OUTPOUT_TYPE_SUM = "/tmp"
    SINGLE_OUTPUT = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/lc/single"
elif signal_ntuples:
    OUTPOUT_TYPE_SUM = "/tmp"
    SINGLE_OUTPUT = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/ntuples/single/"
    WORK_DIR = "/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/SignalNtuples/"
elif data_lepton_collection:
    OUTPOUT_TYPE_SUM = "/tmp"
    SINGLE_OUTPUT = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/lc/single"
    WORK_DIR = "/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/LeptonCollectionFilesMaps/"
else:
    if not os.path.isdir(OUTPUT_SUM):
        os.mkdir(OUTPUT_SUM)

    if not os.path.isdir(OUTPOUT_TYPE_SUM):
        os.mkdir(OUTPOUT_TYPE_SUM)
    if not skim:
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


#def system(command):
#    print "Just Performing: " + command

# Add the histograms
if hadd or all:
    print "Adding histograms."
    fileList = glob(SINGLE_OUTPUT + "/*");
    
    if data_lepton_collection:
        files_glob = fileList
        
        file = "Run2016_SingleMuon.root"
        tmp_dir = "/afs/desy.de/user/n/nissanuv/nfs"
        #file = "Run2016_MET.root"
        print "***NUMBER:" + str(len(files_glob))
        #print files_glob
        print "Checking " + WORK_DIR + "/" + os.path.basename(file)
        if os.path.exists(WORK_DIR + "/" + os.path.basename(file)):
            print "File " + WORK_DIR + "/" + os.path.basename(file) + " exists..."
            exit(1)
    
        command = "./merge_lepton_collection_map.py -o " + tmp_dir + "/" + file + " -i " + SINGLE_OUTPUT + "/*"
        print "Perorming:", command 
        system(command)
        command = "gfal-copy " + tmp_dir + "/" + file + " " + "srm://dcache-se-cms.desy.de" + WORK_DIR
        print "Perorming:", command 
        system(command)
        command = "rm " + tmp_dir + "/" + file
        print "Perorming:", command 
        system(command)
    else:
        for f in fileList :
            filename = None
            if bg:
                filename = os.path.basename(f).split(".")[1]
            else:
                filename = os.path.basename(f).split(".")[0]
            if "MET" in filename:
                continue
            types = filename.split("_")
            type = types[0]
            if signal_ntuples:
                type = types[0] + "_" + types[1] + "_" + types[2]
            if type not in sumTypes:
                sumTypes[type] = {}
            if bg:
                #if type == "DYJetsToLL" or type == "ST":
                #if type == "TT":
                #    sumTypes[type][types[1]] = True
                #else:
                types[2] = types[2].split("AOD")[0]
                sumTypes[type][types[1] + "_" + types[2]] = True
                #else:
                #    sumTypes[type][types[1]] = True

        print sumTypes 

        for type in sumTypes:
            print type
            if bg:
                for typeRange in sumTypes[type]:
                    print "-----"
                    print typeRange
                    print "-----"
                    #continue
                    command = None
                    file = ""
                    files = ""
                    if "M-5to50" in typeRange:
                        #command = "/afs/desy.de/user/n/nissanuv/cms-tools/analysis/scripts/ahadd.py -f " + OUTPOUT_TYPE_SUM + "/" + type + "_" + typeRange + ".root " + SINGLE_OUTPUT + "/RunIISummer16MiniAODv3." + type + "_*" + typeRange + "*.root"
                        file = OUTPOUT_TYPE_SUM + "/" + type + "_" + typeRange + ".root"
                        if lepton_collection:
                            files = SINGLE_OUTPUT + "/Summer16*." + type + "_*" + typeRange + "*.root"
                        else:
                            files = SINGLE_OUTPUT + "/RunIISummer16MiniAODv3." + type + "_*" + typeRange + "*.root"
                        command = "hadd -f " + file + " " + files
                    else:
                        file = OUTPOUT_TYPE_SUM + "/" + type + "_" + typeRange + ".root"
                        files = SINGLE_OUTPUT + "/Summer16*." + type + "_" + typeRange + "*.root"
                        command = "hadd -f " + file + " " + files
                    if lepton_collection:
                        #command = "mkdir tmp"
                        #print "Perorming:", command 
                        #system(command)
                        #command = "gfal-copy -f srm://dcache-se-cms.desy.de/" + files + " ./tmp/"
                        #print "Perorming:", command 
                        #system(command)
                        print files
                        files_glob = glob(files)
                        print "***NUMBER:" + str(len(files_glob)) + " " + type + "_" + typeRange
                        #print files_glob
                        print "Checking " + WORK_DIR + "/" + os.path.basename(file)
                        if os.path.exists(WORK_DIR + "/" + os.path.basename(file)):
                            print "File " + WORK_DIR + "/" + os.path.basename(file) + " exists..."
                            continue
                    
                        command = "./merge_lepton_collection_map.py -o " + file + " -i " + files
                        print "Perorming:", command 
                        system(command)
                        command = "gfal-copy -f " + file + " " + "srm://dcache-se-cms.desy.de" + WORK_DIR
                        print "Perorming:", command 
                        system(command)
                        command = "rm -rf ./tmp"
                        print "Perorming:", command 
                        system(command)
                    else:
                        if os.path.exists(file):
                            print "File", file, " exists. Skipping"
                        else:
                            print "Perorming:", command 
                            system(command)
                    
            elif signal_ntuples:          
                print "-------"
                command = "hadd -f " + OUTPOUT_TYPE_SUM + "/" + type + "_1.root " + SINGLE_OUTPUT + "/" + type + "_*.root"
                print "Perorming:", command
                system(command)
                command = "gfal-copy " + OUTPOUT_TYPE_SUM + "/" + type + "_1.root " + " srm://dcache-se-cms.desy.de" + WORK_DIR
                print "Perorming:", command
                system(command)
                command = "rm " + OUTPOUT_TYPE_SUM + "/" + type + "_1.root "
                print "Perorming:", command
                system(command)
            else:
                command = "hadd -f " + OUTPOUT_TYPE_SUM + "/" + type + ".root " + SINGLE_OUTPUT + "/" + type + "_*.root"
                print "Perorming:", command 
                #system(command)

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
