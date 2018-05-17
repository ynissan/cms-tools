from ROOT import *
from utils import *
from glob import glob
gROOT.SetBatch(True)
from os import system
import sys
event_types = {'QCD':
                   ['_HT200to300','_HT300to500','_HT500to700','_HT700to1000','_HT1000to1500','_HT1500to2000','_HT2000toInf'],
               'ZJetsToNuNu':
                   ['_HT-100To200','_HT-200To400','_HT-400To600','_HT-600To800','_HT-800To1200','_HT-1200To2500','_HT-2500ToInf'],
               'WJetsToLNu':
                   ['_HT-200To400','_HT-400To600','_HT-600To800','_HT-800To1200','_HT-1200To2500','_HT-2500ToInf',],
               'TTJets':
                   ['_TuneCUETP8M1'],#,'_HT-800to1200']
               'pMSSM':['']
               }

try:
    do_hadd=bool(sys.argv[1])
except:
    do_hadd = False

print 'do_hadd: ',do_hadd
for event_type in event_types:
    if not do_hadd:
        break
    occuring_types = []
    for type in event_types[event_type]:
        append = True
        if len(glob('output/*'+event_type+type+'*.root'))==0:
            print event_type,type, ' not in output/ , continuing'
            append = False
            continue
        if append:
            occuring_types.append(type)
        print occuring_types
        if type in occuring_types:
            print type
            command = 'hadd -f output/typesorted/'+event_type+type+'.root '+' output/*'+event_type+type+'*.root'
            print command 
            system(command)

    rootfiles = glob('output/typesorted/*'+event_type+'*.root')
    if len(rootfiles)==0: 
        print 'None found for category: ', event_type
        continue
    for type in occuring_types:#event_types[event_type]:
        print 'Processing file: ', 'output/processed/',event_type,type,'_plots.root'
        fnew = TFile('output/processed/'+event_type+type+'_plots.root','recreate')
#        print rootfiles[0]
        fhists0 = TFile(rootfiles[0])
#        print fhists0,fhists0.ls()
        keys = fhists0.GetListOfKeys()
        hHT0 = fhists0.Get('hHt').Clone()
        Lumi = 36000.
        c1 = mkcanvas('c1')
        c_weighted = mkcanvas('c2')
        c1.SetLogy()
        c_weighted.SetLogy()
        for key in keys:
            name = key.GetName()#histogram name
            if not '_' in name:
                continue
#            print 'Processing histogram ', name
            h = fhists0.Get(name).Clone()
            h_weighted = h.Clone(name+'_weighted')
            h_weighted.Scale(Lumi/(hHT0.Integral(-1,99999999)+0.000000000001))
            histoStyler(h,kBlue+2)
            histoStyler(h_weighted,kRed+2)
            
            for fname in rootfiles[1:]:
            
                f_ = TFile(fname)
                fhists0.cd()
                h_ = f_.Get(name)
                hHT_ = f_.Get('hHt').Clone()
                h_weighted_ = h_.Clone()
                h_weighted_.Scale(Lumi/(hHT_.Integral(-1,99999999)+0.000000000001))
                h.Add(h_)   
                h_weighted.Add(h_weighted_)
                
            fnew.cd()
            c1.cd()
            h.Draw()
            c1.Update()
            h.Write()
            
            c_weighted.cd()
            h_weighted.Draw()
            c_weighted.Update()
            h_weighted.Write()
            fhists0.cd()
        fnew.Close()


    #add all output files of an event type
    command = 'hadd -f output/categorized/'+event_type+'.root'+' output/processed/*'+event_type+'*plots.root'
    print command
    system(command)

canvas = mkcanvas('canvas')
canvas.SetLogz()
canvas.SetLogy()
canvas.cd()
rtstacks = TFile('output/stacked_hists/stacked_histograms.root','recreate')
rtstacks.cd()


canvas.Divide(2,2)
p1 = TPad()
p2 = TPad()
p3 = TPad()
p4 = TPad()
p5 = TPad()
p6 = TPad()

pads = [p1,p2,p3,p4,p5,p6]
for listidx,pad in enumerate(pads):
    pad = canvas.cd(listidx+1)
    pad.SetLogy()
    pad.SetLogz()


