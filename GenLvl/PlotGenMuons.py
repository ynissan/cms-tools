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
import argparse 

parser = argparse.ArgumentParser(description='Plot Lepton properties')
parser.add_argument('-b', '--breakk', help='break after one file' , action='store_true' ,required=False)
parser.add_argument('-n', '--noplots', help ='no plots are created' , action = 'store_true', required = False)
args = parser.parse_args()

#m_stop = 500, m_Chi_pm = 115, dm = 1.4
signal_files = [
glob("/afs/desy.de/user/d/diepholq/nfs/x1x2x1/signal/skim/sum/higgsino_Summer16_stopstop_*GeV_mChipm*GeV_dm*GeV_1.root")
# glob("/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu_2016Fast/ntuple_sidecarv3/higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm0p6GeV_pu35_part*of25_RA2AnalysisTree.root"),
# glob("/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu_2016Fast/ntuple_sidecarv3/higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p0GeV_pu35_part*of25_RA2AnalysisTree.root"),
# glob("/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu_2016Fast/ntuple_sidecarv3/higgsino_Summer16_stopstop_500GeV_mChipm200GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root"),
# glob("/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu_2016Fast/ntuple_sidecarv3/higgsino_Summer16_stopstop_500GeV_mChipm400GeV_dm1p4GeV_pu35_part*of25_RA2AnalysisTree.root")
]
signal_file = "/afs/desy.de/user/n/nissanuv/q_nfs/x1x2x1/signal/skim/sum/higgsino_Summer16_stopstop_500GeV_mChipm115GeV_dm1p4GeV_1.root"

if args.breakk:
	#chain = TChain("TreeMaker2/PreSelection")
	chain = TChain("tEvent")
	for signal_file in signal_files:
		for file in signal_file:
			chain.Add(file)
			break
		break
else:
	#chain = TChain("TreeMaker2/PreSelection")
	chain = TChain("tEvent")
	for signal_file in signal_files:
		for file in signal_file:
			chain.Add(file)
	
	
	
		
number_of_entries = chain.GetEntries()
print("number_of_entries",number_of_entries)


#Definition of histograms-----------------------------------------------------------------

histograms = {

}

def create_hist(Name,axisargs):
	bins = axisargs[0]
	lowest = axisargs[1]
	highest = axisargs[2]
	Name = "hist" + Name
	hist = TH1F(Name,Name,bins,lowest,highest)
	histograms.update({Name: hist})

arglist = ["Muon",[10,0,10],"RecoMuonMultiplicity",[10,0,10],"RecoMuonMultiplicityIso",[10,0,10],"GenfromStop",[10,0,10],"RecofromStop",[10,0,10],"RecofromStopIso",[10,0,10],"DeltaR",[50,0,5],"DeltaRljet",[50,0,5],"MuonParent",[12,0,12],"MuonParentInsideJet",[12,0,12],
"MuonParentInsideBJet",[12,0,12],"MuonStopPt",[60,0,30],"RecoMuonStopPt",[60,0,30],"RecoMuonStopPtIso",[60,0,30],"MuonTopPt",[60,0,30],"RecoMuonTopPt",[60,0,30],"RecoMuonTopPtIso",[60,0,30]]

i = 0
while i < len(arglist):
	create_hist(arglist[i],arglist[i+1])
	i+=2
