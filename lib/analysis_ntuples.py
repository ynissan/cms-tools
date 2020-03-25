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

triggerIndeces = {}
triggerIndeces['MhtMet6pack'] = [124,109,110,111,112,114,115,116]#123
triggerIndeces['SingleMuon'] = [49,50,65]
triggerIndeces['SingleElectron'] = [36,37,39,40]

def passTrig(c,trigname):
    for trigidx in triggerIndeces[trigname]: 
        if c.TriggerPass[trigidx]==1: return True
        #print "Passing trigger %s, index:%s"%(c.TriggerNames[trigidx],trigidx)
    return False

def getTrigEffGraph(file, name):
    ttrig = file.Get(name)
    hpass = ttrig.GetPassedHistogram().Clone('hpass')
    htotal = ttrig.GetTotalHistogram().Clone('htotal')
    gtrig = TGraphAsymmErrors(hpass, htotal)
    return gtrig

def minMaxCsv(event, pt):
    minimum = 1
    maximum = 0
    for ijet in range(event.Jets.size()):
        jet = event.Jets[ijet]
        if jet.Pt() >= pt and abs(jet.Eta()) <= 2.4:
            if event.Jets_bDiscriminatorCSV[ijet] >= 0 and event.Jets_bDiscriminatorCSV[ijet] < minimum:
                minimum = event.Jets_bDiscriminatorCSV[ijet]
            if event.Jets_bDiscriminatorCSV[ijet] >= 0 and event.Jets_bDiscriminatorCSV[ijet] > maximum:
                maximum = event.Jets_bDiscriminatorCSV[ijet]
    return minimum, maximum

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
            if event.GetBranchStatus('Jets_bDiscriminatorCSV') and event.Jets_bDiscriminatorCSV[ijet] > csv:
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

def htJet25Leps(event, leps):
	cleanJets = [ j for j in event.Jets if min(j.DeltaR(l) for l in leps) > 0.4 ]
	objects25 = [ j for j in cleanJets if j.Pt() > 25 ] + leps
	return sum([x.Pt() for x in objects25])

def minDeltaPhiMetJets(event, pt, eta):
	jets = [ j for j in event.Jets if j.Pt() > pt and abs(j.Eta()) <= eta ]
	metvec = TLorentzVector()
	metvec.SetPtEtaPhiE(event.MET, 0, event.METPhi, event.MET)
	return min([abs(j.DeltaPhi(metvec)) for j in jets])
	
def minDeltaPhiMhtJets(event, pt, eta):
	jets = [ j for j in event.Jets if j.Pt() > pt and abs(j.Eta()) <= eta ]
	mhtvec = TLorentzVector()
	mhtvec.SetPtEtaPhiE(event.MHT, 0, event.MHTPhi, event.MHT)
	return min([abs(j.DeltaPhi(mhtvec)) for j in jets])

def minDeltaPhiMetJets25Pt2_4Eta(event):
	return minDeltaPhiMetJets(event, 25, 2.4)

def minDeltaPhiMhtJets25Pt2_4Eta(event):
	return minDeltaPhiMhtJets(event, 25, 2.4)
	

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
	
def classifyGenZLeptons(c):
    genZL, genNonZL = [], []
    partSize = c.GenParticles.size()
    #print partSize
    for ipart in range(partSize):
        if c.GenParticles_Status[ipart] == 1 and (abs(c.GenParticles_PdgId[ipart]) == 11 or abs(c.GenParticles_PdgId[ipart]) == 13):
            if c.GenParticles_ParentId[ipart] == 1000023 or c.GenParticles_ParentId[ipart] == 23:
                genZL.append(ipart)
            else:
                genNonZL.append(ipart)
    if len(genZL) != 2 or (abs(c.GenParticles_PdgId[genZL[0]]) != abs(c.GenParticles_PdgId[genZL[1]])) or (c.GenParticles_PdgId[genZL[0]] * c.GenParticles_PdgId[genZL[1]] > 0 ):
        print "****** WOW!"
        print "genZL=" + str(genZL) 
        for i in genZL:
            print "PdgId" + str(i) + "=" + str(c.GenParticles_PdgId[i])
        return None, None
    # if len(genNonZL) == 0:
    # 		print "===="
    # 		print "partSize=" + str(partSize)
    # 		print "genZL=" + str(len(genZL))
    # 		for ipart in range(partSize):
    # 			print c.GenParticles_PdgId[ipart]
    # 		print "===="
        
    return genZL, genNonZL

