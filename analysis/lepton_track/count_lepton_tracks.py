#!/usr/bin/env python

from ROOT import *
from glob import glob
from math import *
from sys import exit
from array import array
import argparse
import sys
import numpy as np
import os

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import histograms
from lib import utils
from lib import cuts
from lib import analysis_ntuples
from lib import analysis_tools

gROOT.SetBatch(1)

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Clones trees.')
parser.add_argument('-i', '--input_file', nargs=1, help='Input Filename', required=True)
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
parser.add_argument('-log', '--log', dest='log', help='Log Scale', action='store_true')
parser.add_argument('-mm', '--mm', dest='mm', help='Miss match only', action='store_true')
parser.add_argument('-rm', '--rm', dest='rm', help='Remove matched tracks', action='store_true')
args = parser.parse_args()

input_file = None
output_file = None
if args.input_file:
	input_file = args.input_file[0]
if args.output_file:
	output_file = args.output_file[0]
logScale = args.log
mm = args.mm
rm = args.rm
	
######## END OF CMDLINE ARGUMENTS ########

lepTypes = ["Zl", "NZl", "MM"]

if mm:
	lepTypes = ["Zl", "MM"]

def minRecDeltaR(l, c):
	min = None
	for v in [e for e in c.Electrons] + [m for m in c.Muons]:
		deltaR = abs(v.DeltaR(l))
		if min is None or deltaR < min:
			min = deltaR
	return min


class UOFlowTH1F(TH1F):
	epsilon = 0.0000000001
	def Fill(self, x):
		#print "Called UOFlowTH1F Fill"
		super(UOFlowTH1F, self).Fill(min(max(x,self.GetXaxis().GetBinLowEdge(1)+self.epsilon),self.GetXaxis().GetBinLowEdge(self.GetXaxis().GetNbins()+1)-self.epsilon))


def trackCuts(c, ti):
	if c.tracks_trackJetIso[ti] < 1:
		return False
	return True

def track_DeltaR_LJ(c, t, ti):
	return abs(t.DeltaR(c.LeadingJet))

def track_DeltaEta_LJ(c, t, ti):
	return abs(t.Eta() - c.LeadingJet.Eta())

def track_DeltaR_LL(c, t, ti):
	ll = leadingLepton(c)
	if ll is None:
		return 0
	return abs(t.DeltaR(ll))
	
def track_DeltaEta_LL(c, t, ti):
	ll = leadingLepton(c)
	if ll is None:
		return 0
	return abs(t.Eta()-ll.Eta())

def eta(c, ti):
	return abs(c.tracks[ti].Eta()) < 2.4

def pt(c, ti):
	return abs(c.tracks[ti].Pt()) > 2.5

def dz(c, ti):
	return abs(c.tracks_dzVtx[ti]) < 0.035

def dxy(c, ti):
	return abs(c.tracks_dxyVtx[ti]) < 0.05
	
def lepIso(c, ti):
	return c.tracks_trackLeptonIso[ti] < 0.02

def deltaEtaLL(c, ti):
	return track_DeltaEta_LL(c, c.tracks[ti], ti) < 1

def deltaEtaLJ(c, ti):
	return track_DeltaEta_LJ(c, c.tracks[ti], ti) < 3.8

def deltaRLJ(c, ti):
	return track_DeltaR_LJ(c, c.tracks[ti], ti) > 1.8

def deltaRLL(c, ti):
	return track_DeltaR_LL(c, c.tracks[ti], ti) < 1.1


def passedCut(cut, c, ti):
	for func in cut["funcs"]:
		if not func(c, ti):
			return False
	return True
	

