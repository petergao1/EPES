from tkinter import *
from tkinter.ttk import *

payroll = 0;
ratings = "YOU SUCK"
comment = ""
respond = ""
execution = "Employee xxx is fired"
workinghours = 0

def clicked1():
    comment = txt1.get("1.0", "end-1c")
    targetEmployee = combo1.get()
    testingComment(comment,targetEmployee)


def clicked2():
    respond = txt2.get("1.0", "end-1c")
    targetEmployee = combo2.get()
    testingRespond(respond,targetEmployee)


def clicked3():
    res = "Your payroll is: " + get_payroll()
    lbl3.configure(text=res)
    testingPayroll()


def clicked4():
    res = "Your rating is: " + get_ratings()
    lbl4.configure(text=res)
    testingRatings()


def clicked5():
    global payroll
    workinghours = txt5.get()
    payroll = int(workinghours) * 200
    testingSetHours(workinghours)


def get_payroll():
    return str(payroll)


def get_ratings():
    return ratings


def execute(): #do sth
    testExecution()


def testingComment(x, y):
    if x == "TestingComment" and y == "2":
        print("comment functionality test succeeded!")
    else:
        print("comment functionality test failed!")


def testingRespond(x, y):
    if x == "TestingRespond" and y == "1":
        print("comment functionality test succeeded!")
    else:
        print("comment functionality test failed!")


def testingPayroll():
    if get_payroll() == "8000":
        print("view payroll functionality test succeeded!")
    else:
        print(get_payroll())
        print("view payroll functionality test failed!")


def testingRatings():
    if get_ratings() == "YOU SUCK":
        print("view ratings functionality test succeeded!")
    else:
        print("view ratings functionality test failed!")


def testingSetHours(hours):
    if hours == "40":
        print("Set hours functionality test succeeded!")
    else:
        print("Set hours  functionality test failed!")


def testExecution():
    if execution == "Employee xxx is fired":
        print("Execution functionality test succeeded!")
    else:
        print("Execution functionality test failed!")


window = Tk()
window.title("HRDepartmentUI")
window.geometry('700x450')

lbl1 = Label(window, text="Write comment")
lbl1.grid(column=0, row=0)

txt1 = Text(window,width=40,height=10)
txt1.grid(column=1, row=0)
txt1.focus()

btn1 = Button(window, text="Send Comment", command=clicked1)
btn1.grid(column=3, row=0)

combo1 = Combobox(window)
combo1['values'] = (1, 2, 3, 4, 5, "Text")
combo1.current(0)  # set the selected item
combo1.grid(column=2, row=0)

lbl2 = Label(window, text="Write respond")
lbl2.grid(column=0, row=1)

txt2 = Text(window,width=40,height=10)
txt2.grid(column=1, row=1)

btn2 = Button(window, text="Send Respond", command=clicked2)
btn2.grid(column=3, row=1)

combo2 = Combobox(window)
combo2['values'] = (1, 2, 3, 4, 5, "Text")
combo2.current(0)  # set the selected item
combo2.grid(column=2, row=1)

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

btn6 = Button(window, text="Execute Decisions", command=execute)
btn6.grid(column=2, row=5)
window.mainloop()
