import tkinter as tk
from tkinter.font import BOLD
type = 0
from turtle import color
resourcenum = 1
filename= "FILE NAME HERE"
resourcenumstr = str(resourcenum)

def addresourcecommand():
    global type
    global resourcenum
    value = resourcenameentry.get()
    error = False
    resourcenameentry.delete(0, tk.END)
    if type == 0:
        value2 = resourcecountentry.get()
        resourcecountentry.delete(0, tk.END)
        print(value2)
        try: 
            int(value2)
        except ValueError:
            error = True
        if int(value2) <= 0:
           error = True
    
    

    if error == False:
        resourcenum+=1
        resourcenumstr = str(resourcenum)
        if resourcenum <10:
            resourcenumstr = "0"+str(resourcenum)
        resourcenumlabel["text"] = "Resource "+resourcenumstr+":"

def checkcountcommand():
    global type
    if resourcetypebutton["text"] != "Checklist":
         resourcetypebutton["text"] = "Checklist"
         type = 1
    else:
        resourcetypebutton["text"] = "Count"
        type = 0
if resourcenum <10:
    resourcenumstr = "0"+str(resourcenum)
resourcemanagersetup = tk.Tk()
frame1 = tk.Frame(resourcemanagersetup).pack(anchor="w",side="left")
frame2 = tk.Frame(resourcemanagersetup).pack(side="bottom",anchor="w",pady=5)
resourcemanagersetup.title("resource manager "+str(filename)+" setup")
resourcenumlabel = tk.Label(frame1,text="Resource "+resourcenumstr+":",font=("Helevitica","17",BOLD),justify="left")
resourcenamelabel = tk.Label(frame1,text="Name:",font=("Helevitica","17"))
resourcenameentry =tk.Entry(frame1,width=30,justify="left")
resourcetypebutton = tk.Button(frame1,text="Count",command=checkcountcommand,font=("Helevitica","17"),bg="#0050EF")
resourcecountlabel = tk.Label(frame1,text="Count needed(Int)",font=("Helevitica","17",BOLD),justify="left")
resourcecountentry = tk.Entry(frame1,width=30)
finishsetupbutton = tk.Button(frame2,text="Finish setup",command=addresourcecommand,font=("Helevitica","17"),bg="#008A00").pack(side="right",anchor="s",pady=10)
addresourcebutton = tk.Button(frame2,text="Add resource",command=addresourcecommand,font=("Helevitica","17"),bg="#0050EF").pack(side="bottom",anchor="w",pady=10)
while True:
    resourcemanagersetup.update()
    resourcenumlabel.pack(anchor="w")
    resourcenamelabel.pack(anchor="w",pady=5)
    resourcenameentry.pack(anchor="w",pady=5)
    resourcetypebutton.pack(anchor="w",pady=5)

    if type == 0:
        resourcecountlabel.pack(anchor="w")
        resourcecountentry.pack(anchor="w")
    else:
        resourcecountlabel.pack_forget()
        resourcecountentry.pack_forget()