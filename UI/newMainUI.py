import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import hrSystem
import numpy as np


class newMainUI():

    def __init__(self, master):
        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.master = master
        self.frame = tk.Frame(self.master)
        # username label and entry
        self.username = tk.Label(self.frame, text="Username", anchor="w")
        self.entryun = tk.Entry(self.frame)
        # password label and entry
        self.password = tk.Label(self.frame, text="Password:", anchor="w")
        self.entrypw = tk.Entry(self.frame)
        # login button
        self.login = tk.Button(self.frame, text="Login", command=self.login)
        self.quit = tk.Button(self.frame, text="Quit", command=self.close_window)
        # packing labels, entries and buttons
        self.username.pack(side="top", fill="x")
        self.entryun.pack(side="top", fill="x", padx=20)
        self.password.pack(side="top", fill="x")
        self.entrypw.pack(side="top", fill="x", padx=20)
        self.login.pack(side="right")
        self.quit.pack(side="left")
        self.frame.pack()

    def login(self):
        if self.entryun.get() == "staff":
            self.newWindow = tk.Toplevel(self.master)
            self.newWindow.title("Department Staff")
            self.app = departmentStaffUI(self.newWindow)
            root.withdraw()
        elif self.entryun.get() == "manager":
            self.newWindow = tk.Toplevel(self.master)
            self.newWindow.title("Department Manager")
            self.app = departmentManagerUI(self.newWindow)
            root.withdraw()
        elif self.entryun.get() == "HR":
            self.newWindow = tk.Toplevel(self.master)
            self.newWindow.title("HR Department")
            self.app = HRDepartmentUI(self.newWindow)
            root.withdraw()
        elif self.entryun.get() == "senior":
            self.newWindow = tk.Toplevel(self.master)
            self.newWindow.title("Senior Manager")
            self.app = SeniorManagerUI(self.newWindow)
            root.withdraw()

    def close_window(self):
        root.withdraw()

    def HRpage(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title("User Record")
        self.app = hrsystemui(self.newWindow)


class departmentStaffUI:

    def __init__(self, master):
        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.master = master
        self.frame = tk.Frame(self.master)
        self.payroll = 0
        self.ratings = "Test"
        # Logout
        self.logout = tk.Button(self.frame, text="Logout", command=self.logout)
        # Comment
        self.commentlabel = tk.Label(self.frame, text="Write comment:", anchor="w")
        self.comvalue = tk.StringVar()
        self.comboxlist = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist["values"] = ("A", "B", "C")
        self.comboxlist.current(0)
        self.commententry = tk.Text(self.frame, width=40,height=10)
        self.sendcomment = tk.Button(self.frame, text="Send comments", command=self.writecomment)
        # Respond
        self.respondlabel = tk.Label(self.frame, text="Write respond:", anchor="w")
        self.comvalue_2 = tk.StringVar()
        self.comboxlist_2 = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist_2["values"] = ("A", "B", "C")
        self.comboxlist_2.current(0)
        self.respondentry = tk.Text(self.frame, width=40,height=10)
        self.sendrespond = tk.Button(self.frame, text="Send respond", command=self.writerespond)
        # View Payroll
        self.payrolllabel = tk.Label(self.frame, text="Check monthly payroll:", anchor="w")
        self.viewpayroll = tk.Button(self.frame, text="View Payroll", command=self.view_payroll)
        # View Rating
        self.ratingslabel = tk.Label(self.frame, text="Check ratings:", anchor="w")
        self.viewratings = tk.Button(self.frame, text="View Ratings", command=self.view_ratings)
        # Set Hours
        self.sethourslabel = tk.Label(self.frame, text="Set working hours:", anchor="w")
        self.hoursentry = tk.Entry(self.frame)
        self.sethours = tk.Button(self.frame, text="Set Hours", command=self.set_hours)

        self.commentlabel.grid(column=0, row=0)
        self.comboxlist.grid(column=0, row=1)
        self.commententry.grid(column=0, row=2)
        self.sendcomment.grid(column=0, row=3)
        self.respondlabel.grid(column=1, row=0)
        self.comboxlist_2.grid(column=1, row=1)
        self.respondentry.grid(column=1, row=2)
        self.sendrespond.grid(column=1, row=3)
        self.payrolllabel.grid(column=0, row=4)
        self.viewpayroll.grid(column=1, row=4)
        self.ratingslabel.grid(column=0, row=5)
        self.viewratings.grid(column=1, row=5)
        self.sethourslabel.grid(column=0, row=6)
        self.hoursentry.grid(column=1, row=6)
        self.sethours.grid(column=2, row=6)
        self.logout.grid(column=0, row=7)

        self.frame.pack()

    def writecomment(self):
        tmpcomment = self.commententry.get("1.0", "end-1c")
        targetemployee = self.comboxlist.get()
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

    def writerespond(self):
        tmprespond = self.commententry.get("1.0", "end-1c")
        targetemployee = self.comboxlist_2.get()
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

    def view_payroll(self):
        self.payrolllabel.configure(text="Your payroll is: " + self.get_payroll())

    def view_ratings(self):
        global ratings
        ratings = "test"
        window1 = Tk()
        window1.title("Ratings Checking")
        window1.geometry('300x50')
        lbl1_1 = Label(window1, text="Your ratings:")
        lbl1_1.grid(column=0, row=0)
        lbl1_2 = Label(window1, text=" " + self.get_ratings())
        lbl1_2.grid(column=0, row=1)

    def set_hours(self):
        global payroll
        workinghours = self.hoursentry.get()
        if workinghours.replace('.', '', 1).isdigit():
            window1 = Tk()
            window1.title("Input successful")
            window1.geometry('300x200')
            lbl1_1 = Label(window1, text="System received your working hours.")
            lbl1_1.grid(column=0, row=0)
            lbl1_2 = Label(window1, text="Please wait for approval.")
            lbl1_2.grid(column=0, row=1)
            lbl1_2 = Label(window1, text="Your working hours this month is: " + workinghours + " hours")
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

    def logout(self):
        root.deiconify()
        self.master.destroy()

    def get_payroll(self):
        return str(payroll)

    def get_ratings(self):
        return ratings

class departmentManagerUI:
    def __init__(self, master):
        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.master = master
        self.frame = tk.Frame(self.master)
        self.payroll = 0
        self.ratings = ""
        # Comment
        self.commentlabel = tk.Label(self.frame, text="Write comment:", anchor="w")
        self.comvalue = tk.StringVar()
        self.comboxlist = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist["values"] = ("A", "B", "C")
        self.comboxlist.current(0)
        self.commententry = tk.Text(self.frame, width=40,height=10)
        self.sendcomment = tk.Button(self.frame, text="Send comments", command=self.writecomment)
        # Respond
        self.respondlabel = tk.Label(self.frame, text="Write respond:", anchor="w")
        self.comvalue_2 = tk.StringVar()
        self.comboxlist_2 = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist_2["values"] = ("A", "B", "C")
        self.comboxlist_2.current(0)
        self.respondentry = tk.Text(self.frame, width=40,height=10)
        self.sendrespond = tk.Button(self.frame, text="Send respond", command=self.writerespond)
        # View Payroll
        self.payrolllabel = tk.Label(self.frame, text="Check monthly payroll:", anchor="w")
        self.viewpayroll = tk.Button(self.frame, text="View Payroll", command=self.view_payroll)
        # View Rating
        self.ratingslabel = tk.Label(self.frame, text="Check ratings:", anchor="w")
        self.viewratings = tk.Button(self.frame, text="View Ratings", command=self.view_ratings)
        # Set Hours
        self.sethourslabel = tk.Label(self.frame, text="Set working hours:", anchor="w")
        self.hoursentry = tk.Entry(self.frame)
        self.sethours = tk.Button(self.frame, text="Set Hours", command=self.set_hours)
        # Read Decision
        self.readlabel = tk.Label(self.frame, text="Read senior manager's decision:", anchor="w")
        self.readbutton = tk.Button(self.frame, text="Read Decision", command=self.read_decision)
        # Send Decision
        self.sendlabel = tk.Label(self.frame, text="Send decision to HR:", anchor="w")
        self.sendbutton = tk.Button(self.frame, text="Read Decision", command=self.send_decision)
        # Approve Hours
        self.approvelabel = tk.Label(self.frame, text="Approve working hours:", anchor="w")
        self.comvalue_3 = tk.StringVar()
        self.comboxlist_3 = ttk.Combobox(self.frame, textvariable=self.comvalue_3)
        self.comboxlist_3["values"] = ("A", "B", "C")
        self.comboxlist_3.current(0)
        self.approvehours = tk.Button(self.frame, text="Approve Hours", command=self.approve_hours)
        # Logout
        self.logoutButton = tk.Button(self.frame, text="Logout", command=self.logout)

        self.commentlabel.grid(column=0, row=0)
        self.comboxlist.grid(column=0, row=1)
        self.commententry.grid(column=0, row=2)
        self.sendcomment.grid(column=0, row=3)
        self.respondlabel.grid(column=1, row=0)
        self.comboxlist_2.grid(column=1, row=1)
        self.respondentry.grid(column=1, row=2)
        self.sendrespond.grid(column=1, row=3)
        self.payrolllabel.grid(column=0, row=4)
        self.viewpayroll.grid(column=1, row=4)
        self.ratingslabel.grid(column=0, row=5)
        self.viewratings.grid(column=1, row=5)
        self.sethourslabel.grid(column=0, row=6)
        self.hoursentry.grid(column=1, row=6)
        self.sethours.grid(column=2, row=6)
        self.readlabel.grid(column=0, row=7)
        self.readbutton.grid(column=1, row=7)
        self.sendlabel.grid(column=2, row=7)
        self.sendbutton.grid(column=3, row=7)
        self.approvelabel.grid(column=0, row=8)
        self.comboxlist_3.grid(column=1, row=8)
        self.approvehours.grid(column=2, row=8)
        self.logoutButton.grid(column=0, row=9)
        self.frame.pack()

    def writecomment(self):
        tmpcomment = self.commententry.get("1.0", "end-1c")
        targetemployee = self.comboxlist.get()
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

    def writerespond(self):
        tmprespond = self.commententry.get("1.0", "end-1c")
        targetemployee = self.comboxlist_2.get()
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

    def view_payroll(self):
        self.payrolllabel.configure(text="Your payroll is: " + self.get_payroll())

    def view_ratings(self):
        global ratings
        ratings = "test"
        window1 = Tk()
        window1.title("Ratings Checking")
        window1.geometry('300x50')
        lbl1_1 = Label(window1, text="Your ratings:")
        lbl1_1.grid(column=0, row=0)
        lbl1_2 = Label(window1, text=" " + self.get_ratings())
        lbl1_2.grid(column=0, row=1)

    def set_hours(self):
        global payroll
        workinghours = self.hoursentry.get()
        if workinghours.replace('.', '', 1).isdigit():
            window1 = Tk()
            window1.title("Input successful")
            window1.geometry('300x200')
            lbl1_1 = Label(window1, text="System received your working hours.")
            lbl1_1.grid(column=0, row=0)
            lbl1_2 = Label(window1, text="Please wait for approval.")
            lbl1_2.grid(column=0, row=1)
            lbl1_2 = Label(window1, text="Your working hours this month is: " + workinghours + " hours")
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

    def logout(self):
        root.deiconify()
        self.master.destroy()

    def read_decision(self):
        window1 = Tk()
        window1.title("Senior manager's Decision")
        window1.geometry('500x300')
        lbl1_1 = Label(window1, text="")
        lbl1_1.grid(column=0, row=0)
        #if decision_exists:
        #    lbl6_1.configure(text=decision)
        #else:
        #    text = "No decision was made recently"
        #    lbl6_1.configure(text=text)

    def send_decision(self):
        window1 = Tk()
        window1.title("Decision")
        window1.geometry('500x300')
        lbl1_1 = Label(window1, text="")
        lbl1_1.grid(column=0, row=0)
        # if decision_exists:
        #    lbl6_1.configure(text=decision)
        # else:
        #    text = "No decision was made recently"
        #    lbl6_1.configure(text=text)

    def approve_hours(self):
        window = Tk()
        window.title("Approval")
        window.geometry('500x300')
        text = "Employee " + str(self.comboxlist_3.get()) + "'s working hour has been approved"
        lbl7 = Label(window, text=text)
        lbl7.grid(column=0, row=0)

    def get_payroll(self):
        return str(payroll)

    def get_ratings(self):
        return ratings

class HRDepartmentUI:
    def __init__(self, master):
        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.master = master
        self.frame = tk.Frame(self.master)
        self.payroll = 0
        self.ratings = ""
        # Comment
        self.commentlabel = tk.Label(self.frame, text="Write comment:", anchor="w")
        self.comvalue = tk.StringVar()
        self.comboxlist = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist["values"] = ("A", "B", "C")
        self.comboxlist.current(0)
        self.commententry = tk.Text(self.frame, width=40,height=10)
        self.sendcomment = tk.Button(self.frame, text="Send comments", command=self.writecomment)
        # Respond
        self.respondlabel = tk.Label(self.frame, text="Write respond:", anchor="w")
        self.comvalue_2 = tk.StringVar()
        self.comboxlist_2 = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist_2["values"] = ("A", "B", "C")
        self.comboxlist_2.current(0)
        self.respondentry = tk.Text(self.frame, width=40,height=10)
        self.sendrespond = tk.Button(self.frame, text="Send respond", command=self.writerespond)
        # View Payroll
        self.payrolllabel = tk.Label(self.frame, text="Check monthly payroll:", anchor="w")
        self.viewpayroll = tk.Button(self.frame, text="View Payroll", command=self.view_payroll)
        # View Rating
        self.ratingslabel = tk.Label(self.frame, text="Check ratings:", anchor="w")
        self.viewratings = tk.Button(self.frame, text="View Ratings", command=self.view_ratings)
        # Set Hours
        self.sethourslabel = tk.Label(self.frame, text="Set working hours:", anchor="w")
        self.hoursentry = tk.Entry(self.frame)
        self.sethours = tk.Button(self.frame, text="Set Hours", command=self.set_hours)
        self.execution = tk.Button(self.frame, text="Execute", command=self.execution)
        # Logout
        self.logoutButton = tk.Button(self.frame, text="Logout", command=self.logout)

        self.commentlabel.grid(column=0, row=0)
        self.comboxlist.grid(column=0, row=1)
        self.commententry.grid(column=0, row=2)
        self.sendcomment.grid(column=0, row=3)
        self.respondlabel.grid(column=1, row=0)
        self.comboxlist_2.grid(column=1, row=1)
        self.respondentry.grid(column=1, row=2)
        self.sendrespond.grid(column=1, row=3)
        self.payrolllabel.grid(column=0, row=4)
        self.viewpayroll.grid(column=1, row=4)
        self.ratingslabel.grid(column=0, row=5)
        self.viewratings.grid(column=1, row=5)
        self.sethourslabel.grid(column=0, row=6)
        self.hoursentry.grid(column=1, row=6)
        self.sethours.grid(column=2, row=6)
        self.execution.grid(column=0, row=7)
        self.logoutButton.grid(column=0, row=8)

        self.frame.pack()

    def writecomment(self):
        tmpcomment = self.commententry.get("1.0", "end-1c")
        targetemployee = self.comboxlist.get()
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

    def writerespond(self):
        tmprespond = self.commententry.get("1.0", "end-1c")
        targetemployee = self.comboxlist_2.get()
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

    def view_payroll(self):
        self.payrolllabel.configure(text="Your payroll is: " + self.get_payroll())

    def view_ratings(self):
        global ratings
        ratings = "test"
        window1 = Tk()
        window1.title("Ratings Checking")
        window1.geometry('300x50')
        lbl1_1 = Label(window1, text="Your ratings:")
        lbl1_1.grid(column=0, row=0)
        lbl1_2 = Label(window1, text=" " + self.get_ratings())
        lbl1_2.grid(column=0, row=1)

    def set_hours(self):
        global payroll
        workinghours = self.hoursentry.get()
        if workinghours.replace('.', '', 1).isdigit():
            window1 = Tk()
            window1.title("Input successful")
            window1.geometry('300x200')
            lbl1_1 = Label(window1, text="System received your working hours.")
            lbl1_1.grid(column=0, row=0)
            lbl1_2 = Label(window1, text="Please wait for approval.")
            lbl1_2.grid(column=0, row=1)
            lbl1_2 = Label(window1, text="Your working hours this month is: " + workinghours + " hours")
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

    def execution(self):
        newMainUI.HRpage(self.master)
        # need something

    def logout(self):
        root.deiconify()
        self.master.destroy()

    def get_payroll(self):
        return str(payroll)

    def get_ratings(self):
        return ratings

class SeniorManagerUI:
    def __init__(self, master):
        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.master = master
        self.frame = tk.Frame(self.master)
        self.payroll = 0
        self.ratings = ""
        # Comment
        self.commentlabel = tk.Label(self.frame, text="Write comment:", anchor="w")
        self.comvalue = tk.StringVar()
        self.comboxlist = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist["values"] = ("A", "B", "C")
        self.comboxlist.current(0)
        self.commententry = tk.Text(self.frame, width=40,height=10)
        self.sendcomment = tk.Button(self.frame, text="Send comments", command=self.writecomment)
        # Respond
        self.respondlabel = tk.Label(self.frame, text="Write respond:", anchor="w")
        self.comvalue_2 = tk.StringVar()
        self.comboxlist_2 = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist_2["values"] = ("A", "B", "C")
        self.comboxlist_2.current(0)
        self.respondentry = tk.Text(self.frame, width=40,height=10)
        self.sendrespond = tk.Button(self.frame, text="Send respond", command=self.writerespond)
        # View Payroll
        self.payrolllabel = tk.Label(self.frame, text="Check monthly payroll:", anchor="w")
        self.viewpayroll = tk.Button(self.frame, text="View Payroll", command=self.view_payroll)
        # View Rating
        self.ratingslabel = tk.Label(self.frame, text="Check ratings:", anchor="w")
        self.viewratings = tk.Button(self.frame, text="View Ratings", command=self.view_ratings)
        # Set Hours
        self.sethourslabel = tk.Label(self.frame, text="Set working hours:", anchor="w")
        self.hoursentry = tk.Entry(self.frame)
        self.sethours = tk.Button(self.frame, text="Set Hours", command=self.set_hours)
        #Create decision
        self.createlabel = tk.Label(self.frame, text="Create decision:", anchor="w")
        self.createbutton = tk.Button(self.frame, text="Create decision", command=self.create_decision)
        # Logout
        self.logoutButton = tk.Button(self.frame, text="Logout", command=self.logout)

        self.commentlabel.grid(column=0, row=0)
        self.comboxlist.grid(column=0, row=1)
        self.commententry.grid(column=0, row=2)
        self.sendcomment.grid(column=0, row=3)
        self.respondlabel.grid(column=1, row=0)
        self.comboxlist_2.grid(column=1, row=1)
        self.respondentry.grid(column=1, row=2)
        self.sendrespond.grid(column=1, row=3)
        self.payrolllabel.grid(column=0, row=4)
        self.viewpayroll.grid(column=1, row=4)
        self.ratingslabel.grid(column=0, row=5)
        self.viewratings.grid(column=1, row=5)
        self.sethourslabel.grid(column=0, row=6)
        self.hoursentry.grid(column=1, row=6)
        self.sethours.grid(column=2, row=6)
        self.createlabel.grid(column=0, row=7)
        self.createbutton.grid(column=1, row=7)
        self.logoutButton.grid(column=0, row=8)
        self.frame.pack()

    def writecomment(self):
        tmpcomment = self.commententry.get("1.0", "end-1c")
        targetemployee = self.comboxlist.get()
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

    def writerespond(self):
        tmprespond = self.commententry.get("1.0", "end-1c")
        targetemployee = self.comboxlist_2.get()
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

    def view_payroll(self):
        self.payrolllabel.configure(text="Your payroll is: " + self.get_payroll())

    def view_ratings(self):
        global ratings
        ratings = "test"
        window1 = Tk()
        window1.title("Ratings Checking")
        window1.geometry('300x50')
        lbl1_1 = Label(window1, text="Your ratings:")
        lbl1_1.grid(column=0, row=0)
        lbl1_2 = Label(window1, text=" " + self.get_ratings())
        lbl1_2.grid(column=0, row=1)
        
    def set_hours(self):
        global payroll
        workinghours = self.hoursentry.get()
        if workinghours.replace('.', '', 1).isdigit():
            window1 = Tk()
            window1.title("Input successful")
            window1.geometry('300x200')
            lbl1_1 = Label(window1, text="System received your working hours.")
            lbl1_1.grid(column=0, row=0)
            lbl1_2 = Label(window1, text="Please wait for approval.")
            lbl1_2.grid(column=0, row=1)
            lbl1_2 = Label(window1, text="Your working hours this month is: " + workinghours + " hours")
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

    def create_decision(self):
        window = Tk()
        window.title("Decision")
        window.geometry('500x300')
        label1 = Label(window, text="Decision type: ")
        label2 = Label(window, text="Targeting employee: ")
        combo = Combobox(window)
        combo['values'] = ("Promotion", "Fire", "Salary")
        combo.current(0)  # set the selected item
        combo1 = Combobox(window)
        combo1['values'] = ("A", "B", "C")
        combo1.current(0)  # set the selected item
        detaillabel = Label(window, text="Decision details: ")
        changes = Text(window, width=40, height=10)

        def button():
            print(combo.get() + " decision to Employee: " + combo1.get() + "\nDecision detail:\n" + changes.get("1.0", "end-1c"))

        btn = Button(window, text="Click Me", command=button)
        label1.grid(column=0, row=0)
        combo.grid(column=1, row=0)
        label2.grid(column=0, row=1)
        combo1.grid(column=1, row=1)
        detaillabel.grid(column=0, row=2)
        changes.grid(column=1, row=2)
        btn.grid(column=2, row=2)

    def logout(self):
        root.deiconify()
        self.master.destroy()

    def get_payroll(self):
        return str(payroll)

    def get_ratings(self):
        return ratings


class hrsystemui:

    def __init__(self, master):
        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.master = master
        self.frame = tk.Frame(self.master)
        self.name = tk.Label(self.frame, text="Enter a name:", anchor="w")
        self.entryname = tk.Entry(self.frame)
        self.id = tk.Label(self.frame, text="Enter a ID:", anchor="w")
        self.entryid = tk.Entry(self.frame)
        self.department = tk.Label(self.frame, text="Enter a department:", anchor="w")
        self.entrydepartment = tk.Entry(self.frame)
        self.job = tk.Label(self.frame, text="Select a job type:", anchor="w")
        self.comvalue = tk.StringVar()
        self.comboxlist = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist["values"] = ("Staff", "Department Manager", "Senior Manager")
        self.comboxlist.current(0)
        self.title = tk.Label(self.frame, text="Enter a title:", anchor="w")
        self.entrytitle = tk.Entry(self.frame)
        self.submit = tk.Button(self.frame, text="submit", command=self.action)
        self.show = tk.Button(self.frame, text="show the list", command=self.showList)
        self.deleteUser = tk.Button(self.frame, text="delete user", command=self.deletUser)
        self.amend = tk.Button(self.frame, text="promotion/demotion", command=self.amend)
        self.output = tk.Label(self.frame, text="")
        self.flag = np.array("")
        self.list = np.array("")
        self.result = ""
        self.win = ""
        self.deleteWin = ""
        self.deleteid = ""
        self.deleteWin = ""
        self.amendWin = ""
        self.namelist = tk.Label(self.frame, text="")

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

        self.frame.pack()


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
            self.list=np.delete(self.list,flag,axis=0)


    def amendation(self):
        self.deletUserExecution()
        self.action()
        self.amendWin.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main UI")
    app = newMainUI(root)
    root.mainloop()