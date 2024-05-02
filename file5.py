from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD
import subprocess



listofvals = []
listofnames = []
templist = []
root = tk.Tk()
filename= "FILE NAME HERE"
with open("savenames", 'r') as file:
    filename = str(file.readline())
root.title(filename)
with open(filename+"save", 'r') as file:
        info = file.readline()
        export = eval(info)

names = export["names"]
values = export["values"]
for x in templist:
    values.append(int(x.strip("\n")))
componentlist = []
numnum = 0
if "current" in export:
    currentvalue = export["current"]
else:
    currentvalue = []
    for x in values:
        currentvalue.append(0)
    export["current"] = currentvalue
ylist = []
intvarlist = []
for x in values:
    intvarlist.append(0)
with open("allsavenames", 'r') as file:
    templist = file.readlines()
savenames = []
for x in templist:
    savenames.append(x.strip("\n"))

def unsave():
    with open("savenames", 'w') as file:
        file.write(filename)
    root.destroy()
    subprocess.call(["python", "91906-91907-repository\\file4.py"])

def save():
    global export
    export["names"] = []
    export["values"] = []
    for x in listofnames:
        export["names"].append(componentlist[x-1].get())
    for x in listofvals:
        export["values"].append(componentlist[x-1].get())
    print(names)
    print(export)
    with open(filename+"save", "w") as file:
        file.write(str(export))
    with open("savenames", 'w') as file:
        file.write(filename)
    root.destroy()
    subprocess.call(["python", "91906-91907-repository\\file4.py"])

truenum = 0
def generatebuttons(num,cond):
    global truenum
    global numnum
    global componentlist
    global values
    global ylist
    if numnum<len(names):
        x = tk.Entry(root,text=names[num]+":",font=("Helevitica","17"))
        x.insert(0,names[num])
        w = tk.Label(root,text="new name value ^, old:"+names[num],font=("Helevitica","17"))
        componentlist.append(x)
        truenum +=1
        listofnames.append(truenum)
        componentlist.append(w)
        truenum +=1
        if int(values[num]) >0:
            y = tk.Entry(root,font=("Helevitica","17"))
            y.insert(0,str(values[num]))
            x = tk.Label(root,font=("Helevitica","17"),text = "new maximum value ^, old:"+values[num])

            numnum+=1
            componentlist.append(y)
            truenum +=1
            listofvals.append(truenum)
            componentlist.append(x)
            truenum +=1

            generatebuttons(numnum,False)
        else:
            numnum+=1
            generatebuttons(numnum,False)
    else:
        print(currentvalue)
            
generatebuttons(0,False)

title = tk.Label(root,text=filename+":",font=("Helevitica","17",BOLD))

dontsavebutton = tk.Button(root,font=("Helevitica","20"),text="Return",bg="#E51400",fg="#fff",width=8,command=unsave)
savebutton = tk.Button(root,font=("Helevitica","20"),text="Save and return",bg="#008A00",fg="#fff",width=12,command=save)



while True:
    title.pack(anchor="w",pady=2)
    allvalues = []
    for x in componentlist:
        x.pack(anchor="w",pady=2)
    savebutton.pack(anchor="w",pady=2,side="bottom",padx=8)
    dontsavebutton.pack(anchor="w",pady=2,side="bottom",padx=8)
    root.update()