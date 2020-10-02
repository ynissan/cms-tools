from ROOT import *
import sys
import numpy as np

from lib import histograms
from lib import cuts
import os, re
import json
import time
import array
import commands
import math
from glob import glob
import random
import string

gSystem.Load('LumiSectMap_C')
from ROOT import LumiSectMap

gStyle.SetOptStat(0)
TH1D.SetDefaultSumw2()

# gSystem.Load('LeptonCollectionMap_C')
# from ROOT import LeptonCollectionMap
# from ROOT import LeptonCollectionFilesMap
# from ROOT import LeptonCollection

colorPalette = [
    { "name" : "yellow", "fillColor" : "#fcf802", "lineColor" : "#e0dc00", "fillStyle" : 3444 },
    { "name" : "green", "fillColor" : "#0bb200", "lineColor" : "#099300", "fillStyle" : 3444 },
    { "name" : "blue", "fillColor" : "#0033cc", "lineColor" : "#00279e", "fillStyle" : 3444 },
    { "name" : "purple", "fillColor" : "#f442f1", "lineColor" : "#a82ba6", "fillStyle" : 3444 },
    { "name" : "tourq", "fillColor" : "#00ffe9", "lineColor" : "#2a8c83", "fillStyle" : 3444 },
    { "name" : "orange", "fillColor" : "#ffbb00", "lineColor" : "#b78b12", "fillStyle" : 3444 },
    { "name" : "lightgreen", "fillColor" : "#42f498", "lineColor" : "#28a363", "fillStyle" : 3444 },
    { "name" : "red", "fillColor" : "#e60000", "lineColor" : "#c60000", "fillStyle" : 3444 },
    { "name" : "velvet", "fillColor" : "#ff00c9", "lineColor" : "#ff8ee7", "fillStyle" : 3444 },
    { "name" : "darkblue", "fillColor" : "#1B00DC", "lineColor" : "#8373FA", "fillStyle" : 3444 },
    
    { "name" : "maroon", "fillColor" : "#800000", "lineColor" : "#A52A2A", "fillStyle" : 3444 },
    { "name" : "darkslategray", "fillColor" : "#2F4F4F", "lineColor" : "#708090", "fillStyle" : 3444 },
    { "name" : "wheat", "fillColor" : "#F5DEB3", "lineColor" : "#FFDEAD", "fillStyle" : 3444 },
    { "name" : "lightgray", "fillColor" : "#D3D3D3", "lineColor" : "#DCDCDC", "fillStyle" : 3444 },
    
    { "name" : "black", "fillColor" : kBlack, "lineColor" : kBlack, "fillStyle" : 3444 },
]

crossSections = {
    "dm7"  : 1.21547,
    "dm13" : 1.21547,
    "dm20" : 1.21547
}

samCrossSections = {
    'mChipm100GeV' : 16.7972,
    'mChipm115GeV' : 10.6756,
    'mChipm140GeV' : 5.00942,
    'mChipm160GeV' : 2.99724,
    'mChipm180GeV' : 1.90530,
    'mChipm200GeV' : 1.33562,
    'mChipm225GeV' : 0.807605,
    'mChipm250GeV' : 0.577314,
    'mChipm275GeV' : 0.373229,
    'mChipm300GeV' : 0.284855,
    'mChipm400GeV' : 0.0887325,
    'mChipm500GeV' : 0.0338387
}

dyCrossSections = {
    "DYJetsToLL_M-5to50_HT-70to100" : 301.2,
    "DYJetsToLL_M-5to50_HT-100to200" : 224.2,
    "DYJetsToLL_M-5to50_HT-200to400" : 37.2,
    "DYJetsToLL_M-5to50_HT-400to600" : 3.581,
    "DYJetsToLL_M-5to50_HT-600toInf": 1.124
}

# dyCrossSections = {
#     "DYJetsToLL_M-5to50_HT-70to100" : 301.0,
#     "DYJetsToLL_M-5to50_HT-100to200" : 224.4,
#     "DYJetsToLL_M-5to50_HT-200to400" : 37.87,
#     "DYJetsToLL_M-5to50_HT-400to600" : 3.628,
#     "DYJetsToLL_M-5to50_HT-600toInf": 1.107
# }

#LUMINOSITY = 35900. #pb^-1
LUMINOSITY = 135000.
CMS_WD="/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src"
CS_DIR="/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/cs/stdout"
LEPTON_COLLECTION_DIR="/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/LeptonCollection"
LEPTON_COLLECTION_FILES_MAP_DIR="/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/LeptonCollectionFilesMaps"

epsilon = 0.00001

#For solid fill use fillStyle=1001
signalCp = [
    { "name" : "blue", "fillColor" : "#000f96", "lineColor" : "#1d0089", "fillStyle" : 0 },
    { "name" : "grey", "fillColor" : "#898989", "lineColor" : "#636363", "fillStyle" : 0 },
    { "name" : "black", "fillColor" : "#012a6d", "lineColor" : "#01173a", "fillStyle" : 0 },
    { "name" : "red", "fillColor" : "#ff0000", "lineColor" : "#ff0000", "fillStyle" : 0 },
]

