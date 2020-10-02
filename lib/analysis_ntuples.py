from ROOT import *
import sys
sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import analysis_tools

BTAG_CSV_LOOSE = 0.5426
BTAG_CSV_MEDIUM = 0.8484
BTAG_CSV_LOOSE2 = 0.46

BTAG_DEEP_CSV_LOOSE = 0.2219
BTAG_DEEP_CSV_MEDIUM = 0.6324

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

def minMaxCsv(jets, jets_bDiscriminatorCSV, pt):
    minimum = 1
    maximum = 0
    for ijet in range(jets.size()):
        jet = jets[ijet]
        if jet.Pt() >= pt and abs(jet.Eta()) <= 2.4:
            if jets_bDiscriminatorCSV[ijet] >= 0 and jets_bDiscriminatorCSV[ijet] < minimum:
                minimum = jets_bDiscriminatorCSV[ijet]
            if jets_bDiscriminatorCSV[ijet] >= 0 and jets_bDiscriminatorCSV[ijet] > maximum:
                maximum = jets_bDiscriminatorCSV[ijet]
    return minimum, maximum

def numberOfJets(jets, jets_bDiscriminatorCSV, pt, eta, csv):
    nj = 0
    btags = 0
    leadingJet = None
    for ijet in range(jets.size()):
        jet = jets[ijet]
        if jet.Pt() >= pt and abs(jet.Eta()) <= eta:
            nj +=1
            if leadingJet is None:
                leadingJet = ijet
            elif jet.Pt() > jets[leadingJet].Pt():
                leadingJet = ijet
            if jets_bDiscriminatorCSV[ijet] > csv:
                btags += 1
    return nj, btags, leadingJet

# def numberOfJets30Pt2_4Eta_Loose(event):
# 	return numberOfJets(event.Jets, event.Jets_bDiscriminatorCSV, 30, 2.4, BTAG_CSV_LOOSE)
# 
# def numberOfJets25Pt2_4Eta_Loose(event):
# 	return numberOfJets(event.Jets, event.Jets_bDiscriminatorCSV, 25, 2.4, BTAG_CSV_LOOSE)
# 
# def numberOfJets25Pt2_4Eta_Loose2(event):
# 	return numberOfJets(event.Jets, event.Jets_bDiscriminatorCSV, 25, 2.4, BTAG_CSV_LOOSE2)

def eventNumberOfJets25Pt2_4Eta_Loose(jets, jets_bDiscriminatorCSV):
    return numberOfJets(jets, jets_bDiscriminatorCSV, 25, 2.4, BTAG_CSV_LOOSE)

def eventNumberOfJets25Pt2_4Eta_Medium(jets, jets_bDiscriminatorCSV):
    return numberOfJets(jets, jets_bDiscriminatorCSV, 25, 2.4, BTAG_CSV_MEDIUM)

def eventNumberOfJets25Pt2_4Eta_DeepLoose(jets, jets_bDiscriminatorCSV):
    return numberOfJets(jets, jets_bDiscriminatorCSV, 25, 2.4, BTAG_DEEP_CSV_LOOSE)
    
def eventNumberOfJets25Pt2_4Eta_DeepMedium(jets, jets_bDiscriminatorCSV):
    return numberOfJets(jets, jets_bDiscriminatorCSV, 25, 2.4, BTAG_DEEP_CSV_MEDIUM)

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

def htJet25Leps(jets, leps):
	cleanJets = [ j for j in jets if min(j.DeltaR(l) for l in leps) > 0.4 ]
	objects25 = [ j for j in cleanJets if j.Pt() > 25 ] + leps
	return sum([x.Pt() for x in objects25])

def minDeltaPhiMetJets(jets, MET, METPhi, pt, eta):
	jets = [ j for j in jets if j.Pt() > pt and abs(j.Eta()) <= eta ]
	metvec = TLorentzVector()
	metvec.SetPtEtaPhiE(MET, 0, METPhi, MET)
	return min([abs(j.DeltaPhi(metvec)) for j in jets])
	
def minDeltaPhiMhtJets(jets, MHT, MHTPhi, pt, eta):
	jets = [ j for j in jets if j.Pt() > pt and abs(j.Eta()) <= eta ]
	mhtvec = TLorentzVector()
	mhtvec.SetPtEtaPhiE(MHT, 0, MHTPhi, MHT)
	return min([abs(j.DeltaPhi(mhtvec)) for j in jets])

def minDeltaPhiMetJets25Pt2_4Eta(event):
    return minDeltaPhiMetJets(event.Jets, event.MET, event.METPhi, 25, 2.4)

def minDeltaPhiMhtJets25Pt2_4Eta(event):
    return minDeltaPhiMhtJets(event.Jets, event.MHT, event.MHTPhi, 25, 2.4)

def eventMinDeltaPhiMetJets25Pt2_4Eta(jets, MET, METPhi):
    return minDeltaPhiMetJets(jets, MET, METPhi, 25, 2.4)

def eventMinDeltaPhiMhtJets25Pt2_4Eta(jets, MHT, MHTPhi):
    return minDeltaPhiMhtJets(jets, MHT, MHTPhi, 25, 2.4)


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

def isLeptonMatchedGen(genParticles, genParticles_PdgId, genL, genNL, lidx, leptons, leptonsCharge, lepSignedPdgId):
    l = leptons[lidx]
    minZ, minCanZ = minDeltaRGenParticles(l, genL, genParticles)
    minNZ, minCanNZ = minDeltaRGenParticles(l, genNL, genParticles)
    min = 0
    if minNZ is None or minZ < minNZ:
        min = minZ
    else:
        min = minNZ
    if min > 0.01:
        return False
    elif minNZ is None or minZ < minNZ:
        if genParticles_PdgId[minCanZ] == lepSignedPdgId * leptonsCharge[lidx]:
            return True
        else:
            return False
    return False

