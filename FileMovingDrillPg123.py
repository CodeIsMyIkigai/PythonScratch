#!/usr/bin/python3

import sqlite3
from tkinter import *
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import os
import FileMovingDrillPg123_db as fmd
import datetime

def folderSelector(textArea):
    sourcepath = tk.filedialog.askdirectory()
    textArea.update()
    textArea.config(state="normal")
    textArea.delete(0, END)
    textArea.insert(INSERT, sourcepath)
    textArea.config(state="disabled")

def dirSelect1(self):
    folderSelector(self.txt_Dir1)

def dirSelect2(self):
    folderSelector(self.txt_Dir2)

def moveFiles(self):
    print("Move")
    print(self.txt_Dir1.get())
    print(self.txt_Dir2.get())

    if self.txt_Dir1.get() == '':
        tk.messagebox.showinfo("Problem", "Please select a source directory!")
        return
    if self.txt_Dir2.get() == '':
        tk.messagebox.showinfo("Problem", "Please select a destination directory!")
        return

    batch = datetime.datetime.now()
    files = os.listdir(self.txt_Dir1.get())
    for file in files:
        if file.endswith(".txt"):
            sourceFile = os.path.join(self.txt_Dir1.get(), file)
            destFile = os.path.join(self.txt_Dir2.get(), file)
            os.rename(sourceFile, destFile)
            mtime = os.path.getmtime(destFile)
            fmd.logMove(batch, destFile, mtime)
    fmd.printLogs(batch)


def closeProgram(self):
    root.destroy()

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master

        self.master.minsize(700, 300)
        self.master.maxsize(800, 500)
        self.master.title("File Mover")

        self.btn_Browse1 = tk.Button(self.master, width=20, height=2, text='Select Source Directory', command=lambda: dirSelect1(self))
        self.btn_Browse1.grid(row=8, column=0, padx=(25, 0), pady=(45, 10), sticky=W)

        self.btn_Browse2 = tk.Button(self.master, width=20, height=2, text='Select Destination Director', command=lambda: dirSelect2(self))
        self.btn_Browse2.grid(row=9, column=0, padx=(25, 0), pady=(45, 10), sticky=W)

        self.txt_Dir1 = tk.Entry(self.master, width=75, text='', state="disabled")
        self.txt_Dir1.grid(row=8, column=1, rowspan=1, columnspan=8, padx=(25, 0), pady=(45, 10), sticky=NSEW)

        self.txt_Dir2 = tk.Entry(self.master, width=75, text='', state="disabled")
        self.txt_Dir2.grid(row=9, column=1, rowspan=1, columnspan=8, padx=(25, 0), pady=(45, 10), sticky=NSEW)

        self.btn_CheckForFiles = tk.Button(self.master, width=12, height=3, text='Move Files', command=lambda: moveFiles(self))
        self.btn_CheckForFiles.grid(row=10, column=0, rowspan=2, padx=(25, 0), pady=(45, 45), sticky=NSEW)

        self.btn_CloseProgram = tk.Button(self.master, width=12, height=3, text='Close Program', command=lambda: closeProgram(self))
        self.btn_CloseProgram.grid(row=10, column=8, rowspan=2, padx=(25, 0), pady=(45, 45), sticky=NSEW)


if __name__ == "__main__":
    fmd.createDB()
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
