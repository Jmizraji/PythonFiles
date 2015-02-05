import sys
from tools import *

class Student(object):
    """Creates a student profile."""
    def __init__(self, name, major):
        self.name = name
        self.major = major
        print "A student named", self.name, "has been entered into the system " \
              + "as a(n)", self.major, "major.\n"

    def __str__(self):
        global classes_taken
        print self.name + "'s transcript for the", self.major, "major:\n"
        table = ""
        data = classes_taken
        table += "Class\tGrade\tCredits\n"
        table += "-"*25 + "\n"
        for row in data:
            for info in row:
                table += info + "\t"
            table += "\n"
        table += "-"*25
        return table

class Course(object):
    """Creates a course with a student's grade information."""
    def __init__(self, course, grade, credit, student):
        self.course = course
        self.grade = grade
        self.credit = credit
        print student.name, "took", self.course, "worth",\
              self.credit, "credits, and got a", str(grade) + ".\n"

    def to_list(self):
        """Lists the information of the course."""
        return [self.course, self.grade, self.credit]

    def add_to_taken_classes(self, taken_classes):
        """Adds listed class to taken classes."""
        classes_taken.append(self.to_list())

#main
alan = Student("Alan", "Informatics")

classes_taken = []

i101 = Course("I101", "3.0", "3", alan)
i101.add_to_taken_classes(classes_taken)

i201 = Course("I201", "4.0", "3", alan)
i201.add_to_taken_classes(classes_taken)

i210 = Course("I210", "3.0", "3", alan)
i210.add_to_taken_classes(classes_taken)

print alan
