from jobSubmitterSetup import jobSubmitterSetup

def submitJobs():  
    mySubmitter = jobSubmitterSetup()
    mySubmitter.run()
    
if __name__=="__main__":
    submitJobs()