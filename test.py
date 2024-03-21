import tkinter as tk
from tkinter.font import BOLD
root = tk.Tk()
componentlist = []
mainnum = 0

def printnum(num):
    print(num)
    global mainnum
    mainnum +=1
    if mainnum < 5:
        g = tk.Label(root,font=("Helevitica","17"),text="Number"+str(num+1)+":")
        h = tk.Button(root,font=("Helevitica","17"),text="Print",bg="#008A00",command=lambda:printnum(num+1))
        h.invoke()
        componentlist.append(g)
        componentlist.append(h)



for x in range(1):
    a = tk.Label(root,font=("Helevitica","17"),text="Number"+str(1)+":")
    b = tk.Button(root,font=("Helevitica","17"),text="Print",bg="#008A00",command=lambda:printnum(1))
    b.invoke()
    componentlist.append(a)
    componentlist.append(b)



while True:
    for component in componentlist:
        component.pack(anchor="w",pady=2)
    root.update()