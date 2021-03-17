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

plot_stability = False



# hist_signal_integral = {'invMass_5_10_1.2_2.4': 1019.4852705001831, 'id_invMass_10_25_0_1.2': 1667.2375283241272, 'reco_invMass_2_3_0_1.2': 9.821751654148102, 'reco_invMass_10_25_1.2_2.4': 1443.9869174957275, 'invMass_2_3_0_1.2': 894.3325540423393, 'id_invMass_3_5_1.2_2.4': 735.1649420261383, 'id_invMass_2_3_1.2_2.4': 437.24313747882843, 'invMass_3_5_1.2_2.4': 779.504823923111, 'id_invMass_5_10_0_1.2': 1233.4039489626884, 'id_invMass_5_10_1.2_2.4': 999.937216758728, 'reco_invMass_3_5_0_1.2': 793.398924946785, 'invMass_3_5_0_1.2': 1127.6164858341217, 'reco_invMass_5_10_1.2_2.4': 1014.2677640914917, 'invMass_5_10_0_1.2': 1289.267138183117, 'id_invMass_2_3_0_1.2': 8.231943935155869, 'invMass_2_3_1.2_2.4': 554.1936163902283, 'id_invMass_3_5_0_1.2': 689.7469207048416, 'id_invMass_10_25_1.2_2.4': 1437.1604557037354, 'invMass_10_25_1.2_2.4': 1456.6303882598877, 'reco_invMass_2_3_1.2_2.4': 489.0612097978592, 'reco_invMass_3_5_1.2_2.4': 767.6232149600983, 'invMass_10_25_0_1.2': 1703.163152217865, 'reco_invMass_10_25_0_1.2': 1687.6839156150818, 'reco_invMass_5_10_0_1.2': 1262.0459811091423}
# fit_only_signal_integral = {'invMass_5_10_1.2_2.4': 992.4753403522357, 'id_invMass_10_25_0_1.2': 1647.4060494474707, 'reco_invMass_2_3_0_1.2': 8.60762827279467, 'reco_invMass_10_25_1.2_2.4': 1399.078989389184, 'invMass_2_3_0_1.2': 864.2987783298386, 'id_invMass_3_5_1.2_2.4': 720.8718760960961, 'id_invMass_2_3_1.2_2.4': 424.24377182107645, 'invMass_3_5_1.2_2.4': 765.6608341948643, 'id_invMass_5_10_0_1.2': 1199.1477266877093, 'id_invMass_5_10_1.2_2.4': 971.4513311235709, 'reco_invMass_3_5_0_1.2': 784.63451648419, 'invMass_3_5_0_1.2': 1120.8097734590774, 'reco_invMass_5_10_1.2_2.4': 987.8827411877056, 'invMass_5_10_0_1.2': 1271.670479429922, 'id_invMass_2_3_0_1.2': 8.408071431347487, 'invMass_2_3_1.2_2.4': 544.694351031679, 'id_invMass_3_5_0_1.2': 681.5399885908722, 'id_invMass_10_25_1.2_2.4': 1393.9949629782311, 'invMass_10_25_1.2_2.4': 1411.6007851011402, 'reco_invMass_2_3_1.2_2.4': 477.848599981434, 'reco_invMass_3_5_1.2_2.4': 754.4303153600102, 'invMass_10_25_0_1.2': 1682.1977796215028, 'reco_invMass_10_25_0_1.2': 1667.6757997858504, 'reco_invMass_5_10_0_1.2': 1228.2255003954342}
# fit_signal_integral = {'invMass_5_10_1.2_2.4': 1039.6807993890702, 'id_invMass_10_25_0_1.2': 1629.9117665819474, 'reco_invMass_2_3_0_1.2': 33.54176707967502, 'reco_invMass_10_25_1.2_2.4': 1375.5252104302408, 'invMass_2_3_0_1.2': 1484.1844977215258, 'id_invMass_3_5_1.2_2.4': 692.3371128715078, 'id_invMass_2_3_1.2_2.4': 456.2216576688991, 'invMass_3_5_1.2_2.4': 984.8468133701276, 'id_invMass_5_10_0_1.2': 1224.8713413300425, 'id_invMass_5_10_1.2_2.4': 972.7717708852805, 'reco_invMass_3_5_0_1.2': 793.6126705058125, 'invMass_3_5_0_1.2': 1256.5596046590754, 'reco_invMass_5_10_1.2_2.4': 986.6826763283965, 'invMass_5_10_0_1.2': 1487.0482516871007, 'id_invMass_2_3_0_1.2': 34.19613595374151, 'invMass_2_3_1.2_2.4': 562.6048245270454, 'id_invMass_3_5_0_1.2': 698.2236046746027, 'id_invMass_10_25_1.2_2.4': 1375.7941976978223, 'invMass_10_25_1.2_2.4': 1479.4022715502192, 'reco_invMass_2_3_1.2_2.4': 498.172995443117, 'reco_invMass_3_5_1.2_2.4': 707.4581423325429, 'invMass_10_25_0_1.2': 1756.3046365512205, 'reco_invMass_10_25_0_1.2': 1629.3225892413604, 'reco_invMass_5_10_0_1.2': 1253.0440049137048}


###########

# MC

