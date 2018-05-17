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

cutNames = ["Total", "Dilepton", "Sign", "DileptonPt", "DileptonInvMass", "GT1J", "MetCut", "Ht", "MetDHt", "NoBTags", "MtautauVeto", "Mt"]
cutValues = [0,0,0,0,0,0,0,0,0,0,0,0]
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
		if l.Pt() < 30 and l.Pt() > 5 and abs(l.Eta()) < eta:# and miniIsos[i] < 0.5 and miniIsos[i] * l.Pt() < 5:
			passed += 1
			passedMuons.append(l)
			charges.append(lcharges[i])
	return passedMuons, charges

def muonAcceptence(c):
	#and c.Muons_charge[0] * c.Muons_charge[1] < 0
	return passedLep(c.Muons, c.Muons_MiniIso, c.Muons_tightID, 2.4, c) #and passedLep(c.Electrons, c.Electrons_MiniIso, c.Electrons_tightID, 2.5) == 0

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
	muons, muonsCharges = passedLep(c.Muons, c.Muons_MiniIso, c.Muons_tightID, 2.4, c.Muons_charge)
	elecs, elecCharges = passedLep(c.Electrons, c.Electrons_MiniIso, c.Electrons_tightID, 2.5, c.Electrons_charge)
	if len(muons) >= 2:# and len(elecs) == 0:
		cutValues[i] += 1
		i +=1
		l1 = muons[0]
		l2 = muons[1]
		#Ptt > 3
		if muonsCharges[0] * muonsCharges[1] < 0:
			cutValues[i] += 1
			i += 1
			if abs((l1 + l2).Pt()) > 3:
				cutValues[i] += 1
				i +=1
				invMass = (l1 + l2).M()
				# Mll in [4,50]
				if invMass > 4 and invMass < 50:
					#Mll veto [9,10.5]
					if not (invMass > 9 and invMass < 10.5):
						cutValues[i] += 1
						i +=1
						nj, btags, ljet = analysis_ntuples.numberOfJets25Pt2_4Eta_Loose(c)
						#ISR Jet
						if nj >= 1:
							cutValues[i] += 1
							i +=1
							if DileptonLepCorMET(c):
								cutValues[i] += 1
								i +=1
								if c.HT > 100:
									cutValues[i] += 1
									i +=1
									metDHt = c.MET / c.HT
									if metDHt > 0.6 and metDHt < 1.4:
										cutValues[i] += 1
										i +=1
										if btags == 0:
											cutValues[i] += 1
											i +=1
											pt = TLorentzVector()
											pt.SetPtEtaPhiE(c.MET,0,c.METPhi,c.MET)
											mtautau = analysis_tools.Mtautau(pt, l1, l2)
											if not (mtautau > 0 and mtautau < 160):
												cutValues[i] += 1
												i +=1
												mt1 = analysis_tools.MT(c.MET, pt, l1)
												mt2 = analysis_tools.MT(c.MET, pt, l2)
												if mt1 < 70 and mt2 < 70:
													cutValues[i] += 1
													i +=1
													histList["HTWeight"].Fill(c.HT, c.CrossSection)
													histList["MDuoLepCanInvMassGT1J"].Fill(invMass, c.CrossSection)
													if c.MET > 125 and c.MET < 200:
														histList["DuoLepCanInvMassGT1JMET125-200"].Fill(invMass, c.CrossSection)
													elif c.MET > 200 and c.MET < 250:
														histList["DuoLepCanInvMassGT1JMET200-250"].Fill(invMass, c.CrossSection)
													elif c.MET > 250:
														histList["DuoLepCanInvMassGT1JMET250"].Fill(invMass, c.CrossSection)
										


weight = 0.01 * 172004.0 / cutValues[0]
#weight = 209.4 / cutValues[1]

for i in cutValues:
	print cutNames[i] + " " str(i * weight)

fnew = TFile(output_file, "recreate")
utils.writeHistograms(histList)
fnew.Close()

exit(0)

#############    END OF SCRIPT    #############