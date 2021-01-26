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

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes"))
import utils
import analysis_ntuples
import plot_params

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

gSystem.Load('LumiSectMap_C')
from ROOT import LumiSectMap

#lumi = 5746.370
#weight = lumi / utils.LUMINOSITY

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Plot skims for x1x2x1 process with BDTs.')
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
parser.add_argument('-s', '--single', dest='single', help='Single', action='store_true')
parser.add_argument('-c', '--cut', nargs=1, help='Cut', required=False)
parser.add_argument('-obs', '--obs', nargs=1, help='Obs', required=False)
parser.add_argument('-lep', '--lep', dest='lep', help='Single', action='store_true')
#parser.add_argument('-bt', '--bg_retag', dest='bg_retag', help='Background Retagging', action='store_true')
parser.add_argument('-png', '--png', nargs=1, help='Png', required=False)
parser.add_argument('-type', '--type', nargs=1, help='Type', required=False)
parser.add_argument('-l', '--linear', dest='linear', help='Linear', action='store_true')
args = parser.parse_args()

output_file = None

plot_2l = args.lep
#bg_retag = args.bg_retag

plot_par = plot_params.default_params

if args.type is not None:
    plot_par = eval("plot_params." + args.type[0])

bg_retag = plot_par.bg_retag

if args.output_file:
    output_file = args.output_file[0]
else:
    output_file = "obs.pdf"
    
plot_single = args.single

large_version = plot_single

linear = args.linear

req_cut = None
req_obs = None
if plot_single:
    print "Printing Single Plot"
    if args.cut is None:
        print "Must provide cut with single option."
        exit(0)
    if args.obs is None:
        print "Must provide obs with single option."
        exit(0)
    req_cut = args.cut[0]
    req_obs = args.obs[0]

create_png = False
if args.png is not None:
    create_png = True
    png_name = args.png[0]
    if not os.path.isdir(png_name):
        os.mkdir(png_name)
    large_version = True

calculated_lumi = None

not_full = False

######## END OF CMDLINE ARGUMENTS ########

def funcBackground(x,par):
    return par[0]+par[1]*x[0]

def funcGaussian(x,par):
    return par[0]*TMath.Exp(-(x[0]-par[1])*(x[0]-par[1])/(2*par[2]*par[2]))

def funcFullModel(x,par):
    #print "HERE", x[0], par[0], par[1], par[2], par[3], par[4]
    #print x[0], (x[0]-par[1])*(x[0]-par[1]), (2*par[2]*par[2])
    return par[0]*TMath.Exp(-(x[0]-par[1])*(x[0]-par[1])/(2*par[2]*par[2]))+par[3]+par[4]*x[0]

def funcDoubleGaussian(x,par):
    return par[0]*TMath.Exp(-(x[0]-par[1])*(x[0]-par[1])/(2*par[2]*par[2])) + par[3]*TMath.Exp(-(x[0]-par[1])*(x[0]-par[1])/(2*par[4]*par[4]))

# 7 params
def funcFullModelDoubleGaussian(x,par):
    #print "HERE", x[0], par[0], par[1], par[2], par[3], par[4]
    #print x[0], (x[0]-par[1])*(x[0]-par[1]), (2*par[2]*par[2])
    return par[0]*TMath.Exp(-(x[0]-par[1])*(x[0]-par[1])/(2*par[2]*par[2]))+ par[3]*TMath.Exp(-(x[0]-par[1])*(x[0]-par[1])/(2*par[4]*par[4])) + par[5]+par[6]*x[0]

def funcFullModelDoubleGaussianQuadratic(x,par):
    #print "HERE", x[0], par[0], par[1], par[2], par[3], par[4]
    #print x[0], (x[0]-par[1])*(x[0]-par[1]), (2*par[2]*par[2])
    return par[0]*TMath.Exp(-(x[0]-par[1])*(x[0]-par[1])/(2*par[2]*par[2]))+ par[3]*TMath.Exp(-(x[0]-par[1])*(x[0]-par[1])/(2*par[4]*par[4])) + par[5]+par[6]*x[0] + par[7]*x[0]*x[0] + par[8]*x[0]*x[0]*x[0] + par[9]*x[0]*x[0]*x[0]*x[0]


def funcFullModelQuadratic(x,par):
    return par[0]*TMath.Exp(-(x[0]-par[1])*(x[0]-par[1])/(2*par[2]*par[2]))+par[3]+par[4]*x[0] + par[5]*x[0]*x[0]

def funcLorentzian(x,par):
    return (0.5*par[0]*par[1]/TMath.Pi()) / TMath.Max( 1.e-10,(x[0]-par[2])*(x[0]-par[2]) + .25*par[1]*par[1])

def funcFullModelLorentzian(x,par):
    return (0.5*par[0]*par[1]/TMath.Pi()) / TMath.Max( 1.e-10,(x[0]-par[2])*(x[0]-par[2]) + .25*par[1]*par[1]) +par[3]+par[4]*x[0]

def funcBackgroundQuadratic(x,par):
    return par[0]+par[1]*x[0]+par[2]*x[0]*x[0] + par[3]*x[0]*x[0]*x[0] + par[4]*x[0]*x[0]*x[0]*x[0]

def funcFullModelLorentzianQuadratic(x,par):
    return (0.5*par[0]*par[1]/TMath.Pi()) / TMath.Max( 1.e-10,(x[0]-par[2])*(x[0]-par[2]) + .25*par[1]*par[1]) +par[3]+par[4]*x[0] + par[5]*x[0]*x[0]



def styleHist(hist, onlyY = False):
    hist.GetYaxis().SetTitleSize(10);
    hist.GetYaxis().SetTitleFont(42);
    hist.GetYaxis().SetTitleOffset(2.5);
    hist.GetYaxis().SetLabelFont(42); 
    hist.GetYaxis().SetLabelSize(10);
    
    if not onlyY:
        hist.GetXaxis().SetTitleSize(10);
        hist.GetXaxis().SetTitleFont(42);
        hist.GetXaxis().SetTitleOffset(8);
        hist.GetXaxis().SetLabelFont(42); 
        hist.GetXaxis().SetLabelSize(10);

def createPlots(rootfiles, type, histograms, weight=1):
    print "Processing "
    print rootfiles
    
    for f in rootfiles:
        print f
        if os.path.basename(f) in plot_par.ignore_bg_files:
            print "File", f, "in ignore list. Skipping..."
            continue
        rootFile = TFile(f)
        c = rootFile.Get('tEvent')

        nentries = c.GetEntries()
        print 'Analysing', nentries, "entries"
        for ientry in range(nentries):
            if ientry % 10000 == 0:
                print "Processing " + str(ientry)
            c.GetEntry(ientry)
            
            for cut in plot_par.cuts:
                passed = True
                if cut.get("funcs") is not None:
                    for func in cut["funcs"]:
                        passed = func(c)
                        if not passed:
                            break
                if not passed:
                    continue
                
                for hist_def in plot_par.histograms_defs:
                    histName =  cut["name"] + "_" + hist_def["obs"] + "_" + type
                    hist = histograms[histName]
                    if type != "data":
                        #print "Weight=", c.Weight
                        #print "weight=", weight
                        if hist_def.get("func") is not None:
                            hist.Fill(hist_def["func"](c), c.Weight * weight)
                        else:
                            hist.Fill(eval('c.' + hist_def["obs"]), c.Weight * weight)
                    else:
                        hist.Fill(eval('c.' + hist_def["obs"]), 1)
        rootFile.Close()


