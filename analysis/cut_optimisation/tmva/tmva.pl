#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
from array import array
import argparse
import sys

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Run TMVA.')
parser.add_argument('-i', '--input_file', nargs=1, help='Input Signal Filename', required=False)
parser.add_argument('-o', '--output_file', nargs=1, help='Output Filename', required=False)
parser.add_argument('-bg', '--bg', nargs=1, help='Input Background Directory', required=False)
args = parser.parse_args()


input_file = None
if args.input_file:
	input_file = args.input_file[0]
else:
	input_file = "/afs/desy.de/user/n/nissanuv/work/x1x2x1/signal/skim/sum/type_sum/dm20.root"
output_file_name = None
if args.output_file:
	output_file_name = args.output_file[0]
else:
	output_file_name = "tmva_output.root"
bg_dir = None
if args.bg:
	bg_dir = args.bg[0]
else:
	bg_dir = "/afs/desy.de/user/n/nissanuv/work/x1x2x1/bg/skim/sum/type_sum"

	
######## END OF CMDLINE ARGUMENTS ########

gROOT.SetBatch(1)
ROOT.TMVA.Tools.Instance()
outputFile = TFile(output_file_name,'RECREATE')
factory = ROOT.TMVA.Factory("TMVAClassification", outputFile,
                            ":".join([
                                "!V",
                                "!Silent",
                                "Color",
                                "DrawProgressBar",
                                "Transformations=I;D;P;G,D",
                                "AnalysisType=Classification"]
                                     ))


factory.SetWeightExpression("Weight")
fsignal = TFile(input_file, 'recreate')
sTree = fsignal.Get("tEvent")
factory.AddSignalTree(sTree, 1);
bgFiles = []
bTrees = []
bFileNames =  glob(bg_dir + "/*");
for f in bFileNames:
	bFile = TFile(f, 'recreate')
	bgFiles.append(bFile)
	bTree = bFile.Get("tEvent")
	bTrees.append(bTree)
	factory.AddBackgroundTree(bTree, 1)

# Variables

factory.AddVariable('Met', 'F')
factory.AddVariable('NJets', 'I')
factory.AddVariable('Ht', 'F')
factory.AddVariable('Mht', 'F')
factory.AddVariable('Mt2', 'F')
factory.AddVariable('MetDHt', 'F')
factory.AddVariable('HtJet25', 'F')
factory.AddVariable('DileptonPt', 'F')
factory.AddVariable('DeltaPhi', 'F')
factory.AddVariable('DeltaEta', 'F')
factory.AddVariable('DeltaR', 'F')
factory.AddVariable('Pt3', 'F')
factory.AddVariable('Mt1', 'F')
factory.AddVariable('Mt2', 'F')
factory.AddVariable('Mtautau', 'F')

factory.AddVariable('Eta1', 'F')
factory.AddVariable('Eta2', 'F')

factory.AddVariable('Phi1', 'F')
factory.AddVariable('Phi2', 'F')

factory.AddVariable('Pt1', 'F')
factory.AddVariable('Pt2', 'F')

factory.AddVariable('DeltaEtaLeadingJetDilepton', var_DeltaEtaLeadingJetDilepton,'DeltaEtaLeadingJetDilepton/D')
factory.AddVariable('LeadingJetPartonFlavor', var_LeadingJetPartonFlavor,'LeadingJetPartonFlavor/D')
factory.AddVariable('LeadingJetQgLikelihood', var_LeadingJetQgLikelihood,'LeadingJetQgLikelihood/D')

# Spectators
factory.AddSpectator('LeptonsType','I')
factory.AddSpectator('InvMass', 'F')

# cuts defining the signal and background sample
preselectionCut = ROOT.TCut("Mtautau < 0 || Mtautau > 160")
factory.PrepareTrainingAndTestTree(preselectionCut, "SplitMode=random:!V")
factory.BookMethod(ROOT.TMVA.Types.kBDT, "BDT", "NTrees=200:MaxDepth=4")
factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()
outputFile.Close()






