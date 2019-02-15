#!/usr/bin/python3

from tkinter import *
import tkinter as tk


def browse1(self):
    print("howdy")

def browse2(self):
    print("howdy")

def checkForFiles(self):
    print("howdy")


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master

        self.master.minsize(500, 300)
        self.master.maxsize(700, 500)
        self.master.title("Check files")

        self.btn_Browse1 = tk.Button(self.master, width=12, height=2, text='Browse...', command=lambda: browse1(self))
        self.btn_Browse1.grid(row=8, column=0, padx=(25, 0), pady=(45, 10), sticky=W)

        self.btn_Browse2 = tk.Button(self.master, width=12, height=2, text='Browse...', command=lambda: browse2(self))
        self.btn_Browse2.grid(row=10, column=0, padx=(25, 0), pady=(45, 10), sticky=W)


        self.btn_CheckForFiles = tk.Button(self.master, width=12, height=2, text='Check for files...', command=lambda: checkForFiles(self))
        self.btn_CheckForFiles.grid(row=12, column=0, padx=(25, 0), pady=(45, 10), sticky=W)

        self.txt_browse1 = tk.Entry(self.master,text='')
        self.txt_browse1.grid(row=8,column=1,rowspan=1,columnspan=4, padx=(25, 0), pady=(45, 10), sticky=W)

        self.txt_browse2 = tk.Entry(self.master, text='')
        self.txt_browse2.grid(row=10, column=1, rowspan=1, columnspan=4, padx=(25, 0), pady=(45, 10), sticky=W)


        self.btn_CheckForFiles = tk.Button(self.master, width=12, height=2, text='Close Program', command=lambda: closeProgram(self))
        self.btn_CheckForFiles.grid(row=12, column=4, padx=(25, 0), pady=(45, 10), sticky=W)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
