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



hist_signal_integral = {'invMass_5_10_1.2_2.4': 1019.4852705001831, 'id_invMass_10_25_0_1.2': 1667.2375283241272, 'reco_invMass_2_3_0_1.2': 9.821751654148102, 'reco_invMass_10_25_1.2_2.4': 1443.9869174957275, 'invMass_2_3_0_1.2': 894.3325540423393, 'id_invMass_3_5_1.2_2.4': 735.1649420261383, 'id_invMass_2_3_1.2_2.4': 437.24313747882843, 'invMass_3_5_1.2_2.4': 779.504823923111, 'id_invMass_5_10_0_1.2': 1233.4039489626884, 'id_invMass_5_10_1.2_2.4': 999.937216758728, 'reco_invMass_3_5_0_1.2': 793.398924946785, 'invMass_3_5_0_1.2': 1127.6164858341217, 'reco_invMass_5_10_1.2_2.4': 1014.2677640914917, 'invMass_5_10_0_1.2': 1289.267138183117, 'id_invMass_2_3_0_1.2': 8.231943935155869, 'invMass_2_3_1.2_2.4': 554.1936163902283, 'id_invMass_3_5_0_1.2': 689.7469207048416, 'id_invMass_10_25_1.2_2.4': 1437.1604557037354, 'invMass_10_25_1.2_2.4': 1456.6303882598877, 'reco_invMass_2_3_1.2_2.4': 489.0612097978592, 'reco_invMass_3_5_1.2_2.4': 767.6232149600983, 'invMass_10_25_0_1.2': 1703.163152217865, 'reco_invMass_10_25_0_1.2': 1687.6839156150818, 'reco_invMass_5_10_0_1.2': 1262.0459811091423}
fit_only_signal_integral = {'invMass_5_10_1.2_2.4': 992.4753403522357, 'id_invMass_10_25_0_1.2': 1647.4060494474707, 'reco_invMass_2_3_0_1.2': 8.60762827279467, 'reco_invMass_10_25_1.2_2.4': 1399.078989389184, 'invMass_2_3_0_1.2': 864.2987783298386, 'id_invMass_3_5_1.2_2.4': 720.8718760960961, 'id_invMass_2_3_1.2_2.4': 424.24377182107645, 'invMass_3_5_1.2_2.4': 765.6608341948643, 'id_invMass_5_10_0_1.2': 1199.1477266877093, 'id_invMass_5_10_1.2_2.4': 971.4513311235709, 'reco_invMass_3_5_0_1.2': 784.63451648419, 'invMass_3_5_0_1.2': 1120.8097734590774, 'reco_invMass_5_10_1.2_2.4': 987.8827411877056, 'invMass_5_10_0_1.2': 1271.670479429922, 'id_invMass_2_3_0_1.2': 8.408071431347487, 'invMass_2_3_1.2_2.4': 544.694351031679, 'id_invMass_3_5_0_1.2': 681.5399885908722, 'id_invMass_10_25_1.2_2.4': 1393.9949629782311, 'invMass_10_25_1.2_2.4': 1411.6007851011402, 'reco_invMass_2_3_1.2_2.4': 477.848599981434, 'reco_invMass_3_5_1.2_2.4': 754.4303153600102, 'invMass_10_25_0_1.2': 1682.1977796215028, 'reco_invMass_10_25_0_1.2': 1667.6757997858504, 'reco_invMass_5_10_0_1.2': 1228.2255003954342}
fit_signal_integral = {'invMass_5_10_1.2_2.4': 1039.6807993890702, 'id_invMass_10_25_0_1.2': 1629.9117665819474, 'reco_invMass_2_3_0_1.2': 33.54176707967502, 'reco_invMass_10_25_1.2_2.4': 1375.5252104302408, 'invMass_2_3_0_1.2': 1484.1844977215258, 'id_invMass_3_5_1.2_2.4': 692.3371128715078, 'id_invMass_2_3_1.2_2.4': 456.2216576688991, 'invMass_3_5_1.2_2.4': 984.8468133701276, 'id_invMass_5_10_0_1.2': 1224.8713413300425, 'id_invMass_5_10_1.2_2.4': 972.7717708852805, 'reco_invMass_3_5_0_1.2': 793.6126705058125, 'invMass_3_5_0_1.2': 1256.5596046590754, 'reco_invMass_5_10_1.2_2.4': 986.6826763283965, 'invMass_5_10_0_1.2': 1487.0482516871007, 'id_invMass_2_3_0_1.2': 34.19613595374151, 'invMass_2_3_1.2_2.4': 562.6048245270454, 'id_invMass_3_5_0_1.2': 698.2236046746027, 'id_invMass_10_25_1.2_2.4': 1375.7941976978223, 'invMass_10_25_1.2_2.4': 1479.4022715502192, 'reco_invMass_2_3_1.2_2.4': 498.172995443117, 'reco_invMass_3_5_1.2_2.4': 707.4581423325429, 'invMass_10_25_0_1.2': 1756.3046365512205, 'reco_invMass_10_25_0_1.2': 1629.3225892413604, 'reco_invMass_5_10_0_1.2': 1253.0440049137048}


