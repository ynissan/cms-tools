from ROOT import *
import sys
import numpy as np
import os
import math
import xml.etree.ElementTree as ET
from array import array

def get_method_hists(folders, method, gtestBGHists=None, gtrainBGHists=None, gtestSignalHists=None, gtrainSignalHists=None, gmethods=None, gnames=None, bins=10000, condition="", weight=False):
    testBGHists = []
    trainBGHists = []
    testSignalHists = []
    trainSignalHists = []
    methods=[]
    names=[]
    if not folders:
        if not gtestBGHists:
            return (testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names)
        else:
            return (gtestBGHists, gtrainBGHists, gtestSignalHists, gtrainSignalHists, gmethods, gnames)
    for dir in folders:
        name = os.path.basename(dir)
        print("dir=" + dir)
        print("name=" + name)
        names.append(name)
    
        inputFile = dir + "/" + name  + ".root"
        print("Opening file", inputFile)
        print("get_method_hists condition=" + condition)
        fin = TFile(inputFile)

        trainTree = fin.Get("dataset/TrainTree")
        testTree = fin.Get("dataset/TestTree")
        binsStr = ">>hsqrt(" + str(bins) + ")"
        weightStr = "" if not weight else "Weight * "
        testTree.Draw(method + binsStr, weightStr + "(classID==0"+condition+")")
        testSignalHist = testTree.GetHistogram().Clone()
        #print method + " testSignalHist=" + str(testSignalHist.Integral())
        testSignalHist.SetDirectory(0)
        testTree.Draw(method + binsStr, weightStr + "(classID==1"+condition+")")
        testBgHist = testTree.GetHistogram().Clone()
        #print method + " testBgHist=" + str(testBgHist.Integral())
        testBgHist.SetDirectory(0)
        trainTree.Draw(method + binsStr, weightStr + "(classID==0"+condition+")")
        trainSignalHist = trainTree.GetHistogram().Clone()
        #print method + " trainSignalHist=" + str(trainSignalHist.Integral())
        trainSignalHist.SetDirectory(0)
        trainTree.Draw(method + binsStr, weightStr + "(classID==1"+condition+")")
        trainBgHist = trainTree.GetHistogram().Clone()
        #print method + " trainBgHist=" + str(trainBgHist.Integral())
        trainBgHist.SetDirectory(0)
    
        #print "max=", trainSignalHist.GetXaxis().GetXmax()
    
        minX = min(testBgHist.GetXaxis().GetXmin(), testSignalHist.GetXaxis().GetXmin(), trainSignalHist.GetXaxis().GetXmin(), trainBgHist.GetXaxis().GetXmin())
        maxX = max(testBgHist.GetXaxis().GetXmax(), testSignalHist.GetXaxis().GetXmax(), trainSignalHist.GetXaxis().GetXmax(), trainBgHist.GetXaxis().GetXmax())
        #print "======="
        #print minX, maxX
        binsStr = ">>hsqrt(" + str(bins) + ","
        testTree.Draw(method + binsStr + str(minX) + "," + str(maxX) + ")", weightStr + "(classID==0"+condition+")")
        testSignalHist = testTree.GetHistogram().Clone()
        testSignalHist.SetDirectory(0)
        #print method + " testSignalHist=" + str(testSignalHist.Integral())
        testTree.Draw(method + binsStr + str(minX) + "," + str(maxX) + ")", weightStr + "(classID==1"+condition+")")
        testBgHist = testTree.GetHistogram().Clone()
        testBgHist.SetDirectory(0)
        #print method + " testBgHist=" + str(testBgHist.Integral())
        trainTree.Draw(method + binsStr + str(minX) + "," + str(maxX) + "", weightStr + "(classID==0"+condition+")")
        trainSignalHist = trainTree.GetHistogram().Clone()
        trainSignalHist.SetDirectory(0)
        #print method + " trainSignalHist=" + str(trainSignalHist.Integral())
        trainTree.Draw(method + binsStr + str(minX) + "," + str(maxX) + "", weightStr + "(classID==1"+condition+")")
        trainBgHist = trainTree.GetHistogram().Clone()
        trainBgHist.SetDirectory(0)
        #print method + " trainBgHist=" + str(trainBgHist.Integral())
    
        testBGHists.append(testBgHist)
        trainBGHists.append(trainBgHist)
        testSignalHists.append(testSignalHist)
        trainSignalHists.append(trainSignalHist)
        methods.append(method)
    
        fin.Close()
    if gtestBGHists is None:
        return (testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names)
    else:
        gtestBGHists.extend(testBGHists)
        gtrainBGHists.extend(trainBGHists)
        gtestSignalHists.extend(testSignalHists)
        gtrainSignalHists.extend(trainSignalHists)
        gmethods.extend(methods)
        gnames.extend(names)
        return (gtestBGHists, gtrainBGHists, gtestSignalHists, gtrainSignalHists, gmethods, gnames)


