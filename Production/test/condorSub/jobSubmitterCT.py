from Condor.Production.jobSubmitter import *
from glob import glob
import os

defaultModeLocations = {
    "def" : "srm://dcache-se-cms.desy.de/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/def/"
}

class jobSubmitterCT(jobSubmitter):
    def addExtraOptions(self,parser):
        super(jobSubmitterCT,self).addExtraOptions(parser)
        self.removeOptions(parser,"-m")
        print "Parser after remove:", parser
        parser.add_option("-m", "--mode", dest="mode", default="", help="mode to run (required) (default = %default)")
        parser.add_option("-o", "--output", dest="output", default="", help="path to output directory in which root files will be stored (required) (default = %default)"
    
    def checkExtraOptions(self,options,parser):
        super(jobSubmitterCT,self).checkExtraOptions(options,parser)
        
        if len(options.mode)==0 or options.mode not in ("def", "aod", "miniaod", "ntuples"):
            parser.error("Required option: --mode [mode]")
        
        if len(options.output)==0:
            options.output = defaultModeLocations[options.mode]
    
    def generateExtra(self,job):
        super(jobSubmitterCT,self).generateExtra(job)
        job.patterns.update([
            ("JOBNAME",job.name+"_$(Process)_$(Cluster)"),
            ("EXTRAINPUTS","input/args_"+job.name+"_$(Process).txt"),
            ("EXTRAARGS","-j "+job.name+" -p $(Process) -o "+self.output),
        ])
    
    def generateSubmission(self):
        # create protojob
        job = protoJob()
        job.name = self.mode
        self.generatePerJob(job)
        
        modelLocation = os.path.expandvars("$CMSSW_BASE/src/Configuration/Generator/python")
        for file in glob(modelLocation + "/*"):
            print "Adding job for file=" + file
            job.njobs += 1
            if self.count and not self.prepare:
                continue
        