###########

# MC

mc_fit_only_signal_integral = {'id_invMass_20_25_0_1.2': 334.2070116896566, 'invMass_5_10_1.2_2.4': 843.9680150736652, 'id_invMass_10_20_0_1.2': 878.4176041308358, 'invMass_20_25_0_1.2': 341.8185362679077, 'invMass_3_4_0_1.2': 517.2559389283792, 'id_invMass_3_4_1.2_2.4': 320.5924439128414, 'invMass_4_5_1.2_2.4': 283.8783804472692, 'id_invMass_2_3_1.2_2.4': 302.80207629438996, 'id_invMass_4_5_0_1.2': 338.072692079381, 'id_invMass_20_25_1.2_2.4': 259.98947186941297, 'id_invMass_5_10_0_1.2': 1079.6989360766086, 'id_invMass_5_10_1.2_2.4': 828.7280539572467, 'invMass_10_20_0_1.2': 894.405793888353, 'invMass_20_25_1.2_2.4': 263.92990927784507, 'id_invMass_10_20_1.2_2.4': 697.0012242876369, 'invMass_2_3_1.2_2.4': 398.4394337057448, 'invMass_4_5_0_1.2': 411.85264535095223, 'id_invMass_3_4_0_1.2': 227.6695841006641, 'invMass_3_4_1.2_2.4': 345.5945007841578, 'id_invMass_4_5_1.2_2.4': 269.57315594838775, 'invMass_5_10_0_1.2': 1131.9408990629208, 'invMass_10_20_1.2_2.4': 708.0167290251296}
mc_fit_only_signal_integral_error = {'id_invMass_20_25_0_1.2': 19.844732379033964, 'invMass_5_10_1.2_2.4': 60.76359652797092, 'id_invMass_10_20_0_1.2': 31.812127760120678, 'invMass_20_25_0_1.2': 23.372845475876613, 'invMass_3_4_0_1.2': 47.31003588390368, 'id_invMass_3_4_1.2_2.4': 19.317231206933187, 'invMass_4_5_1.2_2.4': 34.71858762397694, 'id_invMass_2_3_1.2_2.4': 18.42594167690223, 'id_invMass_4_5_0_1.2': 19.943485612913715, 'id_invMass_20_25_1.2_2.4': 16.89670431354685, 'id_invMass_5_10_0_1.2': 86.85134944806285, 'id_invMass_5_10_1.2_2.4': 30.53891555858885, 'invMass_10_20_0_1.2': 31.171755238736147, 'invMass_20_25_1.2_2.4': 17.156935560363877, 'id_invMass_10_20_1.2_2.4': 28.06094885355605, 'invMass_2_3_1.2_2.4': 21.18464662966867, 'invMass_4_5_0_1.2': 21.969700388041534, 'id_invMass_3_4_0_1.2': 33.94254947689124, 'invMass_3_4_1.2_2.4': 19.97164295816518, 'id_invMass_4_5_1.2_2.4': 18.006366586998848, 'invMass_5_10_0_1.2': 85.57517777088567, 'invMass_10_20_1.2_2.4': 28.280846533820984}
mc_hist_count = {'id_invMass_20_25_0_1.2': 344.23969680070877, 'invMass_5_10_1.2_2.4': 853.5438833236694, 'id_invMass_10_20_0_1.2': 882.7837867736816, 'invMass_20_25_0_1.2': 352.36952060461044, 'invMass_3_4_0_1.2': 523.9068693518639, 'id_invMass_3_4_1.2_2.4': 336.06057476997375, 'invMass_4_5_1.2_2.4': 288.52745097875595, 'id_invMass_2_3_1.2_2.4': 316.3304854631424, 'id_invMass_4_5_0_1.2': 359.80742609500885, 'id_invMass_20_25_1.2_2.4': 267.6738169193268, 'id_invMass_5_10_0_1.2': 1098.4089276194572, 'id_invMass_5_10_1.2_2.4': 836.6587591171265, 'invMass_10_20_0_1.2': 899.3792419433594, 'invMass_20_25_1.2_2.4': 270.82117104530334, 'id_invMass_10_20_1.2_2.4': 719.744607925415, 'invMass_2_3_1.2_2.4': 402.87252378463745, 'invMass_4_5_0_1.2': 432.7396157979965, 'id_invMass_3_4_0_1.2': 233.65269553661346, 'invMass_3_4_1.2_2.4': 361.9464042186737, 'id_invMass_4_5_1.2_2.4': 277.43652576208115, 'invMass_5_10_0_1.2': 1149.1296202540398, 'invMass_10_20_1.2_2.4': 731.7716636657715}