def createPlotsFast(rootfiles, types, histograms, weight=1, prefix="", conditions=[""], no_weights = False):
    print "Processing "
    print rootfiles
    
    i = 0
    for f in rootfiles:
        if os.path.basename(f) in plot_par.ignore_bg_files:
            print "File", f, "in ignore list. Skipping..."
            continue
        rootFile = TFile(f)
        if not_full and i > 0:
            break
        i += 1
        print f
        c = rootFile.Get('tEvent')
        
        for typeIdx in range(len(types)):
            type = types[typeIdx]
            condition = conditions[typeIdx]

            for cut in plot_par.cuts:
                for hist_def in plot_par.histograms_defs:
                    if prefix != "":
                        histName =  prefix + "_" + cut["name"] + "_" + hist_def["obs"] + "_" + type
                    else:
                        histName =  cut["name"] + "_" + hist_def["obs"] + "_" + type
                    
                    conditionStr = "( " + cut["condition"] + " )"
                    if hist_def.get("condition") is not None:
                        conditionStr += " && ( " + hist_def["condition"] + " )"
                    if len(condition) > 0:
                        conditionStr += " && ( " + condition + " )"
                
                    drawString = ""
                
                    if no_weights:
                        drawString = " ( " + conditionStr + " )"
                    else:
                        drawString = plot_par.weightString[plot_par.plot_kind] + " * " + ((str(weight) + " * ") if type != "data" else "") + " ( " + conditionStr + " )"
                
                    #print "drawString", drawString
                    #print "conditionStr", conditionStr
                
                    formula = hist_def.get("formula") if hist_def.get("formula") is not None else hist_def.get("obs")
                
                    if plot_par.plot_log_x and hist_def["obs"] == "invMass":
                        hist = utils.getRealLogxHistogramFromTree(histName, c, formula, hist_def.get("bins"), hist_def.get("minX"), hist_def.get("maxX"), drawString, plot_par.plot_overflow)
                    else:
                        hist = utils.getHistogramFromTree(histName, c, formula, hist_def.get("bins"), hist_def.get("minX"), hist_def.get("maxX"), drawString, plot_par.plot_overflow)
                
                    if hist is None:
                        continue
                    #if "leptonF" in histName:
                    #    print "Made leptonFlavour for", histName, hist.GetXaxis().GetNbins()
                    hist.GetXaxis().SetTitle("")
                    hist.SetTitle("")
                    hist.Sumw2()

                    if histograms.get(histName) is None:
                        histograms[histName] = hist
                    else:
                        histograms[histName].Add(hist)
                
        
        rootFile.Close()
    
def createRandomHist(name):
    h = utils.UOFlowTH1F(name, "", 100, -5, 5)
    h.Sumw2()
    h.FillRandom("gaus")
    styleHist(h)
    return h
    
def createCRPads(pId, ratioPads, twoRations = False):
    print "Creating pads for id", pId

    histLowY = 0.25
    if twoRations:
        histLowY = 0.30
    histCPad = TPad("pad" + str(pId),"pad" + str(pId),0,histLowY,1,1)
    histCPad.SetLeftMargin(0.18)
    #histCPad.SetBottomMargin(0.16)
    if twoRations:
        histRPad = TPad("rpad" + str(pId),"rpad" + str(pId),0,0,1,0.15)
        histRPad.SetLeftMargin(0.18)
        histR2Pad = TPad("r2pad" + str(pId),"r2pad" + str(pId),0,0.15,1,0.3)
        histR2Pad.SetLeftMargin(0.18)
    else:
        histRPad = TPad("rpad" + str(pId),"rpad" + str(pId),0,0,1,0.24)
        histRPad.SetLeftMargin(0.18)
    ratioPads[pId] = []
    ratioPads[pId].append(histCPad)
    ratioPads[pId].append(histRPad)
    if twoRations:
        histR2Pad.SetBottomMargin(0.2)
        ratioPads[pId].append(histR2Pad)
        histRPad.SetTopMargin(0)
    histCPad.SetBottomMargin(0)
    if not twoRations:
        histRPad.SetTopMargin(0.05)
    histRPad.SetBottomMargin(0.4)
    #if twoRations:
    #    histR2Pad.SetTopMargin(0.05)
    #    histR2Pad.SetBottomMargin(0.25)
    histRPad.Draw()
    histCPad.Draw()
    if twoRations:
        histR2Pad.Draw()
    if twoRations:
        return histCPad, histRPad, histR2Pad
    return histCPad, histRPad

def plotRatio(c1, pad, memory, dataHist, newBgHist, hist_def, title = "Data / BG",setTitle = True, setStyle = False):
    print "Plotting ratio!"

    pad.cd()
    pad.SetGridx()
    pad.SetGridy()
    rdataHist = dataHist.Clone()
    memory.append(rdataHist)
    rdataHist.Divide(newBgHist)
    rdataHist.SetMinimum(-0.5)
    rdataHist.SetMaximum(3.5)
    if setTitle:
        rdataHist.GetXaxis().SetTitle(hist_def["units"] if hist_def.get("units") is not None else hist_def["obs"])
    else:
        rdataHist.GetXaxis().SetTitle("")
    rdataHist.GetYaxis().SetTitle(title)
    #if setStyle:
    utils.histoStyler(rdataHist, True)
    
    #elif setTitle:
    #    styleHist(rdataHist)
    #else:
    #    styleHist(rdataHist, True)
    rdataHist.GetYaxis().SetNdivisions(505)
    rdataHist.Draw("p")
    rdataHist.Draw("same e0")
    line = TLine(rdataHist.GetXaxis().GetXmin(),1,rdataHist.GetXaxis().GetXmax(),1);
    line.SetLineColor(kRed);
    line.Draw("SAME");
    memory.append(line)
    c1.Modified()

def createSumTypes(sumTypes):
    if plot_par.plot_bg:
        if bg_retag:
            for type in plot_par.bgReTagging:
                sumTypes[type] = {}
        else:
            bg_files = glob(plot_par.bg_dir + "/*")
    
            for f in bg_files: 
                filename = os.path.basename(f).split(".")[0]
                types = filename.split("_")
                type = None
        
                #if types[0] == "WJetsToLNu" or types[0] == "ZJetsToNuNu":
                #    continue
        
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

