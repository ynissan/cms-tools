#!/usr/bin/env python3.8

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import numpy as np
import os
import cppyy
import itertools
from datetime import datetime

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib/classes"))
from lib import analysis_ntuples
from lib import analysis_tools
from lib import utils
from lib import analysis_observables

# gSystem.Load('LumiSectMap_C')
# from ROOT import LumiSectMap
# 
# gSystem.Load('LeptonCollectionMap_C')
# from ROOT import LeptonCollectionMap
# from ROOT import LeptonCollectionFilesMap
# from ROOT import LeptonCollection


#def chunker(iterable, chunksize):
#    return zip(*[iter(iterable)] * chunksize)
 
def chunker_longest(iterable, chunksize):
    return itertools.zip_longest(*[iter(iterable)] * chunksize)


#for chunk in chunker_longest(range(101), 11):
#    print(chunk)
    

# print(["bla"]*5)
# 
# elementsList = range(101)
# print(elementsList)
# print(*[iter(elementsList)]*5)
# bla = itertools.zip_longest(*([iter(elementsList)] * 5))
# for chunk in bla:
#     
#     print(chunk)

parser = argparse.ArgumentParser(description='Sum histograms and trees.')
parser.add_argument("-phase1", "--phase1", dest='phase1', help='2017 Background', action='store_true')
args = parser.parse_args()

phase1 = args.phase1
print("phase1", phase1)

WORK_DIR = "/afs/desy.de/user/d/diepholq/nfs/x1x2x1/bg/skim"
if phase1:
    WORK_DIR = "/afs/desy.de/user/d/diepholq/nfs/x1x2x1/bg/skim_phase1"
print("WORK_DIR", WORK_DIR)

SINGLE_OUTPUT = WORK_DIR + "/single"
INPUT_SUM = WORK_DIR + "/sum/input"
OUTPUT_SUM = WORK_DIR + "/sum"

OUTPOUT_TYPE_SUM = OUTPUT_SUM + "/type_sum"

OUTPUT_SUM_OUTPUT = OUTPUT_SUM + "/stdout"
OUTPUT_SUM_ERROR = OUTPUT_SUM + "/stderr"

if not os.path.isdir(OUTPUT_SUM):
    os.mkdir(OUTPUT_SUM)

if not os.path.isdir(INPUT_SUM):
    os.mkdir(INPUT_SUM)

if not os.path.isdir(OUTPOUT_TYPE_SUM):
    os.mkdir(OUTPOUT_TYPE_SUM)

if not os.path.isdir(OUTPUT_SUM_OUTPUT):
    os.mkdir(OUTPUT_SUM_OUTPUT)

if not os.path.isdir(OUTPUT_SUM_ERROR):
    os.mkdir(OUTPUT_SUM_ERROR)

condor_wrapper = os.path.expandvars("$CMSSW_BASE/src/stops/analysis/scripts/condor_wrapper.sh")

sumTypes = {}

def getCompoundTypeFiles(cType):
    rootFiles = []
    for type in utils.compoundTypes[cType]:
        rootFiles.extend(glob(OUTPOUT_TYPE_SUM + "/*" + type + "*.root"))
    return rootFiles

