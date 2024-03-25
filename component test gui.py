import tkinter as tk
from tkinter.font import BOLD
templist = []
root = tk.Tk()
filename= "FILE NAME HERE"
with open("savenames.txt", 'r') as file:
    filename = file.readlines()
root.title(filename)
with open(filename+"names", 'r') as file:
    templist = file.readlines()
names = []
for x in templist:
    names.append(x.strip("\n"))
#print(names)
filename= "FILE NAME HERE"
with open(filename+"values", 'r') as file:
    templist = file.readlines()
values = []
for x in templist:
    values.append(int(x.strip("\n")))
#print(values)
componentlist = []
numnum = 0
currentvalue = []
for x in values:
    currentvalue.append(0)
ylist = []
def generatebuttons(num,positive):
    global numnum
    global componentlist
    global values
    global currentvalue
    global ylist
    if numnum<len(names):
        x = tk.Label(root,text=names[num]+":",font=("Helevitica","17"))
        componentlist.append(x)
        if values[num] >0:
            y = tk.Label(root,text=str(currentvalue[num])+"/"+str(values[num]),font=("Helevitica","17"))
            buttonframe = tk.Frame(root)
            c = tk.Button(buttonframe,font=("Helevitica","17"),text="Config",bg="#647687").pack(anchor="s",pady=2,side="right",padx=8)
            b = tk.Button(buttonframe,font=("Helevitica","17"),text="Value -1",bg="#E51400",command=lambda:generatebuttons(num,False)).pack(anchor="s",pady=2,side="right",padx=8)
            a = tk.Button(buttonframe,font=("Helevitica","17"),text="Value +1",bg="#008A00",command=lambda:generatebuttons(num,True)).pack(anchor="s",pady=2,side="right",padx=8)
            numnum+=1
            ylist.append(y)
            componentlist.append(y)
            componentlist.append(buttonframe)

            generatebuttons(numnum,False)
        else:
            y = tk.Checkbutton(root,text="completed?",font=("Helevitica","17"))
            componentlist.append(y)
            numnum+=1
            ylist.append(y)
            generatebuttons(numnum,False)
    else:
        if num <len(names):
            if positive == True:
                currentvalue[num] +=1
            if positive == False:
                if currentvalue[num] >0:
                    currentvalue[num] -=1
            
generatebuttons(0,False)

title = tk.Label(root,text=filename+":",font=("Helevitica","17",BOLD))

savebutton = tk.Button(root,font=("Helevitica","20"),text="Save",bg="#008A00",width=8)
loadbutton = tk.Button(root,font=("Helevitica","20"),text="Load",bg="#0050EF",width=8)

while True:
    title.pack(anchor="w",pady=2)
    ynum = 0
    for y in ylist:
        if y["text"] != "completed?":
            y["text"] = str(currentvalue[ynum])+"/"+str(values[ynum])
        ynum+=1

    for x in componentlist:
        x.pack(anchor="w",pady=2)
    loadbutton.pack(anchor="s",pady=2,side="right",padx=8)
    savebutton.pack(anchor="w",pady=2,side="bottom",padx=8)
    root.update()