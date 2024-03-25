import tkinter as tk
from tkinter.font import BOLD
root = tk.Tk()
def end():
        with open("savenames.txt", 'w') as file:
                file.writelines(nameenrty.get())
nameenrty = tk.Entry(root).pack()
endbutton = tk.Button(root,text="end",command=end).pack()
root.mainloop()