# DATA

fit_signal_integral = {'id_invMass_20_25_0_1.2': 9181.516008599125, 'invMass_5_10_1.2_2.4': 766.8702591790072, 'id_invMass_10_20_0_1.2': 411.79426346714587, 'invMass_20_25_0_1.2': 9169.855414211277, 'invMass_3_4_0_1.2': 638.1800453606712, 'id_invMass_3_4_1.2_2.4': 456.13610831881334, 'invMass_4_5_1.2_2.4': 521.1799027352286, 'id_invMass_2_3_1.2_2.4': 544.630523005079, 'id_invMass_4_5_0_1.2': 346.33388586659294, 'id_invMass_20_25_1.2_2.4': 6486.822682619575, 'id_invMass_5_10_0_1.2': 941.0203078343225, 'id_invMass_5_10_1.2_2.4': 700.3634857278888, 'invMass_10_20_0_1.2': 426.95514819617114, 'invMass_20_25_1.2_2.4': 6533.116883248389, 'id_invMass_10_20_1.2_2.4': 306.8323533562787, 'invMass_2_3_1.2_2.4': 664.9499163684858, 'invMass_4_5_0_1.2': 378.7533254579253, 'id_invMass_3_4_0_1.2': 297.02159919622557, 'invMass_3_4_1.2_2.4': 618.1427554540849, 'id_invMass_4_5_1.2_2.4': 351.8583729304078, 'invMass_5_10_0_1.2': 1082.557002981367, 'invMass_10_20_1.2_2.4': 308.36001705859275}
fit_signal_integral_error = {'id_invMass_20_25_0_1.2': 100.9033310747355, 'invMass_5_10_1.2_2.4': 120.13716887384642, 'id_invMass_10_20_0_1.2': 21.190979878771973, 'invMass_20_25_0_1.2': 223.49823948020133, 'invMass_3_4_0_1.2': 77.74391909778953, 'id_invMass_3_4_1.2_2.4': 40.85233411480135, 'invMass_4_5_1.2_2.4': 0.0, 'id_invMass_2_3_1.2_2.4': 28.005580511046553, 'id_invMass_4_5_0_1.2': 46.946299903016936, 'id_invMass_20_25_1.2_2.4': 100.18026537964768, 'id_invMass_5_10_0_1.2': 31.87772927499001, 'id_invMass_5_10_1.2_2.4': 28.36321058126898, 'invMass_10_20_0_1.2': 81.15117910325306, 'invMass_20_25_1.2_2.4': 100.99597207733261, 'id_invMass_10_20_1.2_2.4': 18.55067470151647, 'invMass_2_3_1.2_2.4': 142.5489835461554, 'invMass_4_5_0_1.2': 53.07545611128, 'id_invMass_3_4_0_1.2': 18.968852187062105, 'invMass_3_4_1.2_2.4': 85.09230233503935, 'id_invMass_4_5_1.2_2.4': 35.38308778768658, 'invMass_5_10_0_1.2': 145.83502375629993, 'invMass_10_20_1.2_2.4': 46.786632814626344}
bg_reduced = {'id_invMass_20_25_0_1.2': 9226.151844629512, 'invMass_5_10_1.2_2.4': 800.508189141512, 'id_invMass_10_20_0_1.2': 415.563012049739, 'invMass_20_25_0_1.2': 9210.579759162072, 'invMass_3_4_0_1.2': 627.7125242583734, 'id_invMass_3_4_1.2_2.4': 458.2739844035527, 'invMass_4_5_1.2_2.4': 534.1674867505108, 'id_invMass_2_3_1.2_2.4': 558.2278021141877, 'id_invMass_4_5_0_1.2': 356.98321978568976, 'id_invMass_20_25_1.2_2.4': 6473.083070818184, 'id_invMass_5_10_0_1.2': 949.8875952144557, 'id_invMass_5_10_1.2_2.4': 721.7131609505172, 'invMass_10_20_0_1.2': 450.39867237062833, 'invMass_20_25_1.2_2.4': 6522.132306989797, 'id_invMass_10_20_1.2_2.4': 318.56403530717444, 'invMass_2_3_1.2_2.4': 617.2480034530963, 'invMass_4_5_0_1.2': 382.28115984369197, 'id_invMass_3_4_0_1.2': 300.1202654811739, 'invMass_3_4_1.2_2.4': 626.4599486565648, 'id_invMass_4_5_1.2_2.4': 364.9791856478918, 'invMass_5_10_0_1.2': 1083.8296573892007, 'invMass_10_20_1.2_2.4': 325.48615044448616}


