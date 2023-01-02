#!/usr/bin/env python

from ROOT import *
from glob import glob
from sys import exit
import argparse
import sys
import os
import re

sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/"))
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/cms-tools/lib/classes"))
import utils
import analysis_ntuples
import analysis_tools
import plotutils
import analysis_selections

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

conditions = analysis_selections.two_leptons_full_bdt_conditions_outside_mtautau_window
if orth:
    conditions = analysis_selections.two_leptons_full_bdt_conditions_outside_mtautau_window_sos
drawString = analysis_selections.getFastSimString(wanted_year, lep, conditions)

observable = analysis_selections.dilepBDTString[wanted_year] + analysis_selections.jetIsos[lep]