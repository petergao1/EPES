import Tkinter as mainUI

class Example(mainUI.Frame):

    def __init__(self, parent):
        mainUI.Frame.__init__(self, parent)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.prompt1 = mainUI.Label(self, text="Please enter username:", anchor="n")
        self.entry1 = mainUI.Entry(self)
        self.prompt2 = mainUI.Label(self, text="Please enter password:", anchor="n")
        self.entry2 = mainUI.Entry(self)
        self.submit = mainUI.Button(self, text="Login", command = self.login)
        self.output = mainUI.Label(self, text="")

        # lay the widgets out on the screen.
        self.prompt1.pack(side="top", fill="x")
        self.entry1.pack(side="top", fill="x", padx=20)
        self.prompt2.pack(side="top", fill="x")
        self.entry2.pack(side="top", fill="x", padx=20)
        self.output.pack(side="top", fill="x", expand=True)
        self.submit.pack(side="right")

    def login(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
        username = self.entry1.get()
        password = self.entry2.get()
        if username = 


# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    root = mainUI.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()