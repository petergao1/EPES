class CompanyUser:

    def __init__(self, name, number, department, job, title):
        self.name = name
        self.number = number
        self.department = department
        self.job = job
        self.title = title
        self.message = "Inbox"

    def set_name(self, name):
        self.name = name

    def set_number(self, number):
        self.number = number

    def set_department(self, department):
        self.department = department

    def set_job(self, job):
        self.job = job

    def set_title(self, title):
        self.title = title

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_department(self):
        return self.department

    def get_job(self):
        return self.job

    def get_title(self):
        return self.title

    def get_inbox(self):
        return self.message

    def __str__(self):
        return "Name: " + self.name + "\n" + " ID Number " + self.number + "\n" + " Department " + self.department + "\n" + " Job " + self.job + "\n" + " Title " + self.title

    def give_comments(self, employee, content):
        employee.receive_message(content)
        return "Comment has been delivered"

    def receive_message(self, content):
        self.message = self.message + "\n" + content

class SeniorManager(CompanyUser):
    def __init__(self, name, number, department, title):
        self.name = name
        self.number = number
        self.department = department
        self.job = "Senior Manager"
        self.title = title
        self.message = "Inbox"

class DepartmentManager(CompanyUser):
    def __init__(self, name, number, department, title):
        self.name = name
        self.number = number
        self.department = department
        self.job = "Department Manager"
        self.title = title
        self.message = "Inbox"

class Staff(CompanyUser):
    def __init__(self, name, number, department, title):
        self.name = name
        self.number = number
        self.department = department
        self.job = "Staff"
        self.title = title
        self.message = "Inbox"

