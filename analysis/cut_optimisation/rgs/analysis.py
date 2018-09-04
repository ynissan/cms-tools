#!/usr/bin/env python

import os, sys, re
from string import *
from rgsutil import *
from time import sleep
from ROOT import *
import argparse

NAME = 'x10x20x10'
bkgfiledir = "/afs/desy.de/user/n/nissanuv/work/x1x2x1/bg/skim/sum/type_sum"

####### CMDLINE ARGUMENTS #########

parser = argparse.ArgumentParser(description='Create skims for x1x2x1 process.')
parser.add_argument('-i', '--input_dir', nargs=1, help='Input Directory', required=False)
args = parser.parse_args()

input_dir = None
if args.input_dir:
	input_dir = args.input_dir[0]
	
######## END OF CMDLINE ARGUMENTS ########

def main():
    global cut
    
    print "="*80
    print "\t=== %s: find best cuts ===" % NAME
    print "="*80
    
    dir = None
    cuts_name = None
    if input_dir:
    	dir = os.path.realpath(input_dir)
    	cuts_name = os.path.basename(dir)
    else:
    	dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    	cuts_name = NAME
    
    #print dir
    #print cuts_name
    
    treename = "RGS"
    varfilename  = None
    resultsfilename = None
    
    
    varfilename  = dir + "/" + "%s.cuts" % cuts_name
    resultsfilename= dir + "/" + "%s.root" % cuts_name

    print "\n\topen RGS file: %s"  % resultsfilename
    ntuple = Ntuple(resultsfilename, treename)
    
    variables = ntuple.variables()
    var_count = {}
    for name, count in variables:
        print "\t\t%-30s\t%5d" % (name, count)
        var_count[name] = count
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

    print "totals", totals
    print "len(totals)", len(totals)

    # get background totals
    tb = 0
    for i in range(1, len(totals)):
        tb += totals[i][0]

    ts = totals[0][0]
    print "Totals:"
    print "Signal: " + str(ts)
    print "Background: " + str(tb)
    for row, cuts in enumerate(ntuple):
    	#print "Row " + str(row)
    	#print "Cuts: "
    	#print cuts
        b  = 0 #  background count        
        s  = cuts.count_signal #  signal count
        #print cuts
        for name, count in variables:
        	if "count_" in name and name != "count_signal" :
        		#print "Adding name: " + name
        		#print "value: " + str(cuts(name))
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
    croc = TCanvas("h_%s_ROC" % cuts_name, "ROC", 520, 10, 500, 500)
    croc.cd()
    #croc.SetLogx()
    hroc.Draw()
    croc.Update()
    gSystem.ProcessEvents()    
    croc.SaveAs(dir + "/" + cuts_name + ".pdf")  
    
    print "\t=== %s: best cut ===" % NAME
    print "Best Z: " + str(bestZ)
    ntuple.read(bestRow)
    
    b  = 0 #  background count        
    s  = ntuple("count_signal") #  signal count
        
    for name, count in variables:	
	if "count_" in name and name != "count_signal" :
		b += ntuple(name)
	elif "fraction_" not in name:
		if var_count[name] > 1:
			print name + "=(" + str(ntuple(name)[0]) + "," + str(ntuple(name)[1]) + ")"
		else:
			print name + "=" + str(ntuple(name))
    fs = s / ts
    fb = b / tb
    print "-------------"
    print "(fs,fb)=("+str(fs)+","+str(fb)+")"
    print "-------------"
    print "b=" + str(b)
    print "s=" + str(s)
    
    
    
# ---------------------------------------------------------------------
try:
    main()
except KeyboardInterrupt:
    print '\nciao!'