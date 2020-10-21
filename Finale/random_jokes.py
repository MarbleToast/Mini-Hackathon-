import random
global frame_jokes
global answerLabel
def answers ():

    ranNum = random.randint(1, 9)

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


frame_jokes.mainloop()
