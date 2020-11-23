#!/usr/bin/python

from ROOT import *
from math import *
import sys

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import utils

def minDeltaR(v, vs):
    min = None
    for l in vs:
        d = abs(v.DeltaR(l))
        if min is None or d < min:
            min = d
    return min

def isSusy(pdgId):
	pdgId = abs(pdgId)
	if pdgId >= 1000001 and pdgId <= 1000006:
		return True
	if pdgId >= 1000011 and pdgId <= 1000016:
		return True
	if pdgId >= 2000001 and pdgId <= 2000006:
		return True
	if pdgId >= 1000021 and pdgId <= 1000025:
		return True
	if pdgId == 2000011 or pdgId == 2000013 or pdgId == 2000015 or pdgId == 1000035 or pdgId == 1000037 or pdgId == 1000039:
		return True
	return False

def MT(MET, pt, l):
	return sqrt(2 * MET * l.Pt() * (1 - cos(l.DeltaPhi(pt))))

def MT2(MET, MetPhi, l):
	return sqrt(2 * MET * l.Pt() * (1 - cos(MetPhi - l.Phi())))
	
def mt_2(pt1, phi1, pt2, phi2):
	return sqrt(2*pt1*pt2*(1-cos(phi1-phi2)))


def Mtautau(pt, l1, l2):
    #print l1.Pt(), l2.Pt(), (pt.Px() * l2.Py() - pt.Py() * l2.Px()), (l1.Px() * l2.Py() - l2.Px() * l1.Py())
    #print pt.Px(), pt.Py(), l1.Px(), l1.Py(), l2.Px(), l2.Py()
    xi1div = (l1.Px() * l2.Py() - l2.Px() * l1.Py())
    if xi1div == 0.:
        xi1div = utils.epsilon
    xi2div = (l1.Px() * l2.Py() - l2.Px() * l1.Py())
    if xi2div == 0.:
        xi2div = utils.epsilon
    xi1 = (pt.Px() * l2.Py() - pt.Py() * l2.Px()) / xi1div
    xi2 = (pt.Py() * l1.Px() - pt.Px() * l1.Py()) / xi2div

    nu1v = xi1 * l1.Vect()
    nu2v = xi2 * l2.Vect()

    #print "Ptx=" + str(pt.X()) + " nuX=" + str(nu1v.X() + nu2v.X()) + " Pty=" + str(pt.Y()) + " nuY=" + str(nu1v.Y() + nu2v.Y())

    nu1E = nu1v.Mag()
    nu2E = nu2v.Mag()

    #print "xi1=" + str(xi1) + " xi2=" + str(xi2) + " nu1E=" + str(nu1E) + " nu2E=" + str(nu2E) + " sum=" + str(nu1E + nu2E) + " orig=" + str(pt.E())

    nu1 = TLorentzVector(nu1v, nu1E)
    nu2 = TLorentzVector(nu2v, nu2E)

    m = (l1 + l2 + nu1 + nu2).M()

    if m < 0:
        m = -1
    return m

# Sam Bein (samuel.bein@gmail.com)
# gROOT.ProcessLine(open('src/UsefulJet.cc').read())
# exec('from ROOT import *')

def PreciseMtautau(MetPt, MetPhi,  l1, l2 ):
    Met = TLorentzVector()
    Met.SetPtEtaPhiE(MetPt,0,MetPhi,0)
    L1 = TLorentzVector()
    L2 = TLorentzVector()
    L1.SetPtEtaPhiE(l1.Pt(), l1.Eta(), l1.Phi(), 0.106)
    L2.SetPtEtaPhiE(l2.Pt(), l2.Eta(), l2.Phi(), 0.106)
                                                                                                        
    inv_det = 1./( L1.Px()*L2.Py() - L2.Px()*L1.Py())
    A00 = inv_det*L2.Py();
    A01 =-inv_det*L2.Px()
    A10 =-inv_det*L1.Py();
    A11 = inv_det*L1.Px()
    C0  = (Met+L1+L2).Px();
    C1  = (Met+L1+L2).Py()
    X0  = A00*C0 + A01*C1;
    X1  = A10*C0 + A11*C1

    T1 = TLorentzVector( L1.Px()*X0 , L1.Py()*X0 , L1.Pz()*X0 , 1.777 )    # 1.777 tau mass                                                                                                                                     
    T2 = TLorentzVector( L2.Px()*X1 , L2.Py()*X1 , L2.Pz()*X1 , 1.777 )
    if X0>0. and X1>0.:
        return  (T1+T2).M() 
    return -(T1+T2).M()