# histMuon = TH1F("GenMuonMultiplicity"," ; \\mu - multiplicity ; ",10,0,10) #with pt bounds
# histRecoMuonMultiplicity= TH1F("RecoMuonMultiplicity","RecoMuonMultiplicity",10,0,10) #with pt bounds
# histRecoMuonMultiplicityIso= TH1F("RecoMuonMultiplicityIso","RecoMuonMultiplicityIso",10,0,10) #with pt bounds
# # histGenMuons = TH1F("GenMuons","GenMuons",10,0,10) #all muons
# # histRecoMuons = TH1F("RecoMuons","RecoMuons",10,0,10) #all corresponding reco muons
# histDeltaR = TH1F("min_DeltaR_muon_jet"," ; \Delta R ; ",50,0,5)
# histDeltaRljet = TH1F("min_DeltaR_muon_l_jet","min_DeltaR_muon_l_jet",50,0,5)
# # histGenElectrons = TH1F("GenElectrons","GenElectrons",10,0,10) #all electrons
# # histRecoElectrons = TH1F("RecoElectrons","RecoElectrons",10,0,10) #all reco electrons
# histMuonParent = TH1F("MuonParents"," ; Parent ; ",12,0,12)
# histMuonParentInsideJet = TH1F("MuonParentsInsideJet"," ; Parent ; ",12,0,12)
# histMuonParentInsideBJet = TH1F("MuonParentsInsideBJet"," ; Parent ; ",12,0,12)
# histMuonStopPt = TH1F("PtMuonsfromStop"," ; p_{T} ; ",60,0,30)
# histRecoMuonStopPt = TH1F("RecoMuonStopPt","RecoMuonStopPt",60,0,30)
# histRecoMuonStopPtIso = TH1F("RecoMuonStopPtIso","RecoMuonStopPtIso",60,0,30)
# # histMuonPt = TH1F("PtMuons"," ; p_{T} ; ",60,0,30)
# # histRecoMuonPt = TH1F("PtRecoMuons","PtRecoMuons",60,0,30)
# # histRecoMuonPtIso = TH1F("PtRecoMuonsIso","PtRecoMuonsIso",60,0,30)
# histMuonTopPt = TH1F("PtMuonsFromTop"," ; p_{T} ; ",60,0,30)
# histRecoMuonTopPt = TH1F("PtRecoMuonsFromTop","PtRecoMuonsFromTop",60,0,30)
# histRecoMuonTopPtIso = TH1F("PtRecoMuonsFromTopIso","PtRecoMuonsFromTopIso",60,0,30)

MesonList = [511, 411, 521, 431, 421, 443, 531, 221, 113, 541, 333, 223, 331, 100443, 553]
BaryonList = [5232,5122, 4122, 5132, 4132, 4232, 2212, 4332, 5332]
QuarkList = [1,2,3,4,5,6]
WParentList = []


#Definiton of functions-------------------------------------------------------------------


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



def minDeltaLepLeps(lep, leps):
    min, minCan = None, None
    for i, l in enumerate(leps):
        deltaR = abs(lep.DeltaR(l))
        if min is None or deltaR < min:
            min = deltaR
            minCan = i
    return min, minCan


file = open("efficiencies.txt","w")
file.write(" ")
file.close()

def calculate_efficiency(hist1,hist2):
	eff = hist1.Integral()/hist2.Integral()
	file = open("efficiencies.txt","a")
	efficiency_text = f"eff {str(hist1).split(' ')[1]}_{str(hist2).split(' ')[1]}: \n {eff} \n ---------- \n"
	file.write(efficiency_text)
	file.close()


	
#main-------------------------------------------------------------------------------------

PtUpper = [15,11,7]
jetIsoStr = "Muons_passCorrJetIso15Dr0.4"
def main(PtThreshold):
	print("Starting Loop")
	for ientry in range(number_of_entries):
		chain.GetEntry(ientry)
		if ientry % 1000 == 0:
			print("Processing " + str(ientry), "of", number_of_entries)
		partSize = len(chain.GenParticles_PdgId)
		GenMuonMultiplicity = 0
		GenMuons = 0
		RecoMuons = 0
		GenElectrons = 0
		RecoElectrons = 0
		RecoMuonMultiplicity = 0
		RecoMuonMultiplicityIso = 0
		GenfromStopMultiplicity = 0
		RecofromStopMultiplicityIso = 0
		isobranch = getattr(chain,jetIsoStr)
		if chain.MHT < 200:
			continue
		if chain.MET < 140:
			continue
		if chain.MinDeltaPhiMhtJets < 0.4:
			continue
		for idx in range(partSize):
			counter = 0
			# if abs(chain.GenParticles_PdgId[idx]) == 13:
	# 			mindR, minCan = minDeltaLepLeps(chain.GenParticles[idx], chain.Muons)
	# 			if mindR < 0.01:
	# 				if chain.Muons_passCorrJetIso15Dr0.4[minCan]:
	# 					RecoMuons += 1
	# 			GenMuons += 1
	# 		if abs(chain.GenParticles_PdgId[idx]) == 11:
	# 			mindR, minCan = minDeltaLepLeps(chain.GenParticles[idx], chain.Electrons)
	# 			if mindR < 0.01:
	# 				if chain.Electrons_passCorrJetIso15Dr0.4[minCan]:
	# 					RecoElectrons += 1
	# 			GenElectrons += 1
			if abs(chain.GenParticles_PdgId[idx]) == 13 and chain.GenParticles[idx].Pt() > 2 and chain.GenParticles[idx].Pt() < PtThreshold:
				GenMuonMultiplicity += 1
				mindR, minCan = minDeltaLepLeps(chain.GenParticles[idx], chain.Muons)
				MuonMatchIso = False
				antiMuonMatchIso = False
				MuonMatch = False
				if mindR is not None:
					if mindR < 0.01:
						RecoMuonMultiplicity += 1
						MuonMatch = True
						if isobranch[minCan] == True: 
							RecoMuonMultiplicityIso += 1 
							MuonMatchIso = True
				WhatsTheParent(idx,histograms["histMuonParent"])