def minDeltaRGenParticles(l, gens, c):
    min = None
    minCan = None

    for ipart in gens:
        genV = c.GenParticles[ipart]
        deltaR = abs(genV.DeltaR(l))
        if min is None or deltaR < min:
            min = deltaR
            minCan = ipart
    return min, minCan

def minDeltaRLepTracks(l, c):
    return minDeltaLepLeps(l, c.tracks)

def minDeltaLepLeps(lep, leps):
    min, minCan = None, None
    for i, l in enumerate(leps):
        deltaR = abs(lep.DeltaR(l))
        if min is None or deltaR < min:
            min = deltaR
            minCan = i
    return min, minCan


def leadingLepton(c):
    ll = None
    for v in [e for e in c.Electrons] + [m for m in c.Muons]:
        if ll is None:
            ll = v
            continue
        if v.Pt() > ll.Pt():
            ll = v
    return ll

def passed2016BTrigger(t, data=False):
    if not t.globalSuperTightHalo2016Filter: return False
    if not t.HBHENoiseFilter: return False    
    if not t.HBHEIsoNoiseFilter: return False
    if not t.eeBadScFilter: return False      
    if not t.BadChargedCandidateFilter: return False
    if not t.BadPFMuonFilter: return False
    if not t.CSCTightHaloFilter: return False 
    if not t.EcalDeadCellTriggerPrimitiveFilter: return False
    #if data:
    #    if not t.ecalBadCalibReducedExtraFilter: return False
    #    if not t.ecalBadCalibReducedFilter: return False
    return True

def getSingleLeptonAfterSelection(c, leadingJet):
    lep = None
    lepCharge = None
    lepFlavour = None
    nL = 0
    
    for i in range(c.Electrons.size()):
        e = c.Electrons[i]
        if e.Pt() <= 25 and bool(c.Electrons_passIso[i]):
            nL += 1
            if nL > 1:
                return None, None, None
            lep = e
            lepCharge = c.Electrons_charge[i]
            lepFlavour = "Electrons"
    for i in range(c.Muons.size()):
        m = c.Muons[i]
        if m.Pt() <= 25 and m.Pt()>=2 and bool(c.Muons_mediumID[i]) and abs(m.DeltaR(leadingJet)) >= 0.4:
            nL += 1
            if nL > 1:
                return None, None, None
            lep = m
            lepCharge = c.Muons_charge[i]
            lepFlavour = "Muons"
    
    return lep, lepCharge, lepFlavour

def getTwoLeptonsAfterSelection(c, leadingJet):
    leps = []
    lepCharges = []
    lepFlavour = None
    nL = 0
    
    for i in range(c.Electrons.size()):
        e = c.Electrons[i]
        if e.Pt() <= 25 and bool(c.Electrons_passIso[i]):
            nL += 1
            if nL > 2:
                return None, None, None
            leps.append(e)
            lepCharges.append(c.Electrons_charge[i])
            lepFlavour = "Electrons"
    if nL == 1:
        return None, None, None
    if nL == 2:
        if lepCharges[0] * lepCharges[1] > 0:
            return None, None, None
    
    for i in range(c.Muons.size()):
        m = c.Muons[i]
        if m.Pt() <= 25 and m.Pt()>=2 and bool(c.Muons_mediumID[i]) and abs(m.DeltaR(leadingJet)) >= 0.4:
            nL += 1
            if nL > 2:
                return None, None, None
            leps.append(m)
            lepCharges.append(c.Muons_charge[i])
            lepFlavour = "Muons"
    
    if nL != 2 or lepCharges[0] * lepCharges[1] > 0:
        return None, None, None
    
    if leps[0].Pt() < leps[1].Pt():
        leps = [leps[1], leps[0]]
        lepCharges = [lepCharges[1], lepCharges[0]]
    
    return leps, lepCharges, lepFlavour
    
    