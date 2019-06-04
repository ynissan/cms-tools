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
import utils

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

lumi = 5746.370
weight = lumi / utils.LUMINOSITY


####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Plot skims for x1x2x1 process with BDTs.')
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
args = parser.parse_args()

plot_data = True

output_file = None
# signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu100_dm3p28Chi20Chipm.root"
# bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dilepton_signal_bdt/low/single"
signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu100_dm7p39Chi20Chipm.root"
bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dilepton_signal_bdt/dm7/single"
data_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/data/skim_dilepton_signal_bdt/dm7/single"

#signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt/single/higgsino_mu100_dm12p84Chi20Chipm.root"
#bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dilepton_signal_bdt/high/single"

# signal_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/skim_dilepton_signal_bdt_no_preselection/single/higgsino_mu100_dm7p39Chi20Chipm.root"
# bg_dir = "/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/bg/skim_dilepton_signal_bdt_no_preselection/dm7/single"

#skim_dilepton_signal_bdt
#skim_signal_bdt
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

def invMass(c):
    return c.invMass < 30

#and c.dilepHt >= 250 and c.NJets <= 3 and c.mt1 <= 50

histograms_defs = [
    { "obs" : "invMass", "minX" : 0, "maxX" : 30, "bins" : 30 },
    { "obs" : "trackBDT", "minX" : -1, "maxX" : 1, "bins" : 30 },
    { "obs" : "univBDT", "minX" : -1, "maxX" : 1, "bins" : 30 },
    { "obs" : "dilepBDT", "minX" : -1, "maxX" : 1, "bins" : 30 },
    { "obs" : "tracks[0].Eta()", "minX" : -3, "maxX" : 3, "bins" : 30 },
    { "obs" : "tracks[0].Pt()", "minX" : 0, "maxX" : 30, "bins" : 30 },
    { "obs" : "tracks_dxyVtx[0]", "minX" : 0, "maxX" : 0.05, "bins" : 30 },
    { "obs" : "tracks_dzVtx[0]", "minX" : 0, "maxX" : 0.05, "bins" : 30 },
    { "obs" : "dileptonPt", "minX" : 0, "maxX" : 100, "bins" : 30 },
    { "obs" : "deltaPhi", "minX" : 0, "maxX" : 3.2, "bins" : 30 },
    { "obs" : "deltaEta", "minX" : 0, "maxX" : 4, "bins" : 30 },
    { "obs" : "deltaR", "minX" : 0, "maxX" : 4, "bins" : 30 },
    { "obs" : "pt3", "minX" : 0, "maxX" : 300, "bins" : 30 },
    { "obs" : "mtautau", "minX" : 0, "maxX" : 1000, "bins" : 30 },
    { "obs" : "mt1", "minX" : 0, "maxX" : 100, "bins" : 30 },
    { "obs" : "mt2", "minX" : 0, "maxX" : 100, "bins" : 30 },
    { "obs" : "DeltaEtaLeadingJetDilepton", "minX" : 0, "maxX" : 4, "bins" : 30 },
    { "obs" : "DeltaPhiLeadingJetDilepton", "minX" : 0, "maxX" : 4, "bins" : 30 },
    { "obs" : "dilepHt", "minX" : 0, "maxX" : 400, "bins" : 30 },
    { "obs" : "NJets", "minX" : 0, "maxX" : 7, "bins" : 7 },
    { "obs" : "NTracks", "minX" : 0, "maxX" : 7, "bins" : 7 },
    { "obs" : "Met", "minX" : 100, "maxX" : 700, "bins" : 30 },
    { "obs" : "Mht", "minX" : 100, "maxX" : 700, "bins" : 30 },
]

cuts = [{"name":"none", "title": "No Cuts"},
        {"name":"invMass", "title": "Inv Mass < 30", "funcs" : [invMass]},
#         {"name":"trackBDT", "title": "trackBDT >= 0.2", "funcs":[trackBDT]},
#         {"name":"univBDT", "title": "univBDT >= 0", "funcs":[univBDT]},
#         {"name":"dilepBDT", "title": "dilepBDT >= 0.1", "funcs":[dilepBDT]}
        #{"name":"custom", "title": "No Cuts", "funcs" : [custom]},
        #{"name":"custom_dpg", "title": "No Cuts", "funcs" : [custom_dpg]},
        #{"name":"step", "title": "No Cuts", "funcs" : [step]},
        #{"name":"step2", "title": "No Cuts", "funcs" : [step2]},
        #{"name":"step3", "title": "No Cuts", "funcs" : [step3]},
        ]

