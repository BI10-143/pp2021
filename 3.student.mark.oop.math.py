import numpy
import math

Class student;
    def __init__(self, student_id, student_dob, student_name):
        self.id = student_id
        self.dob = student_dob
        self.name = student_name
        self.marksheet = Marksheet()
        self.gpa = None

    def id_info(self):
        return self.id

    def name_info(self):
        return self.name

    def dob_info(self):
        return self.dob

    def gpa(self):
        return self.gpa
    
    def enter_info(self):
        self.name = input("Enter Student name please:" )
        self.id = input("Enter Student ID please:" )
        self.dob = input("Enter Student DOB please:" )
        return print(f"Student Info: \t{self.name} \t {self.id} \t {self.dob} \n ----------"  )

     def str(self):
        return  f"- Student Name: {self.name}" 
                f"- Student ID: {self.id}" 
                f"- Student DOB: {self.dob}"
    
    def describe(self):
        print(self.str())

Class course;
    def __init__(self, course_id, course_name, marksheet):
        self.id = course_id
        self.name = course_name
        self.marksheet = Marksheet()

    def id_info(self):
        return self.id

    def name_info(self):
        return self.name

    def update_mark(self):
        self.marksheet.update(student, mark)

    def enter_info(self):
        self.name = input("Enter Student name please:" )
        self.id = input("Enter Student ID please:" )
        return print(f"Course Info: \t{self.name} \t {self.id} \n ----------"  )

     def str(self):
        return  f"- Student Name: {self.name}" 
                f"- Student ID: {self.id}"
        
    def str(self):
        print(self.str())

Class Marksheet;
    def __init__(self):
        self.marksheet = []

     def has_marks(self):
        return bool(self.marksheet)

    def update(self, student, mark):
        self.marksheet.append((student, mark))

    def get_list(self):
        return self.marksheet

class management(Management):
    def __init__(self):
        self.students = []
        self.courses = []
        self.marksheets = []

    def getStudents(self):
        return self.students[i]

    def getCourse(self):
        return  self.courses[i]

    def getMark(self):
        return self.marksheets[i]

    def inputSudent(self):
        student = Students()
        student.input()
        self.students += [student]

    def inputCourse(self):
        course = Course()
        course.input()
        self.courses += [course]

    def inputMark(self):
        for i in range(len(self.students))
            m = []
            for j in range(len(self.courses)):
                course = int(input(
                    f"-Enter mark of student name {self.students[i].student_name()} in course {self.courses[j].course_information()}: "))
                m += [course]
            self.marksheets += [m]

    def listMark(self):
        for i in range(len(self.students)):
            for j in range(len(self.courses)):
                print(f"Student {self._stds[i].student_name()} gets {self.marksheet[i][j]} in course {self.courses[j].course_information()}")
        
    def calculate_gpa(self, marks, credits):
        mark = numpy.array(self.marks)
        credit = numpy.array(self.credits)

        sum = 0
        for i in range(len(self.credits)):
            sum += self.credits[i]
        gpa = (mark.credit)/sum
        for i in range(len(self.credits)):
            gpas = gpa[i]
            self.gpa += [gpas]