compoundTypes = {
    "Rare" : ["WZZ", "WWZ", "ZZZ"],
    "DiBoson" : ["WZ", "WW", "ZZ"],
    "TTJets": ["ST_t-channel_antitop", "ST_t-channel_top", "TTJets_DiLept", "TTJets_SingleLeptFromT", "TTJets_SingleLeptFromTbar"]
}

trainGroups = {
    "dm1" : ["dm0p", "dm1p"],
    "low" : ["dm2p", "dm3p", "dm4p"],
    "dm7" : ["dm7p"],
    "dm9" : ["dm9p"],
    "high" : ["dm12p", "dm13p"]
}

trainGroupsOrder = ["dm1", "low", "dm7", "dm9", "high"]

#Normal
bgOrder = {
    "Rare" : 0,
    "DiBoson" : 1,
    "DYJetsToLL" : 2,
    "TTJets" : 3,
    "ZJetsToNuNu" : 4,
    "QCD" : 5,
    "WJetsToLNu" : 6,
    #"TT" : 7,
}

#Z Jets
# bgOrder = {
#     "Rare" : 0,
#     "DiBoson" : 5,
#     "ZJetsToNuNu" : 1,
#     "DYJetsToLL" : 6,
#     "TTJets" : 4,
#     "WJetsToLNu" : 3,
#     "QCD" : 2,
# }

tracksVars = (
        {"name":"dxyVtx", "type":"double"},
        {"name":"dzVtx", "type":"double"},
        {"name":"chi2perNdof", "type":"double"},
        {"name":"trkMiniRelIso", "type":"double"},
        {"name":"trkRelIso", "type":"double"},
        {"name":"charge", "type":"int"},
        {"name":"trackJetIso", "type":"double"},
        {"name":"trackQualityHighPurity", "type":"bool"},
        #{"name":"trackLeptonIso", "type":"double"}
)


leptonsCorrJetVecList = {
    "CorrJetIso" : "bool",
    "NonJetIso" : "bool",
    "JetIso" : "bool"
}

leptonCorrJetIsoPtRange = [0, 1, 5, 10, 15]

dileptonObservablesVecList = {
    "leptons" : "TLorentzVector",
    "leptonsIdx" : "int",
    "leptons_charge" : "int"
}

dileptonObservablesStringList = ["leptonFlavour"]

commonObservablesDTypesList = {
    "invMass" : "float",
    "dileptonPt" : "float",
    "deltaPhi" : "float",
    "deltaEta" : "float",
    "deltaR" : "float",
    "pt3" : "float",
    "mtautau" : "float",
    "mt1" : "float",
    "mt2" : "float",
    "deltaEtaLeadingJetDilepton" : "float",
    "deltaPhiLeadingJetDilepton" : "float",
    "dilepHt" : "float",
}

dileptonObservablesDTypesList = {
    "twoLeptons" : "bool",
    "deltaPhiMetLepton1" : "float",
    "deltaPhiMetLepton2" : "float",
}

dileptonObservablesDTypesList.update(commonObservablesDTypesList)

exclusiveTrackObservablesStringList = ["exclusiveTrackLeptonFlavour"]
exclusiveTrackObservablesDTypesList = {
    "exclusiveTrack" : "bool",
    "ti" : "int",
    "sti" : "int",
    "lepton_charge" : "int",
    "leptonIdx" : "int",
    "mtt" : "float",
    "mtl" : "float",
    "NTracks" : "int",
    "deltaRMetTrack" : "float",
    "deltaRMetLepton" : "float",
    "deltaPhiMetTrack" : "float",
    "deltaPhiMetLepton" : "float",
    "trackBDT" : "float",
    "secondTrackBDT" : "float"
}

exclusiveTrackObservablesClassList = {
    "track" : "TLorentzVector",
    "lepton" : "TLorentzVector",
    "secondTrack" : "TLorentzVector",
    "l1" : "TLorentzVector",
    "l2" : "TLorentzVector",
}

leptonIsolationList = [ "JetIso", "CorrJetIso", "NonJetIso" ]
leptonIsolationCategories = {
    "" : { "lowPtTightMuons" : False, "muonPt" : 2},
    "LowPt" : { "lowPtTightMuons" : False, "muonPt" : 1.5},
    "LowPtTight" : { "lowPtTightMuons" : True, "muonPt" : 1.5}
}

typeTranslation = {
    "float" : "D",
    "bool" : "O",
    "int" : "I"
}

tl = TLatex()
tl.SetNDC()
cmsTextFont = 61
extraTextFont = 52
lumiTextSize = 0.6
lumiTextOffset = 0.2
cmsTextSize = 0.75
cmsTextOffset = 0.1
regularfont = 42
originalfont = tl.GetTextFont()

