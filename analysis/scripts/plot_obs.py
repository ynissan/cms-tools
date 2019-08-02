#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import os
import re
from datetime import datetime

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools/lib")
sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools/lib/classes")
import utils

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

gSystem.Load('LumiSectMap_C')
from ROOT import LumiSectMap

#lumi = 5746.370
#weight = lumi / utils.LUMINOSITY

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Plot skims for x1x2x1 process with BDTs.')
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
args = parser.parse_args()

output_file = None
# signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu100_dm3p28Chi20Chipm.root"
# bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dilepton_signal_bdt/low/single"
signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu100_dm7p39Chi20Chipm.root"
bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dilepton_signal_bdt/dm7/single"
data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_dilepton_signal_bdt/dm7/single"

bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_z/sum/type_sum"
data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_z/sum"

#signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_signal_bdt_no_new_dy/single/higgsino_mu100_dm7p39Chi20Chipm.root"
#bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_signal_bdt_no_new_dy/dm7/single"
#data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_signal_bdt_no_new_dy/dm7/single"



plot_data = True
plot_signal = False
plot_ratio = True
plot_rand = False
plot_fast = True

if args.output_file:
    output_file = args.output_file[0]
else:
    output_file = "obs_data_overflow.pdf"
######## END OF CMDLINE ARGUMENTS ########

def trackBDT(c):
    return c.trackBDT >= 0.2

def univBDT(c):
    return c.univBDT >= 0
    
def dilepBDT(c):
    return c.dilepBDT >= 0.1

def custom_cool(c):
    return c.dilepBDT >= 0.1 and c.univBDT >= 0 and c.tracks_dzVtx[0] <= 0.2 and c.tracks_dxyVtx[0] < 0.2 and c.tracks[0].Pt() < 15 and c.tracks[0].Pt() > 3 and abs(c.tracks[0].Eta()) < 2.4

def dilep_skim(c):
    return c.dilepBDT >= -0.3 and c.univBDT >= -0.4 and c.tracks[0].Pt() >= 3 and c.tracks[0].Pt() < 15 and c.tracks_dzVtx[0] < 0.1 and c.tracks_dxyVtx[0] < 0.1 and abs(c.tracks[0].Eta()) <= 2.4
    
def custom(c):
    return c.Met > 200 and c.dilepBDT >= 0.1 and c.univBDT >= 0 and c.tracks_dzVtx[0] <= 0.03 and c.tracks_dxyVtx[0] <= 0.03 and c.tracks[0].Pt() < 10 and c.tracks[0].Pt() > 3 and abs(c.tracks[0].Eta()) < 2.4 and c.dileptonPt <= 35 and c.pt3 >= 100

def custom_dpg(c):
    return c.Met > 200 and c.trackBDT >= 0.1 and c.dilepBDT >= 0.1 and c.univBDT >= 0 and c.tracks_dzVtx[0] <= 0.03 and c.tracks_dxyVtx[0] <= 0.03 and c.tracks[0].Pt() < 10 and c.tracks[0].Pt() > 5 and abs(c.tracks[0].Eta()) < 2.4 and c.dileptonPt <= 35  and c.pt3 >= 100

def step2(c):
    return c.Met > 200 and c.tracks[0].Pt() < 10 and c.tracks_dzVtx[0] <= 0.01 and c.tracks_dxyVtx[0] <= 0.01 and c.univBDT >= 0.1 and c.pt3 >= 225 and c.dilepBDT >= 0.15 and c.trackBDT >= 0.1 and abs(c.tracks[0].Eta()) < 1.8 and c.tracks[0].Pt() > 5

def step(c):
    return c.Met > 200 and c.trackBDT >= 0.1 and c.dilepBDT >= 0.15 and c.univBDT >= 0.1 and c.tracks_dzVtx[0] <= 0.03 and c.tracks_dxyVtx[0] <= 0.03 and c.tracks[0].Pt() < 10 and c.tracks[0].Pt() > 5 and abs(c.tracks[0].Eta()) < 2.4 and c.dileptonPt <= 35 and c.pt3 >= 100