file_num_per_type = {'QCD': {'HT500to700_TuneCUETP8M1': 7241, 'HT300to500_TuneCUETP8M1': 6042, 'HT700to1000_TuneCUETP8M1': 1422, 'HT200to300_TuneCUETP8M1': 4767, 'HT1000to1500_TuneCUETP8M1': 2087, 'HT1500to2000_TuneCUETP8M1': 1914, 'HT2000toInf_TuneCUETP8M1': 862}, 'WJetsToLNu': {'HT-800To1200_TuneCUETP8M1': 855, 'HT-200To400_TuneCUETP8M1': 2027, 'HT-1200To2500_TuneCUETP8M1': 885, 'HT-600To800_TuneCUETP8M1': 1819, 'TuneCUETP8M1_13TeV-madgraphMLM-pythia8': 1961, 'HT-400To600_TuneCUETP8M1': 820, 'HT-2500ToInf_TuneCUETP8M1': 215}, 'TTJets': {'SingleLeptFromTbar_TuneCUETP8M1': 6213, 'SingleLeptFromT_TuneCUETP8M1': 6863, 'DiLept_TuneCUETP8M1': 3291}, 'ST': {'t-channel_top': 6505, 't-channel_antitop': 2501}, 'ZJetsToNuNu': {'HT-200To400_13TeV-madgraph': 1092, 'HT-100To200_13TeV-madgraph': 1825, 'HT-400To600_13TeV-madgraph': 954, 'HT-800To1200_13TeV-madgraph': 221, 'HT-600To800_13TeV-madgraph': 224, 'HT-2500ToInf_13TeV-madgraph': 45, 'HT-1200To2500_13TeV-madgraph': 24}, 'DYJetsToLL': {'M-50_HT-400to600': 786, 'M-50_HT-600to800': 1360, 'M-50_HT-200to400': 909, 'M-50_HT-1200to2500': 103, 'M-50_TuneCUETP8M1': 4012, 'M-5to50_HT-70to100': 424, 'M-5to50_HT-200to400': 94, 'M-50_HT-800to1200': 357, 'M-50_HT-100to200': 890, 'M-50_HT-2500toInf': 62, 'M-5to50_HT-600toInf': 57, 'M-5to50_HT-100to200': 27, 'M-5to50_HT-400to600': 21}, 'WW': {'TuneCUETP8M1_13TeV-pythia8': 332}, 'WZ': {'TuneCUETP8M1_13TeV-pythia8': 395}, 'WWZ': {'TuneCUETP8M1_13TeV-amcatnlo-pythia8': 22}, 'WZZ': {'TuneCUETP8M1_13TeV-amcatnlo-pythia8': 38}, 'ZZ': {'TuneCUETP8M1_13TeV-pythia8': 141}, 'ZZZ': {'TuneCUETP8M1_13TeV-amcatnlo-pythia8': 35}}
print(("Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')))

condor_file="/tmp/condor_submut." + datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
print("condor submit file:", condor_file)

default_file_num = 10000

file_num_per_type = {
"DYJetsToLL_M-50_TuneCUETP8M1" : 10000,
"DYJetsToLL_M-50_HT-1200to2500" : 10000,
"DYJetsToLL_M-50_HT-200to400" : 10000,
"DYJetsToLL_M-50_HT-2500toInf" : 10000,
"DYJetsToLL_M-50_HT-400to600" : 10000,
"DYJetsToLL_M-50_HT-600to800" : 700,
"DYJetsToLL_M-50_HT-800to1200" : 10000,
"DYJetsToLL_M-50_HT-100to200" : 10000,
"DYJetsToLL_M-5to50_HT-100to200" : 10000,
"DYJetsToLL_M-5to50_HT-400to600" : 10000,
"DYJetsToLL_M-5to50_HT-600toInf" : 10000,
"DYJetsToLL_M-5to50_HT-70to100" : 10000,
"QCD_HT1000to1500_TuneCUETP8M1" : 10000,
"QCD_HT1500to2000_TuneCUETP8M1" : 2000,
"QCD_HT2000toInf_TuneCUETP8M1" : 10000,
"QCD_HT200to300_TuneCUETP8M1" : 10000,
"QCD_HT500to700_TuneCUETP8M1" : 10000,
"QCD_HT700to1000_TuneCUETP8M1" : 10000,
"ST_t-channel_antitop" : 10000,
"ST_t-channel_top" : 1900,
"TTJets_DiLept_TuneCUETP8M1" : 514,
"TTJets_SingleLeptFromT_TuneCUETP8M1" : 620,
"TTJets_SingleLeptFromTbar_TuneCUETP8M1" : 530, #910
"WJetsToLNu_HT-1200To2500_TuneCUETP8M1" : 500, #10
"WJetsToLNu_HT-200To400_TuneCUETP8M1" : 1170, #10
"WJetsToLNu_HT-2500ToInf_TuneCUETP8M1" : 10000,#10
"WJetsToLNu_HT-400To600_TuneCUETP8M1" : 500, #10
"WJetsToLNu_HT-600To800_TuneCUETP8M1" : 600, #10
"WJetsToLNu_HT-800To1200_TuneCUETP8M1" : 500, #10
"WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8" : 10000, #200
"ZJetsToNuNu_HT-100To200_13TeV-madgraph" : 10000, #20
"ZJetsToNuNu_HT-200To400_13TeV-madgraph" : 10000,#20?
"ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph" : 10000, #20
"ZJetsToNuNu_HT-400To600_13TeV-madgraph" :500, #10
"ZJetsToNuNu_HT-600To800_13TeV-madgraph" : 10000, #20
"ZJetsToNuNu_HT-800To1200_13TeV-madgraph" : 10000, #10
"ZJetsToNuNu_HT-1200To2500_13TeV-madgraph" : 10000, #20
"ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8" : 10000,
"ZZ_TuneCUETP8M1_13TeV-pythia8" : 10000,
"ZZ_TuneCUETP8M1_13TeV-pythia8" : 10000,
"WW_TuneCUETP8M1_13TeV-pythia8" : 10000, #50
}


file_num_per_type_phase1 = {
 "DYJetsToLL_M-50_HT-1200to2500" : 300, #30
 "DYJetsToLL_M-50_HT-200to400" : 3000, #30
 "DYJetsToLL_M-50_HT-2500toInf" : 45,
 "DYJetsToLL_M-50_HT-400to600" : 2000, #20
 "DYJetsToLL_M-50_HT-600to800" : 2000, #20
 "DYJetsToLL_M-50_HT-800to1200" : 200, #20
 "DYJetsToLL_M-50_TuneCP5" : 4000, #40
 "QCD_HT1500to2000_TuneCP5" : 500, #30
 "QCD_HT2000toInf_TuneCP5" : 500, #30
 "QCD_HT200to300_TuneCP5" : 30000, #300
 "QCD_HT500to700_TuneCP5" : 20000, #200
 "TTJets_DiLept_TuneCP5" : 350, #20
 "TTJets_SingleLeptFromT_TuneCP5" : 300, #30
 "TTJets_SingleLeptFromTbar_TuneCP5" : 360, #30
 "WJetsToLNu_HT-100To200_TuneCP5" : 100000, #30
 "WJetsToLNu_HT-1200To2500_TuneCP5" : 200, #10
 "WJetsToLNu_HT-200To400_TuneCP5" : 500, #20
 "WJetsToLNu_HT-2500ToInf_TuneCP5" : 180, #10
 "WJetsToLNu_HT-400To600_TuneCP5" : 400, #10
 "WJetsToLNu_HT-600To800_TuneCP5" : 400, #10
 "WJetsToLNu_HT-800To1200_TuneCP5" : 350, #10
 "WWTo1L1Nu2Q_13TeV_amcatnloFXFX" : 550, #30
 "WZTo1L1Nu2Q_13TeV_amcatnloFXFX" : 550, #30
 "WZTo1L3Nu_13TeV_amcatnloFXFX" : 3000, #30
 "ZJetsToNuNu_HT-200To400_13TeV-madgraph" : 1000, #30
 "ZJetsToNuNu_HT-400To600_13TeV-madgraph" : 550, #30
 "ZJetsToNuNu_HT-600To800_13TeV-madgraph" : 550, #30
 "ZJetsToNuNu_HT-800To1200_13TeV-madgraph" : 550, #30
}
 
def main():
    
    condor_f = open(condor_file,'w')
    condor_f.write('''
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
''')
    
    print("Adding histograms.")
    fileList = glob(SINGLE_OUTPUT + "/*");
    totalFiles = 0
    
    for f in fileList:
        filename = os.path.basename(f).split(".")[1]
        totalFiles += 1

        types = filename.split("_")
#         print("types", types)
        type = types[0]
        
        if type not in sumTypes:
            sumTypes[type] = {}
        
            #if type == "DYJetsToLL" or type == "ST":
            #if type == "TT":
            #    sumTypes[type][types[1]] = True
            #else:
            #print(types)
        types[2] = types[2].split("AOD")[0]
        if types[1] + "_" + types[2] not in sumTypes[type]:
            sumTypes[type][types[1] + "_" + types[2]] = 1
        else:
            sumTypes[type][types[1] + "_" + types[2]] += 1
    print("totalFiles:", totalFiles)
    print("sumTypes:",sumTypes)
    for type in sumTypes:
        for typeRange in sumTypes[type]:
            print("\n\n\n\n\n-----")
            print(type, typeRange)
            print("-----")
            #continue
            command = None
            base_file = ""
            files = []
            
            if "M-5to50" in typeRange:
                #command = "/afs/desy.de/user/n/nissanuv/cms-tools/analysis/scripts/ahadd.py -f " + OUTPOUT_TYPE_SUM + "/" + type + "_" + typeRange + ".root " + SINGLE_OUTPUT + "/RunIISummer16MiniAODv3." + type + "_*" + typeRange + "*.root"
                base_file = type + "_" + typeRange 
                files = sorted(glob(SINGLE_OUTPUT + "/RunIISummer16MiniAODv3." + type + "_*" + typeRange + "*.root"))
                #command = "hadd -f " + file + " " + files
            else:
                base_file = type + "_" + typeRange
                prefix = "Summer16*."
                if phase1:
                    prefix = "RunIIFall17MiniAODv2."
                files = sorted(glob(SINGLE_OUTPUT + "/" + prefix + type + "_" + typeRange + "*.root"))
                #command = "hadd -f " + file + " " + files
            
            # print(["bla"]*5)
            # 
            # elementsList = range(101)
            # print(elementsList)
            # print(*[iter(elementsList)]*5)
            # bla = itertools.zip_longest(*([iter(elementsList)] * 5))
            # for chunk in bla:
            #     
            #     print(chunk)
            
            first_file = OUTPOUT_TYPE_SUM + "/" + base_file + "_" + str(1) + ".root"
            if os.path.exists(first_file):
                print("File", first_file, " exists. Skipping")
                continue
                
            i = 1

            chunk_size = default_file_num
            if phase1:
                if base_file in file_num_per_type_phase1:
                    chunk_size = file_num_per_type_phase1[base_file]
                else:
                    print("Don't have chunk_size for",base_file)
            else:
                if base_file in file_num_per_type:
                    chunk_size = file_num_per_type[base_file]
                else:
                    print("Don't have chunk_size for",base_file)
            
            for chunk in chunker_longest(files, chunk_size):
                output_file = OUTPOUT_TYPE_SUM + "/" + base_file + "_" + str(i) + ".root"
                if os.path.exists(output_file):
                    print("File", output_file, " exists. Skipping")
                    break
                else:
                    files_list = " ".join([f for f in chunk if f is not None])
                    command = "hadd -f " + output_file + " " + files_list
                    input_file = open(INPUT_SUM+"/"+type+"_"+typeRange+"_"+str(i)+".sh",'w')
                    input_file.write("#!/bin/sh" + "\n")
                    input_file.write(command + "\n")

                    input_file.close()
                    input_file_path = INPUT_SUM+"/"+type+"_"+typeRange+"_"+str(i)+".sh"
                    os.chmod(input_file_path, 0o755)
                    #print("Performing:", command)
                    
                    #system(command)
                    #condor_f.write("arguments = " + condor_wrapper + " " + command + "\n")
                    condor_f.write("arguments = " + condor_wrapper + " " + input_file_path +"\n")
                    condor_f.write("error = " + OUTPUT_SUM_ERROR + "/" + base_file + "_" + str(i) + ".err" + "\n")
                    condor_f.write("output = " + OUTPUT_SUM_OUTPUT + "/" + base_file + "_" + str(i) + ".out" + "\n")
                    condor_f.write("Queue\n")
                    
                    i += 1
    condor_f.close()
    system("condor_submit " + condor_file)
main()

exit(0)