class UOFlowTH1F(TH1F):
    epsilon = 0.0000000001
    def Fill(self, x, weight=1):
        #print "Called UOFlowTH1F Fill"
        super(UOFlowTH1F, self).Fill(min(max(x,self.GetXaxis().GetBinLowEdge(1)+self.epsilon),self.GetXaxis().GetBinLowEdge(self.GetXaxis().GetNbins()+1)-self.epsilon),weight)

class UOFlowTH2F(TH1F):
    epsilon = 0.0000000001
    def Fill(self, x, y, weight=1):
        #print "Called UOFlowTH1F Fill"
        super(UOFlowTH2F, self).Fill(min(max(x,h.GetXaxis().GetBinLowEdge(1)+epsilon),h.GetXaxis().GetBinLowEdge(h.GetXaxis().GetNbins()+1)-epsilon), min(max(y,h.GetYaxis().GetBinLowEdge(1)+epsilon),h.GetYaxis().GetBinLowEdge(h.GetYaxis().GetNbins()+1)-epsilon),weight)

def isCoumpoundType(key):
    #print "Looking for:" + key + "|:
    if key in compoundTypes:
        return True
    return False

def existsInCoumpoundType(key):
    #print "Looking for:" + key + "|:
    for cType in compoundTypes:
        if key in compoundTypes[cType]:
            return True
    return False

def getFilesForCompoundType(cType, directory):
    print "In getFilesForCompoundType"
    bgFiles = []
    #print compoundTypes[cType]
    for miniType in compoundTypes[cType]:
        #if miniType not in sumTypes:
        #    print "skipping", miniType, "because not in", sumTypes
        #    continue
        #print "globbing", miniType
        if "ST_" in miniType:
            #print "In ST***"
            #print "Globing " + directory + "/" + miniType + ".root"
            bgFiles.extend(glob(directory + "/" + miniType + ".root"))
        else:
            #print "Globing " + directory + "/" + miniType + "_*.root"
            bgFiles.extend(glob(directory + "/" + miniType + "_*.root"))

    return bgFiles


def createHistograms(definitions, cutsDef) :
    histograms = {}
    for name, definition in definitions.items():
        for cut, cutDef in cutsDef.items():
            histName = name
            if cut != "none":
                if name == "HT":
                    continue
                histName += "_" + cut
            defTitle = (cutDef["histDef"].get(name) and cutDef["histDef"].get(name).get("title")) or definition["title"]
            defBins = (cutDef["histDef"].get(name) and cutDef["histDef"].get(name).get("bins")) or definition["bins"]
            defMinX = (cutDef["histDef"].get(name) and cutDef["histDef"].get(name).get("minX")) or definition.get("minX")
            defMaxX = (cutDef["histDef"].get(name) and cutDef["histDef"].get(name).get("maxX")) or definition.get("maxX")
            defBinArr = (cutDef["histDef"].get(name) and cutDef["histDef"].get(name).get("binsArr")) or definition.get("binsArr")
            if defBinArr is not None:
                histograms[histName] = TH1F(histName, defTitle, defBins, array.array('d', defBinArr))
            else:
                histograms[histName] = TH1F(histName, defTitle, defBins, defMinX, defMaxX)
            histograms[histName].Sumw2()
    return histograms

def scaleHistograms(histograms, histDefs, weight):
    for name, hist in histograms.items():
        if histDefs.has_key(name) and histDefs[name].has_key("noScale") and histDefs[name]["noScale"] :
            print "Not scaling " + name + " ... Skipping."
            continue
        histograms[name].Scale(weight)

def writeHistograms(histList):
    for name, hist in histList.items():
        histList[name].Write()
    
def printNullHistograms(histList):
    for name, hist in histList.items():
        if histList[name].GetMaximum() == 0:
            print "Null Historgram " + name

def getSortedKeysFromRootFile(rootFile):
    hashKeys = rootFile.GetListOfKeys()
    keys = []
    for hashKey in hashKeys:
        keys.append(hashKey.GetName())
    keys.sort()
    return keys

def getSortedCutsFromRootFile(rootFile):
    hashKeys = rootFile.GetListOfKeys()
    cutsOrderMap = cuts.getCutsOrderMap(histograms.cutsOrder)
    cutsOrder = []
    for i, cut in enumerate(histograms.cutsOrder):
        cutsOrder.append({ "name" : cut, "hists" : []})
    print cutsOrder
    for hashKey in hashKeys:
        histName = hashKey.GetName()
        splitName = histName.split("_")
        cutName = "none"
        histName = splitName[0]
        if len(splitName) > 1:
            cutName = "_".join(splitName[1:])
        cutsOrder[cutsOrderMap[cutName]].get("hists").append(histName)
    
    
    for i, cut in enumerate(cutsOrder):
        cut.get("hists").sort()
    return cutsOrder

def formatHist(hist, cP, alpha=0.35,noFillStyle=False):
    fillC = TColor.GetColor(cP["fillColor"])
    lineC = TColor.GetColor(cP["lineColor"])
    if "fillStyle" in cP and not noFillStyle:
        hist.SetFillStyle(cP["fillStyle"])
    else:
        hist.SetFillStyle(1001)
    hist.SetFillColorAlpha(fillC, alpha)
    hist.SetLineColor(lineC)
    hist.SetLineWidth(1)
    hist.SetOption("HIST")
 
