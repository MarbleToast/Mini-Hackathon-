from Tkinter import *
global num1EntryField
global num2EntryField
global answerlabel
def plus():
    num1 = int(num1EntryField.get())
    num2 = int(num2EntryField.get())
    answer = num1+ num2
    answerlabel.config(text=answer)

def minus():
    num1 = int(num1EntryField.get())
    num2 = int(num2EntryField.get())
    answer = num1 - num2
    answerlabel.config(text=answer)

def divided():
    num1 = float(num1EntryField.get())
    num2 = float(num2EntryField.get())
    answer = num1 / num2
    answer = round(answer,3)
    answerlabel.config(text=answer)

def times():
    num1 = int(num1EntryField.get())
    num2 = int(num2EntryField.get())
    answer = num1 * num2
    answerlabel.config(text=answer)
def back ():
    frame.deiconify()
    global frame1
    frame1.destroy()

frame1 = Tk()
frame1.geometry ("800x400")


title = Label (frame1, text="Calculator")
title.pack()




num1 = Label (frame1, text="Enter number")
num1.pack()


num1EntryField = Entry(frame1)
num1EntryField.pack()
num1EntryField.configure(bg="white")



num2 = Label (frame1, text="Enter number")
num2.pack()


num2EntryField = Entry(frame1)
num2EntryField.pack()


addButton1 = Button(frame1, text="+",command=plus)
addButton1.pack()

addButton2 = Button(frame1, text="-",command= minus)
addButton2.pack()

addButton3 = Button(frame1, text="/",command= divided)
addButton3.pack()

addButton4 = Button(frame1, text="*",command= times)
addButton4.pack()

addButton5 = Button(frame1, text="Go Back", command= back)
addButton5.pack()

answerlabel = Label (frame1, text="answer")
answerlabel.pack()

frame1.mainloop()
