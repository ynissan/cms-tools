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



histogram_dir = "/afs/desy.de/user/d/diepholq/CMSSW_11_3_1/src/stops/analysis/scripts/histograms_root_files/"   #File with all signals and all bg
#bg_retag_all_file = histogram_dir + "bg_retag_all_2.root"
#bg_retag_all_file = histogram_dir + "stops_control_region.root"                #File with data control region plots, not actually bg retag all 
root_file = histogram_dir + "stops_unblinding.root"
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


# print("reading file"
# nFile = TFile(bg_retag_all_file, "read")
# print("read file")
# hist_keys = nFile.GetListOfKeys()
keynames, histograms = loadHistograms()
#print(keynames)
# bdt_custom_dilepBDTCorrJetNoMultIso15Dr0.4_higgsino_Summer16_stopstop_800GeV_mChipm200GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root

#exit()

def calculate_efficiencies(calculation_type = "sosobs"):
    efficiencies = {
    }
    print("starting calculation")
    for i in range(len(keynames)):
        signal_point_name = keynames[i].split("_")
        if len(signal_point_name) < 12:
            continue
            print("wha")
        stop_mass = signal_point_name[6].split("G")[0]
        chipm_mass = signal_point_name[7].split("G")[0].split("pm")[1]
        mass_splitting = signal_point_name[8].split("m")[1].split("G")[0]
        signal_point = stop_mass + "_" + chipm_mass + "_" + mass_splitting
        print(signal_point)
        if calculation_type == "sosobs":                                                         #s/sqrt(b+eb^2)
            sosobs = [] #first entry = first signal region (0.3-1),last entry is squared eff.
            print("Number of Bins:",histograms[i].GetNbinsX())
            number_of_bins = histograms[i].GetNbinsX()
           #  for bin_nr in range(1,number_of_bins+1):                                              #richtig bis hier
#                 print(bin_nr,histograms[i].GetBinContent(bin_nr))
            s = []
            b = []
            for bin_nr in [15,14,13]:
                bin_signal = histograms[i].GetBinContent(bin_nr)
                s.append(bin_signal)
                bin_background = histograms[len(histograms)-1].GetBinContent(bin_nr)
                b.append(bin_background)
                bin_berr = histograms[len(histograms)-1].GetBinError(bin_nr)
                sosobs.append(bin_signal/((bin_background+bin_berr**2)**(1/2)))
            sosobs.append((sosobs[0]**2+sosobs[1]**2+sosobs[2]**2)**(1/2))
            efficiencies.update({signal_point: sosobs})
#             efficiencies.update({signal_point: [*s,*b]})
#             print(bin_signal,bin_background)
        if calculation_type == "sososabs":                                                      #s/sqrt(s+b+eb^2)
            sososabs = [] 
            for bin_nr in [15,14,13]:
                s = histograms[i].GetBinContent(bin_nr)
                b = histograms[len(histograms)-1].GetBinContent(bin_nr)
                b_err = histograms[len(histograms)-1].GetBinError(bin_nr)
                sososabs.append(numpy.round(s/((s + b + b_err**2)**(1/2)),6))
                # print("s:",s)
#                 print("b:",b)
#                 print("s/sqrt(b+b_err**2)",s/numpy.sqrt(b+b_err**2))
#                 print("s/sqrt(s+b+b_err**2)",s/numpy.sqrt(s+b+b_err**2))
#                 print("s/((s + b + b_err**2)**(1/2))",s/((s + b + b_err**2)**(1/2)))
            sososabs.append(numpy.round((sososabs[0]**2+sososabs[1]**2+sososabs[2]**2)**(1/2),6))
#             print("sososabs (Liste)",sososabs,"\n")
            efficiencies.update({signal_point: sososabs})
    return efficiencies
    
    
    
    
