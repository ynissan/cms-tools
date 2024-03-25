from ROOT import *
import CMS_lumi, tdrstyle

class StampStr:
    WIP = "Work in Progress"
    SIM = "Simulation"
    PRE = "Preliminary"
    SIMWIP = "#splitline{Simulation}{Work in Progress}"

class Plotting():
    
    def __init__(self, W_ref=800,H_ref=600):

#        self.text = "13 TeV"
#        self.extratext = "Preliminary"
#        self.H_ref = 600
#        self.W_ref = 800
    
        self.W = W_ref
        self.H  = H_ref
    
    def setStyle(self):
        self.currStyle = tdrstyle.setTDRStyle()
        gROOT.SetStyle("tdrStyle")
        gROOT.ForceStyle()
    
    def createCanvas(self, name):
        return TCanvas(name, name, self.W, self.H)

    def stampPlot(self,canvas, lumiStr, labelText, cmsLocation, showLumi):
        iPeriod = 0
        if showLumi:
            iPeriod = 4
        iPos = 10
        CMS_lumi.extraText = labelText
        CMS_lumi.lumi_13TeV = lumiStr + " fb^{-1}"
        CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)


defaultColorPalette = [
    { "name" : "azure", "fillColor" : kAzure-4, "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 4,  "markerStyle" : kOpenTriangleUp },
    { "name" : "yellow", "fillColor" : kYellow-4, "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 5,  "markerStyle" : kOpenCircle},
    { "name" : "red", "fillColor" : kRed-4, "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "azure", "fillColor" : kAzure-4, "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 4,  "markerStyle" : kOpenTriangleUp },
    { "name" : "cyan", "fillColor" : kCyan-7, "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 3,  "markerStyle" : kOpenSquare },
    { "name" : "spring", "fillColor" : kSpring-1, "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 3,  "markerStyle" : kOpenSquare },
    { "name" : "gray", "fillColor" : kGray+1, "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 6,  "markerStyle" : kOpenDiamond },
    { "name" : "teal", "fillColor" : kTeal-9, "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "orange", "fillColor" : "#ffbb00", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "lightgreen", "fillColor" : "#42f498", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    
    { "name" : "velvet", "fillColor" : "#ff00c9", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "darkblue", "fillColor" : "#1B00DC", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    
    { "name" : "maroon", "fillColor" : "#800000", "lineColor" : "#A52A2A", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "darkslategray", "fillColor" : "#2F4F4F", "lineColor" : "#708090", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "wheat", "fillColor" : "#F5DEB3", "lineColor" : "#FFDEAD", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "lightgray", "fillColor" : "#D3D3D3", "lineColor" : "#DCDCDC", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    
    { "name" : "black", "fillColor" : kBlack, "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
]
# defaultColorPalette = [
#     { "name" : "su", "fillColor" : "#3f90da", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 4,  "markerStyle" : kOpenTriangleUp },
#     { "name" : "sy", "fillColor" : "#ffa90e", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 5,  "markerStyle" : kOpenCircle},
#     { "name" : "sus", "fillColor" : "#bd1f01", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
#     { "name" : "y", "fillColor" : "#94a4a2", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 4,  "markerStyle" : kOpenTriangleUp },
#     { "name" : "susy", "fillColor" : "#832db6", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 3,  "markerStyle" : kOpenSquare },
#     { "name" : "ys", "fillColor" : "#a96b59", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 3,  "markerStyle" : kOpenSquare },
#     { "name" : "us", "fillColor" : "#e76300", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 6,  "markerStyle" : kOpenDiamond },
#     { "name" : "ysu", "fillColor" : "#b9ac70", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
#     { "name" : "s", "fillColor" : "#717581", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
#     { "name" : "ysus", "fillColor" : "#92dadd", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
#     
#     { "name" : "velvet", "fillColor" : "#ff00c9", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
#     { "name" : "darkblue", "fillColor" : "#1B00DC", "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
#     
#     { "name" : "maroon", "fillColor" : "#800000", "lineColor" : "#A52A2A", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
#     { "name" : "darkslategray", "fillColor" : "#2F4F4F", "lineColor" : "#708090", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
#     { "name" : "wheat", "fillColor" : "#F5DEB3", "lineColor" : "#FFDEAD", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
#     { "name" : "lightgray", "fillColor" : "#D3D3D3", "lineColor" : "#DCDCDC", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
#     
#     { "name" : "black", "fillColor" : kBlack, "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
# ]

#For solid fill use fillStyle=1001
# signalCp = [
#     { "name" : "blue", "fillColor" : kBlue+3, "lineColor" : kBlue+3, "fillStyle" : 0, "lineStyle" : 1 },
#     { "name" : "cyan", "fillColor" : kCyan+3, "lineColor" : kCyan+3, "fillStyle" : 0, "lineStyle" : 2 },
#     { "name" : "orange", "fillColor" : kOrange, "lineColor" : kOrange, "fillStyle" : 0, "lineStyle" : 5 },
#     { "name" : "pink", "fillColor" : kPink+3, "lineColor" : kPink+4, "fillStyle" : 0, "lineStyle" : 6 },
#     { "name" : "grey", "fillColor" : kGray, "lineColor" : kGray, "fillStyle" : 0, "lineStyle" : 4 },
#     { "name" : "red", "fillColor" : kRed, "lineColor" : kRed, "fillStyle" : 0, "lineStyle" : 3 },
# ]


signalCp = [
    { "name" : "blue", "fillColor" : kRed, "lineColor" : kRed-6, "fillStyle" : 0, "lineStyle" : 1 },
    { "name" : "cyan", "fillColor" : kRed+1, "lineColor" : kYellow-4, "fillStyle" : 0, "lineStyle" : 2 },
    { "name" : "orange", "fillColor" : kRed+2, "lineColor" : kRed+4, "fillStyle" : 0, "lineStyle" : 5 },
    { "name" : "pink", "fillColor" : kRed+3, "lineColor" : kTeal-9, "fillStyle" : 0, "lineStyle" : 6 },
    { "name" : "grey", "fillColor" : kRed+4, "lineColor" : kRed+4, "fillStyle" : 0, "lineStyle" : 4 },
    { "name" : "red", "fillColor" : kRed-1, "lineColor" : kRed-1, "fillStyle" : 0, "lineStyle" : 3 }, #startet copypasting below here
    { "name" : "blue", "fillColor" : kRed, "lineColor" : kRed, "fillStyle" : 0, "lineStyle" : 1 },
    { "name" : "cyan", "fillColor" : kRed+1, "lineColor" : kRed+1, "fillStyle" : 0, "lineStyle" : 2 },
    { "name" : "orange", "fillColor" : kRed+2, "lineColor" : kRed+2, "fillStyle" : 0, "lineStyle" : 5 },
    { "name" : "pink", "fillColor" : kRed+3, "lineColor" : kRed+3, "fillStyle" : 0, "lineStyle" : 6 },
    { "name" : "grey", "fillColor" : kRed+4, "lineColor" : kRed+4, "fillStyle" : 0, "lineStyle" : 4 },
    { "name" : "red", "fillColor" : kRed-1, "lineColor" : kRed-1, "fillStyle" : 0, "lineStyle" : 3 },    
    { "name" : "blue", "fillColor" : kRed, "lineColor" : kRed, "fillStyle" : 0, "lineStyle" : 1 },
    { "name" : "cyan", "fillColor" : kRed+1, "lineColor" : kRed+1, "fillStyle" : 0, "lineStyle" : 2 },
    { "name" : "orange", "fillColor" : kRed+2, "lineColor" : kRed+2, "fillStyle" : 0, "lineStyle" : 5 },
    { "name" : "pink", "fillColor" : kRed+3, "lineColor" : kRed+3, "fillStyle" : 0, "lineStyle" : 6 },
    { "name" : "grey", "fillColor" : kRed+4, "lineColor" : kRed+4, "fillStyle" : 0, "lineStyle" : 4 },
    { "name" : "red", "fillColor" : kRed-1, "lineColor" : kRed-1, "fillStyle" : 0, "lineStyle" : 3 },
    { "name" : "blue", "fillColor" : kRed, "lineColor" : kRed, "fillStyle" : 0, "lineStyle" : 1 },
    { "name" : "cyan", "fillColor" : kRed+1, "lineColor" : kRed+1, "fillStyle" : 0, "lineStyle" : 2 },
    { "name" : "orange", "fillColor" : kRed+2, "lineColor" : kRed+2, "fillStyle" : 0, "lineStyle" : 5 },
    { "name" : "pink", "fillColor" : kRed+3, "lineColor" : kRed+3, "fillStyle" : 0, "lineStyle" : 6 },
    { "name" : "grey", "fillColor" : kRed+4, "lineColor" : kRed+4, "fillStyle" : 0, "lineStyle" : 4 },
    { "name" : "red", "fillColor" : kRed-1, "lineColor" : kRed-1, "fillStyle" : 0, "lineStyle" : 3 },
    { "name" : "blue", "fillColor" : kRed, "lineColor" : kRed, "fillStyle" : 0, "lineStyle" : 1 },
    { "name" : "cyan", "fillColor" : kRed+1, "lineColor" : kRed+1, "fillStyle" : 0, "lineStyle" : 2 },
    { "name" : "orange", "fillColor" : kRed+2, "lineColor" : kRed+2, "fillStyle" : 0, "lineStyle" : 5 },
    { "name" : "pink", "fillColor" : kRed+3, "lineColor" : kRed+3, "fillStyle" : 0, "lineStyle" : 6 },
    { "name" : "grey", "fillColor" : kRed+4, "lineColor" : kRed+4, "fillStyle" : 0, "lineStyle" : 4 },
    { "name" : "red", "fillColor" : kRed-1, "lineColor" : kRed-1, "fillStyle" : 0, "lineStyle" : 3 },
    { "name" : "blue", "fillColor" : kRed, "lineColor" : kRed, "fillStyle" : 0, "lineStyle" : 1 },
    { "name" : "cyan", "fillColor" : kRed+1, "lineColor" : kRed+1, "fillStyle" : 0, "lineStyle" : 2 },
    { "name" : "orange", "fillColor" : kRed+2, "lineColor" : kRed+2, "fillStyle" : 0, "lineStyle" : 5 },
    { "name" : "pink", "fillColor" : kRed+3, "lineColor" : kRed+3, "fillStyle" : 0, "lineStyle" : 6 },
    { "name" : "grey", "fillColor" : kRed+4, "lineColor" : kRed+4, "fillStyle" : 0, "lineStyle" : 4 },
    { "name" : "red", "fillColor" : kRed-1, "lineColor" : kRed-1, "fillStyle" : 0, "lineStyle" : 3 },    
]

# For signal with only lines - only first two arguments relevant (alpha is only for the fill)
# then the fill is set to 0 by "fillStyle" : 0  in the signalCp
# For a filled histogram normally alpha is given and noFillStyle=True (so that 1001 is picked)

def setHistColorFillLine(hist, cP, alpha=0.35,noFillStyle=False, lineWidth = 1):
    fillC = cP["fillColor"]
    lineC = cP["lineColor"]
    if "fillStyle" in cP and not noFillStyle:
        hist.SetFillStyle(cP["fillStyle"])
    else:
        hist.SetFillStyle(1001)
    hist.SetFillColorAlpha(fillC, alpha)
    print("SetLineColor(", lineC, ")")
    hist.SetLineColor(lineC)
    #if cP.get("lineStyle") is not None:
    #    hist.SetLineStyle(cP["lineStyle"])

    hist.SetLineWidth(lineWidth)
    hist.SetOption("HIST")

def styledStackFromStack(bgHist, memory, legend=None, title="", colorInx=None, noFillStyle=False, plotPoint = False, legendNames = {}, noStack=False, colorPalette=defaultColorPalette):
    newStack = THStack(bgHist.GetName(), title)
    newStack.UseCurrentStyle()
    memory.append(newStack)
    
    if bgHist is None or bgHist.GetNhists() == 0:
        return newStack
    #print "Num of hists: " + str(bgHist.GetNhists())
    bgHists = bgHist.GetHists()

    for i, hist in enumerate(bgHists):
        if hist.GetMaximum() == 0:
            print("Skipping " + hist.GetName())
            continue
        newHist = hist.Clone()
        newHist.UseCurrentStyle()
        memory.append(newHist)
        colorI = i
        if colorInx is not None:
            colorI = colorInx[i]
        print(colorI, colorInx)
        setHistColorFillLine(newHist, colorPalette[colorI], 0.75, noFillStyle)
        if noStack:
            newHist.SetFillStyle(0)
        lineC = TColor.GetColor(colorPalette[colorI]["fillColor"])
        
        #newHist.SetMarkerColorAlpha(colorPalette[colorI]["markerColor"], 0.9)
        
        if plotPoint:
            newHist.SetMarkerColorAlpha(lineC, 1)
            newHist.SetMarkerStyle(colorPalette[colorI]["markerStyle"])
            newHist.SetLineColor(lineC)
        else:
            newHist.SetMarkerColorAlpha(lineC, 0.9)

        newStack.Add(newHist)

        if legend is not None:
            legendName = hist.GetName().split("_")[-1]
            print("Adding to legend " + legendName, legendNames)
            if legendNames.get(hist.GetName().split("_")[-1]) is not None:
                legendName = legendNames[hist.GetName().split("_")[-1]]
            if plotPoint:
                legend.AddEntry(newHist, legendName, 'p')
            elif noStack:
                legend.AddEntry(newHist, legendName, 'l')
            else:
                legend.AddEntry(newHist, legendName, 'F')

    return newStack
 


##### DEPRECATED FORMATTING MOVED FROM UTILS

def deprecated_setLabels(sigHist, histDef):
    sigHist.SetTitle(histDef["title"])
    if "xAxis" in histDef:
        sigHist.GetXaxis().SetTitle(histDef["xAxis"])
    if "yAxis" in histDef:
        sigHist.GetXaxis().SetTitle(histDef["yAxis"])

def deprecated_histoStyler(h, ratio = False):
    #h.SetLineWidth(2)
    #h.SetLineColor(color)
    if h is None or h.GetXaxis() is None:
        return
    font = 132
    if ratio:
        size = 0.15
        labelSize = 0.14
        h.GetYaxis().SetTitleOffset(0.38)
    else:
        size = 0.04
        labelSize = 0.04
        #print h.GetXaxis()
        h.GetXaxis().SetTitleOffset(1.0)
        h.GetYaxis().SetTitleOffset(1.5)
    
    h.GetXaxis().SetLabelFont(font)
    h.GetYaxis().SetLabelFont(font)
    h.GetXaxis().SetTitleFont(font)
    h.GetYaxis().SetTitleFont(font)
    h.GetYaxis().SetTitleSize(size)
    h.GetXaxis().SetTitleSize(size)
    h.GetXaxis().SetLabelSize(labelSize)   
    h.GetYaxis().SetLabelSize(labelSize)

def deprecated_formatLegend(legend):
    legend.SetTextFont(132)

class StampCoor:
    #ABOVE_PLOT = {"x" : 0.18, "y" : 0.915}
    #ABOVE_PLOT = {"x" : 0.1, "y" : 0.915}
    ABOVE_PLOT = {"x" : 0.13, "y" : 0.915}
    ABOVE_PLOT_SPACE_FOR_EXP = {"x" : 0.25, "y" : 0.915}
    TOP_OF_PLOT = {"x" : 0.205, "y" : 0.85}
    TOP_OF_PLOT_LABEL_BELLOW_CMS = {"x" : 0.205, "y" : 0.85, "labelX" : 0.205, "labelY" : 0.8}

def stamp_plot(lumi = 135.0, label = StampStr.WIP, cmsLocation = StampCoor.ABOVE_PLOT, showlumi = True):
    
    tl = TLatex()
    tl.SetNDC()
    # DEFUALT TEXT ALIGNMENT IS 11 (left adjusted and bottom adjusted)
    
    cmsTextFont = 61
    extraTextFont = 52
    regularfont = 42
    
    lumiTextSize = 0.6
    lumiTextOffset = 0.2
    
    cmsTextSize = 0.75
    cmsTextOffset = 0.1
    
    tl.SetTextFont(cmsTextFont)
    # DEFUALT TEXT SIZE IS 0.05
    tl.SetTextSize(0.85*tl.GetTextSize())
    tl.DrawLatex(cmsLocation["x"],cmsLocation["y"], 'CMS')
    print(cmsLocation)

    tl.SetTextFont(extraTextFont)
    tl.SetTextSize(0.78*tl.GetTextSize())
    labelX = cmsLocation["labelX"] if cmsLocation.get("labelX") is not None else cmsLocation["x"] + 0.095
    labelY = cmsLocation["labelY"] if cmsLocation.get("labelY") is not None else cmsLocation["y"]
    tl.DrawLatex(labelX, labelY, label)
    
    tl.SetTextFont(regularfont)
    tl.SetTextSize(0.81*tl.GetTextSize())
    #lumiText = '#sqrt{s}=13 TeV'
    lumiText = '(13 TeV)'
    #if showlumi: lumiText+=', L = '+str(lumi)+' fb^{-1}'
    if showlumi: lumiText = str(lumi)+' fb^{-1} (13 TeV)'
    # align right
    tl.SetTextAlign(31)
    
    #tl.DrawLatex(0.9,StampCoor.ABOVE_PLOT["y"],lumiText)
    tl.DrawLatex(0.98,StampCoor.ABOVE_PLOT["y"],lumiText)
    #tl.SetTextSize(1.0/0.81*tl.GetTextSize())
    
    # testing = TLatex()
#     testing.SetNDC()
#     testing.SetTextFont(cmsTextFont)
#     testing.SetTextSize(0.85*testing.GetTextSize()) 
#     print "--------", testing.GetTextSize()
#     testing.DrawLatex(0.18,0.915, 'CMS')
#     
#     testing.SetTextFont(extraTextFont)
#     testing.SetTextSize(0.78*testing.GetTextSize())
#     testing.DrawLatex(0.27,0.915, label)
#     #testing.DrawLatex(0.34,0.915, label)
#     
#     #testing.DrawLatex(0.34,0.915, label)
#     
#     testing.DrawLatex(0.205,0.85, 'TEST2')
#     testing.SetTextFont(extraTextFont)
#     testing.SetTextSize(0.78*testing.GetTextSize())
#     testing.DrawLatex(0.205,0.80, label)
    
    

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
    
    #h.Sumw2()

oldColorPalette = [
    { "name" : "yellow", "fillColor" : "#fcf802", "lineColor" : "#e0dc00", "fillStyle" : 3444, "markerColor" : 5,  "markerStyle" : kOpenCircle},
    { "name" : "green", "fillColor" : "#0bb200", "lineColor" : "#099300", "fillStyle" : 3444, "markerColor" : 3,  "markerStyle" : kOpenSquare },
    { "name" : "blue", "fillColor" : "#0033cc", "lineColor" : "#00279e", "fillStyle" : 3444, "markerColor" : 4,  "markerStyle" : kOpenTriangleUp },
    { "name" : "purple", "fillColor" : "#f442f1", "lineColor" : "#a82ba6", "fillStyle" : 3444, "markerColor" : 6,  "markerStyle" : kOpenDiamond },
    { "name" : "tourq", "fillColor" : "#00ffe9", "lineColor" : "#2a8c83", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "orange", "fillColor" : "#ffbb00", "lineColor" : "#b78b12", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "lightgreen", "fillColor" : "#42f498", "lineColor" : "#28a363", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "red", "fillColor" : "#e60000", "lineColor" : "#c60000", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "velvet", "fillColor" : "#ff00c9", "lineColor" : "#ff8ee7", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "darkblue", "fillColor" : "#1B00DC", "lineColor" : "#8373FA", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    
    { "name" : "maroon", "fillColor" : "#800000", "lineColor" : "#A52A2A", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "darkslategray", "fillColor" : "#2F4F4F", "lineColor" : "#708090", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "wheat", "fillColor" : "#F5DEB3", "lineColor" : "#FFDEAD", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    { "name" : "lightgray", "fillColor" : "#D3D3D3", "lineColor" : "#DCDCDC", "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
    
    { "name" : "black", "fillColor" : kBlack, "lineColor" : kBlack, "fillStyle" : 3444, "markerColor" : 38,  "markerStyle" : kOpenCross },
]

oldSignalCp = [
    { "name" : "blue", "fillColor" : "#000f96", "lineColor" : "#1d0089", "fillStyle" : 0 },
    { "name" : "grey", "fillColor" : "#898989", "lineColor" : "#636363", "fillStyle" : 0 },
    { "name" : "black", "fillColor" : "#012a6d", "lineColor" : "#01173a", "fillStyle" : 0 },
    { "name" : "red", "fillColor" : "#ff0000", "lineColor" : "#ff0000", "fillStyle" : 0 },
    { "name" : "purple", "fillColor" : "#a82ba6", "lineColor" : "#a82ba6", "fillStyle" : 0 },
    { "name" : "orange", "fillColor" : "#b78b12", "lineColor" : "#b78b12", "fillStyle" : 0 },
]
