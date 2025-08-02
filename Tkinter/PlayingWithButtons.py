import tkinter as tk
import time

message_label = None
command = None
entry = None

window = tk.Tk()
window.title("Playing with buttons")
window.geometry("1100x700")


def message():
    global message_label

    if message_label is None:
        message_label = tk.Label(window, text="Hello")
        message_label.grid(column=0, row=1, columnspan=4, pady=20)
    elif not message_label.winfo_ismapped():
        message_label.grid(column=0, row=1, columnspan=4, pady=20)


def hiterminala():
    print("hi")

def findlost():
    print("searching.")
    time.sleep(0.3)
    print("searching..")
    time.sleep(0.3)
    print("searching...")
    time.sleep(0.3)
    print("Sorry not found")

def terminal():
    global entry
    entry = tk.Entry(window, width=50)
    entry.grid(column=5, row=0, padx=10, pady=10)

    submit_btn = tk.Button(window, text="Submit", command=checkCommand)
    submit_btn.grid(column=6, row=0, padx=10, pady=10)

def checkCommand():
    global command
    command = entry.get()
    comlabel = tk.Label(window, text=f"Command Entered: {command}")
    comlabel.grid(column=5, row=1, padx=10, pady=10)
    if command.lower() == "settings":
        settingsWin()
    elif command.lower() == "quit":
        window.destroy()
    elif command.lower() == "find my lost brother":
        findlost()


def clear():
    if message_label:
        message_label.grid_forget()


def settingsWin():
    settings = tk.Toplevel(window)
    settings.title("Settings")
    settings.geometry("500x500")

    quit_btn = tk.Button(settings, text="Quit", command=settings.destroy)
    quit_btn.pack()

    adva = tk.Button(settings, text="Advanced Settings", command=advancedSettings)
    adva.pack()


def advancedSettings():
    advancedSets = tk.Toplevel(window)
    advancedSets.title("Advanced Setttings")
    advancedSets.geometry("600x600")

    quit_btn = tk.Button(advancedSets, text="Quit", command=advancedSets.destroy)
    quit_btn.pack()


quitBut = tk.Button(window, text="Quit", command=window.destroy)
quitBut.grid(column=0, row=0, padx=10, pady=10)

messageBut = tk.Button(window, text="Click Me", command=message)
messageBut.grid(column=1, row=0, padx=10, pady=10)

hiterminal = tk.Button(window, text="Say hi in terminal", command=hiterminala)
hiterminal.grid(column=2, row=0, padx=10, pady=10)

clear = tk.Button(window, text="Clear", command=clear)
clear.grid(column=3, row=0, padx=10, pady=10)

settingsBut = tk.Button(window, text="Settings", command=settingsWin)
settingsBut.grid(column=4, row=0, padx=10, pady=10)

terminal()

window.mainloop()
