import tkinter as tk
names = []
root = tk.Tk()
filename= "FILE NAME HERE"
with open(filename+"names", 'r') as file:
    names = file.readlines()
newlist = []
for x in names:
    newlist.append(x.strip("\n"))
print(newlist)

#print(names)