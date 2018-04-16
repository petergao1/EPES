from tkinter import *
from tkinter.ttk import *
import hrSystem

payroll = 0
ratings = "YOU SUCK"
comment = ""
respond = ""
workinghours = 0
decision_exists = False
decision = "Bazinga"
targetEmployee = "0"
employeeID = 0000
hoursApproved = False


def writecomment():
    tmpcomment = txt1.get("1.0", "end-1c")
    targetemployee = combo1.get()
    if tmpcomment != "":
        window1 = Tk()
        window1.title("Input successful")
        window1.geometry('500x500')
        lbl1_1 = Label(window1, text="System received your comment to employee " + targetemployee)
        lbl1_1.grid(column=0, row=0)
        lbl1_2 = Label(window1, text="Your comment is: " + tmpcomment)
        lbl1_2.grid(column=0, row=1)
    else:
        window1 = Tk()
        window1.title("ERROR MESSAGE")
        window1.geometry('300x50')
        lbl1_1 = Label(window1, text="Wrong input. Input cannot be empty.")
        lbl1_1.grid(column=0, row=0)
    testingComment(tmpcomment, targetemployee)


def writerespond():
    tmprespond = txt2.get("1.0", "end-1c")
    targetemployee = combo2.get()
    if tmprespond != "":
        window1 = Tk()
        window1.title("Input successful")
        window1.geometry('500x500')
        lbl1_1 = Label(window1, text="System received your respond to employee " + targetemployee)
        lbl1_1.grid(column=0, row=0)
        lbl1_2 = Label(window1, text="Your respond is: " + tmprespond)
        lbl1_2.grid(column=0, row=1)
    else:
        window1 = Tk()
        window1.title("ERROR MESSAGE")
        window1.geometry('300x50')
        lbl1_1 = Label(window1, text="Wrong input. Input cannot be empty.")
        lbl1_1.grid(column=0, row=0)
    testingRespond(tmprespond, targetemployee)


def viewpayroll():
    res = "Your payroll is: " + get_payroll()
    lbl3.configure(text=res)
    testingPayroll()


def viewratings():
    res = "Your rating is: " + get_ratings()
    lbl4.configure(text=res)
    testingRatings()


def setHours():
    global payroll
    workinghours = txt5.get()
    if workinghours.replace('.','',1).isdigit():
        window1 = Tk()
        window1.title("Input successful")
        window1.geometry('300x200')
        lbl1_1 = Label(window1, text="System received your working hours.")
        lbl1_1.grid(column=0, row=0)
        lbl1_2 = Label(window1, text="Please wait for approval.")
        lbl1_2.grid(column=0, row=1)
        lbl1_2 = Label(window1, text="Your working hours this month is: " + workinghours + "hours")
        lbl1_2.grid(column=0, row=2)
        payroll = float(workinghours) * 150
    elif workinghours == "":
        window1 = Tk()
        window1.title("ERROR MESSAGE")
        window1.geometry('300x50')
        lbl1_1 = Label(window1, text="Wrong input. Input cannot be empty.")
        lbl1_1.grid(column=0, row=0)
    else:
        window1 = Tk()
        window1.title("ERROR MESSAGE")
        window1.geometry('300x50')
        lbl1_1 = Label(window1, text="Wrong input. Please type in only numbers.")
        lbl1_1.grid(column=0, row=0)
    testingSetHours(workinghours)


def readdecision():
    window1 = Tk()
    window1.title("Decision")
    window1.geometry('500x300')
    lbl1_1 = Label(window1, text=decision)
    lbl1_1.grid(column=0, row=0)
    if decision_exists:
        lbl6_1.configure(text=decision)
    else:
        text = "No decision was made recently"
        lbl6_1.configure(text=text)
    testingReadDecision()


def senddecision():
    lbl6_1.configure(text="Decision sent")


def clicked7():
    global hoursApproved
    hoursApproved = True
    text = "Employee " + str(combo7.get()) + "'s working hour has been approved"
    lbl7.configure(text=text)
    testingApproveHours()


def get_payroll():
    return str(payroll)


def get_ratings():
    return ratings


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


def testingReadDecision():
    global decision
    if decision == "Bazinga":
        print("read decision functionality test succeeded!")
    else:
        print("read decision functionality test failed!")


def testingApproveHours():
    targetEmployee = combo7.get()
    global hoursApproved
    if targetEmployee == "4" and hoursApproved == True:
        print("Approve Hours functionality test succeeded!")
    else:
        print("Approve Hours functionality test failed!")


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

if __name__ == "__main__":
    window = Tk()
    window.title("DepartmentManger")
    window.geometry('1000x600')

    lbl1 = Label(window, text="Write comment")
    lbl1.grid(column=0, row=0)

    txt1 = Text(window,width=40,height=10)
    txt1.grid(column=1, row=0)
    txt1.focus()

    btn1 = Button(window, text="Send Comment", command=writecomment)
    btn1.grid(column=3, row=0)

    combo1 = Combobox(window)
    combo1['values'] = (1, 2, 3, 4, 5, "Text")
    combo1.current(0)  # set the selected item
    combo1.grid(column=2, row=0)

    lbl2 = Label(window, text="Write respond")
    lbl2.grid(column=0, row=1)

    txt2 = Text(window,width=40,height=10)
    txt2.grid(column=1, row=1)

    btn2 = Button(window, text="Send Respond", command=writerespond)
    btn2.grid(column=3, row=1)

    combo2 = Combobox(window)
    combo2['values'] = (1, 2, 3, 4, 5, "Text")
    combo2.current(0)  # set the selected item
    combo2.grid(column=2, row=1)

    btn3 = Button(window, text="View Payroll", command=viewpayroll)
    btn3.grid(column=1, row=2)

    lbl3 = Label(window, text="Your payroll is: ")
    lbl3.grid(column=0, row=2)

    btn4 = Button(window, text="View Ratings", command=viewratings)
    btn4.grid(column=1, row=3)

    lbl4 = Label(window, text="Your rating is: ")
    lbl4.grid(column=0, row=3)

    lbl5 = Label(window, text="Your working hours: ")
    lbl5.grid(column=0, row=4)

    txt5 = Entry(window, width=40)
    txt5.grid(column=1, row=4)

    btn5 = Button(window, text="Set hours", command=setHours)
    btn5.grid(column=2, row=4)

    lbl6 = Label(window, text="Senior Manager's Decision: ")
    lbl6.grid(column=0, row=5)

    lbl6_1 = Label(window, text="")
    lbl6_1.grid(column=1, row=5)

    btn6 = Button(window, text="Read Decision", command=readdecision)
    btn6.grid(column=2, row=5)

    btn6_1 = Button(window, text="Send Decision", command=senddecision)
    btn6_1.grid(column=3, row=5)

    lbl7 = Label(window, text="")
    lbl7.grid(column=1, row=6)

    btn7 = Button(window, text="Approve Hours", command=clicked7)
    btn7.grid(column=0, row=6)

    combo7 = Combobox(window)
    combo7['values'] = (1, 2, 3, 4, 5, "Text")
    combo7.current(0)  # set the selected item
    combo7.grid(column=2, row=6)

    window.mainloop()