#Create stacked histrograms
selectionsets = [
    'nocuts',
    #                 'nocuts_1Jet',
    #                 'nocuts_2Jet',
    #                 'baseline',
    #                 'baseline_1Jet',
    #                 'baseline_2Jet',
    #                 'baseline_noMET',
    #                 'baseline_noMETsig',
    #                 'baseline_noDeltaPhi1',
    #                 'baseline_noDeltaPhi2',
    #                 'baseline_noNJets',
    #                 'baseline_noLepPt',
    #                 'baseline_noHTcut',
    #                 'baseline_noNBtags',
    #                 'baseline_noHTMETfrac',
    #                 'baseline_noTrkQl',
    
    #                 'baseline_1JetnoMET',
    #                 'baseline_1JetnoMETsig',
    #                 'baseline_1JetnoDeltaPhi1',
    #                 'baseline_1JetnoDeltaPhi2',
    #                 'baseline_1JetnoLepPt',
    #                 'baseline_1JetnoHTcut',
    #                 'baseline_1JetnoNBtags',
    #                 'baseline_1JetnoHTMETfrac',
    #                 'baseline_1JetnoTrkQl',
    
    #                 'baseline_2JetnoMET',
    #                 'baseline_2JetnoMETsig',
    #                 'baseline_2JetnoDeltaPhi1',
    #                 'baseline_2JetnoDeltaPhi2',
    #                 'baseline_2JetnoLepPt',
    #                 'baseline_2JetnoHTcut',
    #                 'baseline_2JetnoNBtags',
    #                 'baseline_2JetnoHTMETfrac',
    #                 'baseline_2JetnoTrkQl',
    
    'tight',
    
    'tight_noMET',
    'tight_noMETsig',
    'tight_noDeltaPhi1',
    'tight_noDeltaPhi2',
    'tight_noNJets',
    'tight_noLepPt',
    'tight_noHTcut',
    'tight_noNBtags',
    'tight_noHTMETfrac',
    'tight_noTrkQl',
    
    
    #                 'lepbaseline'
]

MET_stacks = {}
HT_stacks = {}
METsig_stacks = {}
NJets_stacks = {}
DeltaPhi1_stacks = {}
DeltaPhi2_stacks = {}
LepPtmax_stacks = {}
HTMET_stacks = {}
HTMETfrac_stacks = {}
METLepdPhi_stacks = {}
NBtags_stacks = {}
JetIso_stacks = {}
LepIso_stacks = {}
TrkRelIso_stacks = {}
TrkIsoXPt_stacks = {}
TrkPt_stacks = {}
TrkEta_stacks = {}
TrkPtVIso_stack = {}
NTracks_stack = {}
TrkDeltaPhi1_stack = {}
for selection in selectionsets:
    MET_stacks[selection] = THStack('MET_stack'+selection,'Event MET'+selection)
    HT_stacks[selection] = THStack('HT_stack'+selection,'Event HT'+selection)
    NJets_stacks[selection] = THStack('NJets_stack'+selection,'Event Jet multiplicity'+selection)
    DeltaPhi1_stacks[selection] = THStack('DeltaPhi1_stack'+selection,'Event DeltaPhi1'+selection)
    DeltaPhi2_stacks[selection] = THStack('DeltaPhi2_stack'+selection,'Event DeltaPhi2'+selection)
    LepPtmax_stacks[selection] = THStack('LepPtmax_stack'+selection,'Event Lep_max_pt'+selection)
    HTMET_stacks[selection] = THStack('HTMET_stack'+selection,'Event HT vs MET'+selection)
    METsig_stacks[selection] = THStack('METsig_stack'+selection,'Event MET significance'+selection)
    HTMETfrac_stacks[selection] = THStack('HTMETfrac_stack'+selection,'Event HTMETfrac_stack'+selection)
    METLepdPhi_stacks[selection] = THStack('METLeldR_stack'+selection,'Event METLepdPhi_stack'+selection)
    NBtags_stacks[selection] = THStack('NBtags_stack'+selection, 'Event NBtags_stack'+selection)
    JetIso_stacks[selection] = THStack('JetIso_stack'+selection, 'JetIso_stack'+selection)
    LepIso_stacks[selection] = THStack('LepIso_stack'+selection, 'LepIso_stack'+selection)
    TrkRelIso_stacks[selection] = THStack('TrkRelIso_stack'+selection, 'TrkRelIso_stack'+selection)
    TrkIsoXPt_stacks[selection] = THStack('TrkIsoXPt_stack'+selection, 'TrkIsoXPt_stack'+selection)
        
    TrkPt_stacks[selection] = THStack('TrkPt_stack'+selection, 'TrkPt_stack'+selection)
    TrkEta_stacks[selection] = THStack('TrkEta_stack'+selection, 'TrkEta_stack'+selection)
    TrkPtVIso_stack[selection] = THStack('TrkPtVIso_stack'+selection, 'TrkPtVIso_stack'+selection)
    NTracks_stack[selection] = THStack('NTracks_stack'+selection,'NTracks_stack'+selection)
    TrkDeltaPhi1_stack[selection] = THStack('TrkDeltaPhi1_stack'+selection,'TrkDeltaPhi1_stack'+selection)