def step3(c):
    return c.Met > 200 and c.tracks[0].Pt() < 10 and c.tracks_dzVtx[0] <= 0.01 and c.tracks_dxyVtx[0] <= 0.01 and c.univBDT >= 0.1 and c.pt3 >= 225 and c.dilepBDT >= 0.15 and c.trackBDT >= 0.1 and abs(c.tracks[0].Eta()) < 1.8 and c.tracks[0].Pt() > 5 and c.deltaR <= 1

def step2_200_250(c):
    return step2(c) and c.Met < 250

def step2_250(c):
    return step2(c) and c.Met > 250

def invMass(c):
    return c.invMass < 30

def metMht(c):
    return c.Met > 200 and c.Mht > 100

#and c.dilepHt >= 250 and c.NJets <= 3 and c.mt1 <= 50

histograms_defs = [
    { "obs" : "invMass", "minX" : 91.19 - 10.0, "maxX" : 91.19 + 10.0, "bins" : 30 },
    #{ "obs" : "invMass", "minX" : 0, "maxX" : 30, "bins" : 30 },
    # { "obs" : "trackBDT", "minX" : -1, "maxX" : 1, "bins" : 30 },
#     { "obs" : "univBDT", "minX" : -1, "maxX" : 1, "bins" : 30 },
#     { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30 },
#     { "obs" : "tracks[0].Eta()", "minX" : -3, "maxX" : 3, "bins" : 30 },
#     { "obs" : "tracks[0].Pt()", "minX" : 0, "maxX" : 30, "bins" : 30 },
#     { "obs" : "tracks_dxyVtx[0]", "minX" : 0, "maxX" : 0.05, "bins" : 30 },
#     { "obs" : "tracks_dzVtx[0]", "minX" : 0, "maxX" : 0.05, "bins" : 30 },
#     { "obs" : "dileptonPt", "minX" : 0, "maxX" : 100, "bins" : 30 },
#     { "obs" : "deltaPhi", "minX" : 0, "maxX" : 3.2, "bins" : 30 },
#     { "obs" : "deltaEta", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "deltaR", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "pt3", "minX" : 0, "maxX" : 300, "bins" : 30 },
#     { "obs" : "mtautau", "minX" : 0, "maxX" : 1000, "bins" : 30 },
#     { "obs" : "mt1", "minX" : 0, "maxX" : 100, "bins" : 30 },
#     { "obs" : "mt2", "minX" : 0, "maxX" : 100, "bins" : 30 },
#     { "obs" : "DeltaEtaLeadingJetDilepton", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "DeltaPhiLeadingJetDilepton", "minX" : 0, "maxX" : 4, "bins" : 30 },
#     { "obs" : "dilepHt", "minX" : 0, "maxX" : 400, "bins" : 30 },
#     { "obs" : "NJets", "minX" : 0, "maxX" : 7, "bins" : 7 },
#     { "obs" : "NTracks", "minX" : 0, "maxX" : 7, "bins" : 7 },
#     { "obs" : "Met", "minX" : 100, "maxX" : 700, "bins" : 30 },
#     { "obs" : "Mht", "minX" : 100, "maxX" : 700, "bins" : 30 },
]

