#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import numpy as np
import os
import xml.etree.ElementTree as ET

sys.path.append("/afs/desy.de/user/n/nissanuv/cms-tools")
from lib import analysis_ntuples
from lib import analysis_tools
from lib import utils
from lib import cut_optimisation

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Create skims for x1x2x1 process with BDTs.')
parser.add_argument('-i', '--input_file', nargs=1, help='Input Filename', required=True)
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=True)
parser.add_argument('-ub', '--univ_bdt', nargs=1, help='Universal BDT Folder', required=True)
parser.add_argument('-tb', '--track_bdt', nargs=1, help='Track BDT Folder', required=True)

parser.add_argument('-s', '--signal', dest='signal', help='Signal', action='store_true')
parser.add_argument('-bg', '--background', dest='bg', help='Background', action='store_true')
args = parser.parse_args()
	

signal = args.signal
bg = args.bg

input_file = None
if args.input_file:
	input_file = args.input_file[0]
output_file = None
if args.output_file:
	output_file = args.output_file[0]

if (bg and signal) or not (bg or signal):
	signal = True
	bg = False
	
univ_bdt = None
track_bdt = None
if args.univ_bdt:
	univ_bdt = args.univ_bdt[0]
if args.track_bdt:
	track_bdt = args.track_bdt[0]
	
######## END OF CMDLINE ARGUMENTS ########

tracksVars = (
		{"name":"dxyVtx", "type":"double"},
		{"name":"dzVtx", "type":"double"},
		{"name":"chi2perNdof", "type":"double"},
		{"name":"trkMiniRelIso", "type":"double"},
		{"name":"trkRelIso", "type":"double"},
		{"name":"charge", "type":"int"},
		{"name":"trackJetIso", "type":"double"},
		{"name":"trackLeptonIso", "type":"double"}
		)