# 				if MuonMatch:
# 					histRecoMuonPt.Fill(chain.Muons[minCan].Pt())
# 				if MuonMatchIso:
# 					histRecoMuonPtIso.Fill(chain.Muons[minCan].Pt())
				if abs(chain.GenParticles_ParentId[idx]) == 24 and abs(chain.GenParticles_ParentId[chain.GenParticles_ParentIdx[idx]]) == 6:
					histograms["histMuonTopPt"].Fill(chain.GenParticles[idx].Pt())
					if MuonMatch:
						histograms["histRecoMuonTopPt"].Fill(chain.Muons[minCan].Pt())
					if MuonMatchIso:
						histograms["histRecoMuonTopPtIso"].Fill(chain.Muons[minCan].Pt())
					
				
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
								counter += 1
								if counter > 1:
									print("DeltaR corrected ")
				if minDeltaR is not None:
					histograms["histDeltaR"].Fill(minDeltaR)
					histograms["histDeltaRljet"].Fill(minDeltaRljet)
					if minDeltaR < 0.4:
						WhatsTheParent(idx, histograms["histMuonParentInsideJet"])
						if chain.Jets_bJetTagDeepCSVBvsAll[jidx]is not None:
							if chain.Jets_bJetTagDeepCSVBvsAll[jidx] > 0.6324:
								WhatsTheParent(idx, histograms["histMuonParentInsideBJet"])
						else:
							print("The muon is not inside a bjet")
				if chain.GenParticles_PdgId[idx] == 13 and chain.GenParticles_ParentId[idx] == 1000023 and chain.GenParticles_ParentId[chain.GenParticles_ParentIdx[idx]] == 1000006:
					MuonIdx = idx
					Chi02idx = chain.GenParticles_ParentIdx[idx]
					for idx2 in range(partSize):
						if chain.GenParticles_PdgId[idx2] == -13 and chain.GenParticles_ParentIdx[idx2] == Chi02idx and chain.GenParticles[idx2].Pt() > 2 and chain.GenParticles[idx2].Pt() < PtThreshold:
							mindRAnti, minCanAnti = minDeltaLepLeps(chain.GenParticles[idx2], chain.Muons)
							if mindRAnti is not None:
								if mindRAnti < 0.01:
									histograms["histRecoMuonStopPt"].Fill(chain.Muons[minCanAnti].Pt())
									histograms["histRecoMuonStopPt"].Fill(chain.Muons[minCan].Pt())
									if isobranch[minCanAnti]:
										antiMuonMatchIso = True
										histograms["histRecoMuonStopPtIso"].Fill(chain.Muons[minCanAnti].Pt())
										histograms["histRecoMuonStopPtIso"].Fill(chain.Muons[minCan].Pt())
							GenfromStopMultiplicity += 2
							if MuonMatchIso == True and antiMuonMatchIso == True:
								RecofromStopMultiplicityIso +=2
							histograms["histMuonStopPt"].Fill(chain.GenParticles[MuonIdx].Pt())
							histograms["histMuonStopPt"].Fill(chain.GenParticles[idx2].Pt())
		histograms["histRecofromStopIso"].Fill(RecofromStopMultiplicityIso)
		histograms["histGenfromStop"].Fill(GenfromStopMultiplicity)
		histograms["histMuon"].Fill(GenMuonMultiplicity)
		histograms["histRecoMuonMultiplicity"].Fill(RecoMuonMultiplicity)
		histograms["histRecoMuonMultiplicityIso"].Fill(RecoMuonMultiplicityIso)
		# histGenMuons.Fill(GenMuons)
		# histRecoMuons.Fill(RecoMuons)
		# histGenElectrons.Fill(GenElectrons)
		# histRecoElectrons.Fill(RecoElectrons)

	#efficiencies-----------------------------------

	# eff_RecoGen_Multiplicity = calculate_efficiency(histRecoMuonMultiplicity,histMuon)
