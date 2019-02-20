#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import numpy as np
import os

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import analysis_ntuples
from lib import analysis_tools
from lib import utils

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Create skims for x1x2x1 process.')
parser.add_argument('-i', '--input_file', nargs=1, help='Input Filename', required=False)
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
parser.add_argument('-madHTgt', '--madHTgt', nargs=1, help='madHT lower bound', required=False)
parser.add_argument('-madHTlt', '--madHTlt', nargs=1, help='madHT uppper bound', required=False)

parser.add_argument('-s', '--signal', dest='signal', help='Signal', action='store_true')
parser.add_argument('-bg', '--background', dest='bg', help='Background', action='store_true')
args = parser.parse_args()

madHTgt = None
madHTlt = None
if args.madHTgt:
	madHTgt = int(args.madHTgt[0])
	print "Got madHT lower bound of " + str(madHTgt)
if args.madHTlt:
	madHTlt = int(args.madHTlt[0])
	print "Got madHT upper bound of " + str(madHTlt)
	

signal = args.signal
bg = args.bg

input_file = None
if args.input_file:
	input_file = args.input_file[0]
output_file = None
if args.output_file:
	output_file = args.output_file[0]

if (bg and signal) or not (bg or signal):
	signal = True
	bg = False
	
######## END OF CMDLINE ARGUMENTS ########
def main():
	chain = TChain('TreeMaker2/PreSelection')
	chain.Add(input_file)
	c = chain.CloneTree()
	chain = None

	fnew = TFile(output_file,'recreate')

	hHt = TH1F('hHt','hHt',100,0,3000)
	hHtWeighted = TH1F('hHtWeighted','hHtWeighted',100,0,3000)
	hHtAfterMadHt = TH1F('hHtAfterMadHt','hHtAfterMadHt',100,0,3000)
	hHt.Sumw2()

	var_Met = np.zeros(1,dtype=float)
	var_METPhi = np.zeros(1,dtype=float)
	var_CrossSection = np.zeros(1,dtype=float)
	var_NJets = np.zeros(1,dtype=int)
	var_BTags = np.zeros(1,dtype=int)
	var_Ht = np.zeros(1,dtype=float)
	var_Mht = np.zeros(1,dtype=float)
	var_MetDHt = np.zeros(1,dtype=float)
	#var_MetDHt2 = np.zeros(1,dtype=float)
	var_Mt2 = np.zeros(1,dtype=float)
	var_Electrons = ROOT.std.vector(TLorentzVector)()
	var_Electrons_charge = ROOT.std.vector(int)()
	var_Muons = ROOT.std.vector(TLorentzVector)()
	var_Muons_charge    = ROOT.std.vector(int)()
	var_GenParticles    = ROOT.std.vector(TLorentzVector)()
  	var_GenParticles_ParentId = ROOT.std.vector(int)()
  	var_GenParticles_ParentIdx = ROOT.std.vector(int)()
 	var_GenParticles_PdgId = ROOT.std.vector(int)()
  	var_GenParticles_Status = ROOT.std.vector(int)()
  	var_LeadingJetPt = np.zeros(1,dtype=float)
	var_NL = np.zeros(1,dtype=int)
 	var_NLGen = np.zeros(1,dtype=int)
 	var_NLGenZ = np.zeros(1,dtype=int)
	
	var_Jets = ROOT.std.vector(TLorentzVector)()
	
	var_LeadingJetPartonFlavor = np.zeros(1,dtype=int)
	var_LeadingJetQgLikelihood = np.zeros(1,dtype=float)
	var_MinDeltaPhiMetJets = np.zeros(1,dtype=float)
	var_MinDeltaPhiMhtJets = np.zeros(1,dtype=float)
	
	#### TRACKS ####
	
	var_tracks          = ROOT.std.vector(TLorentzVector)()
	var_tracks_charge   = ROOT.std.vector(int)()
	var_tracks_chi2perNdof = ROOT.std.vector(double)()
	var_tracks_dxyVtx   = ROOT.std.vector(double)()
	var_tracks_dzVtx    = ROOT.std.vector(double)()
	var_tracks_trackJetIso = ROOT.std.vector(double)()
	var_tracks_trackLeptonIso = ROOT.std.vector(double)()
	var_tracks_trkMiniRelIso = ROOT.std.vector(double)()
	var_tracks_trkRelIso = ROOT.std.vector(double)()
	var_LeadingJet = TLorentzVector()
	

	tEvent = TTree('tEvent','tEvent')
	tEvent.Branch('Met', var_Met,'Met/D')
	tEvent.Branch('METPhi', var_METPhi,'METPhi/D')
	tEvent.Branch('CrossSection', var_CrossSection,'CrossSection/D')
	tEvent.Branch('NJets', var_NJets,'NJets/I')
	tEvent.Branch('BTags', var_BTags,'BTags/I')
	tEvent.Branch('NL', var_NL,'NL/I')
	tEvent.Branch('NLGen', var_NLGen,'NLGen/I')
	tEvent.Branch('NLGenZ', var_NLGenZ,'NLGenZ/I')
	tEvent.Branch('Ht', var_Ht,'Ht/D')
	tEvent.Branch('Mht', var_Mht,'Mht/D')
	tEvent.Branch('MetDHt', var_MetDHt,'MetDHt/D')
	#tEvent.Branch('MetDHt2', var_MetDHt2,'MetDHt2/D')
	tEvent.Branch('Mt2', var_Mt2,'Mt2/D')
	
	tEvent.Branch('Electrons', 'std::vector<TLorentzVector>', var_Electrons)
	tEvent.Branch('Electrons_charge', 'std::vector<int>', var_Electrons_charge)
	tEvent.Branch('Muons', 'std::vector<TLorentzVector>', var_Muons)
	tEvent.Branch('Muons_charge', 'std::vector<int>', var_Muons_charge)
	
	tEvent.Branch('GenParticles', 'std::vector<TLorentzVector>', var_GenParticles)
	tEvent.Branch('GenParticles_ParentId', 'std::vector<int>', var_GenParticles_ParentId)
	tEvent.Branch('GenParticles_ParentIdx', 'std::vector<int>', var_GenParticles_ParentIdx)
	tEvent.Branch('GenParticles_PdgId', 'std::vector<int>', var_GenParticles_PdgId)
	tEvent.Branch('GenParticles_Status', 'std::vector<int>', var_GenParticles_Status)

	tEvent.Branch('Jets', 'std::vector<TLorentzVector>', var_Jets)
	
	tEvent.Branch('LeadingJetPartonFlavor', var_LeadingJetPartonFlavor,'LeadingJetPartonFlavor/I')
	tEvent.Branch('LeadingJetQgLikelihood', var_LeadingJetQgLikelihood,'LeadingJetQgLikelihood/D')
	tEvent.Branch('MinDeltaPhiMetJets', var_MinDeltaPhiMetJets,'MinDeltaPhiMetJets/D')
	tEvent.Branch('MinDeltaPhiMhtJets', var_MinDeltaPhiMhtJets,'MinDeltaPhiMhtJets/D')
	tEvent.Branch('LeadingJetPt', var_LeadingJetPt,'LeadingJetPt/D')

		###### Tracks #######
	tEvent.Branch('tracks', 'std::vector<TLorentzVector>', var_tracks)
	tEvent.Branch('tracks_charge', 'std::vector<int>', var_tracks_charge)
	tEvent.Branch('tracks_chi2perNdof', 'std::vector<double>', var_tracks_chi2perNdof)
	tEvent.Branch('tracks_dxyVtx', 'std::vector<double>', var_tracks_dxyVtx)
	tEvent.Branch('tracks_dzVtx', 'std::vector<double>', var_tracks_dzVtx)
	tEvent.Branch('tracks_trackJetIso', 'std::vector<double>', var_tracks_trackJetIso)
	tEvent.Branch('tracks_trackLeptonIso', 'std::vector<double>', var_tracks_trackLeptonIso)
	tEvent.Branch('tracks_trkMiniRelIso', 'std::vector<double>', var_tracks_trkMiniRelIso)
	tEvent.Branch('tracks_trkRelIso', 'std::vector<double>', var_tracks_trkRelIso)
	tEvent.Branch('LeadingJet', 'TLorentzVector', var_LeadingJet)
	
	nentries = c.GetEntries()
	print 'Analysing', nentries, "entries"

	count = 0
	afterPreselection = 0
	afterMET = 0
	afterBTAGS = 0
	afterNj = 0
	nLMap = {}
	nLGenMap = {}
	nLGenMapZ = {}
	
	crossSection = 1
	if signal:
		filename = os.path.basename(input_file).split("Chi20Chipm.root")[0]
		crossSection = utils.getCrossSection(filename)
		if crossSection is None:			
			if utils.crossSections.get(filename) is not None:
				crossSection = utils.crossSections.get(filename)
			else:
				crossSection = 1.21547

	for ientry in range(nentries):
		if ientry % 1000 == 0:
			print "Processing " + str(ientry)
		c.GetEntry(ientry)
	
		### MADHT ###
		rightProcess = True
		
		if signal:
			rightProcess = analysis_ntuples.isX1X2X1Process(c)
		else:
			crossSection = c.CrossSection
			if (madHTgt is not None and c.madHT < madHTgt) or (madHTlt is not None and c.madHT > madHTlt):
				rightProcess = False

		hHt.Fill(c.HT)
		hHtWeighted.Fill(c.HT, crossSection)
	
		if not rightProcess:
			continue
		count += 1
		hHtAfterMadHt.Fill(c.madHT)
	
		nj, btags, ljet = analysis_ntuples.numberOfJets25Pt2_4Eta_Loose(c)
		nL = c.Electrons.size() + c.Muons.size()
		
		# leptonType = 0
