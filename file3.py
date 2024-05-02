import tkinter as tk
from tkinter.font import BOLD
import subprocess
type = 0
from turtle import color
resourcenum = 1
filename = "FILE NAME HERE"
call1 = False
with open("savenames", 'r') as file:
    filename = str(file.readline())
print(filename)
resourcenumstr = str(resourcenum)
resourcemanagersetup = tk.Tk()
done = False
export= {
    "names" : [],
    "values" : []
}
error = ""
c = 0.0
c2 = 0
dir = "up"

def finish():
    global done
    with open(filename+"save", "w") as file:
        file.write(str(export))
    done = True
def addresourcecommand():
    global error
    global type
    global resourcenum
    global export
    value = resourcenameentry.get()
    error = ""
    if type == 0:
        value2 = resourcecountentry.get()
        resourcecountentry.delete(0, tk.END)
        try: 
            int(value2)
        except ValueError:
            error = "ERROR, NOT INT"
        if error == "":
           if int(value2) <= 0:
            error = "ERROR, INT must be greater than 0"
    if error == "":
        resourcenameentry.delete(0, tk.END)
        resourcecountentry["bg"] = "#ffffff"
        resourcenum+=1
        resourcenumstr = str(resourcenum)
        if resourcenum <10:
            resourcenumstr = "0"+str(resourcenum)
        resourcenumlabel["text"] = "Resource "+resourcenumstr+":"
        export["names"].append(value)
        if type == 0:
            export["values"].append(str(value2))
        else:
            export["values"].append(str(-1))
        print(export)
    else:
        resourcecountentry.insert("end", error)
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
frame1 = tk.Frame(resourcemanagersetup).pack(anchor="w",side="left")
frame2 = tk.Frame(resourcemanagersetup).pack(side="bottom",anchor="w",pady=5)
resourcemanagersetup.title(str(filename)+" setup")
resourcenumlabel = tk.Label(frame1,text="Resource "+resourcenumstr+":",font=("Helevitica","17",BOLD),justify="left")
resourcenamelabel = tk.Label(frame1,text="Name:",font=("Helevitica","17"))
resourcenameentry =tk.Entry(frame1,width=35,justify="left")
resourcetypebutton = tk.Button(frame1,text="Count",command=checkcountcommand,font=("Helevitica","17"),bg="#0050EF")
resourcecountlabel = tk.Label(frame1,text="Count needed(Int)",font=("Helevitica","17",BOLD),justify="left")
resourcecountentry = tk.Entry(frame1,width=35)
finishsetupbutton = tk.Button(frame2,text="Finish setup",command=finish,font=("Helevitica","17"),bg="#008A00").pack(side="right",anchor="s",pady=10)
addresourcebutton = tk.Button(frame2,text="Add resource",command=addresourcecommand,font=("Helevitica","17"),bg="#0050EF").pack(side="bottom",anchor="w",pady=10)
while done != True:
    if error != "":
        if dir == "up":
            if c2 == 9:
                if c >8:
                    dir = "down"
            if c < 9.4:
                c += 0.04
            else:
                c=0
                c2+=1
        else:
            if c2 == 0:
                if c < 1:
                    dir = "up"
            if c > 0:
                c -= 0.04
            else:
                c=9
                c2-=1
        resourcecountentry["bg"] = "#ff"+str(round(c2))+str(round(c))+str(round(c2))+str(round(c))
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
else:
    resourcemanagersetup.destroy()
    subprocess.call(["python", "91906-91907-repository\\file4.py"])