stacks = {
    'MET':MET_stacks,
    'HT':HT_stacks,
    'DeltaPhi1':DeltaPhi1_stacks,
    'DeltaPhi2':DeltaPhi2_stacks,
    'NJets':NJets_stacks,
    'LepPtmax':LepPtmax_stacks,
#    '2HTMET':HTMET_stacks,
    'METsig':METsig_stacks,
    'HTMETfrac':HTMETfrac_stacks,
    'METLepdPhi':METLepdPhi_stacks,
    'NBtags':NBtags_stacks,
    'JetIso':JetIso_stacks,
    'LepIso':LepIso_stacks,
    'TrkRelIso':TrkRelIso_stacks,
    'TrkIsoXPt':TrkIsoXPt_stacks,
    'TrkPt':TrkPt_stacks,
    'TrkEta':TrkEta_stacks,
#    'TrkPtVIso':TrkPtVIso_stack
    'NTrack':NTracks_stack,
    'TrkDeltaPhi1':TrkDeltaPhi1_stack
    }
format_stacks = {
    'MET':('MET [GeV]','Weighted to L=36 fb^-1'),
    'HT':('HT [GeV]','Weighted to L=36 fb^-1'),
    'DeltaPhi1':('#Delta #Phi_{J1,MET}','Weighted to L=36 fb^-1'),
    'DeltaPhi2':('#Delta #Phi_{J2,MET}','Weighted to L=36 fb^-1'),
    'NJets':('Jet multiplicity','Weighted to L=36 fb^-1'),
    'LepPtmax':('Pt [GeV]','Weighted to L=36 fb^-1'),
    '2dHTMET':('MET [GeV]','HT [GeV]'),
    'METsig':('MET significance [#sqrt{GeV}]','Weighted to L=36 fb^-1'),
    'HTMETfrac':('#frac{HT}{MET}','Weighted to L=36 fb^-1'),
    'METLepdPhi':('#Delta R_{MET,Lep_{max}}','Weighted to L=36 fb^-1'),
    'NBtags':('Nr. of BTags','Weighted to L=36 fb^-1'),
    'JetIso':('Jet Isolation','#frac{Weighted to L=36 fb^-1}{N_{Tracks}}'),
    'LepIso':('Lep Isolation','#frac{Weighted to L=36 fb^-1}{N_{Tracks}}'),
    'TrkRelIso':('Track Relative Isolation','#frac{Weighted to L=36 fb^-1}{N_{Tracks}}'),
    'TrkPt':('Track Pt [GeV]','#frac{Weighted to L=36 fb^-1}{N_{Tracks}}'),
    'TrkEta':('Track Eta','#frac{Weighted to L=36 fb^-1}{N_{Tracks}}'),
    '2dTrkPtVsIso':('Track Pt [GeV]','Track Relative Isolation'),
    'TrkIsoXPt':('Isolation #times P_{T} [GeV]','#frac{Weighted to L=36 fb^-1}{N_{Tracks}}'),
    '2dTrkPtVsIsoXPt':('Track Pt [GeV]','Isolation #times P_{T} [GeV]'),
    'NTrack':('Number of Tracks','#frac{Weighted to L=36 fb^-1}{N_{Tracks}}'),
    'TrkDeltaPhi1': ('#Delta#Phi_{Track,J1}','Number of Tracks')
    }