# 
# 	eff_RecoIsoGen_Multiplicity = calculate_efficiency(histRecoMuonMultiplicityIso,histMuon)
# 
# 	eff_RecoIsoReco_Multiplicity = calculate_efficiency(histRecoMuonMultiplicityIso,histRecoMuonMultiplicity)
# 
# 	eff_RecoIsoGen_TopPt = calculate_efficiency(histRecoMuonTopPtIso,histMuonTopPt)
# 
# 	eff_RecoIsoGen_StopPt = calculate_efficiency(histRecoMuonStopPtIso,histMuonStopPt)
# 
# 	eff_RecoIsoReco_StopPt = calculate_efficiency(histRecoMuonStopPtIso,histRecoMuonStopPt)
# 
# 	eff_RecoIsoReco_TopPt = calculate_efficiency(histRecoMuonTopPtIso, histRecoMuonTopPt)
# 	
# 	eff_RecoGen_MuonPt = calculate_efficiency(histRecoMuonPt, histMuonPt)
# 	
# 	eff_RecoIsoReco_MuonPt = calculate_efficiency(histRecoMuonPtIso, histRecoMuonPt)

	if args.noplots:
		exit(0)
		
# for pT_Value in PtUpper:
# 	main(pT_Value)
main(PtUpper[0])

#plotting---------------------------------------------------------------------------------
def plot_hist(key,linestyle,linewidth,linecolor,same,legendentry,pdf,canvasglobal,legendglobal):
	key = str(key)
	h1 = histograms[key]
	h1.SetLineStyle(linestyle)
	h1.SetLineWidth(linewidth)
	if linecolor == "kBlue-4":
		h1.SetLineColor(kBlue-4)
	if linecolor == "kRed-4":
		h1.SetLineColor(kRed-4)
	if same == False:
		canvas = TCanvas("canvas",key)
		canvas.SetCanvasSize(800,600)
		legend = TLegend(0.7,0.7,0.9,0.9)
		legend.AddEntry(key,legendentry,"f")
		h1.Draw("hist")
		return canvas,legend
	if same:
		h1.Draw("hist same")
		legend = legendglobal
		legend.AddEntry(key,legendentry,"f")
		canvas = canvasglobal
	legend.Draw()
	canvas.Update()
	if pdf:
		Titel = key+ ".pdf"
		canvas.Print(Titel)
		
histograms["histMuon"].SetMaximum(max(histograms["histMuon"].GetMaximum(),histograms["histRecoMuonMultiplicity"].GetMaximum(),histograms["histRecoMuonMultiplicityIso"].GetMaximum(),histograms["histGenfromStop"].GetMaximum(),histograms["histRecofromStopIso"].GetMaximum())+500)
canvasMuon,legendMuon = plot_hist("histMuon",1,2,"default",False,"GenMuons",False,None,None)
plot_hist("histRecoMuonMultiplicity",3,3,"default",True,"Reco",False,canvasMuon,legendMuon)
plot_hist("histRecoMuonMultiplicityIso",2,2,"default",True,"Reco Iso",False,canvasMuon,legendMuon)
plot_hist("histGenfromStop",1,2,"kRed-4",True, "Gen from \\tilde t", False, canvasMuon,legendMuon)
plot_hist("histRecofromStopIso",2,3,"kRed-4",True, "Reco Iso from \\tilde t", True, canvasMuon,legendMuon)

#plot_hist(key,linestyle,linewidth,linecolor,same,legendentry,pdf,canvasglobal,legendglobal,extra):