###########

# BARREL #

for region in (0,1):

    barrel_postfix = "_0_1.2"
    pt_ranges = [3,4,5,10,20]
    
    if region == 1:
        barrel_postfix = "_1.2_2.4"
        pt_ranges = [2,3,4,5,10,20]

    bins = np.zeros(len(pt_ranges),dtype=float)
    for i in range(len(pt_ranges)):
        bins[i] = pt_ranges[i]

    barrelHist = TH1F("barrelHist", "", len(pt_ranges)-1, bins)
    barrelHist.Sumw2()
    barrelHistDen = TH1F("barrelHistDen", "", len(pt_ranges)-1, bins)
    barrelHistDen.Sumw2()

    truthBarrelHist = TH1F("truthBarrelHist", "", len(pt_ranges)-1, bins)
    truthBarrelHist.Sumw2()
    truthBarrelHistDen = TH1F("truthBarrelHistDen", "", len(pt_ranges)-1, bins)
    truthBarrelHistDen.Sumw2()


    dataBarrelHist = TH1F("dataBarrelHist", "", len(pt_ranges)-1, bins)
    dataBarrelHist.Sumw2()
    dataBarrelHistDen = TH1F("dataBarrelHistDen", "", len(pt_ranges)-1, bins)
    dataBarrelHistDen.Sumw2()

    truthDataBarrelHist = TH1F("truthDataBarrelHist", "", len(pt_ranges)-1, bins)
    truthDataBarrelHist.Sumw2()
    truthDataBarrelHistDen = TH1F("truthDataBarrelHistDen", "", len(pt_ranges)-1, bins)
    truthDataBarrelHistDen.Sumw2()


    c1 = TCanvas("c1", "c1", 800, 800)

    legend = TLegend(.60,.40,.89,.60)
    legend.SetNColumns(1)
    legend.SetBorderSize(1)
    legend.SetFillStyle(0)

    ####### MC #########

    for pti in range(len(pt_ranges)):
        if pti == len(pt_ranges) - 1:
            continue
        pt1 = pt_ranges[pti]
        pt2 = pt_ranges[pti+1]
    
        obsBaseName = "invMass_"+str(pt1)+"_"+str(pt2)+barrel_postfix
    
        barrelHist.SetBinContent(pti+1, mc_fit_only_signal_integral["id_" + obsBaseName])
        barrelHist.SetBinError(pti+1, mc_fit_only_signal_integral_error["id_" + obsBaseName])
    
        barrelHistDen.SetBinContent(pti+1, mc_fit_only_signal_integral[obsBaseName])
        barrelHistDen.SetBinError(pti+1, mc_fit_only_signal_integral_error[obsBaseName])
    
        truthBarrelHist.SetBinContent(pti+1, mc_hist_count["id_" + obsBaseName])
        truthBarrelHistDen.SetBinContent(pti+1, mc_hist_count[obsBaseName])
    
    
        ####### DATA #########
    
        dataBarrelHist.SetBinContent(pti+1, fit_signal_integral["id_" + obsBaseName])
        dataBarrelHist.SetBinError(pti+1, fit_signal_integral_error["id_" + obsBaseName])
    
        dataBarrelHistDen.SetBinContent(pti+1, fit_signal_integral[obsBaseName])
        dataBarrelHistDen.SetBinError(pti+1, fit_signal_integral_error[obsBaseName])
    
        truthDataBarrelHist.SetBinContent(pti+1, bg_reduced["id_" + obsBaseName])
        truthDataBarrelHistDen.SetBinContent(pti+1, bg_reduced[obsBaseName])


    barrelHist.Divide(barrelHistDen)
    truthBarrelHist.Divide(truthBarrelHistDen)


    ####### DATA #########


    dataBarrelHist.Divide(dataBarrelHistDen)
    truthDataBarrelHist.Divide(truthDataBarrelHistDen)


    minimum = min(barrelHist.GetMinimum(), dataBarrelHist.GetMinimum(), truthBarrelHist.GetMinimum(), truthDataBarrelHist.GetMinimum())#, barrelHistHistCount.GetMinimum())
    maximum = max(barrelHist.GetMaximum(), dataBarrelHist.GetMaximum(), truthBarrelHist.GetMaximum(), truthDataBarrelHist.GetMaximum())#, barrelHistHistCount.GetMaximum())

    barrelHist.SetMinimum(minimum-0.1)
    barrelHist.SetMaximum(maximum+0.1)

    utils.formatHist(barrelHist, utils.colorPalette[14], 0, True, True)

    barrelHist.SetLineColor(kRed)
    barrelHist.SetMarkerColor(kRed)
    barrelHist.SetMarkerStyle(kOpenSquare)


    #setMarkers(barrelHist, 14)
    #setMarkers(barrelHistSignalFit, 7)
    #setMarkers(barrelHistHistCount, 1)

    #setMarkers(barrelHist, 1)
    #setMarkers(dataBarrelHist, kFullCircle)

    dataBarrelHist.SetMarkerStyle(kFullCircle)
    dataBarrelHist.SetLineColor(kBlack)

    truthBarrelHist.SetLineColor(kGreen)
    truthBarrelHist.SetMarkerColor(kGreen)
    truthBarrelHist.SetMarkerStyle(kFullSquare)

    truthDataBarrelHist.SetLineColor(kBlue)
    truthDataBarrelHist.SetMarkerColor(kBlue)
    truthDataBarrelHist.SetMarkerStyle(kFullCircle)


    legend.AddEntry(barrelHist, "MC", 'p')
    legend.AddEntry(truthBarrelHist, "MC Count", 'p')

    legend.AddEntry(dataBarrelHist, "Data", 'p')
    legend.AddEntry(truthDataBarrelHist, "Data Count", 'p')
    #legend.AddEntry(barrelHistHistCount, "Signal Count Efficiency", 'p')
    barrelHist.GetXaxis().SetTitle("pT")

    barrelHist.Draw("p")
    truthBarrelHist.Draw("p same")
    dataBarrelHist.Draw("p same")
    truthDataBarrelHist.Draw("p same")
    #barrelHistHistCount.Draw("p same")

    legend.Draw("SAME")
    utils.stamp_plot("22.9")
    if region == 0:
        c1.SaveAs("barrelGranHist.pdf")
    else:
        c1.SaveAs("endcapsGranHist.pdf")
    
    
    #Scale Factors
    
    dataBarrelHist.Divide(barrelHist)
    dataBarrelHist.GetXaxis().SetTitle("pT")
    dataBarrelHist.Draw("p")
    utils.stamp_plot("22.9")
    
    truthDataBarrelHist.Divide(truthBarrelHist)
    truthDataBarrelHist.Draw("p same")
    
    if region == 0:
        c1.SaveAs("barrelGranScaleFactors.pdf")
    else:
        c1.SaveAs("endcapsGranScaleFactors.pdf")
    
