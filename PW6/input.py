import numpy
import math

def enter_info(self):
        self.name = input("Enter Student name please:" )
        self.id = input("Enter Student ID please:" )
        self.dob = input("Enter Student DOB please:" )
        return print(f"Student Info: \t{self.name} \t {self.id} \t {self.dob}"  )

     def str(self):
        return  f"- Student Name: {self.name}" 
                f"- Student ID: {self.id}" 
                f"- Student DOB: {self.dob}"
    
    def describe(self):
        print(self.str())

def enter_info(self):
        self.name = input("Enter Student name please:" )
        self.id = input("Enter Student ID please:" )
        return print(f"Course Info: \t{self.name} \t {self.id}"  )

     def str(self):
        return  f"- Student Name: {self.name}" 
        return  f"- Student ID: {self.id}"
        
    def str(self):
        print(self.str())

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
                    f"Please Enter mark of student name {self.students[i].student_name()} in course {self.courses[j].course_information()}: "))
                m += [course]
            self.marksheets += [m]s