def pause(str_='push enter key when ready'):
    import sys
    print str_
    sys.stdout.flush() 
    raw_input('')


def fillth1(h,x, weight=1):
    h.Fill(min(max(x,h.GetXaxis().GetBinLowEdge(1)+epsilon),h.GetXaxis().GetBinLowEdge(h.GetXaxis().GetNbins()+1)-epsilon),weight)

def styledStackFromStack(bgHist, memory, legend=None, title="", colorInx=None, noFillStyle=False):
    newStack = THStack(bgHist.GetName(), title)
    memory.append(newStack)

    if bgHist is None or bgHist.GetNhists() == 0:
        return newStack
    #print "Num of hists: " + str(bgHist.GetNhists())
    bgHists = bgHist.GetHists()

    for i, hist in enumerate(bgHists):
        if hist.GetMaximum() == 0:
            print "Skipping " + hist.GetName()
            continue
        newHist = hist.Clone()
        memory.append(newHist)
        colorI = i
        if colorInx is not None:
            colorI = colorInx[i]
        formatHist(newHist, colorPalette[colorI], 0.35, noFillStyle)
        newStack.Add(newHist)
        if legend is not None:
            #print "Adding to legend " + hist.GetName().split("_")[-1]
            legend.AddEntry(newHist, hist.GetName().split("_")[-1], 'F')

    return newStack
 
def setLabels(sigHist, histDef):
    sigHist.SetTitle(histDef["title"])
    if "xAxis" in histDef:
        sigHist.GetXaxis().SetTitle(histDef["xAxis"])
    if "yAxis" in histDef:
        sigHist.GetXaxis().SetTitle(histDef["yAxis"])
 
def fillHistWithCuts(key, value, hists, cutsDef, type, event, weight=1, eventParams={}):
    #print "Filling key=" + key
    for cutName in cutsDef:
        if cutName == "none":
            hists[key].Fill(value, weight)
            #print "Fill " + key + " weight=" + str(weight)
            continue
        cut = cutsDef[cutName]
        if cuts.applyCut(cut, event, eventParams, type, cutName):
            #print "Fill " + key + "_" + cutName + " weight=" + str(weight)
            hists[key + "_" + cutName].Fill(value, weight)#new filling with over/under flow!
        #else:
        #	print "Not filling " + key + "_" + cutName

def getBgOrder(file):
    basename = os.path.basename(file).split(".")[0]
    if basename in bgOrder:
        return bgOrder[basename]
    else:
        return -1

def orderBgFiles(files):
    return sorted(files, key=getBgOrder)

def addMemToTreeVarsDef(treeVarsDef):
    for v in treeVarsDef:
        if v.get("type2") is not None:
            v["var"] = eval(v["type2"] + "()")
        else:
            if v["type"] == "D":
                v["var"] = np.zeros(1,dtype=np.dtype(np.float64))
            elif v["type"] == "I":
                v["var"] = np.zeros(1,dtype=int)

def barchTreeFromVarsDef(tree, treeVarsDef):
    for v in treeVarsDef:
        if v.get("type2") is not None:
            tree.Branch(v["name"], v["type2"], v["var"])
        else:
            tree.Branch(v["name"], v["var"], v["name"] + "/" + v["type"])

def get_histogram_from_tree(tree, var, cutstring="", drawoptions="", nBinsX=False, xmin=False, xmax=False, nBinsY=False, ymin=False, ymax=False, numevents=-1, add_overflow = False):

    hName = str(uuid.uuid1()).replace("-", "")

    canvas = TCanvas("c_" + hName)

    if not nBinsY:
        histo = TH1F(hName, hName, nBinsX, xmin, xmax)
    else:
        histo = TH2F(hName, hName, nBinsX, xmin, xmax, nBinsY, ymin, ymax)

    if numevents>0:
        tree.Draw("%s>>%s" % (var, hName), cutstring, drawoptions, numevents)
    else:
        tree.Draw("%s>>%s" % (var, hName), cutstring, drawoptions)

    # add overflow bin(s) for 1D and 2D histograms:
    if add_overflow:
        if not nBinsY:
            bin = histo.GetNbinsX()+1
            overflow = histo.GetBinContent(bin)
            histo.AddBinContent((bin-1), overflow)
        else:
            binX = histo.GetNbinsX()+1
            binY = histo.GetNbinsX()+1
        
            # read and set overflow x values:
            for x in range(0, binX-1):
                overflow_up = histo.GetBinContent(x, binY)
                bin = histo.GetBin(x, binY-1)
                histo.SetBinContent(bin, overflow_up)
        
            # read and set overflow y values:
            for y in range(0, binY-1):
                overflow_right = histo.GetBinContent(binX, y)
                bin = histo.GetBin(binX-1, y)
                histo.SetBinContent(bin, overflow_right)
        
            # read and set overflow diagonal values:
            overflow_diag = histo.GetBinContent(binX, binY)
            bin = histo.GetBin(binX-1, binY-1)
            histo.SetBinContent(bin, overflow_diag)
   
    histo.SetDirectory(0)
    return histo

