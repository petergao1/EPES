import tkinter as tk
import companyuser
from  tkinter  import ttk
import numpy as np

class Example(tk.Frame):

    def __init__(self, parent):
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
        self.submit = tk.Button(self, text="Submit", command = self.calculate)
        self.output = tk.Label(self, text="")
        self.flag = np.array("")
        self.list = np.array("")
        self.result = ""

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

    def calculate(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
        if self.comboxlist.get()=="Staff":
            self.flag=np.append(self.flag,[companyuser.Staff(self.entryname.get(),self.entryid.get(),self.entrydepartment.get(),self.entrytitle.get())])
        if self.comboxlist.get()=="Department Manager":
            self.flag=np.append(self.flag,[companyuser.DepartmentManager(self.entryname.get(),self.entryid.get(),self.entrydepartment.get(),self.entrytitle.get())])
        if self.comboxlist.get()=="Senior Manager":
            self.flag=np.append(self.flag,[companyuser.SeniorManager(self.entryname.get(),self.entryid.get(),self.entrydepartment.get(),self.entrytitle.get())])
        self.result = self.result+"\n"+"\n"+self.flag[1].__str__()
        self.list = np.append(self.list,self.flag[1])
        self.flag = np.delete(self.flag,1)
        print(self.entryname.get(),self.flag.size)
        self.output.configure(text=self.result)

        # set the output widget to have our result


# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()