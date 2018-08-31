#!/usr/bin/env python

import os, sys, re
from string import *
from rgsutil import *
from time import sleep
from ROOT import *

NAME = 'x10x20x10'
bkgfiledir = "/afs/desy.de/user/n/nissanuv/work/x1x2x1/bg/skim/sum/type_sum"

def main():
    global cut
    
    print "="*80
    print "\t=== %s: find best cuts ===" % NAME
    print "="*80
    
    treename = "RGS"
    varfilename  = "%s.cuts" % NAME
    resultsfilename= "%s.root" % NAME

    print "\n\topen RGS file: %s"  % resultsfilename
    ntuple = Ntuple(resultsfilename, treename)
    
    variables = ntuple.variables()
    for name, count in variables:
        print "\t\t%-30s\t%5d" % (name, count)        
    print "\tnumber of cut-points: ", ntuple.size()

    setStyle()
    
    # Create a 2-D histogram for ROC plot
    msize = 0.30  # marker size for points in ROC plot
    
    xbins =  10000   # number of bins in x (background)
    xmin  =  0.0    # lower bound of x
    xmax  =  1.0    # upper bound of y

    ybins =  50
    ymin  =  0.0
    ymax  =  1.0

    color = kBlue+1
    hroc  = mkhist2("hroc",
                    "#font[12]{#epsilon_{B}}",
                    "#font[12]{#epsilon_{S}}",
                    xbins, xmin, xmax,
                    ybins, ymin, ymax,
                    color=color)
    hroc.SetMinimum(0)
    hroc.SetMarkerSize(msize)

    # loop over all cut-points, compute a significance measure Z
    # for each cut-point, and find the cut-point with the highest
    # significance and the associated cuts.

    bestZ   = -1    # best Z value
    bestRow = -1    # row with best cut-point
    totals = ntuple.totals()

    #print "totals", totals
    #print "len(totals)", len(totals)

    # get background totals
    tb = 0
    for i in range(1, len(totals)):
        tb += totals[i][0]

    ts = totals[0][0]
    
    for row, cuts in enumerate(ntuple):
        b  = 0 #  background count        
        s  = cuts.count_signal #  signal count
        
        for name, count in variables:
        	if "count_" in name and name != "count_signal" :
        		b += cuts(name)
        
        fs = s / ts
        fb = b / tb
        
        hroc.Fill(fb, fs)
        #print "----------------------------"
        #print "Fraction Signal: " + str(fs)
        #print "Fraction Background: " + str(fb)

        Z = signalSignificance(s, b)
        if Z > bestZ:
            bestZ = Z
            bestRow = row
        
    
    print "\t== plot ROC ==="	
    croc = TCanvas("h_%s_ROC" % NAME, "ROC", 520, 10, 500, 500)
    croc.cd()
    croc.SetLogx()
    hroc.Draw()
    croc.Update()
    gSystem.ProcessEvents()    
    croc.SaveAs(".pdf")  
    
    print "\t=== %s: best cut ===" % NAME
    print "Best Z: " + str(bestZ)
    ntuple.read(bestRow)
    
    b  = 0 #  background count        
    s  = ntuple("count_signal") #  signal count
        
    for name, count in variables:	
	if "count_" in name and name != "count_signal" :
		b += ntuple(name)
	elif "fraction_" not in name:
		print name + "=" + str(ntuple(name))
    fs = s / ts
    fb = b / tb
    print "-------------"
    print "(fs,fb)=("+str(fs)+","+str(fb)+")"
    
    
    
# ---------------------------------------------------------------------
try:
    main()
except KeyboardInterrupt:
    print '\nciao!'