exit(0)

### SCALE FACTORS #####

c1 = TCanvas("c1", "c1", 800, 800)

legend = TLegend(.60,.40,.89,.60)
legend.SetNColumns(1)
legend.SetBorderSize(1)
legend.SetFillStyle(0)

dataBarrelHist.Divide(barrelHist)
dataBarrelHist.GetXaxis().SetTitle("pT")
dataBarrelHist.Draw("p")
utils.stamp_plot("22.9")
c1.SaveAs("barrelScaleFactors.pdf")



##### ENDCAPS #####




bins = np.zeros(5,dtype=float)
bins[0] = 2
bins[1] = 3
bins[2] = 5
bins[3] = 10
bins[4] = 25


barrelHist = TH1F("barrelHist", "", 4, bins)
barrelHist.Sumw2()
barrelHistDen = TH1F("barrelHistDen", "", 4, bins)
barrelHistDen.Sumw2()


#barrelHistSignalFit = TH1F("barrelHistSignalFit", "", 3, bins)
#barrelHistHistCount = TH1F("barrelHistHistCount", "", 3, bins)

dataBarrelHist = TH1F("dataBarrelHist", "", 4, bins)
dataBarrelHist.Sumw2()
dataBarrelHistDen = TH1F("dataBarrelHistDen", "", 4, bins)
dataBarrelHistDen.Sumw2()