def createAllHistograms(histograms, sumTypes):
    
    foundReqObs = False
    foundReqCut = False
    
    if plot_single:
        plot_par.plot_title = False
        for obs in plot_par.histograms_defs:
            if obs["obs"] == req_obs:
                foundReqObs = True
                plot_par.histograms_defs = [obs]
                break
        if not foundReqObs:
            print "Could not find obs " + req_obs
            exit(0)
        for cut in plot_par.cuts:
            if cut["name"] == req_cut:
                foundReqCut = True
                plot_par.cuts = [cut]
                break
        if not foundReqCut:
            print "Could not find cut " + req_cut
            exit(0)
            
    if not plot_par.plot_rand:
        c2 = TCanvas("c2")
        c2.cd()
        
        if not plot_par.plot_fast:
            print "NOT PLOTTING FAST"
            for cut in plot_par.cuts:
                    for hist_def in plot_par.histograms_defs:
                        baseName = cut["name"] + "_" + hist_def["obs"]
                        sigName = baseName + "_signal"
                        dataName = baseName + "_data"
                        histograms[sigName] = utils.UOFlowTH1F(sigName, "", hist_def["bins"], hist_def["minX"], hist_def["maxX"])
                        histograms[dataName] = utils.UOFlowTH1F(dataName, "", hist_def["bins"], hist_def["minX"], hist_def["maxX"])
                        utils.formatHist(histograms[sigName], utils.signalCp[0], 0.8, large_version)
                        for type in sumTypes:
                            if utils.existsInCoumpoundType(type):
                                continue
                            bgName = baseName + "_" + type
                            histograms[bgName] = utils.UOFlowTH1F(bgName, "", hist_def["bins"], hist_def["minX"], hist_def["maxX"])
                        for type in utils.compoundTypes:
                            bgName = baseName + "_" + type
                            histograms[bgName] = utils.UOFlowTH1F(bgName, "", hist_def["bins"], hist_def["minX"], hist_def["maxX"])
        
        if plot_par.plot_data:
            dataFiles = glob(plot_par.data_dir + "/*")
            if plot_par.plot_fast:
                createPlotsFast(dataFiles, ["data"], histograms, 1, "", [""], plot_par.no_weights)
            else:
                createPlots(dataFiles, ["data"], histograms, 1, "", [""], plot_par.no_weights)
        
        global calculated_lumi
        weight=0
        
        if plot_par.calculatedLumi.get(plot_par.plot_kind) is not None:
            calculated_lumi = plot_par.calculatedLumi.get(plot_par.plot_kind) #should be in fb-1
            weight = calculated_lumi * 1000 #convert to pb-1
        else:
            calculated_lumi = utils.LUMINOSITY / 1000
            weight = utils.LUMINOSITY
            
        if plot_par.plot_data and plot_par.plot_sc:
            print "CREATING SC CATEGORY!"
            dataFiles = glob(plot_par.sc_data_dir + "/*")
            createPlotsFast(dataFiles, ["data"], histograms, 1, "sc", [""], plot_par.no_weights)
    
        if plot_par.plot_signal:
            if plot_par.plot_fast:
                print "Plotting Signal Fast"
                for signalFile in plot_par.signal_dir:
                    signalBasename = os.path.basename(signalFile)
                    createPlotsFast([signalFile], [signalBasename], histograms, weight, "", [""], plot_par.no_weights)
            else:
                for signalFile in plot_par.signal_dir:
                    signalBasename = os.path.basename(signalFile)
                    createPlots([signalFile], [signalBasename], histograms, weight, "", [""], plot_par.no_weights)
        if plot_par.plot_bg:
        
            allBgFiles = glob(plot_par.bg_dir + "/*.root")
            
            print sumTypes
            
            if bg_retag:
                print "GOT BG RETAG"
                bgFilesToPlot = []
                if plot_par.choose_bg_files:
                    print "In plot_par.choose_bg_files"
                    for bgChooseType in plot_par.choose_bg_files_list:
                        if utils.isCoumpoundType(bgChooseType):
                            print "Compound", bgChooseType
                            bgFilesToPlot.extend(utils.getFilesForCompoundType(bgChooseType, plot_par.bg_dir))
                            print bgFilesToPlot
                        else:
                            print "Not in compound", bgChooseType
                            bgFilesToPlot.extend(glob(plot_par.bg_dir + "/*" + bgChooseType + "_*.root"))
                else:
                    bgFilesToPlot = allBgFiles
        
                typesArr = [type for type in sumTypes]
                condArr = [plot_par.bgReTagging[type] for type in typesArr]

                if plot_par.plot_fast:
                    createPlotsFast(bgFilesToPlot, typesArr, histograms, str(weight), "", condArr, plot_par.no_weights)
                else:
                    createPlots(bgFilesToPlot, typesArr, histograms, str(weight), "", condArr, plot_par.no_weights)
                    
            else:
                for type in sumTypes:
                    if utils.existsInCoumpoundType(type):
                        continue
                    #if type == "ZJetsToNuNu" or type == "WJetsToLNu":
                    #    continue
                    if plot_par.choose_bg_files and type not in plot_par.choose_bg_files_list:
                        print "Skipping type", type, "because not in chosen list"
                        continue
                    print "Summing type", type
                    rootfiles = glob(plot_par.bg_dir + "/*" + type + "_*.root")
                    if plot_par.plot_fast:
                        createPlotsFast(rootfiles, [type], histograms, weight, "", [""], plot_par.no_weights)
                    else:
                        createPlots(rootfiles, [type], histograms, weight, "", [""], plot_par.no_weights)

                for cType in utils.compoundTypes:
            
                    if plot_par.choose_bg_files and cType not in plot_par.choose_bg_files_list:
                        print "Skipping cType", cType, "because not in chosen list"
                        continue
            
                    print "Creating compound type", cType
            
                    rootFiles = utils.getFilesForCompoundType(cType, plot_par.bg_dir)
                    if len(rootFiles):
                        if plot_par.plot_fast:
                            createPlotsFast(rootFiles, [cType], histograms, weight, "", [""], plot_par.no_weights)
                        else:
                            createPlots(rootFiles, [cType], histograms, weight, "", [""], plot_par.no_weights)
                    else:
                        print "**Couldn't find file for " + cType
        
            if plot_par.plot_sc:
                print "CREATING SC CATEGORY!"
            
                bgFilesToPlot = []
                if plot_par.choose_bg_files and plot_par.choose_bg_files_for_sc:
                    for bgChooseType in plot_par.choose_bg_files_list:
                        if utils.isCoumpoundType(bgChooseType):
                            print bgChooseType, "is a compound type!"
                            bgFilesToPlot.extend(utils.getFilesForCompoundType(bgChooseType, plot_par.sc_bg_dir))
                        else:
                            bgFilesToPlot.extend(glob(plot_par.sc_bg_dir + "/*" + bgChooseType + "_*.root"))
                else:
                    bgFilesToPlot = glob(plot_par.sc_bg_dir + "/*")

                createPlotsFast(bgFilesToPlot, ["bg"], histograms, weight, "sc", [""], plot_par.no_weights)
        
        if plot_par.plot_data and plot_par.blind_data and plot_par.plot_signal:
            for cut in plot_par.cuts:
                for hist_def in plot_par.histograms_defs:
                    firstSignalName = os.path.basename(plot_par.signal_dir[0])
                    
                    signal_hist = histograms[cut["name"] + "_" + hist_def["obs"] + "_" + firstSignalName]
                    
                    prefixes = [""]
                    if plot_par.plot_sc:
                        prefixes.append("sc")
                    for prefix in prefixes:
                        histName = None
                        if prefix != "":
                            histName =  prefix + "_" + cut["name"] + "_" + hist_def["obs"] + "_data"
                        else:
                            histName =  cut["name"] + "_" + hist_def["obs"] + "_data"
                        data_hist = histograms[histName]
                        
                        bg_hist = None
                        
                        types = []
                        if bg_retag:
                            types = [k for k in plot_par.bgReTagging]
                            types = sorted(types, key=lambda a: plot_par.bgReTaggingOrder[a])
                        else:
                            types = [k for k in utils.bgOrder]
                            types = sorted(types, key=lambda a: utils.bgOrder[a])
                        for type in types:
                            hname = cut["name"] + "_" + hist_def["obs"] + "_" + type
                            if histograms.get(hname) is not None:
                                if bg_hist is None:
                                    bg_hist = histograms[hname].Clone()
                                else:
                                    bg_hist.Add(histograms[hname])

                        for i in range(1,data_hist.GetNbinsX() + 1):
                            data_num = data_hist.GetBinContent(i)
                            signal_num = signal_hist.GetBinContent(i)
                            bg_num = bg_hist.GetBinContent(i)
                            if data_num == 0:
                                continue
                            if bg_num == 0:
                                data_hist.SetBinContent(i, 0)
                                continue
                            if ((0.1 * signal_num / math.sqrt(bg_num)) > 0.1):
                                print "Blinding bin", i, "for", histName
                                data_hist.SetBinContent(i, 0)

def saveHistogramsToFile(histograms):
    nFile = TFile(plot_par.histrograms_file, "recreate")
    for k in histograms:
        histograms[k].Write(k)
    nFile.Close()

def loadAllHistograms(histograms):
    nFile = TFile(plot_par.histrograms_file, "read")
    keys = nFile.GetListOfKeys()
    for key in keys:
        name = key.GetName()#histogram name
        h = nFile.Get(name)
        h.SetDirectory(0)
        histograms[name] = h
    nFile.Close()