def pt3(pt1, phi1, pt2, phi2, pt3, phi3):
    phi2 -= phi1;
    phi3 -= phi1;
    return hypot(pt1 + pt2 * cos(phi2) + pt3 * cos(phi3), pt2*sin(phi2) + pt3*sin(phi3));


def Mtautau2(pt, l1, l2, t1, t2, n1, n2):
	xi1 = (pt.Px() * l2.Py() - pt.Py() * l2.Px()) / (l1.Px() * l2.Py() - l2.Px() * l1.Py())
	xi2 = (pt.Py() * l1.Px() - pt.Px() * l1.Py()) / (l1.Px() * l2.Py() - l2.Px() * l1.Py())
	
	if xi1 < 0 or xi2 < 0:
		print "negative"
	
	nu1v = xi1 * l1.Vect()
	nu2v = xi2 * l2.Vect()
	
	print "Ptx=" + str(pt.X()) + " nuX=" + str(nu1v.X() + nu2v.X()) + " Pty=" + str(pt.Y()) + " nuY=" + str(nu1v.Y() + nu2v.Y())
	print "Gen:"
	print "Ptx=" + str(pt.X()) + " nuX=" + str(n1.X() + n2.X()) + " Pty=" + str(pt.Y()) + " nuY=" + str(n1.Y() + n2.Y())
	print ""
	print "genX=" + str(n1.X()) + " repX=" + str(nu1v.X()) + " genY=" + str(n1.Y()) + " repY=" + str(nu1v.Y()) + " genZ=" + str(n1.Z()) + " repZ=" + str(nu1v.Z())
	print "genX=" + str(n2.X()) + " repX=" + str(nu2v.X()) + " genY=" + str(n2.Y()) + " repY=" + str(nu2v.Y()) + " genZ=" + str(n2.Z()) + " repZ=" + str(nu2v.Z())
	
	nu1E = nu1v.Mag()
	nu2E = nu2v.Mag()
	
	print "nu1E=" + str(nu1E) + " genNu1E=" + str(n1.Vect().Mag())
	print "nu2E=" + str(nu2E) + " genNu2E=" + str(n2.Vect().Mag())
	
	#print "xi1=" + str(xi1) + " xi2=" + str(xi2) + " nu1E=" + str(nu1E) + " nu2E=" + str(nu2E) + " sum=" + str(nu1E + nu2E) + " orig=" + str(pt.E())
	
	nu1 = TLorentzVector(nu1v, nu1E)
	nu2 = TLorentzVector(nu2v, nu2E)
	
	print "Total:"
	print "genX=" + str(n1.X()) + " repX=" + str(nu1.X()) + " genY=" + str(n1.Y()) + " repY=" + str(nu1.Y()) + " genZ=" + str(n1.Z()) + " repZ=" + str(nu1.Z()) +  " genE=" + str(n1.E()) + " repE=" + str(nu1.E())
	print "genX=" + str(n2.X()) + " repX=" + str(nu2.X()) + " genY=" + str(n2.Y()) + " repY=" + str(nu2.Y()) + " genZ=" + str(n2.Z()) + " repZ=" + str(nu2.Z()) +  " genE=" + str(n2.E()) + " repE=" + str(nu2.E())
	
	m = (l1 + l2 + nu1 + nu2).M()
	print "m=" + str(m) + " genM=" + str((l1 + l2 + n1 + n2).M())
	
	if m < 0:
		m = -1
	return m
	