c1 = TCanvas("c1", "c1", 800, 800)

legend = TLegend(.60,.40,.89,.60)
legend.SetNColumns(1)
legend.SetBorderSize(1)
legend.SetFillStyle(0)


barrelHist.SetBinContent(1, mc_fit_only_signal_integral["id_invMass_2_3_1.2_2.4"])#/fit_signal_integral["invMass_2_3_1.2_2.4"])
barrelHist.SetBinContent(2, mc_fit_only_signal_integral["id_invMass_3_5_1.2_2.4"])#/fit_signal_integral["invMass_3_5_1.2_2.4"])
barrelHist.SetBinContent(3, mc_fit_only_signal_integral["id_invMass_5_10_1.2_2.4"])#/fit_signal_integral["invMass_5_10_1.2_2.4"])
barrelHist.SetBinContent(4, mc_fit_only_signal_integral["id_invMass_10_25_1.2_2.4"])#/fit_signal_integral["invMass_10_25_1.2_2.4"])

barrelHist.SetBinError(1, mc_fit_only_signal_integral_error["id_invMass_2_3_1.2_2.4"])#/fit_signal_integral["invMass_2_3_1.2_2.4"])
barrelHist.SetBinError(2, mc_fit_only_signal_integral_error["id_invMass_3_5_1.2_2.4"])#/fit_signal_integral["invMass_3_5_1.2_2.4"])
barrelHist.SetBinError(3, mc_fit_only_signal_integral_error["id_invMass_5_10_1.2_2.4"])#/fit_signal_integral["invMass_5_10_1.2_2.4"])
barrelHist.SetBinError(4, mc_fit_only_signal_integral_error["id_invMass_10_25_1.2_2.4"])#/fit_signal_integral["invMass_10_25_1.2_2.4"])

