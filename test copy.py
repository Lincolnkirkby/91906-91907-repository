import tkinter as tk
from tkinter.font import BOLD
root = tk.Tk()
componentlist = []

def printnum(num):
    print(num)
num = 0


dict = {}
def buttons():
    for i in range(0,5):
        dict[f"b{i}"] = tk.Button(root,font=("Helevitica","17"),text="Print",bg="#008A00",command=lambda:printnum(i))
buttons()

while True:
    for component in dict:
        component.pack(anchor="w",pady=2)
    root.update()