def main():
	iFile = TFile(input_file)
	hHt = iFile.Get('hHt')
	c = iFile.Get('tEvent')
	
	tree = c.CloneTree(0)
	tree.SetDirectory(0)
	
	nentries = c.GetEntries()
	print 'Analysing', nentries, "entries"
	
	(univ_testBGHists, univ_trainBGHists, univ_testSignalHists, univ_trainSignalHists, univ_methods, univ_names) = cut_optimisation.get_bdt_hists([univ_bdt])
	univ_trainSignalHist, univ_trainBGHist, univ_testSignalHist, univ_testBGHist = univ_trainSignalHists[0], univ_trainBGHists[0], univ_testSignalHists[0], univ_testBGHists[0]
	univ_highestZ, univ_highestS, univ_highestB, univ_highestMVA, univ_ST, univ_BT = cut_optimisation.getHighestZ(univ_trainSignalHist, univ_trainBGHist, univ_testSignalHist, univ_testBGHist)
	
	univ_bdt_weights = univ_bdt + "/dataset/weights/TMVAClassification_BDT.weights.xml"
	univ_bdt_vars = cut_optimisation.getVariablesFromXMLWeightsFile(univ_bdt_weights)
	univ_bdt_vars_map = cut_optimisation.getVariablesMemMap(univ_bdt_vars)
	univ_bdt_reader = cut_optimisation.prepareReader(univ_bdt_weights, univ_bdt_vars, univ_bdt_vars_map)
	
	
	(track_testBGHists, track_trainBGHists, track_testSignalHists, track_trainSignalHists, track_methods, track_names) = cut_optimisation.get_bdt_hists([track_bdt])
	track_trainSignalHist, track_trainBGHist, track_testSignalHist, track_testBGHist = track_trainSignalHists[0], track_trainBGHists[0], track_testSignalHists[0], track_testBGHists[0]
	track_highestZ, track_highestS, track_highestB, track_highestMVA, track_ST, track_BT = cut_optimisation.getHighestZ(track_trainSignalHist, track_trainBGHist, track_testSignalHist, track_testBGHist)
	
	track_bdt_weights = track_bdt + "/dataset/weights/TMVAClassification_BDT.weights.xml"
	track_bdt_vars = cut_optimisation.getVariablesFromXMLWeightsFile(track_bdt_weights)
	track_bdt_vars_map = cut_optimisation.getVariablesMemMap(track_bdt_vars)
	track_bdt_reader = cut_optimisation.prepareReader(track_bdt_weights, track_bdt_vars, track_bdt_vars_map)
	
	print track_bdt_vars_map
	
	print "-------------------"
	
	print "univ_highestZ=" + str(univ_highestZ)
	print "univ_highestS=" + str(univ_highestS)
	print "univ_highestB=" + str(univ_highestB)
	print "univ_highestMVA=" + str(univ_highestMVA)
	print "univ_ST=" + str(univ_ST)
	print "univ_BT=" + str(univ_BT)
	
	print "-------------------"
	
	print "track_highestZ=" + str(track_highestZ)
	print "track_highestS=" + str(track_highestS)
	print "track_highestB=" + str(track_highestB)
	print "track_highestMVA=" + str(track_highestMVA)
	print "track_ST=" + str(track_ST)
	print "track_BT=" + str(track_BT)
	
	print "-------------------"
	
	afterMonoLepton = 0
	afterUniversalBdt = 0
	afterMonoTrack = 0
	
	totalTracks = 0
	totalSurvivedTracks = 0
	eventsWithGreaterThanOneOppSignTracks = 0
	
	for ientry in range(nentries):
		if ientry % 1000 == 0:
			print "Processing " + str(ientry)
		c.GetEntry(ientry)
		
		nL = c.Electrons.size() + c.Muons.size()
		if nL != 1:
			continue
		
		afterMonoLepton += 1
		
		for k, v in univ_bdt_vars_map.items():
			v[0] = eval("c." + k)
		univ_tmva_value = univ_bdt_reader.EvaluateMVA("BDT")
		if univ_tmva_value < univ_highestMVA:
			continue
		
		afterUniversalBdt += 1
		
		ll = analysis_ntuples.leadingLepton(c)
		survivedTracks = []
		
		for ti in range(c.tracks.size()):
			t = c.tracks[ti]
			if c.tracks_trkRelIso[ti] > 0.1:
				continue 
				
			totalTracks +=1
			
			deltaRLL = abs(t.DeltaR(ll))
			if deltaRLL < 0.1:
				continue
			
			track_bdt_vars_map["deltaEtaLL"][0] = abs(t.Eta()-ll.Eta()) 
			track_bdt_vars_map["deltaRLL"][0] = deltaRLL
			track_bdt_vars_map["deltaEtaLJ"][0] = abs(t.Eta() - c.LeadingJet.Eta())
			track_bdt_vars_map["deltaRLJ"][0] = abs(t.DeltaR(c.LeadingJet))
			track_bdt_vars_map["track.Phi()"][0] = t.Phi()
			track_bdt_vars_map["track.Pt()"][0] = t.Pt()
			track_bdt_vars_map["track.Eta()"][0] = t.Eta()
			for trackVar in ['dxyVtx', 'dzVtx', 'trkMiniRelIso', 'trkRelIso']:
				track_bdt_vars_map[trackVar][0] = eval("c.tracks_" + trackVar + "[" + str(ti) + "]")
			
			track_tmva_value = track_bdt_reader.EvaluateMVA("BDT")

			if track_tmva_value > track_highestMVA:
				survivedTracks.append(ti)
				totalSurvivedTracks += 1
		#print "-------------"
		#print "Total Tracks=" + str(c.tracks.size())
		#print "Passed Tracks=" + str(len(survivedTracks))
		
		#print "survivedTracks=" + str(len(survivedTracks))
		
		numberOfOppositeChargeTracks = 0
		oppositeChargeTrack = 0
		
		leptonCharge = 0
		if c.Electrons.size() == 1:
			leptonCharge = c.Electrons_charge[0]
		elif c.Muons.size() == 1:
			leptonCharge = c.Muons_charge[0]
		
		for i in survivedTracks:
			if c.tracks_charge[i] * leptonCharge < 0:
				numberOfOppositeChargeTracks +=1
				oppositeChargeTrack = i
		
		if numberOfOppositeChargeTracks > 1:
			eventsWithGreaterThanOneOppSignTracks += 1
			
		if numberOfOppositeChargeTracks != 1:
			continue
		
		#print "Track charge=" + str(c.tracks_charge[survivedTracks[0]])
		#print "Lepton charge=" + str(leptonCharge)
		
		#if c.tracks_charge[survivedTracks[0]] * leptonCharge > 0:
		#	continue
		
		afterMonoTrack += 1
		
		tracksMem = {}
		tracksMem["tracks"] = ROOT.std.vector(TLorentzVector)()
		tracksMem["tracks"].push_back(c.tracks[oppositeChargeTrack])
		tree.SetBranchAddress('tracks', tracksMem["tracks"])

		for v in tracksVars:
			tracksMem[v["name"]] = eval("ROOT.std.vector(" + v["type"] + ")()")
			#print eval("c.tracks_" + v["name"] + "[survivedTracks[0]]")
			tracksMem[v["name"]].push_back(eval("c.tracks_" + v["name"] + "[oppositeChargeTrack]"))
			tree.SetBranchAddress('tracks_' + v["name"], tracksMem[v["name"]])
		
		tree.Fill()
	
	if tree.GetEntries() != 0:
		fnew = TFile(output_file,'recreate')
		tree.Write()
		hHt.Write()
		fnew.Close()
	else:
		print "*** RESULT EMPTY"
	iFile.Close()
	
	print "nentries=" + str(nentries)
	print "totalTracks=" + str(totalTracks)
	print "totalSurvivedTracks=" + str(totalSurvivedTracks)
	print "eventsWithGreaterThanOneOppSignTracks=" + str(eventsWithGreaterThanOneOppSignTracks)
	print "afterMonoLepton=" + str(afterMonoLepton)
	print "afterUniversalBdt=" + str(afterUniversalBdt)
	print "afterMonoTrack=" + str(afterMonoTrack)

main()