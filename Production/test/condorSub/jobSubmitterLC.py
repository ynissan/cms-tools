from Condor.Production.jobSubmitter import *
from glob import glob
import os
import time
import commands

slimmedProductionPath = "srm://dcache-se-cms.desy.de/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/SlimmedProduction/"

class jobSubmitterLC(jobSubmitter):
    def __init__(self,argv=None,parser=None):
        super(jobSubmitterLC,self).__init__(argv, parser)
        self.scripts = ["step1.sh","step2_lc.sh"]
        
    def addExtraOptions(self,parser):
        super(jobSubmitterLC,self).addExtraOptions(parser)
        parser.add_option("-N", "--nFiles", dest="nFiles", default=1, help="number of files to process (default = %default)")
        parser.add_option("-J", "--nFilesPerJob", dest="nFiles", default=1, help="number of files to process per job (default = %default)")
        parser.add_option("-o", "--output", dest="output", default="", help="path to output directory in which root files will be stored (required) (default = %default)")
        parser.add_option("-d", "--dicts", dest="dicts", type="string", action="callback", callback=list_callback, default=None,
            help="comma-separated list of input sample names (default = %default)")
    
    def checkExtraOptions(self,options,parser):
        super(jobSubmitterLC,self).checkExtraOptions(options,parser)
        
        if len(options.output)==0:
            options.output = "srm://dcache-se-cms.desy.de/pnfs/desy.de/cms/tier2/store/user/ynissan/NtupleHub/LeptonCollection/"
    
    def generateExtra(self,job):
        super(jobSubmitterLC,self).generateExtra(job)
        job.patterns.update([
            ("JOBNAME",job.name+"_$(Process)_$(Cluster)"),
            ("EXTRAINPUTS","input/args_"+job.name+"_$(Process).txt"),
            ("EXTRAARGS","-j "+job.name+" -p $(Process) -o "+self.output),
        ])
        
    
    def generateSubmission(self):
        # create protojob
        job = protoJob()
        job.name = "leptonCollection"
        self.generatePerJob(job)
        print "Wanted dicts", self.dicts
        self.timenow = int(time.time())
        print "Getting files in SlimmedProduction..."
        status, out = commands.getstatusoutput('gfal-ls ' + slimmedProductionPath)
        print "Getting files existing in LeptonCollection..."
        status, existingOut = commands.getstatusoutput('gfal-ls ' + self.output)
        existingFiles = existingOut.split("\n")
        for file in out.split("\n"):
            if file in existingFiles:
                print "File", file, " alreading exists. Skipping."
            if self.dicts is not None and len(options.dicts) > 0:
                shouldProcess = False
                for dict in self.dicts:
                    if dict in file:
                        shouldProcess = True
                        break
                if not shouldProcess:
                    continue
            print "Adding job for file=" + file
            job.njobs += 1
            if self.count and not self.prepare:
                continue
            job.nums.append(job.njobs-1)
            # just keep list of jobs
            if self.missing and not self.prepare:
                continue
        
            # write job options to file - will be transferred with job
            if self.prepare:
                jname = job.makeName(job.nums[-1])
                with open("input/args_"+jname+".txt",'w') as argfile:
                    id = file.split("_")[-1].split(".")[0]
                    basename = os.path.basename(file)
                    config_out = defaultModeLocations['def'] + "/" + file
                    args = config_out
                    argfile.write(args)
            
        
        job.queue = "-queue "+str(job.njobs)
        print "Job queue", job.queue
        self.protoJobs.append(job)