#!/usr/bin/env python
# coding: utf-8


class students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print("name and age is:" + self.name + self.age)

    def marks(self):
        return self.grade

    def sitting(self):
        self.sit = True
        return self.sit

    def standing(self):
        self.sit = False
        return self.sit


r = students('bob', '18', '50')
r1 = students('sam', '20', '10')
print(r1.marks())
print(r1.sitting())


class kolkata:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def introduction(self):
        return self.name

    def statusreport(self):
        return self.name


r3 = kolkata('ajay', 'police')
print(r3.statusreport())
# owning a class instances in another class and working with it
r3.statusreport_own = r
print(r3.statusreport())
print(r3.statusreport_own.marks())
