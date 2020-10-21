global num1EntryField
global num2EntryField
global answerlabel
global frame_calc
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
    frame_calc.destroy()

frame_calc = Tk()
frame_calc.geometry ("800x400")


title = Label (frame_calc, text="Calculator")
title.pack()




num1 = Label (frame_calc, text="Enter number")
num1.pack()


num1EntryField = Entry(frame_calc)
num1EntryField.pack()
num1EntryField.configure(bg="white")



num2 = Label (frame_calc, text="Enter number")
num2.pack()


num2EntryField = Entry(frame_calc)
num2EntryField.pack()


addButton1 = Button(frame_calc, text="+",command=plus)
addButton1.pack()

addButton2 = Button(frame_calc, text="-",command= minus)
addButton2.pack()

addButton3 = Button(frame_calc, text="/",command= divided)
addButton3.pack()

addButton4 = Button(frame_calc, text="*",command= times)
addButton4.pack()

addButton5 = Button(frame_calc, text="Go Back", command= back)
addButton5.pack()

answerlabel = Label (frame_calc, text="answer")
answerlabel.pack()

frame_calc.mainloop()
