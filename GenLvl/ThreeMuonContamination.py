#!/usr/bin/env python3.8
from ROOT import *
import sys
import os
from glob import glob
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib/classes"))
# from lib import utils
# from lib import analysis_ntuples
# from lib import analysis_tools
# from lib import analysis_observables
from lib import plot_params_stops_bg_vs_signal
import cppyy
import argparse 
import matplotlib.pyplot as plt
import numpy 
import csv


histogram_dir = "/afs/desy.de/user/d/diepholq/CMSSW_11_3_1/src/stops/analysis/scripts/histograms_root_files/"   #loading hists from root file
root_file = histogram_dir + "stops_bg_vs_signal_Iso_NSelectionMuons.root"
def loadHistograms():
    nFile = TFile(root_file, "read")
    keys = nFile.GetListOfKeys()
    keynames = []
    histograms = []
    for key in keys:
        name = key.GetName()#histogram name
        keynames.append(name)
        h = nFile.Get(name)
        h.SetDirectory(0)
        h.UseCurrentStyle()
        #histograms[name] = h
        histograms.append(h)
    nFile.Close()
    return  keynames, histograms
keynames, histograms = loadHistograms()
#print(keynames)


def calculate_efficiencies():
    contaminations = {}
    for i in range(len(keynames)):
        print(keynames[i])
        signal_point_name = keynames[i].split("_")
        print(signal_point_name)
        stop_mass = signal_point_name[5].split("G")[0]
        chipm_mass = signal_point_name[6].split("G")[0].split("pm")[1]
        mass_splitting = signal_point_name[7].split("m")[1].split("G")[0]
        signal_point = stop_mass + "_" + chipm_mass + "_" + mass_splitting
        print("Number of Bins:",histograms[i].GetNbinsX())
        number_of_bins = histograms[i].GetNbinsX()
        twos = histograms[i].GetBinContent(3)
        threes = histograms[i].GetBinContent(4)
        contaminations.update({signal_point: [threes/(threes+twos)] })

    return contaminations
    

efficiencies = calculate_efficiencies()

dm0p6 = {}
dm1p0 = {}
dm1p4 = {}

for key in efficiencies:
    signal_point_characteristics = key.split("_")
    if signal_point_characteristics[2] == "0p6":
        dm_key = signal_point_characteristics[0] + "_" + signal_point_characteristics[1]
        dm0p6.update({dm_key: efficiencies[key]})
    if signal_point_characteristics[2] == "1p0":
        dm1p0.update({signal_point_characteristics[0] + "_" + signal_point_characteristics[1]: efficiencies[key]})
    if signal_point_characteristics[2] == "1p4":
        dm1p4.update({signal_point_characteristics[0] + "_" + signal_point_characteristics[1]: efficiencies[key]})

csv_file = open("ThreeMuonContamination.csv","w")
csvwriter = csv.writer(csv_file)
for dm in [dm0p6,dm1p0,dm1p4]:
    for key in dm:
        row = [*key.split("_"), *dm[key]]
        csvwriter.writerow(row)