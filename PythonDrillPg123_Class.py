#!/usr/bin/python3

from tkinter import *
import tkinter as tk
import tkinter.filedialog

def checkForFiles(self):
    sourcepath = tkinter.filedialog.askdirectory()
    print(sourcepath)
    self.txt_TextArea.delete(self)
    self.txt_TextArea.config(state="normal")
    self.txt_TextArea.insert(INSERT, sourcepath)
    self.txt_TextArea.config(state="disabled")

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master

        self.master.minsize(700, 300)
        self.master.maxsize(800, 500)
        self.master.title("Ask Director Example")

        self.btn_CheckFiles = tk.Button(self.master, text='Launch Directory Dialog', command=lambda: checkForFiles(self))
        self.btn_CheckFiles.grid(row=0, column=0, padx=(25, 0), pady=(45, 10), sticky=NSEW)

        self.txt_TextArea = tk.Text(self.master, height=2)
        self.txt_TextArea.grid(row=1, column=0, rowspan=2, padx=(25, 0), pady=(45, 10), sticky=NSEW)
        self.txt_TextArea.config(state="disabled")



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
