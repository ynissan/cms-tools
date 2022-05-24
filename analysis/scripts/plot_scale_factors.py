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

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib/classes"))
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

mc_fit_only_signal_integral = {'invMass_10_25_1.2_2.4': 1433.9311055258397, 'id_invMass_5_10_0_1.2': 1214.609297950704, 'invMass_2_3_1.2_2.4': 547.1465014368986, 'id_invMass_5_10_1.2_2.4': 984.8963909309842, 'id_invMass_3_5_0_1.2': 675.2577445880007, 'invMass_5_10_1.2_2.4': 1002.3659570557165, 'id_invMass_3_5_1.2_2.4': 721.6198021438195, 'invMass_3_5_0_1.2': 1109.7280196660408, 'id_invMass_2_3_1.2_2.4': 426.15359421264793, 'invMass_10_25_0_1.2': 1677.0640418831845, 'id_invMass_10_25_1.2_2.4': 1415.3868666113221, 'invMass_3_5_1.2_2.4': 764.6315053699992, 'id_invMass_10_25_0_1.2': 1642.478376723696, 'reco_invMass_10_25_0_1.2': 1662.7833621022703, 'reco_invMass_3_5_1.2_2.4': 740.9694342413133, 'reco_invMass_5_10_0_1.2': 1244.972199485492, 'invMass_5_10_0_1.2': 1271.9589548102094, 'reco_invMass_3_5_0_1.2': 773.3775201503289, 'reco_invMass_10_25_1.2_2.4': 1420.809835065643, 'reco_invMass_5_10_1.2_2.4': 997.7908964405235, 'reco_invMass_2_3_1.2_2.4': 461.3089783045703}
mc_fit_only_signal_integral_error = {'invMass_10_25_1.2_2.4': 40.13911043440323, 'id_invMass_5_10_0_1.2': 37.878309546727984, 'invMass_2_3_1.2_2.4': 24.753829605940496, 'id_invMass_5_10_1.2_2.4': 68.88722942594322, 'id_invMass_3_5_0_1.2': 28.157346748054707, 'invMass_5_10_1.2_2.4': 33.4784915186515, 'id_invMass_3_5_1.2_2.4': 28.428445611660003, 'invMass_3_5_0_1.2': 35.914295505146846, 'id_invMass_2_3_1.2_2.4': 21.772477453663186, 'invMass_10_25_0_1.2': 44.22737988399962, 'id_invMass_10_25_1.2_2.4': 40.733096923847455, 'invMass_3_5_1.2_2.4': 29.512908155827787, 'id_invMass_10_25_0_1.2': 43.812621057092684, 'reco_invMass_10_25_0_1.2': 44.0772046202088, 'reco_invMass_3_5_1.2_2.4': 15.739326007546108, 'reco_invMass_5_10_0_1.2': 38.30343977789584, 'invMass_5_10_0_1.2': 38.75063688893417, 'reco_invMass_3_5_0_1.2': 30.133125726774665, 'reco_invMass_10_25_1.2_2.4': 39.99534854185232, 'reco_invMass_5_10_1.2_2.4': 33.37892466986633, 'reco_invMass_2_3_1.2_2.4': 10.069607496869702}

# DATA

