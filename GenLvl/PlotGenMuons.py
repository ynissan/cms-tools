#!/usr/bin/env python3.8
from ROOT import *
import sys
import os
from glob import glob
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/stops/lib/classes"))
from lib import utils
from lib import analysis_ntuples
from lib import analysis_tools
from lib import analysis_observables
import cppyy



#m_stop = 500, m_Chi_pm = 115, dm = 1.4
signal_files = [
glob("/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu_2016Fast/ntuple_sidecarv3/higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root"),
glob("/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu_2016Fast/ntuple_sidecarv3/higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root"),
glob("/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu_2016Fast/ntuple_sidecarv3/higgsino_Summer16_stopstop_500GeV_mChipm200GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root"),
glob("/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu_2016Fast/ntuple_sidecarv3/higgsino_Summer16_stopstop_500GeV_mChipm400GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root")
]
#signal_file = "/afs/desy.de/user/n/nissanuv/q_nfs/x1x2x1/signal/skim/sum/higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p4GeV_1.root"

chain = TChain("TreeMaker2/PreSelection")
#chain = TChain("tEvent")
for signal_file in signal_files:
	for file in signal_file:
		chain.Add(file)
		#break
	#break
	
		
number_of_entries = chain.GetEntries()
print("number_of_entries",number_of_entries)

histMuon = TH1F("MuonMultiplicity","MuonMultiplicity",10,0,10)
histAllMuons = TH1F("AllMuons","AllMuons",10,0,10)
histDeltaR = TH1F("min_DeltaR_muon_jet","min_DeltaR_muon_jet",50,0,5)
histDeltaRljet = TH1F("min_DeltaR_muon_l_jet","min_DeltaR_muon_l_jet",50,0,5)
histMuonsElectrons = TH1F("MuonsElectrons","MuonsElectrons",10,0,10)
histMuonParent = TH1F("MuonParents","MuonParents",12,0,12)
histMuonParentInsideJet = TH1F("MuonParentsInsideJet","MuonParentsInsideJet",12,0,12)
histMuonParentInsideBJet = TH1F("MuonParentsInsideBJet","MuonParentsInsideBJet",12,0,12)
histMuonTopPt = TH1F("PtMuonsFromTop","PtMuonsFromTop",90,0,30)

MesonList = [511, 411, 521, 431, 421, 443, 531, 221, 113, 541, 333, 223, 331, 100443, 553]
BaryonList = [5232,5122, 4122, 5132, 4132, 4232, 2212, 4332, 5332]
QuarkList = [1,2,3,4,5,6]
WParentList = []


def WhatsTheParent(idx,histMuonParent):
	MuonParentPdgId = chain.GenParticles_ParentId[idx]
	ParentFound = False
	if abs(MuonParentPdgId) == 6:				#top
		histMuonParent.AddBinContent(1)
		ParentFound = True
	if abs(MuonParentPdgId) == 1000023:			#second neutralino
		histMuonParent.AddBinContent(2)
		ParentFound = True
	if abs(MuonParentPdgId) == 1000024:			#first chargino
		histMuonParent.AddBinContent(3)
		ParentFound = True
	if abs(MuonParentPdgId) == 24:				#W-Boson/Top -> Pt
		histMuonParent.AddBinContent(4)
		AlreadyInList = False
		for WParent in WParentList:
			if WParent == chain.GenParticles_ParentId[chain.GenParticles_ParentIdx[idx]]:
				AlreadyInList = True
		if AlreadyInList == False:
			WParentList.append(chain.GenParticles_ParentId[chain.GenParticles_ParentIdx[idx]])
		ParentFound = True
	if abs(MuonParentPdgId) == 15:				#Tau
		histMuonParent.AddBinContent(5)
		ParentFound = True
	if abs(MuonParentPdgId) == 1000006:			#stop
		histMuonParent.AddBinContent(6)
		print("The stop is the parent")
		ParentFound = True
	for Meson in MesonList:
		if abs(MuonParentPdgId) == Meson:
			histMuonParent.AddBinContent(7) 
			ParentFound = True
	for Baryon in BaryonList:
		if abs(MuonParentPdgId) == Baryon:
			histMuonParent.AddBinContent(8)
			ParentFound = True
	if abs(MuonParentPdgId) == 22:				#gamma
		histMuonParent.AddBinContent(9)
		ParentFound = True
	if abs(MuonParentPdgId) == 21:				#gluino?
		histMuonParent.AddBinContent(10)
		ParentFound = True
	for Quark in QuarkList:
		if abs(MuonParentPdgId) == Quark:
			histMuonParent.AddBinContent(11)
			ParentFound = True
	if ParentFound == False:
		histMuonParent.AddBinContent(12)
		print(f"Different parent with PdgId {MuonParentPdgId}")