# mc_fit_only_signal_integral = {'id_invMass_20_25_0_1.2': 334.2070116896566, 'invMass_5_10_1.2_2.4': 843.9680150736652, 'id_invMass_10_20_0_1.2': 878.4176041308358, 'invMass_20_25_0_1.2': 341.8185362679077, 'invMass_3_4_0_1.2': 517.2559389283792, 'id_invMass_3_4_1.2_2.4': 320.5924439128414, 'invMass_4_5_1.2_2.4': 283.8783804472692, 'id_invMass_2_3_1.2_2.4': 302.80207629438996, 'id_invMass_4_5_0_1.2': 338.072692079381, 'id_invMass_20_25_1.2_2.4': 259.98947186941297, 'id_invMass_5_10_0_1.2': 1079.6989360766086, 'id_invMass_5_10_1.2_2.4': 828.7280539572467, 'invMass_10_20_0_1.2': 894.405793888353, 'invMass_20_25_1.2_2.4': 263.92990927784507, 'id_invMass_10_20_1.2_2.4': 697.0012242876369, 'invMass_2_3_1.2_2.4': 398.4394337057448, 'invMass_4_5_0_1.2': 411.85264535095223, 'id_invMass_3_4_0_1.2': 227.6695841006641, 'invMass_3_4_1.2_2.4': 345.5945007841578, 'id_invMass_4_5_1.2_2.4': 269.57315594838775, 'invMass_5_10_0_1.2': 1131.9408990629208, 'invMass_10_20_1.2_2.4': 708.0167290251296}
# mc_fit_only_signal_integral_error = {'id_invMass_20_25_0_1.2': 19.844732379033964, 'invMass_5_10_1.2_2.4': 60.76359652797092, 'id_invMass_10_20_0_1.2': 31.812127760120678, 'invMass_20_25_0_1.2': 23.372845475876613, 'invMass_3_4_0_1.2': 47.31003588390368, 'id_invMass_3_4_1.2_2.4': 19.317231206933187, 'invMass_4_5_1.2_2.4': 34.71858762397694, 'id_invMass_2_3_1.2_2.4': 18.42594167690223, 'id_invMass_4_5_0_1.2': 19.943485612913715, 'id_invMass_20_25_1.2_2.4': 16.89670431354685, 'id_invMass_5_10_0_1.2': 86.85134944806285, 'id_invMass_5_10_1.2_2.4': 30.53891555858885, 'invMass_10_20_0_1.2': 31.171755238736147, 'invMass_20_25_1.2_2.4': 17.156935560363877, 'id_invMass_10_20_1.2_2.4': 28.06094885355605, 'invMass_2_3_1.2_2.4': 21.18464662966867, 'invMass_4_5_0_1.2': 21.969700388041534, 'id_invMass_3_4_0_1.2': 33.94254947689124, 'invMass_3_4_1.2_2.4': 19.97164295816518, 'id_invMass_4_5_1.2_2.4': 18.006366586998848, 'invMass_5_10_0_1.2': 85.57517777088567, 'invMass_10_20_1.2_2.4': 28.280846533820984}
# mc_hist_count = {'id_invMass_20_25_0_1.2': 344.23969680070877, 'invMass_5_10_1.2_2.4': 853.5438833236694, 'id_invMass_10_20_0_1.2': 882.7837867736816, 'invMass_20_25_0_1.2': 352.36952060461044, 'invMass_3_4_0_1.2': 523.9068693518639, 'id_invMass_3_4_1.2_2.4': 336.06057476997375, 'invMass_4_5_1.2_2.4': 288.52745097875595, 'id_invMass_2_3_1.2_2.4': 316.3304854631424, 'id_invMass_4_5_0_1.2': 359.80742609500885, 'id_invMass_20_25_1.2_2.4': 267.6738169193268, 'id_invMass_5_10_0_1.2': 1098.4089276194572, 'id_invMass_5_10_1.2_2.4': 836.6587591171265, 'invMass_10_20_0_1.2': 899.3792419433594, 'invMass_20_25_1.2_2.4': 270.82117104530334, 'id_invMass_10_20_1.2_2.4': 719.744607925415, 'invMass_2_3_1.2_2.4': 402.87252378463745, 'invMass_4_5_0_1.2': 432.7396157979965, 'id_invMass_3_4_0_1.2': 233.65269553661346, 'invMass_3_4_1.2_2.4': 361.9464042186737, 'id_invMass_4_5_1.2_2.4': 277.43652576208115, 'invMass_5_10_0_1.2': 1149.1296202540398, 'invMass_10_20_1.2_2.4': 731.7716636657715}

# DATA

# fit_signal_integral = {'id_invMass_20_25_0_1.2': 9181.516008599125, 'invMass_5_10_1.2_2.4': 766.8702591790072, 'id_invMass_10_20_0_1.2': 411.79426346714587, 'invMass_20_25_0_1.2': 9169.855414211277, 'invMass_3_4_0_1.2': 638.1800453606712, 'id_invMass_3_4_1.2_2.4': 456.13610831881334, 'invMass_4_5_1.2_2.4': 521.1799027352286, 'id_invMass_2_3_1.2_2.4': 544.630523005079, 'id_invMass_4_5_0_1.2': 346.33388586659294, 'id_invMass_20_25_1.2_2.4': 6486.822682619575, 'id_invMass_5_10_0_1.2': 941.0203078343225, 'id_invMass_5_10_1.2_2.4': 700.3634857278888, 'invMass_10_20_0_1.2': 426.95514819617114, 'invMass_20_25_1.2_2.4': 6533.116883248389, 'id_invMass_10_20_1.2_2.4': 306.8323533562787, 'invMass_2_3_1.2_2.4': 664.9499163684858, 'invMass_4_5_0_1.2': 378.7533254579253, 'id_invMass_3_4_0_1.2': 297.02159919622557, 'invMass_3_4_1.2_2.4': 618.1427554540849, 'id_invMass_4_5_1.2_2.4': 351.8583729304078, 'invMass_5_10_0_1.2': 1082.557002981367, 'invMass_10_20_1.2_2.4': 308.36001705859275}
# fit_signal_integral_error = {'id_invMass_20_25_0_1.2': 100.9033310747355, 'invMass_5_10_1.2_2.4': 120.13716887384642, 'id_invMass_10_20_0_1.2': 21.190979878771973, 'invMass_20_25_0_1.2': 223.49823948020133, 'invMass_3_4_0_1.2': 77.74391909778953, 'id_invMass_3_4_1.2_2.4': 40.85233411480135, 'invMass_4_5_1.2_2.4': 0.0, 'id_invMass_2_3_1.2_2.4': 28.005580511046553, 'id_invMass_4_5_0_1.2': 46.946299903016936, 'id_invMass_20_25_1.2_2.4': 100.18026537964768, 'id_invMass_5_10_0_1.2': 31.87772927499001, 'id_invMass_5_10_1.2_2.4': 28.36321058126898, 'invMass_10_20_0_1.2': 81.15117910325306, 'invMass_20_25_1.2_2.4': 100.99597207733261, 'id_invMass_10_20_1.2_2.4': 18.55067470151647, 'invMass_2_3_1.2_2.4': 142.5489835461554, 'invMass_4_5_0_1.2': 53.07545611128, 'id_invMass_3_4_0_1.2': 18.968852187062105, 'invMass_3_4_1.2_2.4': 85.09230233503935, 'id_invMass_4_5_1.2_2.4': 35.38308778768658, 'invMass_5_10_0_1.2': 145.83502375629993, 'invMass_10_20_1.2_2.4': 46.786632814626344}
# bg_reduced = {'id_invMass_20_25_0_1.2': 9226.151844629512, 'invMass_5_10_1.2_2.4': 800.508189141512, 'id_invMass_10_20_0_1.2': 415.563012049739, 'invMass_20_25_0_1.2': 9210.579759162072, 'invMass_3_4_0_1.2': 627.7125242583734, 'id_invMass_3_4_1.2_2.4': 458.2739844035527, 'invMass_4_5_1.2_2.4': 534.1674867505108, 'id_invMass_2_3_1.2_2.4': 558.2278021141877, 'id_invMass_4_5_0_1.2': 356.98321978568976, 'id_invMass_20_25_1.2_2.4': 6473.083070818184, 'id_invMass_5_10_0_1.2': 949.8875952144557, 'id_invMass_5_10_1.2_2.4': 721.7131609505172, 'invMass_10_20_0_1.2': 450.39867237062833, 'invMass_20_25_1.2_2.4': 6522.132306989797, 'id_invMass_10_20_1.2_2.4': 318.56403530717444, 'invMass_2_3_1.2_2.4': 617.2480034530963, 'invMass_4_5_0_1.2': 382.28115984369197, 'id_invMass_3_4_0_1.2': 300.1202654811739, 'invMass_3_4_1.2_2.4': 626.4599486565648, 'id_invMass_4_5_1.2_2.4': 364.9791856478918, 'invMass_5_10_0_1.2': 1083.8296573892007, 'invMass_10_20_1.2_2.4': 325.48615044448616}

