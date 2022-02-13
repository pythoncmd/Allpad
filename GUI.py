from tkinter import *
import os

from tkinter.ttk import *
from tkinter.filedialog import *
from time import strftime
import tkinter as tk
root = Tk()
root.title("Clock")
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
label = Label(root, font=("ds-digital", 80), background = "black", foreground="cyan")
label.pack(anchor='center')


time()
mainloop()

def saveFile():
    new_file = asksaveasfile(mode = 'w')
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()


def NOTES():
    global canvas
    canvas = tk.Tk()
    canvas.configure(bg='grey')
    canvas.geometry("400x600")
    canvas.title("Allpad")

    top = Frame(canvas)

    def openFile():
        file = askopenfile(mode='r', filetype=[('text files', '*.txt')])
        if file is not None:
            content = file.read()
        entry.insert(INSERT, content)
        openFile()
    b1 = Button(canvas, text="Open", command = openFile)
    b1.pack(in_ = top, side=LEFT)

    top.pack(padx = 10, pady = 5, anchor = 'nw')
    b2 = Button(canvas, text="Save", command=saveFile)
    b2.pack(in_ = top, side=LEFT)

    def clearFile():
        entry.delete(1.0, END)
        clearFile()
    b3 = Button(canvas, text="Clear", command=clearFile)
    b3.pack(in_ = top, side=LEFT)

    b4 = Button(canvas, text="Exit", command = exit)
    b4.pack(in_ = top, side=LEFT)

    def Newpage():
        NOTES()
        canvas.mainloop()
    b5 = Button(canvas, text="NewPage", command=Newpage)
    b5.pack(in_ = top, side=LEFT)



    entry = Text(canvas,padx=70, pady=70, wrap=WORD,bg = "grey", font=("popins", 15))
    entry.pack(padx=5, pady=5, fill=BOTH, expand=1)



    canvas.mainloop()
NOTES()
def clearFile():
    entry.delete(0,END)