def getCrossSection(filename):
    cs = 0
    p = re.compile("^NLO\+NLL.*")
    for m in ("","-"):
        f = CS_DIR + "/" + filename + m + ".output"
        print "Checking ", f
        fh = open(f, "r")
        for line in fh.readlines():
                if p.match(line):
                        print line
                        crossSection = float(line.split("(")[1].split(" ")[0])
                        print "CrossSection: ", crossSection
                        fh.close()
                        cs += crossSection
                        break
                fh.close()
    print "Summed cs:", cs
    if cs > 0:
        return cs
    return None

def stamp_plot():
    showlumi = True
    lumi = 135.0
    tl = TLatex()
    tl.SetNDC()
    cmsTextFont = 61
    extraTextFont = 52
    lumiTextSize = 0.6
    lumiTextOffset = 0.2
    cmsTextSize = 0.75
    cmsTextOffset = 0.1
    regularfont = 42
    tl.SetTextFont(cmsTextFont)
    tl.SetTextSize(0.85*tl.GetTextSize()) 
    tl.DrawLatex(0.165,0.915, 'CMS')
    tl.SetTextFont(extraTextFont)
    tl.SetTextSize(0.9*tl.GetTextSize())
    xlab = 0.26
    tl.DrawLatex(xlab,0.915, 'Work in Progress')
    tl.SetTextFont(regularfont)
    tl.SetTextSize(0.81*tl.GetTextSize())
    thingy = ''
    if showlumi: thingy+='#sqrt{s}=13 TeV, L = '+str(lumi)+' fb^{-1}'
    xthing = 0.6
    if not showlumi: xthing+=0.13 
    tl.DrawLatex(xthing,0.915,thingy)
    tl.SetTextSize(1.0/0.81*tl.GetTextSize())

def stampFab(lumi,datamc='MC'):
    tl.SetTextFont(cmsTextFont)
    tl.SetTextSize(1.55*tl.GetTextSize())
    tl.DrawLatex(0.152,0.82, 'CMS')
    tl.SetTextFont(extraTextFont)
    tl.DrawLatex(0.14,0.74, ('MC' in datamc)*' simulation'+' Progress')
    tl.SetTextFont(regularfont)
    if lumi=='': tl.DrawLatex(0.62,0.82,'#sqrt{s} = 13 TeV')
    else: tl.DrawLatex(0.42,0.82,'#sqrt{s} = 13 TeV, L = '+str(lumi)+' fb^{-1}')
    #tl.DrawLatex(0.64,0.82,'#sqrt{s} = 13 TeV')#, L = '+str(lumi)+' fb^{-1}')	
    tl.SetTextSize(tl.GetTextSize()/1.55)

def mkcanvas(name='canvas'):
    c = TCanvas(name,name, 800, 800)
    c.SetTopMargin(0.07)
    c.SetBottomMargin(0.16)
    c.SetLeftMargin(0.19)
    return c

def histoStyler(h):
    #h.SetLineWidth(2)
    #h.SetLineColor(color)
    size = 0.065
    font = 132
    h.GetXaxis().SetLabelFont(font)
    h.GetYaxis().SetLabelFont(font)
    h.GetXaxis().SetTitleFont(font)
    h.GetYaxis().SetTitleFont(font)
    h.GetYaxis().SetTitleSize(size)
    h.GetXaxis().SetTitleSize(size)
    h.GetXaxis().SetLabelSize(size)   
    h.GetYaxis().SetLabelSize(size)
    h.GetXaxis().SetTitleOffset(1.0)
    h.GetYaxis().SetTitleOffset(0.9)
    #h.Sumw2()

def getJsonLumiSection(lumiSecs):
    lumiSecsDict = {}
    lumiMap = lumiSecs.getMap()
    for k, v in lumiMap:
        lumiSecsDict[k] = []
        lumis = []
        for a in v: 
            lumis.append(a)
        lumis.sort()
        #print "Before:"
        #print lumis
        for lumisec in lumis:
            if len(lumiSecsDict[k]) > 0 and lumisec == lumiSecsDict[k][-1][-1]+1:
                lumiSecsDict[k][-1][-1] = lumisec
            else:
                lumiSecsDict[k].append([lumisec, lumisec])
        #print "After:"
        #print lumiSecsDict[k]
    #print "End:"
    return json.dumps(lumiSecsDict)