def createPlots(rootfiles, type, histograms):
    print "Processing "
    print rootfiles
    
    for f in rootfiles:
        print f
        rootFile = TFile(f)
        c = rootFile.Get('tEvent')
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
                        hist.Fill(eval('c.' + hist_def["obs"]), c.Weight * weight)
                    else:
                        hist.Fill(eval('c.' + hist_def["obs"]), 1)
            
def main():
    
    print "Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    histograms = {}
    
    bg_files = glob(bg_dir + "/*")
    sumTypes = {}
    memory = []

    for f in bg_files: 
        filename = os.path.basename(f).split(".")[0]
        types = filename.split("_")
        if types[0] == "TTJets" or types[0] == "ST":
            if types[0] not in sumTypes:
                sumTypes[filename] = {}
            sumTypes[filename][""] = True
        else:
            if types[0] not in sumTypes:
                sumTypes[types[0]] = {}
            sumTypes[types[0]][types[1]] = True

    print sumTypes
    #exit(0)
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
    
    createPlots([signal_dir], "signal", histograms)
    dataFiles = glob(data_dir + "/*")
    createPlots(dataFiles, "data", histograms)
    
    for type in sumTypes:
        if utils.existsInCoumpoundType(type):
            continue
        #if type == "ZJetsToNuNu" or type == "WJetsToLNu":
        #    continue
        print "Summing type", type
        rootfiles = glob(bg_dir + "/*" + type + "*.root")
        createPlots(rootfiles, type, histograms)
    
    for cType in utils.compoundTypes:
        print "Creating compound type", cType
        rootFiles = []
        for type in utils.compoundTypes[cType]:
            rootFiles.extend(glob(bg_dir + "/*" + type + "*.root"))
        if len(rootFiles):
            createPlots(rootFiles, cType, histograms)
        else:
            print "**Couldn't find file for " + cType
    
    print "Plotting observable"

    c1 = TCanvas("c1", "c1", 800, 800)
    
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
                if histograms.get(hname) is not None:
                    hs.Add(histograms[hname])
                    typesInx.append(i)
                    foundBg = True
                i += 1
            sigHistName = cut["name"] + "_" + hist_def["obs"] + "_signal"
            sigHist = histograms[sigHistName]
            sigMax = sigHist.GetMaximum()
            maximum = sigMax
            if foundBg:
                bgMax = hs.GetMaximum()
                maximum = max(bgMax, sigMax)

            legend = TLegend(.20,.60,.89,.89)
            legend.SetNColumns(2)
            legend.SetBorderSize(0)
            legend.SetFillStyle(0)
            memory.append(legend)
            if foundBg:
                newBgHist = utils.styledStackFromStack(hs, memory, legend, "", typesInx, True)
                #newBgHist.SetFillColorAlpha(fillC, 0.35)
                newBgHist.SetMaximum(maximum*1000)
                newBgHist.SetMinimum(0.01)
                newBgHist.Draw("hist")
                #utils.histoStyler(newBgHist)
                newBgHist.GetXaxis().SetTitle(hist_def["obs"])
                newBgHist.GetYaxis().SetTitle("Number of events")
                #newBgHist.GetYaxis().SetTitleOffset(1.15)
                #newBgHist.GetXaxis().SetLabelSize(0.055)
                c1.Modified()
            
                
            legend.AddEntry(sigHist, "signal", 'l')
            if foundBg:
                sigHist.SetMaximum(maximum)
            sigHist.SetMinimum(0.01)
            sigHist.SetLineWidth(2)
            sigHist.GetXaxis().SetTitle("GeV")
            if foundBg:
                sigHist.Draw("HIST SAME")
            else:
                sigHist.Draw("HIST")
            
            dataHistName = cut["name"] + "_" + hist_def["obs"] + "_data"
            dataHist = histograms[dataHistName]
            dataHist.SetMinimum(0.01)
            dataHist.SetMarkerStyle(kFullCircle)
            dataHist.Draw("P SAME")
            legend.AddEntry(dataHist, "data", 'p')
            
            legend.Draw("SAME")
            pad.SetLogy()
            c1.Update()

            pId += 1

            if pId > 4:
                pId = 1
                c1.Print(output_file);
                needToDraw = False;
            
            linBgHist = newBgHist.Clone()
            memory.append(linBgHist)
            linBgHist.SetMaximum(maximum*1.1)
            pad = histPad.cd(pId)
            pad.SetLogy(0)
            linBgHist.Draw("hist")
            sigHist.Draw("HIST SAME")
            dataHist.Draw("P e SAME")
            legend.Draw("SAME")
            
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


