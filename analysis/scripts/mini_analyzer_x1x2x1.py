#!/usr/bin/python

from ROOT import *
from glob import glob
from math import *
from sys import exit
import array
import argparse
import sys

# load FWLite C++ libraries
#gSystem.Load("libFWCoreFWLite.so");
#gSystem.Load("libDataFormatsFWLite.so");
#FWLiteEnabler.enable()

# load FWlite python libraries
#from DataFormats.FWLite import Handle, Events
#import FWCore.ParameterSet.Config as cms

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import analysis_ntuples
from lib import utils
from lib import analysis_tools
import itertools

#############    CMD ARGS    #############

parser = argparse.ArgumentParser(description='Create histograms for x1x2x1 process.')
parser.add_argument('-i', '--input_file', nargs=1, help='Input Filename', required=False)
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
parser.add_argument('-madHTgt', '--madHTgt', nargs=1, help='madHT lower bound', required=False)
parser.add_argument('-madHTlt', '--madHTlt', nargs=1, help='madHT uppper bound', required=False)
parser.add_argument('-cf', '--cut_flow', nargs=1, help='Cut Flow', required=False)

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

print "Bg=" + str(bg) + " Signal=" + str(signal)

cf = None

if args.cut_flow:
	cf = args.cut_flow[0]

input_file = None
if args.input_file:
	input_file = args.input_file[0]
output_file = None
if args.output_file:
	output_file = args.output_file[0]

if (bg and signal) or not (bg or signal):
	signal = True
	bg = False

###############################################


histList = {
	"HT" : TH1F("HT", "HT", 100, 0, 5000),
	"HTWeight" : TH1F("HTWeight", "HT Weighted", 100, 0, 5000),
	"MDuoLepCanInvMassGT1J" : TH1F("MDuoLepCanInvMassGT1J", "Invariant Mass - Di Muons Candidates >= 1 Jet", 50, 0, 70),
	"DuoLepCanInvMassGT1JMET125-200" : TH1F("DuoLepCanInvMassGT1JMET125-200", "Invariant Mass - Dilepton Candidates >= 1 Jet, 125 < MET < 200"
						, 4, array.array('d', [4,10,20,30,50])),
	"DuoLepCanInvMassGT1JMET200-250" : TH1F("DuoLepCanInvMassGT1JMET200-250", "Invariant Mass - Dilepton Candidates >= 1 Jet, 200 < MET < 250"
						, 4, array.array('d', [4,10,20,30,50])),
	"DuoLepCanInvMassGT1JMET250" : TH1F("DuoLepCanInvMassGT1JMET250", "Invariant Mass - Dilepton Candidates >= 1 Jet, MET > 250"
						, 4, array.array('d', [4,10,20,30,50]))
}

c = TChain("TreeMaker2/PreSelection");
print input_file
c.Add(input_file)

nentries = c.GetEntries()
print "nentries=" + str(nentries)

cutNames = ["Total", "2mu", "leplepPt", "pt5sublep", "opposite-sign", "dilepPt", "Mll>4", "Mll<50", "Upsilon_veto", "lowMET","HT", "METovHT", "bveto", "mtautau", "MT"]
cutValues = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cutValues[0] = nentries

def DileptonLepCorMET(c):
	ptmiss = TLorentzVector()
	ptmiss.SetPtEtaPhiE(c.MET,0,c.METPhi,c.MET)
	
	for lep in c.Muons:
		lepPt = TLorentzVector(lep.Px(), lep.Py(), 0, lep.Pt())
		ptmiss += lepPt
	#print "ptmis=" + str(c.MET) + " corr=" + str(ptmiss.Pt())
	#if ptmiss.Pt() >= 125:
	#	print "******** ptmiss=" + str(ptmiss.Pt())
	return ptmiss.Pt() >= 125
		
def passedLep(leps, miniIsos, tightIDs, eta, lcharges):
	passed = 0
	passedMuons = []
	charges = []
	for i, l in enumerate(leps):
		if miniIsos[i] < 0.5 and miniIsos[i] * l.Pt() < 5:# l.Pt() < 30 and l.Pt() > 5:# and abs(l.Eta()) < eta:# and 
			passed += 1
			passedMuons.append(l)
			charges.append(lcharges[i])
	return passedMuons, charges
	
	

def twoMuons(c):
	if len(c.Electrons) == 0 and len(c.Muons) == 2:
		if c.Muons[0].Pt() > c.Muons[1].Pt():
			return [0,1]
		else:
			return [1,0]
	return None	

