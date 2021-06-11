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
import numpy as np

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes"))
import utils
import analysis_ntuples
import plot_params
# 
gROOT.SetBatch(True)
gStyle.SetOptStat(0)

#lumi = 5746.370
#weight = lumi / utils.LUMINOSITY

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Plot Scale Factors.')
args = parser.parse_args()

def setMarkers(hist, colorI):
    lineC = TColor.GetColor(utils.colorPalette[colorI]["fillColor"])
    hist.SetMarkerColorAlpha(lineC, 1)
    hist.SetMarkerStyle(utils.colorPalette[colorI]["markerStyle"])
    hist.SetLineColor(lineC)

###########

# MC
#bug
#mc_fit_only_signal_integral = {'iso_invMass_0.5_1.5_1.2_2.4': 825.219292705425, 'id_invMass_0.5_1.5_1.2_2.4': 1212.1687119672215, 'invMass_0.5_1.5_1.2_2.4': 1358.406309204982, 'invMass_0_0.3_1.2_2.4': 1242.226444810194, 'iso_invMass_0.5_1.5_0_1.2': 461.36020807635174, 'id_invMass_0.3_0.5_1.2_2.4': 1869.6891945787622, 'id_invMass_0_0.3_1.2_2.4': 1229.4838834581765, 'invMass_0_0.3_0_1.2': 1483.3740144458595, 'iso_invMass_0_0.3_0_1.2': 173.28446536748194, 'iso_invMass_0.3_0.5_0_1.2': 957.2732884322727, 'iso_invMass_0.3_0.5_1.2_2.4': 666.4988849989352, 'invMass_0.3_0.5_1.2_2.4': 1939.5115403864093, 'id_invMass_0.3_0.5_0_1.2': 2320.3756245960435, 'id_invMass_0_0.3_0_1.2': 1448.074028176608, 'invMass_0.3_0.5_0_1.2': 2809.8449325753577, 'invMass_0.5_1.5_0_1.2': 1826.1968582152037, 'id_invMass_0.5_1.5_0_1.2': 647.6770198075196, 'iso_invMass_0_0.3_1.2_2.4': 123.94422036049698}
#mc_fit_only_signal_integral_error = {'iso_invMass_0.5_1.5_1.2_2.4': 30.96583590374441, 'id_invMass_0.5_1.5_1.2_2.4': 37.5186886655028, 'invMass_0.5_1.5_1.2_2.4': 39.61013943844631, 'invMass_0_0.3_1.2_2.4': 37.31234936135069, 'iso_invMass_0.5_1.5_0_1.2': 23.04316280301899, 'id_invMass_0.3_0.5_1.2_2.4': 45.944090278191155, 'id_invMass_0_0.3_1.2_2.4': 82.00324138643832, 'invMass_0_0.3_0_1.2': 40.88557132318864, 'iso_invMass_0_0.3_0_1.2': 13.976757801362941, 'iso_invMass_0.3_0.5_0_1.2': 34.05836533485333, 'iso_invMass_0.3_0.5_1.2_2.4': 27.602954686953893, 'invMass_0.3_0.5_1.2_2.4': 47.03570518813685, 'id_invMass_0.3_0.5_0_1.2': 52.46304074313171, 'id_invMass_0_0.3_0_1.2': 40.83007522430172, 'invMass_0.3_0.5_0_1.2': 57.481624288485655, 'invMass_0.5_1.5_0_1.2': 101.09391706753645, 'id_invMass_0.5_1.5_0_1.2': 27.320761224442467, 'iso_invMass_0_0.3_1.2_2.4': 11.796310216319814}

