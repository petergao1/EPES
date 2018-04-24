import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import psycopg2
import hrSystem
import numpy as np
import pandas as pd
import csv
import os


class newMainUI():

    def __init__(self, master):
        # database connection setup
        # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()

        cur.execute(
            "Select e.name, l.username from employee e, login_information l where l.employee_id = e.employee_id")
        rows = cur.fetchall()
        print("\n Login Usernames:\n")
        for row in rows:
            print("  ", row[0], ":", row[1])

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.master = master
        self.username = ""
        self.password = ""
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
        # new user button
        self.newuser = tk.Button(self.frame, text="New user", command=self.new_user)
        # packing labels, entries and buttons
        self.username.pack(side="top", fill="x")
        self.entryun.pack(side="top", fill="x", padx=20)
        self.password.pack(side="top", fill="x")
        self.entrypw.pack(side="top", fill="x", padx=20)
        self.login.pack(side="right")
        self.quit.pack(side="left")
        self.newuser.pack(side="right")
        self.frame.pack()
        # database
        self.employeeID = ""
        
    def login(self):
        # database connection setup
        # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get password and authenticate login
        loginSql = ("select l.password, l.employee_id, e.name from login_information l, employee e where l.employee_id = e.employee_id AND l.username = %s")
        loginValues = str(self.entryun.get())
        cur.execute(loginSql, [loginValues])
        rows = cur.fetchall()

        for row in rows:
            print("   ", row[0])
            userPass = row[0]
        self.employeeID = row[1]
        userName = row[2]
        if (self.entrypw.get() == userPass):
            print("Sucessful login")
            window1 = Tk()
            window1.title("Login")
            window1.geometry('200x75')
            lbl1_1 = Label(window1, text="Login Successful")
            lbl1_1.grid(column=0, row=0)
            lbl1_2 = Label(window1, text="Welcome to EPES " + userName)
            lbl1_2.grid(column=0, row=1)
            
                # find role title to display UI
            roleSql = ("select r.title from employee e, role r where e.employee_id = %s AND r.role_id = e.role")
            roleValues = self.employeeID
            cur.execute(roleSql, [roleValues])
            rows = cur.fetchall()
            print("\n " + roleValues + "'s title: ")
            for row in rows:
                print("   ", row[0])
            employeeTitle = row[0]
            
            if "Human" in employeeTitle:
                self.newWindow = tk.Toplevel(self.master)
                self.newWindow.title("HR Department")
                self.app = HRDepartmentUI(self.newWindow, self.employeeID)
                root.withdraw()
            elif "Senior" in employeeTitle:
                self.newWindow = tk.Toplevel(self.master)
                self.newWindow.title("Senior Manager")
                self.app = SeniorManagerUI(self.newWindow, self.employeeID)
                root.withdraw()
            elif "Staff" in employeeTitle:
                self.newWindow = tk.Toplevel(self.master)
                self.newWindow.title("Department Staff")
                self.app = departmentStaffUI(self.newWindow, self.employeeID)
                root.withdraw()
            elif "Manager" in employeeTitle:
                self.newWindow = tk.Toplevel(self.master)
                self.newWindow.title("Department Manager")
                self.app = departmentManagerUI(self.newWindow, self.employeeID)
                root.withdraw()
        else:
            print("Login failed")

        

    def close_window(self):
        root.withdraw()

    def HRpage(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title("User Record")
        self.app = hrsystemui(self.newWindow)

    def new_user(self):
        window = Tk()
        window.title("New User")
        window.geometry('400x200')
        ID_label = Label(window, text="Provide your ID:")
        ID_entry = Entry(window)
        name_label = Label(window, text="Provide your name:")
        name_entry = Entry(window)
        create_un_label = Label(window, text="Create your username:")
        create_pw_label = Label(window, text="Create your password:")
        un_entry = Entry(window)
        pw_entry = Entry(window)

        def save():
            # connect to database
            try:
                conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
            except:
                print("I am unable to connect to the database")
            # database cursor
            cur = conn.cursor()
            newID = ID_entry.get()
            newName = name_entry.get()
            username = un_entry.get()
            password = pw_entry.get()    
                
            try: # Connect to database here, create new user allowed if ID exists
                newUserSql = ("insert into employee (employee_id, name, department, role, salary) VALUES (%s, %s, %s, %s, %s)")
                newUserValues = [newID, newName, "TEMPDEPT", "TEMPROLE", "TEMPSALARY"]
                cur.execute(newUserSql, newUserValues)
                conn.commit()
                newUserLoginSql = ("insert into login_information (username, password, employee_id) VALUES (%s, %s, %s)")
                newUserLoginValues = [username, password, newID]
                cur.execute(newUserLoginSql, newUserLoginValues)
                conn.commit()
            except:
                print("ID already in use. New user not created")

        save = Button(window, text="Save", command=save)
        ID_label.grid(column=0, row=0)
        ID_entry.grid(column=1, row=0)
        name_label.grid(column=0, row=1)
        name_entry.grid(column=1, row=1)
        create_un_label.grid(column=0, row=2)
        create_pw_label.grid(column=1, row=2)
        un_entry.grid(column=0, row=3)
        pw_entry.grid(column=1, row=3)
        save.grid(column=1, row=4)

class HRDepartmentUI:
    def __init__(self, master, eid):
        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.master = master
        self.frame = tk.Frame(self.master)
        self.payroll = 0
        self.ratings = ""
        # Database
        self.employeeID = eid
        # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get employee ids from database to populate dropdown 
        eidSql = ("select employee_id from employee")
        cur.execute(eidSql)
        rows = cur.fetchall()
        self.employeeIDs = []
        for row in rows:
            self.employeeIDs.append(row[0])
         
        # Comment
        self.commentlabel = tk.Label(self.frame, text="Write comment:", anchor="w")
        self.comvalue = tk.StringVar()
        self.comboxlist = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist["values"] = (self.employeeIDs)
        self.comboxlist.current(0)
        self.commententry = tk.Text(self.frame, width=40, height=10)
        self.sendcomment = tk.Button(self.frame, text="Send comments", command=self.writecomment)
        # Respond
        self.respondlabel = tk.Label(self.frame, text="Write response:", anchor="w")
        self.comvalue_2 = tk.StringVar()
        self.comboxlist_2 = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist_2["values"] = (self.employeeIDs)
        self.comboxlist_2.current(0)
        self.respondentry = tk.Text(self.frame, width=40, height=10)
        self.sendrespond = tk.Button(self.frame, text="Send response", command=self.writerespond)
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
        if targetemployee != "":
            window1 = Tk()
            window1.title("Input successful")
            window1.geometry('500x500')
            lbl1_1 = Label(window1, text="System received your comment to employee " + targetemployee)
            lbl1_1.grid(column=0, row=0)
            lbl1_2 = Label(window1, text="Your comment is: " + tmpcomment)
            lbl1_2.grid(column=0, row=1)
            # connect to database
            try:
                conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
            except:
                print("I am unable to connect to the database")
            # database cursor
            cur = conn.cursor()
            # insert new report into database
            insertReportSql = ("insert into rating_report (rating_report_id, report, reportee, reporter) VALUES (%s, %s, %s, %s)")
            import time
            cur.execute(insertReportSql, [time.strftime("%y"+targetemployee+"%m%d"+self.employeeID), tmpcomment, targetemployee, self.employeeID])
            conn.commit()
        else:
            window1 = Tk()
            window1.title("ERROR MESSAGE")
            window1.geometry('300x50')
            lbl1_1 = Label(window1, text="Wrong input. Input cannot be empty.")
            lbl1_1.grid(column=0, row=0)

    def writerespond(self):
        tmprespond = self.respondentry.get("1.0", "end-1c")
        targetemployee = self.comboxlist_2.get()
        if tmprespond != "":
            window1 = Tk()
            window1.title("Input successful")
            window1.geometry('500x200')
            # connect to database
            try:
                conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
            except:
                print("I am unable to connect to the database")
            # database cursor
            cur = conn.cursor()
            # get password and authenticate login
            getReportSql = ("select rr.rating_report_id from rating_report rr where rr.reporter = %s")
            cur.execute(getReportSql, [targetemployee])
            report_id = ""
            rows = cur.fetchall()
            for row in rows:
                report_id = row[0]
                
            insertCommentSql = ("insert into rating_comment (rating_comment_id, comment, rating_report_id) VALUES (%s, %s, %s)")
            import time
            cur.execute(insertCommentSql, [time.strftime("%y"+targetemployee+"%m%d"+self.employeeID), tmprespond, report_id])
            conn.commit()
            lbl1_1 = Label(window1, text="System received your response to employee " + targetemployee)
            lbl1_1.grid(column=0, row=0)
            lbl1_2 = Label(window1, text="Your response is: " + tmprespond)
            lbl1_2.grid(column=0, row=1)
        else:
            window1 = Tk()
            window1.title("ERROR MESSAGE")
            window1.geometry('300x50')
            lbl1_1 = Label(window1, text="Wrong input. Input cannot be empty.")
            lbl1_1.grid(column=0, row=0)

    def view_payroll(self):     
        # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get password and authenticate login
        payrollSql = ("select s.wage, s.bonus, w.hours from work_day w, salary s, employee e where e.salary = s.salary_id AND w.employee_id = e.employee_id AND w.employee_id = %s")
        cur.execute(payrollSql, [self.employeeID])
        rows = cur.fetchall()
        payroll = 0
        for row in rows:
                payroll += (row[0] + row[1]) * row[2]
        self.payrolllabel.configure(text="Your payroll is: " + str(payroll))

    def view_ratings(self):
        global ratings
        ratings = "test"
        window1 = Tk()
        window1.title("Check Ratings")
        window1.geometry('400x100')
        lbl1_1 = Label(window1, text="Your ratings:")
        lbl1_1.grid(column=0, row=0)
        
        
        # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get password and authenticate login
        
        ratingSql = ("select rr.reporter, rr.report, rr.rating_report_id from rating_report rr where rr.reportee= %s")
        cur.execute(ratingSql, [self.employeeID])
        rows = cur.fetchall()
        ratings = ""
        for row in rows:
            try:
                commentSql = ("select comment from rating_comment where rating_report_id = %s")
                cur2=conn.cursor()
                cur2.execute(commentSql, [row[2]])
                comments = cur2.fetchall()
                comment = ""
                for com in comments:
                    comment = com[0]
                ratings += "\nFrom "+row[0] +": \t" +row[1] + "\n\t Response: " + comment
            except:
                ratings += "\nFrom "+row[0] +": \t" +row[1]
            
                
        lbl1_2 = Label(window1, text=" " + ratings)
        lbl1_2.grid(column=0, row=1)

    def set_hours(self):
        workinghours = self.hoursentry.get()
        if workinghours.replace('.', '', 1).isdigit():
            # connect to database
            try:
                conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
            except:
                print("I am unable to connect to the database")
            # database cursor
            cur = conn.cursor()
            # get password and authenticate login
            #getSalarySql = ("select wage
            insertHoursSql = ("insert into work_day (day, employee_id, hours) VALUES (%s, %s, %s)")
            import time
            try:
                cur.execute(insertHoursSql, [time.strftime("%Y-%m-%d"),self.employeeID, workinghours])
                conn.commit()
                window1 = Tk()
                window1.title("Input successful")
                window1.geometry('300x200')
                lbl1_1 = Label(window1, text="System received your working hours.")
                lbl1_1.grid(column=0, row=0)
                lbl1_2 = Label(window1, text="Please wait for approval.")
                lbl1_2.grid(column=0, row=1)
                lbl1_2 = Label(window1, text="You have worked: " + workinghours + " hours today")
                lbl1_2.grid(column=0, row=2)
            except:
                window1 = Tk()
                window1.title("Input failed")
                window1.geometry('100x200')
                lbl1_1 = Label(window1, text="Input error or time already entered today")
                lbl1_1.grid(column=0, row=0)
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


class departmentStaffUI:
    def __init__(self, master, eid):
        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.master = master
        self.frame = tk.Frame(self.master)
        self.payroll = 0
        self.ratings = ""
        # Database
        self.employeeID = eid
        # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get employee ids from database to populate dropdown 
        eidSql = ("select employee_id from employee")
        cur.execute(eidSql)
        rows = cur.fetchall()
        self.employeeIDs = []
        for row in rows:
            self.employeeIDs.append(row[0])
         
        # Comment
        self.commentlabel = tk.Label(self.frame, text="Write comment:", anchor="w")
        self.comvalue = tk.StringVar()
        self.comboxlist = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist["values"] = (self.employeeIDs)
        self.comboxlist.current(0)
        self.commententry = tk.Text(self.frame, width=40, height=10)
        self.sendcomment = tk.Button(self.frame, text="Send comments", command=self.writecomment)
        # Respond
        self.respondlabel = tk.Label(self.frame, text="Write response:", anchor="w")
        self.comvalue_2 = tk.StringVar()
        self.comboxlist_2 = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist_2["values"] = (self.employeeIDs)
        self.comboxlist_2.current(0)
        self.respondentry = tk.Text(self.frame, width=40, height=10)
        self.sendrespond = tk.Button(self.frame, text="Send response", command=self.writerespond)
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
        if targetemployee != "":
            window1 = Tk()
            window1.title("Input successful")
            window1.geometry('500x500')
            lbl1_1 = Label(window1, text="System received your comment to employee " + targetemployee)
            lbl1_1.grid(column=0, row=0)
            lbl1_2 = Label(window1, text="Your comment is: " + tmpcomment)
            lbl1_2.grid(column=0, row=1)
            # connect to database
            try:
                conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
            except:
                print("I am unable to connect to the database")
            # database cursor
            cur = conn.cursor()
            # insert new report into database
            insertReportSql = ("insert into rating_report (rating_report_id, report, reportee, reporter) VALUES (%s, %s, %s, %s)")
            import time
            cur.execute(insertReportSql, [time.strftime("%y"+targetemployee+"%m%d"+self.employeeID), tmpcomment, targetemployee, self.employeeID])
            conn.commit()
        else:
            window1 = Tk()
            window1.title("ERROR MESSAGE")
            window1.geometry('300x50')
            lbl1_1 = Label(window1, text="Wrong input. Input cannot be empty.")
            lbl1_1.grid(column=0, row=0)

    def writerespond(self):
        tmprespond = self.respondentry.get("1.0", "end-1c")
        targetemployee = self.comboxlist_2.get()
        if tmprespond != "":
            window1 = Tk()
            window1.title("Input successful")
            window1.geometry('500x200')
            # connect to database
            try:
                conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
            except:
                print("I am unable to connect to the database")
            # database cursor
            cur = conn.cursor()
            # get password and authenticate login
            getReportSql = ("select rr.rating_report_id from rating_report rr where rr.reporter = %s")
            cur.execute(getReportSql, [targetemployee])
            report_id = ""
            rows = cur.fetchall()
            for row in rows:
                report_id = row[0]
                
            insertCommentSql = ("insert into rating_comment (rating_comment_id, comment, rating_report_id) VALUES (%s, %s, %s)")
            import time
            cur.execute(insertCommentSql, [time.strftime("%y"+targetemployee+"%m%d"+self.employeeID), tmprespond, report_id])
            conn.commit()
            lbl1_1 = Label(window1, text="System received your response to employee " + targetemployee)
            lbl1_1.grid(column=0, row=0)
            lbl1_2 = Label(window1, text="Your response is: " + tmprespond)
            lbl1_2.grid(column=0, row=1)
        else:
            window1 = Tk()
            window1.title("ERROR MESSAGE")
            window1.geometry('300x50')
            lbl1_1 = Label(window1, text="Wrong input. Input cannot be empty.")
            lbl1_1.grid(column=0, row=0)

    def view_payroll(self):     
        # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get password and authenticate login
        payrollSql = ("select s.wage, s.bonus, w.hours from work_day w, salary s, employee e where e.salary = s.salary_id AND w.employee_id = e.employee_id AND w.employee_id = %s")
        cur.execute(payrollSql, [self.employeeID])
        rows = cur.fetchall()
        payroll = 0
        for row in rows:
                payroll += (row[0] + row[1]) * row[2]
        self.payrolllabel.configure(text="Your payroll is: " + str(payroll))

    def view_ratings(self):
        global ratings
        ratings = "test"
        window1 = Tk()
        window1.title("Check Ratings")
        window1.geometry('400x100')
        lbl1_1 = Label(window1, text="Your ratings:")
        lbl1_1.grid(column=0, row=0)
        
        
        # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get password and authenticate login
        
        ratingSql = ("select rr.reporter, rr.report, rr.rating_report_id from rating_report rr where rr.reportee= %s")
        cur.execute(ratingSql, [self.employeeID])
        rows = cur.fetchall()
        ratings = ""
        for row in rows:
            try:
                commentSql = ("select comment from rating_comment where rating_report_id = %s")
                cur2=conn.cursor()
                cur2.execute(commentSql, [row[2]])
                comments = cur2.fetchall()
                comment = ""
                for com in comments:
                    comment = com[0]
                ratings += "\nFrom "+row[0] +": \t" +row[1] + "\n\t Response: " + comment
            except:
                ratings += "\nFrom "+row[0] +": \t" +row[1]
            
                
        lbl1_2 = Label(window1, text=" " + ratings)
        lbl1_2.grid(column=0, row=1)
    def set_hours(self):
        workinghours = self.hoursentry.get()
        if workinghours.replace('.', '', 1).isdigit():
            # connect to database
            try:
                conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
            except:
                print("I am unable to connect to the database")
            # database cursor
            cur = conn.cursor()
            # get password and authenticate login
            #getSalarySql = ("select wage
            insertHoursSql = ("insert into work_day (day, employee_id, hours) VALUES (%s, %s, %s)")
            import time
            try:
                cur.execute(insertHoursSql, [time.strftime("%Y-%m-%d"),self.employeeID, workinghours])
                conn.commit()
                window1 = Tk()
                window1.title("Input successful")
                window1.geometry('300x200')
                lbl1_1 = Label(window1, text="System received your working hours.")
                lbl1_1.grid(column=0, row=0)
                lbl1_2 = Label(window1, text="Please wait for approval.")
                lbl1_2.grid(column=0, row=1)
                lbl1_2 = Label(window1, text="You have worked: " + workinghours + " hours today")
                lbl1_2.grid(column=0, row=2)
            except:
                window1 = Tk()
                window1.title("Input failed")
                window1.geometry('100x200')
                lbl1_1 = Label(window1, text="Input error or time already entered today")
                lbl1_1.grid(column=0, row=0)
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


class departmentManagerUI:
    def __init__(self, master, eid):
        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.master = master
        self.frame = tk.Frame(self.master)
        self.payroll = 0
        self.ratings = ""
        # Database
        self.employeeID = eid
        # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get employee ids from database to populate dropdown 
        eidSql = ("select employee_id from employee")
        cur.execute(eidSql)
        rows = cur.fetchall()
        self.employeeIDs = []
        for row in rows:
            self.employeeIDs.append(row[0])
        # Comment
        self.commentlabel = tk.Label(self.frame, text="Write comment:", anchor="w")
        self.comvalue = tk.StringVar()
        self.comboxlist = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist["values"] = (self.employeeIDs)
        self.comboxlist.current(0)
        self.commententry = tk.Text(self.frame, width=40, height=10)
        self.sendcomment = tk.Button(self.frame, text="Send comments", command=self.writecomment)
        # Respond
        self.respondlabel = tk.Label(self.frame, text="Write response:", anchor="w")
        self.comvalue_2 = tk.StringVar()
        self.comboxlist_2 = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist_2["values"] = (self.employeeIDs)
        self.comboxlist_2.current(0)
        self.respondentry = tk.Text(self.frame, width=40, height=10)
        self.sendrespond = tk.Button(self.frame, text="Send response", command=self.writerespond)
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
        self.decisionID = ""
        # Send Decision
        self.sendlabel = tk.Label(self.frame, text="Send decision to HR:", anchor="w")
        self.sendbutton = tk.Button(self.frame, text="Send Decision", command=self.send_decision)
        # Approve Hours
        self.approvelabel = tk.Label(self.frame, text="Approve working hours:", anchor="w")
        self.comvalue_3 = tk.StringVar()
        self.comboxlist_3 = ttk.Combobox(self.frame, textvariable=self.comvalue_3)
        self.comboxlist_3["values"] = (self.employeeIDs)
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
        if targetemployee != "":
            window1 = Tk()
            window1.title("Input successful")
            window1.geometry('500x500')
            lbl1_1 = Label(window1, text="System received your comment to employee " + targetemployee)
            lbl1_1.grid(column=0, row=0)
            lbl1_2 = Label(window1, text="Your comment is: " + tmpcomment)
            lbl1_2.grid(column=0, row=1)
            # connect to database
            try:
                conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
            except:
                print("I am unable to connect to the database")
            # database cursor
            cur = conn.cursor()
            # insert new report into database
            insertReportSql = ("insert into rating_report (rating_report_id, report, reportee, reporter) VALUES (%s, %s, %s, %s)")
            import time
            cur.execute(insertReportSql, [time.strftime("%y"+targetemployee+"%m%d"+self.employeeID), tmpcomment, targetemployee, self.employeeID])
            conn.commit()
        else:
            window1 = Tk()
            window1.title("ERROR MESSAGE")
            window1.geometry('300x50')
            lbl1_1 = Label(window1, text="Wrong input. Input cannot be empty.")
            lbl1_1.grid(column=0, row=0)

    def writerespond(self):
        tmprespond = self.respondentry.get("1.0", "end-1c")
        targetemployee = self.comboxlist_2.get()
        if tmprespond != "":
            window1 = Tk()
            window1.title("Input successful")
            window1.geometry('500x200')
            # connect to database
            try:
                conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
            except:
                print("I am unable to connect to the database")
            # database cursor
            cur = conn.cursor()
            # get password and authenticate login
            getReportSql = ("select rr.rating_report_id from rating_report rr where rr.reporter = %s")
            cur.execute(getReportSql, [targetemployee])
            report_id = ""
            rows = cur.fetchall()
            for row in rows:
                report_id = row[0]
                
            insertCommentSql = ("insert into rating_comment (rating_comment_id, comment, rating_report_id) VALUES (%s, %s, %s)")
            import time
            cur.execute(insertCommentSql, [time.strftime("%y"+targetemployee+"%m%d"+self.employeeID), tmprespond, report_id])
            conn.commit()
            lbl1_1 = Label(window1, text="System received your response to employee " + targetemployee)
            lbl1_1.grid(column=0, row=0)
            lbl1_2 = Label(window1, text="Your response is: " + tmprespond)
            lbl1_2.grid(column=0, row=1)
        else:
            window1 = Tk()
            window1.title("ERROR MESSAGE")
            window1.geometry('300x50')
            lbl1_1 = Label(window1, text="Wrong input. Input cannot be empty.")
            lbl1_1.grid(column=0, row=0)

    def view_payroll(self):     
        # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get password and authenticate login
        payrollSql = ("select s.wage, s.bonus, w.hours from work_day w, salary s, employee e where e.salary = s.salary_id AND w.employee_id = e.employee_id AND w.employee_id = %s")
        cur.execute(payrollSql, [self.employeeID])
        rows = cur.fetchall()
        payroll = 0
        for row in rows:
                payroll += (row[0] + row[1]) * row[2]
        self.payrolllabel.configure(text="Your payroll is: " + str(payroll))

    def view_ratings(self):
        global ratings
        ratings = "test"
        window1 = Tk()
        window1.title("Check Ratings")
        window1.geometry('400x100')
        lbl1_1 = Label(window1, text="Your ratings:")
        lbl1_1.grid(column=0, row=0)
        
        
        # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get password and authenticate login
        
        ratingSql = ("select rr.reporter, rr.report, rr.rating_report_id from rating_report rr where rr.reportee= %s")
        cur.execute(ratingSql, [self.employeeID])
        rows = cur.fetchall()
        ratings = ""
        for row in rows:
            try:
                commentSql = ("select comment from rating_comment where rating_report_id = %s")
                cur2=conn.cursor()
                cur2.execute(commentSql, [row[2]])
                comments = cur2.fetchall()
                comment = ""
                for com in comments:
                    comment = com[0]
                ratings += "\nFrom "+row[0] +": \t" +row[1] + "\n\t Response: " + comment
            except:
                ratings += "\nFrom "+row[0] +": \t" +row[1]
            
                
        lbl1_2 = Label(window1, text=" " + ratings)
        lbl1_2.grid(column=0, row=1)
        
    def set_hours(self):
        workinghours = self.hoursentry.get()
        if workinghours.replace('.', '', 1).isdigit():
            # connect to database
            try:
                conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
            except:
                print("I am unable to connect to the database")
            # database cursor
            cur = conn.cursor()
            # insert hours into database
            insertHoursSql = ("insert into work_day (day, employee_id, hours) VALUES (%s, %s, %s)")
            import time
            try:
                cur.execute(insertHoursSql, [time.strftime("%Y-%m-%d"),self.employeeID, workinghours])
                conn.commit()
                window1 = Tk()
                window1.title("Input successful")
                window1.geometry('300x200')
                lbl1_1 = Label(window1, text="System received your working hours.")
                lbl1_1.grid(column=0, row=0)
                lbl1_2 = Label(window1, text="Please wait for approval.")
                lbl1_2.grid(column=0, row=1)
                lbl1_2 = Label(window1, text="You have worked: " + workinghours + " hours today")
                lbl1_2.grid(column=0, row=2)
            except:
                window1 = Tk()
                window1.title("Input failed")
                window1.geometry('100x200')
                lbl1_1 = Label(window1, text="Input error or time already entered today")
                lbl1_1.grid(column=0, row=0)
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
        try:
             conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
            # database cursor
        cur = conn.cursor()
        # insert hours into database
        getDecisionSql = ("select senior_manager, decision, decision_id from decision where decision.dept_manager = %s") 
        cur.execute(getDecisionSql, [self.employeeID])
        decisions = cur.fetchall()
        decisiontext = ""
        for dec in decisions:
            decisiontext += "\n Senior Manager: "+dec[0] + ":\n\tDecision:" +dec[1]
        
        self.decisionID = dec[2]     
        window1 = Tk()
        window1.title("Senior manager's Decision")
        window1.geometry('500x300')
        lbl1_1 = Label(window1, text=decisiontext)
        lbl1_1.grid(column=0, row=0)
        

    def send_decision(self):
        try:
             conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
            # database cursor
        cur = conn.cursor()
        # insert hours into database
        sendDecisionSql = ("update decision set hr_staff = %s where decision_id = %s")
        cur.execute(sendDecisionSql, ["sf1", self.decisionID])
        conn.commit()
        
        window1 = Tk()
        window1.title("Senior manager's Decision")
        window1.geometry('500x300')
        lbl1_1 = Label(window1, text="Send decision to sf1")
        lbl1_1.grid(column=0, row=0)

    def approve_hours(self):
    # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get work days and approve them
        workingEmployee = str(self.comboxlist_3.get())
        approveSql = ("update work_day set approved = 'TRUE' where employee_id = %s")
        cur.execute(approveSql, [workingEmployee])
        conn.commit()
        window = Tk()
        window.title("Approval")
        window.geometry('500x300')
        text = "Employee " + workingEmployee+ "'s working hour has been approved"
        lbl7 = Label(window, text=text)
        lbl7.grid(column=0, row=0)

class SeniorManagerUI:
    def __init__(self, master, eid):
        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.master = master
        self.frame = tk.Frame(self.master)
        self.payroll = 0
        self.ratings = ""
        # Database
        self.employeeID = eid
        # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get employee ids from database to populate dropdown 
        eidSql = ("select employee_id from employee")
        cur.execute(eidSql)
        rows = cur.fetchall()
        self.employeeIDs = []
        for row in rows:
            self.employeeIDs.append(row[0])
        # Comment
        self.commentlabel = tk.Label(self.frame, text="Write comment:", anchor="w")
        self.comvalue = tk.StringVar()
        self.comboxlist = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist["values"] = (self.employeeIDs)
        self.comboxlist.current(0)
        self.commententry = tk.Text(self.frame, width=40, height=10)
        self.sendcomment = tk.Button(self.frame, text="Send comments", command=self.writecomment)
        # Respond
        self.respondlabel = tk.Label(self.frame, text="Write response:", anchor="w")
        self.comvalue_2 = tk.StringVar()
        self.comboxlist_2 = ttk.Combobox(self.frame, textvariable=self.comvalue)
        self.comboxlist_2["values"] = (self.employeeIDs)
        self.comboxlist_2.current(0)
        self.respondentry = tk.Text(self.frame, width=40, height=10)
        self.sendrespond = tk.Button(self.frame, text="Send response", command=self.writerespond)
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
        # Create decision
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
        if targetemployee != "":
            window1 = Tk()
            window1.title("Input successful")
            window1.geometry('500x500')
            lbl1_1 = Label(window1, text="System received your comment to employee " + targetemployee)
            lbl1_1.grid(column=0, row=0)
            lbl1_2 = Label(window1, text="Your comment is: " + tmpcomment)
            lbl1_2.grid(column=0, row=1)
            # connect to database
            try:
                conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
            except:
                print("I am unable to connect to the database")
            # database cursor
            cur = conn.cursor()
            # insert new report into database
            insertReportSql = ("insert into rating_report (rating_report_id, report, reportee, reporter) VALUES (%s, %s, %s, %s)")
            import time
            cur.execute(insertReportSql, [time.strftime("%y"+targetemployee+"%m%d"+self.employeeID), tmpcomment, targetemployee, self.employeeID])
            conn.commit()
        else:
            window1 = Tk()
            window1.title("ERROR MESSAGE")
            window1.geometry('300x50')
            lbl1_1 = Label(window1, text="Wrong input. Input cannot be empty.")
            lbl1_1.grid(column=0, row=0)

    def writerespond(self):
        tmprespond = self.respondentry.get("1.0", "end-1c")
        targetemployee = self.comboxlist_2.get()
        if tmprespond != "":
            window1 = Tk()
            window1.title("Input successful")
            window1.geometry('500x200')
            # connect to database
            try:
                conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
            except:
                print("I am unable to connect to the database")
            # database cursor
            cur = conn.cursor()
            # get password and authenticate login
            getReportSql = ("select rr.rating_report_id from rating_report rr where rr.reporter = %s")
            cur.execute(getReportSql, [targetemployee])
            report_id = ""
            rows = cur.fetchall()
            for row in rows:
                report_id = row[0]
                
            insertCommentSql = ("insert into rating_comment (rating_comment_id, comment, rating_report_id) VALUES (%s, %s, %s)")
            import time
            cur.execute(insertCommentSql, [time.strftime("%y"+targetemployee+"%m%d"+self.employeeID), tmprespond, report_id])
            conn.commit()
            lbl1_1 = Label(window1, text="System received your response to employee " + targetemployee)
            lbl1_1.grid(column=0, row=0)
            lbl1_2 = Label(window1, text="Your response is: " + tmprespond)
            lbl1_2.grid(column=0, row=1)
        else:
            window1 = Tk()
            window1.title("ERROR MESSAGE")
            window1.geometry('300x50')
            lbl1_1 = Label(window1, text="Wrong input. Input cannot be empty.")
            lbl1_1.grid(column=0, row=0)

    def view_payroll(self):     
        # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get password and authenticate login
        payrollSql = ("select s.wage, s.bonus, w.hours from work_day w, salary s, employee e where e.salary = s.salary_id AND w.employee_id = e.employee_id AND w.employee_id = %s")
        cur.execute(payrollSql, [self.employeeID])
        rows = cur.fetchall()
        payroll = 0
        for row in rows:
                payroll += (row[0] + row[1]) * row[2]
        self.payrolllabel.configure(text="Your payroll is: " + str(payroll))

    def view_ratings(self):
        global ratings
        ratings = "test"
        window1 = Tk()
        window1.title("Check Ratings")
        window1.geometry('400x100')
        lbl1_1 = Label(window1, text="Your ratings:")
        lbl1_1.grid(column=0, row=0)
        
        
        # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get password and authenticate login
        
        ratingSql = ("select rr.reporter, rr.report from rating_report rr where rr.reportee= %s")
        cur.execute(ratingSql, [self.employeeID])
        rows = cur.fetchall()
        ratings = ""
        for row in rows:
            comments = []
            try:
                commentSql = ("select comment from rating_comment where rating_report_id = %s")                
                cur.execute(commentSql, [row[1]])
                comments = cur.fetchall()
                ratings += "\nFrom "+row[0] +": \t" +row[1] + "\n\t Response: " + comments[0]
            except:
                ratings += "\nFrom "+row[0] +": \t" +row[1]
                
        lbl1_2 = Label(window1, text=" " + ratings)
        lbl1_2.grid(column=0, row=1)

    def set_hours(self):
        workinghours = self.hoursentry.get()
        if workinghours.replace('.', '', 1).isdigit():
            # connect to database
            try:
                conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
            except:
                print("I am unable to connect to the database")
            # database cursor
            cur = conn.cursor()
            # get password and authenticate login
            #getSalarySql = ("select wage
            insertHoursSql = ("insert into work_day (day, employee_id, hours) VALUES (%s, %s, %s)")
            import time
            try:
                cur.execute(insertHoursSql, [time.strftime("%Y-%m-%d"),self.employeeID, workinghours])
                conn.commit()
                window1 = Tk()
                window1.title("Input successful")
                window1.geometry('300x200')
                lbl1_1 = Label(window1, text="System received your working hours.")
                lbl1_1.grid(column=0, row=0)
                lbl1_2 = Label(window1, text="Please wait for approval.")
                lbl1_2.grid(column=0, row=1)
                lbl1_2 = Label(window1, text="You have worked: " + workinghours + " hours today")
                lbl1_2.grid(column=0, row=2)
            except:
                window1 = Tk()
                window1.title("Input failed")
                window1.geometry('100x200')
                lbl1_1 = Label(window1, text="Input error or time already entered today")
                lbl1_1.grid(column=0, row=0)
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
        
         # connect to database
        try:
            conn = psycopg2.connect("dbname='EPES' user='postgres' host='localhost' password='123'")
        except:
            print("I am unable to connect to the database")
        # database cursor
        cur = conn.cursor()
        # get employee ids from database to populate dropdown 
        eidSql = ("select employee_id from employee")
        cur.execute(eidSql)
        rows = cur.fetchall()
        self.employeeIDs = []
        for row in rows:
            self.employeeIDs.append(row[0])
            
        combo = Combobox(window)
        combo['values'] = ("Promotion", "Fire", "Salary")
        combo.current(0)  # set the selected item
        combo1 = Combobox(window)
        combo1['values'] = self.employeeIDs
        combo1.current(0)  # set the selected item
        detaillabel = Label(window, text="Decision details: ")
        changes = Text(window, width=40, height=10)
        def button():
            try:                
                toEmployee = combo1.get()
                decisionID = combo.get()+toEmployee
                decisionText = combo.get()+":"+toEmployee +":"+ str(changes.get("1.0", "end-1c"))
                createDecisionSql = ("insert into decision (senior_manager, dept_manager, decision, decision_id) VALUES(%s, %s, %s, %s)")
                cur.execute(createDecisionSql, [self.employeeID, "ed", decisionText, decisionID])
                conn.commit()
                window1 = Tk()
                window1.title("Creation Success")
                window1.geometry('150x50')
                lbl1_1 = Label(window1, text="Created decision for ed.")
                lbl1_1.grid(column=0, row=0)
            except:
                window1 = Tk()
                window1.title("ERROR MESSAGE")
                window1.geometry('200x50')
                lbl1_1 = Label(window1, text="Decision already exists.")
                lbl1_1.grid(column=0, row=0)
    
        btn = Button(window, text="Create", command=button)
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
        self.header = ['name', 'ID', 'department', 'title', 'job']

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
        if self.comboxlist.get() == "Staff":
            self.flag = np.append(self.flag, [
                hrSystem.Staff(self.entryname.get(), self.entryid.get(), self.entrydepartment.get(),
                               self.entrytitle.get())])
        if self.comboxlist.get() == "Department Manager":
            self.flag = np.append(self.flag, [
                hrSystem.DepartmentManager(self.entryname.get(), self.entryid.get(), self.entrydepartment.get(),
                                           self.entrytitle.get())])
        if self.comboxlist.get() == "Senior Manager":
            self.flag = np.append(self.flag, [
                hrSystem.SeniorManager(self.entryname.get(), self.entryid.get(), self.entrydepartment.get(),
                                       self.entrytitle.get())])
        self.result = self.result + "\n" + "\n" + self.flag[1].__str__()
        self.list = np.append(self.list, self.flag[1])
        self.output.configure(text=self.flag[1].__str__() + "\n has been saved")
        data = np.array([self.flag[1].get_name(), self.flag[1].get_number(), self.flag[1].get_department(),
                         self.flag[1].get_title(), self.flag[1].get_job()])
        df = pd.DataFrame([data])
        if not os.path.isfile('namelist.csv'):
            df.to_csv('namelist.csv', header=self.header, index=False)
        else:
            df.to_csv('namelist.csv', mode='a', header=False, index=False)

        self.flag = np.delete(self.flag, 1)

    def showList(self):
        self.result = ""
        for i in range(self.list.size):
            self.result = self.result + "\n" + "\n" + self.list[i].__str__()
        from tkinter import scrolledtext
        win = tk.Toplevel()
        txt = scrolledtext.ScrolledText(win)
        win.title("Name List")
        win.geometry("240x225")
        txt.insert(tk.INSERT, self.result)
        txt.pack()
        win.mainloop()

    def deletUser(self):
        self.deleteWin = tk.Toplevel()
        self.deleteWin.title("Delete User")
        id = tk.Label(self.deleteWin, text="Enter an ID:", anchor="w")
        idEntry = tk.Entry(self.deleteWin)
        deletebutton = tk.Button(self.deleteWin, text="delete user", command=self.deletUserExecution)
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
        executebutton = tk.Button(self.amendWin, text="Execution", command=self.amendation)
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
            df = pd.read_csv('namelist.csv', header=None)
            df = df.drop(index=flag)
            df.to_csv('namelist.csv', index=False, header=None)
            self.list = np.delete(self.list, flag, axis=0)

    def amendation(self):
        self.deletUserExecution()
        self.action()
        self.amendWin.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main UI")
    app = newMainUI(root)
    root.mainloop()