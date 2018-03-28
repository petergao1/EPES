from tkinter import *

username = ""
password = ""


def clicked():
    username = txt1.get()
    password = txt2.get()
    print(username)


window = Tk()
window.title("MainUI")
window.geometry('300x100')

lbl1 = Label(window, text="Username:")
lbl1.grid(column=0, row=0)

txt1 = Entry(window,width=20)
txt1.grid(column=1, row=0)
txt1.focus()

lbl2 = Label(window, text="Password")
lbl2.grid(column=0, row=1)

txt2 = Entry(window,width=20)
txt2.grid(column=1, row=1)

btn = Button(window, text="Login", command=clicked)
btn.grid(column=1, row=2)

window.mainloop()
