from Tkinter import *


def plus():
    num1 = int(num1EntryField.get())
    num2 = int(num2EntryField.get())
    answer = num1+ num2
    answervariable = answer
    answerlabel.config(text=answervariable)

def minus():
    num1 = int(num1EntryField.get())
    num2 = int(num2EntryField.get())
    answer = num1 - num2
    answervariable = answer
    answerlabel.config(text=answervariable)

def divided():
    num1 = float(num1EntryField.get())
    num2 = float(num2EntryField.get())
    answer = num1 / num2
    answer = round(answer,3)
    answervariable = answer
    answerlabel.config(text=answervariable)

def times():
    num1 = int(num1EntryField.get())
    num2 = int(num2EntryField.get())
    answer = num1 * num2
    answervariable = answer
    answerlabel.config(text=answervariable)

frame = Tk()
frame.geometry ("800x400")


title = Label (frame, text="Calculator")
title.pack()




num1 = Label (frame, text="Enter number")
num1.pack()


num1EntryField = Entry(frame)
num1EntryField.pack()
num1EntryField.configure(bg="white")



num2 = Label (frame, text="Enter number")
num2.pack()


num2EntryField = Entry(frame)
num2EntryField.pack()


addButton1 = Button(frame, text="+",command=plus)
addButton1.pack()


addButton2 = Button(frame, text="-",command= minus)
addButton2.pack()


addButton3 = Button(frame, text="/",command= divided)
addButton3.pack()


addButton4 = Button(frame, text="*",command= times)
addButton4.pack()

answerlabel = Label (frame, text="answer")
answerlabel.pack()

frame.mainloop()
