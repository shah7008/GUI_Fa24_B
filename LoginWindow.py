import tkinter as tk
def login():
    if (entry_userName.get()=="admin") & (entry_password.get()=="admin"):
        # print("login Successfull")
        label_status.config(text="login Successfull")
    else:
        label_status.config(text="login Failed", bg="red")
root=tk.Tk()
root.title("Login Window")
root.geometry("200x200")


label_userName=tk.Label(root, text="User Name")
label_userName.pack()

entry_userName=tk.Entry(root,width=20)
entry_userName.pack()

label_password=tk.Label(root, text="Password")
label_password.pack()

entry_password=tk.Entry(root,width=20)
entry_password.pack()

button_login=tk.Button(root, text="login", command=login)
button_login.pack()

label_status=tk.Label(root, text="")
label_status.pack()



root.mainloop()