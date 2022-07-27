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
parser.add_argument('-r','--recoplots',action = 'store_true', required = False)
parser.add_argument('-5','--fivegev', action = 'store_true', required = False)
args = parser.parse_args()

#m_stop = 500, m_Chi_pm = 115, dm = 1.4
signal_files = [
glob("/afs/desy.de/user/d/diepholq/nfs/x1x2x1/signal/skim/sum/higgsino_Summer16_stopstop_*GeV_mChipm*GeV_dm*GeV_1.root")
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
"MuonParentInsideBJet",[12,0,12],"MuonStopPt",[60,0,30],"RecoMuonStopPt",[60,0,30],"RecoMuonStopPtIso",[60,0,30],"MuonTopPt",[60,0,30],"RecoMuonTopPt",[60,0,30],"RecoMuonTopPtIso",[60,0,30],
"FractionsBothGen2",[4,0,4],"FractionsSameChi2",[4,0,4],"Fakes2",[4,0,4],"FractionsBothGen3",[4,0,4],"FractionsSameChi3",[4,0,4],"Fakes3",[4,0,4],
"FractionsBothGen4",[4,0,4],"FractionsSameChi4",[4,0,4],"Fakes4",[4,0,4],"pT2",[60,0,15],"pT3",[60,0,15],"pT4",[60,0,15],"invMass2",[40,0,10],"invMass3",[40,0,10],"invMass4",[40,0,10]]

i = 0
while i < len(arglist):
	create_hist(arglist[i],arglist[i+1])
	i+=2
# histMuonParent = TH1F("MuonParents"," ; Parent ; ",12,0,12)

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

def plot_hist(key,linestyle,linewidth,linecolor,same,legendentry,pdf,canvasglobal,legendglobal):
	key = str(key)
	h1 = histograms[key]
	h1.SetLineStyle(linestyle)
	h1.SetLineWidth(linewidth)
	if linecolor == "2":
		h1.SetLineColor(2)
	if linecolor == "4":
		h1.SetLineColor(4)
	if linecolor == "40":
		h1.SetLineColor(40)
	if same == False:
		canvas = TCanvas("canvas",key)
		canvas.SetCanvasSize(800,600)
		legend = TLegend(0.7,0.7,0.9,0.9)
		if legendentry is not None:
			legend.AddEntry(key,legendentry,"f")
		h1.Draw("hist")
		if pdf == False:
			return canvas,legend
	if same:
		h1.Draw("hist same")
		legend = legendglobal
		if legendentry is not None:
			legend.AddEntry(key,legendentry,"f")
		canvas = canvasglobal
	legend.Draw()
	canvas.Update()
	if pdf:
		Titel = key+ ".pdf"
		canvas.Print(Titel)



# genmuons2 = []
# for ientry in range(number_of_entries):
# 	chain.GetEntry(ientry)
# 	if ientry % 1000 == 0:
# 		print("Processing " + str(ientry), "of", number_of_entries)
# 	for idx in range(len(chain.GenParticles)):
# 		if abs(chain.GenParticles_PdgId[idx]) == 13 and chain.GenParticles[idx].Pt() > 2 and chain.GenParticles[idx].Pt() < 15:
# 			genmuons2.append(chain.GenParticles[idx])
# 	genmuons = [chain.GenParticles[idx] for idx in range(len(chain.GenParticles)) if (abs(chain.GenParticles_PdgId[idx]) == 13 and 
# 	chain.GenParticles[idx].Pt() > 2 and chain.GenParticles[idx].Pt() < 15)]	
# 	print(len(genmuons),"      ", len(genmuons2))





#main-------------------------------------------------------------------------------------

PtUpper = [15,11,7]
jetIsoStr = "Muons_passCorrJetIso15Dr0.4"
def mainGen(PtThreshold):
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
				if chain.GenParticles_PdgId[idx] == 13 and abs(chain.GenParticles_ParentId[idx]) == 1000023 and abs(chain.GenParticles_ParentId[chain.GenParticles_ParentIdx[idx]]) == 1000006:
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








def mainReco(PtThreshold,MuonNumber,comparison_type,histinvMass,histpT):
	print("Starting Loop")
	MuonNumberEvents = 0
	AllGenMatchedEvents = 0
	AtLeastOnefromChi = 0
	AllFromChi = 0
	both_from_same_chi = 0
	for ientry in range(number_of_entries):
		chain.GetEntry(ientry)
		if ientry % 1000 == 0:
			print("Processing " + str(ientry), "of", number_of_entries)
		MuonSize = len(chain.Muons)
		MuonMultiplicityPtPassed = 0
		selectedMuonsIdxs = []
		charges_list = []

		if chain.MHT < 200:                 #cuts
			continue
		if chain.MET < 140:
			continue
		if chain.MinDeltaPhiMhtJets < 0.4:
			continue

		for muon in range(len(chain.Muons)):                   #pT criterion
			if chain.Muons[muon].Pt() < PtThreshold and chain.Muons[muon].Pt() > 2:
				MuonMultiplicityPtPassed += 1
				selectedMuonsIdxs.append(muon)
		if MuonMultiplicityPtPassed != MuonNumber:              #check for right number of muons that pass pT criterion
			continue

		opposite_charge = None
		
		for midx in range(MuonNumber):                    #opposite charge check
			charges_list.append(chain.Muons_charge[selectedMuonsIdxs[midx]])
		mus = charges_list.count(-1)
		antimus = charges_list.count(1)
		if mus == 0 or antimus == 0:
			continue 
		#MuonNumberEvents += 1  # 
