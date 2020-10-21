from Tkinter import *

frame = Tk()
frame.geometry("800x400")

title = Label(frame, text="Python GUI")
title.pack()

addButton1 = Button(frame, text = "Calculator") #, command=...
addButton1.pack()
addButton1.place(relx=0.5, rely=0.5, anchor=CENTER)

addButton2 = Button(frame,text= "Random joke generator")#, command=...
addButton2.pack()

frame.mainloop()
