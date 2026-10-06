# Problem Statement:
# Create a class Person and derive Doctor and Patient. Create additional classes
# representing Surgeon and MedicalResearcher. Design the hierarchy so that the program
# demonstrates multiple inheritance along with hierarchical inheritance.

class Person:
    def __init__(self, name):
        self.name = name


class Doctor(Person):
    def treat(self):
        print(self.name, "treats patients")


class Patient(Person):
    def consult(self):
        print(self.name, "consults doctor")


class Surgeon(Doctor, Patient):
    def operate(self):
        print(self.name, "performs surgery")


class MedicalResearcher(Doctor):
    def research(self):
        print(self.name, "conducts medical research")


s = Surgeon("Dr. Rahul")
m = MedicalResearcher("Dr. Amit")

s.treat()
s.consult()
s.operate()
m.treat()
m.research()
