# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 19:20:28 2022

@author: VICTUS
"""
# =============================================================================
# Object Oriented
# =============================================================================
class Student:
    def __init__(self,name,surname,was_born):
        self.name = name
        self.surname = surname
        self.was_born = was_born
        self.course = 1
    def set_course(self,new_course):
        self.course = new_course
    def update_course(self):
        self.course += 1
    def get_info(self):
        return f'{self.name} {self.surname} is {self.course} course student'
    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_wasborn(self):
        return self.was_born

class Subject():
    def __init__(self,named):
        self.named = named
        self.students_number = 0
        self.students = []
    def add_student(self,student):
        """add a student to this subject"""
        self.students.append(student)
        self.students_number += 1
    def get_students(self):
        return [student.get_info() for student in self.students]
        