fit_signal_integral = {'invMass_10_25_1.2_2.4': 24267.51277423747, 'id_invMass_5_10_0_1.2': 8879.912176445909, 'invMass_2_3_1.2_2.4': 75226.2822480937, 'id_invMass_5_10_1.2_2.4': 10832.880179003147, 'id_invMass_3_5_0_1.2': 34103.14295054003, 'invMass_5_10_1.2_2.4': 11424.015850440508, 'id_invMass_3_5_1.2_2.4': 46686.273374516255, 'invMass_3_5_0_1.2': 72958.30871523834, 'id_invMass_2_3_1.2_2.4': 54482.19902741232, 'invMass_10_25_0_1.2': 24981.519747995095, 'id_invMass_10_25_1.2_2.4': 23658.590776369412, 'invMass_3_5_1.2_2.4': 51797.73002027704, 'id_invMass_10_25_0_1.2': 24754.032652783142, 'reco_invMass_10_25_0_1.2': 24988.689596079235, 'reco_invMass_3_5_1.2_2.4': 49078.500338252736, 'reco_invMass_5_10_0_1.2': 9052.538654641856, 'invMass_5_10_0_1.2': 9683.674465458136, 'reco_invMass_3_5_0_1.2': 37846.475938839365, 'reco_invMass_10_25_1.2_2.4': 24334.142510783626, 'reco_invMass_5_10_1.2_2.4': 11204.942701510357, 'reco_invMass_2_3_1.2_2.4': 61014.93125637753}
fit_signal_integral_error = {'invMass_10_25_1.2_2.4': 380.6432249253492, 'id_invMass_5_10_0_1.2': 100.88478750397634, 'invMass_2_3_1.2_2.4': 707.5141003962434, 'id_invMass_5_10_1.2_2.4': 113.08392895312538, 'id_invMass_3_5_0_1.2': 194.30840823366216, 'invMass_5_10_1.2_2.4': 122.49257594818596, 'id_invMass_3_5_1.2_2.4': 258.15678031843885, 'invMass_3_5_0_1.2': 432.0249529038372, 'id_invMass_2_3_1.2_2.4': 526.387655634525, 'invMass_10_25_0_1.2': 173.12558405105437, 'id_invMass_10_25_1.2_2.4': 139.32205262541797, 'invMass_3_5_1.2_2.4': 735.7187140228808, 'id_invMass_10_25_0_1.2': 168.02052177342833, 'reco_invMass_10_25_0_1.2': 169.72686341463628, 'reco_invMass_3_5_1.2_2.4': 177.10234117998473, 'reco_invMass_5_10_0_1.2': 99.9902378734231, 'invMass_5_10_0_1.2': 259.7000668494758, 'reco_invMass_3_5_0_1.2': 146.6379686819823, 'reco_invMass_10_25_1.2_2.4': 165.62679452867707, 'reco_invMass_5_10_1.2_2.4': 132.33511880765482, 'reco_invMass_2_3_1.2_2.4': 173.28377042157146}


###########


bins = np.zeros(4,dtype=float)
bins[0] = 3
bins[1] = 5
bins[2] = 10
bins[3] = 25

barrelHist = TH1F("barrelHist", "", 3, bins)
barrelHist.Sumw2()
barrelHistDen = TH1F("barrelHistDen", "", 3, bins)
barrelHistDen.Sumw2()


#barrelHistSignalFit = TH1F("barrelHistSignalFit", "", 3, bins)
#barrelHistHistCount = TH1F("barrelHistHistCount", "", 3, bins)

dataBarrelHist = TH1F("dataBarrelHist", "", 3, bins)
dataBarrelHist.Sumw2()
dataBarrelHistDen = TH1F("dataBarrelHistDen", "", 3, bins)
dataBarrelHistDen.Sumw2()


c1 = TCanvas("c1", "c1", 800, 800)

legend = TLegend(.60,.40,.89,.60)
legend.SetNColumns(1)
legend.SetBorderSize(1)
legend.SetFillStyle(0)

####### MC #########

barrelHist.SetBinContent(1, mc_fit_only_signal_integral["id_invMass_3_5_0_1.2"])#/fit_signal_integral["invMass_3_5_0_1.2"])
barrelHist.SetBinError(1, mc_fit_only_signal_integral_error["id_invMass_3_5_0_1.2"])


barrelHist.SetBinContent(2, mc_fit_only_signal_integral["id_invMass_5_10_0_1.2"])#/fit_signal_integral["invMass_5_10_0_1.2"])
barrelHist.SetBinError(2, mc_fit_only_signal_integral_error["id_invMass_5_10_0_1.2"])


barrelHist.SetBinContent(3, mc_fit_only_signal_integral["id_invMass_10_25_0_1.2"])#/fit_signal_integral["invMass_10_25_0_1.2"])
barrelHist.SetBinError(3, mc_fit_only_signal_integral_error["id_invMass_10_25_0_1.2"])

############### DENOMINATOR ###############

barrelHistDen.SetBinContent(1, mc_fit_only_signal_integral["invMass_3_5_0_1.2"])#/fit_signal_integral["invMass_3_5_0_1.2"])
barrelHistDen.SetBinError(1, mc_fit_only_signal_integral_error["invMass_3_5_0_1.2"])


barrelHistDen.SetBinContent(2, mc_fit_only_signal_integral["invMass_5_10_0_1.2"])#/fit_signal_integral["invMass_5_10_0_1.2"])
barrelHistDen.SetBinError(2, mc_fit_only_signal_integral_error["invMass_5_10_0_1.2"])


