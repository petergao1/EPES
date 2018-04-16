from tkinter import *
from tkinter.ttk import *
import hrSystem

payroll = 1000000;
ratings = "YOU ARE THE BOSS"
comment = ""
respond = ""
workinghours = 0
decision_exists = False
decision = "Bazinga"
employeeID = 0000


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


def clicked5():
    decision = txt5.get("1.0", "end-1c")
    testingDecision(decision)


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
    if get_payroll() == "1000000":
        print("view payroll functionality test succeeded!")
    else:
        print(get_payroll())
        print("view payroll functionality test failed!")


def testingRatings():
    if get_ratings() == "YOU ARE THE BOSS":
        print("view ratings functionality test succeeded!")
    else:
        print("view ratings functionality test failed!")


def testingDecision(decision):
    if decision == "Testing Decision":
        print("Making Decision functionality test succeeded!")
    else:
        print("Making Decision functionality test failed!")

if __name__ == "__main__":
    window = Tk()
    window.title("SeniorManagerUI")
    window.geometry('600x400')

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

    lbl5 = Label(window, text="Create Decision: ")
    lbl5.grid(column=0, row=4)

    btn5 = Button(window, text="Create Decision", command=clicked5)
    btn5.grid(column=2, row=4)

    txt5 = Text(window,width=40,height=10)
    txt5.grid(column=1, row=4)

    window.mainloop()