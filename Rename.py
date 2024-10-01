import os
import re

def renameFiles(filename):
    filenameArray = filename.split("\\")
    fn = filenameArray[len(filenameArray)-1]
    endung = fn.split(".")[1]
    fn = fn.split(".")[0]
    newFilename = re.sub(r'\W+', '_', fn)
    filenameArray[len(filenameArray)-1] = newFilename
    newFilename = "\\".join(filenameArray)
    newFilename = newFilename + "." + endung
    
    os.rename(filename, newFilename)

def goThroughFiles(foldername):
    if os.path.isdir(foldername) == True:
        for filename in os.listdir(foldername):
            if os.path.isdir(foldername) == True:
                goThroughFiles(foldername + "\\" + filename)
            else:
                renameFiles(filename)
    else:
        renameFiles(foldername)

        
foldername = "data"
goThroughFiles(foldername)
