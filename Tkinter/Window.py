import tkinter as tk

window = tk.Tk()
window.title("Hello")
window.geometry("333x444")

label = tk.Label(window, text="Hello")
label.pack()

window.mainloop()