#def get_bdt_hists(folders, testBGHists=None, trainBGHists=None, testSignalHists=None, trainSignalHists=None, methods=None, names=None, bins=10000,  condition=""):
#    return get_method_hists(folders, "BDT", testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names, bins, condition)

#def get_mlp_hists(folders, testBGHists=None, trainBGHists=None, testSignalHists=None, trainSignalHists=None, methods=None, names=None, bins=10000, condition=""):
#    return get_method_hists(folders, "MLP", testBGHists, trainBGHists, testSignalHists, trainSignalHists, methods, names, bins, condition)

def getHighestZ(trainSignalHist, trainBGHist, testSignalHist, testBGHist, h=None,cs=1):
    highestZ = 0
    highestS = 0
    highestB = 0
    highestBDT = 0

    numOfBins = testBGHist.GetNbinsX()
    #print "These are all the bins:"
    #print testBGHist.GetNbinsX(), trainBGHist.GetNbinsX(), testSignalHist.GetNbinsX(), testBGHist.GetNbinsX()
    #print "numOfBins=" , numOfBins

    ST = (trainSignalHist.Integral() + testSignalHist.Integral())*cs
    BT = (trainBGHist.Integral() + testBGHist.Integral())*cs
    print("==================")
    print("Signal: " + str(ST))
    print("Background: " + str(BT))

    for i in range(numOfBins):
        S = (trainSignalHist.Integral(i,numOfBins+1) + testSignalHist.Integral(i,numOfBins+1))*cs
        B = (trainBGHist.Integral(i,numOfBins+1) + testBGHist.Integral(i,numOfBins+1))*cs
        if h is not None:
            h.SetPoint(i,S/ST, 1 - B/BT)
        if S + B:
            Z = 1.0 * S/math.sqrt(S+B)
            if Z > highestZ:
                highestZ = Z
                highestS = S
                highestB = B
                highestMVA = trainSignalHist.GetBinCenter(i)
                #print trainSignalHist.GetBinCenter(i), testSignalHist.GetBinCenter(i), trainBGHist.GetBinCenter(i), testBGHist.GetBinCenter(i)

    #print "=================="

    return highestZ, highestS, highestB, highestMVA, ST, BT

def getRocWithMvaCut(trainSignalHist, trainBGHist, testSignalHist, testBGHist, mvaCut=0, h=None,cs=1):
    S = 0
    B = 0

    numOfBins = testBGHist.GetNbinsX()

    ST = (trainSignalHist.Integral() + testSignalHist.Integral())*cs
    BT = (trainBGHist.Integral() + testBGHist.Integral())*cs
    print("==================")
    print("Signal: " + str(ST))
    print("Background: " + str(BT))

    for i in range(numOfBins):
        s = (trainSignalHist.Integral(i,numOfBins+1) + testSignalHist.Integral(i,numOfBins+1))*cs
        b = (trainBGHist.Integral(i,numOfBins+1) + testBGHist.Integral(i,numOfBins+1))*cs
        if h is not None:
            h.SetPoint(i,s/ST, 1 - b/BT)
        if trainSignalHist.GetBinCenter(i) <= mvaCut:
            S = s
            B = b
    return S, B, ST, BT

def getVariablesFromXMLWeightsFile(file):
    tree = ET.parse(file)
    root = tree.getroot()
    vars = root.find('Variables')
    varsFromFile = []
    for var in vars.iter('Variable'):
        varsFromFile.append({"name" : var.get('Expression'), "type" : var.get('Type')})
    return varsFromFile

def getSpecSpectatorFromXMLWeightsFile(file):
    tree = ET.parse(file)
    root = tree.getroot()
    vars = root.find('Spectators')
    varsFromFile = []
    for var in vars.iter('Spectator'):
        varsFromFile.append({"name" : var.get('Expression'), "type" : var.get('Type')})
    return varsFromFile

def getVariablesMemMap(vars):
    memMap = {}
    for var in vars:
        memMap[var["name"]] = array('f', [0])
    return memMap

def getSpectatorsMemMap(vars):
    memMap = {}
    if vars is None:
        return None
    for var in vars:
        memMap[var["name"]] = array('f', [0])
    return memMap

def prepareReader(xmlfilename, vars, varsMap, specs=None, specsMap=None):
    reader = TMVA.Reader()
    for var in vars:
        print("AddVar=" + var["name"])
        reader.AddVariable(var["name"], varsMap[var["name"]])
    if specs is not None:
        for spec in specs:
            print("AddSpec=" + spec["name"])
            reader.AddSpectator(spec["name"], specsMap[spec["name"]])
    reader.BookMVA("BDT", xmlfilename)
    return reader
