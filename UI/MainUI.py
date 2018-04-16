from tkinter import *

username = ""
password = ""


def clicked():
    username = txt1.get()
    password = txt2.get()
    print(username)
    print(password)

    if username == "cxs496":
        lbl3 = Label(window, text="Login successful")
        lbl3.grid(column=0, row=3)
    else:
        lbl3 = Label(window, text="Login failed")
        lbl3.grid(column=0, row=3)
    testLogin(username,password)

def testLogin(un,pw):
    if un == "cxs496" and pw == "testing":
        print("Login functionality test succeeded")
        print("Logging in...")
    else:
        print("Login functionality test failed")


if __name__ == "__main__":
    window = Tk()
    window.title("MainUI")
    window.geometry('400x150')

    lbl1 = Label(window, text="Username:")
    lbl1.grid(column=0, row=0)

    txt1 = Entry(window,width=20)
    txt1.grid(column=1, row=0)
    txt1.focus()

    lbl2 = Label(window, text="Password:")
    lbl2.grid(column=0, row=1)

    txt2 = Entry(window,width=20)
    txt2.grid(column=1, row=1)

    btn = Button(window, text="Login", command=clicked)
    btn.grid(column=1, row=2)

    window.mainloop()