def main():
    print "Start: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    #deltaM = utils.getDmFromFileName(plot_par.signal_dir[0])
    #print "deltaM=" + deltaM

    histograms = {}
    sumTypes = {}
    fit_funcs = {}
    fit_hist_integral = {}
    fit_full_integral = {}
    fit_signal_integral = {}
    fit_bg_integral = {}
    hist_signal_integral = {}
    
    errorStr = ""
    if plot_par.plot_error:
        errorStr = "e"
    
    plotStr = "HIST"
    if plot_par.plot_point:
        plotStr = "p"
    if plot_par.nostack:
        plotStr += " nostack"
    
    createSumTypes(sumTypes)
    
    if plot_par.load_histrograms_from_file and os.path.isfile(plot_par.histrograms_file):
        print "Loading histogram from file", plot_par.load_histrograms_from_file
        loadAllHistograms(histograms)
    else:
        print "Creating histogram from scratch"
        createAllHistograms(histograms, sumTypes)
    
    if plot_par.save_histrograms_to_file and not os.path.isfile(plot_par.histrograms_file):
        saveHistogramsToFile(histograms)
    
    global calculated_lumi  
    calculated_lumi= plot_par.calculatedLumi.get(plot_par.plot_kind)
    print "plot_par.plot_kind", plot_par.plot_kind
    print "plot_par.calculatedLumi", plot_par.calculatedLumi
    print "calculated_lumi", calculated_lumi
        
    print "Plotting observable"

    c1 = TCanvas("c1", "c1", 800, 800)
    
    #if plot_single:
    #    c1.SetBottomMargin(0.16)
    #    c1.SetLeftMargin(0.18)
    
    c1.cd()
    
    titlePad = None
    histPad = None
    t = None
    if plot_par.plot_title and not large_version:
        titlePad = TPad("titlePad", "",0.0,0.93,1.0,1.0)
        histPad = TPad("histPad", "",0.0,0.0,1.0,0.93)
        titlePad.Draw()
        t = TPaveText(0.0,0.93,1.0,1.0,"NB")
        t.SetFillStyle(0)
        t.SetLineColor(0)
        t.SetTextFont(40);
        t.AddText("No Cuts")
        t.Draw()
    else:
        histPad = c1
    
    histPad.Draw()
    if not large_version:
        histPad.Divide(2,2)
    
    canvasFile = None
    if plot_par.create_canvas:
        canvasFile = TFile("canvas_" + output_file.split(".")[0] + ".root", "recreate")
    
    if not create_png:
        c1.Print(output_file+"[");

    plot_num = 0

    pId = 1
    needToDraw = False

    memory = []
    
    ratioPads = {}
    
    for cut in plot_par.cuts:
        
        sigNum = 0
        bgNum = 0
        
        cutName = cut["name"]
        print "Cut " + cutName
        if plot_par.plot_title and not large_version:
            t.Clear()
            t.AddText(cut["title"])
            t.Draw()
            titlePad.Update()
        pId = 1
        for hist_def in plot_par.histograms_defs:
            
            needToDraw = True
            pad = None
            if large_version:
                pad = histPad.cd()
            else:
                pad = histPad.cd(pId)
            if not plot_par.plot_ratio:
                pad.SetBottomMargin(0.16)
                pad.SetLeftMargin(0.18)
            histCPad = None
            histRPad = None
            histR2Pad = None
            if plot_par.plot_ratio or plot_par.plot_custom_ratio > 0:
                if large_version or ratioPads.get(pId) is None:
                    if (plot_par.plot_sc and plot_par.plot_data) or plot_par.plot_custom_ratio > 1:
                        histCPad, histRPad, histR2Pad = createCRPads(pId, ratioPads, True)
                    else:
                        histCPad, histRPad = createCRPads(pId, ratioPads)
                else:
                    histCPad = ratioPads[pId][0]
                    histRPad = ratioPads[pId][1]
                    if (plot_par.plot_sc and plot_par.plot_data) or plot_par.plot_custom_ratio > 1:
                        histR2Pad = ratioPads[pId][2]
                pad = histCPad
                pad.cd()
            
            #print "*", ratioPads
            #print histCPad, histRPad
            #exit(0)
            hs = THStack(str(plot_num),"")
            plot_num += 1
            memory.append(hs)
            types = []
            if bg_retag:
                types = [k for k in plot_par.bgReTagging]
                types = sorted(types, key=lambda a: plot_par.bgReTaggingOrder[a])
            else:
                types = [k for k in utils.bgOrder]
                types = sorted(types, key=lambda a: utils.bgOrder[a])
            typesInx = []
            i = 0
            foundBg = False
            
            # normalise BG histograms:
            if plot_par.normalise:
                bgSum = 0
                for type in types:
                    hname = cut["name"] + "_" + hist_def["obs"] + "_" + type
                    if histograms.get(hname) is not None:
                        bgSum += histograms[hname].Integral()
                if bgSum > 0:
                    for type in types:
                        hname = cut["name"] + "_" + hist_def["obs"] + "_" + type
                        if histograms.get(hname) is not None and bgSum > 0:
                            histograms[hname].Scale(1./bgSum)

            for type in types:
                hname = cut["name"] + "_" + hist_def["obs"] + "_" + type
                if plot_par.plot_rand:
                    histograms[hname] = createRandomHist(hname)
                if histograms.get(hname) is not None:
                    hs.Add(histograms[hname])
                    typesInx.append(i)
                    foundBg = True
                i += 1
            
            efficiencies = {}
            
            if plot_par.plot_efficiency and bg_retag:
                for efficiency in plot_par.efficiencies:
                    #print efficiency
                    numerator = 0
                    denominator = 0
                    for type in efficiency["numerator"]:
                        hname = cut["name"] + "_" + hist_def["obs"] + "_" + type
                        numerator += histograms[hname].Integral()
                    for type in efficiency["denominator"]:
                        hname = cut["name"] + "_" + hist_def["obs"] + "_" + type
                        denominator += histograms[hname].Integral()
                    
                    if denominator == 0:
                        efficiencies[efficiency["name"]] = -1
                    else:
                        efficiencies[efficiency["name"]] = numerator / denominator
            
            print efficiencies
            
            dataHistName = cut["name"] + "_" + hist_def["obs"] + "_data"
            if plot_par.plot_rand:
                histograms[dataHistName] = createRandomHist(dataHistName)
            
            dataHist = None
            sigHists = []
            sigHistsBaseNames = []
            sigHistsNames = []
            sigMax = 0
            if plot_par.plot_signal: 
                for i in range(len(plot_par.signal_dir)):
                    signalFile = plot_par.signal_dir[i]
                    signalBasename = os.path.basename(signalFile)
                    sigHistsBaseNames.append(signalBasename.split(".")[0].split("_")[-1])
                    sigHistName = cut["name"] + "_" + hist_def["obs"] + "_" + signalBasename
                    sigHistsNames.append(sigHistName)
                    sigHist = histograms[sigHistName]
                    if plot_par.normalise:
                        sigHist.Scale(1./sigHist.Integral())
                    print sigHistName, sigHist.GetMaximum()
                    sigHists.append(sigHist)
                    utils.formatHist(sigHist, utils.signalCp[i], 0.8, large_version)
                    sigMax = max(sigHist.GetMaximum(), sigMax)
            maximum = sigMax
            if foundBg:
                bgMax = hs.GetMaximum()
                print "Bg max:", bgMax
                maximum = max(bgMax, sigMax)
            if plot_par.plot_data:
                dataHist = histograms[dataHistName]
                if plot_par.normalise and dataHist.Integral() > 0:
                    dataHist.Scale(1./dataHist.Integral())
                if not (linear and plot_single):
                    dataHist.SetMinimum(0.0001)
                else:
                    dataHist.SetMinimum(0)
                dataHist.SetMarkerStyle(kFullCircle)
                if large_version:
                    dataHist.SetMarkerSize(1)
                else:
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
                newBgHist = None
                if plot_par.solid_bg:
                    newBgHist = hs.GetStack().Last().Clone("newBgHist")
                    memory.append(newBgHist)
                    utils.formatHist(newBgHist, utils.colorPalette[6], 0.35, True, large_version)
                    lineC = TColor.GetColor(utils.colorPalette[6]["fillColor"])
        
                    #newHist.SetMarkerColorAlpha(colorPalette[colorI]["markerColor"], 0.9)
        
                    if plot_par.plot_point:
                        newBgHist.SetMarkerColorAlpha(lineC, 1)
                        newBgHist.SetMarkerStyle(colorPalette[colorI]["markerStyle"])
                        newBgHist.SetLineColor(lineC)
                    else:
                        newBgHist.SetMarkerColorAlpha(lineC, 0.9)
        
                    if legend is not None:
                        #print "Adding to legend " + hist.GetName().split("_")[-1]
                        if plot_par.plot_point:
                            legend.AddEntry(newBgHist, "SM Background", 'p')
                        else:
                            legend.AddEntry(newBgHist, "SM Background", 'F')
                else:
                    newBgHist = utils.styledStackFromStack(hs, memory, legend, "", typesInx, True, large_version, plot_par.plot_point)
                    #Will hang otherwise!
                    SetOwnership(newBgHist, False)
                    #newBgHist.SetFillColorAlpha(fillC, 0.35)
                if not (linear and plot_single):
                    newBgHist.SetMaximum(maximum*1000)
                else:
                    newBgHist.SetMaximum(maximum*1.1)
                if not (linear and plot_single):
                    newBgHist.SetMinimum(0.0001)
                else:
                    newBgHist.SetMinimum(0)
                
                newBgHist.Draw(plotStr + errorStr)
                # h = newBgHist.GetStack().Last()