barrelHistDen.SetBinContent(1, mc_fit_only_signal_integral["invMass_2_3_1.2_2.4"])#/fit_signal_integral["invMass_2_3_1.2_2.4"])
barrelHistDen.SetBinContent(2, mc_fit_only_signal_integral["invMass_3_5_1.2_2.4"])#/fit_signal_integral["invMass_3_5_1.2_2.4"])
barrelHistDen.SetBinContent(3, mc_fit_only_signal_integral["invMass_5_10_1.2_2.4"])#/fit_signal_integral["invMass_5_10_1.2_2.4"])
barrelHistDen.SetBinContent(4, mc_fit_only_signal_integral["invMass_10_25_1.2_2.4"])#/fit_signal_integral["invMass_10_25_1.2_2.4"])

barrelHistDen.SetBinError(1, mc_fit_only_signal_integral_error["invMass_2_3_1.2_2.4"])#/fit_signal_integral["invMass_2_3_1.2_2.4"])
barrelHistDen.SetBinError(2, mc_fit_only_signal_integral_error["invMass_3_5_1.2_2.4"])#/fit_signal_integral["invMass_3_5_1.2_2.4"])
barrelHistDen.SetBinError(3, mc_fit_only_signal_integral_error["invMass_5_10_1.2_2.4"])#/fit_signal_integral["invMass_5_10_1.2_2.4"])
barrelHistDen.SetBinError(4, mc_fit_only_signal_integral_error["invMass_10_25_1.2_2.4"])#/fit_signal_integral["invMass_10_25_1.2_2.4"])

barrelHist.Divide(barrelHistDen)


dataBarrelHist.SetBinContent(1, fit_signal_integral["id_invMass_2_3_1.2_2.4"])#/fit_signal_integral["invMass_2_3_1.2_2.4"])
dataBarrelHist.SetBinContent(2, fit_signal_integral["id_invMass_3_5_1.2_2.4"])#/fit_signal_integral["invMass_3_5_1.2_2.4"])
dataBarrelHist.SetBinContent(3, fit_signal_integral["id_invMass_5_10_1.2_2.4"])#/fit_signal_integral["invMass_5_10_1.2_2.4"])
dataBarrelHist.SetBinContent(4, fit_signal_integral["id_invMass_10_25_1.2_2.4"])#/fit_signal_integral["invMass_10_25_1.2_2.4"])

dataBarrelHist.SetBinError(1, fit_signal_integral_error["id_invMass_2_3_1.2_2.4"])#/fit_signal_integral["invMass_2_3_1.2_2.4"])
dataBarrelHist.SetBinError(2, fit_signal_integral_error["id_invMass_3_5_1.2_2.4"])#/fit_signal_integral["invMass_3_5_1.2_2.4"])
dataBarrelHist.SetBinError(3, fit_signal_integral_error["id_invMass_5_10_1.2_2.4"])#/fit_signal_integral["invMass_5_10_1.2_2.4"])
dataBarrelHist.SetBinError(4, fit_signal_integral_error["id_invMass_10_25_1.2_2.4"])#/fit_signal_integral["invMass_10_25_1.2_2.4"])

