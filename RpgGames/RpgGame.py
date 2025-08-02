import time
import random
import sys
from os import WCONTINUED

CommonItems = ("Spider Web", "Hair", "Clothes", "Spider Web", "Hair", "Clothes", "Notebook(1/7 chance of getting this)")
UncommonItems = ("Perfume", "Cologne", "dmblosh")
RareItems = ("Spider Web", "Hair", "Flashlight", "Spider Web", "Batteries", "Phone")
gold = 0
haskey = False
hashands = False

def commonchest():
    global CommonItems
    item = random.choice(CommonItems)
    if item == "Spider Web":
        time.sleep(0.2);
        print("Unpacking...")
        time.sleep(1)
        print("You got ")
        time.sleep(1)
        print(f"{item}, but it crumbled in your hands (its a useless item")
    else:
        time.sleep(0.2);
        print("Unpacking...")
        time.sleep(1)
        print("You got ")
        time.sleep(0.5)
        print(item)

def uncommonChest():
    global UncommonItems
    item = random.choice(UncommonItems)
    time.sleep(0.2)
    print("Unpacking...")
    time.sleep(1)
    print("you got a")
    time.sleep(0.5)
    print(item)

def rarechest():
    global RareItems
    item = random.choice(RareItems)
    time.sleep(0.2);
    print("Unpacking...")
    time.sleep(1)
    print("You got ")
    time.sleep(0.5)
    print(item)

def quit():
    for i in range(0, 4):
        print(i)
        time.sleep(1)
        if i == 3:
            break
    sys.exit()

def room1():
    global hashands  # if hashands is a global variable

    while True:
        question = input("You are currently in room 1. What would you like to do?\n1) Collect 15 gold (LOCKED)\n2) Next room\n3) Quit\n> ")

        if question == "1":
            if not hashands:
                print("To grab anything, you first must acquire hands.")
                continue  # repeat the room
            else:
                print("You collected 15 gold!")
                global gold
                gold += 15
                break  # exit the room

        elif question == "2":
            print("You go to the next room.")
            break  # move to next room (maybe call room2() here)

        elif question == "3":
            quit()

        else:
            print("Invalid input. Try again.")