def calculate_significance_unblinding():
    significances = {}
    for i in range(len(keynames)):
        if keynames[i] == "unblinding_custom_dilepBDTCorrJetNoMultIso15Dr0.4_data":
            data_idx = i
            print("data_idx", data_idx)
        if keynames[i] == "unblinding_custom_dilepBDTCorrJetNoMultIso15Dr0.4_all":
            bg_idx = i
            print("bg_idx", bg_idx)
        number_of_bins = histograms[i].GetNbinsX()
    sosob = []
    for bin_nr in [15,14,13]:
        data = histograms[data_idx].GetBinContent(bin_nr)
        data_err = histograms[data_idx].GetBinError(bin_nr)
        print("data", data)
        background = histograms[bg_idx].GetBinContent(bin_nr)
        print("background", background)
        background_err = histograms[bg_idx].GetBinError(bin_nr)
        print("background_err", background_err)
        sosob.append([(data-background)/((background+background_err**2+0.3**2)**(1/2)),data,data_err,background,(background_err**2+0.3**2)**(1/2)])
    return sosob
        
        
        
        
def calculate_signal_contamination():
    contaminations = {
    }
    for i in range(len(keynames)):
        signal_point_name = keynames[i].split("_")
        if len(signal_point_name) < 12:
            continue
        stop_mass = signal_point_name[6].split("G")[0]
        chipm_mass = signal_point_name[7].split("G")[0].split("pm")[1]
        mass_splitting = signal_point_name[8].split("m")[1].split("G")[0]
        signal_point = stop_mass + "_" + chipm_mass + "_" + mass_splitting

        signal_contamination = []   
        bin_signal = 0  
        bin_background = 0                                         
        for bin_nr in [1,2,3,4,5,6,7,8,9]:                              #< -0.1: 1-9, < -0.1: 1-8
            bin_signal += histograms[i].GetBinContent(bin_nr)
            bin_background += histograms[len(histograms)-1].GetBinContent(bin_nr)
            # print(bin_nr)
#             print(bin_signal)
#             print(bin_background,"\n")
        signal_contamination.append(bin_signal/(bin_signal+bin_background))
        contaminations.update({signal_point: signal_contamination})
    return contaminations




def calculate_tautau_contamination():
    contaminations = {
    }
    bin_jetty = 0  
    bin_tautau = 0
    for i in range(len(keynames)):                          #select right keys
        keyname = keynames[i].split("_")
        if keyname[2] != "without":
            bg_type = keyname[len(keyname)-1]
            if bg_type == "data":
                continue
        else:
            continue
        print(keynames[i])
        tautau_contamination = []                                   
        for bin_nr in [0,1,2,3,4,5,6,7,8,9]:
            if bg_type == "jetty":
                bin_jetty += histograms[i].GetBinContent(bin_nr)
            if bg_type == "tautau":
                bin_tautau += histograms[i].GetBinContent(bin_nr)
    contaminations.update({"tautau contamination": bin_tautau/(bin_tautau+bin_jetty)})
    return contaminations
    



#######################         Running Stuff          ####################################

# for method in ["sosobs","sososabs"]:
#     efficiencies = calculate_efficiencies(method)
#     for key in efficiencies:
#         print(key,",",efficiencies[key],"\n")

# print(efficiencies)
efficiencies = calculate_efficiencies("sosobs")
# print(efficiencies)
# efficiencies = calculate_signal_contamination()
#contaminations = calculate_signal_contamination()
# contaminations = calculate_tautau_contamination()
# print("without tautau cut:", contaminations)
# exit()
# print(contaminations)
# for key in contaminations:
#     print(key,",",contaminations[key],"\n")


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
# 
csv_file = open("efficiencies_file.csv","w")
csvwriter = csv.writer(csv_file)
for dm in [dm0p6,dm1p0,dm1p4]:
    for key in dm:
        row = [*key.split("_"), *dm[key]]
        csvwriter.writerow(row)
        #print(*key.split("_"), *dm[key])



######################## UNBLINDING #########################
# unblinding_significances = calculate_significance_unblinding()
# print(unblinding_significances)
# 
# csv_file = open("unblinding_significances.csv","w")
# csvwriter = csv.writer(csv_file)
# for sr in range(3):
#     csvwriter.writerow(unblinding_significances[sr])