def minDeltaRGenParticles(l, gens, genParticles):
    min = None
    minCan = None

    for ipart in gens:
        genV = genParticles[ipart]
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

def electronPassesKinematicSelection(i, electrons, electrons_deltaRLJ):
    return electrons[i].Pt() <= 25 and electrons_deltaRLJ[i] >= 0.4

def electronPassesLooseSelection(i, electrons, electrons_passIso):
    return bool(electrons_passIso[i])

def electronPassesTightSelection(i, electrons, electrons_passIso, electrons_deltaRLJ):
    #print electrons[i].Pt(), electrons_deltaRLJ[i], electrons_passIso[i], electronPassesLooseSelection(i, electrons, electrons_passIso)
    return electronPassesKinematicSelection(i, electrons, electrons_deltaRLJ) and electronPassesLooseSelection(i, electrons, electrons_passIso)

def muonPassesKinematicSelection(i, muons, muons_deltaRLJ, muonLowerPt = 2):
    #if muonLowerPt<2:
        #print "low pt", muonLowerPt
    return muons[i].Pt()>= muonLowerPt and muons[i].Pt() <= 25 and abs(muons_deltaRLJ[i]) >= 0.4

def muonPassesLooseSelection(i, muons, muons_mediumID, muons_deltaRLJ, muonLowerPt = 2, muonLowerPtTight = False, muons_tightID = None):
    if not muonPassesKinematicSelection(i, muons, muons_deltaRLJ, muonLowerPt):
        return False
    if muons[i].Pt() < 2 and muonLowerPtTight:
        #print "looking for tight!"
        return bool(muons_tightID[i])
    else:
        return bool(muons_mediumID[i])

def muonPassesTightSelection(i, muons, muons_mediumID, muons_passJetIso, muons_deltaRLJ, muonLowerPt = 2, muonLowerPtTight = False, muons_tightID = None):
    return muonPassesLooseSelection(i, muons, muons_mediumID, muons_deltaRLJ, muonLowerPt, muonLowerPtTight, muons_tightID) and bool(muons_passJetIso[i])

def getSingleLeptonAfterSelection(Electrons, Electrons_passJetIso, Electrons_deltaRLJ, Electrons_charge, Muons, Muons_passJetIso, Muons_mediumID, Muons_deltaRLJ, Muons_charge, muonLowerPt = 2, muonLowerPtTight = False, muons_tightID = None):
    lep = None
    lepCharge = None
    lepFlavour = None
    lepIdx = None
    nL = 0
    
    for i in range(Electrons.size()):
        e = Electrons[i]
        if electronPassesTightSelection(i, Electrons, Electrons_passJetIso, Electrons_deltaRLJ):
            nL += 1
            if nL > 1:
                return None, None, None, None
            lep = e
            lepCharge = Electrons_charge[i]
            lepFlavour = "Electrons"
            lepIdx = i
    for i in range(Muons.size()):
        m = Muons[i]
        if muonPassesTightSelection(i, Muons, Muons_mediumID, Muons_passJetIso, Muons_deltaRLJ, muonLowerPt, muonLowerPtTight, muons_tightID):
            nL += 1
            if nL > 1:
                return None, None, None, None
            lep = m
            lepCharge = Muons_charge[i]
            lepFlavour = "Muons"
            lepIdx = i
    
    return lep, lepIdx, lepCharge, lepFlavour

def getTwoLeptonsAfterSelection(Electrons, Electrons_passJetIso, Electrons_deltaRLJ, Electrons_charge, Muons, Muons_passJetIso, Muons_mediumID, Muons_deltaRLJ, Muons_charge, same_sign = False, muonLowerPt = 2, muonLowerPtTight = False, muons_tightID = None):
    leps = []
    lepCharges = []
    lepIdx = []
    lepFlavour = None
    nL = 0
    
    for i in range(Electrons.size()):
        e = Electrons[i]
        #print e, e.Pt(), bool(Electrons_passJetIso[i]), Electrons_deltaRLJ[i]
        if electronPassesTightSelection(i, Electrons, Electrons_passJetIso, Electrons_deltaRLJ):
            #print "here..."
            nL += 1
            if nL > 2:
                return None, None, None, None
            leps.append(e)
            lepIdx.append(i)
            lepCharges.append(Electrons_charge[i])
            lepFlavour = "Electrons"
    if nL == 1:
        return None, None, None, None
    if nL == 2:
        if same_sign:
            if lepCharges[0] * lepCharges[1] < 0:
                return None, None, None, None
        else:
            if lepCharges[0] * lepCharges[1] > 0:
                return None, None, None, None
    
    for i in range(Muons.size()):
        m = Muons[i]
        if muonPassesTightSelection(i, Muons, Muons_mediumID, Muons_passJetIso, Muons_deltaRLJ, muonLowerPt, muonLowerPtTight, muons_tightID):
            nL += 1
            if nL > 2:
                return None, None, None, None
            leps.append(m)
            lepIdx.append(i)
            lepCharges.append(Muons_charge[i])
            lepFlavour = "Muons"
    
    if nL != 2:
        return None, None, None, None
    
    if same_sign:
        if lepCharges[0] * lepCharges[1] < 0:
            return None, None, None, None
    else:
        if lepCharges[0] * lepCharges[1] > 0:
            return None, None, None, None
    
    if leps[0].Pt() < leps[1].Pt():
        leps = [leps[1], leps[0]]
        lepIdx = [lepIdx[1], lepIdx[0]]
        lepCharges = [lepCharges[1], lepCharges[0]]
    
    #if lepFlavour == "Electrons":
    #    print "YEY!!!"
    
    return leps, lepIdx, lepCharges, lepFlavour
    
    