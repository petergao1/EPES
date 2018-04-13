import unittest
from tttt import hrsystemui
import hrSystem
import tkinter as tk

class hrsystemunittest(unittest.TestCase):

    def setUp(self):
        self.staff = hrSystem.Staff("Tom","0001","tech","tech staff")
        self.staff1 = hrSystem.DepartmentManager("Reno","0002","tech","tech manager")

    def test_get(self):
        self.assertEqual(self.staff.get_name(), "Tom")
        self.assertEqual(self.staff.get_number(), "0001")
        self.assertEqual(self.staff.get_department(), "tech")
        self.assertEqual(self.staff.get_job(), "Staff")
        self.assertEqual(self.staff.get_title(), "tech staff")

    def test_set(self):
        self.staff.set_department("marketing")
        self.staff.set_job("Department Manager")
        self.staff.set_name("Tom Law")
        self.staff.set_title("Marketing Manager")
        self.assertEqual(self.staff.get_department(), "marketing")
        self.assertEqual(self.staff.get_job(), "Department Manager")
        self.assertEqual(self.staff.get_title(), "Marketing Manager")
        self.assertEqual(self.staff.get_name(), "Tom Law")

    def test_comment(self):
        self.assertEqual(self.staff.give_comments(self.staff1,"Appoint the meeting on Monday"), "Comment has been delivered")
        self.assertEqual(self.staff1.get_inbox(),"Inbox"+"\n"+"Appoint the meeting on Monday")


if __name__ == '__main__':
    unittest.main()