# 		duoLepton = False
	
		# if c.Electrons.size() == 2 and c.Electrons_charge[0] * c.Electrons_charge[1] < 0:
# 			if c.Electrons[0].Pt() > c.Electrons[1].Pt():
# 				var_Leptons[0] = c.Electrons[0]
# 				var_Leptons[1] = c.Electrons[1]
# 			else:
# 				var_Leptons[0] = c.Electrons[1]
# 				var_Leptons[1] = c.Electrons[0]
# 			leptonType = 0
# 			duoLepton = True
# 		if c.Muons.size() == 2 and c.Muons_charge[0] * c.Muons_charge[1] < 0:
# 			if c.Muons[0].Pt() > c.Muons[1].Pt():
# 				var_Leptons[0] = c.Muons[0]
# 				var_Leptons[1] = c.Muons[1]
# 			else:
# 				var_Leptons[0] = c.Muons[1]
# 				var_Leptons[1] = c.Muons[0]
# 			leptonType = 1
# 			duoLepton = True
		
		#### GEN LEVEL STUFF ####
		nLGen = 0
		nLGenZ = 0
		partSize = c.GenParticles.size()
		for ipart in range(partSize):
			if c.GenParticles_Status[ipart] == 1 and (abs(c.GenParticles_PdgId[ipart]) == 11 or abs(c.GenParticles_PdgId[ipart]) == 13):
				nLGen += 1
				if c.GenParticles_ParentId[ipart] == 1000023 or c.GenParticles_ParentId[ipart] == 23:
					nLGenZ += 1
		
		
		if nLMap.get(nL) is not None:
			nLMap[nL] += 1
		else:
			nLMap[nL] = 1
		if nLGenMap.get(nLGen) is not None:
			nLGenMap[nLGen] += 1
		else:
			nLGenMap[nLGen] = 1
		if nLGenMapZ.get(nLGenZ) is not None:
			nLGenMapZ[nLGenZ] += 1
		else:
			nLGenMapZ[nLGenZ] = 1
		#### END OF GEN LEVEL STUFF ####
		
		var_NL[0] = nL
		var_NLGen[0] = nLGen
		var_NLGenZ[0] = nLGenZ
		
		#### PRECUTS ###
		if c.MET < 120: continue
		afterMET += 1
		if btags > 0: continue
		afterBTAGS += 1
		if nj < 1: continue
		afterNj += 1
		#if not duoLepton: continue
		var_MinDeltaPhiMetJets[0] = analysis_ntuples.minDeltaPhiMetJets25Pt2_4Eta(c)
		var_MinDeltaPhiMhtJets[0] = analysis_ntuples.minDeltaPhiMhtJets25Pt2_4Eta(c)
		if var_MinDeltaPhiMhtJets[0] < 0.5: continue
 		if c.MHT < 100: continue
		## END PRECUTS##
	
		afterPreselection += 1
	
		var_Met[0] = c.MET
		var_METPhi[0] = c.METPhi
		var_Mht[0] = c.MHT    	
		var_Ht[0] = c.HT
		var_Mt2[0] = c.MT2
		var_CrossSection[0] = crossSection
		var_NJets[0] = nj
		var_BTags[0] = btags
		var_LeadingJetPt[0] = c.Jets[ljet].Pt()
		var_LeadingJet = c.Jets[ljet]
		
		var_Electrons = c.Electrons
		var_Electrons_charge= c.Electrons_charge
		var_Muons = c.Muons
		var_Muons_charge = c.Muons_charge
		var_Jets = c.Jets
		
		var_GenParticles = c.GenParticles
		var_GenParticles_ParentId = c.GenParticles_ParentId
		var_GenParticles_ParentIdx = c.GenParticles_ParentIdx
		var_GenParticles_PdgId = c.GenParticles_PdgId
		var_GenParticles_Status = c.GenParticles_Status
		
		###### Tracks ######
		var_tracks = c.tracks
		var_tracks_charge = c.tracks_charge
		var_tracks_chi2perNdof = c.tracks_chi2perNdof
		var_tracks_dxyVtx = c.tracks_dxyVtx
		var_tracks_dzVtx = c.tracks_dzVtx
		var_tracks_trackJetIso = c.tracks_trackJetIso
		var_tracks_trackLeptonIso = c.tracks_trackLeptonIso
		var_tracks_trkMiniRelIso = c.tracks_trkMiniRelIso
		var_tracks_trkRelIso = c.tracks_trkRelIso
		
		tEvent.SetBranchAddress('Electrons', var_Electrons)
		tEvent.SetBranchAddress('Electrons_charge', var_Electrons_charge)
		tEvent.SetBranchAddress('Muons', var_Muons)
		tEvent.SetBranchAddress('Muons_charge', var_Muons_charge)
		tEvent.SetBranchAddress('GenParticles', var_GenParticles)
		tEvent.SetBranchAddress('GenParticles_ParentId', var_GenParticles_ParentId)
		tEvent.SetBranchAddress('GenParticles_Status', var_GenParticles_Status)
		tEvent.SetBranchAddress('GenParticles_ParentIdx', var_GenParticles_ParentIdx)
		tEvent.SetBranchAddress('GenParticles_PdgId', var_GenParticles_PdgId)
		tEvent.SetBranchAddress('Jets', var_Jets)
		
		tEvent.SetBranchAddress('tracks', var_tracks)
		tEvent.SetBranchAddress('tracks_charge', var_tracks_charge)
		tEvent.SetBranchAddress('tracks_chi2perNdof', var_tracks_chi2perNdof)
		tEvent.SetBranchAddress('tracks_dxyVtx', var_tracks_dxyVtx)
		tEvent.SetBranchAddress('tracks_dzVtx', var_tracks_dzVtx)
		tEvent.SetBranchAddress('tracks_trackJetIso', var_tracks_trackJetIso)
		tEvent.SetBranchAddress('tracks_trackLeptonIso', var_tracks_trackLeptonIso)
		tEvent.SetBranchAddress('tracks_trkMiniRelIso', var_tracks_trkMiniRelIso)
		tEvent.SetBranchAddress('tracks_trkRelIso', var_tracks_trkRelIso)
		tEvent.SetBranchAddress('LeadingJet', var_LeadingJet)

		# l1 = var_Leptons[0]
