import tkinter as tk

message_label = None

window = tk.Tk()
window.title("Playing with buttons")
window.geometry("1100x700")

def quit():
    window.destroy()

def message():
    global message_label
    if message_label is None:
        message_label = tk.Label(window, text="Hello")
        message_label.grid(column=0, row=1, columnspan=4, pady=20)
    elif not message_label.winfo_ismapped():
        message_label.grid(column=0, row=1, columnspan=4, pady=20)

def hiterminala():
    print("hi")

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
    advancedSets.title("Advanced Settings")
    advancedSets.geometry("600x600")

    quit_btn = tk.Button(advancedSets, text="Quit", command=advancedSets.destroy)
    quit_btn.pack()

quitBut = tk.Button(window, text="Quit", command=quit)
quitBut.grid(column=0, row=0, padx=10, pady=10)

messageBut = tk.Button(window, text="Click Me", command=message)
messageBut.grid(column=1, row=0, padx=10, pady=10)

hiterminal = tk.Button(window, text="Say hi in terminal", command=hiterminala)
hiterminal.grid(column=2, row=0, padx=10, pady=10)

clear = tk.Button(window, text="Clear", command=clear)
clear.grid(column=3, row=0, padx=10, pady=10)

settingsBut = tk.Button(window, text="Settings", command=settingsWin)
settingsBut.grid(column=4, row=0, padx=10, pady=10)

window.mainloop()
