import random


def roll():
    diceNumber = random.randint(1, 6)
    print("The chosen number is " + str(diceNumber) + "!")

    print("Press enter to roll again or type 'exit' to exit the program!")
    choice = input()
    if choice == "":
        roll()
    elif choice == "exit":
        exit()
    else:
        roll

roll()
