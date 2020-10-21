import tkinter


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

frame = tkinter.Tk()
frame.geometry ("800x400")


title = tkinter.Label (frame, text="Calculator")
title.pack()




num1 = tkinter.Label (frame, text="Enter number")
num1.pack()


num1EntryField = tkinter.Entry(frame)
num1EntryField.pack()
num1EntryField.configure(bg="white")



num2 = tkinter.Label (frame, text="Enter number")
num2.pack()


num2EntryField = tkinter.Entry(frame)
num2EntryField.pack()
num2EntryField.configure(bg="white")


addButton1 = tkinter.Button(frame, text="+",command=plus)
addButton1.pack()
addButton1.configure(bg="red")


addButton2 = tkinter.Button(frame, text="-",command= minus)
addButton2.pack()
addButton2.configure(bg="red")


addButton3 = tkinter.Button(frame, text="/",command= divided)
addButton3.pack()
addButton3.configure(bg="red")


addButton4 = tkinter.Button(frame, text="*",command= times)
addButton4.pack()
addButton4.configure(bg="red")

answerlabel = tkinter.Label (frame, text="answer")
answerlabel.pack()




frame.mainloop()
