import os
from ZIP import extract_files
from ParseXML import parseXML
from ZIP import zip_files

def convert(file):
    print(file)
    if file.endswith(".zip"):
        extract_files(file)
        dir = file[:-4]
        parseXML(dir + "/imsmanifest.xml")
        zip_files(dir)
    else:
        return

def goThroughFiles(foldername):
    if os.path.isdir(foldername) == True:
        for filename in os.listdir(foldername):
            if os.path.isdir(foldername) == True:
                goThroughFiles(foldername + "\\" + filename)
            else:
                convert(foldername + "\\" + filename)
    else:
        convert(foldername)

foldername = "data"
goThroughFiles(foldername)
