from tkinter import *

payroll = 0;
ratings = "YOU SUCK"
comment = ""
respond = ""
workinghours = 0

def clicked1():
    comment = txt1.get("1.0", "end-1c")
    print(comment)


def clicked2():
    respond = txt2.get("1.0", "end-1c")
    print(respond)


def clicked3():
    res = "Your payroll is: " + get_payroll()
    lbl3.configure(text=res)


def clicked4():
    res = "Your rating is: " + get_ratings()
    lbl4.configure(text=res)


def clicked5():
    workinghours = txt5.get()
    print(workinghours)

def get_payroll():
    return str(payroll)


def get_ratings():
    return ratings


window = Tk()
window.title("departmentStaffUI")
window.geometry('600x400')

lbl1 = Label(window, text="Write comment")
lbl1.grid(column=0, row=0)

txt1 = Text(window,width=40,height=10)
txt1.grid(column=1, row=0)
txt1.focus()

btn1 = Button(window, text="Send Comment", command=clicked1)
btn1.grid(column=2, row=0)

lbl2 = Label(window, text="Write respond")
lbl2.grid(column=0, row=1)

txt2 = Text(window,width=40,height=10)
txt2.grid(column=1, row=1)

btn2 = Button(window, text="Send Respond", command=clicked2)
btn2.grid(column=2, row=1)

btn3 = Button(window, text="View Payroll", command=clicked3)
btn3.grid(column=1, row=2)

lbl3 = Label(window, text="Your payroll is: ")
lbl3.grid(column=0, row=2)

btn4 = Button(window, text="View Ratings", command=clicked4)
btn4.grid(column=1, row=3)

lbl4 = Label(window, text="Your rating is: ")
lbl4.grid(column=0, row=3)

lbl5 = Label(window, text="Your working hours: ")
lbl5.grid(column=0, row=4)

txt5 = Entry(window, width=40)
txt5.grid(column=1, row=4)

btn5 = Button(window, text="Set hours", command=clicked5)
btn5.grid(column=2, row=4)

window.mainloop()