# with tag pt cut
#mc_fit_only_signal_integral = {'id_invMass_0.5_1.5_1.2_2.4': 1212.1687119672215, 'invMass_0.5_1.5_1.2_2.4': 1358.406309204982, 'invMass_0_0.3_1.2_2.4': 821.6956637002436, 'id_invMass_0.3_0.5_1.2_2.4': 1868.657930388279, 'id_invMass_0_0.3_1.2_2.4': 810.9217364791946, 'invMass_0.3_0.5_1.2_2.4': 1938.4495438015822, 'id_invMass_0.5_1.5_0_1.2': 650.4503351184957, 'id_invMass_0.3_0.5_0_1.2': 2318.8719501267933, 'id_invMass_0_0.3_0_1.2': 911.3413636946444, 'invMass_0.3_0.5_0_1.2': 2627.455015718407, 'invMass_0.5_1.5_0_1.2': 1000.3697043214511, 'invMass_0_0.3_0_1.2': 934.2441158894381}
#mc_fit_only_signal_integral_error = {'id_invMass_0.5_1.5_1.2_2.4': 37.5186886655028, 'invMass_0.5_1.5_1.2_2.4': 39.61013943844631, 'invMass_0_0.3_1.2_2.4': 30.097902146385984, 'id_invMass_0.3_0.5_1.2_2.4': 45.93634675328968, 'id_invMass_0_0.3_1.2_2.4': 29.82929480062246, 'invMass_0.3_0.5_1.2_2.4': 47.02373404751074, 'id_invMass_0.5_1.5_0_1.2': 27.330029387981142, 'id_invMass_0.3_0.5_0_1.2': 52.44334532340869, 'id_invMass_0_0.3_0_1.2': 32.11839991265201, 'invMass_0.3_0.5_0_1.2': 55.79300940418125, 'invMass_0.5_1.5_0_1.2': 33.9178157528494, 'invMass_0_0.3_0_1.2': 62.80470199116078}
#no tag pt cut
mc_fit_only_signal_integral = {'id_invMass_0.5_1.5_1.2_2.4': 1212.1687119672215, 'invMass_0.5_1.5_1.2_2.4': 1358.406309204982, 'invMass_0_0.3_1.2_2.4': 1831.6961400372004, 'id_invMass_0.3_0.5_1.2_2.4': 2265.8721702322014, 'id_invMass_0_0.3_1.2_2.4': 1819.515546284128, 'invMass_0.3_0.5_1.2_2.4': 2410.85270409826, 'id_invMass_0.5_1.5_0_1.2': 650.4503351184957, 'id_invMass_0.3_0.5_0_1.2': 2451.8867549315078, 'id_invMass_0_0.3_0_1.2': 1723.8172742029271, 'invMass_0.3_0.5_0_1.2': 2888.1585358786956, 'invMass_0.5_1.5_0_1.2': 1000.3697043214511, 'invMass_0_0.3_0_1.2': 1780.106184603731}
mc_fit_only_signal_integral_error = {'id_invMass_0.5_1.5_1.2_2.4': 37.5186886655028, 'invMass_0.5_1.5_1.2_2.4': 39.61013943844631, 'invMass_0_0.3_1.2_2.4': 45.00060235563775, 'id_invMass_0.3_0.5_1.2_2.4': 50.468947998558455, 'id_invMass_0_0.3_1.2_2.4': 44.88956508039257, 'invMass_0.3_0.5_1.2_2.4': 52.289371912778655, 'id_invMass_0.5_1.5_0_1.2': 27.330029387981142, 'id_invMass_0.3_0.5_0_1.2': 53.85527175353975, 'id_invMass_0_0.3_0_1.2': 77.58256739016653, 'invMass_0.3_0.5_0_1.2': 119.74495320896493, 'invMass_0.5_1.5_0_1.2': 33.9178157528494, 'invMass_0_0.3_0_1.2': 45.17724566290194}
# DATA
#bug
#fit_signal_integral = {'iso_invMass_0.5_1.5_1.2_2.4': 1487.039013623537, 'id_invMass_0.5_1.5_1.2_2.4': 2417.1348680513106, 'invMass_0.5_1.5_1.2_2.4': 2946.105870762553, 'invMass_0_0.3_1.2_2.4': 13361.121188441017, 'iso_invMass_0.5_1.5_0_1.2': 740.7061324338875, 'id_invMass_0.3_0.5_1.2_2.4': 1990.6059714006255, 'id_invMass_0_0.3_1.2_2.4': 13230.737253066603, 'invMass_0_0.3_0_1.2': 18813.359822761304, 'iso_invMass_0_0.3_0_1.2': 9204.860185197495, 'iso_invMass_0.3_0.5_0_1.2': 1181.7145292217824, 'iso_invMass_0.3_0.5_1.2_2.4': 961.2923061974819, 'invMass_0.3_0.5_1.2_2.4': 2433.5159794996384, 'id_invMass_0.3_0.5_0_1.2': 2349.030408323999, 'id_invMass_0_0.3_0_1.2': 18565.892948701927, 'invMass_0.3_0.5_0_1.2': 2912.125833466333, 'invMass_0.5_1.5_0_1.2': 3556.0815233138983, 'id_invMass_0.5_1.5_0_1.2': 1202.5186603502073, 'iso_invMass_0_0.3_1.2_2.4': 4925.283450511285}
#fit_signal_integral_error = {'iso_invMass_0.5_1.5_1.2_2.4': 46.834467155316894, 'id_invMass_0.5_1.5_1.2_2.4': 55.321177678633525, 'invMass_0.5_1.5_1.2_2.4': 253.83280247238238, 'invMass_0_0.3_1.2_2.4': 234.39266904288584, 'iso_invMass_0.5_1.5_0_1.2': 29.25805903968685, 'id_invMass_0.3_0.5_1.2_2.4': 48.096531023307605, 'id_invMass_0_0.3_1.2_2.4': 229.4864743054384, 'invMass_0_0.3_0_1.2': 324.73868561441066, 'iso_invMass_0_0.3_0_1.2': 227.38872792097317, 'iso_invMass_0.3_0.5_0_1.2': 36.73974917119866, 'iso_invMass_0.3_0.5_1.2_2.4': 32.65579909265255, 'invMass_0.3_0.5_1.2_2.4': 123.8668816787346, 'id_invMass_0.3_0.5_0_1.2': 51.17251781849989, 'id_invMass_0_0.3_0_1.2': 294.68837537719486, 'invMass_0.3_0.5_0_1.2': 142.96290627536774, 'invMass_0.5_1.5_0_1.2': 181.69736546540437, 'id_invMass_0.5_1.5_0_1.2': 38.16540975739797, 'iso_invMass_0_0.3_1.2_2.4': 140.74484299702664}

