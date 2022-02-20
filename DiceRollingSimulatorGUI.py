import random
from tkinter import *


window = Tk()
window.geometry("200x200")
window.title("Dice Rolling Simulator")
gridFrame = Frame(window)
gridFrame.pack(side=TOP)


def play():
    diceNumber = random.randint(1, 6)
    yourNumberIsLabel = Label(gridFrame, text="Your number is " + str(diceNumber) + "!", font=(None, 15))
    yourNumberIsLabel.grid(column=0, row=0)

    diceImage = PhotoImage(file = "img/dice%s.png" % diceNumber)
    imgButton = Button(gridFrame, image=diceImage)
    imgButton.grid(column=0, row=1)

    newNumberButton = Button(gridFrame, text="Roll Again", command = lambda: play())
    newNumberButton.grid(column=0, row=2, pady=15)

    window.mainloop()


play()
