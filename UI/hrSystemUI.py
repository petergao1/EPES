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
        self.aname = ""
        self.aid = ""
        self.adepartment = ""
        self.atitle = ""
        self.acomboxlist =""

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
        usrid = self.entryid.get()
        if not os.path.isfile('namelist.csv'):
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
            validated = True
        else:
            userids = pd.read_csv('namelist.csv')['ID'].values
            contains = False
            validated = True
            for i in range(len(userids)):
                if userids[i]==usrid:
                    contains = True
                    validated = False
            if not contains:
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
        if validated:
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
        else:
            self.output.configure(text="Duplicated ID, please try typing another ID")


    def showList(self):
        self.result = ""
        df = pd.read_csv('namelist.csv')
        for i in range(len(df)):
            for j in range(0,4):
                self.result = self.result + "\n"+"\n" + str(df.iloc[i][j])
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
        self.aname = nameEntry
        self.aid = idEntry
        self.deleteid = idEntry
        self.adepartment = departmentEntry
        self.atitle = titleEntry
        self.acomboxlist = job
        self.amendWin.mainloop()

    def deletUserExecution(self):
        flag = ""
        idlist = pd.read_csv('namelist.csv')['ID'].values
        deletid = self.deleteid.get()
        for i in range(0, len(idlist)-1):
            print(idlist[i])
            if idlist[i] == deletid:
                if self.deleteWin != "":
                    self.deleteWin.destroy()
                flag = i+1
        if flag != "":
            df = pd.read_csv('namelist.csv',header=None)
            df = df.drop(index=flag)
            df.to_csv('namelist.csv',index=False,header=None)
            self.list=np.delete(self.list,flag,axis=0)


    def amendation(self):
        self.deletUserExecution()
        usrid = self.entryid.get()
        if not os.path.isfile('namelist.csv'):
            if self.acomboxlist.get() == "Staff":
                self.flag = np.append(self.flag, [
                    hrSystem.Staff(self.aname.get(), self.aid.get(), self.adepartment.get(),
                                   self.atitle.get())])
            if self.acomboxlist.get() == "Department Manager":
                self.flag = np.append(self.flag, [
                    hrSystem.DepartmentManager(self.aname.get(), self.aid.get(), self.adepartment.get(),
                                               self.atitle.get())])
            if self.acomboxlist.get() == "Senior Manager":
                self.flag = np.append(self.flag, [
                    hrSystem.SeniorManager(self.aname.get(), self.aid.get(), self.adepartment.get(),
                                           self.atitle.get())])
            validated = True
        else:
            userids = pd.read_csv('namelist.csv')['ID'].values
            contains = False
            validated = True
            for i in range(len(userids)):
                if userids[i] == usrid:
                    contains = True
                    validated = False
            if not contains:
                if self.acomboxlist.get() == "Staff":
                    self.flag = np.append(self.flag, [
                        hrSystem.Staff(self.aname.get(), self.aid.get(), self.adepartment.get(),
                                       self.atitle.get())])
                if self.acomboxlist.get() == "Department Manager":
                    self.flag = np.append(self.flag, [
                        hrSystem.DepartmentManager(self.aname.get(), self.aid.get(), self.adepartment.get(),
                                                   self.atitle.get())])
                if self.acomboxlist.get() == "Senior Manager":
                    self.flag = np.append(self.flag, [
                        hrSystem.SeniorManager(self.aname.get(), self.aid.get(), self.adepartment.get(),
                                               self.atitle.get())])
        if validated:
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
        else:
            self.output.configure(text="Duplicated ID, please try typing another ID")
        self.amendWin.destroy()




        # set the output widget to have our result


# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    root = tk.Tk()
    hrsystemui(root).pack(fill="both", expand=True)
    root.mainloop()