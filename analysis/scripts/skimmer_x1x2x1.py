#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
from array import array
import argparse
import sys
import numpy as np
import os

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import analysis_ntuples
from lib import analysis_tools

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
var_CrossSection = np.zeros(1,dtype=float)
var_NJets = np.zeros(1,dtype=int)
var_BTags = np.zeros(1,dtype=int)
var_NLeptons = np.zeros(1,dtype=int)
var_Ht = np.zeros(1,dtype=float)
var_Mht = np.zeros(1,dtype=float)
var_MetDHt = np.zeros(1,dtype=float)
var_MetDHt2 = np.zeros(1,dtype=float)
var_LeptonsType = np.zeros(1,dtype=int)
var_Leptons = ROOT.std.vector(TLorentzVector)(2)
var_DilepHt = np.zeros(1,dtype=float)
### CALCULATED FROM DILEPTON - MIGHT NOT BE NEEDED
var_InvMass = np.zeros(1,dtype=float)
var_DileptonPt = np.zeros(1,dtype=float)
var_DeltaPhi = np.zeros(1,dtype=float)
var_DeltaEta = np.zeros(1,dtype=float)
var_DeltaR = np.zeros(1,dtype=float)
var_Pt3 = np.zeros(1,dtype=float)
var_Mt1 = np.zeros(1,dtype=float)
var_Mt2 = np.zeros(1,dtype=float)
var_Mtautau = np.zeros(1,dtype=float)

var_Eta1 = np.zeros(1,dtype=float)
var_Eta2 = np.zeros(1,dtype=float)
 
var_Phi1 = np.zeros(1,dtype=float)
var_Phi2 = np.zeros(1,dtype=float)

var_Pt1 = np.zeros(1,dtype=float)
var_Pt2 = np.zeros(1,dtype=float)

########### END OF DILEPTON ###########
var_DeltaEtaLeadingJetDilepton = np.zeros(1,dtype=float)
var_LeadingJetPartonFlavor = np.zeros(1,dtype=int)
var_LeadingJetQgLikelihood = np.zeros(1,dtype=float)

tEvent = TTree('tEvent','tEvent')
tEvent.Branch('Met', var_Met,'Met/D')
tEvent.Branch('CrossSection', var_CrossSection,'CrossSection/D')
tEvent.Branch('NJets', var_NJets,'NJets/I')
tEvent.Branch('BTags', var_BTags,'BTags/I')
#tEvent.Branch('NLeptons', var_NLeptons,'NLeptons/I')
tEvent.Branch('Ht', var_Ht,'Ht/D')
tEvent.Branch('Mht', var_Mht,'Mht/D')
tEvent.Branch('MetDHt', var_MetDHt,'MetDHt/D')
tEvent.Branch('MetDHt2', var_MetDHt2,'MetDHt2/D')
tEvent.Branch('LeptonsType', var_LeptonsType,'LeptonsType/I')
tEvent.Branch('Leptons', 'std::vector<TLorentzVector>', var_Leptons)
tEvent.Branch('DilepHt', var_DilepHt,'DilepHt/D')
### CALCULATED FROM DILEPTON - MIGHT NOT BE NEEDED
tEvent.Branch('InvMass', var_InvMass,'InvMass/D')
tEvent.Branch('DileptonPt', var_DileptonPt,'DileptonPt/D')
tEvent.Branch('DeltaPhi', var_DeltaPhi,'DeltaPhi/D')
tEvent.Branch('DeltaEta', var_DeltaEta,'DeltaEta/D')
tEvent.Branch('DeltaR', var_DeltaR,'DeltaR/D')
tEvent.Branch('Pt3', var_Pt3,'Pt3/D')
tEvent.Branch('Mt1', var_Mt1,'Mt1/D')
tEvent.Branch('Mt2', var_Mt2,'Mt2/D')
tEvent.Branch('Mtautau', var_Mtautau,'Mtautau/D')

tEvent.Branch('Eta1', var_Eta1,'Eta1/D')
tEvent.Branch('Eta2', var_Eta2,'Eta2/D')

tEvent.Branch('Phi1', var_Phi1,'Phi1/D')
tEvent.Branch('Phi2', var_Phi2,'Phi2/D')

tEvent.Branch('Pt1', var_Pt1,'Pt1/D')
tEvent.Branch('Pt2', var_Pt2,'Pt2/D')
########### END OF DILEPTON ###########
tEvent.Branch('DeltaEtaLeadingJetDilepton', var_DeltaEtaLeadingJetDilepton,'DeltaEtaLeadingJetDilepton/D')
tEvent.Branch('LeadingJetPartonFlavor', var_LeadingJetPartonFlavor,'LeadingJetPartonFlavor/I')
tEvent.Branch('LeadingJetQgLikelihood', var_LeadingJetQgLikelihood,'LeadingJetQgLikelihood/D')

