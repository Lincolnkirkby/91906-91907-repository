import tkinter as tk
from tkinter.font import BOLD
type = 0
from turtle import color
def testcommand():
    global type
    if resourcetypebutton["text"] != "Checklist":
         resourcetypebutton["text"] = "Checklist"
         type = 1
    else:
        resourcetypebutton["text"] = "Count"
        type = 0
filename= "FILE NAME HERE"
resourcenum = 1
resourcenumstr = str(resourcenum)
if resourcenum <10:
    resourcenumstr = "0"+str(resourcenum)
resourcemanagersetup = tk.Tk()
frame1 = tk.Frame(resourcemanagersetup).pack()
resourcemanagersetup.title("resource manager "+str(filename)+" setup")
resourcenumlabel = tk.Label(frame1,text="Resource "+resourcenumstr+":",font=("Helevitica","17",BOLD),justify="left").pack(anchor="w")
resourcenamelabel = tk.Label(frame1,text="Name:",font=("Helevitica","17")).pack(anchor="w")
resourcenameentry =tk.Entry(frame1,width=30,justify="left").pack(anchor="w")
resourcetypebutton = tk.Button(frame1,text="Count",command=testcommand,font=("Helevitica","17"),bg="#0050EF")
resourcetypebutton.pack(anchor="w")
resourcecountlabel = tk.Label(frame1,text="Count needed(Int) "+resourcenumstr+":",font=("Helevitica","17",BOLD),justify="left")
resourcecountentry = tk.Entry(frame1,width=30)
frame2 = tk.Frame(resourcemanagersetup).pack(side="bottom")
addresourcebutton = tk.Button(frame2,text="Add resource",command=testcommand,font=("Helevitica","17"),bg="#0050EF").pack(side="left")
finishsetupbutton = tk.Button(frame2,text="Finish setup",command=testcommand,font=("Helevitica","17"),bg="#008A00").pack(side="right")
while True:
    resourcemanagersetup.update()
    if type == 0:
        resourcecountlabel.pack(anchor="w")
        resourcecountentry.pack(anchor="w")
    else:
        resourcecountlabel.pack_forget()
        resourcecountentry.pack_forget()