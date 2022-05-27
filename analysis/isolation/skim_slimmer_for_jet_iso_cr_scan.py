#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import os
import re
from datetime import datetime
import math

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib/classes"))
import utils
import analysis_ntuples

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Slim skims for jet iso scan..')
parser.add_argument('-s', '--signal', dest='signal', help='Signal', action='store_true')
parser.add_argument('-bg', '--background', dest='bg', help='Background', action='store_true')
parser.add_argument('-data', '--data', dest='data', help='Background', action='store_true')
args = parser.parse_args()

signal = args.signal
bg = args.bg
data = args.data

if not signal and not bg and not data:
    bg = True

signal_dir = None
bg_dir = None

base_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1"

if signal:
    input_dir = base_dir + "/signal/skim/single"
    output_dir = base_dir + "/signal/skim/slim"
    output_dir_stdout = base_dir + "/signal/skim/stdout"
    output_dir_stderr = base_dir + "/signal/skim/stderr"
elif bg:
    input_dir = base_dir + "/bg/skim/sum/type_sum"
    output_dir = base_dir + "/bg/skim/sum/slim"
    output_dir_stdout = base_dir + "/bg/skim/stdout"
    output_dir_stderr = base_dir + "/bg/skim/stderr"
else:
    input_dir = base_dir + "/data/skim/sum"
    output_dir = base_dir + "/data/skim/slim"
    output_dir_stdout = base_dir + "/data/skim/stdout"
    output_dir_stderr = base_dir + "/data/skim/stderr"

print "input_dir", input_dir
print "output_dir", output_dir
print "output_dir_stdout", output_dir_stdout
print "output_dir_stderr", output_dir_stderr

if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

if not os.path.isdir(output_dir_stdout):
    os.mkdir(output_dir_stdout)

if not os.path.isdir(output_dir_stdout):
    os.mkdir(output_dir_stdout)


######## END OF CMDLINE ARGUMENTS ########

condor_wrapper = os.path.expandvars("$CMSSW_BASE/src/cms-tools/analysis/scripts/condor_wrapper.sh")
slimmer_script = os.path.expandvars("$CMSSW_BASE/src/cms-tools/analysis/isolation/skim_slimmer_for_jet_iso_cr_scan_job.py")

def main():
    print "Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    condor_file="/tmp/condor_submut." + datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    print("condor submit file:", condor_file)
    
    condor_f = open(condor_file,'w')
    condor_f.write('''
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
''')
    
    files = glob(input_dir + "/*")
    #files= [input_dir+"/QCD_HT1500to2000_TuneCUETP8M1_16.root"]

    
    for filename in files:
        print "Opening", filename
        baseFileName = os.path.basename(filename)
        baseFileNameNoStem = '.'.join(os.path.basename(filename).split('.')[:-1])
        output_file = output_dir + "/" + baseFileName
        print "output_file", output_file
        
        if os.path.isfile(output_file):
            print "File exits. Skipping", output_file
            continue
        
        command = slimmer_script + " -i " + filename + " -o " + output_file
        print("Perorming:", command)
        
        #system(command)
        condor_f.write("arguments = " + condor_wrapper + " " + command + "\n")
        condor_f.write("error = " + output_dir_stderr + "/" + baseFileNameNoStem + "_slimmer.err\n")
        condor_f.write("output = " + output_dir_stdout + "/" + baseFileNameNoStem + "_slimmer.out\n")
        condor_f.write("Queue\n")
    
    condor_f.close()
    system("condor_submit " + condor_file)
    print "End: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
main()
exit(0)