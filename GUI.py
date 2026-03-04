import tkinter as tk

def button_click():
    print("button clicked")
    label.config(bg='yellow')
    button.config(bg='green')
    print("You typed",entry.get())


window=tk.Tk()
window.title("My First GUI APP with FA24-B")
window.geometry("400x200")

button=tk.Button(window, text="click me", command=button_click)
button.pack()
label = tk.Label(window, text="Hello, Tkinter!",bg="green" , font=("Arial", 16))
label.pack()
entry = tk.Entry(window, width=30)
entry.pack()


window.mainloop()