# with tag pt cut
#fit_signal_integral = {'id_invMass_0.5_1.5_1.2_2.4': 2417.1348680513106, 'invMass_0.5_1.5_1.2_2.4': 2830.50236885607, 'invMass_0_0.3_1.2_2.4': 352.2424017979031, 'id_invMass_0.3_0.5_1.2_2.4': 1900.9174201701792, 'id_invMass_0_0.3_1.2_2.4': 309.97378872744827, 'invMass_0.3_0.5_1.2_2.4': 2314.971872700843, 'id_invMass_0.5_1.5_0_1.2': 1197.1534351629934, 'id_invMass_0.3_0.5_0_1.2': 2288.045423011509, 'id_invMass_0_0.3_0_1.2': 461.4623355053305, 'invMass_0.3_0.5_0_1.2': 2562.666195384524, 'invMass_0.5_1.5_0_1.2': 2051.503491168046, 'invMass_0_0.3_0_1.2': 448.74722869516523}
#fit_signal_integral_error = {'id_invMass_0.5_1.5_1.2_2.4': 55.321177678633525, 'invMass_0.5_1.5_1.2_2.4': 256.36578052271733, 'invMass_0_0.3_1.2_2.4': 26.523775535732092, 'id_invMass_0.3_0.5_1.2_2.4': 47.24157140753381, 'id_invMass_0_0.3_1.2_2.4': 19.476603261445735, 'invMass_0.3_0.5_1.2_2.4': 111.70025660218654, 'id_invMass_0.5_1.5_0_1.2': 36.88406907979794, 'id_invMass_0.3_0.5_0_1.2': 51.85531570783529, 'id_invMass_0_0.3_0_1.2': 22.160287280059272, 'invMass_0.3_0.5_0_1.2': 133.8938630640998, 'invMass_0.5_1.5_0_1.2': 174.0917121609346, 'invMass_0_0.3_0_1.2': 29.887789816966873}

