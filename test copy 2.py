import tkinter as tk
import subprocess
from tkinter.font import BOLD

root = tk.Tk()
componentlist = []
mainnum = 0

def save():
    dictionary = {
        "names" : ["bread","sugar","milk"],
        "valuesmax" : ["-1","15","23"],
        "valuescurrent" : ["0","25","12"]
    }
    with open("FILENAMEfullsave", "w") as file:
        file.write(str(dictionary))


button = tk.Button(root,text="press",command=save).pack()


while True:
    root.update()