import sys
#import tkinter as tk

#gets file names from command line
fsa = sys.argv[1];
text = sys.argv[2];

#open files and get strings from said files

fsaFile = open(fsa, "r")
textFile = open(text, "r")

fsaString = fsaFile.readline()
textString = textFile.readline()

fsaArray = fsaString.split(';')
fsaArray = fsaArray[:-1]
print(fsaArray)

#split fsa into its different parts




#create graphic of fsa using fsa

#determine if text is legal using fsa adjaceny matrix