#no tag pt cut
fit_signal_integral = {'id_invMass_0.5_1.5_1.2_2.4': 2419.6890354634015, 'invMass_0.5_1.5_1.2_2.4': 2948.1972517173062, 'invMass_0_0.3_1.2_2.4': 37182.13466619498, 'id_invMass_0.3_0.5_1.2_2.4': 169070.61689098115, 'id_invMass_0_0.3_1.2_2.4': 35916.4859566633, 'invMass_0.3_0.5_1.2_2.4': 218773.98000676156, 'id_invMass_0.5_1.5_0_1.2': 1197.1534351629934, 'id_invMass_0.3_0.5_0_1.2': 60169.36890076794, 'id_invMass_0_0.3_0_1.2': 31907.685688333855, 'invMass_0.3_0.5_0_1.2': 121957.22529551818, 'invMass_0.5_1.5_0_1.2': 2051.503491168046, 'invMass_0_0.3_0_1.2': 33226.57711140616}
fit_signal_integral_error = {'id_invMass_0.5_1.5_1.2_2.4': 54.92785691399385, 'invMass_0.5_1.5_1.2_2.4': 455.08241564625945, 'invMass_0_0.3_1.2_2.4': 537.3346517353856, 'id_invMass_0.3_0.5_1.2_2.4': 428.4299225155758, 'id_invMass_0_0.3_1.2_2.4': 411.8338927752829, 'invMass_0.3_0.5_1.2_2.4': 1988.9315911380945, 'id_invMass_0.5_1.5_0_1.2': 36.88406907979794, 'id_invMass_0.3_0.5_0_1.2': 251.95905968926962, 'id_invMass_0_0.3_0_1.2': 195.1636660571641, 'invMass_0.3_0.5_0_1.2': 493.39899046313155, 'invMass_0.5_1.5_0_1.2': 174.0917121609346, 'invMass_0_0.3_0_1.2': 238.04213472322945}
###########

plot_stability = True
id_only = True