###########


###########

# MC

mc_fit_only_signal_integral = {'id_invMass_20_25_0_1.2': 668.4216131606287, 'invMass_5_10_1.2_2.4': 1687.9342906601005, 'id_invMass_10_20_0_1.2': 1756.808232580973, 'invMass_20_25_0_1.2': 683.648526071099, 'invMass_3_4_0_1.2': 1034.4937416251396, 'id_invMass_3_4_1.2_2.4': 641.1919726811818, 'invMass_4_5_1.2_2.4': 566.815195704907, 'iso_invMass_4_5_1.2_2.4': 398.7374252046873, 'iso_invMass_10_20_0_1.2': 366.4510048489833, 'id_invMass_2_3_1.2_2.4': 605.5955473156221, 'iso_invMass_20_25_0_1.2': 44.4666849943181, 'id_invMass_4_5_0_1.2': 689.08430186688, 'iso_invMass_3_4_1.2_2.4': 518.5201959326623, 'id_invMass_20_25_1.2_2.4': 520.1947326489092, 'iso_invMass_4_5_0_1.2': 528.652213420336, 'iso_invMass_5_10_0_1.2': 1221.39964510875, 'iso_invMass_2_3_1.2_2.4': 501.67108198279215, 'id_invMass_5_10_0_1.2': 2159.3923151599597, 'id_invMass_5_10_1.2_2.4': 1656.0711037527242, 'invMass_10_20_0_1.2': 1788.8214475132224, 'iso_invMass_10_20_1.2_2.4': 256.8603159647443, 'invMass_20_25_1.2_2.4': 528.0902778376383, 'iso_invMass_3_4_0_1.2': 368.64964121936947, 'iso_invMass_20_25_1.2_2.4': 33.54461370169754, 'iso_invMass_5_10_1.2_2.4': 867.6162640076074, 'id_invMass_10_20_1.2_2.4': 1393.9816082140014, 'invMass_2_3_1.2_2.4': 796.8777594658812, 'invMass_4_5_0_1.2': 823.7181745104252, 'id_invMass_3_4_0_1.2': 455.3340659240398, 'invMass_3_4_1.2_2.4': 691.1774305280425, 'id_invMass_4_5_1.2_2.4': 539.1536703083743, 'invMass_5_10_0_1.2': 2263.883682337992, 'invMass_10_20_1.2_2.4': 1416.0227829618384}
mc_fit_only_signal_integral_error = {'id_invMass_20_25_0_1.2': 32.660538508468335, 'invMass_5_10_1.2_2.4': 43.644369072955236, 'id_invMass_10_20_0_1.2': 45.14939424206131, 'invMass_20_25_0_1.2': 33.054503752047204, 'invMass_3_4_0_1.2': 67.1379671870571, 'id_invMass_3_4_1.2_2.4': 27.108998720911256, 'invMass_4_5_1.2_2.4': 30.929426117896867, 'iso_invMass_4_5_1.2_2.4': 21.553888068603225, 'iso_invMass_10_20_0_1.2': 39.50196727188444, 'id_invMass_2_3_1.2_2.4': 25.80333651981367, 'iso_invMass_20_25_0_1.2': 14.408978990776909, 'id_invMass_4_5_0_1.2': 36.731336995303714, 'iso_invMass_3_4_1.2_2.4': 24.52453863771126, 'id_invMass_20_25_1.2_2.4': 24.061618137614296, 'iso_invMass_4_5_0_1.2': 27.669717268297692, 'iso_invMass_5_10_0_1.2': 38.91580331459157, 'iso_invMass_2_3_1.2_2.4': 23.905625463785256, 'id_invMass_5_10_0_1.2': 50.613893162845265, 'id_invMass_5_10_1.2_2.4': 43.210153493712454, 'invMass_10_20_0_1.2': 45.434622866615705, 'iso_invMass_10_20_1.2_2.4': 16.964582705069382, 'invMass_20_25_1.2_2.4': 24.241308789057726, 'iso_invMass_3_4_0_1.2': 20.784199267124723, 'iso_invMass_20_25_1.2_2.4': 0, 'iso_invMass_5_10_1.2_2.4': 31.33867076176886, 'id_invMass_10_20_1.2_2.4': 39.68399990473135, 'invMass_2_3_1.2_2.4': 29.95960041690516, 'invMass_4_5_0_1.2': 70.0384326587707, 'id_invMass_3_4_0_1.2': 45.9004712196126, 'invMass_3_4_1.2_2.4': 28.242399195742653, 'id_invMass_4_5_1.2_2.4': 47.98589853817073, 'invMass_5_10_0_1.2': 51.74941158481472, 'invMass_10_20_1.2_2.4': 39.99553495190278}
mc_hist_count = {'id_invMass_20_25_0_1.2': 688.4793936014175, 'invMass_5_10_1.2_2.4': 1707.087739944458, 'id_invMass_10_20_0_1.2': 1765.5674991607666, 'invMass_20_25_0_1.2': 704.7390545606613, 'invMass_3_4_0_1.2': 1047.8137129545212, 'id_invMass_3_4_1.2_2.4': 672.1211304664612, 'invMass_4_5_1.2_2.4': 577.0549319982529, 'iso_invMass_4_5_1.2_2.4': 413.38122594356537, 'iso_invMass_10_20_0_1.2': 380.3078489303589, 'id_invMass_2_3_1.2_2.4': 632.66095662117, 'iso_invMass_20_25_0_1.2': 61.14192062616348, 'id_invMass_4_5_0_1.2': 719.6148540973663, 'iso_invMass_3_4_1.2_2.4': 544.4619081020355, 'id_invMass_20_25_1.2_2.4': 535.347626209259, 'iso_invMass_4_5_0_1.2': 551.1629350185394, 'iso_invMass_5_10_0_1.2': 1244.5508378744125, 'iso_invMass_2_3_1.2_2.4': 524.3503725528717, 'id_invMass_5_10_0_1.2': 2196.8180450201035, 'id_invMass_5_10_1.2_2.4': 1673.3174839019775, 'invMass_10_20_0_1.2': 1798.758409500122, 'iso_invMass_10_20_1.2_2.4': 269.0652103424072, 'invMass_20_25_1.2_2.4': 541.6423268318176, 'iso_invMass_3_4_0_1.2': 378.48994517326355, 'iso_invMass_20_25_1.2_2.4': 35.87927660346031, 'iso_invMass_5_10_1.2_2.4': 888.1175956726074, 'id_invMass_10_20_1.2_2.4': 1439.4891948699951, 'invMass_2_3_1.2_2.4': 805.7450399398804, 'invMass_4_5_0_1.2': 865.4791877269745, 'id_invMass_3_4_0_1.2': 467.3053948879242, 'invMass_3_4_1.2_2.4': 723.8928008079529, 'id_invMass_4_5_1.2_2.4': 554.8730586767197, 'invMass_5_10_0_1.2': 2298.2594512701035, 'invMass_10_20_1.2_2.4': 1463.5433368682861}

