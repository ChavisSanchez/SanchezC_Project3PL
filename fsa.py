import sys
from tkinter import *

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

numOfStates = fsaArray[0]
alphabet = fsaArray[1].split(',')
links = fsaArray[2].split(',')
start = fsaArray[3]
accept = fsaArray[4].split(',')

print(numOfStates)
print(alphabet)
print(links)
print(start)
print(accept)

linkDic = {}

for item in links:
    item = item.strip('()')
    connection = item.split(':')
    key = connection[0] + ":" + connection[2]
    linkDic[key] = connection[1]

print(linkDic)

numOfStates = int(numOfStates)
start = int(start)

for i in range(len(accept)):
    accept[i] = int(accept[i])


legal = False;

current = start
textString.strip('\n')
for symbol in textString:
    if symbol not in alphabet:
        print("not in alphabet")
        legal = False
        break
    if str(current) + ":" + str(symbol) not in linkDic:
        print("not in links")
        legal = False
        break
    current = linkDic[str(current) + ":" + str(symbol)]

legal = int(current) in accept

print(legal)
print(linkDic)
#create graphic of fsa using fsa


root = Tk()
root.title("FSA Processor")
root.geometry("400x600")
c = Canvas(root, width = 400, height = 600, borderwidth = 0, highlightthickness = 0, bg = "black")
c.pack()

#create circles for FSA

radius = 30
x = 30
y = 30
for i in range(numOfStates):
    if i in accept:
        c.create_oval(x - radius, y - radius, x + radius, y + radius)
        c.create_oval(x - radius / 1.5, y - radius / 1.5, x + radius / 1.5, y + radius / 1.5)
    else:
        c.create_oval(x - radius, y - radius, x + radius, y + radius)
    c.create_text(x, y, text=i)
    x = x + 60
    y = y + 60

#show connections for FSA
temp = 1
radius = radius * 2
for i in linkDic:
    #if next state is +1 from current state
    c.create_line((temp * radius) - 15, (temp * radius) - 15, (temp * radius) + 15, (temp * radius) + 15, arrow = LAST, width = 2, fill = "white")
    temp = temp + 1




root.mainloop()