dataBarrelHistDen.SetBinContent(1, fit_signal_integral["invMass_2_3_1.2_2.4"])#/fit_signal_integral["invMass_2_3_1.2_2.4"])
dataBarrelHistDen.SetBinContent(2, fit_signal_integral["invMass_3_5_1.2_2.4"])#/fit_signal_integral["invMass_3_5_1.2_2.4"])
dataBarrelHistDen.SetBinContent(3, fit_signal_integral["invMass_5_10_1.2_2.4"])#/fit_signal_integral["invMass_5_10_1.2_2.4"])
dataBarrelHistDen.SetBinContent(4, fit_signal_integral["invMass_10_25_1.2_2.4"])#/fit_signal_integral["invMass_10_25_1.2_2.4"])

dataBarrelHistDen.SetBinError(1, fit_signal_integral_error["invMass_2_3_1.2_2.4"])#/fit_signal_integral["invMass_2_3_1.2_2.4"])
dataBarrelHistDen.SetBinError(2, fit_signal_integral_error["invMass_3_5_1.2_2.4"])#/fit_signal_integral["invMass_3_5_1.2_2.4"])
dataBarrelHistDen.SetBinError(3, fit_signal_integral_error["invMass_5_10_1.2_2.4"])#/fit_signal_integral["invMass_5_10_1.2_2.4"])
dataBarrelHistDen.SetBinError(4, fit_signal_integral_error["invMass_10_25_1.2_2.4"])#/fit_signal_integral["invMass_10_25_1.2_2.4"])

dataBarrelHist.Divide(dataBarrelHistDen)


minimum = min(barrelHist.GetMinimum(), dataBarrelHist.GetMinimum())#, barrelHistHistCount.GetMinimum())
maximum = max(barrelHist.GetMaximum(), dataBarrelHist.GetMaximum())#, barrelHistHistCount.GetMaximum())

barrelHist.SetMinimum(minimum-0.1)
barrelHist.SetMaximum(maximum+0.1)


utils.formatHist(barrelHist, utils.colorPalette[14], 0, True, True)

#setMarkers(barrelHist, 14)
#setMarkers(barrelHistSignalFit, 7)
#setMarkers(barrelHistHistCount, 1)

#setMarkers(barrelHist, 1)
barrelHist.SetLineColor(kRed)
barrelHist.SetMarkerColor(kRed)
barrelHist.SetMarkerStyle(kOpenSquare)

barrelHist.GetXaxis().SetTitle("pT")


#setMarkers(dataBarrelHist, kFullCircle)

dataBarrelHist.SetMarkerStyle(kFullCircle)
dataBarrelHist.SetLineColor(kBlack)


legend.AddEntry(barrelHist, "MC", 'p')
legend.AddEntry(dataBarrelHist, "Data", 'p')
#legend.AddEntry(barrelHistHistCount, "Signal Count Efficiency", 'p')


barrelHist.Draw("p")
dataBarrelHist.Draw("p same")
#barrelHistHistCount.Draw("p same")

legend.Draw("SAME")

utils.stamp_plot("22.9")

c1.SaveAs("endcapsHist.pdf")

### SCALE FACTORS #####

c1 = TCanvas("c1", "c1", 800, 800)

legend = TLegend(.60,.40,.89,.60)
legend.SetNColumns(1)
legend.SetBorderSize(1)
legend.SetFillStyle(0)

dataBarrelHist.Divide(barrelHist)

dataBarrelHist.GetXaxis().SetTitle("pT")

dataBarrelHist.Draw("p")
utils.stamp_plot("22.9")

c1.SaveAs("endcapsScaleFactors.pdf")
