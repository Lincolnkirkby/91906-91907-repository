import tkinter as tk
from tkinter.font import BOLD
import subprocess

root = tk.Tk()
root.title("Time Reourse Manager Start")
label = tk.Label(text="Welcome!",font=("Helevitica","17",BOLD))
label2 = tk.Label(text="If you have already set up a Time resource you may press the 'Load' button and input the name of the file you saved it to, or if this is your first time or you want to set up a new time resource press the 'New' button.",font=("Helevitica","15"))