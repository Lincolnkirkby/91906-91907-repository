import tkinter as tk
import subprocess
from tkinter.font import BOLD

root = tk.Tk()
componentlist = []
mainnum = 0

def quit():
    root.destroy()
    subprocess.call(["python", "91906-91907-repository\\file3.py"])
    print("HIII")


button = tk.Button(root,text="press",command=quit).pack()


while True:
    root.update()