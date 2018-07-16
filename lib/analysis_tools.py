#!/usr/bin/python

from ROOT import *
from math import *

# load FWLite C++ libraries
# gSystem.Load("libFWCoreFWLite.so");
# gSystem.Load("libDataFormatsFWLite.so");
# FWLiteEnabler.enable()

# load FWlite python libraries
# from DataFormats.FWLite import Handle, Events
# import FWCore.ParameterSet.Config as cms

def MT(MET, pt, l):
	return sqrt(2 * MET * l.Pt() * (1 - cos(l.DeltaPhi(pt))))

def MT2(MET, MetPhi, l):
	return sqrt(2 * MET * l.Pt() * (1 - cos(MetPhi - l.Phi())))
	
def mt_2(pt1, phi1, pt2, phi2):
	return sqrt(2*pt1*pt2*(1-cos(phi1-phi2)))


def Mtautau(pt, l1, l2):
	xi1 = (pt.Px() * l2.Py() - pt.Py() * l2.Px()) / (l1.Px() * l2.Py() - l2.Px() * l1.Py())
	xi2 = (pt.Py() * l1.Px() - pt.Px() * l1.Py()) / (l1.Px() * l2.Py() - l2.Px() * l1.Py())
	
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

def PreciseMtautau(MetPt, MetPhi,  L1, L2 ):
  Met = TLorentzVector()
  Met.SetPtEtaPhiE(MetPt,0,MetPhi,0)
  
  #L1 = TLorentzVector( l1.Px(), l1.Py(), l1.Pz(), sqrt((l1.Px())**2 + (l1.Py())**2 + (l1.Py())**2 + 0.106**2))
  #L2 = TLorentzVector( l2.Px(), l2.Py(), l2.Pz(), sqrt((l2.Px())**2 + (l2.Py())**2 + (l2.Py())**2 + 0.106**2))  
  
  #print "Masses: ",str(L1.M()),str(L2.M())                                                                                                                                                
  #float A00,A01,A10,A11,  C0,C1,  X0,X1,  inv_det;     // Define A:2x2 matrix, C,X 2x1 vectors & det[A]^-1   
  if ( L1.Px()*L2.Py() - L2.Px()*L1.Py()) == 0:
  	print "*********WTF!!!!"
  	return -1                                                                                                             
  inv_det = 1./( L1.Px()*L2.Py() - L2.Px()*L1.Py())
  A00 = inv_det*L2.Py();     A01 =-inv_det*L2.Px()
  A10 =-inv_det*L1.Py();     A11 = inv_det*L1.Px()
  C0  = (Met+L1+L2).Px();    C1  = (Met+L1+L2).Py()
  X0  = A00*C0 + A01*C1;     X1  = A10*C0 + A11*C1
  
  T1 = TLorentzVector( L1.Px()*X0 , L1.Py()*X0 , L1.Pz()*X0 , sqrt((L1.Px()*X0)**2 + (L1.Py()*X0)**2 + (L1.Py()*X0)**2 + 1.777**2) )    # 1.777 tau mass                                                                                                                                     
  T2 = TLorentzVector( L2.Px()*X1 , L2.Py()*X1 , L2.Pz()*X1 , sqrt((L2.Px()*X0)**2 + (L2.Py()*X0)**2 + (L2.Py()*X0)**2 + 1.777**2) )
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
	