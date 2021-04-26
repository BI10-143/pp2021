from domain.Student import *
from domain.Course import *
from domain.Mark import *


s = int(numberofstudent())
m = 1
while m <= s:
    m += 1
    student_info()
student()
c = int(course_num())
p = 1
while p <= c:
    p += 1
    self.course()
course()
mark()

print("  Choose  ")
print("1=YESsss")
print("2=NOooo")
for i in range(0, len(course)):
    course = int(input(" Enter your choose: "))
    if ca == 1:
        print(" Mark of the student ")
        mark()
        break
    else:
        break