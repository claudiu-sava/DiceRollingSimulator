import os.path
import random
from tkinter import *
import platform
import pathlib
import os
from PIL import Image, ImageTk


os_name = platform.system()



window = Tk()
window.geometry("200x200")
window.title("Dice Rolling Simulator")
gridFrame = Frame(window)
gridFrame.pack(side=TOP)

programPath = pathlib.Path(__file__).parent.absolute()


def play():
    diceNumber = random.randint(1, 6)
    yourNumberIsLabel = Label(gridFrame, text="Your number is " + str(diceNumber) + "!", font=(None, 15))
    yourNumberIsLabel.grid(column=0, row=0)

    showDiceIcon(diceNumber)

    newNumberButton = Button(gridFrame, text="Roll Again", command = lambda: play())
    newNumberButton.grid(column=0, row=2, pady=15)

    window.mainloop()


def showDiceIcon(diceNumber):
    load = Image.open(str(programPath) + os.path.sep + "icons" + os.path.sep + "dice" + str(diceNumber) + ".png" )
    render = ImageTk.PhotoImage(load)

    img = Label(gridFrame, image=render)
    img.image = render
    img.grid(column=0, row=1)


play()