# 		l2 = var_Leptons[1]
# 	
# 		ht = analysis_ntuples.htJet25(c) - l1.Pt() - l2.Pt() 
		#var_DilepHt[0] = ht
		#ht = analysis_ntuples.htJet25(c)
		metDHt = 9999999
		if c.HT != 0:
			metDHt = c.MET / c.HT
		#metDHt2 = 9999999
		#if ht != 0:
		#	metDHt2 = c.MET / ht
	
		var_MetDHt[0] = metDHt
		#var_MetDHt2[0] = metDHt2
	
		# var_InvMass[0] = (l1 + l2).M()
# 		var_DileptonPt[0] = abs((l1 + l2).Pt())
# 		var_DeltaPhi[0] = abs(l1.DeltaPhi(l2))
# 		var_DeltaEta[0] = abs(l1.Eta() - l2.Eta())
# 		var_DeltaR[0] = abs(l1.DeltaR(l2))
# 		var_Pt3[0] = analysis_tools.pt3(l1.Pt(),l1.Phi(),l2.Pt(),l2.Phi(),c.MET,c.METPhi)
# 		var_Mt1[0] = analysis_tools.MT2(c.MET, c.METPhi, l1)
# 		var_Mt2[0] = analysis_tools.MT2(c.MET, c.METPhi, l2)
# 		var_Mtautau[0] = analysis_tools.PreciseMtautau(c.MET, c.METPhi, l1, l2)
# 	
# 		var_Eta1[0] = l1.Eta()
# 		var_Eta2[0] = l2.Eta()
# 
# 		var_Phi1[0] = l1.Phi()
# 		var_Phi2[0] = l2.Phi()
# 
# 		var_Pt1[0] = l1.Pt()
# 		var_Pt2[0] = l2.Pt()
# 	
# 		var_DeltaEtaLeadingJetDilepton[0] = abs((l1 + l2).Eta() - c.Jets[ljet].Eta())	
		var_LeadingJetPartonFlavor[0] = c.Jets_partonFlavor[ljet]
		var_LeadingJetQgLikelihood[0] = c.Jets_qgLikelihood[ljet]
		
		
		
		tEvent.Fill()

	fnew.cd()
	tEvent.Write()
	print 'just created', fnew.GetName()
	print "Total: " + str(nentries)
	print "Right Process: " + str(count)
	print "After MET: " + str(afterMET)
	print "After BTAGS: " + str(afterBTAGS)
	print "After NJ: " + str(afterNj)
	print "After Preselection: " + str(afterPreselection)
	print "nL:"
	print nLMap
	print "nLGen:"
	print nLGenMap
	print "nLGenZ:"
	print nLGenMapZ

	hHt.Write()
	hHtWeighted.Write()
	hHtAfterMadHt.Write()
	fnew.Close()

main()