def get_lumi_from_bril(json_file_name, cern_username, retry=False):
    status, out = commands.getstatusoutput('ps axu | grep "itrac5117-v.cern.ch:1012" | grep -v grep')
    if status != 0:
        print "Opening SSH tunnel for brilcalc..."
        os.system("ssh -f -N -L 10121:itrac5117-v.cern.ch:10121 %s@lxplus.cern.ch" % cern_username)
    else:
        print "Existing tunnel for brilcalc found"
    print "Getting lumi for %s..." % json_file_name
    status, out = commands.getstatusoutput("export PATH=$HOME/.local/bin:/cvmfs/cms-bril.cern.ch/brilconda/bin:$PATH; brilcalc lumi --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -u /fb -c offsite -i %s > %s.briloutput; grep '|' %s.briloutput | tail -n1" % (json_file_name, json_file_name, json_file_name))
    if status != 0:
        if not retry:
            print "Trying to re-establish the tunnel..."
            os.system("pkill -f itrac5117")
            get_lumi_from_bril(json_file_name, cern_username, retry=True)
        else:
            print "Error while running brilcalc!"
            if cern_username == "ynissan":
                print "Did you set your CERN username with '--cern_username'?"
        lumi = -1
    else:
        print "Output: " + out
        lumi = float(out.split("|")[-2])
    
    print "lumi:", lumi
    return lumi

def calculateLumiFromLumiSecs(lumiSecs):
    json = getJsonLumiSection(lumiSecs)
    #print "Json:"
    #print json
    timestamp = int(time.time())
    tmpJsonFile = "/tmp/tmp_json_" + str(timestamp) + ".json"
    with open(tmpJsonFile, "w") as fo:
        fo.write(json)
    print "Created json file: " + tmpJsonFile
    lumi = get_lumi_from_bril(tmpJsonFile, 'ynissan')
    #os.remove(tmpJsonFile)
    return lumi
    
def getStackSum(hist):
    hists = hist.GetHists()
    newHist = hists[0].Clone()
    for i in range(1, len(hists)):
        newHist.Add(hists[i])
    return newHist

def mkhistlogx(name, title, nbins, xmin, xmax):
    logxmin = TMath.Log10(xmin)
    logxmax = TMath.Log10(xmax)
    binwidth = (logxmax-logxmin)/nbins
    xbins = array.array('d',[0]*(nbins+1))##might need to be defined out as 0's
    #xbins[0] = TMath.Power(10,logxmin)#xmin
    for i in range(0,nbins+1):
        xbins[i] = xmin + TMath.Power(10,logxmin+i*binwidth)    
    #print 'xbins', xbins        
    h = TH1F(name,title,nbins,xbins);
    return h

def getRealLogxHistogramFromTree(name, tree, obs, bins, minX, maxX, condition, overflow=True):
    h = mkhistlogx(name + "_logx", "", bins, minX, maxX)
    return getHistogramFromTree(name, tree, obs, bins, minX, maxX, condition, overflow, name + "_logx", True)
    
def getHistogramFromTree(name, tree, obs, bins, minX, maxX, condition, overflow=True, tmpName="hsqrt", predefBins = False, twoD = False, binsY = None, minBinsY = None, maxBinsY = None):
    if tree.GetEntries() == 0:
        return None
    binsStr = None
    # if tmpName == "hsqrt":
#         letters = string.ascii_lowercase
#         result_str = ''.join(random.choice(letters) for i in range(6))
#         tmpName += result_str
#         print "new tmp name is", tmpName
    if predefBins:
        binsStr = ">>" + tmpName
        tree.Draw(obs + binsStr, condition, "e")
    else:
        if bins is not None:
            binsStr = ">>" + tmpName + "(" + str(bins) + ","
            #print """tree.Draw(""" + obs + binsStr + str(minX) + "," + str(maxX) + ")", condition+""")"""
            tree.Draw(obs + binsStr + str(minX) + "," + str(maxX) + ")", condition, "e")
            #print obs + binsStr + str(minX) + "," + str(maxX) + ")"
            #print condition
        else:
            tree.Draw(obs + ">>" + tmpName, condition, "e")
    hist = tree.GetHistogram().Clone(name)
    hist.SetDirectory(0)
    if overflow:
        useCond = condition
        if not useCond:
            useCond = "1"
        over = hist.GetBinContent(hist.GetXaxis().GetNbins() + 1) #tree.Draw(obs, "(" + useCond + ") && " + obs + ">" + str(maxX))
        if over:
            hist.Fill(hist.GetXaxis().GetBinCenter(hist.GetXaxis().GetNbins()), over)
        under = hist.GetBinContent(0)# tree.Draw(obs, "(" + useCond + ") && " + obs + "<" + str(minX))
        if under:
            hist.Fill(hist.GetXaxis().GetBinCenter(1), under)
    return hist

