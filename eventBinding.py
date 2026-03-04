import tkinter as tk

def handle_right_click(event):
    print("right click")
    button.config(bg='red')

def handle_click(event):
    print(f"Button clicked at X={event.x}, Y={event.y}")
    button.config(bg="green")

def handle_key(event):
    print(f"Key pressed: {event.char}")

def mouseEnteronButton(event):
    button.config(text="mouse enter", fg="yellow", bg="tomato")

def mouseLeaveButton(event):
    button.config(text="mouse Leave", fg="blue", bg="white")

window = tk.Tk()
button = tk.Button(window, text="Click Me")
button.pack()

entry = tk.Entry(window)
entry.pack()

# Bind a function to a left mouse click on the button
button.bind("<Button-1>", handle_click)

# Bind a function to a right mouse click on the button
button.bind("<Button-3>", handle_right_click)

button.bind("<Enter>", mouseEnteronButton)

button.bind("<Leave>", mouseLeaveButton)
# Bind a function to any key press on the entry widget
entry.bind("<Key>", handle_key)



window.mainloop()
