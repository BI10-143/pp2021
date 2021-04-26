from domain.Student import *
from domain.Course import *
from domain.Mark import *

class output():
    def student_info(self):
        self.name = input("Enter Student name please:" )
        self.id = input("Enter Student ID please:" )
        self.dob = input("Enter Student DOB please:" )
        return print(f"Student Info: \t{self.name} \t {self.id} \t {self.dob} \n ----------"  )

    def course_info(self):
        self.name = input("Enter Student name please:" )
        self.id = input("Enter Student ID please:" )
        return print(f"Course Info: \t{self.name} \t {self.id} \n ----------"  )

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