def madHtCheck(current_file_name, madHT):
    if (madHT>0) and \
       ("DYJetsToLL_M-50_Tune" in current_file_name and madHT>100) or \
       ("WJetsToLNu_TuneCUETP8M1_13TeV" in current_file_name and madHT>100) or \
       ("HT-100to200_" in current_file_name and (madHT<100 or madHT>200)) or \
       ("HT-200to300_" in current_file_name and (madHT<200 or madHT>300)) or \
       ("HT-200to400_" in current_file_name and (madHT<200 or madHT>400)) or \
       ("HT-300to500_" in current_file_name and (madHT<300 or madHT>500)) or \
       ("HT-400to600_" in current_file_name and (madHT<400 or madHT>600)) or \
       ("HT-600to800_" in current_file_name and (madHT<600 or madHT>800)) or \
       ("HT-800to1200_" in current_file_name and (madHT<800 or madHT>1200)) or \
       ("HT-1200to2500_" in current_file_name and (madHT<1200 or madHT>2500)) or \
       ("HT-2500toInf_" in current_file_name and madHT<2500) or \
       ("HT-500to700_" in current_file_name and (madHT<500 or madHT>700)) or \
       ("HT-700to1000_" in current_file_name and (madHT<700 or madHT>1000)) or \
       ("HT-1000to1500_" in current_file_name and (madHT<1000 or madHT>1500)) or \
       ("HT-1500to2000_" in current_file_name and (madHT<1500 or madHT>2000)) or \
       ("HT-600toInf_" in current_file_name and (madHT<600)) or \
       ("HT-70to100_" in current_file_name and (madHT<70 or madHT>100)) or \
       ("HT-100To200_" in current_file_name and (madHT<100 or madHT>200)) or \
       ("HT-200To300_" in current_file_name and (madHT<200 or madHT>300)) or \
       ("HT-200To400_" in current_file_name and (madHT<200 or madHT>400)) or \
       ("HT-300To500_" in current_file_name and (madHT<300 or madHT>500)) or \
       ("HT-400To600_" in current_file_name and (madHT<400 or madHT>600)) or \
       ("HT-500To700_" in current_file_name and (madHT<500 or madHT>700)) or \
       ("HT-600To800_" in current_file_name and (madHT<600 or madHT>800)) or \
       ("HT-700To1000_" in current_file_name and (madHT<700 or madHT>1000)) or \
       ("HT-800To1200_" in current_file_name and (madHT<800 or madHT>1200)) or \
       ("HT-1000To1500_" in current_file_name and (madHT<1000 or madHT>1500)) or \
       ("HT-1200To2500_" in current_file_name and (madHT<1200 or madHT>2500)) or \
       ("HT-1500To2000_" in current_file_name and (madHT<1500 or madHT>2000)) or \
       ("HT-2500ToInf_" in current_file_name and madHT<2500):
        #print "MADHT FALSE"
        return False
    else:
        return True

def getLeptonCollectionFileMapFile(baseFileName):
    currLeptonCollectionFileMapFile, currLeptonCollectionFileMap = None, None
    mapNameFile = ""
    if "Run2016" in baseFileName and ".MET" in baseFileName:
        mapNameFile = "Run2016_MET.root"
    elif "Run2016" in baseFileName and ".SingleMuon" in baseFileName:
        mapNameFile = "Run2016_SingleMuon.root"
    else:
        mapNameFile = ("_".join(baseFileName.split(".")[1].split("_")[0:3])).split("AOD")[0] + ".root"

    print mapNameFile
    if not os.path.isfile(LEPTON_COLLECTION_FILES_MAP_DIR + "/" + mapNameFile):
        print "File " + LEPTON_COLLECTION_FILES_MAP_DIR + "/" + mapNameFile + " does not exist."
        return None
    print "Opening file map: " + LEPTON_COLLECTION_FILES_MAP_DIR + "/" + mapNameFile
    currLeptonCollectionFileMapFile = TFile(LEPTON_COLLECTION_FILES_MAP_DIR + "/" + mapNameFile, "read")
    print "After open"
    if currLeptonCollectionFileMapFile is None:
        return None
    
    return currLeptonCollectionFileMapFile
    
def getLeptonCollectionFileMap(currLeptonCollectionFileMapFile, runNum, lumiBlockNum, evtNum):
    #import gc
    currLeptonCollectionFileMap = None
    keys = currLeptonCollectionFileMapFile.GetListOfKeys()
    print "Looping over keys"
    print [key.GetName() for key in keys]
    for key in keys:
        print key.GetName()
        currLeptonCollectionFileMap = currLeptonCollectionFileMapFile.Get(key.GetName())
        if not currLeptonCollectionFileMap.contains(runNum, lumiBlockNum, evtNum):
            currLeptonCollectionFileMap.IsA().Destructor(currLeptonCollectionFileMap)
            #currLeptonCollectionFileMap.Delete()
            currLeptonCollectionFileMap = None
            #gc.collect()
            continue
        print "Found the correct file map!"
        return currLeptonCollectionFileMap
    print "Could not find file map for ", runNum, lumiBlockNum, evtNum
    return None 
    
def getLeptonCollection(currLeptonCollectionFileName):
    print "Opening file map: " + LEPTON_COLLECTION_DIR + "/" + currLeptonCollectionFileName
    currLeptonCollectionFile = TFile(LEPTON_COLLECTION_DIR + "/" + currLeptonCollectionFileName, "read")
    print "After open"
    leptonCollectionMap = currLeptonCollectionFile.Get("leptonCollectionMap")
    currLeptonCollectionFile.Close()
    return leptonCollectionMap

def getDmFromFileName(filename):
    print "Filename: " + filename
    return filename.split('_')[-1].split('Chi20Chipm')[0]

