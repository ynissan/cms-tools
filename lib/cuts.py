#!/usr/bin/python

from ROOT import *

# load FWLite C++ libraries
# gSystem.Load("libFWCoreFWLite.so");
# gSystem.Load("libDataFormatsFWLite.so");
# FWLiteEnabler.enable()

# load FWlite python libraries
# from DataFormats.FWLite import Handle, Events
# import FWCore.ParameterSet.Config as cms

def applyCut(cut, event, eventParams, type, cutName):
	if cut.get(type) is None:
		return True
	if cut.get("once") and cut.get("result") is not None:
		return cut.get("result")
	cut["result"] = True
	for cutFunc in cut.get(type): #aod or ntuples
		cut["result"] = cutFunc(cut.get("params"), event, eventParams)
		if not cut["result"]:
			return False
	return cut["result"]
	
def resetCuts(cutsDefs):
	for cut in cutsDefs.keys():
		cutsDefs[cut]["result"] = None

def getCutsOrderMap(cutsOrder):
	cutsOrderMap = {}
	for i, cut in enumerate(cutsOrder):
		cutsOrderMap[cut] = i
	return cutsOrderMap
	
def createCutFlow(cut, cutsDef, cutsType):
	cutFlow = []
	if cutsDef.get(cut) is None:
		return cutFlow
	#This is the total one
	cutFlow.append(0)
	for cutFunc in cutsDef.get(cut).get(cutsType):
		cutFlow.append(0)
	return cutFlow

def appendCutFlow(cut, cutsDef, cutFlow, cutsType, event, params):
	# total
	cutFlow[0] += 1
	for i, cutFunc in enumerate(cutsDef.get(cut).get(cutsType)):
		if cutFunc(cutsDef.get(cut).get("params"), event, params):
			cutFlow[i+1] +=1
		else:
			return
	
def printCutFlow(cut, cutsDef, cutFlow, cutsType):
		total = cutFlow[0]
		print "Total " + str(total) + " 100(100)"
		for i, cutFunc in enumerate(cutsDef.get(cut).get(cutsType)):
			rel = 0.
			relTotal = 0.
			if cutFlow[i] > 0 and cutFlow[i + 1] > 0:
				relTotal = (float(cutFlow[i + 1]) / total) * 100
				rel = (float(cutFlow[i + 1]) / cutFlow[i]) * 100
			print cutFunc.__name__ + " " + str(cutFlow[i + 1]) + " " + str(rel)  + " " + str(relTotal)
			
	
# SPECIFIC CUTS

def MetCut(params, event, eventParams):
	met = eventParams["met"]
	return met >= params.get("met")

def Ht(params, event, eventParams):
	return eventParams["ht"] >= params.get("ht")
	
def Dilepton(params, event, eventParams):
	return eventParams["dilepton"]

def NoBTags(params, event, eventParams):
	return eventParams["BTags"] == 0
	
def DileptonInvMass(params, event, eventParams):
	return eventParams["dilepton"] and eventParams["invMass"] <= params["invMassMax"] and eventParams["invMass"] >= params["invMassMin"] and not (eventParams["invMass"] >= params["invMassRange"].get("min") and eventParams["invMass"] <= params["invMassRange"].get("max"))
	
def DileptonDeltaEta(params, event, eventParams):
	return eventParams["dilepton"] and eventParams["deltaEta"] <= params["deltaEta"]

def DileptonDeltaPhi(params, event, eventParams):
	return eventParams["dilepton"] and eventParams["deltaPhi"] <= params["deltaPhi"]
	
def DileptonDeltaR(params, event, eventParams):
	return eventParams["dilepton"] and eventParams["deltaR"] <= params["deltaR"]

def DileptonLepCorMET(params, event, eventParams):
	if not eventParams["dilepton"]:
		return False
	if eventParams["leptonsType"] == "E":
		return True
	
	ptmiss = TLorentzVector()
	ptmiss.SetPtEtaPhiE(event.MET,0,event.METPhi,event.MET)
	
	for lep in eventParams["leptons"]:
		lepPt = TLorentzVector(lep.Px(), lep.Py(), 0, lep.Pt())
		ptmiss += lepPt
	
	return ptmiss.Pt() >= params["lepCurMet"]
	

def MetDHt(params, event, eventParams):
	return eventParams["metDHt"] >= params["minMetDHt"] and eventParams["metDHt"] <= params["maxMetDHt"]

def Mt(params, event, eventParams):
	return eventParams["dilepton"] and eventParams["mt1"] <= params["mt"] and eventParams["mt2"] <= params["mt"]

def DileptonPt(params, event, eventParams):
	return eventParams["dilepton"] and eventParams["dileptonPt"] >= params["dileptonPt"]

def GT1J(params, event, eventParams):
	return eventParams["nj"] >= 1

def Eta(params, event, eventParams):
	etaOK = True
	for lep in eventParams["leptons"]:
		if abs(lep.Eta()) > params["eta" + eventParams["leptonsType"]]:
			etaOK = False
	return etaOK

def LeptonPt(params, event, eventParams):
	ptOk = True
	for lep in eventParams["leptons"]:
		if lep.Pt() > params["pt"]:
			ptOk = False
	return ptOk

def MtautauVeto(params, event, eventParams):
	return eventParams["mtautau"] < params["mTauTauVeto"][0] or eventParams["mtautau"] > params["mTauTauVeto"][1]

	
	