nentries = c.GetEntries()
print 'Analysing', nentries, "entries"

for ientry in range(nentries):
	if ientry % 1000 == 0:
		print "Processing " + str(ientry)
	c.GetEntry(ientry)
	
	### MADHT ###
	rightProcess = True
	crossSection = 1
	if signal:
		rightProcess = analysis_ntuples.isX1X2X1Process(c)
		filename = os.path.basename(input_file).split("_")[0]
		if utils.crossSections.get(filename) is not None:
			crossSection = utils.crossSections.get(filename)
	else:
		crossSection = c.CrossSection
		if (madHTgt is not None and c.madHT < madHTgt) or (madHTlt is not None and c.madHT > madHTlt):
			rightProcess = False

	hHt.Fill(c.madHT)
	hHtWeighted.Fill(c.madHT, crossSection)
	
	if not rightProcess:
		continue
	
	hHtAfterMadHt.Fill(c.madHT)
	
 	nj, btags, ljet = analysis_ntuples.numberOfJets25Pt2_4Eta_Loose(c)
 	nL = c.Electrons.size() + c.Muons.size()
 	leptonType = 0
 	duoLepton = False
 	
 	if c.Electrons.size() == 2 and c.Electrons_charge[0] * c.Electrons_charge[1] < 0:
		if c.Electrons[0].Pt() > c.Electrons[1].Pt():
			var_Leptons[0] = c.Electrons[0]
			var_Leptons[1] = c.Electrons[1]
		else:
			var_Leptons[0] = c.Electrons[1]
			var_Leptons[1] = c.Electrons[0]
		leptonType = 0
		duoLepton = True
	elif c.Muons.size() == 2 and c.Muons_charge[0] * c.Muons_charge[1] < 0:
		if c.Muons[0].Pt() > c.Muons[1].Pt():
			var_Leptons[0] = c.Muons[0]
			var_Leptons[1] = c.Muons[1]
		else:
			var_Leptons[0] = c.Muons[1]
			var_Leptons[1] = c.Muons[0]
		leptonType = 1
		duoLepton = True
	#### PRECUTS ###
	if c.MET < 120: continue
	if btags > 0: continue
	if nj < 1: continue
	if not duoLepton: continue
	## END PRECUTS##
 	
 	var_Met[0] = c.MET
 	var_Mht[0] = c.MHT    	
 	var_Ht[0] = c.HT
 	var_CrossSection[0] = crossSection
 	var_NJets[0] = nj
 	var_BTags[0] = btags
 
 	var_NLeptons[0] = nL
 	var_LeptonsType[0] = leptonType
 	
 	l1 = var_Leptons[0]
 	l2 = var_Leptons[1]
	
 	ht = analysis_ntuples.htJet25(c) - l1.Pt() - l2.Pt() 
	
 	var_DilepHt[0] = ht
	
	metDHt = 9999999
 	if c.HT != 0:
 		metDHt = c.MET / c.HT		
	metDHt2 = 9999999
	if ht != 0:
		metDHt2 = c.MET / ht
	
	var_MetDHt[0] = metDHt
	var_MetDHt2[0] = metDHt2
	
	var_InvMass[0] = (l1 + l2).M()
	var_DileptonPt[0] = abs((l1 + l2).Pt())
	var_DeltaPhi[0] = abs(l1.DeltaPhi(l2))
	var_DeltaEta[0] = abs(l1.Eta() - l2.Eta())
	var_DeltaR[0] = abs(l1.DeltaR(l2))
	var_Pt3[0] = analysis_tools.pt3(l1.Pt(),l1.Phi(),l2.Pt(),l2.Phi(),c.MET,c.METPhi)
	var_Mt1[0] = analysis_tools.MT2(c.MET, c.METPhi, l1)
	var_Mt2[0] = analysis_tools.MT2(c.MET, c.METPhi, l2)
	var_Mtautau[0] = analysis_tools.PreciseMtautau(c.MET, c.METPhi, l1, l2)
	
	var_Eta1[0] = l1.Eta()
	var_Eta2[0] = l2.Eta()

	var_Phi1[0] = l1.Phi()
	var_Phi2[0] = l2.Phi()

	var_Pt1[0] = l1.Pt()
	var_Pt2[0] = l2.Pt()
	
	var_DeltaEtaLeadingJetDilepton[0] = abs((l1 + l2).Eta() - c.Jets[ljet].Eta())	
	var_LeadingJetPartonFlavor[0] = c.Jets_partonFlavor[ljet]
	var_LeadingJetQgLikelihood[0] = c.Jets_qgLikelihood[ljet]

	tEvent.Fill()

fnew.cd()
tEvent.Write()
print 'just created', fnew.GetName()
hHt.Write()
hHtWeighted.Write()
hHtAfterMadHt.Write()
fnew.Close()
