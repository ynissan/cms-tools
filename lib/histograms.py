#!/usr/bin/python

import sys

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import cuts

commonHistDefs = {
	"MET" : { "name" : "MET", "title" : "MET", "bins" : 100, "minX" : 0, "maxX" : 700, "xAxis" : "GeV" },
	
	"MET1J" : { "name" : "MET1J", "title" : "MET - 1 Jet", "bins" : 100, "minX" : 0, "maxX" : 700, "xAxis" : "GeV" },
	
	"METGT1J" : { "name" : "METGT1J", "title" : "MET >= 1 Jet", "bins" : 100, "minX" : 0, "maxX" : 700, "xAxis" : "GeV" },

	"MET2J" : { "name" : "MET2J", "title" : "MET - 2 Jets", "bins" : 100, "minX" : 0, "maxX" : 700, "xAxis" : "GeV" },
	
	"METDHT" : { "name" : "METDHT", "title" : "MET/HT", "bins" : 100, "minX" : 0, "maxX" : 2, "xAxis" : "GeV" },
	
	"METDHT1J" : { "name" : "METDHT1J", "title" : "MET/HT - 1 Jet", "bins" : 100, "minX" : 0, "maxX" : 2, "xAxis" : "GeV" },
	
	"METDHTGT1J" : { "name" : "METDHTGT1J", "title" : "MET/HT >= 1 Jet", "bins" : 100, "minX" : 0, "maxX" : 2, "xAxis" : "GeV" },

	"METDHT2J" : { "name" : "MET2J", "title" : "MET/HT - 2 Jets", "bins" : 100, "minX" : 0, "maxX" : 2, "xAxis" : "GeV" },
	
	"MT" : { "name" : "MT", "title" : "MT", "bins" : 100, "minX" : 0, "maxX" : 700, "xAxis" : "GeV" },
	
	"MT1J" : { "name" : "MT1J", "title" : "MT - 1 Jet", "bins" : 100, "minX" : 0, "maxX" : 700, "xAxis" : "GeV" },
	
	"MTGT1J" : { "name" : "MTGT1J", "title" : "MT >= 1 Jet", "bins" : 100, "minX" : 0, "maxX" : 700, "xAxis" : "GeV" },

	"MT2J" : { "name" : "MT2J", "title" : "MT - 2 Jets", "bins" : 100, "minX" : 0, "maxX" : 700, "xAxis" : "GeV" },
	
	### MTauTau ###
	
	"MTauTau" : { "name" : "MTauTau", "title" : "M_{#tau#tau}", "bins" : 100, "minX" : -1, "maxX" : 500, "xAxis" : "GeV" },
	
	"MTauTau1J" : { "name" : "MTauTau1J", "title" : "M_{#tau#tau} - 1 Jet", "bins" : 100, "minX" : -1, "maxX" : 500, "xAxis" : "GeV" },
	
	"MTauTauGT1J" : { "name" : "MTauTauGT1J", "title" : "M_{#tau#tau} >= 1 Jet", "bins" : 100, "minX" : -1, "maxX" : 500, "xAxis" : "GeV" },

	"MTauTau2J" : { "name" : "MTauTau2J", "title" : "M_{#tau#tau} - 2 Jets", "bins" : 100, "minX" : -1, "maxX" : 500, "xAxis" : "GeV" },
	
	"MTauTauGenLep" : { "name" : "MTauTauGenLep", "title" : "M_{#tau#tau} - Gen Lep", "bins" : 100, "minX" : -1, "maxX" : 500, "xAxis" : "GeV" },
	
	"MTauTauGenLepNeu" : { "name" : "MTauTauGenLepNeu", "title" : "M_{#tau#tau} - Gen Lep Neu", "bins" : 100, "minX" : -1, "maxX" : 500, "xAxis" : "GeV" },
	
	###############
	
	"HT" : { "name" : "HT", "title" : "HT", "bins" : 100, "minX" : 0, "maxX" : 5000, "noScale" : True, "xAxis" : "GeV" },

	"HTWeight" : { "name" : "HTWeight", "title" : "HT Weighted", "bins" : 100, "minX" : 0, "maxX" : 5000, "xAxis" : "GeV" },
	
	"HT1J" : { "name" : "HT1J", "title" : "HT - 1 Jet", "bins" : 100, "minX" : 0, "maxX" : 5000, "xAxis" : "GeV" },
	
	"HTGT1J" : { "name" : "HTGT1J", "title" : "HT >= 1 Jet", "bins" : 100, "minX" : 0, "maxX" : 5000, "xAxis" : "GeV" },
	
	"HT2J" : { "name" : "HT2J", "title" : "HT - 2 Jets", "bins" : 100, "minX" : 0, "maxX" : 5000, "xAxis" : "GeV" },

	"NJ" : { "name" : "NJ", "title" : "Number of Jets", "bins" : 10, "minX" : 0, "maxX" : 10 },

	"NLGen" : { "name" : "NLGen", "title" : "Number of Generated Leptons", "bins" : 10, "minX" : 0, "maxX" : 10 },
	
	"NLCan" : { "name" : "NLCan", "title" : "Number of Candidate Leptons", "bins" : 10, "minX" : 0, "maxX" : 10 },
	
	"DuoLepPt" : { "name" : "DuoLepPt", "title" : "Dilepton Pt", "bins" : 50,
			       "minX" : 0, "maxX" : 300, "xAxis" : "GeV" },
	
	"DuoLepPt1J" : { "name" : "DuoLepPt1J", "title" : "Dilepton Pt - 1 Jet",
				 "bins" : 50, "minX" : 0, "maxX" : 300, "xAxis" : "GeV" },
	
	"DuoLepPtGT1J" : { "name" : "DuoLepPtGT1J", "title" : "Dilepton Pt >= 1 Jet",
				 "bins" : 50, "minX" : 0, "maxX" : 300, "xAxis" : "GeV" },
	
	"DuoLepPt2J" : { "name" : "DuoLepPt2J", "title" : "Dilepton Pt - 2 Jets",
				 "bins" : 50, "minX" : 0, "maxX" : 300, "xAxis" : "GeV" },

	"DuoLepCanInvMass" : { "name" : "DuoLepCanInvMass", "title" : "Invariant Mass - Dilepton Candidates", "bins" : 50,
			       "minX" : 0, "maxX" : 100, "xAxis" : "GeV" },
	
	"DuoLepCanInvMass1J" : { "name" : "DuoLepCanInvMass1J", "title" : "Invariant Mass - Dilepton Candidates - 1 Jet",
				 "bins" : 50, "minX" : 0, "maxX" : 100, "xAxis" : "GeV" },
	
	"DuoLepCanInvMassGT1J" : { "name" : "DuoLepCanInvMassGT1J", "title" : "Invariant Mass - Dilepton Candidates >= 1 Jet",
				 "bins" : 50, "minX" : 0, "maxX" : 100, "xAxis" : "GeV" },
	
	"DuoLepCanInvMass2J" : { "name" : "DuoLepCanInvMass2J", "title" : "Invariant Mass - Dilepton Candidates - 2 Jets",
				 "bins" : 50, "minX" : 0, "maxX" : 100, "xAxis" : "GeV" },
	
	"DuoLepCanInvMassMET125-200" : { "name" : "DuoLepCanInvMassMET125-200", "title" : "Invariant Mass - Dilepton Candidates, 125 < MET < 200", "bins" : 4,
			       "binsArr" : [4,10,20,30,50], "xAxis" : "GeV" },
	
	"DuoLepCanInvMass1JMET125-200" : { "name" : "DuoLepCanInvMass1JMET125-200", "title" : "Invariant Mass - Dilepton Candidates - 1 Jet, 125 < MET < 200",
				 "bins" : 4,  "binsArr" : [4,10,20,30,50], "xAxis" : "GeV" },
	
	"DuoLepCanInvMassGT1JMET125-200" : { "name" : "DuoLepCanInvMassGT1JMET125-200", "title" : "Invariant Mass - Dilepton Candidates >= 1 Jet, 125 < MET < 200",
				 "bins" : 4,  "binsArr" : [4,10,20,30,50], "xAxis" : "GeV" },
	
	"DuoLepCanInvMass2JMET125-200" : { "name" : "DuoLepCanInvMass2JMET125-200", "title" : "Invariant Mass - Dilepton Candidates - 2 Jets, 125 < MET < 200",
				 "bins" : 4,  "binsArr" : [4,10,20,30,50], "xAxis" : "GeV" },
				 
	"DuoLepCanInvMassMET200-250" : { "name" : "DuoLepCanInvMassMET200-250", "title" : "Invariant Mass - Dilepton Candidates, 200 < MET < 250", "bins" : 4,
			       "binsArr" : [4,10,20,30,50], "xAxis" : "GeV" },
	
	"DuoLepCanInvMass1JMET200-250" : { "name" : "DuoLepCanInvMass1JMET200-250", "title" : "Invariant Mass - Dilepton Candidates - 1 Jet, 200 < MET < 250",
				 "bins" : 4,  "binsArr" : [4,10,20,30,50], "xAxis" : "GeV" },
	
	"DuoLepCanInvMassGT1JMET200-250" : { "name" : "DuoLepCanInvMassGT1JMET200-250", "title" : "Invariant Mass - Dilepton Candidates >= 1 Jet, 200 < MET < 250",
				 "bins" : 4,  "binsArr" : [4,10,20,30,50], "xAxis" : "GeV" },
	
	"DuoLepCanInvMass2JMET200-250" : { "name" : "DuoLepCanInvMass2JMET200-250", "title" : "Invariant Mass - Dilepton Candidates - 2 Jets, 200 < MET < 250",
				 "bins" : 4,  "binsArr" : [4,10,20,30,50], "xAxis" : "GeV" },
				 
	"DuoLepCanInvMassMET250" : { "name" : "DuoLepCanInvMassMET250", "title" : "Invariant Mass - Dilepton Candidates, MET > 250", "bins" : 4,
			       "binsArr" : [4,10,20,30,50], "xAxis" : "GeV" },
	
	"DuoLepCanInvMass1JMET250" : { "name" : "DuoLepCanInvMass1JMET250", "title" : "Invariant Mass - Dilepton Candidates - 1 Jet, MET > 250",
				 "bins" : 4,  "binsArr" : [4,10,20,30,50], "xAxis" : "GeV" },
	
	"DuoLepCanInvMassGT1JMET250" : { "name" : "DuoLepCanInvMassGT1JMET250", "title" : "Invariant Mass - Dilepton Candidates >= 1 Jet, MET > 250",
				 "bins" : 4,  "binsArr" : [4,10,20,30,50], "xAxis" : "GeV" },
	
	"DuoLepCanInvMass2JMET250" : { "name" : "DuoLepCanInvMass2JMET250", "title" : "Invariant Mass - Dilepton Candidates - 2 Jets, MET > 250",
				 "bins" : 4,  "binsArr" : [4,10,20,30,50], "xAxis" : "GeV" },
				 
	"EDuoLepCanInvMass" : { "name" : "EDuoLepCanInvMass", "title" : "Invariant Mass - Di Electrons Candidates", "bins" : 100,
			       "minX" : 0, "maxX" : 70, "xAxis" : "GeV" },
	
	"EDuoLepCanInvMass1J" : { "name" : "EDuoLepCanInvMass1J", "title" : "Invariant Mass - Di Electrons Candidates - 1 Jet",
				 "bins" : 50, "minX" : 0, "maxX" : 70, "xAxis" : "GeV" },
				 
	"EDuoLepCanInvMassGT1J" : { "name" : "EDuoLepCanInvMassGT1J", "title" : "Invariant Mass - Di Electrons Candidates >= 1 Jet",
				 "bins" : 50, "minX" : 0, "maxX" : 70, "xAxis" : "GeV" },
	
	"EDuoLepCanInvMass2J" : { "name" : "EDuoLepCanInvMass2J", "title" : "Invariant Mass - Di Electrons Candidates - 2 Jets",
				 "bins" : 50, "minX" : 0, "maxX" : 70, "xAxis" : "GeV" },
	
	"MDuoLepCanInvMass" : { "name" : "EDuoLepCanInvMass", "title" : "Invariant Mass - Di Muons Candidates", "bins" : 50,
			       "minX" : 0, "maxX" : 70, "xAxis" : "GeV" },
	
	"MDuoLepCanInvMass1J" : { "name" : "EDuoLepCanInvMass1J", "title" : "Invariant Mass - Di Muons Candidates - 1 Jet",
				 "bins" : 50, "minX" : 0, "maxX" : 70, "xAxis" : "GeV" },
				 
	"MDuoLepCanInvMassGT1J" : { "name" : "MDuoLepCanInvMassGT1J", "title" : "Invariant Mass - Di Muons Candidates >= 1 Jet",
				 "bins" : 50, "minX" : 0, "maxX" : 70, "xAxis" : "GeV" },
	
	"MDuoLepCanInvMass2J" : { "name" : "EDuoLepCanInvMass2J", "title" : "Invariant Mass - Di Muons Candidates - 2 Jets",
				 "bins" : 50, "minX" : 0, "maxX" : 70, "xAxis" : "GeV" },

	#"DeltaPhiGen" : { "name" : "DeltaPhiGen", "title" : "Delta Phi - Generated Dileptons", "bins" : 100, "minX" : -4, "maxX" : 4 },
	
	#"DeltaRGen" : { "name" : "DeltaRGen", "title" : "Delta R - Generated Dileptons", "bins" : 100, "minX" : 0, "maxX" : 4 },
	
	#"DeltaEtaGen" : { "name" : "DeltaEtaGen", "title" : "Delta Eta - Generated Dileptons", "bins" : 100, "minX" : 0, "maxX" : 4 },
	
	"DeltaPhiCan" : { "name" : "DeltaPhiCan", "title" : "Delta Phi - Candidate Dileptons", "bins" : 50, "minX" : 0, "maxX" : 3.142 },
	
	"DeltaRCan" : { "name" : "DeltaRCan", "title" : "Delta R - Candidate Dileptons", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"DeltaEtaCan" : { "name" : "DeltaEtaCan", "title" : "Delta Eta - Candidate Dileptons", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"DeltaPhiCan1J" : { "name" : "DeltaPhiCan1J", "title" : "Delta Phi - Candidate Dileptons - 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 3.142 },
	
	"DeltaPhiCanGT1J" : { "name" : "DeltaPhiCanGT1J", "title" : "Delta Phi - Candidate Dileptons >= 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 3.142 },
	
	"DeltaRCan1J" : { "name" : "DeltaRCan1J", "title" : "Delta R - Candidate Dileptons - 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"DeltaRCanGT1J" : { "name" : "DeltaRCanGT1J", "title" : "Delta R - Candidate Dileptons >= 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"DeltaEtaCan1J" : { "name" : "DeltaEtaCan1J", "title" : "Delta Eta - Candidate Dileptons - 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"DeltaEtaCanGT1J" : { "name" : "DeltaEtaCanGT1J", "title" : "Delta Eta - Candidate Dileptons >= 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"DeltaPhiCan2J" : { "name" : "DeltaPhiCan2J", "title" : "Delta Phi - Candidate Dileptons - 2 Jets", "bins" : 50, "minX" : 0, "maxX" : 3.142 },
	
	"DeltaRCan2J" : { "name" : "DeltaRCan2J", "title" : "Delta R - Candidate Dileptons - 2 Jets", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"DeltaEtaCan2J" : { "name" : "DeltaEtaCan2J", "title" : "Delta Eta - Candidate Dileptons - 2 Jets", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	# LEADING JET
	
	"DeltaEtaLeadingJet" : { "name" : "DeltaEtaLeadingJet", "title" : "Delta Eta - Leading Jet Dileptons", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"DeltaEtaLeadingJet1J" : { "name" : "DeltaEtaLeadingJet1J", "title" : "Delta Eta - Leading Jet Dileptons - 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"DeltaEtaLeadingJetGT1J" : { "name" : "DeltaEtaLeadingJetGT1J", "title" : "Delta Eta - Leading Jet Dileptons >= 1 Jets", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"DeltaEtaLeadingJet2J" : { "name" : "DeltaEtaLeadingJet2J", "title" : "Delta Eta - Leading Jet Dileptons - 2 Jets", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"LeadingJetPartonFlavor" : { "name" : "LeadingJetPartonFlavor", "title" : "Leading Jet Parton Flavor", "bins" : 31, "minX" : -7, "maxX" : 23 },
	
	"LeadingJetPartonFlavor1J" : { "name" : "LeadingJetPartonFlavor1J", "title" : "Leading Jet Parton Flavor - 1 Jet", "bins" : 31, "minX" : -7, "maxX" : 23 },
	
	"LeadingJetPartonFlavorGT1J" : { "name" : "LeadingJetPartonFlavorGT1J", "title" : "Leading Jet Parton Flavor >= 1 Jets", "bins" : 31, "minX" : -7, "maxX" : 23 },
	
	"LeadingJetPartonFlavor2J" : { "name" : "LeadingJetPartonFlavor2J", "title" : "Leading Jet Parton Flavor - 2 Jets", "bins" : 31, "minX" : -7, "maxX" : 23 },
	
	"LeadingJetQgLikelihood" : { "name" : "LeadingJetQgLikelihood", "title" : "Leading Jet QG Likelihood", "bins" : 80, "minX" : -1, "maxX" : 1 },
	
	"LeadingJetQgLikelihood1J" : { "name" : "LeadingJetQgLikelihood1J", "title" : "Leading Jet QG Likelihood - 1 Jet", "bins" : 80, "minX" : -1, "maxX" : 1 },
	
	"LeadingJetQgLikelihoodGT1J" : { "name" : "LeadingJetQgLikelihoodGT1J", "title" : "Leading Jet QG Likelihood >= 1 Jets", "bins" : 80, "minX" : -1, "maxX" : 1 },
	
	"LeadingJetQgLikelihood2J" : { "name" : "LeadingJetQgLikelihood2J", "title" : "Leading Jet QG Likelihood - 2 Jets", "bins" : 80, "minX" : -1, "maxX" : 1 },
	
	
	
	
	#ELECTRONS
	
	"EDeltaPhiCan" : { "name" : "EDeltaPhiCan", "title" : "Delta Phi - Candidate Di Electrons", "bins" : 50, "minX" : 0, "maxX" : 3.142 },
	
	"EDeltaRCan" : { "name" : "EDeltaRCan", "title" : "Delta R - Candidate Di Electrons", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"EDeltaEtaCan" : { "name" : "EDeltaEtaCan", "title" : "Delta Eta - Candidate Di Electrons", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"EDeltaPhiCan1J" : { "name" : "EDeltaPhiCan1J", "title" : "Delta Phi - Candidate Di Electrons - 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 3.142 },
	
	"EDeltaPhiCanGT1J" : { "name" : "EDeltaPhiCanGT1J", "title" : "Delta Phi - Candidate Di Electrons >= 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 3.142 },
	
	"EDeltaRCan1J" : { "name" : "EDeltaRCan1J", "title" : "Delta R - Candidate Di Electrons - 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"EDeltaEtaCan1J" : { "name" : "EDeltaEtaCan1J", "title" : "Delta Eta - Candidate Di Electrons - 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"EDeltaRCanGT1J" : { "name" : "EDeltaRCanGT1J", "title" : "Delta R - Candidate Di Electrons >= 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"EDeltaEtaCanGT1J" : { "name" : "EDeltaEtaCanGT1J", "title" : "Delta Eta - Candidate Di Electrons >= 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"EDeltaPhiCan2J" : { "name" : "EDeltaPhiCan2J", "title" : "Delta Phi - Candidate Di Electrons - 2 Jets", "bins" : 50, "minX" : 0, "maxX" : 3.142 },
	
	"EDeltaRCan2J" : { "name" : "EDeltaRCan2J", "title" : "Delta R - Candidate Di Electrons - 2 Jets", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"EDeltaEtaCan2J" : { "name" : "EDeltaEtaCan2J", "title" : "Delta Eta - Candidate Di Electrons - 2 Jets", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	#MUONS
	
	"MDeltaPhiCan" : { "name" : "MDeltaPhiCan", "title" : "Delta Phi - Candidate Di Muons", "bins" : 50, "minX" : 0, "maxX" : 3.142 },
	
	"MDeltaRCan" : { "name" : "MDeltaRCan", "title" : "Delta R - Candidate Di Muons", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"MDeltaEtaCan" : { "name" : "MDeltaEtaCan", "title" : "Delta Eta - Candidate Di Muons", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"MDeltaPhiCan1J" : { "name" : "MDeltaPhiCan1J", "title" : "Delta Phi - Candidate Di Muons - 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 3.142 },
	
	"MDeltaRCan1J" : { "name" : "MDeltaRCan1J", "title" : "Delta R - Candidate Di Muons - 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"MDeltaEtaCan1J" : { "name" : "MDeltaEtaCan1J", "title" : "Delta Eta - Candidate Di Muons - 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"MDeltaPhiCanGT1J" : { "name" : "MDeltaPhiCanGT1J", "title" : "Delta Phi - Candidate Di Muons >= 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 3.142 },
	
	"MDeltaRCanGT1J" : { "name" : "MDeltaRCanGT1J", "title" : "Delta R - Candidate Di Muons >= 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"MDeltaEtaCanGT1J" : { "name" : "MDeltaEtaCanGT1J", "title" : "Delta Eta - Candidate Di Muons >= 1 Jet", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"MDeltaPhiCan2J" : { "name" : "MDeltaPhiCan2J", "title" : "Delta Phi - Candidate Di Muons - 2 Jets", "bins" : 50, "minX" : 0, "maxX" : 3.142 },
	
	"MDeltaRCan2J" : { "name" : "MDeltaRCan2J", "title" : "Delta R - Candidate Di Muons - 2 Jets", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	"MDeltaEtaCan2J" : { "name" : "MDeltaEtaCan2J", "title" : "Delta Eta - Candidate Di Muons - 2 Jets", "bins" : 50, "minX" : 0, "maxX" : 4 },
	
	#####

	"DeltaRLepMatchCand" : { "name" : "DeltaRLepMatchCand", "title" : "Delta R - Lepton and Match", "bins" : 50, "minX" : 0, "maxX" : 1 },

	"MatchLep" : { "name" : "MatchLep", "title" : "Matched Lepton", "bins" : 2, "minX" : 0, "maxX" : 2 },
	
	"LPT" : { "name" : "LPT", "title" : "Lepton Pt", "bins" : 150, "minX" : 0, "maxX" : 200, "xAxis" : "GeV" },
	
	"LPT1J" : { "name" : "LPT1J", "title" : "Lepton Pt - Dilepton - 1 Jet", "bins" : 150, "minX" : 0, "maxX" : 200, "xAxis" : "GeV" },
	
	"LPTGT1J" : { "name" : "LPTGT1J", "title" : "Lepton Pt - Dilepton >= 1 Jet", "bins" : 150, "minX" : 0, "maxX" : 200, "xAxis" : "GeV" },
	
	"LPT2J" : { "name" : "LPT2J", "title" : "Lepton Pt - Dilepton - 2 Jets", "bins" : 150, "minX" : 0, "maxX" : 200, "xAxis" : "GeV" },
	
	"LEta" : { "name" : "LEta", "title" : "Lepton Eta", "bins" : 100, "minX" : -5, "maxX" : 5 },
	
	"LEta1J" : { "name" : "LEta1J", "title" : "Lepton Eta - 1 Jet", "bins" : 100, "minX" : -5, "maxX" : 5 },
	
	"LEta2J" : { "name" : "LEta2J", "title" : "Lepton Eta - 2 Jets", "bins" : 100, "minX" : -5, "maxX" : 5 },
	
	"LEtaGT1J" : { "name" : "LEtaGT1J", "title" : "Lepton Eta >= 1 Jet", "bins" : 100, "minX" : -5, "maxX" : 5 },
	
	"LPhi" : { "name" : "LPhi", "title" : "Lepton Phi", "bins" : 100, "minX" : -7, "maxX" : 7 },
	
	"LPhi1J" : { "name" : "LPhi1J", "title" : "Lepton Phi - 1 Jet", "bins" : 100, "minX" : -7, "maxX" : 7 },
	
	"LPhiGT1J" : { "name" : "LPhiGT1J", "title" : "Lepton Phi >= 1 Jet", "bins" : 100, "minX" : -7, "maxX" : 7 },
	
	"LPhi2J" : { "name" : "LPhi2J", "title" : "Lepton Phi - 2 Jets", "bins" : 100, "minX" : -7, "maxX" : 7 },
	
	"EPT" : { "name" : "EPT", "title" : "Electron Pt", "bins" : 150, "minX" : 0, "maxX" : 200, "xAxis" : "GeV" },
	
	"EPT1J" : { "name" : "EPT1J", "title" : "Electron Pt - Dilepton - 1 Jet", "bins" : 150, "minX" : 0, "maxX" : 200, "xAxis" : "GeV" },
	
	"EPTGT1J" : { "name" : "EPTGT1J", "title" : "Electron Pt - Dilepton >= 1 Jet", "bins" : 150, "minX" : 0, "maxX" : 200, "xAxis" : "GeV" },
	
	"EPT2J" : { "name" : "EPT2J", "title" : "Electron Pt - Dilepton - 2 Jets", "bins" : 150, "minX" : 0, "maxX" : 200, "xAxis" : "GeV" },
	
	"EEta" : { "name" : "EEta", "title" : "Electron Eta", "bins" : 150, "minX" : -5, "maxX" : 5 },
	
	"EEta1J" : { "name" : "EEta1J", "title" : "Electron Eta - 1 Jet", "bins" : 150, "minX" : -5, "maxX" : 5 },
	
	"EEtaGT1J" : { "name" : "EEtaGT1J", "title" : "Electron Eta >= 1 Jet", "bins" : 150, "minX" : -5, "maxX" : 5 },
	
	"EEta2J" : { "name" : "EEta2J", "title" : "Electron Eta - 2 Jets", "bins" : 150, "minX" : -5, "maxX" : 5 },
	
	"EPhi" : { "name" : "EPhi", "title" : "Electron Phi", "bins" : 150, "minX" : -7, "maxX" : 7 },
	
	"EPhi1J" : { "name" : "EPhi1J", "title" : "Electron Phi - 1 Jet", "bins" : 150, "minX" : -7, "maxX" : 7 },
	
	"EPhiGT1J" : { "name" : "EPhiGT1J", "title" : "Electron Phi >= 1 Jet", "bins" : 150, "minX" : -7, "maxX" : 7 },
	
	"EPhi2J" : { "name" : "EPhi2J", "title" : "Electron Phi - 2 Jets", "bins" : 150, "minX" : -7, "maxX" : 7 },
	
	"MPT" : { "name" : "MPT", "title" : "Muon Pt", "bins" : 150, "minX" : 0, "maxX" : 200, "xAxis" : "GeV" },
	
	"MPT1J" : { "name" : "MPT1J", "title" : "Muon Pt - Dilepton - 1 Jet", "bins" : 150, "minX" : 0, "maxX" : 200, "xAxis" : "GeV" },
	
	"MPTGT1J" : { "name" : "MPTGT1J", "title" : "Muon Pt - Dilepton >= 1 Jet", "bins" : 150, "minX" : 0, "maxX" : 200, "xAxis" : "GeV" },
	
	"MPT2J" : { "name" : "MPT2J", "title" : "Muon Pt - Dilepton - 2 Jets", "bins" : 150, "minX" : 0, "maxX" : 200, "xAxis" : "GeV" },
	
	"MEta" : { "name" : "MEta", "title" : "Muon Eta", "bins" : 150, "minX" : -5, "maxX" : 5 },
	
	"MEta1J" : { "name" : "MEta1J", "title" : "Muon Eta - 1 Jet", "bins" : 150, "minX" : -5, "maxX" : 5 },
	
	"MEtaGT1J" : { "name" : "MEtaGT1J", "title" : "Muon Eta >= 1 Jet", "bins" : 150, "minX" : -5, "maxX" : 5 },
	
	"MEta2J" : { "name" : "MEta2J", "title" : "Muon Eta - 2 Jets", "bins" : 150, "minX" : -5, "maxX" : 5 },
	
	"MPhi" : { "name" : "MPhi", "title" : "Muon Phi", "bins" : 100, "minX" : -7, "maxX" : 7 },
	
	"MPhi1J" : { "name" : "MPhi1J", "title" : "Muon Phi - 1 Jet", "bins" : 100, "minX" : -7, "maxX" : 7 },
	
	"MPhiGT1J" : { "name" : "MPhiGT1J", "title" : "Muon Phi >= 1 Jet", "bins" : 100, "minX" : -7, "maxX" : 7 },
	
	"MPhi2J" : { "name" : "MPhi2J", "title" : "Muon Phi - 2 Jets", "bins" : 100, "minX" : -7, "maxX" : 7 }
	
}

genHistDefs = {
	"InvMassGen" : { "name" : "InvMassGen", "title" : "Generated Products Invariant Mass", "bins" : 100, "minX" : 0, "maxX" : 30, "xAxis" : "GeV" },
	
	"X1PT" : { "name" : "X1PT", "title" : "Generated X10 Pt", "bins" : 200, "minX" : 0, "maxX" : 600, "xAxis" : "GeV" },
	
	"X2PT" : { "name" : "X2PT", "title" : "Generated X20 Pt", "bins" : 200, "minX" : 0, "maxX" : 600, "xAxis" : "GeV" }
}

cutsOrder = ["none", "MET125", "BTAGS", "MET125_METDHT_BTAGS", "DILEPTON_DELTA_ETA_1_5", 
	     "DILEPTON_LEPPT_30", "DILEPTON_MTT_0_160", "DILEPTON_DELTA_R_1_5",
	     "ALL", "PAPER"]
cutsDefs = {
	"none" : {"title" : "No Cuts", "histDef" : {}},
	"MET125" : {"title" : "MET >= 125GeV", "histDef" : {
			"MET" : {"minX" : 125, "maxX" : 700},
			"MET1J" : {"minX" : 125, "maxX" : 700},
			"MET2J" : {"minX" : 125, "maxX" : 700}
	
		   }, "once" : True, "params" : { "met" : 125 }, "aod" : [cuts.MetCut], "ntuples" : [cuts.MetCut]},
	
	"BTAGS" : {"title" : "No BTags", "histDef" : {}, "once" : True, "params" : {}, "aod" : [cuts.NoBTags], "ntuples" : [cuts.NoBTags]},
		   
	"MET125_METDHT_BTAGS" : {"title" : "MET >= 125GeV,0.6<MetDHt<1.4,BTags", "histDef" : {
			"MET" : {"minX" : 125, "maxX" : 700},
			"MET1J" : {"minX" : 125, "maxX" : 700},
			"MET2J" : {"minX" : 125, "maxX" : 700},
			"METDHT" : { "minX" : 0.6, "maxX" : 1.4 },
			"METDHT1J" : { "minX" : 0.6, "maxX" : 1.4 },
			"METDHTGT1J" : { "minX" : 0.6, "maxX" : 1.4 },
			"METDHT2J": { "minX" : 0.6, "maxX" : 1.4 },
		   }, "once" : True, "params" : { "met" : 125, "minMetDHt" : 0.6, "maxMetDHt" : 1.4 },
		      "aod" : [cuts.MetCut, cuts.MetDHt, cuts.NoBTags], "ntuples" : [cuts.MetCut, cuts.MetDHt, cuts.NoBTags]},
	
	"DILEPTON_DELTA_ETA_1_5" : {"title" : "Dilepton, Delta Eta <= 1.5, No BTags", "histDef" : {
					"DeltaEtaCan" : {"maxX" : 1.5},
					"DeltaEtaCan1J" : {"maxX" : 1.5},
					"DeltaEtaCanGT1J" : {"maxX" : 1.5},
					"DeltaEtaCan2J" : {"maxX" : 1.5},
					"EDeltaEtaCan" : {"maxX" : 1.5},
					"EDeltaEtaCan1J" : {"maxX" : 1.5},
					"EDeltaEtaCanGT1J" : {"maxX" : 1.5},
					"EDeltaEtaCan2J" : {"maxX" : 1.5},
					"MDeltaEtaCan" : {"maxX" : 1.5},
					"MDeltaEtaCan1J" : {"maxX" : 1.5},
					"MDeltaEtaCanGT1J" : {"maxX" : 1.5},
					"MDeltaEtaCan2J" : {"maxX" : 1.5},
	
				  }, "once" : True, "aod" : [cuts.NoBTags, cuts.DileptonDeltaEta], "ntuples" : [cuts.NoBTags, cuts.DileptonDeltaEta],
				 "params" : { "deltaEta" : 1.5 }},
	"DILEPTON_LEPPT_30" : {"title" : "Dilepton, Lepton Pt <= 30, No BTags", "histDef" : {
				 	"LPT" : {"maxX" : 30},
				 	"LPT1J" : {"maxX" : 30},
				 	"LPTGT1J" : {"maxX" : 30},
				 	"LPT2J" : {"maxX" : 30},
				 	"EPT" : {"maxX" : 30},
				 	"EPT1J" : {"maxX" : 30},
				 	"EPTGT1J" : {"maxX" : 30},
				 	"EPT2J" : {"maxX" : 30},
				 	"MPT" : {"maxX" : 30},
				 	"MPT1J" : {"maxX" : 30},
				 	"MPTGT1J" : {"maxX" : 30},
				 	"MPT2J" : {"maxX" : 30},
				 }, "once" : True,
				 "aod" : [cuts.NoBTags, cuts.Dilepton, cuts.LeptonPt], "ntuples" : [cuts.NoBTags, cuts.Dilepton, cuts.LeptonPt],
				 "params" : { "pt" : 30 }},
	"DILEPTON_MTT_0_160" : {"title" : "Dilepton, MTT veto [0,160], No BTags", "histDef" : {
				 }, "once" : True,
				 "aod" : [cuts.NoBTags, cuts.Dilepton, cuts.MtautauVeto], "ntuples" : [cuts.NoBTags, cuts.Dilepton, cuts.MtautauVeto],
				 "params" : { "mTauTauVeto" : [0,160] }},
	"DILEPTON_DELTA_R_1_5" : {"title" : "Dilepton, Delta R <= 1.5, No BTags", "histDef" : {
				   }, "once" : True,
				    "aod" : [cuts.NoBTags, cuts.DileptonDeltaR], "ntuples" : [cuts.NoBTags, cuts.DileptonDeltaR],
				 "params" : { "deltaR" : 1.5 }},
	"ALL" : {"title" : "Dilepton, MET>=125, Pt<=30, DeltaR<=1.5, DeltaEta<=1.5, No BTags, 0.6<MetDHt<1.4, MT<70, 4<MLL<50 not 9<MLL<10.5, HT>100, ETAM<2.4,ETAE<2.5", "once" : True, 
					     "aod" : [cuts.NoBTags, cuts.DileptonDeltaEta, cuts.DileptonDeltaR, cuts.MetCut, cuts.LeptonPt, 
					     	      cuts.MetDHt, cuts.Mt, cuts.DileptonInvMass, cuts.Ht, cuts.Eta],
					     "ntuples" : [cuts.NoBTags, cuts.DileptonDeltaEta, cuts.DileptonDeltaR, cuts.MetCut, cuts.LeptonPt,
					     		  cuts.MetDHt, cuts.Mt, cuts.DileptonInvMass, cuts.Ht, cuts.Eta],
				 	     "params" : { "pt" : 30, "deltaEta" : 1.5, "deltaR" : 1.5, "deltaPhi" : 1.5, "met" : 125,
				 	     		   "minMetDHt" : 0.6, "maxMetDHt" : 1.4, "mt" : 70,
				 	     		   "invMassMin" : 4, "invMassMax" : 50, "invMassRange" : { "min" : 9, "max" : 10.5 },
				 	     		   "ht" : 100, "etaM" : 2.4, "etaE" : 2.5  },
				 	      "histDef" : {
				 	      		"MET" : {"minX" : 150, "maxX" : 700},
							"MET1J" : {"minX" : 150, "maxX" : 700},
							"METGT1J" : {"minX" : 150, "maxX" : 700},
							"MET2J" : {"minX" : 150, "maxX" : 700},
							"DeltaEtaCan" : {"maxX" : 1.5},
							"DeltaEtaCan1J" : {"maxX" : 1.5},
							"DeltaEtaCanGT1J" : {"maxX" : 1.5},
							"DeltaEtaCan2J" : {"maxX" : 1.5},
							"EDeltaEtaCan" : {"maxX" : 1.5},
							"EDeltaEtaCan1J" : {"maxX" : 1.5},
							"EDeltaEtaCanGT1J" : {"maxX" : 1.5},
							"EDeltaEtaCan2J" : {"maxX" : 1.5},
							"MDeltaEtaCan" : {"maxX" : 1.5},
							"MDeltaEtaCan1J" : {"maxX" : 1.5},
							"MDeltaEtaCanGT1J" : {"maxX" : 1.5},
							"MDeltaEtaCan2J" : {"maxX" : 1.5},
							"LPT" : {"maxX" : 30},
							"LPT1J" : {"maxX" : 30},
							"LPTGT1J" : {"maxX" : 30},
							"LPT2J" : {"maxX" : 30},
							"EPT" : {"maxX" : 30},
							"EPT1J" : {"maxX" : 30},
							"EPTGT1J" : {"maxX" : 30},
							"EPT2J" : {"maxX" : 30},
							"MPT" : {"maxX" : 30},
							"MPT1J" : {"maxX" : 30},
							"MPTGT1J" : {"maxX" : 30},
							"MPT2J" : {"maxX" : 30},
							"METDHT" : { "minX" : 0.6, "maxX" : 1.4},
							"METDHT1J" : {"minX" : 0.6, "maxX" : 1.4},
							"METDHTGT1J" : {"minX" : 0.6, "maxX" : 1.4},
							"METDHT2J" : {"minX" : 0.6, "maxX" : 1.4 },
							"MT" : {"maxX" : 70},
							"MT1J" : {"maxX" : 70},
							"MTGT1J" : {"maxX" : 70},
							"MT2J" : {"maxX" : 70},
				 	      }},
	"PAPER" : {"title" : "PAPER", "once" : True, 
					     "aod" : [cuts.Dilepton, cuts.GT1J, cuts.NoBTags, cuts.MetCut, cuts.DileptonPt, cuts.LeptonPt, 
					     	      cuts.MetDHt, cuts.Mt, cuts.DileptonInvMass, cuts.Ht, cuts.Eta,
					     	      cuts.MtautauVeto, cuts.DileptonLepCorMET],
					    #  "ntuples" : [cuts.Dilepton, cuts.DileptonPt, cuts.DileptonInvMass,
# 					     		  cuts.GT1J, cuts.MetCut, cuts.Ht,
# 					     		  cuts.MetDHt, cuts.NoBTags, cuts.MtautauVeto, 
# 					     		  cuts.Mt, cuts.LeptonPt, cuts.Eta,
# 					     		  cuts.DileptonLepCorMET],
# 					     "ntuples" : [cuts.Dilepton, cuts.DileptonPt, cuts.DileptonInvMass,
# 					     		  cuts.GT1J, cuts.MetCut, cuts.Ht,
# 					     		  cuts.MetDHt, cuts.NoBTags, cuts.MtautauVeto, 
# 					     		  cuts.Mt],
					     "ntuples" : [cuts.TwoMu, cuts.LeplepPt, cuts.Pt5sublep, cuts.OppositeSign,
					     		  cuts.DileptonPt, cuts.DileptonInvMassMin, cuts.DileptonInvMassMax,
					     		  cuts.DileptonInvMassRange,
					     		  cuts.LowMET, cuts.Ht,
					     		  cuts.MetDHt, cuts.NoBTags, cuts.MtautauVeto, 
					     		  cuts.Mt],
# MiniAnalyzer
#["Total", "2mu", "leplepPt", "pt5sublep", "opposite-sign", "dilepPt", "Mll>4", "Mll<50", "Upsilon_veto",
# "lowMET","HT", "METovHT", "bveto", "mtautau", "MT"]
				 	     "params" : { "pt" : 30, "deltaEta" : 1.5, "deltaR" : 1.5, "deltaPhi" : 1.5, "met" : 125,
				 	     		   "minMetDHt" : 2.0/3.0, "maxMetDHt" : 1.4, "mt" : 70.0,
				 	     		   "invMassMin" : 4, "invMassMax" : 50, "invMassRange" : { "min" : 9, "max" : 10.5 },
				 	     		   "ht" : 100, "etaM" : 2.4, "etaE" : 2.5, "dileptonPt" : 3, "mTauTauVeto" : [0.,160.],
				 	     		   "lepCurMet" : 125  },
				 	      "histDef" : {
				 	      		"MET" : {"minX" : 150, "maxX" : 700},
							"MET1J" : {"minX" : 150, "maxX" : 700},
							"METGT1J" : {"minX" : 150, "maxX" : 700},
							"MET2J" : {"minX" : 150, "maxX" : 700},
							"DeltaEtaCan" : {"maxX" : 1.5},
							"DeltaEtaCan1J" : {"maxX" : 1.5},
							"DeltaEtaCanGT1J" : {"maxX" : 1.5},
							"DeltaEtaCan2J" : {"maxX" : 1.5},
							"EDeltaEtaCan" : {"maxX" : 1.5},
							"EDeltaEtaCan1J" : {"maxX" : 1.5},
							"EDeltaEtaCanGT1J" : {"maxX" : 1.5},
							"EDeltaEtaCan2J" : {"maxX" : 1.5},
							"MDeltaEtaCan" : {"maxX" : 1.5},
							"MDeltaEtaCan1J" : {"maxX" : 1.5},
							"MDeltaEtaCanGT1J" : {"maxX" : 1.5},
							"MDeltaEtaCan2J" : {"maxX" : 1.5},
							"LPT" : {"maxX" : 30},
							"LPT1J" : {"maxX" : 30},
							"LPTGT1J" : {"maxX" : 30},
							"LPT2J" : {"maxX" : 30},
							"EPT" : {"maxX" : 30},
							"EPT1J" : {"maxX" : 30},
							"EPTGT1J" : {"maxX" : 30},
							"EPT2J" : {"maxX" : 30},
							"MPT" : {"maxX" : 30},
							"MPT1J" : {"maxX" : 30},
							"MPTGT1J" : {"maxX" : 30},
							"MPT2J" : {"maxX" : 30},
							"METDHT" : { "minX" : 0.6, "maxX" : 1.4},
							"METDHT1J" : {"minX" : 0.6, "maxX" : 1.4},
							"METDHTGT1J" : {"minX" : 0.6, "maxX" : 1.4},
							"METDHT2J" : {"minX" : 0.6, "maxX" : 1.4 },
							"MT" : {"maxX" : 70},
							"MT1J" : {"maxX" : 70},
							"MTGT1J" : {"maxX" : 70},
							"MT2J" : {"maxX" : 70},
				 	      }},
	
}

def getHistDef(definition):
	if definition in commonHistDefs:
		return commonHistDefs[definition]
	if definition in genHistDefs:
		return genHistDefs[definition]
	return None

