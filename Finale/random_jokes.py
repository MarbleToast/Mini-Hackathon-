from Tkinter import *
import random

def answers ():

    ranNum = random.randint(1, 9)

    if (ranNum == 1):
                answer = "Yo mama so fat, her portrait fell off the wall"
                answervariable = answer
                answerLabel.config(text=answervariable)

    elif(ranNum == 2) :
                answer = "Why can't a blonde dial 911?   She can't find the eleven."
                answervariable = answer
                answerLabel.config(text=answervariable)

    elif(ranNum == 3) :
                answer = "If con is the opposite of pro, then is Congress the opposite of progress?"
                answervariable = answer
                answerLabel.config(text=answervariable)
    elif(ranNum == 4) :
                answer = "My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away."
                answervariable = answer
                answerLabel.config(text=answervariable)

    elif(ranNum == 5) :
                answer = "Two guys stole a calendar. They got six months each."
                answervariable = answer
                answerLabel.config(text=answervariable)
    elif(ranNum == 6) :
                answer = "I can't believe I forgot to go to the gym today. That's 7 years in a row now."
                answervariable = answer
                answerLabel.config(text=answervariable)

    elif (ranNum == 7):
                answer = "I made a pencil with two erasers. It was pointless."
                answervariable = answer
                answerLabel.config(text=answervariable)

    elif(ranNum == 8) :
                answer = "Yo momma is so fat, I took a picture of her last Christmas and it's still printing."
                answervariable = answer
                answerLabel.config(text=answervariable)

    elif(ranNum == 9) :
                answer = "I used to hate facial hair...but then it grew on me."
                answervariable = answer
                answerLabel.config(text=answervariable)




frame = Tk()
frame.geometry ("600x400")


question = Label (frame, text="wana hear a joke?")
question.pack()



addButton1 = Button(frame, text="Here it is",command= answers)
addButton1.pack()

answerLabel = Label (frame, text="")
answerLabel.pack()


frame.mainloop()