legend = TLegend(0.4,0.75,0.68,0.9)
signalfile = TFile('output/categorized/pMSSM.root')
legend.AddEntry(signalfile.Get('hHT'),'Signal','L')
for file in glob('output/categorized/*.root'):
    eventtype = file.split('/')[-1]
    eventtype = eventtype[:eventtype.find('.root')]
    histfile = TFile(file)
    histfile.cd()
    keys = histfile.GetListOfKeys()
    added_to_legend = False
    processed = []
    for key in keys:
        name = key.GetName()
        if name.find('weighted') == -1:
            continue
        selection = name[name.find('_')+1:name.find('weighted')-1]
        if len(selection) == 0:
            continue
        histtype = name[1:name.find('_')]
        if name.find('2d') != -1:
            continue
        if eventtype == 'pMSSM':
            continue

        print 'processing histogram: ', name
#        print 'selection: ', selection
#        print 'histogram type: ', histtype
        h = histfile.Get(name)
        h.SetDirectory(0)
        rtstacks.cd()
        if eventtype == 'QCD':
            h.SetLineColor(kYellow+1)
            h.SetFillColor(kYellow+1)
            if not added_to_legend:
                legend.AddEntry(h,'QCD','F')
                added_to_legend = True
        elif eventtype == 'TTJets':
            h.SetLineColor(kRed+1)
            h.SetFillColor(kRed+1)
            if not added_to_legend:
                legend.AddEntry(h,'TTJets','F')
                added_to_legend = True


        elif eventtype == 'ZJetsToNuNu':
            h.SetLineColor(kGreen+1)
            h.SetFillColor(kGreen+1)
            if not added_to_legend:
                legend.AddEntry(h,'ZJetsToNuNu','F')
                added_to_legend = True

        elif eventtype == 'WJetsToLNu':
            h.SetLineColor(kGreen+3)
            h.SetFillColor(kGreen+3)
            if not added_to_legend:
                legend.AddEntry(h,'WJetsToLNu','F')
                added_to_legend = True
        """
        elif file.find('pMSSM') != -1:
            h.Scale(10000)
            h.SetLineColor(kBlue)
            h.SetFillColor(kBlue)
            if not added_to_legend:
                legend.AddEntry(h,'signal','l')
                added_to_legend = True
                """
        """
        rtstacks.cd()
        if name.find('2d')!= -1 and selection in selectionsets and (histtype not in processed):
            for pad in pads:
                pad.SetLogy(0)
            processed.append(histtype)
            switch = 1
            for sel in selectionsets:
                canvas.cd(switch)
                canvas.SetLogy(0)
                if switch % min(6,len(selectionsets)) ==0:
                    switch = 1
                else:
                    switch +=1
                h=histfile.Get('h'+histtype+'_'+sel+'_weighted')
                h.Draw('hist colz')
                h.GetXaxis().SetTitle(format_stacks[histtype][0])
                h.GetYaxis().SetTitle(format_stacks[histtype][1])
                h.SetMinimum(1.)#(1./10,50*stacks[stack][selection].GetMaximum())
                h.SetTitle(histtype+'_'+sel)
                h.Write('hist_'+eventtype[:eventtype.find('.root')]+'_'+histtype+'_'+sel)
            canvas.Write(eventtype[:eventtype.find('.root')]+'_'+histtype)
,            canvas.SaveAs('plots/stacked_plots/'+histtype+'/'+eventtype[:eventtype.find('.root')]+'_'+histtype+'.pdf')
            for pad in pads:
                pad.SetLogy()
                """
        rtstacks.cd()

        if selection in selectionsets:
            stacks[histtype][selection].Add(h)
c2 = mkcanvas('c2')
c2.Divide(2,3)

a = TPad()
b = TPad()
c = TPad()
d = TPad()
e = TPad()
pads2 = [a,b,c,d,e]
for pad in pads2:
    pad.SetLogz()
