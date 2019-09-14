from Condor.Production.jobSubmitter import *

class jobSubmitterCT(jobSubmitter):
    def addExtraOptions(self,parser):
        super(jobSubmitterCT,self).addExtraOptions(parser)
    
    def checkExtraOptions(self,options,parser):
        super(jobSubmitterCT,self).checkExtraOptions(options,parser)
    
    def generateExtra(self,job):
        super(jobSubmitterTM,self).generateExtra(job)
        job.patterns.update([
            ("JOBNAME",job.name+"_$(Process)_$(Cluster)"),
            ("EXTRAINPUTS","input/args_"+job.name+"_$(Process).txt"),
            ("EXTRAARGS","-j "+job.name+" -p $(Process) -o "+self.output),
        ])
    
    def generateSubmission(self):
        