histograms["histMuonTopPt"].SetMaximum(max(histograms["histMuonStopPt"].GetMaximum(),histograms["histRecoMuonStopPtIso"].GetMaximum())+100)
canvasPt,legendPt = plot_hist("histMuonTopPt",1,2,"default",False," \mu from t",False,None,None)
plot_hist("histRecoMuonTopPt",3,3,"default",True,"Reco \mu from t",False,canvasPt,legendPt)
plot_hist("histRecoMuonTopPtIso",2,2,"default",True,"Reco Iso \mu from t",False,canvasPt,legendPt)
plot_hist("histMuonStopPt",1,2,"kRed-4",True, " \mu from \\tilde t",False,canvasPt,legendPt)
plot_hist("histRecoMuonStopPt",3,3,"kRed-4",True, "Reco \mu from \\tilde t",False,canvasPt,legendPt)
plot_hist("histRecoMuonStopPtIso",2,2,"kRed-4",True, "Reco Iso \mu from \\tilde t",True,canvasPt,legendPt)

calculate_efficiency(histograms["histGenfromStop"],histograms["histRecofromStopIso"])
calculate_efficiency(histograms["histRecoMuonStopPt"],histograms["histMuonStopPt"])
calculate_efficiency(histograms["histRecoMuonStopPtIso"],histograms["histRecoMuonStopPt"])
#calculate_efficiency(histograms[""],histograms[""])
exit(0)
	
#-----------------------------------------------------------------------------------------------------------------------



canvas4 = TCanvas("canvas4", "PtMuonsFromTop")
canvas4.SetCanvasSize(800,600)
histMuonTopPt.SetMaximum(max(histMuonStopPt.GetMaximum(),histRecoMuonStopPtIso.GetMaximum())+10)
histMuonTopPt.SetLineWidth(2)
histMuonStopPt.SetLineWidth(2)
histMuonStopPt.SetLineColor(kRed-4)
histRecoMuonTopPt.SetLineStyle(3)
histRecoMuonTopPt.SetLineWidth(3)
histRecoMuonStopPt.SetLineStyle(3)
histRecoMuonStopPt.SetLineWidth(3)
histRecoMuonStopPt.SetLineColor(kRed-4)
histRecoMuonTopPtIso.SetLineStyle(2)
histRecoMuonTopPtIso.SetLineWidth(2)
histRecoMuonStopPtIso.SetLineStyle(2)
histRecoMuonStopPtIso.SetLineWidth(2)
histRecoMuonStopPtIso.SetLineColor(kRed-4)
# histMuonPt.SetLineWidth(2)
# histMuonPt.SetLineColor(41)
# histRecoMuonPt.SetLineColor(41)
# histRecoMuonPt.SetLineStyle(2)
# histRecoMuonPt.SetLineWidth(2)
# histRecoMuonPtIso.SetLineColor(41)
# histRecoMuonPtIso.SetLineStyle(3)
# histRecoMuonPtIso.SetLineWidth(3)
histMuonTopPt.Draw("hist3")
histMuonStopPt.Draw("hist3 same")
histRecoMuonTopPtIso.Draw("hist3 same")
histRecoMuonStopPtIso.Draw("hist3 same")
histRecoMuonStopPt.Draw("hist3 same")
histRecoMuonTopPt.Draw("hist3 same")
# histRecoMuonPtIso.Draw("hist3 same")
# histRecoMuonPt.Draw("hist3 same")
# histMuonPt.Draw("hist3 same")
legend4 = TLegend(0.7,0.1,0.9,0.3)
legend4.AddEntry(histMuonTopPt," \mu from t")
legend4.AddEntry(histRecoMuonTopPt,"Reco \mu from t")
legend4.AddEntry(histRecoMuonTopPtIso, "Reco Iso \mu from t ")
legend4.AddEntry(histMuonStopPt," \mu from \\tilde t")
legend4.AddEntry(histRecoMuonStopPt,"Reco \mu from \\tilde t ")
legend4.AddEntry(histRecoMuonStopPtIso, "Reco Iso \mu from \\tilde t ")
legend4.AddEntry(histMuonPt," \mu")
legend4.AddEntry(histRecoMuonPt,"Reco \mu ")
legend4.AddEntry(histRecoMuonPtIso, "Reco Iso \mu")
legend4.Draw()
canvas4.Update()
canvas4.Print("PtMuonsFromTop.pdf")




print(f"List of W-parents: {WParentList}")