cuts = [{"name":"none", "title": "No Cuts", "condition" : "1"},
#        {"name":"dilep_skim", "title": "dilep_skim", "funcs" : [dilep_skim, invMass]},     
        #{"name":"invMass", "title": "Inv Mass < 30", "funcs" : [invMass, dilep_skim]},
#        {"name":"metMht", "title": "MET > 200, Mht > 100", "funcs" : [metMht]},
#         {"name":"trackBDT", "title": "trackBDT >= 0.2", "funcs":[trackBDT]},
#         {"name":"univBDT", "title": "univBDT >= 0", "funcs":[univBDT]},
#         {"name":"dilepBDT", "title": "dilepBDT >= 0.1", "funcs":[dilepBDT]}
#        {"name":"custom", "title": "No Cuts", "funcs" : [custom, dilep_skim]},
#         {"name":"custom_dpg", "title": "No Cuts", "funcs" : [custom_dpg, dilep_skim]},
#         {"name":"step", "title": "No Cuts", "funcs" : [step]},
#         {"name":"step2", "title": "No Cuts", "funcs" : [step2]},
#         {"name":"step2_200_250", "title": "No Cuts", "funcs" : [step2_200_250]},
#         {"name":"step2_250", "title": "No Cuts", "funcs" : [step2_250]},
#         {"name":"step3", "title": "No Cuts", "funcs" : [step3]},
        ]

def styleHist(hist):
    hist.GetYaxis().SetTitleSize(10);
    hist.GetYaxis().SetTitleFont(43);
    hist.GetYaxis().SetTitleOffset(2.5);
    hist.GetYaxis().SetLabelFont(43); 
    hist.GetYaxis().SetLabelSize(10);

    hist.GetXaxis().SetTitleSize(10);
    hist.GetXaxis().SetTitleFont(43);
    hist.GetXaxis().SetTitleOffset(7.5);
    hist.GetXaxis().SetLabelFont(43); 
    hist.GetXaxis().SetLabelSize(10);

def createPlots(rootfiles, type, histograms, weight=1):
    print "Processing "
    print rootfiles
    lumiSecs = LumiSectMap()
    
    for f in rootfiles:
        print f
        rootFile = TFile(f)
        c = rootFile.Get('tEvent')
        if type == "data":
            lumis = rootFile.Get('lumiSecs')
            col = TList()
            col.Add(lumis)
            lumiSecs.Merge(col)
        nentries = c.GetEntries()
        print 'Analysing', nentries, "entries"
        for ientry in range(nentries):
            if ientry % 10000 == 0:
                print "Processing " + str(ientry)
            c.GetEntry(ientry)
            
            for cut in cuts:
                passed = True
                if cut.get("funcs") is not None:
                    for func in cut["funcs"]:
                        passed = func(c)
                        if not passed:
                            break
                if not passed:
                    continue
                
                for hist_def in histograms_defs:
                    histName =  cut["name"] + "_" + hist_def["obs"] + "_" + type
                    hist = histograms[histName]
                    if type != "data":
                        #print "Weight=", c.Weight
                        #print "weight=", weight
                        hist.Fill(eval('c.' + hist_def["obs"]), c.Weight * weight)
                    else:
                        hist.Fill(eval('c.' + hist_def["obs"]), 1)
        rootFile.Close()
    
    if type == "data":
        #return 3.939170474
        #return 35.574589421
        #return 35.493718415
        #return 27.360953311
        return 27.677964176
        #return utils.calculateLumiFromLumiSecs(lumiSecs)


def createPlotsFast(rootfiles, type, histograms, weight=1):
    print "Processing "
    print rootfiles
    lumiSecs = LumiSectMap()
    
    for f in rootfiles:
        print f
        rootFile = TFile(f)
        c = rootFile.Get('tEvent')
        if type == "data":
            lumis = rootFile.Get('lumiSecs')
            col = TList()
            col.Add(lumis)
            lumiSecs.Merge(col)
        
        for cut in cuts:
            for hist_def in histograms_defs:
                histName =  cut["name"] + "_" + hist_def["obs"] + "_" + type
                if type != "data":
                    hist = utils.getHistogramFromTree(histName, c, hist_def["obs"], hist_def["bins"], hist_def["minX"], hist_def["maxX"], "puWeight * (" + cut["condition"] + ")")
                else:
                    hist = utils.getHistogramFromTree(histName, c, hist_def["obs"], hist_def["bins"], hist_def["minX"], hist_def["maxX"], cut["condition"])
                if hist is None:
                    continue
                hist.GetXaxis().SetTitle("")
                hist.SetTitle("")
                #hist.Sumw2()
                if type != "data":
                    c.GetEntry(0)
                    print "Weight=", c.Weight, "*", weight
                    hist.Scale(c.Weight * weight)
                if histograms.get(histName) is None:
                    histograms[histName] = hist
                else:
                    histograms[histName].Add(hist)
        
        rootFile.Close()
    
    if type == "data":
        #return 3.939170474
        #return 35.574589421
        #return 35.493718415
        #return 27.360953311
        return 27.677786572
        #return utils.calculateLumiFromLumiSecs(lumiSecs)