# region is barrel - endcaps
for region in (0,1):

    postfix = "_0_1.2"
    prefix = "endcaps" if region else "barrel"
    
    ranges = [0,0.3,0.5,1.5]
    
    if region == 1:
        postfix = "_1.2_2.4"


    bins = np.zeros(len(ranges),dtype=float)
    for i in range(len(ranges)):
        bins[i] = ranges[i]

    barrelHist = TH1F(prefix + "Hist", "", len(ranges)-1, bins)
    barrelHist.Sumw2()
    barrelHistDen = TH1F(prefix + "HistDen", "", len(ranges)-1, bins)
    barrelHistDen.Sumw2()
    #isoBarrelHist = TH1F(prefix + "IsolHist", "", len(ranges)-1, bins)
    #isoBarrelHist.Sumw2()

    
    dataBarrelHist = TH1F(prefix + "DataHist", "", len(ranges)-1, bins)
    dataBarrelHist.Sumw2()
    dataBarrelHistDen = TH1F(prefix + "DataHistDen", "", len(ranges)-1, bins)
    dataBarrelHistDen.Sumw2()
    #isoDataBarrelHist = TH1F(prefix + "IsoDataHist", "", len(ranges)-1, bins)
    #isoDataBarrelHist.Sumw2()
    

    c1 = TCanvas("c1", "c1", 800, 800)
    c1.SetLeftMargin(0.13)
    c1.SetRightMargin(0.02)
    c1.SetGridx()
    c1.SetGridy()

    legend = TLegend(.60,.40,.89,.60)
    legend.SetNColumns(1)
    legend.SetBorderSize(1)
    legend.SetFillStyle(0)

    ####### MC #########

    for pti in range(len(ranges)):
        if pti == len(ranges) - 1:
            continue
        pt1 = ranges[pti]
        pt2 = ranges[pti+1]

        obsBaseName = "invMass_"+str(pt1)+"_"+str(pt2)+postfix
        
        #isoBarrelHist.SetBinContent(pti+1, mc_fit_only_signal_integral["iso_" + obsBaseName])
        #isoBarrelHist.SetBinError(pti+1, mc_fit_only_signal_integral_error["iso_" + obsBaseName])
        
        barrelHist.SetBinContent(pti+1, mc_fit_only_signal_integral["id_" + obsBaseName])
        barrelHist.SetBinError(pti+1, mc_fit_only_signal_integral_error["id_" + obsBaseName])

        barrelHistDen.SetBinContent(pti+1, mc_fit_only_signal_integral[obsBaseName])
        barrelHistDen.SetBinError(pti+1, mc_fit_only_signal_integral_error[obsBaseName])

        ####### DATA #########
        
        #isoDataBarrelHist.SetBinContent(pti+1, fit_signal_integral["iso_" + obsBaseName])
        #isoDataBarrelHist.SetBinError(pti+1, fit_signal_integral_error["iso_" + obsBaseName])

        dataBarrelHist.SetBinContent(pti+1, fit_signal_integral["id_" + obsBaseName])
        dataBarrelHist.SetBinError(pti+1, fit_signal_integral_error["id_" + obsBaseName])

        dataBarrelHistDen.SetBinContent(pti+1, fit_signal_integral[obsBaseName])
        dataBarrelHistDen.SetBinError(pti+1, fit_signal_integral_error[obsBaseName])

    # isoBarrelHistFactor - iso/id
    # isoBarrelHist = iso/den
    # barrelHist = id/den
    #isoBarrelHistFactor = isoBarrelHist.Clone()
    #isoBarrelHistFactor.Divide(barrelHist.Clone())
    #isoBarrelHist.Divide(barrelHistDen)
    barrelHist.Divide(barrelHistDen)

    ####### DATA #########
    
    
    # isoDataBarrelHistFactor - iso/id
    # isoDataBarrelHist - iso/den
    # dataBarrelHist - id/den
    #isoDataBarrelHistFactor = isoDataBarrelHist.Clone()
    #isoDataBarrelHistFactor.Divide(dataBarrelHist.Clone())
    #isoDataBarrelHist.Divide(dataBarrelHistDen)
    dataBarrelHist.Divide(dataBarrelHistDen)
    
    if id_only:
        minimum = min(barrelHist.GetMinimum(), dataBarrelHist.GetMinimum())
        maximum = max(barrelHist.GetMaximum(), dataBarrelHist.GetMaximum())
    else:
    
        minimum = min(barrelHist.GetMinimum(), dataBarrelHist.GetMinimum(), isoDataBarrelHist.GetMinimum(), isoBarrelHist.GetMinimum(), isoBarrelHistFactor.GetMinimum(), isoDataBarrelHistFactor.GetMinimum())
        maximum = max(barrelHist.GetMaximum(), dataBarrelHist.GetMaximum(), isoDataBarrelHist.GetMaximum(), isoBarrelHist.GetMaximum(), isoBarrelHistFactor.GetMaximum(), isoDataBarrelHistFactor.GetMaximum())
    
    barrelHist.SetMinimum(minimum-0.1)
    barrelHist.SetMaximum(maximum+0.1)
    
    #Originally it was here isoBarrelHist formatted
    
    utils.formatHist(barrelHist, utils.colorPalette[14], 0, True, True)
    utils.histoStyler(barrelHist)
    #barrelHist.GetYaxis().SetTitleOffset(1.5)
    
    #isoBarrelHist.SetLineColor(kBlack)
    #isoBarrelHist.SetMarkerColor(kBlack)
    #isoBarrelHist.SetMarkerStyle(kOpenSquare)
    
    # isoBarrelHistFactor.SetLineColor(kBlue)
#     isoBarrelHistFactor.SetMarkerColor(kBlue)
#     isoBarrelHistFactor.SetMarkerStyle(kOpenSquare)
    
    barrelHist.SetLineColor(kRed)
    barrelHist.SetMarkerColor(kRed)
    barrelHist.SetMarkerStyle(kFullSquare)
    
    #isoDataBarrelHist.SetMarkerStyle(kFullCircle)
    #isoDataBarrelHist.SetLineColor(kBlack)
    
    dataBarrelHist.SetMarkerStyle(kFullCircle)
    dataBarrelHist.SetMarkerColor(kBlack)
    dataBarrelHist.SetLineColor(kBlack)
    
    # isoDataBarrelHistFactor.SetMarkerStyle(kFullCircle)