def getPointFromSamFileName(filename):
    print "Filename: " + filename
    return "_".join(os.path.basename(filename).split('_')[0:2])

def calcSignificance(sigHist, bgHist, ignoreCrossSection = False):
    sig = 0
    sigNum = 0
    bgNum = 0
    accumulate = False
    binsNumber = sigHist.GetNbinsX()
    cs = 1
    if not ignoreCrossSection:
        cs = 0.1
    #print "binsNumber=", binsNumber
    for bin in range(1, binsNumber + 1):
        if accumulate:
            sigNum += sigHist.GetBinContent(bin)
            bgNum += bgHist.GetBinContent(bin)
        else:
            sigNum = sigHist.GetBinContent(bin)
            bgNum = bgHist.GetBinContent(bin)
        if bgNum == 0:
            accumulate = True
        else:
            accumulate = False
            if bin <= binsNumber and bgHist.Integral(bin+1, binsNumber) == 0:
                sigNum += sigHist.Integral(bin, binsNumber)
                bgErr = 0.2 * bgNum
                sig = math.sqrt(sig**2 + (cs * (sigNum / math.sqrt(bgNum + bgErr**2)))**2)
                #print "**sigNum=", sigNum, "bgNum=", bgNum, "sig=", sig
                break
            else:
                #print "sigNum=", sigNum, "bgNum=", bgNum, "sig=", 0.1 * (sigNum / math.sqrt(bgNum))
                bgErr = 0.2 * bgNum
                sig = math.sqrt(sig**2 + (cs * (sigNum / math.sqrt(bgNum + bgErr**2)))**2)
    return sig

def calcZ(lhdH1, lhdH0):
    bayesfactor = lhdH1/lhdH0
    z = math.log(bayesfactor)/abs(math.log(bayesfactor))*math.sqrt(2*abs(math.log(bayesfactor)))
    return z

def calcSignificanceLlhdSingleCount(sigHist, bgHist):
    sig = 0
    sigNum = 0
    bgNum = 0
    bgError = 0
    accumulate = False
    binsNumber = sigHist.GetNbinsX()
    lhdH0 = 1
    lhdH1 = 1
    
    #print "binsNumber=", binsNumber
    for bin in range(1, binsNumber + 1):
        if accumulate:
            sigNum += sigHist.GetBinContent(bin)          
            bgNum += bgHist.GetBinContent(bin)
            bgError = math.sqrt(bgError**2 + bgHist.GetBinError(bin)**2)
        else:
            sigNum = sigHist.GetBinContent(bin)
            bgNum = bgHist.GetBinContent(bin)
            bgError = bgHist.GetBinError(bin)
        if bgNum == 0:
            accumulate = True
        else:
            accumulate = False
            if bin <= binsNumber and bgHist.Integral(bin+1, binsNumber) == 0:
                sigNum += sigHist.Integral(bin, binsNumber)
                #lhd(double N,double s,double B,double dB)
                lhdH0 *= lhd(bgNum,0,bgNum,bgError)
                lhdH1 *= lhd(bgNum,0.1*sigNum,bgNum,bgError)
                
                if lhdH1 / lhdH0 != 1 and calcZ(lhdH1, lhdH0) > 0:
                    print "OOOOOOPPPPS!", "lhdH1", lhdH1, "lhdH0", lhdH0, "sigNum", sigNum, "bgNum", bgNum, "bgError", bgError, "Z", calcZ(lhdH1, lhdH0)
                #sig += 0.1 * (sigNum / math.sqrt(bgNum))
                #print "**sigNum=", sigNum, "bgNum=", bgNum, "sig=", sig
                break
            else:
                #print "sigNum=", sigNum, "bgNum=", bgNum, "sig=", 0.1 * (sigNum / math.sqrt(bgNum))
                if lhdH1 / lhdH0 != 1 and calcZ(lhdH1, lhdH0) > 0:
                    print "BEFORE OOOOOOPPPPS!", "lhdH1", lhdH1, "lhdH0", lhdH0, "sigNum", sigNum, "bgNum", bgNum, "bgError", bgError, "Z", calcZ(lhdH1, lhdH0)
                
                lhdH0 *= lhd(bgNum,0,bgNum,bgError)
                lhdH1 *= lhd(bgNum,0.1*sigNum,bgNum,bgError)
                
                if lhdH1 / lhdH0 != 1 and calcZ(lhdH1, lhdH0) > 0:
                    print "AFTER OOOOOOPPPPS!", "lhdH1", lhdH1, "lhdH0", lhdH0, "sigNum", sigNum, "bgNum", bgNum, "bgError", bgError, "Z", calcZ(lhdH1, lhdH0)
                
    
    if lhdH1 / lhdH0 == 1:
        return 0
                
    bayesfactor = lhdH1/lhdH0
    if math.log(bayesfactor)/abs(math.log(bayesfactor)) >0:
        print "WOW!! lhdH1", lhdH1, "lhdH0", lhdH0
        
    return calcZ(lhdH1, lhdH0)



