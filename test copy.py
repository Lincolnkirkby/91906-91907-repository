import tkinter as tk
import subprocess
from tkinter.font import BOLD

root = tk.Tk()


def load():
    with open("FILENAMEfullsave", "r") as file:
        info = file.readline()
    dictionary = eval(info)
    print(dictionary["names"])


button = tk.Button(root,text="press",command=load).pack()

while True:
    root.update()