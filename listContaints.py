import os
def listOfFiles(path,noOfDash):
    for files                                                                                                                      in os.listdir(path):
        print("-"*noOfDash,files)
        #print(os.path.join(path,files))
        if os.path.isdir(os.path.join(path,files)):
            listOfFiles(os.path.join(path,files),noOfDash*2)
            

listOfFiles("E:\\Python\\test",1)
