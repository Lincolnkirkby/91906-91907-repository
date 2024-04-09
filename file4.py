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
#print(values)
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

with open("allsavenames", 'r') as file:
    templist = file.readlines()
savenames = []
for x in templist:
    savenames.append(x.strip("\n"))


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
    subprocess.call(["python", "91906-91907-repository\\file4.py"])


def loadopen():
    if loadwindow.state() == "iconic":
      loadwindow.deiconify()
    else:
      loadwindow.iconify()

def generatebuttons(num,positive):
    global numnum
    global componentlist
    global values
    global currentvalue
    global ylist
    if numnum<len(names):
        x = tk.Label(root,text=names[num]+":",font=("Helevitica","17"))
        componentlist.append(x)
        print(values)
        print(names)
        if int(values[num]) >0:
            y = tk.Label(root,text=str(currentvalue[num])+"/"+str(values[num]),font=("Helevitica","17"))
            buttonframe = tk.Frame(root)
            b = tk.Button(buttonframe,font=("Helevitica","17"),text="Value -1",bg="#E51400",fg="#fff",command=lambda:generatebuttons(num,False)).pack(anchor="s",pady=2,side="right",padx=8)
            a = tk.Button(buttonframe,font=("Helevitica","17"),text="Value +1",bg="#008A00",fg="#fff",command=lambda:generatebuttons(num,True)).pack(anchor="s",pady=2,side="right",padx=8)
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
        print(currentvalue)
            
generatebuttons(0,False)

title = tk.Label(root,text=filename+":",font=("Helevitica","17",BOLD))

configbutton = tk.Button(text="config",bg="#647687",fg="#fff",width=8,font=("Helevitica","20"))
savebutton = tk.Button(root,font=("Helevitica","20"),text="Save",bg="#008A00",fg="#fff",width=8,command=save)
loadopenbutton = tk.Button(root,font=("Helevitica","20"),text="Load",bg="#0050EF",fg="#fff",width=8,command=loadopen)


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
    configbutton.pack(anchor="s",pady=2,side="bottom",padx=8)
    loadopenbutton.pack(anchor="s",pady=2,side="right",padx=8)
    savebutton.pack(anchor="w",pady=2,side="bottom",padx=8)
    root.update()