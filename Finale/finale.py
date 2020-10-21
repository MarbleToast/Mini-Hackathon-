from Tkinter import *
import time
import random
global answerlabel_math
def calc ():
    frame.withdraw()
    frame_calc = Tk()
    frame_calc.title("Calculator")
    frame_calc.geometry ("800x400")
    def plus():
        num1 = int(num1EntryField.get())
        num2 = int(num2EntryField.get())
        answer = num1+ num2
        answerlabel_math.config(text=answer)

    def minus():
        num1 = int(num1EntryField.get())
        num2 = int(num2EntryField.get())
        answer = num1 - num2
        answerlabel_math.config(text=answer)

    def divided():
        num1 = float(num1EntryField.get())
        num2 = float(num2EntryField.get())
        answer = num1 / num2
        answer = round(answer,3)
        answerlabel_math.config(text=answer)

    def times():
        num1 = int(num1EntryField.get())
        num2 = int(num2EntryField.get())
        answer = num1 * num2
        answerlabel_math.config(text=answer)
    def back ():
        frame.deiconify()
        frame_calc.destroy()

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

    addButton1_math = Button(frame_calc, text="+",command=plus)
    addButton1_math.pack()

    addButton2_math = Button(frame_calc, text="-",command= minus)
    addButton2_math.pack()

    addButton3_math = Button(frame_calc, text="/",command= divided)
    addButton3_math.pack()

    addButton4_math = Button(frame_calc, text="*",command= times)
    addButton4_math.pack()

    addButton5_math = Button(frame_calc, text="Go Back", command= back)
    addButton5_math.pack()

    answerlabel_math = Label (frame_calc, text="answer")
    answerlabel_math.pack()

def joke():
    frame.withdraw()
    def answers ():
        t=True
        if(len(nums)==9):
            answerLabel.config(text="Sorry, thats all the jokes we have :(")
            t=False
        else:
            while t == True :
                ranNum = random.randint(1, 9)
                for i in range (0,len(nums)):
                    if(ranNum == nums[i]):
                        t=False
                t= not t
            nums.append(ranNum)
            if (ranNum == 1):
                        answerLabel.config(text="Yo mama so fat, her portrait fell off the wall")

            elif(ranNum == 2) :
                        answerLabel.config(text="Why can't a blonde dial 911?   She can't find the eleven.")

            elif(ranNum == 3) :
                        answerLabel.config(text="If con is the opposite of pro, then is Congress the opposite of progress?")
            elif(ranNum == 4) :
                        answerLabel.config(text="My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.")

            elif(ranNum == 5) :
                        answerLabel.config(text="Two guys stole a calendar. They got six months each.")

            elif(ranNum == 6) :
                        answerLabel.config(text="I can't believe I forgot to go to the gym today. That's 7 years in a row now.")

            elif (ranNum == 7):
                        answerLabel.config(text="I made a pencil with two erasers. It was pointless.")

            elif(ranNum == 8) :
                        answerLabel.config(text="Yo momma is so fat, I took a picture of her last Christmas and it's still printing.")

            elif(ranNum == 9) :
                        answerLabel.config(text="I used to hate facial hair...but then it grew on me.")
    def back():
        frame.deiconify()
        frame_jokes.destroy()


    nums = []
    frame_jokes = Tk()
    frame_jokes.geometry ("600x400")


    question = Label (frame_jokes, text="wana hear a joke?")
    question.pack()



    addButton1 = Button(frame_jokes, text="Here it is",command= answers)
    addButton1.pack()

    addButton2 = Button(frame_jokes, text= "Go Back", command= back)
    addButton2.pack()

    answerLabel = Label (frame_jokes, text="")
    answerLabel.pack()
#Finale frame

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
