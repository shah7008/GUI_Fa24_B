import tkinter as tk

def change_color():
    background_color=button.cget("bg")
    if background_color=="red":
        button.config(bg="green")
    else:
        button.config(bg="red")

window=tk.Tk()
button=tk.Button(window,text="click me", command=change_color)
button.pack()

window.mainloop()