# 		print([chain.Muons[i].Pt() for i in selectedMuonsIdxs])
# 		continue
		if MuonNumber == 3:
			if mus == 1:
				opposite_midx = charges_list.index(-1)
				same_idx1 = charges_list.index(1)
				same_idx2 = charges_list.index(1,same_idx1+1)
			else:
				opposite_midx = charges_list.index(1)
				same_idx1 = charges_list.index(-1)
				same_idx2 = charges_list.index(-1,same_idx1+1)

		if MuonNumber == 4:
			if comparison_type == "invMass":
				invMass_list = []
				invMass_dict = {}
				if mus == 1:
					muon1invMass = charges_list.index(-1)
					same_idx1 = charges_list.index(1)
					same_idx2 = charges_list.index(1,same_idx1+1)
					same_idx3 = charges_list.index(1,same_idx2+1)
				if antimus == 1:
					muon1invMass = charges_list.index(1)
					same_idx1 = charges_list.index(-1)
					same_idx2 = charges_list.index(-1,same_idx1+1)
					same_idx3 = charges_list.index(-1,same_idx2+1)
					same_idx_list= [same_idx1,same_idx2,same_idx3]
				for idx in same_idx_list:
					invMass_list.append((chain.Muons[selectedMuonsIdxs[muon1invMass]]+chain.Muons[selectedMuonsIdxs[idx]]).M())
					min_invMass = min(invMass_list)
					min_invMass_index = invMass_list.index(min_invMass)
					muon2invMass = same_idx_list[min_invMass_index] 
					if args.fivegev:
						if min_invMass > 5:
							continue
				#print(invMass_list,min_invMass_index)
				if mus == 2:
					mu_idx1 = charges_list.index(-1)
					mu_idx2 = charges_list.index(-1,mu_idx1+1)
					antimu_idx1 = charges_list.index(1)
					antimu_idx2 = charges_list.index(1,antimu_idx1+1)
					key1 = str(mu_idx1) + "," + str(antimu_idx1)
					key2 = str(mu_idx2) + "," + str(antimu_idx1)
					key3 = str(mu_idx1) + "," + str(antimu_idx2)
					key4 = str(mu_idx2) + "," + str(antimu_idx2)
					invMass_dict.update({key1: (chain.Muons[selectedMuonsIdxs[mu_idx1]]+chain.Muons[selectedMuonsIdxs[antimu_idx1]]).M()})
					invMass_dict.update({key2: (chain.Muons[selectedMuonsIdxs[mu_idx2]]+chain.Muons[selectedMuonsIdxs[antimu_idx1]]).M()})
					invMass_dict.update({key3: (chain.Muons[selectedMuonsIdxs[mu_idx1]]+chain.Muons[selectedMuonsIdxs[antimu_idx2]]).M()})
					invMass_dict.update({key4: (chain.Muons[selectedMuonsIdxs[mu_idx2]]+chain.Muons[selectedMuonsIdxs[antimu_idx2]]).M()})
					#print(invMass_dict)
					min_invMass = None
					min_invMass_key = None
					for key in invMass_dict:
						if min_invMass is None or min_invMass > invMass_dict[key]:
							min_invMass = invMass_dict[key]
							min_invMass_key = key
					muon1invMass = int(min_invMass_key.split(",")[0])
					muon2invMass = int(min_invMass_key.split(",")[1])
					#print(muon1invMass,muon2invMass)
					if args.fivegev:
						if min_invMass > 5:
							continue
				selectedMuonsIdxs = [selectedMuonsIdxs[muon1invMass],selectedMuonsIdxs[muon2invMass]]
			if comparison_type == "pT":
				pT_list = [chain.Muons[mu].Pt() for mu in selectedMuonsIdxs]
				pT_list.index(min(pT_list))
				pT_dict = {}
				for i in range(len(pT_list)):
					min_idx = pT_list.index(min(pT_list))
					pT_dict.update({str(min_idx) +","+str(i) + "," + str(charges_list[min_idx]): min(pT_list)})
					pT_list.pop(min_idx)
				#	print(pT_list)
				#print(pT_dict)
				min_pT_key = [key for key in pT_dict if int(key.split(",")[1]) == 0][0]
				min_pT_idx = int(min_pT_key.split(",")[0])
				min_pT_charge = int(min_pT_key.split(",")[2])
				del pT_dict[min_pT_key]
				charge = min_pT_charge
				i = 0 
				while charge == min_pT_charge:
					second_key = min(pT_dict, key = pT_dict.get)
				#	print("pt second_key", pT_dict[second_key])
					second_idx = int(second_key.split(",")[0])
					second_charge = int(second_key.split(",")[2])
					charge = second_charge
					if second_charge == min_pT_charge:
						del pT_dict[second_key]
					i += 1
					if i > 3:
						break
				selectedMuonsIdxs = [selectedMuonsIdxs[min_pT_idx],selectedMuonsIdxs[second_idx]]

		if MuonNumber == 3:         #choosing the second muon with less pT
			muon1 = opposite_midx
			if chain.Muons[same_idx1].Pt() < chain.Muons[same_idx2].Pt():
				muon2pT = same_idx1
			else: 
				muon2pT = same_idx2
			if (chain.Muons[opposite_midx] + chain.Muons[same_idx1]).M() < (chain.Muons[opposite_midx] + chain.Muons[same_idx2]).M():   #choosing 2nd muon with min invMass together with opposite sign muon
				muon2invMass = same_idx1
			else:
				muon2invMass = same_idx2
			if comparison_type == "invMass":
				selectedMuonsIdxs = [selectedMuonsIdxs[opposite_midx],selectedMuonsIdxs[muon2invMass]]
			if comparison_type == "pT":
				selectedMuonsIdxs = [selectedMuonsIdxs[opposite_midx],selectedMuonsIdxs[muon2pT]]

		MuonNumberEvents += 1 
		genmuons = [chain.GenParticles[idx] for idx in range(len(chain.GenParticles)) if (abs(chain.GenParticles_PdgId[idx]) == 13 and 
		chain.GenParticles[idx].Pt() > 2 and chain.GenParticles[idx].Pt() < 15)]        #gen muons selection from genparticles, followed by matching
		# genmuons_from_neutralino = [chain.GenParticles[idx] for idx in range(len(chain.GenParticles)) if (abs(chain.GenParticles_PdgId[idx]) == 13 and 