def main():

	c = TChain('tEvent')
	print "Going to open the file"
	print input_file
	c.Add(input_file)

	nentries = c.GetEntries()
	print 'Analysing', nentries, "entries"
	
	histograms = {}
	memory = []
	
	objs = ["Gen", "Rec", "Track"]
	funcs = ["Pt", "Phi", "Eta"]
	lepTrackHists = ["LepTypePerRecoBin"]
	lepTrackHistsTitle = ["Lep Type Per Reco Bin"]
	lepTrackHistsMaxX = [5]
	lepTrackHistsBins = [5]
	
	trackHists = ["Track_DeltaR_LJ", "Track_DeltaEta_LJ", "Track_DeltaR_LL", "Track_DeltaEta_LL"]
	trackHistsFuncs = [track_DeltaR_LJ, track_DeltaEta_LJ, track_DeltaR_LL, track_DeltaEta_LL]
	trackHistsTitle = ["Delta R Track Leading Jet", "Delta Eta Track Leading Jet", "Delta R Track Leading Lepton", "Delta Eta Track Leading Lepton"]
	trackHistsMaxX = [5,5,5,5]
	trackHistsBins = [50,50,50,50]
	
	trackHistsNoType = ["Track_NumIso",  "NM_Track_NumIso"]
	trackHistsTitleNoType = ["Number of Isolated Tracks",  "Number of Non Matched Tracks"]
	trackHistsMaxXNoType = [20, 20]
	trackHistsBinsNoType = [20, 20]
	
	h2DHists = ["NM_Track_NumIso_Per_Reco", "NM_ZL_Track_NumIso_Per_Reco"]
	h2DHistsTitle = ["Number of Non Matched Tracks Per Reco Bin", "Number of Non Matched Zl Tracks Per Reco Bin"]
	h2DHistsXBins = [5,5]
	h2DHistsXMin = [0,0]
	h2DHistsXMax = [5,5]
	h2DHistsYBins = [5,5]
	h2DHistsYMin = [0,0]
	h2DHistsYMax = [5,5]
	
	tracksFuncs = ["tracks_trkRelIso", "tracks_chi2perNdof", "tracks_dxyVtx", "tracks_dzVtx", "tracks_trackQualityHighPurity", "tracks_trackJetIso", "tracks_trackLeptonIso"]
	maxX = [15, 3.5, 3.5]
	tracksMaxX = [0.1, 10, 0.1, 0.1, 2, 1, 0.2]

	binNum = 50
	
	cuts = [{"name":"", "title": "No Cuts"},			        
		{"name":"Eta_deltaEtaLL", "title": "Eta < 2.6, deltaEtaLL < 1", "funcs":[eta, deltaEtaLL]},
		{"name":"Eta_deltaEtaLL_deltaEtaLJ", "title": "Eta < 2.6, deltaEtaLL < 1, deltaEtaLJ < 3.8", "funcs":[eta, deltaEtaLL, deltaEtaLJ]},
		{"name":"Pt_Eta_dxy_dz", "title": "Eta < 2.6, Pt > 2.5, dxy < 0.05, dz < 0.06", "funcs":[eta, pt, dxy, dz]},
		{"name":"Pt_Eta_dxy_dz_lepIso", "title": "Eta < 2.6, Pt > 2.5, dxy < 0.05, dz < 0.06, lepIso < 0.02", "funcs":[eta, pt, dxy, dz, lepIso]},
		{"name":"Pt_Eta_dxy_dz_deltaEtaLL", "title": "Eta < 2.6, Pt > 2.5, dxy < 0.05, dz < 0.06, deltaEtaLL < 1", "funcs":[eta, pt, dxy, dz, deltaEtaLL]},
		{"name":"Pt_Eta_dxy_dz_deltaEtaLL_deltaEtaLJ", "title": "Eta < 2.6, Pt > 2.5, dxy < 0.05, dz < 0.06, deltaEtaLL < 1, deltaEtaLJ < 3.8", "funcs":[eta, pt, dxy, dz, deltaEtaLL, deltaEtaLJ]},
		{"name":"Pt_Eta_dxy_dz_deltaEtaLL_deltaRLJ", "title": "Eta < 2.6, Pt > 2.5, dxy < 0.05, dz < 0.06, deltaEtaLL < 1, deltaRLJ > 1.8", "funcs":[eta, pt, dxy, dz, deltaEtaLL, deltaRLJ]},
		{"name":"Pt_Eta_dxy_dz_deltaEtaLL_deltaRLJ_deltaRLL", "title": "Eta < 2.6, Pt > 2.5, dxy < 0.05, dz < 0.06, deltaEtaLL < 1, deltaRLJ > 1.8, deltaRLL < 1.1", "funcs":[eta, pt, dxy, dz, deltaEtaLL, deltaRLJ, deltaRLL]}]
		
	
	for obj in objs:
		for lepType in lepTypes:
			if not mm and obj == "Gen" and lepType == "MM":
				continue
			for h, hists in enumerate([funcs,lepTrackHists]):
				if h == 1 and obj == "Gen":
					continue
				for i, func in enumerate(hists):
					name = obj + "_" + lepType + "_" + func
					if obj == "Track":
						for cut in cuts:
							tname = name + "_" + cut["name"]
							if h == 1:
								histograms[tname] = UOFlowTH1F(tname, lepTrackHistsTitle[i] + " - " + obj, lepTrackHistsBins[i], 0, lepTrackHistsMaxX[i])
							else:
								histograms[tname] = UOFlowTH1F(tname, obj + " " + func, binNum, 0, maxX[i])
					else:
						if h == 1:
							histograms[name] = UOFlowTH1F(name, lepTrackHistsTitle[i] + " - " + obj, lepTrackHistsBins[i], 0, lepTrackHistsMaxX[i])
						else:
							histograms[name] = UOFlowTH1F(name, obj + " " + func, binNum, 0, maxX[i])
										
	for i, trackHist in enumerate(trackHists):
		for lepType in lepTypes:
			for cut in cuts:
				tname = trackHist + "_" + lepType + "_" + cut["name"]
				histograms[tname] = UOFlowTH1F(tname, trackHistsTitle[i], trackHistsBins[i], 0, trackHistsMaxX[i])
	
	for i, trackHist in enumerate(trackHistsNoType):
		for cut in cuts:
			tname = trackHist + "_" + cut["name"]
			histograms[tname] = UOFlowTH1F(tname, trackHistsTitleNoType[i], trackHistsBinsNoType[i], 0, trackHistsMaxXNoType[i])		
	
				
	histograms["Lepton_minDealZ"] = UOFlowTH1F("Lepton_minDealZ", "Lepton Min Delta Z", binNum, 0, 0.02)
	histograms["Reco_Num"] = UOFlowTH1F("Reco_Num", "Number of Reco Leptons", 5, 0, 5)
	
	histograms["Track_minDealZ"] = UOFlowTH1F("Track_minDealZ", "Track Min Delta Z", binNum, 0, 0.2)
	histograms["Track_RelIso"] = UOFlowTH1F("Track_RelIso", "Track RelIso for Delta Z < 0.1", binNum, 0, 0.01)
	
	for i, hist in enumerate(h2DHists):
		for cut in cuts:
			name = hist + "_" + cut["name"]
			histograms[name] = TH2I(name, h2DHistsTitle[i], h2DHistsXBins[i], h2DHistsXMin[i], h2DHistsXMax[i], h2DHistsYBins[i], h2DHistsYMin[i], h2DHistsYMax[i])
	
	for i, func in enumerate(tracksFuncs):
		for lepType in lepTypes:
			for cut in cuts:
				name = func + "_" + lepType + "_" + cut["name"]
				if func == "tracks_trackQualityHighPurity":
					histograms[name] = UOFlowTH1F(name, func, 2, 0, tracksMaxX[i])
				else:
					histograms[name] = UOFlowTH1F(name, func, binNum, 0, tracksMaxX[i])
	
	for k, h in histograms.items():
		h.Sumw2()
		h.SetStats(0)
		h.SetMinimum(0.001)
	
	notCorrect = 0
	for ientry in range(nentries):
		if ientry % 5000 == 0:
			print "Processing " + str(ientry)
		c.GetEntry(ientry)
		rightProcess = analysis_ntuples.isX1X2X1Process(c)
		if not rightProcess:
			print "No"
			notCorrect += 1
			continue
		
		recoNum = c.Electrons.size() + c.Muons.size()
		if recoNum != 1:
			continue
		
		genZL, genNonZL = analysis_ntuples.classifyGenZLeptons(c)
		if genZL is None:
			continue
		for li in genZL:
			for func in funcs:
				histograms["Gen_Zl_" + func].Fill(abs(getattr(c.GenParticles[li], func)()))
		for li in genNonZL:
			for func in funcs:
				if mm:
					histograms["Gen_MM_" + func].Fill(abs(getattr(c.GenParticles[li], func)()))
				else:
					histograms["Gen_NZl_" + func].Fill(abs(getattr(c.GenParticles[li], func)()))
		histograms["Reco_Num"].Fill(recoNum)
		
		
		for lepVal in ["Electrons", -11], ["Muons", -13]:
			lepFlavour = lepVal[0]
			lepCharge = lepVal[1]
			leps = getattr(c, lepFlavour)
			for li in range(leps.size()):
				l = leps[li]
				minZ, minCanZ = analysis_ntuples.minDeltaRGenParticles(l, genZL, c)
				minNZ, minCanNZ = analysis_ntuples.minDeltaRGenParticles(l, genNonZL, c)
				min = 0
				if minNZ is None or minZ < minNZ:
					min = minZ
				else:
					min = minNZ
				histograms["Lepton_minDealZ"].Fill(min)
				if min > 0.01:
					#print "No Match"
					for h, hists in enumerate([funcs,lepTrackHists]):
						for func in hists:
							if h == 0:
								histograms["Rec_MM_" + func].Fill(abs(getattr(l, func)()))
							elif h == 1:
								histograms["Rec_MM_" + func].Fill(recoNum)
					continue
				name = ""
				if minNZ is None or minZ < minNZ:
					#print "E Z min: " + str(minZ)
					if c.GenParticles_PdgId[minCanZ] == lepCharge * getattr(c, lepFlavour + "_charge")[li]:
						name = "Rec_Zl_"
					else:
						name = "Rec_MM_"
				else:
					if c.GenParticles_PdgId[minCanNZ] == lepCharge * getattr(c, lepFlavour + "_charge")[li]:
						if mm:
							name = "Rec_MM_"
						else:
							name = "Rec_NZl_"
					else:
						name = "Rec_MM_"
				for h, hists in enumerate([funcs,lepTrackHists]):
					for func in hists:
						if h == 0:
							histograms[name + func].Fill(abs(getattr(l, func)()))
						elif h == 1:
							histograms[name + func].Fill(recoNum)
		
		numIsoTracks = [0] * len(cuts)
		numMMIsoTracks = [0] * len(cuts)
		numMMZlIsoTracks = [0] * len(cuts)
		for ti in range(c.tracks.size()):
			if c.tracks_trkRelIso[ti] > 0.1:
				continue 
			#continue
			t = c.tracks[ti]
			minRecR = minRecDeltaR(t, c)
			if rm and minRecR < 0.1:
				continue
			
			#if abs(t.Eta()) > 0.1:
			#	continue
			minZ, minCanZ = analysis_ntuples.minDeltaRGenParticles(t, genZL, c)
			minNZ, minCanNZ = analysis_ntuples.minDeltaRGenParticles(t, genNonZL, c)
			
			min = 0
			if minNZ is None or minZ < minNZ:
				min = minZ
			else:
				min = minNZ
			#print "*********"
			#print "Min=" + str(min)
			histograms["Track_minDealZ"].Fill(min)
			if min <= 0.1:
				histograms["Track_RelIso"].Fill(c.tracks_trkRelIso[ti])

			result = ""
			
			if min > 0.1:
				result = "MM"
			elif minNZ is None or minZ < minNZ:
				if c.tracks_charge[ti] * c.GenParticles_PdgId[minCanZ] < 0:
					result = "Zl"
				else:
					result = "MM"
			else:
				if c.tracks_charge[ti] * c.GenParticles_PdgId[minCanNZ] < 0:
					if mm:
						result = "MM"
					else:
						result = "NZl"
				else:
					result = "MM"
			#if result == "Zl":
			#	print "min=", min, " iso:", c.tracks_trkRelIso[ti]

			for i, cut in enumerate(cuts):
				if len(cut["name"]) > 0:
					#print "Checking cut " + cut["name"]
					if not passedCut(cut, c, ti):
						#print "not passed"
						continue
				
				numIsoTracks[i] += 1
				
				if minRecR is None or minRecR > 0.1:
					numMMIsoTracks[i] += 1
					if result == "Zl":
						numMMZlIsoTracks[i] +=1
				
				for h, hists in enumerate([funcs,lepTrackHists]):
					for func in hists:
						name = "Track_" + result + "_" + func + "_" + cut["name"]
						if h == 0:
							histograms[name].Fill(abs(getattr(t, func)()))
						elif h == 1:
							histograms[name].Fill(recoNum)
				for i, trackHist in enumerate(trackHists):
					name = trackHist + "_" + result + "_" + cut["name"]
					if trackHistsFuncs[i] is not None:
						histograms[name].Fill(trackHistsFuncs[i](c, t, ti))
				for func in tracksFuncs:
					name = func + "_" + result + "_" + cut["name"]
					if func == "tracks_trackQualityHighPurity":
						val = getattr(c, func)[ti]
						if val:
							val = 1
						else:
							val = 0
						histograms[name].Fill(val)
					else:
						histograms[name].Fill(abs(getattr(c, func)[ti]))
		for i, cut in enumerate(cuts):
			histograms["Track_NumIso_" + cut["name"]].Fill(numIsoTracks[i])
			histograms["NM_Track_NumIso_" + cut["name"]].Fill(numMMIsoTracks[i])
			histograms["NM_Track_NumIso_Per_Reco_" + cut["name"]].Fill(recoNum, numMMIsoTracks[i])
			if numMMIsoTracks[i] == numMMZlIsoTracks[i]:
				histograms["NM_ZL_Track_NumIso_Per_Reco_" + cut["name"]].Fill(recoNum, numMMZlIsoTracks[i])
	
	print "Not Correct Procs=" + str(notCorrect)
	
	hNM = histograms["NM_Track_NumIso_Per_Reco_" + cuts[-1]["name"]]
	xNMAxis = hNM.GetXaxis()
	yNMAxis = hNM.GetYaxis()
	binNMX = xNMAxis.FindBin(1)
	binNMY = yNMAxis.FindBin(1)
	
	hZL = histograms["NM_ZL_Track_NumIso_Per_Reco_" + cuts[-1]["name"]]
	xZLAxis = hZL.GetXaxis()
	yZLAxis = hZL.GetYaxis()
	binZLX = xZLAxis.FindBin(1)
	binZLY = yZLAxis.FindBin(1)
	
	print "Number of 1,1 bins NM_Track_NumIso_Per_Reco=" + str(hNM.GetBinContent(binNMX,binNMY) ) + " NM_ZL_Track_NumIso_Per_Reco=" + str(hZL.GetBinContent(binZLX,binZLY)) 
	
	c1 = TCanvas("c1")

	titlePad = TPad("titlePad", "",0.0,0.93,1.0,1.0)
	histPad = TPad("histPad", "",0.0,0.0,1.0,0.93)

	titlePad.Draw()
	t = TPaveText(0.0,0.93,1.0,1.0,"NB")
	t.SetFillStyle(0)
	t.SetLineColor(0)
	t.SetTextFont(40);
	t.Draw()

	histPad.Draw()
	histPad.Divide(3,2)
	OUTPUT_FILE = output_file or "./count_lepton_tracks.pdf"
	c1.Print(OUTPUT_FILE + "[");
	
	for cut in cuts:
	
		t.Clear()
		t.AddText(cut["title"])
		t.Draw();
		titlePad.Update()
		pId = 1
		needToDraw = False
		drawSame = False
		for h, hists in enumerate([funcs,lepTrackHists]):
			for func in hists:
				for obj in objs:
					#print "***"
					#print cut["name"], obj, func
					if len(cut["name"]) > 0 and obj != "Track":
						#print "Breaking"
						continue
					if h == 1 and obj == "Gen":
						continue
					maxY = 0
					for lepType in lepTypes:
						if obj == "Gen" and lepType == "MM":
							continue
						name = obj + "_" + lepType + "_" + func
						if obj == "Track":
							name += "_" + cut["name"]
						h =  histograms[name]
						maxY = max(maxY, h.GetMaximum())
		
					drawSame = False
					pad = histPad.cd(pId)
					needToDraw = True
					legend = TLegend(.69,.7,.85,.89)
					memory.append(legend)
					cP = 0
					for lepType in lepTypes:
						if obj == "Gen" and lepType == "MM":
							continue
						name = obj + "_" + lepType + "_" + func
						if obj == "Track":
							name += "_" + cut["name"]
						print name
						h =  histograms[name]
						utils.formatHist(h, utils.colorPalette[cP])
						cP += 1
						h.SetMaximum(maxY)
						legend.AddEntry(h, lepType, 'F')
						if drawSame:
							h.Draw("HIST SAME")
						else:
							drawSame = True
							#utils.setLabels(h, histDef)
							h.Draw("HIST")
			
					legend.Draw("SAME")
					if logScale:
						pad.SetLogy()
					c1.Update()		
					pId += 1
		
					if pId > 6:
						pId = 1
						c1.Print(OUTPUT_FILE);
						needToDraw = False;
	
		if len(cut["name"]) == 0:
			for name in "Lepton_minDealZ", "Track_minDealZ", "Track_RelIso", "Reco_Num":
				needToDraw = True
				pad = histPad.cd(pId)
				h =  histograms[name]
				utils.formatHist(h, utils.colorPalette[cP])
				h.Draw("HIST")
				if logScale:
					pad.SetLogy()
				c1.Update()		
				pId += 1
				if pId > 6:
					pId = 1
					c1.Print(OUTPUT_FILE);
					needToDraw = False
					
		for i, trackHist in enumerate(trackHistsNoType):
				name = trackHist + "_" + cut["name"]
				needToDraw = True
				pad = histPad.cd(pId)
				h =  histograms[name]
				utils.formatHist(h, utils.colorPalette[cP])
				h.Draw("HIST")
				if logScale:
					pad.SetLogy()
				c1.Update()		
				pId += 1
				if pId > 6:
					pId = 1
					c1.Print(OUTPUT_FILE);
					needToDraw = False
		
		for hist in h2DHists:
			name = hist + "_" + cut["name"]
			needToDraw = True
			pad = histPad.cd(pId)
			h =  histograms[name]
			h.Draw("TEXT")
			c1.Update()		
			pId += 1
			if pId > 6:
				pId = 1
				c1.Print(OUTPUT_FILE);
				needToDraw = False
	
		for func in tracksFuncs + trackHists:
			maxY = 0
			for lepType in lepTypes:
				name = func + "_" + lepType + "_" + cut["name"]
				h =  histograms[name]
				maxY = max(maxY, h.GetMaximum())
			drawSame = False
			pad = histPad.cd(pId)
			needToDraw = True
			legend = TLegend(.69,.7,.80,.89)
			memory.append(legend)
			cP = 0
			for lepType in lepTypes:
				name = func + "_" + lepType + "_" + cut["name"]
				print name
				h =  histograms[name]
				utils.formatHist(h, utils.colorPalette[cP])
				cP += 1
				h.SetMaximum(maxY)
				legend.AddEntry(h, lepType, 'F')
				if drawSame:
					h.Draw("HIST SAME")
				else:
					drawSame = True
					#utils.setLabels(h, histDef)
					h.Draw("HIST")
		
			legend.Draw("SAME")
			if logScale:
				pad.SetLogy()
			c1.Update()		
			pId += 1
	
			if pId > 6:
				pId = 1
				c1.Print(OUTPUT_FILE);
				needToDraw = False;
		
			
		if needToDraw:
			for id in range(pId, 7):
				print "Clearing pad " + str(id)
				pad = histPad.cd(id)
				pad.Clear()
			c1.Print(OUTPUT_FILE);
	
	c1.Print(OUTPUT_FILE+"]");
		
main()	
	