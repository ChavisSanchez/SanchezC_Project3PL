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

output = textString
if legal == True:
    output = output + " is a valid string"
else:
    output = output + " is not a valid string"
#create graphic of fsa using fsa


root = Tk()
root.title("FSA Processor")
root.geometry("400x600")
c = Canvas(root, width = 400, height = 600, borderwidth = 0, highlightthickness = 0, bg = "black")
c.pack()

c.create_text(250, 20, text = output, fill = "white")
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
c.create_line(radius + 30, radius/2, 50, radius/2, arrow = LAST, width = 2, fill = "white")
for i in range(len(links)):
    currentState = int(links[i][1])
    nextState = int(links[i][3])
    #if next state == current state
    if nextState == currentState:
        c.create_arc((temp * radius) + 60, (temp * radius) - 50, (temp * radius) - 80, (temp * radius) - 20, start = 90, extent = -180, outline = "white", width = 2, style = "arc")
        c.create_text((temp * radius) + 65, (temp * radius) - 45, text = links[i][5], fill = "white")
    #if next state is +1 from current state
    if nextState == (currentState + 1):
        c.create_line((temp * radius) - 15, (temp * radius) - 15, (temp * radius) + 15, (temp * radius) + 15, arrow = LAST, width = 2, fill = "white")
        c.create_text((temp * radius) + 6, (temp * radius) - 6, text = links[i][5], fill = "white")
        temp = temp + 1
    #if next state is behind cirrent state
    if nextState < currentState:
        c.create_line((temp * radius) - 25, (temp * radius), radius + 30, (temp * radius), width = 2, fill = "white")
        c.create_line(temp * 18, temp * 22, temp * 18, radius * temp, arrow = FIRST, width = 2, fill = "white")
        c.create_text((temp * 18) - 6, (temp * 22) + 20, text = links[i][5], fill = "white")


root.mainloop()
