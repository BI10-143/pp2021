def number_of_students():
    i = int(input('Please enter number of students: '))
    return i

def student_information():
    ids = []
    names = []
    dobs = []
    for i in range(1, count + 1)
        id = int(input('Please enter student ID: '))
        name = int(input('Please enter student Name: '))
        dob = int(input('Please enter student Date of Birth: '))
        ids += id
        names += name
        dobs += dos
    return [ id, name, dob]

def number_of_courses():
    i = int(input('Please enter number of courses: '))
    return i

def course_information():
    id = int(input('Please enter course ID: '))
    name = int(input('Please enter course Name: '))
    return [id, name]

def update_marks(course):
    print("Please enter marks for the course {course['name']}:")
    course['marks'] = []

    for student in students:
        course['marks'].append((student,
            input("Please enter mark for student {student['name']}: ")))

def list_courses():
    print('Listing available courses:')

    for course in courses:
        print("[{course['id']}]. {course['name']}")

def list_students():
    print('Listing students:')

    for student in students:
        print("({student['id']}. {student['dob']}. {student['name']}")

def student_marks(course):
    print("Show marks of the course {course['name']}:")

    for student, mark in course['marks']:
        print("{student['name']}: {mark}")

