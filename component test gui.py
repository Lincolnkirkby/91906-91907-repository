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
print(names)
filename= "FILE NAME HERE"
with open(filename+"values", 'r') as file:
    templist = file.readlines()
values = []
for x in templist:
    values.append(x.strip("\n"))
print(values)

componentlist = []
title = tk.Label(root,text=filename+":",font=("Helevitica","17",BOLD))
num = 0
for x in names:
    x = tk.Label(root,text=x+":",font=("Helevitica","17"))
    componentlist.append(x)
    if int(values[num]) == -1:
        y = tk.Checkbutton(root,text="completed?")
        componentlist.append(y)
    else:
        y = tk.Label(root,text="0/"+values[num],font=("Helevitica","17"))
        buttonframe = tk.Frame(root)
        a = tk.Button(buttonframe,font=("Helevitica","17"),text="Value +1",bg="#008A00").pack(side="left")
        b = tk.Button(buttonframe,font=("Helevitica","17"),text="Value -1",bg="#E51400").pack()
        c = tk.Button(buttonframe,font=("Helevitica","17"),text="Config",bg="#647687").pack(side="right")
        componentlist.append(y)
        componentlist.append(buttonframe)

    num+=1
    print(componentlist)

while True:
    title.pack(anchor="w")
    num = 0
    for x in componentlist:
        x.pack(anchor="w")
    root.update()