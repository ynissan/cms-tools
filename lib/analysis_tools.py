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
	