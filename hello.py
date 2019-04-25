import os
import re
import shutil
import operator
import tkinter
from tkinter import filedialog
from tkinter import simpledialog
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
    dirPath = Path(filedialog.askdirectory(title = 'Select directory to sort...'))
    fileSplit = simpledialog.askstring("Split Selector", "Enter a delimiting string")
    fileSplit.strip()
    splitWithWhiteSpace = " " + fileSplit + " ", " " + fileSplit, fileSplit + " ", fileSplit
    delimiters= '|'.join(map(re.escape, splitWithWhiteSpace))
    #List all files that aren't folders
    dirList = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
    if(not dirList):
        print("No files in directory. Enter a different path value: ")
        return
    #Now, for each file in the list, split it into folder name and file name.
    fileList = []
    for dirFile in dirList:
        fileObj = (re.split(delimiters, dirFile))
        fileList.append(fileUnion(dirFile, fileObj[0],fileObj[1]))

    #Next, sort the list by folder name, to make it easier to match files
    #This will make it so all files with the same folder name are next
    #To each other
    fileList.sort(key=operator.attrgetter('folderName'))

    #Now, we make folders for the files
    for currentFile in fileList:
        currentFolder = currentFile.folderName
        folderPath = dirPath / currentFolder

    #If the file belongs in the folder, put it in there.
        if(folderPath.is_dir()):
            (dirPath / currentFile.fullName).replace(folderPath/ currentFile.fileName)
    #If not, make a new folder, and put it in there.
        else:
            os.mkdir(folderPath)
            (dirPath / currentFile.fullName).replace(folderPath / currentFile.fileName)
        
if(__name__ == "__main__"):
    main()