canvas = TCanvas("canvas","GenMuonMultiplicity")
canvas.SetCanvasSize(800,600)
histMuon.SetLineWidth(3)
histMuon.SetMaximum(max(histMuon.GetMaximum(),histRecoMuonMultiplicity.GetMaximum(),histRecoMuonMultiplicityIso.GetMaximum())+10)
histMuon.SetLineStyle(3)
histMuon.Draw("hist")
histRecoMuonMultiplicity.SetLineColor(kRed-4)
histRecoMuonMultiplicity.SetLineWidth(2)
histRecoMuonMultiplicity.Draw("hist same")
histRecoMuonMultiplicityIso.SetLineColor(kBlue-4)
histRecoMuonMultiplicityIso.SetLineWidth(2)
histRecoMuonMultiplicityIso.Draw("hist same")
#histGenMuons.SetLineColor(kRed-4)
#histGenMuons.SetLineWidth(2)
#histGenMuons.Draw(" hist same")
#histGenElectrons.Draw("hist same")
#histGenElectrons.SetLineColor(kBlue)
#histGenElectrons.SetLineWidth(2)
legend = TLegend(0.7,0.7,0.9,0.9)
legend.AddEntry(histRecoMuonMultiplicity,"RecoNoIso","f")
legend.AddEntry(histRecoMuonMultiplicityIso,"RecoIso","f")
#legend.AddEntry(histGenMuons,"All Muons","f")
#legend.AddEntry(histGenElectrons,"Muons+Electrons","f")
legend.AddEntry(histMuon,"GenMuons","f")
legend.Draw()
# TText1 = TText(7,25000,eff_)
# TText1.Draw()

canvas.Update()
canvas.Print("MuonMultiplicity.pdf")


# canvas2 = TCanvas("canvas2","minDeltaRMuonJet")
# canvas2.SetCanvasSize(800,600)
# histDeltaR.SetLineWidth(2)
# histDeltaRljet.SetLineWidth(2)
# histDeltaRljet.SetLineStyle(2)
# histDeltaRljet.SetLineColor(kRed-4)
# histDeltaR.Draw("hist4")
# histDeltaRljet.Draw("hist4 same")
# legend = TLegend(0.6,0.7,0.9,0.9)
# legend.AddEntry(histDeltaR," to nearest Jet")
# legend.AddEntry(histDeltaRljet," to leading Jet")
# legend.Draw()
# canvas2.Update()
# canvas2.Print("minDeltaRMuonJet.pdf")
# 
# canvas3 = TCanvas("canvas3","MuonParents")
# canvas3.SetCanvasSize(800,600)
# xAxis = histMuonParent.GetXaxis()
# xAxis.SetBinLabel(1,"t")
# xAxis.SetBinLabel(2,"\chi_{2}^{0}")
# xAxis.SetBinLabel(3,"\chi_{1}^{\pm}")
# xAxis.SetBinLabel(4,"W^{\pm}")
# xAxis.SetBinLabel(5, " \\tau ")
# xAxis.SetBinLabel(6, " \\tilde t ")
# xAxis.SetBinLabel(7,"Mesons")
# xAxis.SetBinLabel(8,"Baryons")
# xAxis.SetBinLabel(9," \gamma ")
# xAxis.SetBinLabel(10," g ")
# xAxis.SetBinLabel(11," quarks ")
# xAxis.SetBinLabel(12,"else")
# histMuonParent.SetLineWidth(2)
# histMuonParentInsideJet.SetLineWidth(2)
# histMuonParentInsideJet.SetLineColor(kRed)
# histMuonParentInsideBJet.SetLineWidth(2)
# histMuonParentInsideBJet.SetLineColor(kGreen-3)
# histMuonParentInsideBJet.SetLineStyle(2)
# histMuonParent.Draw("hist2")
# histMuonParentInsideJet.Draw("hist2 same")
# histMuonParentInsideBJet.Draw("hist2 same")
# legend2 = TLegend(0.7,0.7,0.9,0.9)
# legend2.AddEntry(histMuonParent,"GenMuons","f")
# legend2.AddEntry(histMuonParentInsideJet,"Muons inside Jets","f")
# legend2.AddEntry(histMuonParentInsideBJet,"Muons inside BJets","f")
# legend2.Draw()
# canvas3.Update()
# canvas3.Print("MuonParent.pdf")






