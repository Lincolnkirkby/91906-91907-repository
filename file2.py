import tkinter as tk
import subprocess
from tkinter.font import BOLD

with open("allsavenames", 'r') as file:
        templist = file.readlines()
print(templist)

savenames = []
for x in templist:
        savenames.append(x.strip("\n"))
print(savenames)

root = tk.Tk()
root.title("Resourse Time Managaer New")
def end():
        with open("savenames", 'w') as file:
                file.write(nameenrty.get())
        savenames.append(nameenrty.get())
        print(savenames)
        with open("allsavenames", 'w') as file:
                file.writelines(string + '\n' for string in savenames)
        root.destroy()
        subprocess.call(["python", "91906-91907-repository\\file3.py"])
label = tk.Label(font=("Helevitica","17",BOLD),text= "SETTINGS:").pack(anchor="w",pady=10)
label2 = tk.Label(font=("Helevitica","14",BOLD),text= "File Name:").pack(anchor="w")
nameenrty = tk.Entry(root,width=35,font=("Helevitica","14",BOLD))
nameenrty.pack()
Label3 = tk.Label(font=("Helevitica","14",BOLD),text= "Mode:").pack(anchor="w")
modebutton = tk.Button(root,text="Resource",command=end,font=("Helevitica","17",BOLD),width=10,bg="#E51400",fg="#fff").pack(anchor = "w")
endbutton = tk.Button(root,text="Start",command=end,font=("Helevitica","17",BOLD),width=10,bg="#008A00",fg="#fff").pack(anchor = "e",pady=10)
while True:
        root.update()