mc_fit_only_signal_integral_full = {'id_invMass_20_25_0_1.2': 910.347754905567, 'invMass_5_10_1.2_2.4': 2004.7339166650859, 'id_invMass_10_20_0_1.2': 2372.7931442221875, 'invMass_20_25_0_1.2': 927.6160197859116, 'invMass_3_4_0_1.2': 1277.0064527643322, 'id_invMass_3_4_1.2_2.4': 777.282216821456, 'invMass_4_5_1.2_2.4': 665.6345980634958, 'iso_invMass_4_5_1.2_2.4': 432.8137617664839, 'iso_invMass_10_20_0_1.2': 587.2122546805417, 'id_invMass_2_3_1.2_2.4': 852.3095994747849, 'iso_invMass_20_25_0_1.2': 122.8311218745726, 'id_invMass_4_5_0_1.2': 773.8719330097332, 'iso_invMass_3_4_1.2_2.4': 563.3208436997722, 'id_invMass_20_25_1.2_2.4': 756.0362120316937, 'iso_invMass_4_5_0_1.2': 567.1404467746635, 'iso_invMass_5_10_0_1.2': 1299.8174515350086, 'iso_invMass_2_3_1.2_2.4': 620.0844385246731, 'id_invMass_5_10_0_1.2': 2429.2219980413392, 'id_invMass_5_10_1.2_2.4': 1969.8041047552915, 'invMass_10_20_0_1.2': 2423.5369544355895, 'iso_invMass_10_20_1.2_2.4': 453.31231049759856, 'invMass_20_25_1.2_2.4': 769.0746911617291, 'iso_invMass_3_4_0_1.2': 422.4442390111359, 'iso_invMass_20_25_1.2_2.4': 91.8804948277954, 'iso_invMass_5_10_1.2_2.4': 951.4711571471709, 'id_invMass_10_20_1.2_2.4': 2057.577889698505, 'invMass_2_3_1.2_2.4': 1094.3020561282954, 'invMass_4_5_0_1.2': 926.2867480906389, 'id_invMass_3_4_0_1.2': 562.0463729705174, 'invMass_3_4_1.2_2.4': 842.6836249709316, 'id_invMass_4_5_1.2_2.4': 631.0846850053441, 'invMass_5_10_0_1.2': 2543.9211134126385, 'invMass_10_20_1.2_2.4': 2080.2813119183265}
mc_fit_only_signal_integral_error_full = {'id_invMass_20_25_0_1.2': 32.75429229843355, 'invMass_5_10_1.2_2.4': 47.326648528871104, 'id_invMass_10_20_0_1.2': 53.36534360277459, 'invMass_20_25_0_1.2': 33.042032983358986, 'invMass_3_4_0_1.2': 38.38457471220256, 'id_invMass_3_4_1.2_2.4': 29.450232080341433, 'invMass_4_5_1.2_2.4': 27.623179764451578, 'iso_invMass_4_5_1.2_2.4': 22.41716970570889, 'iso_invMass_10_20_0_1.2': 25.94781894860551, 'id_invMass_2_3_1.2_2.4': 30.19120534628788, 'iso_invMass_20_25_0_1.2': 26.888810215333546, 'id_invMass_4_5_0_1.2': 30.55340320984348, 'iso_invMass_3_4_1.2_2.4': 25.493866825028203, 'id_invMass_20_25_1.2_2.4': 29.25247588166469, 'iso_invMass_4_5_0_1.2': 28.339053521146056, 'iso_invMass_5_10_0_1.2': 39.176245676206335, 'iso_invMass_2_3_1.2_2.4': 26.19148252174379, 'id_invMass_5_10_0_1.2': 53.56791190110559, 'id_invMass_5_10_1.2_2.4': 46.9126931012353, 'invMass_10_20_0_1.2': 63.497221553718035, 'iso_invMass_10_20_1.2_2.4': 22.541512035990433, 'invMass_20_25_1.2_2.4': 29.59990564271794, 'iso_invMass_3_4_0_1.2': 22.263186043208652, 'iso_invMass_20_25_1.2_2.4': 22.48141503512337, 'iso_invMass_5_10_1.2_2.4': 32.71906014991631, 'id_invMass_10_20_1.2_2.4': 47.427310117946384, 'invMass_2_3_1.2_2.4': 35.00585928196889, 'invMass_4_5_0_1.2': 33.130608082759565, 'id_invMass_3_4_0_1.2': 28.17692281385799, 'invMass_3_4_1.2_2.4': 30.968836913624056, 'id_invMass_4_5_1.2_2.4': 27.147031144282273, 'invMass_5_10_0_1.2': 54.80140318838824, 'invMass_10_20_1.2_2.4': 48.51105528673553}
mc_hist_count_full = {'id_invMass_20_25_0_1.2': 943.8690876960754, 'invMass_5_10_1.2_2.4': 2038.9705715179443, 'id_invMass_10_20_0_1.2': 2390.606184542179, 'invMass_20_25_0_1.2': 963.7989716529846, 'invMass_3_4_0_1.2': 1294.2559858560562, 'id_invMass_3_4_1.2_2.4': 808.8062913417816, 'invMass_4_5_1.2_2.4': 684.5827771425247, 'iso_invMass_4_5_1.2_2.4': 451.6638252735138, 'iso_invMass_10_20_0_1.2': 599.4886977672577, 'id_invMass_2_3_1.2_2.4': 874.4862902164459, 'iso_invMass_20_25_0_1.2': 130.83453571796417, 'id_invMass_4_5_0_1.2': 801.2459251880646, 'iso_invMass_3_4_1.2_2.4': 586.6885828971863, 'id_invMass_20_25_1.2_2.4': 763.3461952209473, 'iso_invMass_4_5_0_1.2': 586.4246881008148, 'iso_invMass_5_10_0_1.2': 1330.5108889341354, 'iso_invMass_2_3_1.2_2.4': 643.3448632359505, 'id_invMass_5_10_0_1.2': 2466.8080466985703, 'id_invMass_5_10_1.2_2.4': 1999.8744564056396, 'invMass_10_20_0_1.2': 2442.527567446232, 'iso_invMass_10_20_1.2_2.4': 466.1335725784302, 'invMass_20_25_1.2_2.4': 777.5592002868652, 'iso_invMass_3_4_0_1.2': 433.0910003185272, 'iso_invMass_20_25_1.2_2.4': 98.42716157436371, 'iso_invMass_5_10_1.2_2.4': 983.1878795623779, 'id_invMass_10_20_1.2_2.4': 2110.9746017456055, 'invMass_2_3_1.2_2.4': 1108.3872079849243, 'invMass_4_5_0_1.2': 960.9768302440643, 'id_invMass_3_4_0_1.2': 578.2478903532028, 'invMass_3_4_1.2_2.4': 874.426837682724, 'id_invMass_4_5_1.2_2.4': 661.5235501527786, 'invMass_5_10_0_1.2': 2578.5344594717026, 'invMass_10_20_1.2_2.4': 2135.7014656066895}

