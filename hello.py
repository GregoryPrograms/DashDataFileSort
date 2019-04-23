import os
import shutil
import operator
import tkinter
from tkinter import filedialog
from pathlib import Path

#File Union gives the whole description of a file, both the file and
#folder name.
class fileUnion:
    def __init__(self, fullName, folderName, fileName):
        self.fullName = fullName
        self.folderName = folderName
        self.fileName = fileName


def main():
    #First, get list of files.
    #To do this, we define the path to the files, as well as 
    #The character we use to split the file name and folder name.
    tkinter.Tk().withdraw() # Close the root window
    dirPath = filedialog.askopenfilename()
    fileSplit = " -- "
    #List all files that aren't folders
    dirList = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
    if(not dirList):
        print("No files in directory. Enter a different path value: ")
        return
    #Now, for each file in the list, split it into folder name and file name.
    fileList = []
    for dirFile in dirList:
        fileObj = (dirFile.split(fileSplit))
        fileList.append(fileUnion(dirFile, fileObj[0],fileObj[1]))

    #Next, sort the list by folder name, to make it easier to match files
    #This will make it so all files with the same folder name are next
    #To each other
    fileList.sort(key=operator.attrgetter('folderName'))

    #Now, we make folders for the files
    currentFolder = fileList[0].folderName
    fullPath = dirPath / currentFolder
    os.mkdir(fullPath)

    currentFile = dirPath / fileList[0].fullName
    print(currentFile.read_text())
    for currentFile in fileList:
    #If the file belongs in the folder, put it in there.
        if(currentFile.folderName == currentFolder):
            (dirPath / currentFile.fullName).replace(fullPath / currentFile.fileName)
    #If not, make a new folder, and put it in there.
        else:
            currentFolder = currentFile.folderName
            fullPath = dirPath / currentFolder
            os.mkdir(fullPath)
            (dirPath / currentFile.fullName).replace(fullPath / currentFile.fileName)
        
if(__name__ == "__main__"):
    main()