for ientry in range(nentries) :
	if ientry % 10000 == 0 :
		print "processing entry" , ientry, "out of", nentries
	#print "Calling get entry ientry=" + str(ientry)
	c.GetEntry(ientry)
	if (madHTgt is not None and c.madHT < madHTgt) or (madHTlt is not None and c.madHT > madHTlt):
		histList["HT"].Fill(c.HT)
		continue
	weight = c.CrossSection
	histList["HT"].Fill(c.HT)
	# two muons
	i=1
	#muons, muonsCharges = passedLep(c.Muons, c.Muons_MiniIso, c.Muons_tightID, 2.4, c.Muons_charge)
	#elecs, elecCharges = passedLep(c.Electrons, c.Electrons_MiniIso, c.Electrons_tightID, 2.5, c.Electrons_charge)
	muons = twoMuons(c)
	#2mu
	if muons is None:# and len(elecs) == 0:
		continue
	cutValues[i] += 1
	i +=1
	l1 = c.Muons[muons[0]]
	l2 = c.Muons[muons[1]]
	#leplepPt
	if not (l1.Pt() > 5 and l1.Pt() < 30):
		continue
	cutValues[i] += 1
	i += 1
	#pt5sublep
	if not l2.Pt() > 5:
		continue
	cutValues[i] += 1
	i +=1
	#opposite-sign
	if not (c.Muons_charge[0] * c.Muons_charge[1] < 1):
		continue
	cutValues[i] += 1
	i +=1
	#dilepPt
	if not (l1 + l2).Pt() > 3:
		continue
	cutValues[i] += 1
	i +=1
	#Mll>4
	invMass = (l1 + l2).M()
	if not invMass > 4:
		continue
	cutValues[i] += 1
	i +=1
	#Mll<50
	if not invMass < 50:
		continue
	cutValues[i] += 1
	i +=1
	#Upsilon_veto
	#Mll veto [9,10.5]
	if (invMass > 9 and invMass < 10.5):
		continue		
	cutValues[i] += 1
	i +=1
	#lowMET
	pt3 = analysis_tools.pt3(l1.Pt(),l1.Phi(),l2.Pt(),l2.Phi(),c.MET,c.METPhi) 
	if not (c.MET > 250 and pt3 > 250):
		continue
	cutValues[i] += 1
	i +=1
	
	#HT
	HT = analysis_ntuples.htJet25(c)
	if not (HT - l1.Pt() - l2.Pt() > 100):
		continue
	cutValues[i] += 1
	i +=1
	
	#METovHT
	if not ((c.MET / HT) > (2.0/3.0) and (c.MET / HT) < 1.4):
		continue
	cutValues[i] += 1
	i +=1
	
	#bveto
	nj, btags, ljet = analysis_ntuples.numberOfJets25Pt2_4Eta_Loose2(c)
	if not (btags == 0):
		continue
	cutValues[i] += 1
	i +=1
	
	#mtautau
	mtautau = analysis_tools.PreciseMtautau(c.MET, c.METPhi, l1, l2)
	if not (mtautau < 0. or mtautau > 160.):
		continue
	cutValues[i] += 1
	i +=1
	#MT
	mt1 = analysis_tools.MT2(c.MET, c.METPhi, l1)
	mt2 = analysis_tools.MT2(c.MET, c.METPhi, l2)
	if not (mt1 < 70.0 and mt2 < 70.0):
		continue
	cutValues[i] += 1
	i +=1
	
# 	if nj >= 1:
# 		cutValues[i] += 1
# 		i +=1
# 		if DileptonLepCorMET(c):
# 			cutValues[i] += 1
# 			i +=1
# 			if c.HT > 100:
# 				cutValues[i] += 1
# 				i +=1
# 				metDHt = c.MET / c.HT
# 				if metDHt > 0.6 and metDHt < 1.4:
# 					cutValues[i] += 1
# 					i +=1
# 					if btags == 0:
# 						cutValues[i] += 1
# 						i +=1
# 						pt = TLorentzVector()
# 						pt.SetPtEtaPhiE(c.MET,0,c.METPhi,c.MET)
# 						mtautau = analysis_tools.Mtautau(pt, l1, l2)
# 						if not (mtautau > 0 and mtautau < 160):
# 							cutValues[i] += 1
# 							i +=1
# 							mt1 = analysis_tools.MT(c.MET, pt, l1)
# 							mt2 = analysis_tools.MT(c.MET, pt, l2)
# 							if mt1 < 70 and mt2 < 70:
# 								cutValues[i] += 1
# 								i +=1
# 								histList["HTWeight"].Fill(c.HT, c.CrossSection)
# 								histList["MDuoLepCanInvMassGT1J"].Fill(invMass, c.CrossSection)
# 								if c.MET > 125 and c.MET < 200:
# 									histList["DuoLepCanInvMassGT1JMET125-200"].Fill(invMass, c.CrossSection)
# 								elif c.MET > 200 and c.MET < 250:
# 									histList["DuoLepCanInvMassGT1JMET200-250"].Fill(invMass, c.CrossSection)
# 								elif c.MET > 250:
# 									histList["DuoLepCanInvMassGT1JMET250"].Fill(invMass, c.CrossSection)
					


#weight = 0.1 * 172004.0 / cutValues[0]
#weight = 10757.0 / 42312.0
#weight = 10757.0 / cutValues[1]
weight = 1

for i, val in enumerate(cutValues):
	print cutNames[i] + " " + str(val * weight)

fnew = TFile(output_file, "recreate")
utils.writeHistograms(histList)
fnew.Close()

exit(0)

#############    END OF SCRIPT    #############