#                 h.SetMarkerColorAlpha(kBlack, 1)
#                 h.SetMarkerStyle(kOpenCross)
#                 h.SetLineColor(kBlack)
#                 h.Draw("p e same")

                utils.histoStyler(newBgHist)
                
                if newBgHist is not None and (plot_par.solid_bg or newBgHist.GetNhists() > 0):
                    if not plot_par.plot_ratio:
                        newBgHist.GetXaxis().SetTitle(hist_def["units"] if hist_def.get("units") is not None else hist_def["obs"])
                    newBgHist.GetYaxis().SetTitle("Events")
                    newBgHist.GetYaxis().SetTitleOffset(1.15)
                
                
                #newBgHist.GetXaxis().SetLabelSize(0.055)
                c1.Modified()
            else:
                utils.histoStyler(dataHist)
                if not plot_par.plot_ratio:
                    dataHist.GetXaxis().SetTitle(hist_def["units"] if hist_def.get("units") is not None else hist_def["obs"])
                dataHist.GetYaxis().SetTitle("Events")
                dataHist.GetYaxis().SetTitleOffset(1.15)
                if not (linear and plot_single):
                    print "Setting max", maximum*1000
                    dataHist.SetMaximum(maximum*1000)
                else:
                    dataHist.SetMaximum(maximum*1.1)
                if not (linear and plot_single):
                    print "NOT LINER!"
                    print "dataHist.SetMinimum(0.0001)"
                    dataHist.SetMinimum(0.0001)
                else:
                    print " LINER!"
                    print "dataHist.SetMinimum(0)"
                    dataHist.SetMinimum(0)
            
            if plot_par.plot_signal:
                for i in range(len(sigHists)):
                    legend.AddEntry(sigHists[i], sigHistsBaseNames[i], 'l')
            if foundBg and plot_par.plot_signal:
                for i in range(len(sigHists)):
                    sigHists[i].SetMaximum(maximum)
            if plot_par.plot_signal:
                for i in range(len(sigHists)):
                    if not (linear and plot_single):
                        sigHists[i].SetMinimum(0.0001)
                    else:
                        sigHists[i].SetMinimum(0)
                    sigHists[i].SetLineWidth(2)
            if foundBg and plot_par.plot_signal:
                for i in range(len(sigHists)):
                    sigHists[i].Draw("HIST SAME " + errorStr)
            elif plot_par.plot_signal:
                for i in range(len(sigHists)):
                    sigHists[i].Draw("HIST" + errorStr)
            
            if plot_par.plot_significance and hist_def["obs"] == "invMass":
                accBgHist = None
                for bgHist in newBgHist.GetHists():
                    if accBgHist is None:
                        accBgHist = bgHist.Clone()
                    else:
                        accBgHist.Add(bgHist)
                significance = utils.calcSignificance(sigHists[0], accBgHist)
                # sigNum = sigHist.Integral(1, sigHist.FindBin(8))
