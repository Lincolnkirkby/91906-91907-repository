import tkinter as tk
from tkinter.font import BOLD
templist = []
root = tk.Tk()
filename= "FILE NAME HERE"
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
    values.append(x.strip("\n"))
#print(values)

def numberbig(name):
    print(name)


componentlist = []
title = tk.Label(root,text=filename+":",font=("Helevitica","17",BOLD))
num = 0
for x in names:
    nm = 1
    x = tk.Label(root,text=x+":",font=("Helevitica","17"))
    componentlist.append(x)
    if int(values[num]) == -1:
        y = tk.Checkbutton(root,text="completed?",font=("Helevitica","17"))
        componentlist.append(y)
    else:
        y = tk.Label(root,text="0/"+values[num],font=("Helevitica","17"))
        buttonframe = tk.Frame(root)
        a = tk.Button(buttonframe,font=("Helevitica","17"),text="Value +1",bg="#008A00",command=lambda:numberbig(nm)).pack(side="left",padx=2)
        b = tk.Button(buttonframe,font=("Helevitica","17"),text="Value -1",bg="#E51400",command=lambda:numberbig(nm)).pack(anchor="w",side = "left",padx=2)
        c = tk.Button(buttonframe,font=("Helevitica","17"),text="Config",bg="#647687").pack(side="right",padx=2)
        componentlist.append(y)
        componentlist.append(buttonframe)

    num+=1
    #print(componentlist)

savebutton = tk.Button(root,font=("Helevitica","20"),text="Save",bg="#008A00",width=8)
loadbutton = tk.Button(root,font=("Helevitica","20"),text="Load",bg="#0050EF",width=8)

while True:
    title.pack(anchor="w",pady=2)
    num = 0
    for x in componentlist:
        x.pack(anchor="w",pady=2)
    loadbutton.pack(anchor="s",pady=2,side="right",padx=8)
    savebutton.pack(anchor="w",pady=2,side="bottom",padx=8)
    root.update()