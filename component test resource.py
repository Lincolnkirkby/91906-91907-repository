import tkinter as tk
from tkinter.font import BOLD
from turtle import color
def testcommand():
    if resourcetypebutton["text"] != "Checklist":
         resourcetypebutton["text"] = "Checklist"
    else:
        resourcetypebutton["text"] = "Count"
filename= "FILE NAME HERE"
resourcenum = 1
resourcenumstr = str(resourcenum)
if resourcenum <10:
    resourcenumstr = "0"+str(resourcenum)
resourcemanagersetup = tk.Tk()
resourcemanagersetup.title("resource manager "+str(filename)+" setup")
resourcenumlabel = tk.Label(master=resourcemanagersetup,text="Resource "+resourcenumstr+":",font=("Helevitica","15",BOLD),justify="left").grid(row=0,column=0)
resourcenamelabel = tk.Label(master=resourcemanagersetup,text="Name:",font=("Helevitica","15")).grid(row=1,column=0)
resourcenameentry =tk.Entry(master=resourcemanagersetup,width=30).grid(row=2,column=0)
resourcetypebutton = tk.Button(master=resourcemanagersetup,text="Count",command=testcommand,font=("Helevitica","15"),bg="#0050EF")
resourcetypebutton.grid(row=3)
while True:
    resourcemanagersetup.update()