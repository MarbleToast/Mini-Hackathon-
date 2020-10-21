try:
    from Tkinter import *
except:
    from tkinter import *
import time
import random

def calc ():
    #frame.destroy()
    frame.withdraw()
    execfile('calculator.py')
def joke():
    frame.withdraw()
    execfile('random_jokes.py')

frame = Tk()
frame.geometry("800x400")

title = Label(frame, text="Python GUI")
title.pack()

addButton1 = Button(frame, text = "Calculator", command=calc)
addButton1.pack()
addButton1.place(relx=0.3, rely=0.1, anchor=CENTER)

addButton2 = Button(frame,text= "Random joke generator",command=joke)
addButton2.pack()
addButton2.place(relx=0.5, rely=0.1, anchor=CENTER)

frame.mainloop()
