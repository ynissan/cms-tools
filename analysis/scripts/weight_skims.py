#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import numpy as np
import argparse
import sys
import os

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import utils

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Weight skims for x1x2x1 process.')
parser.add_argument('-i', '--input_dir', nargs=1, help='Input Directory', required=True)
parser.add_argument('-f', '--Force', dest='force', help='Force Update', action='store_true')
args = parser.parse_args()

input_dir = args.input_dir[0]
force = args.force
######## END OF CMDLINE ARGUMENTS ########

fileList = glob(input_dir + "/*");
for f in fileList:
	if os.path.isdir(f): continue
	print "processing file " + f 
	f = TFile(f, "update")
	h = f.Get("hHt")
	numOfEvents = h.Integral(-1,99999999)+0.000000000001
	print "Number of event:", numOfEvents
	
 	t = f.Get("tEvent")
 	t.GetEntry(0)
 	cs = t.CrossSection
 	print "CrossSection:", cs
 	weight = (utils.LUMINOSITY * cs)/numOfEvents
 	print "weight:", weight
 	var_Weight = np.zeros(1,dtype=float)
 	var_Weight[0] = weight
 	nentries = t.GetEntries();
 	if t.GetBranchStatus("Weight"):
 		if not force:
			print "This tree is already weighted! Skipping..."
		else:
			branch = t.GetBranch("Weight")
			branch.Reset()
			branch.SetAddress(var_Weight)
			for ientry in range(nentries):
				branch.Fill()
			t.Write("tEvent",TObject.kOverwrite)
			print "Done"
		f.Close()
		continue
		
 	newBranch = t.Branch("Weight",var_Weight,"Weight/D");
 	for ientry in range(nentries):
 		newBranch.Fill()
 	print "Writing Tree"
 	t.Write("tEvent",TObject.kOverwrite)
 	print "Done"
 	f.Close()
 	
# 	
# 	
# 	
# 	 TFile f("tree3.root","update");
#    Float_t new_v;
#    TTree *t3 = (TTree*)f->Get("t3");
#    TBranch *newBranch = t3-> Branch("new_v",&new_v,"new_v/F");
#    //read the number of entries in the t3
#    Int_t nentries = (Int_t)t3->GetEntries();
#    for (Int_t i = 0; i < nentries; i++){
#       new_v= gRandom->Gaus(0,1);
#       newBranch->Fill();
#    }
#    t3->Write("",TObject::kOverwrite); // save only the new version of
#                                       // the tree