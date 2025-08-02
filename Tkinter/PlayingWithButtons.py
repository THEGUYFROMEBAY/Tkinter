import tkinter as tk

message_label = None

window = tk.Tk()
window.title("Playing with Buttons")
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


hiterminal = tk.Button(window, text="Say hi in terminal", command=hiterminala)
hiterminal.grid(column=2, row=0, pady=10, padx=10)


def clear():
    if message_label:
        message_label.grid_forget()


clear = tk.Button(window, text="Clear", command=clear)
clear.grid(column=3, row=0, pady=10, padx=10)

window.mainloop()