# 		chain.GenParticles[idx].Pt() > 2 and chain.GenParticles[idx].Pt() < 15 and chain.GenParticles_ParentId[idx] == 1000023 
# 		and chain.GenParticles_ParentId[chain.GenParticles_ParentIdx[idx]] == 1000006)] #gen muons whose parent is the scnd neutralino
		gen_matched = 0 
		gen_matched_chi = 0
		genmuons_from_neutralino = []
		genmuons_from_neutralino_ParentIdxs = []
		for idx in range(len(chain.GenParticles)):
			if abs(chain.GenParticles_PdgId[idx]) == 13 and chain.GenParticles[idx].Pt() > 2 and chain.GenParticles[idx].Pt() < 15 and abs(chain.GenParticles_ParentId[idx]) == 1000023 and abs(chain.GenParticles_ParentId[chain.GenParticles_ParentIdx[idx]]) == 1000006 and chain.GenParticles_Status[idx] == 1:
				#print(chain.GenParticles[idx].Pt(),chain.GenParticles_ParentIdx[idx],chain.GenParticles_ParentId[idx])
				genmuons_from_neutralino.append(chain.GenParticles[idx])
				genmuons_from_neutralino_ParentIdxs.append(chain.GenParticles_ParentIdx[idx])
		#print([i.Pt() for i in genmuons_from_neutralino],genmuons_from_neutralino_ParentIdxs)
		#print(genmuons_from_neutralino_ParentIdxs)
		for midx in range(2):  
			mindR, minCan = minDeltaLepLeps(chain.Muons[selectedMuonsIdxs[midx]], genmuons)  #prevent matching to same muons?
			if mindR is not None:
				if mindR < 0.01:
					gen_matched += 1
		for midx in range(2): 
			mindR_chi, minCan_chi = minDeltaLepLeps(chain.Muons[selectedMuonsIdxs[midx]], genmuons_from_neutralino)
			if mindR_chi is not None:
				if mindR_chi < 0.01:
					gen_matched_chi += 1
					#print("midx:",midx,"minCan_chi:",minCan_chi, genmuons_from_neutralino_ParentIdxs[minCan_chi])
					if midx == 0:
						parentidx = genmuons_from_neutralino_ParentIdxs[minCan_chi]
						#print(midx,parentidx)
					if midx == 1 and gen_matched_chi == 2:
						if parentidx == genmuons_from_neutralino_ParentIdxs[minCan_chi]:
							both_from_same_chi += 1
							#print(midx,parentidx)

		for muon in selectedMuonsIdxs:
			histpT.Fill(chain.Muons[muon].Pt())
		histinvMass.Fill((chain.Muons[selectedMuonsIdxs[0]]+chain.Muons[selectedMuonsIdxs[1]]).M())

		if gen_matched == 2: 
			AllGenMatchedEvents += 1