barrelHistDen.SetBinContent(3, mc_fit_only_signal_integral["invMass_10_25_0_1.2"])#/fit_signal_integral["invMass_10_25_0_1.2"])
barrelHistDen.SetBinError(3, mc_fit_only_signal_integral_error["invMass_10_25_0_1.2"])


barrelHist.Divide(barrelHistDen)



####### DATA #########

dataBarrelHist.SetBinContent(1, fit_signal_integral["id_invMass_3_5_0_1.2"])#/fit_signal_integral["invMass_3_5_0_1.2"])
dataBarrelHist.SetBinError(1, fit_signal_integral_error["id_invMass_3_5_0_1.2"])


dataBarrelHist.SetBinContent(2, fit_signal_integral["id_invMass_5_10_0_1.2"])#/fit_signal_integral["invMass_5_10_0_1.2"])
dataBarrelHist.SetBinError(2, fit_signal_integral_error["id_invMass_5_10_0_1.2"])


dataBarrelHist.SetBinContent(3, fit_signal_integral["id_invMass_10_25_0_1.2"])#/fit_signal_integral["invMass_10_25_0_1.2"])
dataBarrelHist.SetBinError(3, fit_signal_integral_error["id_invMass_10_25_0_1.2"])

############### DENOMINATOR ###############

dataBarrelHistDen.SetBinContent(1, fit_signal_integral["invMass_3_5_0_1.2"])#/fit_signal_integral["invMass_3_5_0_1.2"])
dataBarrelHistDen.SetBinError(1, fit_signal_integral_error["invMass_3_5_0_1.2"])


dataBarrelHistDen.SetBinContent(2, fit_signal_integral["invMass_5_10_0_1.2"])#/fit_signal_integral["invMass_5_10_0_1.2"])
dataBarrelHistDen.SetBinError(2, fit_signal_integral_error["invMass_5_10_0_1.2"])


dataBarrelHistDen.SetBinContent(3, fit_signal_integral["invMass_10_25_0_1.2"])#/fit_signal_integral["invMass_10_25_0_1.2"])
dataBarrelHistDen.SetBinError(3, fit_signal_integral_error["invMass_10_25_0_1.2"])

dataBarrelHist.Divide(dataBarrelHistDen)



# barrelHistSignalFit.SetBinContent(1, fit_only_signal_integral["id_invMass_3_5_0_1.2"]/fit_only_signal_integral["invMass_3_5_0_1.2"])
# barrelHistSignalFit.SetBinContent(2, fit_only_signal_integral["id_invMass_5_10_0_1.2"]/fit_only_signal_integral["invMass_5_10_0_1.2"])
# barrelHistSignalFit.SetBinContent(3, fit_only_signal_integral["id_invMass_10_25_0_1.2"]/fit_only_signal_integral["invMass_10_25_0_1.2"])
# 
# barrelHistHistCount.SetBinContent(1, hist_signal_integral["id_invMass_3_5_0_1.2"]/hist_signal_integral["invMass_3_5_0_1.2"])
# barrelHistHistCount.SetBinContent(2, hist_signal_integral["id_invMass_5_10_0_1.2"]/hist_signal_integral["invMass_5_10_0_1.2"])
# barrelHistHistCount.SetBinContent(3, hist_signal_integral["id_invMass_10_25_0_1.2"]/hist_signal_integral["invMass_10_25_0_1.2"])


minimum = min(barrelHist.GetMinimum(), dataBarrelHist.GetMinimum())#, barrelHistHistCount.GetMinimum())
maximum = max(barrelHist.GetMaximum(), dataBarrelHist.GetMaximum())#, barrelHistHistCount.GetMaximum())

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


legend.AddEntry(barrelHist, "MC", 'p')
legend.AddEntry(dataBarrelHist, "Data", 'p')
#legend.AddEntry(barrelHistHistCount, "Signal Count Efficiency", 'p')
barrelHist.GetXaxis().SetTitle("pT")

barrelHist.Draw("p")
dataBarrelHist.Draw("p same")
#barrelHistHistCount.Draw("p same")

legend.Draw("SAME")
utils.stamp_plot("22.9")
c1.SaveAs("barrelHist.pdf")

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