def createRandomHist(name):
    h = utils.UOFlowTH1F(name, "", 100, -5, 5)
    h.Sumw2()
    h.FillRandom("gaus")
    styleHist(h)
    return h
    
def createCRPads(pId, ratioPads):
    histCPad = TPad("pad" + str(pId),"pad" + str(pId),0,0.21,1,1)
    histRPad = TPad("rpad" + str(pId),"rpad" + str(pId),0,0,1,0.2);
    ratioPads[pId] = []
    ratioPads[pId].append(histCPad)
    ratioPads[pId].append(histRPad)
    histCPad.SetBottomMargin(0)
    histRPad.SetTopMargin(0.05)
    histRPad.SetBottomMargin(0.25)
    histRPad.Draw()
    histCPad.Draw()
    return histCPad, histRPad

def plotRatio(c1, pad, memory, dataHist, newBgHist, hist_def):
    print "Ratio"
    pad.cd()
    rdataHist = dataHist.Clone()
    memory.append(rdataHist)
    rdataHist.Divide(utils.getStackSum(newBgHist))
    print "Minumum ", rdataHist.GetMinimum()
    print "Maximum", rdataHist.GetMaximum()
    rdataHist.SetMinimum(0)
    rdataHist.SetMaximum(2)
    rdataHist.GetXaxis().SetTitle(hist_def["obs"])
    rdataHist.GetYaxis().SetTitle("Data / BG")
    styleHist(rdataHist)
    rdataHist.GetYaxis().SetNdivisions(505)
    rdataHist.Draw("p")
    line = TLine(rdataHist.GetXaxis().GetXmin(),1,rdataHist.GetXaxis().GetXmax(),1);
    line.SetLineColor(kRed);
    line.Draw("SAME");
    memory.append(line)
    c1.Modified()