#     isoDataBarrelHistFactor.SetMarkerColor(kBlue)
#     isoDataBarrelHistFactor.SetLineColor(kBlue)
    
    isoLegend = TLegend(.76,.75,.97,.89)
    isoLegend.SetNColumns(1)
    isoLegend.SetBorderSize(1)
    isoLegend.SetFillStyle(0)
    
    utils.formatLegend(isoLegend)
    
    if id_only:
        isoLegend.AddEntry(barrelHist, "MC", 'p')
        isoLegend.AddEntry(dataBarrelHist, "Data", 'p')
    else:
        isoLegend.AddEntry(isoBarrelHist, "MC (iso)", 'p')
        isoLegend.AddEntry(isoDataBarrelHist, "Data (iso)", 'p')
        if plot_stability:
            isoLegend.AddEntry(barrelHist, "MC (id)", 'p')
            isoLegend.AddEntry(dataBarrelHist, "Data (id)", 'p')
            isoLegend.AddEntry(isoBarrelHistFactor, "MC (iso/ID)", 'p')
            isoLegend.AddEntry(isoDataBarrelHistFactor, "Data (iso/ID)", 'p')
        
    #legend.AddEntry(barrelHistHistCount, "Signal Count Efficiency", 'p')
    barrelHist.GetXaxis().SetTitle("\Delta_{}R")
    if region == 0:
        barrelHist.GetYaxis().SetTitle("barrel #varepsilon")
    else:
        barrelHist.GetYaxis().SetTitle("endcaps #varepsilon")
    #isoBarrelHist.GetYaxis().SetTitle("#varepsilon")
    
    barrelHist.Draw("p")
    dataBarrelHist.Draw("p same")
    if not id_only:
        isoBarrelHist.Draw("p")
        isoDataBarrelHist.Draw("p same")
        if plot_stability:
            isoBarrelHistFactor.Draw("p same")
            isoDataBarrelHistFactor.Draw("p same")
            barrelHist.Draw("p same")
            dataBarrelHist.Draw("p same")

    isoLegend.Draw("SAME")
    #utils.stamp_plot("22.9")
    utils.stamp_plot("", utils.StampStr.PRE, utils.StampCoor.ABOVE_PLOT, False)
    if id_only:
        if region == 0:
            c1.SaveAs("barrelDeltaRidOnlyNoTagCut.pdf")
        else:
            c1.SaveAs("endcapsDeltaRidOnlyNoTagCut.pdf")
    else:
        if region == 0:
            c1.SaveAs("barrelDeltaRisoNoTagCut.pdf")
        else:
            c1.SaveAs("endcapsDeltaRisoNoTagCut.pdf")
    
    #Scale Factors
    
    isoLegend = TLegend(.70,.75,.89,.88)
    isoLegend.SetNColumns(1)
    isoLegend.SetBorderSize(1)
    isoLegend.SetFillStyle(0)

    #isoDataBarrelHist.Divide(isoBarrelHist)
    #isoDataBarrelHistFactor.Divide(isoBarrelHistFactor)
    dataBarrelHist.Divide(barrelHist)
    # was isoDataBarrelHist
    utils.histoStyler(dataBarrelHist)
    #dataBarrelHist.GetYaxis().SetTitleOffset(1.5)
    utils.formatLegend(isoLegend)
    
    dataBarrelHist.GetXaxis().SetTitle("\Delta_{}R")
    if region == 0:
        dataBarrelHist.GetYaxis().SetTitle("barrel scale factors")
    else:
        dataBarrelHist.GetYaxis().SetTitle("endcaps scale factors")
    #isoDataBarrelHist.GetYaxis().SetTitle("scale factor")
    if not id_only:
        isoLegend.AddEntry(isoDataBarrelHist, "Isolation", 'p')
        isoLegend.AddEntry(isoDataBarrelHistFactor, "Isolation from ID", 'p')
    isoLegend.AddEntry(dataBarrelHist, "ID", 'p')
    
    dataBarrelHist
    if not id_only:
        isoDataBarrelHist.Draw("p")
        isoDataBarrelHistFactor.Draw("p same")
        dataBarrelHist.Draw("p same")
    else:
        dataBarrelHist.Draw("p")
    if not id_only:
        isoLegend.Draw("SAME")
    utils.stamp_plot("22.9")

    if region == 0:

        c1.SaveAs("barrelDeltaRisoScaleFactorsNoTagCut.pdf")
    else:

         c1.SaveAs("endcapsDeltaRisoScaleFactorsNoTagCut.pdf")
    
exit(0)