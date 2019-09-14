from jobSubmitterCT import jobSubmitterCT

def submitJobs():  
    mySubmitter = jobSubmitterCT()
    mySubmitter.run()
    
if __name__=="__main__":
    submitJobs()