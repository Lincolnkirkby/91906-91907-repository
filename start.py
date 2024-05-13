from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD
import os
import subprocess

if not os.path.exists("allsavenames"):
   with open("allsavenames", 'w') as file:
      pass
   

with open("allsavenames", 'r') as file:
    templist = file.readlines()
savenames = []
for x in templist:
    savenames.append(x.strip("\n"))

def new():
   root.destroy()
   loadwindow.destroy()
   subprocess.call(["python", "settings.py"])

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


root = tk.Tk()
root.title("Resource Manager Start")
label = tk.Label(root,text="Welcome!",font=("Helevitica","18",BOLD)).pack(anchor="w",padx=20,pady=5)
label2 = tk.Label(root,text="If you have already set up a Resource you may press the 'Load' button and select the name of the file you saved it to, or if this is your first time or you want to set up a new Resource press the 'New' button.",font=("Helevitica","12"),wraplength=400,justify="left").pack(anchor="w",padx=5,pady=5)
button1 = tk.Button(root,text="Load",font=("Helevitica","17",BOLD),width=10,bg="#008A00",fg="#fff",command=loadopen).pack(side="left",anchor="s",padx=5,pady=5)
button2 = tk.Button(root,text="New",font=("Helevitica","17",BOLD),width=10,bg="#0050EF",fg="#fff",command=new).pack(side="right",anchor="s",padx=5,pady=5)

loadwindow = tk.Tk()
loadwindow.title("Load screen")
loadlabel = tk.Label(loadwindow,text="Filename:",font=("Helevitica","18",BOLD)).pack(anchor="w")
loadcombo = ttk.Combobox(loadwindow,values=savenames)
loadcombo.pack(anchor="w")
loadbutton = tk.Button(loadwindow,text="Load",font=("Helevitica","16",BOLD),bg="#008A00",width=8,fg="#fff",command=load).pack(anchor="w",padx=10,pady=15)
loadwindow.iconify()

while True:
    root.update()