def main():
    print "Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    histograms = {}
    sumTypes = {}
    
    if not plot_rand:
        c2 = TCanvas("c2")
        c2.cd()
    
        bg_files = glob(bg_dir + "/*")

        for f in bg_files: 
            filename = os.path.basename(f).split(".")[0]
            types = filename.split("_")
            type = None
        
            if types[0] == "TTJets":
                type = "_".join(types[0:2])
            elif types[0] == "ST":
                type = "_".join(types[0:3])
            else:
                type = types[0]
            if type not in sumTypes:
                sumTypes[type] = {}
            #sumTypes[types[0]][types[1]] = True

        print sumTypes
        if not plot_fast:
            for cut in cuts:
                    for hist_def in histograms_defs:
                        baseName = cut["name"] + "_" + hist_def["obs"]
                        sigName = baseName + "_signal"
                        dataName = baseName + "_data"
                        histograms[sigName] = utils.UOFlowTH1F(sigName, "", hist_def["bins"], hist_def["minX"], hist_def["maxX"])
                        histograms[dataName] = utils.UOFlowTH1F(dataName, "", hist_def["bins"], hist_def["minX"], hist_def["maxX"])
                        utils.formatHist(histograms[sigName], utils.signalCp[0], 0.8)
                        for type in sumTypes:
                            if utils.existsInCoumpoundType(type):
                                continue
                            bgName = baseName + "_" + type
                            histograms[bgName] = utils.UOFlowTH1F(bgName, "", hist_def["bins"], hist_def["minX"], hist_def["maxX"])
                        for type in utils.compoundTypes:
                            bgName = baseName + "_" + type
                            histograms[bgName] = utils.UOFlowTH1F(bgName, "", hist_def["bins"], hist_def["minX"], hist_def["maxX"])
    
        calculated_lumi = None
        weight=0
        if plot_data:
            dataFiles = glob(data_dir + "/*")
            if plot_fast:
                calculated_lumi = createPlotsFast(dataFiles, "data", histograms)
            else:
                calculated_lumi = createPlots(dataFiles, "data", histograms)
            print "Calculated Luminosity: ", calculated_lumi
            weight = calculated_lumi * 1000
            print "Weight=", weight
    
        if plot_signal:
            if plot_fast:
                createPlotsFast([signal_dir], "signal", histograms, weight)
            else:
                createPlots([signal_dir], "signal", histograms, weight)
            
            utils.formatHist(histograms[sigName], utils.signalCp[0], 0.8)
    
        for type in sumTypes:
            if utils.existsInCoumpoundType(type):
                continue
            #if type == "ZJetsToNuNu" or type == "WJetsToLNu":
            #    continue
            print "Summing type", type
            rootfiles = glob(bg_dir + "/*" + type + "*.root")
            if plot_fast:
                createPlotsFast(rootfiles, type, histograms, weight)
            else:
                createPlots(rootfiles, type, histograms, weight)
    
        for cType in utils.compoundTypes:
            print "Creating compound type", cType
            rootFiles = []
            for type in utils.compoundTypes[cType]:
                if type not in sumTypes:
                    continue
                if "TTJets" in type:
                    rootFiles.extend(glob(bg_dir + "/" + type + ".root"))
                else:
                    rootFiles.extend(glob(bg_dir + "/" + type + "_*.root"))
            if len(rootFiles):
                if plot_fast:
                    createPlotsFast(rootFiles, cType, histograms, weight)
                else:
                    createPlots(rootFiles, cType, histograms, weight)
            else:
                print "**Couldn't find file for " + cType

    print "Plotting observable"

    c1 = TCanvas("c1", "c1", 800, 800)
    c1.cd()
    
    titlePad = TPad("titlePad", "",0.0,0.93,1.0,1.0)
    histPad = TPad("histPad", "",0.0,0.0,1.0,0.93)

    titlePad.Draw()

    t = TPaveText(0.0,0.93,1.0,1.0,"NB")
    t.SetFillStyle(0)
    t.SetLineColor(0)
    t.SetTextFont(40);
    t.AddText("No Cuts")
    t.Draw()
    histPad.Draw()
    histPad.Divide(2,2)

    c1.Print(output_file+"[");

    plot_num = 0

    pId = 1
    needToDraw = False

    memory = []
    
    ratioPads = {}
    
    for cut in cuts:
        cutName = cut["name"]
        print "Cut " + cutName
        t.Clear()
        t.AddText(cutName)
        t.Draw()
        titlePad.Update()
        pId = 1
        for hist_def in histograms_defs:
            needToDraw = True
            pad = histPad.cd(pId)
            histCPad = None
            histRPad = None
            if plot_ratio:
                if ratioPads.get(pId) is None:
                    histCPad, histRPad = createCRPads(pId, ratioPads)
                else:
                    histCPad = ratioPads[pId][0]
                    histRPad = ratioPads[pId][1]
                pad = histCPad
                pad.cd()
            
            hs = THStack(str(plot_num),"")
            plot_num += 1
            memory.append(hs)
            types = [k for k in utils.bgOrder]
            types = sorted(types, key=lambda a: utils.bgOrder[a])
            typesInx = []
            i = 0
            foundBg = False
            for type in types:
                hname = cut["name"] + "_" + hist_def["obs"] + "_" + type
                if plot_rand:
                    histograms[hname] = createRandomHist(hname)
                if histograms.get(hname) is not None:
                    hs.Add(histograms[hname])
                    typesInx.append(i)
                    foundBg = True
                i += 1
            sigHistName = cut["name"] + "_" + hist_def["obs"] + "_signal"
            dataHistName = cut["name"] + "_" + hist_def["obs"] + "_data"
            if plot_rand:
                histograms[dataHistName] = createRandomHist(dataHistName)
            dataHist = None
            sigHist = None
            sigMax = 0
            if plot_signal: 
                sigHist = histograms[sigHistName]
                sigMax = sigHist.GetMaximum()
            maximum = sigMax
            if foundBg:
                bgMax = hs.GetMaximum()
                maximum = max(bgMax, sigMax)
            if plot_data:
                dataHist = histograms[dataHistName]
                dataHist.SetMinimum(0.01)
                dataHist.SetMarkerStyle(kFullCircle)
                dataHist.SetMarkerSize(0.5)
                dataMax = dataHist.GetMaximum()
                maximum = max(dataMax, maximum)
            
            if maximum == 0:
                maximum == 10

            legend = TLegend(.20,.60,.89,.89)
            legend.SetNColumns(2)
            legend.SetBorderSize(0)
            legend.SetFillStyle(0)
            newBgHist = None
            memory.append(legend)
            if foundBg:
                newBgHist = utils.styledStackFromStack(hs, memory, legend, "", typesInx, True)
                #newBgHist.SetFillColorAlpha(fillC, 0.35)
                newBgHist.SetMaximum(maximum*1000)
                newBgHist.SetMinimum(0.01)
                newBgHist.Draw("hist")
                #utils.histoStyler(newBgHist)
                if not plot_ratio:
                    newBgHist.GetXaxis().SetTitle(hist_def["obs"])
                newBgHist.GetYaxis().SetTitle("Number of events")
                #newBgHist.GetYaxis().SetTitleOffset(1.15)
                #newBgHist.GetXaxis().SetLabelSize(0.055)
                c1.Modified()
            
            if plot_signal: 
                legend.AddEntry(sigHist, "signal", 'l')
            if foundBg and plot_signal:
                sigHist.SetMaximum(maximum)
            if plot_signal:
                sigHist.SetMinimum(0.01)
                sigHist.SetLineWidth(2)
            if foundBg and plot_signal:
                sigHist.Draw("HIST SAME")
            elif plot_signal:
                sigHist.Draw("HIST")
            
            if plot_data:
                dataHist.Draw("P SAME")
                legend.AddEntry(dataHist, "data", 'p')
            
            legend.Draw("SAME")
            pad.SetLogy()
            c1.Update()
            
            if plot_ratio:
                plotRatio(c1, histRPad, memory, dataHist, newBgHist, hist_def)

            pId += 1

            if pId > 4:
                pId = 1
                c1.Print(output_file);
                needToDraw = False;
            
            linBgHist = newBgHist.Clone()
            memory.append(linBgHist)
            linBgHist.SetMaximum(maximum*1.1)
            
            if plot_ratio:
                if ratioPads.get(pId) is None:
                    pad = histPad.cd(pId)
                    histCPad, histRPad = createCRPads(pId, ratioPads)
                else:
                    histCPad = ratioPads[pId][0]
                    histRPad = ratioPads[pId][1]
                pad = histCPad
                pad.cd()
            else:
                pad = histPad.cd(pId)
            
            pad.SetLogy(0)
            linBgHist.Draw("hist")
            if plot_signal:
                sigHist.Draw("HIST SAME")
            if plot_data:
                dataHist.Draw("P e SAME")
            legend.Draw("SAME")
            
            if plot_ratio:
                plotRatio(c1, histRPad, memory, dataHist, newBgHist, hist_def)
            
            pId += 1

            if pId > 4:
                pId = 1
                c1.Print(output_file);
                needToDraw = False;
            
        
        if needToDraw:
            for id in range(pId, 5):
                print "Clearing pad " + str(id)
                pad = histPad.cd(id)
                pad.Clear()
        c1.Print(output_file);
        
    c1.Print(output_file+"]");
    
    print "End: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')

main()


