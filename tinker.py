import tkinter as tk
from tkinter import simpledialog

def usrImp():
    ROOT = tk.Tk()

    ROOT.withdraw()
    ROOT.geometry('450x200')
    # the input dialog
    USER_INP = simpledialog.askstring(title="Graph Plotter",
                                    prompt="Enter the file name: ")

    # print("Hello", USER_INP)
    return USER_INP