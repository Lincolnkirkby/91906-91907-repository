from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD
import subprocess
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

def goback():
    loadwindow.destroy()
    root.destroy()
    subprocess.call(["python", "start.py"])
  

def config():
    loadwindow.destroy()
    root.destroy()
    subprocess.call(["python", "fileconfig.py"])

def save():
    with open(filename+"save", "w") as file:
        file.write(str(export))


def load():
   filename = loadcombo.get()
   print(filename)
   if filename!="":
    with open("savenames", 'w') as file:
        file.write(filename)
    loadwindow.destroy()
    root.destroy()
    subprocess.call(["python", "runfile.py"])


def loadopen():
    if loadwindow.state() == "iconic":
      loadwindow.deiconify()
    else:
      loadwindow.iconify()

def generatebuttons(num,cond):
    global numnum
    global componentlist
    global values
    global currentvalue
    global ylist
    if numnum<len(names):
        x = tk.Label(root,text=names[num]+":",font=("Helevitica","17"))
        componentlist.append(x)
        print(values)
        if int(values[num]) >0:
            y = tk.Label(root,text=str(currentvalue[num])+"/"+str(values[num]),font=("Helevitica","17"))
            buttonframe = tk.Frame(root)
            b = tk.Button(buttonframe,font=("Helevitica","17"),text="Value -1",bg="#E51400",fg="#fff",command=lambda:generatebuttons(num,"minus")).pack(anchor="s",pady=2,side="right",padx=8)
            a = tk.Button(buttonframe,font=("Helevitica","17"),text="Value +1",bg="#008A00",fg="#fff",command=lambda:generatebuttons(num,"plus")).pack(anchor="s",pady=2,side="right",padx=8)
            numnum+=1
            ylist.append(y)
            componentlist.append(y)
            componentlist.append(buttonframe)

            generatebuttons(numnum,False)
        else:
            a = tk.IntVar()
            y = tk.Checkbutton(root,text="completed?",font=("Helevitica","17"),variable=a,command=lambda:generatebuttons(num,"swap"))
            componentlist.append(y)
            intvarlist[num] = a
            numnum+=1
            ylist.append(y)
            generatebuttons(numnum,False)
    else:
        if num <len(names):
            if cond == "plus":
                currentvalue[num] +=1
            if cond == "minus":
                if currentvalue[num] >0:
                    currentvalue[num] -=1
            if cond == "swap":
                currentvalue[num] = intvarlist[num].get()
        else: 
            for x in range(len(names)):
                if intvarlist[x]!=0:
                    intvarlist[x].set(currentvalue[x])
        print(currentvalue)
            
generatebuttons(0,False)

title = tk.Label(root,text=filename+":",font=("Helevitica","17",BOLD))

buttonframe = tk.Frame(root)
buttonframe2 = tk.Frame(root)
configbutton = tk.Button(buttonframe,text="Config",bg="#647687",fg="#fff",width=8,font=("Helevitica","20"),command=config).pack()
removebutton = tk.Button(buttonframe,text="return",bg="#E51400",fg="#fff",width=8,font=("Helevitica","20"),command=goback).pack()
savebutton = tk.Button(buttonframe2,font=("Helevitica","20"),text="Save",bg="#008A00",fg="#fff",width=8,command=save).pack()
loadopenbutton = tk.Button(buttonframe2,font=("Helevitica","20"),text="Load",bg="#0050EF",fg="#fff",width=8,command=loadopen).pack()


loadwindow = tk.Tk()
loadwindow.title("Load screen")
loadlabel = tk.Label(loadwindow,text="Filename:",font=("Helevitica","18",BOLD)).pack(anchor="w")
loadcombo = ttk.Combobox(loadwindow,values=savenames)
loadcombo.pack(anchor="w")
loadbutton = tk.Button(loadwindow,text="Load",font=("Helevitica","16",BOLD),bg="#008A00",width=8,fg="#fff",command=load).pack(anchor="w",padx=10,pady=15)
loadwindow.iconify()

while True:
    title.pack(anchor="w",pady=2)
    ynum = 0
    for y in ylist:
        if y["text"] != "completed?":
            y["text"] = str(currentvalue[ynum])+"/"+str(values[ynum])
        ynum+=1

    for x in componentlist:
        x.pack(anchor="w",pady=2)
    buttonframe.pack(anchor="se",side="right")
    buttonframe2.pack(anchor="sw",side="left")
   
    root.update()