#                 bgNum = 0
#                 for bgHist in newBgHist.GetHists():
#                     bgNum += bgHist.Integral(1, bgHist.FindBin(8))
#                 significance = 0.1*sigNum/math.sqrt(bgNum)
                print "cutName ", cutName, "sig", significance
                if not large_version and plot_par.plot_significance:
                    pt = TPaveText(.60,.1,.95,.2, "NDC")
                    pt.SetFillColor(0)
                    pt.SetTextAlign(11)
                    pt.SetBorderSize(0)
                    memory.append(pt)
                    pt.AddText("sigNum=" + str(sigNum))
                    pt.AddText("bgNum=" + str(bgNum))
                    pt.AddText("sig=" + str(significance))
                    pt.Draw()
            
            if plot_par.plot_efficiency and bg_retag:
                pt = TPaveText(.50,.55,.85,.65, "NDC")
                pt.SetFillColor(0)
                pt.SetTextAlign(11)
                pt.SetBorderSize(0)
                memory.append(pt)
                for effName, eff in efficiencies.items():
                    pt.AddText(effName + "=" + str(eff))
                    #pt.AddText(effName + "=" + str(eff))
                pt.Draw()
                
            
            if plot_par.plot_data:
                if plot_par.plot_bg:
                    print "dataHist.Draw(P e SAME)"
                    dataHist.Draw("P e SAME")
                else:
                    print "dataHist.Draw(P e)"
                    dataHist.Draw("P e")
                legend.AddEntry(dataHist, "Data", 'p')
            
            scDataHist = None
            scBgHist = None
            if plot_par.plot_sc:
                if plot_par.plot_data:
                    scDataHistName = "sc_" + cut["name"] + "_" + hist_def["obs"] + "_data"
                    scDataHist = histograms[scDataHistName]
                    if plot_par.normalise:
                        scDataHist.Scale(1./scDataHist.Integral())
                    if not (linear and plot_single):
                        scDataHist.SetMinimum(0.0001)
                    else:
                        scDataHist.SetMinimum(0)
                    scDataHist.SetMarkerStyle(kFullCircle)
                    if large_version:
                        scDataHist.SetMarkerSize(1)
                    else:
                        scDataHist.SetMarkerSize(0.5)
                    scDataHist.SetMarkerColor(kRed)
                    scDataHist.Draw("P SAME")
                    legend.AddEntry(scDataHist, "Same-Sign Data", 'p')
                
                scBgHistName = "sc_" + cut["name"] + "_" + hist_def["obs"] + "_bg"
                scBgHist = histograms[scBgHistName]
                if plot_par.normalise:
                    scBgHist.Scale(1./scBgHist.Integral())
                if not (linear and plot_single):
                    scBgHist.SetMinimum(0.0001)
                else:
                    scBgHist.SetMinimum(0)
                scBgHist.SetLineWidth(2)
                scBgHist.SetLineColor(6)
                scBgHist.Draw("HIST SAME" + errorStr)
                
                legend.AddEntry(scBgHist, "sc bg", 'l')
            
            if plot_par.fit_inv_mass_jpsi and plot_par.fit_inv_mass_cut_jpsi == cut["name"] and plot_par.fit_inv_mass_obs_jpsi in hist_def["obs"]:
                print "FITTING INVARIANT MASS PLOT!", hist_def["obs"]
                fitHist = None
                jpsiHist = None
                
                if plot_par.fit_inv_mass_jpsi_func_bg:
                    if plot_par.solid_bg:
                        fitHist = newBgHist
                    else:
                        jpsiHist = ((newBgHist.GetHists())[0]).Clone("invMassJpsi"+ hist_def["obs"])
                        fitHist = newBgHist.GetStack().Last().Clone("invMassFitHist"+ hist_def["obs"])
                        memory.append(fitHist)
                        memory.append(jpsiHist)
                else:
                    fitHist = dataHist
                
                print "Sum", fitHist.Integral()
                xax = fitHist.GetXaxis()
                lowedge, highedge = xax.GetBinLowEdge(1), xax.GetBinUpEdge(xax.GetNbins())
                print "lowedge, highedge", lowedge, highedge
                
                fFullModel = None
                gauss = plot_par.fit_inv_mass_jpsi_func == "gauss"
                linear_fit = plot_par.fit_inv_mass_jpsi_bg_func == "linear"
                
                
                if plot_par.fit_inv_mass_jpsi_func == "gauss":
                    if linear_fit:
                        fFullModel = TF1('fFullModel' + hist_def["obs"], funcFullModel, lowedge, highedge, 5)
                    else:
                        fFullModel = TF1('fFullModel' + hist_def["obs"], funcFullModelQuadratic, lowedge, highedge, 6)
                    fFullModel.SetNpx(500);
                    
                    jpsiBin = fitHist.FindBin(3.096916)
                    maxJpsiPeak = fitHist.GetBinContent(jpsiBin)
                    print "jpsiBin", jpsiBin, "maxJpsiPeak", maxJpsiPeak
                    for i in range(jpsiBin-2, jpsiBin+2):
                        if i < 1 or  i > fitHist.GetNbinsX():
                            continue
                        print "Getting jpsi bin at", i, fitHist.GetBinContent(i)
                        maxJpsiPeak = max(maxJpsiPeak, fitHist.GetBinContent(i))
                    print "maxJpsiPeak", maxJpsiPeak
                    #fFullModel.FixParameter(0,maxJpsiPeak)
                    fFullModel.SetParameter(1,3.096916)
                    fFullModel.SetParLimits(1,3.08,3.12)
                    fFullModel.SetParameter(2,0.1)
                    fFullModel.SetParLimits(2,0.05,0.2)
                elif plot_par.fit_inv_mass_jpsi_func == "lorentzian":
                    if linear_fit:
                        fFullModel = TF1('fFullModel' + hist_def["obs"], funcFullModelLorentzian, lowedge, highedge, 5)
                    else:
                        fFullModel = TF1('fFullModel' + hist_def["obs"], funcFullModelLorentzianQuadratic, lowedge, highedge, 6)
                    fFullModel.SetNpx(500);
                    fFullModel.SetParameter(2, 3.096916)
                    fFullModel.SetParLimits(2,3.05, 3.15)
                    fFullModel.SetParameter(1, 0.1)
                elif plot_par.fit_inv_mass_jpsi_func == "doubleGaussian":
                    if linear_fit:
                        fFullModel = TF1('fFullModel' + hist_def["obs"], funcFullModelDoubleGaussian, lowedge, highedge, 7)
                    else:
                        fFullModel = TF1('fFullModel' + hist_def["obs"], funcFullModelDoubleGaussianQuadratic, lowedge, highedge, 10)
                    fFullModel.SetNpx(500);
                    fFullModel.SetParameter(0,10)
                    fFullModel.SetParLimits(0,0.01,10000)
                    fFullModel.SetParameter(3,0.01)
                    fFullModel.SetParLimits(3,0.01,10000)
                    fFullModel.SetParameter(1,3.096916)
                    fFullModel.SetParLimits(1,3.08,3.11)
                    fFullModel.SetParameter(2,0.05)
                    fFullModel.SetParameter(4,0.05)
                    fFullModel.SetParLimits(2,0.005,0.1)
                    fFullModel.SetParLimits(4,0.005,0.1)
                    
                    
                fit_funcs["fFullModel" + hist_def["obs"]] = fFullModel
                # s option creates the result
                fFullModel.SetLineWidth(2)
                fFullModel.SetLineColor(kRed)
                fitresult = fitHist.Fit(fFullModel,'s0','same', lowedge, highedge)
                fFullModel.Draw("SAME")
                legend.AddEntry(fFullModel, "Global fit", 'l')
                
                fSignal = None
                
                if plot_par.fit_inv_mass_jpsi_func == "gauss":
                    fSignal = TF1('fSignal' + hist_def["obs"], funcGaussian, lowedge, highedge, 3)
                elif plot_par.fit_inv_mass_jpsi_func == "lorentzian":
                    fSignal = TF1('fSignal' + hist_def["obs"], funcLorentzian, lowedge, highedge, 3)
                elif plot_par.fit_inv_mass_jpsi_func == "doubleGaussian":
                    fSignal = TF1('fSignal' + hist_def["obs"], funcDoubleGaussian, lowedge, highedge, 5)
                fSignal.SetNpx(500);
                fit_funcs["fSignal" + hist_def["obs"]] = fSignal
                fSignal.SetParameter(0, fFullModel.GetParameter(0))
                fSignal.SetParameter(1, fFullModel.GetParameter(1))
                fSignal.SetParameter(2, fFullModel.GetParameter(2))
                if plot_par.fit_inv_mass_jpsi_func == "doubleGaussian":
                    fSignal.SetParameter(3, fFullModel.GetParameter(3))
                    fSignal.SetParameter(4, fFullModel.GetParameter(4))
                
                fSignal.SetLineWidth(2)
                fSignal.SetLineColor(kBlue)
                fSignal.Draw("SAME")
                legend.AddEntry(fSignal, "J/#psi", 'l')
                
                if linear_fit:
                    fBg = TF1('fBg' + hist_def["obs"], funcBackground, lowedge, highedge, 2)
                else:
                    fBg = TF1('fBg' + hist_def["obs"], funcBackgroundQuadratic, lowedge, highedge, 5)
                fit_funcs["fBg" + hist_def["obs"]] = fBg
                bgIndex = 3
                if plot_par.fit_inv_mass_jpsi_func == "doubleGaussian":
                    bgIndex = 5
                fBg.SetParameter(0, fFullModel.GetParameter(bgIndex))
                fBg.SetParameter(1, fFullModel.GetParameter(bgIndex+1))
                if not linear:
                    fBg.SetParameter(2, fFullModel.GetParameter(bgIndex+2))
                    fBg.SetParameter(3, fFullModel.GetParameter(bgIndex+3))
                    fBg.SetParameter(4, fFullModel.GetParameter(bgIndex+4))
                fBg.SetLineWidth(2)
                fBg.SetLineColor(kBlack)
                fBg.Draw("SAME")
                legend.AddEntry(fBg, "Continuum", 'l')
                
                print "printing values for", hist_def["obs"]
                print "Bin Width:", jpsiHist.GetBinWidth(jpsiHist.FindBin(3.0))
                print "Full Hist Integral:", fitHist.Integral(fitHist.FindBin(3.0), fitHist.FindBin(3.2))
                print "Full JPsi Integral:", jpsiHist.Integral(jpsiHist.FindBin(3.0), jpsiHist.FindBin(3.2))
                print "Full JPsi Integral Width:", jpsiHist.Integral(jpsiHist.FindBin(3.0), jpsiHist.FindBin(3.2), "width")
                print "Full Fit Integral:", fFullModel.Integral(3.0, 3.2)
                print "Full Fit Integral Width:", fFullModel.Integral(3.0, 3.2) / jpsiHist.GetBinWidth(jpsiHist.FindBin(3.0))
                print "BG Integral:", fBg.Integral(3.0, 3.2)
                print "Signal Integral:", fSignal.Integral(3.0, 3.2)
                print "Signal Integral Width:", fSignal.Integral(3.0, 3.2) / jpsiHist.GetBinWidth(jpsiHist.FindBin(3.0))
                
                fit_hist_integral[hist_def["obs"]] = fitHist.Integral(fitHist.FindBin(3.0), fitHist.FindBin(3.2))
                fit_full_integral[hist_def["obs"]] = fFullModel.Integral(3.0, 3.2) / jpsiHist.GetBinWidth(jpsiHist.FindBin(3.0))
                fit_signal_integral[hist_def["obs"]] = fSignal.Integral(3.0, 3.2) / jpsiHist.GetBinWidth(jpsiHist.FindBin(3.0))
                fit_bg_integral[hist_def["obs"]] = fBg.Integral(3.0, 3.2) / jpsiHist.GetBinWidth(jpsiHist.FindBin(3.0))
                hist_signal_integral[hist_def["obs"]] = jpsiHist.Integral(jpsiHist.FindBin(3.0), jpsiHist.FindBin(3.2))
                
            
            legend.Draw("SAME")
            if not (linear and plot_single):
                pad.SetLogy()
                
            pad.SetGridx()
            pad.SetGridy()
            
            if plot_par.plot_log_x and hist_def["obs"] == "invMass":
                pad.SetLogx()
                if plot_par.plot_ratio or plot_par.plot_custom_ratio > 0:
                    histRPad.SetLogx()
                    if (plot_par.plot_sc and plot_par.plot_data) or plot_par.plot_custom_ratio > 1:
                        histR2Pad.SetLogx()
            else:
                pad.SetLogx(0)
                if plot_par.plot_ratio or plot_par.plot_custom_ratio > 0:
                    histRPad.SetLogx(0)
                    if (plot_par.plot_sc and plot_par.plot_data) or plot_par.plot_custom_ratio > 1:
                        histR2Pad.SetLogx(0)
            
            c1.Update()
            
            #print "**", ratioPads
            
            if plot_par.plot_ratio or plot_par.plot_custom_ratio > 0:
                
                if plot_par.plot_sc:
                    #print "Going to plot for ", histRPad, dataHist, scDataHist, hist_def
                    
                    #print "***********", pId, ratioPads
                    stackSum = None
                    if plot_par.solid_bg:
                        stackSum = newBgHist
                    else:
                        stackSum = newBgHist.GetStack().Last().Clone("stackSum")
                        memory.append(stackSum)
                    #stackSum = utils.getStackSum(newBgHist)
                    memory.append(stackSum)
                    plotRatio(c1, histRPad, memory, stackSum, scBgHist, hist_def, "Bg / Bg")
                    if plot_par.plot_data:
                        plotRatio(c1, histR2Pad, memory, dataHist, scDataHist, hist_def, "Data / Data", False)
                    #print "-------", pId, ratioPads
                else:
                    if plot_par.plot_custom_ratio > 0:
                        bgHists = hs.GetHists()
                        for ratioNum in range(plot_par.plot_custom_ratio):
                            cutomRatio = plot_par.customRatios[ratioNum]
                            numDenHists = [None, None]
                            titles = [None, None]
                            for numDenHistInx in range(2):
                                for histName in cutomRatio[numDenHistInx]:
                                    if histName == "data":
                                        if numDenHists[numDenHistInx] is None:
                                            numDenHists[numDenHistInx] = dataHist.Clone()
                                            memory.append(numDenHists[numDenHistInx])
                                            titles[numDenHistInx] = "data"
                                        else:
                                            numDenHists[numDenHistInx].Add(dataHist)
                                            titles[numDenHistInx] = " + data"
                                    else:
                                        for i, hist in enumerate(bgHists):
                                            if histName == hist.GetName().split("_")[-1]:
                                                if numDenHists[numDenHistInx] is None:
                                                    numDenHists[numDenHistInx] = hist.Clone()
                                                    memory.append(numDenHists[numDenHistInx])
                                                    titles[numDenHistInx] = histName
                                                else:
                                                    numDenHists[numDenHistInx].Add(hist)
                                                    titles[numDenHistInx] = " + " + histName
                            if ratioNum == 0:
                                plotRatio(c1, histRPad, memory, numDenHists[0], numDenHists[1], hist_def, titles[0] + " / " + titles[1])
                            else:
                                plotRatio(c1, histR2Pad, memory, numDenHists[0], numDenHists[1], hist_def, titles[0] + " / " + titles[1], False)
                    else:
                        stackSum = None
                        if plot_par.solid_bg:
                            stackSum = newBgHist
                        else:
                            stackSum = newBgHist.GetStack().Last().Clone("stackSum")
                            memory.append(stackSum)
                        #stackSum = utils.getStackSum(newBgHist)
                        memory.append(stackSum)
                        plotRatio(c1, histRPad, memory, dataHist, stackSum, hist_def, "Data / BG", True, large_version)
            
            #print "***", ratioPads
            print calculated_lumi
            lumiStr = "{:.1f}".format(calculated_lumi)
            
            if large_version:
                if plot_par.plot_ratio:
                    #c1.cd()
                    histCPad.cd()
                utils.stamp_plot(lumiStr)
                if create_png:
                    filename = (cut["name"] + "_" + hist_def["obs"])
                    print "Saving file " + "./" + png_name + "/" + filename + "_log.pdf"
                    c1.SaveAs("./" + png_name + "/" + filename + "_log.pdf")
                else:
                    print "BREAKING IN LOG SCALE"
                    break
            else:
                pad.cd()
                utils.stamp_plot(lumiStr)
            
            if create_png:
                c1.Clear()
            
            pId += 1
            
            ###### LINEAR SCALE NOW #######
            
            print "GLOBAL LINER SCALE!!"

            if pId > 4 and not large_version:
                pId = 1
                c1.Print(output_file);
                if plot_par.create_canvas:
                    c1.Write(cutName)
                needToDraw = False;
            if plot_par.plot_bg:
                linBgHist = newBgHist.Clone()
                memory.append(linBgHist)
                linBgHist.SetMaximum(maximum*1.1)
                linBgHist.SetMinimum(0)
            else:
                dataHist.SetMaximum(maximum*1.1)
                dataHist.SetMinimum(0)
            
            #print "****", ratioPads
            if large_version:
                pad = c1
            else:
                pad = histPad.cd(pId)
            
            histCPad = None
            histRPad = None
            histR2Pad = None
            if plot_par.plot_ratio or plot_par.plot_custom_ratio > 0:
                if large_version or ratioPads.get(pId) is None:
                    if (plot_par.plot_sc and plot_par.plot_data) or plot_par.plot_custom_ratio > 1:
                        histCPad, histRPad, histR2Pad = createCRPads(pId, ratioPads, True)
                        #print "After:", histCPad, histRPad, histR2Pad
                    else:
                        histCPad, histRPad = createCRPads(pId, ratioPads)
                else:
                    histCPad = ratioPads[pId][0]
                    histRPad = ratioPads[pId][1]
                    if (plot_par.plot_sc and plot_par.plot_data) or plot_par.plot_custom_ratio > 1:
                        histR2Pad = ratioPads[pId][2]
                    #print "Was trying to get Id", pId, ratioPads
                    #print "After in here", histCPad, histRPad, histR2Pad
                print "Assigning ", histCPad
                pad = histCPad
                pad.cd()
            else:
                if large_version:
                    pad = c1
                else:
                    pad = histPad.cd(pId)
            
            pad.SetLogy(0)
            pad.SetGridx()
            pad.SetGridy()
            if not plot_par.plot_ratio:
                pad.SetBottomMargin(0.16)
                pad.SetLeftMargin(0.18)
            
            if plot_par.plot_log_x and hist_def["obs"] == "invMass":
                pad.SetLogx()
                if plot_par.plot_ratio or plot_par.plot_custom_ratio > 0:
                    histRPad.SetLogx()
                    if (plot_par.plot_sc and plot_par.plot_data) or plot_par.plot_custom_ratio > 1:
                        histR2Pad.SetLogx()
            else:
                pad.SetLogx(0)
                
                if plot_par.plot_ratio or plot_par.plot_custom_ratio > 0:
                    histRPad.SetLogx(0)
                    if (plot_par.plot_sc and plot_par.plot_data) or plot_par.plot_custom_ratio > 1:
                        histR2Pad.SetLogx(0)
            if plot_par.plot_bg:
                linBgHist.Draw(plotStr + errorStr)
            if plot_par.plot_signal:
                for i in range(len(sigHists)):
                    sigHists[i].Draw("HIST SAME" + errorStr)
            if plot_par.plot_data:
                print "LINEAR"
                if not plot_par.plot_bg:
                    print "dataHist.Draw(P e)"
                    dataHist.Draw("P e")
                else:
                    print "dataHist.Draw(P e SAME)"
                    dataHist.Draw("P e SAME")
            if plot_par.plot_sc:
                if plot_par.plot_data:
                    scDataHist.Draw("P e SAME")
                linScBgHist = scBgHist.Clone()
                memory.append(linScBgHist)
                linScBgHist.SetMaximum(maximum*1.1)
                linScBgHist.SetMinimum(0)
                linScBgHist.Draw("HIST SAME" + errorStr)
            
            if plot_par.fit_inv_mass_jpsi and plot_par.fit_inv_mass_cut_jpsi == cut["name"] and plot_par.fit_inv_mass_obs_jpsi in hist_def["obs"]:
                fit_funcs["fFullModel" + hist_def["obs"]].Draw("SAME")
                fit_funcs["fSignal" + hist_def["obs"]].Draw("SAME")
                fit_funcs["fBg" + hist_def["obs"]].Draw("SAME")
                
            legend.Draw("SAME")
            
            if plot_par.plot_ratio or plot_par.plot_custom_ratio > 0:
                if plot_par.plot_sc:
                    stackSum = None
                    if plot_par.solid_bg:
                        stackSum = newBgHist
                    else:
                        stackSum = newBgHist.GetStack().Last().Clone("stackSum")
                        memory.append(stackSum)
                    #stackSum = utils.getStackSum(newBgHist)
                    memory.append(stackSum)
                    plotRatio(c1, histRPad, memory, stackSum, scBgHist, hist_def, "Bg / Bg")
                    if plot_par.plot_data:
                        plotRatio(c1, histR2Pad, memory, dataHist, scDataHist, hist_def, "Data / Data", False)
                else:
                    if plot_par.plot_custom_ratio > 0:
                        bgHists = hs.GetHists()
                        
                        for ratioNum in range(plot_par.plot_custom_ratio):
                            cutomRatio = plot_par.customRatios[ratioNum]
                            numDenHists = [None, None]
                            titles = [None, None]
                            for numDenHistInx in range(2):
                                for histName in cutomRatio[numDenHistInx]:
                                    if histName == "data":
                                        if numDenHists[numDenHistInx] is None:
                                            numDenHists[numDenHistInx] = dataHist.Clone()
                                            memory.append(numDenHists[numDenHistInx])
                                            titles[numDenHistInx] = "data"
                                        else:
                                            numDenHists[numDenHistInx].Add(dataHist)
                                            titles[numDenHistInx] = " + data"
                                    else:
                                        for i, hist in enumerate(bgHists):
                                            if histName == hist.GetName().split("_")[-1]:
                                                if numDenHists[numDenHistInx] is None:
                                                    numDenHists[numDenHistInx] = hist.Clone()
                                                    memory.append(numDenHists[numDenHistInx])
                                                    titles[numDenHistInx] = histName
                                                else:
                                                    numDenHists[numDenHistInx].Add(hist)
                                                    titles[numDenHistInx] = " + " + histName
                            if ratioNum == 0:
                                plotRatio(c1, histRPad, memory, numDenHists[0], numDenHists[1], hist_def, titles[0] + " / " + titles[1])
                            else:
                                plotRatio(c1, histR2Pad, memory, numDenHists[0], numDenHists[1], hist_def, titles[0] + " / " + titles[1], False)
                    else:
                        stackSum = None
                        if plot_par.solid_bg:
                            stackSum = newBgHist
                        else:
                            stackSum = newBgHist.GetStack().Last().Clone("stackSum")
                            memory.append(stackSum)
                        #stackSum = utils.getStackSum(newBgHist)
                        memory.append(stackSum)
                        plotRatio(c1, histRPad, memory, dataHist, stackSum, hist_def, "Data / BG", True, large_version)
            
            print calculated_lumi
            lumiStr = "{:.1f}".format(calculated_lumi)
            if large_version:
                if plot_par.plot_ratio:
                    #c1.cd()
                    histCPad.cd()
                utils.stamp_plot(lumiStr)
                if create_png:
                    filename = (cut["name"] + "_" + hist_def["obs"])
                    print "Saving file " + "./" + png_name + "/" + filename + ".pdf"
                    c1.SaveAs("./" + png_name + "/" + filename + ".pdf")
                    c1.Clear()
                    pId = 1
                    continue
                else:
                    break
            else:
                pad.cd()
                utils.stamp_plot(lumiStr)
            
            pId += 1

            if pId > 4:
                pId = 1
                if not large_version:
                    c1.Print(output_file);
                    if plot_par.create_canvas:
                        c1.Write(cutName)
                needToDraw = False;
            
        if needToDraw and not plot_single and not large_version:
            for id in range(pId, 5):
                print "Clearing pad " + str(id)
                pad = histPad.cd(id)
                if plot_par.plot_ratio and ratioPads.get(pId) is not None:
                    ratioPads[pId][0].Clear()
                    ratioPads[pId][1].Clear()
                    if (plot_par.plot_sc and plot_par.plot_data) or plot_par.plot_custom_ratio > 1:
                        ratioPads[pId][2].Clear()
                else:
                    pad.Clear()
        if needToDraw and not create_png:
            print "Printing canvas to", output_file
            c1.Print(output_file);
            if plot_par.create_canvas:
                print "Writing canvas", cutName
                c1.Write(cutName)
    if plot_single or not create_png:
        c1.Print(output_file+"]");
    if plot_par.create_canvas and not large_version:
        print "Just created", canvasFile.GetName()
        canvasFile.Close()
        
    print "fit_hist_integral", fit_hist_integral
    print "fit_full_integral", fit_full_integral
    print "fit_signal_integral", fit_signal_integral
    print "fit_bg_integral", fit_bg_integral
    
    print "============== FIT SUMMARY =============="
    
    print ",fit_hist_integral,hist_signal_integral,fit_full_integral,fit_signal_integral,fit_bg_integral,fit_hist_integral_reco,hist_signal_integral_reco,fit_full_integral_reco,fit_signal_integral_reco,fit_bg_integral_reco,fit_hist_integral_id,hist_signal_integral_id,fit_full_integral_id,fit_signal_integral_id,fit_bg_integral_id,reco_eff,reco_eff_hist,id_eff,id_eff_hist"
    
    for hist_def in plot_par.histograms_defs:
        if "reco_" in hist_def["obs"] or "id_" in hist_def["obs"]:
            continue
        print hist_def["obs"] + "," + str(fit_hist_integral[hist_def["obs"]]) + "," + str(hist_signal_integral[hist_def["obs"]]) + "," +  str(fit_full_integral[hist_def["obs"]]) + "," + str(fit_signal_integral[hist_def["obs"]]) + "," + str(fit_bg_integral[hist_def["obs"]])  + "," + str(fit_hist_integral["reco_" + hist_def["obs"]]) + "," + str(fit_full_integral["reco_" + hist_def["obs"]])  + "," + str(hist_signal_integral["reco_" + hist_def["obs"]])+ "," + str(fit_signal_integral["reco_" + hist_def["obs"]]) + "," + str(fit_bg_integral["reco_" + hist_def["obs"]])    + "," + str(fit_hist_integral["id_" + hist_def["obs"]])+ "," + str(hist_signal_integral["id_" + hist_def["obs"]]) + "," + str(fit_full_integral["id_" + hist_def["obs"]]) + "," + str(fit_signal_integral["id_" + hist_def["obs"]]) + "," + str(fit_bg_integral["id_" + hist_def["obs"]]) + "," + str(fit_signal_integral["reco_" + hist_def["obs"]]/fit_signal_integral[hist_def["obs"]])  + "," + str(hist_signal_integral["reco_" + hist_def["obs"]]/hist_signal_integral[hist_def["obs"]]) + "," + str(fit_signal_integral["id_" + hist_def["obs"]]/fit_signal_integral[hist_def["obs"]])  + "," + str(hist_signal_integral["id_" + hist_def["obs"]]/hist_signal_integral[hist_def["obs"]]) 
    
    print "End: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    exit(0)

main()
exit(0)



