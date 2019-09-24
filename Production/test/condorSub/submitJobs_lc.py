from jobSubmitterLC import jobSubmitterLC

def submitJobs():  
    mySubmitter = jobSubmitterLC()
    mySubmitter.run()
    
if __name__=="__main__":
    submitJobs()