# 		if gen_matched_chi > 0:
# 			AtLeastOnefromChi += 1 
		if gen_matched_chi == 2: 
			AllFromChi += 1
	#event loop end
	fraction_both_gen = AllGenMatchedEvents/MuonNumberEvents
	#fraction_at_least_one = AtLeastOnefromChi/MuonNumberEvents
	#fraction_genmatched_at_least_one = AtLeastOnefromChi/AllGenMatchedEvents
	print(f"Number of events with MuonNumber = {MuonNumber}: {MuonNumberEvents}")
	print("Fraction of those events where all muons are matched to gen muons :",fraction_both_gen)
	#print("Fraction of all gen matched events where at least one is matched to a muon from chi02 decay:",AtLeastOnefromChi/AllGenMatchedEvents)
	#print("Fraction of all events where all muons are genmatched and at least one is matched to a muon from chi02 decay:",AtLeastOnefromChi/MuonNumberEvents)
	print("Fraction of those events where all muons are genmatched to a muon from a chi02 decay:",AllFromChi/MuonNumberEvents)
	print("Fraction of those events where both $\mu$ are matched to gen muons from the same chi02 decay:",both_from_same_chi/MuonNumberEvents)
	return AllGenMatchedEvents, AllFromChi, both_from_same_chi, MuonNumberEvents

#plot_hist(key,linestyle,linewidth,linecolor,same,legendentry,pdf,canvasglobal,legendglobal):

#mainReco(PtUpper[0],4,"pT",histograms["histinvMass4"],histograms["histpT4"])		
# plot_hist("histpT4",1,2,"default",False,None,True,None,None)
# plot_hist("histpT4",1,2,"default",False,None,True,None,None)
if args.recoplots:
	for munumber in [2,3,4]:
		AllGenMatchedEvents,AllFromChi,both_from_same_chi,MuonNumberEvents = mainReco(PtUpper[0],munumber,"invMass",histograms["histinvMass"+str(munumber)],histograms["histpT"+str(munumber)])  #pT or invMass
		print("plotting")
		xaxis = histograms["histFractionsBothGen"+str(munumber)].GetXaxis()
		histograms["histFractionsBothGen"+str(munumber)].SetMaximum(1)
		xaxis.SetBinLabel(3,"Both \mu genmatched")
		xaxis.SetBinLabel(1,"At least one fake \mu")
		xaxis.SetBinLabel(4,"Both to \chi_{2}^{0} decay")
		histograms["histFractionsBothGen"+str(munumber)].AddBinContent(3,AllGenMatchedEvents/MuonNumberEvents)
		histograms["histFractionsSameChi"+str(munumber)].AddBinContent(4,both_from_same_chi/MuonNumberEvents)
		histograms["histFakes"+str(munumber)].AddBinContent(1,1-AllGenMatchedEvents/MuonNumberEvents)
# 	plot_hist("histpT3",1,2,"kRed-4",True,"3 \mu",False,canvaspT,legendpT)
# 	plot_hist("histpT4",1,2,"kGreen-2",True,"4 \mu",True,canvaspT,legendpT)
# 	canvasinvMass,legendinvMass = plot_hist("histinvMass2",1,2,"default",False,"2 \mu",False,None,None)
# 	plot_hist("histinvMass3",1,2,"kRed-4",True,"3 \mu",False,canvasinvMass,legendinvMass)
# 	plot_hist("histinvMass4",1,2,"kGreen-2",True,"4 \mu",True,canvasinvMass,legendinvMass)

canvasFractions,legendFractions = plot_hist("histFractionsBothGen2",1,2,"2",False,None,False,None,None)
if args.recoplots:
	for munumber in [2,3,4]:
		if munumber == 2:
			color = "2"
		if munumber == 3:
			color = "4"
		if munumber == 4:
			color = "40"
		if munumber != 2:
			plot_hist("histFractionsBothGen"+str(munumber),1,2,color,True,None,False,canvasFractions,legendFractions)
		plot_hist("histFakes"+str(munumber),1,2,color,True,None,False,canvasFractions,legendFractions)
		if munumber != 4:
			plot_hist("histFractionsSameChi"+str(munumber),1,2,color,True,str(munumber)+" \mu",False,canvasFractions,legendFractions)
plot_hist("histFractionsSameChi4",1,2,"40",True,str(munumber)+" \mu",True,canvasFractions,legendFractions)


#plotting---------------------------------------------------------------------------------




if args.noplots:
	exit(0)
mainGen(PtUpper[0])









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
	