# DATA

fit_signal_integral = {'id_invMass_20_25_0_1.2': 9181.516008599125, 'invMass_5_10_1.2_2.4': 766.8702591790072, 'id_invMass_10_20_0_1.2': 411.79426346714587, 'invMass_20_25_0_1.2': 9169.855414211277, 'invMass_3_4_0_1.2': 638.1800453606712, 'id_invMass_3_4_1.2_2.4': 456.13610831881334, 'invMass_4_5_1.2_2.4': 473.45582493609834, 'iso_invMass_4_5_1.2_2.4': 276.9470101087994, 'iso_invMass_10_20_0_1.2': 132.53537772096277, 'id_invMass_2_3_1.2_2.4': 544.630523005079, 'iso_invMass_20_25_0_1.2': 4910.19410913693, 'id_invMass_4_5_0_1.2': 346.33388586659294, 'iso_invMass_3_4_1.2_2.4': 390.31735387320026, 'id_invMass_20_25_1.2_2.4': 6486.822682619575, 'iso_invMass_4_5_0_1.2': 272.0836126821409, 'iso_invMass_5_10_0_1.2': 590.5475850266637, 'iso_invMass_2_3_1.2_2.4': 476.572228732819, 'id_invMass_5_10_0_1.2': 941.0203078343225, 'id_invMass_5_10_1.2_2.4': 700.3634857278888, 'invMass_10_20_0_1.2': 426.95514819617114, 'iso_invMass_10_20_1.2_2.4': 59.605788769434525, 'invMass_20_25_1.2_2.4': 6533.116883248389, 'iso_invMass_3_4_0_1.2': 246.61576112411967, 'iso_invMass_20_25_1.2_2.4': 1765.008018804622, 'iso_invMass_5_10_1.2_2.4': 434.508936252761, 'id_invMass_10_20_1.2_2.4': 306.8323533562787, 'invMass_2_3_1.2_2.4': 664.9499163684858, 'invMass_4_5_0_1.2': 378.73198811716367, 'id_invMass_3_4_0_1.2': 297.02159919622557, 'invMass_3_4_1.2_2.4': 618.1427554540849, 'id_invMass_4_5_1.2_2.4': 351.8583729304078, 'invMass_5_10_0_1.2': 1082.557002981367, 'invMass_10_20_1.2_2.4': 308.36001705859275}
fit_signal_integral_error = {'id_invMass_20_25_0_1.2': 100.9033310747355, 'invMass_5_10_1.2_2.4': 120.13716887384642, 'id_invMass_10_20_0_1.2': 21.190979878771973, 'invMass_20_25_0_1.2': 223.49823948020133, 'invMass_3_4_0_1.2': 77.74391909778953, 'id_invMass_3_4_1.2_2.4': 40.85233411480135, 'invMass_4_5_1.2_2.4': 53.04590025824674, 'iso_invMass_4_5_1.2_2.4': 17.785819072455244, 'iso_invMass_10_20_0_1.2': 23.238825241443358, 'id_invMass_2_3_1.2_2.4': 28.005580511046553, 'iso_invMass_20_25_0_1.2': 74.81461498554202, 'id_invMass_4_5_0_1.2': 46.946299903016936, 'iso_invMass_3_4_1.2_2.4': 38.67906906105717, 'id_invMass_20_25_1.2_2.4': 100.18026537964768, 'iso_invMass_4_5_0_1.2': 17.866169602999445, 'iso_invMass_5_10_0_1.2': 52.42906984157253, 'iso_invMass_2_3_1.2_2.4': 53.52103039924738, 'id_invMass_5_10_0_1.2': 31.87772927499001, 'id_invMass_5_10_1.2_2.4': 28.36321058126898, 'invMass_10_20_0_1.2': 81.15117910325306, 'iso_invMass_10_20_1.2_2.4': 8.599454458717704, 'invMass_20_25_1.2_2.4': 100.99597207733261, 'iso_invMass_3_4_0_1.2': 17.34661183510158, 'iso_invMass_20_25_1.2_2.4': 45.13514000128152, 'iso_invMass_5_10_1.2_2.4': 21.989048255451404, 'id_invMass_10_20_1.2_2.4': 18.55067470151647, 'invMass_2_3_1.2_2.4': 142.5489835461554, 'invMass_4_5_0_1.2': 53.172924094382566, 'id_invMass_3_4_0_1.2': 18.968852187062105, 'invMass_3_4_1.2_2.4': 85.09230233503935, 'id_invMass_4_5_1.2_2.4': 35.38308778768658, 'invMass_5_10_0_1.2': 145.83502375629993, 'invMass_10_20_1.2_2.4': 46.786632814626344}
bg_reduced = {'id_invMass_20_25_0_1.2': 9226.151844629512, 'invMass_5_10_1.2_2.4': 800.508189141512, 'id_invMass_10_20_0_1.2': 415.563012049739, 'invMass_20_25_0_1.2': 9210.579759162072, 'invMass_3_4_0_1.2': 627.7125242583734, 'id_invMass_3_4_1.2_2.4': 458.2739844035527, 'invMass_4_5_1.2_2.4': 483.26420436665376, 'iso_invMass_4_5_1.2_2.4': 289.9927714159512, 'iso_invMass_10_20_0_1.2': 136.18049920598, 'id_invMass_2_3_1.2_2.4': 558.2278021141877, 'iso_invMass_20_25_0_1.2': 4939.786687306672, 'id_invMass_4_5_0_1.2': 356.98321978568976, 'iso_invMass_3_4_1.2_2.4': 391.7510155368186, 'id_invMass_20_25_1.2_2.4': 6473.083070818184, 'iso_invMass_4_5_0_1.2': 274.52352505232466, 'iso_invMass_5_10_0_1.2': 600.8651668242364, 'iso_invMass_2_3_1.2_2.4': 486.7066769270225, 'id_invMass_5_10_0_1.2': 949.8875952144557, 'id_invMass_5_10_1.2_2.4': 721.7131609505172, 'invMass_10_20_0_1.2': 450.39867237062833, 'iso_invMass_10_20_1.2_2.4': 71.69352157390686, 'invMass_20_25_1.2_2.4': 6522.132306989797, 'iso_invMass_3_4_0_1.2': 254.4420015565268, 'iso_invMass_20_25_1.2_2.4': 1800.047607082659, 'iso_invMass_5_10_1.2_2.4': 448.24375876367947, 'id_invMass_10_20_1.2_2.4': 318.56403530717444, 'invMass_2_3_1.2_2.4': 617.2480034530963, 'invMass_4_5_0_1.2': 382.2613163679289, 'id_invMass_3_4_0_1.2': 300.1202654811739, 'invMass_3_4_1.2_2.4': 626.4599486565648, 'id_invMass_4_5_1.2_2.4': 364.9791856478918, 'invMass_5_10_0_1.2': 1083.8296573892007, 'invMass_10_20_1.2_2.4': 325.48615044448616}