hists = {}
#for pad in pads2:
#    pad.SetLogy(0)
for histo in ['2dHTMET','2dTrkPtVsIso','2dTrkPtVsIsoXPt']:
    switch = 1
    for ix,file in enumerate(glob('output/categorized/*.root')):
        eventtype = file.split('/')[-1]
        eventtype = eventtype[:file.find('.root')]
        histfile = TFile(file)
#        histfile.cd()
        rtstacks.cd()
        
        hists[ix] = histfile.Get('h'+histo+'_tight_weighted').Clone()
        c2.cd(switch)
        if switch % 6==0:
            switch = 1
        else:
            switch +=1
#        rtstacks.cd()
        hists[ix].Draw('hist colz')
        c2.Update()
        hists[ix].GetXaxis().SetTitle(format_stacks[histtype][0])
        hists[ix].GetYaxis().SetTitle(format_stacks[histtype][1])
        hists[ix].SetMinimum(1.)#(1./10,50*stacks[stack][selection].GetMaximum())
        hists[ix].SetTitle(histo+'_'+eventtype+'_tight_weighted')
        hists[ix].SetStats(False)
#        hist.Write('hist_'+eventtype+'_'+histo+'_tight_weighted')
    c2.Write(histo+'_tight_weighted')
    command = 'mkdir /nfs/dust/cms/user/mrowietm/CMSSW_8_0_25/src/master/analysis/plots/stacked_plots/'+histo
    """
    try:
        system(command)
    except:
        print "Can't create directory, it already exists."
        """
    c2.SaveAs('plots/stacked_plots/'+histo+'/'+histo+'_tight_weighted'+'.pdf')
#for pad in pads:
#    pad.SetLogy()
     


for stack in stacks:#'MET','HT',...
    switch = 1
    canvas.Clear('D')#clears all pads
#    empty_pads()
#    command = 'mkdir /nfs/dust/cms/user/mrowietm/CMSSW_8_0_25/src/master/analysis/plots/stacked_plots/'+stack
#    print command
#    system(command)
#and (len(selection[selection.find('no'+stack):selection.find('no'+stack)+2+len(stack)]) != len(selection[selection.find('no'+stack):])))
    for selection in selectionsets:#mac 'nocuts','baseline',...
        if selection.find('_') != -1:
            if (selection.find('no'+stack) == -1) and (selection.find('TrkQl') == -1) or (len(selection[selection.find('no'+stack):selection.find('no'+stack)+2+len(stack)]) != len(selection[selection.find('no'+stack):])):
                continue
                
        canvas.cd(switch)
#        pads[switch-1]=canvas.cd(switch)
#        pads[switch-1].SetLogy()
        if switch % 4 !=0:
            switch+=1
        else:
            switch = 1
        sighist = signalfile.Get('h'+stack+'_'+selection)
        
        sighist.SetStats(False)
        stacks[stack][selection].Draw('hist')
        canvas.Update()
        stacks[stack][selection].GetXaxis().SetTitle(format_stacks[stack][0])
        stacks[stack][selection].GetYaxis().SetTitle(format_stacks[stack][1])
        stacks[stack][selection].SetMinimum(1.)#(1./10,50*stacks[stack][selection].GetMaximum())
        stacks[stack][selection].SetTitle(stack+'_'+selection)
        stacks[stack][selection].Write('hist_'+stack+'_stack_'+selection)
        sighist.Draw('hist same')
        legend.Draw('same')
        canvas.Update()
    
    command = 'mkdir /nfs/dust/cms/user/mrowietm/CMSSW_8_0_25/src/master/analysis/plots/stacked_plots/'+stack
    """
    try:
       system(command)
    except:
        print "Can't create directory, it already exists."
        """
    canvas.SaveAs('plots/stacked_plots/'+stack+'/'+stack+'_stack.pdf')#_'+selection+'.pdf')
#        canvas.SaveAs('plots/stacked_plots/'+stack+'/'+stack+'_stack_'+selection+'.eps')

    canvas.Write(stack+'_stack_')#+selection)
#        pause()


#    pause()