print("Starting Loop")
for ientry in range(number_of_entries):
	chain.GetEntry(ientry)
	if ientry % 1000 == 0:
		print("Processing " + str(ientry), "of", number_of_entries)
	partSize = len(chain.GenParticles_PdgId)
	MuonMultiplicity = 0
	allMuons = 0
	MuonsElectrons = 0
	for idx in range(partSize):
		if abs(chain.GenParticles_PdgId[idx]) == 13:
			allMuons += 1
		if abs(chain.GenParticles_PdgId[idx]) == 13 or abs(chain.GenParticles_PdgId[idx]) == 11:
			MuonsElectrons += 1
		if abs(chain.GenParticles_PdgId[idx]) == 13 and chain.GenParticles[idx].Pt() > 2 and chain.GenParticles[idx].Pt() < 30:
			MuonMultiplicity += 1
			WhatsTheParent(idx,histMuonParent)
			if abs(chain.GenParticles_ParentId[idx]) == 24 and abs(chain.GenParticles_ParentId[chain.GenParticles_ParentIdx[idx]]) == 6:
				histMuonTopPt.Fill(chain.GenParticles[idx].Pt())
			minDeltaR = None
			minDeltaRidx = None 
			minDeltaRljet = None
			ljet = None
			for jidx in range(len(chain.Jets)):
				if chain.Jets[jidx].Pt() > 30 and abs(chain.Jets[jidx].Eta()) < 2.4:
					DeltaR = chain.GenParticles[idx].DeltaR(chain.Jets[jidx])
					if minDeltaR is None or DeltaR < minDeltaR:
						minDeltaR = DeltaR
						minDeltaRidx = jidx
					if ljet is None or chain.Jets[jidx].Pt() > chain.Jets[ljet].Pt():
						ljet = jidx
						DeltaRljet = chain.GenParticles[idx].DeltaR(chain.Jets[ljet])
						if minDeltaRljet is None or DeltaRljet < minDeltaRljet:
							minDeltaRljet = DeltaRljet
			if minDeltaR is not None:
				histDeltaR.Fill(minDeltaR)
				histDeltaRljet.Fill(minDeltaRljet)
				if minDeltaR < 0.4:
					WhatsTheParent(idx, histMuonParentInsideJet)
					if chain.Jets_bJetTagDeepCSVBvsAll[jidx]is not None:
						if chain.Jets_bJetTagDeepCSVBvsAll[jidx] > 0.6324:
							WhatsTheParent(idx, histMuonParentInsideBJet)
					else:
						print("The muon is not inside a bjet")
				

	histMuon.Fill(MuonMultiplicity)
	histAllMuons.Fill(allMuons)
	histMuonsElectrons.Fill(MuonsElectrons)

canvas = TCanvas("canvas","GenMuonMultiplicity")
canvas.SetCanvasSize(800,600)
histMuon.SetLineWidth(2)
histMuon.Draw("hist")
histAllMuons.SetLineColor(kRed-4)
histAllMuons.SetLineWidth(2)
histAllMuons.Draw(" hist same")
histMuonsElectrons.Draw("hist same")
histMuonsElectrons.SetLineColor(kBlue)
histMuonsElectrons.SetLineWidth(2)
legend = TLegend(0.7,0.7,0.9,0.9)
legend.AddEntry(histAllMuons,"All Muons","f")
legend.AddEntry(histMuonsElectrons,"Muons+Electrons","f")
legend.AddEntry(histMuon,"selected Muons","f")
legend.Draw()

canvas.Update()
canvas.Print("GenMuonMultiplicity.pdf")


canvas2 = TCanvas("canvas2","minDeltaRMuonJet")
canvas2.SetCanvasSize(800,600)
histDeltaR.SetLineWidth(2)
histDeltaRljet.SetLineWidth(2)
histDeltaRljet.SetLineStyle(2)
histDeltaRljet.SetLineColor(kRed-4)
histDeltaR.Draw("hist4")
histDeltaRljet.Draw("hist4 same")
legend = TLegend(0.7,0.7,0.9,0.9)
legend.AddEntry(histDeltaR,"min \Delta R to Jet")
legend.AddEntry(histDeltaRljet,"min \Delta R to leading Jet")
legend.Draw()
canvas2.Update()
canvas2.Print("minDeltaRMuonJet.pdf")

canvas3 = TCanvas("canvas3","MuonParents")
canvas3.SetCanvasSize(800,600)
xAxis = histMuonParent.GetXaxis()
xAxis.SetBinLabel(1,"t")
xAxis.SetBinLabel(2,"\chi_{2}^{0}")
xAxis.SetBinLabel(3,"\chi_{1}^{\pm}")
xAxis.SetBinLabel(4,"W^{\pm}")
xAxis.SetBinLabel(5, " \\tau ")
xAxis.SetBinLabel(6, " \\tilde t ")
xAxis.SetBinLabel(7,"Mesons")
xAxis.SetBinLabel(8,"Baryons")
xAxis.SetBinLabel(9," \gamma ")
xAxis.SetBinLabel(10," g ")
xAxis.SetBinLabel(11," quarks ")
xAxis.SetBinLabel(12,"else")
histMuonParent.SetLineWidth(2)
histMuonParentInsideJet.SetLineWidth(2)
histMuonParentInsideJet.SetLineColor(kRed)
histMuonParentInsideBJet.SetLineWidth(2)
histMuonParentInsideBJet.SetLineColor(kGreen-3)
histMuonParentInsideBJet.SetLineStyle(2)
histMuonParent.Draw("hist2")
histMuonParentInsideJet.Draw("hist2 same")
histMuonParentInsideBJet.Draw("hist2 same")
legend2 = TLegend(0.7,0.7,0.9,0.9)
legend2.AddEntry(histMuonParent,"AllMuons","f")
legend2.AddEntry(histMuonParentInsideJet,"Muons inside Jets","f")
legend2.AddEntry(histMuonParentInsideBJet,"Muons inside BJets","f")
legend2.Draw()
canvas3.Update()
canvas3.Print("MuonParent.pdf")

canvas4 = TCanvas("canvas4", "PtMuonsFromTop")
canvas4.SetCanvasSize(800,600)
histMuonTopPt.SetLineStyle(1)
histMuonTopPt.Draw("hist3")
canvas4.Update()
canvas4.Print("PtMuonsFromTop.pdf")


print(f"List of W-parents: {WParentList}")