fit_signal_integral_full = {'id_invMass_20_25_0_1.2': 10996.21460828482, 'invMass_5_10_1.2_2.4': 9156.495879898766, 'id_invMass_10_20_0_1.2': 8153.424949250544, 'invMass_20_25_0_1.2': 11051.511665123464, 'invMass_3_4_0_1.2': 55200.24157929562, 'id_invMass_3_4_1.2_2.4': 34645.51386841157, 'invMass_4_5_1.2_2.4': 4773.561600644311, 'iso_invMass_4_5_1.2_2.4': 1673.3998742273222, 'iso_invMass_10_20_0_1.2': 605.6340491196307, 'id_invMass_2_3_1.2_2.4': 47425.73171709934, 'iso_invMass_20_25_0_1.2': 5037.867062130475, 'id_invMass_4_5_0_1.2': 5625.875236477211, 'iso_invMass_3_4_1.2_2.4': 5948.129558590291, 'id_invMass_20_25_1.2_2.4': 8093.263437898787, 'iso_invMass_4_5_0_1.2': 2895.3641896335407, 'iso_invMass_5_10_0_1.2': 1203.0972060163692, 'iso_invMass_2_3_1.2_2.4': 13070.918739252964, 'id_invMass_5_10_0_1.2': 7808.345230213584, 'id_invMass_5_10_1.2_2.4': 8883.838648142879, 'invMass_10_20_0_1.2': 8344.178537275891, 'iso_invMass_10_20_1.2_2.4': 237.01174801956412, 'invMass_20_25_1.2_2.4': 8004.067657930198, 'iso_invMass_3_4_0_1.2': 6479.008419425483, 'iso_invMass_20_25_1.2_2.4': 1833.663115423078, 'iso_invMass_5_10_1.2_2.4': 836.2511548790523, 'id_invMass_10_20_1.2_2.4': 8037.099090211521, 'invMass_2_3_1.2_2.4': 65253.74243712779, 'invMass_4_5_0_1.2': 6196.482408158062, 'id_invMass_3_4_0_1.2': 25361.059378609185, 'invMass_3_4_1.2_2.4': 36969.16925149233, 'id_invMass_4_5_1.2_2.4': 5021.025716704396, 'invMass_5_10_0_1.2': 8637.28540857505, 'invMass_10_20_1.2_2.4': 8207.179690074101}
fit_signal_integral_error_full = {'id_invMass_20_25_0_1.2': 111.24118111654788, 'invMass_5_10_1.2_2.4': 140.2159056951089, 'id_invMass_10_20_0_1.2': 96.644052920673, 'invMass_20_25_0_1.2': 112.84358096482369, 'invMass_3_4_0_1.2': 714.1268784009818, 'id_invMass_3_4_1.2_2.4': 190.12575285474796, 'invMass_4_5_1.2_2.4': 232.65525096286163, 'iso_invMass_4_5_1.2_2.4': 41.834833665409214, 'iso_invMass_10_20_0_1.2': 26.385362923808696, 'id_invMass_2_3_1.2_2.4': 240.05936856205452, 'iso_invMass_20_25_0_1.2': 75.89736928620688, 'id_invMass_4_5_0_1.2': 80.05319933065128, 'iso_invMass_3_4_1.2_2.4': 78.66222535978572, 'id_invMass_20_25_1.2_2.4': 0.0, 'iso_invMass_4_5_0_1.2': 51.97864954162152, 'iso_invMass_5_10_0_1.2': 43.52027227353776, 'iso_invMass_2_3_1.2_2.4': 120.64096993821181, 'id_invMass_5_10_0_1.2': 101.30360478506942, 'id_invMass_5_10_1.2_2.4': 102.11366251290092, 'invMass_10_20_0_1.2': 103.53302763064565, 'iso_invMass_10_20_1.2_2.4': 16.431296766532082, 'invMass_20_25_1.2_2.4': 105.48731644410044, 'iso_invMass_3_4_0_1.2': 81.64238815320626, 'iso_invMass_20_25_1.2_2.4': 54.083729895677585, 'iso_invMass_5_10_1.2_2.4': 30.942749339795352, 'id_invMass_10_20_1.2_2.4': 96.98690470324449, 'invMass_2_3_1.2_2.4': 566.7448353207583, 'invMass_4_5_0_1.2': 116.7699164347403, 'id_invMass_3_4_0_1.2': 369.78675476215136, 'invMass_3_4_1.2_2.4': 627.4321290872689, 'id_invMass_4_5_1.2_2.4': 75.65812656547092, 'invMass_5_10_0_1.2': 274.56854127456745, 'invMass_10_20_1.2_2.4': 207.5544997027816}
bg_reduced_full = {'id_invMass_20_25_0_1.2': 11050.28319284532, 'invMass_5_10_1.2_2.4': 9175.53539529075, 'id_invMass_10_20_0_1.2': 8155.409662716823, 'invMass_20_25_0_1.2': 11114.288649292905, 'invMass_3_4_0_1.2': 55825.82948758763, 'id_invMass_3_4_1.2_2.4': 34736.353755323194, 'invMass_4_5_1.2_2.4': 4773.811387634887, 'iso_invMass_4_5_1.2_2.4': 1684.176126096083, 'iso_invMass_10_20_0_1.2': 609.6325621928629, 'id_invMass_2_3_1.2_2.4': 47521.26166599337, 'iso_invMass_20_25_0_1.2': 5073.594111064857, 'id_invMass_4_5_0_1.2': 5755.672539673904, 'iso_invMass_3_4_1.2_2.4': 5972.8899369394785, 'id_invMass_20_25_1.2_2.4': 8076.520255617308, 'iso_invMass_4_5_0_1.2': 2999.7034153483687, 'iso_invMass_5_10_0_1.2': 1224.343877745202, 'iso_invMass_2_3_1.2_2.4': 13110.594867698395, 'id_invMass_5_10_0_1.2': 7831.541668686939, 'id_invMass_5_10_1.2_2.4': 8863.381375892182, 'invMass_10_20_0_1.2': 8354.782722109758, 'iso_invMass_10_20_1.2_2.4': 258.11636840909466, 'invMass_20_25_1.2_2.4': 8023.396919420584, 'iso_invMass_3_4_0_1.2': 6553.4205525222715, 'iso_invMass_20_25_1.2_2.4': 1857.0688883759374, 'iso_invMass_5_10_1.2_2.4': 851.1384015225549, 'id_invMass_10_20_1.2_2.4': 8049.318531822656, 'invMass_2_3_1.2_2.4': 65822.27917977743, 'invMass_4_5_0_1.2': 6329.889905888558, 'id_invMass_3_4_0_1.2': 25625.379932504038, 'invMass_3_4_1.2_2.4': 37116.13592333776, 'id_invMass_4_5_1.2_2.4': 5036.356835238432, 'invMass_5_10_0_1.2': 8676.609699940165, 'invMass_10_20_1.2_2.4': 8209.978333197618}


