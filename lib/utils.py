from ROOT import *
import sys
import numpy as np

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import histograms
from lib import cuts
import os, re

import array

colorPalette = [
    { "name" : "green", "fillColor" : "#0bb200", "lineColor" : "#099300", "fillStyle" : 3444 },
    { "name" : "yellow", "fillColor" : "#fcf802", "lineColor" : "#e0dc00", "fillStyle" : 3444 },
    { "name" : "blue", "fillColor" : "#0033cc", "lineColor" : "#00279e", "fillStyle" : 3444 },
    { "name" : "purple", "fillColor" : "#f442f1", "lineColor" : "#a82ba6", "fillStyle" : 3444 },
    { "name" : "tourq", "fillColor" : "#00ffe9", "lineColor" : "#2a8c83", "fillStyle" : 3444 },
    { "name" : "orange", "fillColor" : "#ffbb00", "lineColor" : "#b78b12", "fillStyle" : 3444 },
    { "name" : "lightgreen", "fillColor" : "#42f498", "lineColor" : "#28a363", "fillStyle" : 3444 },
    { "name" : "red", "fillColor" : "#e60000", "lineColor" : "#c60000", "fillStyle" : 3444 },
    { "name" : "black", "fillColor" : kBlack, "lineColor" : kBlack, "fillStyle" : 3444 },
]

crossSections = {
    "dm7"  : 1.21547,
    "dm13" : 1.21547,
    "dm20" : 1.21547
}

LUMINOSITY = 35900. #pb^-1
CMS_WD="/afs/desy.de/user/n/nissanuv/CMSSW_10_1_0/src"
CS_DIR="/afs/desy.de/user/n/nissanuv/nfs/x1x2x1/signal/cs/stdout"

epsilon = 0.00001

#For solid fill use fillStyle=1001
signalCp = [
    { "name" : "blue", "fillColor" : "#000f96", "lineColor" : "#1d0089", "fillStyle" : 0 },
    { "name" : "grey", "fillColor" : "#898989", "lineColor" : "#636363", "fillStyle" : 0 },
    { "name" : "black", "fillColor" : "#012a6d", "lineColor" : "#01173a", "fillStyle" : 0 },
]

compoundTypes = {
    "Rare" : ["WZZ", "WWZ", "ZZZ"],
    "DiBoson" : ["WZ", "WW", "ZZ"],
    "TTJets": ["ST_t-channel_antitop", "ST_t-channel_top", "TTJets_DiLept", "TTJets_SingleLeptFromT", "TTJets_SingleLeptFromTbar"]
}

bgOrder = {
    "Rare" : 0,
    "TTWJetsToLNu" : 1,
    "DiBoson" : 2,
    "ZJetsToNuNu" : 3,
    "DYJetsToLL" : 4,
    "TTJets" : 5,
#    "QCD" : 6,
    "WJetsToLNu" : 6
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


def existsInCoumpoundType(key):
    for cType in compoundTypes:
        if key in compoundTypes[cType]:
            return True
    return False

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

    bgHists = bgHist.GetHists()

    for i, hist in enumerate(bgHists):
        newHist = hist.Clone()
        memory.append(newHist)
        colorI = i
        if colorInx is not None:
            colorI = colorInx[i]
        formatHist(newHist, colorPalette[colorI], 0.35, noFillStyle)
        newStack.Add(newHist)
        if legend is not None:
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
    lumi = 35.9
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