from ROOT import *
import sys
sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import analysis_tools

BTAG_CSV_LOOSE = 0.5426
BTAG_CSV_MEDIUM = 0.8484
BTAG_CSV_LOOSE2 = 0.46

# def printTree(event, pId, space=0):
# 	particle = event.GenParticles[l1]
# 	delim = ""
# 	if space > 0:
# 		delim = "|- "
# 	print ("|  " * space) + delim + str(event.GenParticles_PdgId[pId])+"("+str(particle.E())+","+str(particle.Px())+","+str(particle.Py())+","+str(particle.Pz())")"
# 	if particle.numberOfDaughters() == 0:
# 		return
# 	for p in range(particle.numberOfDaughters()):
# 		printTree(particle.daughter(p), space + 1)


def numberOfJets(event, pt, eta, csv):
	nj = 0
	btags = 0
	leadingJet = None
	for ijet in range(event.Jets.size()):
		jet = event.Jets[ijet]
		if jet.Pt() >= pt and abs(jet.Eta()) <= eta:
			nj +=1
			if leadingJet is None:
				leadingJet = ijet
			elif jet.Pt() > event.Jets[leadingJet].Pt():
				leadingJet = ijet
			if event.Jets_bDiscriminatorCSV[ijet] > csv:
				btags += 1
	return nj, btags, leadingJet

def numberOfJets30Pt2_4Eta_Loose(event):
	return numberOfJets(event, 30, 2.4, BTAG_CSV_LOOSE)

def numberOfJets25Pt2_4Eta_Loose(event):
	return numberOfJets(event, 25, 2.4, BTAG_CSV_LOOSE)

def numberOfJets25Pt2_4Eta_Loose2(event):
	return numberOfJets(event, 25, 2.4, BTAG_CSV_LOOSE2)

def numberOfLooseBTags(event):
	loose = 0
	for ijet in range(event.Jets_bDiscriminatorCSV.size()):
		if event.Jets_bDiscriminatorCSV[ijet] > BTAG_CSV_LOOSE:
			loose+=1
	return loose
	
def htJet25(event):
	leps = [l for l in event.Electrons] + [m for m in event.Muons]
	cleanJets = [ j for j in event.Jets if min(j.DeltaR(l) for l in leps) > 0.4 ]
	objects25 = [ j for j in cleanJets if j.Pt() > 25 ] + leps
	return sum([x.Pt() for x in objects25])

def numberOfMediumBTags(event):
	#./analyzer_x1x2x1.py -bg -i /pnfs/desy.de/cms/tier2/store/user/sbein/CommonNtuples/Summer16.QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_24_RA2AnalysisTree.root -o test.root | tee output
	medium = 0
	for ijet in range(event.Jets_bDiscriminatorCSV.size()):
		if event.Jets_bDiscriminatorCSV[ijet] > BTAG_CSV_MEDIUM:
			jet = event.Jets[ijet]
			if jet.Pt() >= 30 and abs(jet.Eta()) <= 2.4:
				medium+=1
	# if medium != event.BTags:
#  		print "******"
#  		print "Jets= " + str(event.Jets_bDiscriminatorCSV.size()) + " BTags=" + str(event.BTags) + " medium=" + str(medium)
#  		for ijet in range(event.Jets_bDiscriminatorCSV.size()):
#  			print event.Jets_bDiscriminatorCSV[ijet]
	return medium

def isDuoTauEvent(event):
	partSize = event.GenParticles.size()
	if partSize == 0:
		print "No Taus!"
		return False
	nT = 0
	t1 = None
	t2 = None
	for ipart in range(partSize):
		if abs(event.GenParticles_PdgId[ipart]) == 15:
			nT += 1
			if t1 is None:
				t1 = ipart
			else:
				t2 = ipart
	
	# Is this a duo Tau event?
	if nT == 2 and (event.GenParticles_PdgId[t1] * event.GenParticles_PdgId[t2] < 0) and event.GenParticles_ParentId[t1] == 23 and event.GenParticles_ParentId[t2]:
		#print "Mother=" + str(event.GenParticles_ParentId[t1]) + " Mother2=" + str(event.GenParticles_ParentId[t2])
		return True
	return False
	
def isX1X2X1Process(event):
	partSize = event.GenParticles.size()
	for ipart in range(partSize):
		if event.GenParticles_PdgId[ipart] == 1000022:
			#print "Found x10"
			if event.GenParticles_ParentId[ipart] == 1000023:
				#print "Mother x20"
				if not analysis_tools.isSusy(event.GenParticles_ParentId[event.GenParticles_ParentIdx[ipart]]):
					#print "Found!!!"
					return True
	return False	
		