from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import hrSystem
import hrSystemUI

payroll = 0;
ratings = "YOU SUCK"
comment = ""
respond = ""
execution = "Employee xxx is fired"
workinghours = 0

import tkinter as tk
import hrSystem
from  tkinter  import ttk
import numpy as np
import pandas as pd
import csv
import os

class hrsystemui(tk.Frame):

    def __init__(self, parent):
        root.title("User record")
        root.geometry("480x450")
        tk.Frame.__init__(self, parent)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.name = tk.Label(self, text="Enter a name:", anchor="w")
        self.entryname = tk.Entry(self)
        self.id = tk.Label(self, text="Enter a ID:", anchor="w")
        self.entryid = tk.Entry(self)
        self.department = tk.Label(self, text="Enter a department:", anchor="w")
        self.entrydepartment = tk.Entry(self)
        self.job = tk.Label(self, text="Select a job type:", anchor="w")
        self.comvalue = tk.StringVar()
        self.comboxlist = ttk.Combobox(self, textvariable=self.comvalue)
        self.comboxlist["values"] = ("Staff", "Department Manager", "Senior Manager")
        self.comboxlist.current(0)
        self.title = tk.Label(self, text="Enter a title:", anchor="w")
        self.entrytitle = tk.Entry(self)
        self.submit = tk.Button(self, text="submit", command = self.action)
        self.show = tk.Button(self, text="show the list", command = self.showList)
        self.deleteUser = tk.Button(self, text="delete user", command = self.deletUser)
        self.amend = tk.Button(self, text="promotion/demotion", command=self.amend)
        self.output = tk.Label(self, text="")
        self.flag = np.array("")
        self.list = np.array("")
        self.result = ""
        self.win=""
        self.deleteWin=""
        self.deleteid=""
        self.deleteWin=""
        self.amendWin=""
        self.namelist=tk.Label(self, text="")
        self.header = ['name','ID','department','title','job']

        # lay the widgets out on the screen.
        self.name.pack(side="top", fill="x")
        self.entryname.pack(side="top", fill="x", padx=20)
        self.id.pack(side="top", fill="x")
        self.entryid.pack(side="top", fill="x", padx=20)
        self.department.pack(side="top", fill="x")
        self.entrydepartment.pack(side="top", fill="x", padx=20)
        self.job.pack(side="top", fill="x")
        self.comboxlist.pack(side="top", fill="x", padx=20)
        self.title.pack(side="top", fill="x")
        self.entrytitle.pack(side="top", fill="x", padx=20)
        self.output.pack(side="top", fill="x", expand=True)
        self.submit.pack(side="right")
        self.deleteUser.pack(side="right")
        self.amend.pack(side="right")
        self.show.pack(side="left")


    def action(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
        if self.comboxlist.get()=="Staff":
            self.flag=np.append(self.flag, [hrSystem.Staff(self.entryname.get(), self.entryid.get(), self.entrydepartment.get(), self.entrytitle.get())])
        if self.comboxlist.get()=="Department Manager":
            self.flag=np.append(self.flag, [hrSystem.DepartmentManager(self.entryname.get(), self.entryid.get(), self.entrydepartment.get(), self.entrytitle.get())])
        if self.comboxlist.get()=="Senior Manager":
            self.flag=np.append(self.flag, [hrSystem.SeniorManager(self.entryname.get(), self.entryid.get(), self.entrydepartment.get(), self.entrytitle.get())])
        self.result = self.result+"\n"+"\n"+self.flag[1].__str__()
        self.list = np.append(self.list,self.flag[1])
        self.output.configure(text=self.flag[1].__str__()+"\n has been saved")
        data = np.array([self.flag[1].get_name(),self.flag[1].get_number(),self.flag[1].get_department(),self.flag[1].get_title(),self.flag[1].get_job()])
        df = pd.DataFrame([data])
        if not os.path.isfile('namelist.csv'):
            df.to_csv('namelist.csv', header=self.header,index=False)
        else:
            df.to_csv('namelist.csv', mode='a',header=False,index=False)

        self.flag = np.delete(self.flag,1)


    def showList(self):
        self.result = ""
        for i in range(self.list.size):
            self.result = self.result + "\n"+"\n"+self.list[i].__str__()
        from tkinter import scrolledtext
        win = tk.Toplevel()
        txt = scrolledtext.ScrolledText(win)
        win.title("Name List")
        win.geometry("240x225")
        txt.insert(tk.INSERT,self.result)
        txt.pack()
        win.mainloop()

    def deletUser(self):
        self.deleteWin = tk.Toplevel()
        self.deleteWin.title("Delete User")
        id = tk.Label(self.deleteWin, text="Enter an ID:", anchor="w")
        idEntry = tk.Entry(self.deleteWin)
        deletebutton = tk.Button(self.deleteWin, text="delete user", command = self.deletUserExecution)
        id.pack(side="top", fill="x")
        idEntry.pack(side="top", fill="x", padx=20)
        deletebutton.pack(side="bottom")
        self.deleteid = idEntry
        self.deleteWin.mainloop()

    def amend(self):
        self.amendWin = tk.Toplevel()
        self.amendWin.title("Promotion/Demotion")
        name = tk.Label(self.amendWin, text="Enter the name:", anchor="w")
        nameEntry = tk.Entry(self.amendWin)
        department = tk.Label(self.amendWin, text="Enter the department (enter the new one if changed):", anchor="w")
        departmentEntry = tk.Entry(self.amendWin)
        id = tk.Label(self.amendWin, text="Enter the ID:", anchor="w")
        idEntry = tk.Entry(self.amendWin)
        title = tk.Label(self.amendWin, text="Enter the new title:", anchor="w")
        titleEntry = tk.Entry(self.amendWin)
        newJob = tk.Label(self.amendWin, text="Enter the new job:", anchor="w")
        jobvalue = tk.StringVar()
        job = ttk.Combobox(self.amendWin, textvariable=jobvalue)
        job["values"] = ("Staff", "Department Manager", "Senior Manager")
        executebutton = tk.Button(self.amendWin, text="Execution", command = self.amendation)
        name.pack(side="top", fill="x")
        nameEntry.pack(side="top", fill="x", padx=20)
        department.pack(side="top", fill="x")
        departmentEntry.pack(side="top", fill="x", padx=20)
        id.pack(side="top", fill="x")
        idEntry.pack(side="top", fill="x", padx=20)
        title.pack(side="top", fill="x")
        titleEntry.pack(side="top", fill="x", padx=20)
        newJob.pack(side="top", fill="x")
        job.pack(side="top", fill="x", padx=20)
        executebutton.pack(side="bottom")
        self.entryname = nameEntry
        self.entryid = idEntry
        self.deleteid = idEntry
        self.entrydepartment = departmentEntry
        self.entrytitle = titleEntry
        self.comboxlist = job
        self.amendWin.mainloop()

    def deletUserExecution(self):
        flag = ""
        for i in range(1, self.list.size):
            if self.list[i].get_number() == self.deleteid.get():
                if self.deleteWin != "":
                    self.deleteWin.destroy()
                flag = i
        if flag != "":
            df = pd.read_csv('namelist.csv',header=None)
            df = df.drop(index=flag)
            df.to_csv('namelist.csv',index=False,header=None)
            self.list=np.delete(self.list,flag,axis=0)


    def amendation(self):
        self.deletUserExecution()
        self.action()
        self.amendWin.destroy()




        # set the output widget to have our result


# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop
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
    root = Toplevel()
    hrsystemui(root).pack(fill="both", expand=True)
    root.mainloop()
    #if execution == "Employee xxx is fired":
     #   print("Execution functionality test succeeded!")
    #else:
    #    print("Execution functionality test failed!")


if __name__ == "__main__":
    root = Tk()
    window = Tk()
    window.title("HRDepartmentUI")
    window.geometry('700x450')

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

    btn5 = Button(window, text="Set hours:", command=setHours)
    btn5.grid(column=2, row=4)

    btn6 = Button(window, text="Execute Decisions", command=execute)
    btn6.grid(column=2, row=5)

    window.mainloop()