###########



# BARREL #

for full in (0,1):

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
        
        isoBarrelHist = TH1F("isoBarrelHist", "", len(pt_ranges)-1, bins)
        isoBarrelHist.Sumw2()

        truthBarrelHist = TH1F("truthBarrelHist", "", len(pt_ranges)-1, bins)
        truthBarrelHist.Sumw2()
        truthBarrelHistDen = TH1F("truthBarrelHistDen", "", len(pt_ranges)-1, bins)
        truthBarrelHistDen.Sumw2()

        isoDataBarrelHist = TH1F("dataBarrelHist", "", len(pt_ranges)-1, bins)
        isoDataBarrelHist.Sumw2()
        
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
            
            if full:
                
                isoBarrelHist.SetBinContent(pti+1, mc_fit_only_signal_integral_full["iso_" + obsBaseName])
                isoBarrelHist.SetBinError(pti+1, mc_fit_only_signal_integral_error_full["iso_" + obsBaseName])
            
                barrelHist.SetBinContent(pti+1, mc_fit_only_signal_integral_full["id_" + obsBaseName])
                barrelHist.SetBinError(pti+1, mc_fit_only_signal_integral_error_full["id_" + obsBaseName])
    
                barrelHistDen.SetBinContent(pti+1, mc_fit_only_signal_integral_full[obsBaseName])
                barrelHistDen.SetBinError(pti+1, mc_fit_only_signal_integral_error_full[obsBaseName])
    
                truthBarrelHist.SetBinContent(pti+1, mc_hist_count_full["id_" + obsBaseName])
                truthBarrelHistDen.SetBinContent(pti+1, mc_hist_count_full[obsBaseName])
    
    
                ####### DATA #########
                
                isoDataBarrelHist.SetBinContent(pti+1, fit_signal_integral_full["iso_" + obsBaseName])
                isoDataBarrelHist.SetBinError(pti+1, fit_signal_integral_error_full["iso_" + obsBaseName])
            
                dataBarrelHist.SetBinContent(pti+1, fit_signal_integral_full["id_" + obsBaseName])
                dataBarrelHist.SetBinError(pti+1, fit_signal_integral_error_full["id_" + obsBaseName])
    
                dataBarrelHistDen.SetBinContent(pti+1, fit_signal_integral_full[obsBaseName])
                dataBarrelHistDen.SetBinError(pti+1, fit_signal_integral_error_full[obsBaseName])
    
                truthDataBarrelHist.SetBinContent(pti+1, bg_reduced_full["id_" + obsBaseName])
                truthDataBarrelHistDen.SetBinContent(pti+1, bg_reduced_full[obsBaseName])
            
            else:
                
                isoBarrelHist.SetBinContent(pti+1, mc_fit_only_signal_integral["iso_" + obsBaseName])
                isoBarrelHist.SetBinError(pti+1, mc_fit_only_signal_integral_error["iso_" + obsBaseName])
                
                barrelHist.SetBinContent(pti+1, mc_fit_only_signal_integral["id_" + obsBaseName])
                barrelHist.SetBinError(pti+1, mc_fit_only_signal_integral_error["id_" + obsBaseName])
    
                barrelHistDen.SetBinContent(pti+1, mc_fit_only_signal_integral[obsBaseName])
                barrelHistDen.SetBinError(pti+1, mc_fit_only_signal_integral_error[obsBaseName])
    
                truthBarrelHist.SetBinContent(pti+1, mc_hist_count["id_" + obsBaseName])
                truthBarrelHistDen.SetBinContent(pti+1, mc_hist_count[obsBaseName])
    
    
                ####### DATA #########
                
                isoDataBarrelHist.SetBinContent(pti+1, fit_signal_integral["iso_" + obsBaseName])
                isoDataBarrelHist.SetBinError(pti+1, fit_signal_integral_error["iso_" + obsBaseName])
    
                dataBarrelHist.SetBinContent(pti+1, fit_signal_integral["id_" + obsBaseName])
                dataBarrelHist.SetBinError(pti+1, fit_signal_integral_error["id_" + obsBaseName])
    
                dataBarrelHistDen.SetBinContent(pti+1, fit_signal_integral[obsBaseName])
                dataBarrelHistDen.SetBinError(pti+1, fit_signal_integral_error[obsBaseName])
    
                truthDataBarrelHist.SetBinContent(pti+1, bg_reduced["id_" + obsBaseName])
                truthDataBarrelHistDen.SetBinContent(pti+1, bg_reduced[obsBaseName])

        
        isoBarrelHistFactor = isoBarrelHist.Clone()
        isoBarrelHistFactor.Divide(barrelHist.Clone())
        isoBarrelHist.Divide(barrelHistDen)
        
        barrelHist.Divide(barrelHistDen)
        truthBarrelHist.Divide(truthBarrelHistDen)


        ####### DATA #########
        
        isoDataBarrelHistFactor = isoDataBarrelHist.Clone()
        isoDataBarrelHistFactor.Divide(dataBarrelHist.Clone())
        isoDataBarrelHist.Divide(dataBarrelHistDen)

        dataBarrelHist.Divide(dataBarrelHistDen)
        truthDataBarrelHist.Divide(truthDataBarrelHistDen)
        
        minimum = min(isoDataBarrelHist.GetMinimum(), isoBarrelHist.GetMinimum(), isoBarrelHistFactor.GetMinimum(), isoDataBarrelHistFactor.GetMinimum())
        maximum = max(isoDataBarrelHist.GetMaximum(), isoBarrelHist.GetMaximum(), isoBarrelHistFactor.GetMaximum(), isoDataBarrelHistFactor.GetMaximum())
        
        isoBarrelHist.SetMinimum(minimum-0.1)
        isoBarrelHist.SetMaximum(maximum+0.1)
        
        utils.formatHist(isoBarrelHist, utils.colorPalette[14], 0, True, True)
        
        isoBarrelHist.SetLineColor(kRed)
        isoBarrelHist.SetMarkerColor(kRed)
        isoBarrelHist.SetMarkerStyle(kOpenSquare)
        
        isoBarrelHistFactor.SetLineColor(kOrange)
        isoBarrelHistFactor.SetMarkerColor(kOrange)
        isoBarrelHistFactor.SetMarkerStyle(kOpenSquare)
        
        isoDataBarrelHist.SetMarkerStyle(kFullCircle)
        isoDataBarrelHist.SetLineColor(kBlack)
        
        isoDataBarrelHistFactor.SetMarkerStyle(kFullCircle)
        isoDataBarrelHistFactor.SetMarkerColor(kBlue)
        isoDataBarrelHistFactor.SetLineColor(kBlue)
        
        isoLegend = TLegend(.60,.40,.89,.60)
        isoLegend.SetNColumns(1)
        isoLegend.SetBorderSize(1)
        isoLegend.SetFillStyle(0)
        
        isoLegend.AddEntry(isoBarrelHist, "MC", 'p')
        isoLegend.AddEntry(isoDataBarrelHist, "Data", 'p')
        if plot_stability:
            isoLegend.AddEntry(isoBarrelHistFactor, "MC (med-iso)", 'p')
            isoLegend.AddEntry(isoDataBarrelHistFactor, "Data (med-iso)", 'p')

        #legend.AddEntry(barrelHistHistCount, "Signal Count Efficiency", 'p')
        isoBarrelHist.GetXaxis().SetTitle("p_{T}")
        if region == 0:
            isoBarrelHist.GetYaxis().SetTitle("barrel #varepsilon")
        else:
            isoBarrelHist.GetYaxis().SetTitle("endcaps #varepsilon")
        #isoBarrelHist.GetYaxis().SetTitle("#varepsilon")
        isoBarrelHist.Draw("p")
        isoDataBarrelHist.Draw("p same")
        if plot_stability:
            isoBarrelHistFactor.Draw("p same")
            isoDataBarrelHistFactor.Draw("p same")

        isoLegend.Draw("SAME")
        utils.stamp_plot("22.9")
        if region == 0:
            if full:
                c1.SaveAs("barrelGranHistFullIso.pdf")
            else:
                c1.SaveAs("barrelGranHistIso.pdf")
        else:
            if full:
                c1.SaveAs("endcapsGranHistFullIso.pdf")
            else:
                c1.SaveAs("endcapsGranHistIso.pdf")
    
    
        #Scale Factors
    
        isoDataBarrelHist.Divide(isoBarrelHist)
        isoDataBarrelHistFactor.Divide(isoBarrelHistFactor)
        isoDataBarrelHist.GetXaxis().SetTitle("pT")
        if region == 0:
            isoDataBarrelHist.GetYaxis().SetTitle("barrel scale factors")
        else:
            isoDataBarrelHist.GetYaxis().SetTitle("endcaps scale factors")
        #isoDataBarrelHist.GetYaxis().SetTitle("scale factor")
        isoDataBarrelHist.Draw("p")
        isoDataBarrelHistFactor.Draw("p same")
        utils.stamp_plot("22.9")
    
        if region == 0:
            if full:
                c1.SaveAs("barrelGranScaleFactorsFullIso.pdf")
            else:
                c1.SaveAs("barrelGranScaleFactorsIso.pdf")
        else:
            if full:
                c1.SaveAs("endcapsGranScaleFactorsFullIso.pdf")
            else:
                c1.SaveAs("endcapsGranScaleFactorsIso.pdf")
        
        
        ###### END OF ISOLATION
        


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
        if plot_stability:
            legend.AddEntry(truthBarrelHist, "MC Count", 'p')

        legend.AddEntry(dataBarrelHist, "Data", 'p')
        if plot_stability:
            legend.AddEntry(truthDataBarrelHist, "Data Count", 'p')
        #legend.AddEntry(barrelHistHistCount, "Signal Count Efficiency", 'p')
        barrelHist.GetXaxis().SetTitle("p_{T}")
        if region == 0:
            barrelHist.GetYaxis().SetTitle("barrel #varepsilon")
        else:
            barrelHist.GetYaxis().SetTitle("endcaps #varepsilon")

        barrelHist.Draw("p")
        if plot_stability:
            truthBarrelHist.Draw("p same")
        dataBarrelHist.Draw("p same")
        if plot_stability:
            truthDataBarrelHist.Draw("p same")
        #barrelHistHistCount.Draw("p same")

        legend.Draw("SAME")
        utils.stamp_plot("22.9")
        if region == 0:
            if full:
                c1.SaveAs("barrelGranHistFull.pdf")
            else:
                c1.SaveAs("barrelGranHist.pdf")
        else:
            if full:
                c1.SaveAs("endcapsGranHistFull.pdf")
            else:
                c1.SaveAs("endcapsGranHist.pdf")
    
    
        #Scale Factors
    
        dataBarrelHist.Divide(barrelHist)
        #dataBarrelHist.GetXaxis().SetTitle("pT")
        dataBarrelHist.GetXaxis().SetTitle("p_{T}")
        if region == 0:
            dataBarrelHist.GetYaxis().SetTitle("barrel scale factors")
        else:
            dataBarrelHist.GetYaxis().SetTitle("endcaps scale factors")
        #dataBarrelHist.GetYaxis().SetTitle("#varepsilon")
        dataBarrelHist.Draw("p")
        utils.stamp_plot("22.9")
    
        truthDataBarrelHist.Divide(truthBarrelHist)
        if plot_stability:
            truthDataBarrelHist.Draw("p same")
    
        if region == 0:
            if full:
                c1.SaveAs("barrelGranScaleFactorsFull.pdf")
            else:
                c1.SaveAs("barrelGranScaleFactors.pdf")
        else:
            if full:
                c1.SaveAs("endcapsGranScaleFactorsFull.pdf")
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
