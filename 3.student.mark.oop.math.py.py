Class student;
    def __init__(self, student_id, student_dob, student_name):
        self.id = student_id
        self.dob = student_dob
        self.name = student_name

    def id_info(self):
        return self.id

    def name_info(self):
        return self.name

    def dob_info(self):
        return self.dob

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

Class Marksheet;
    def __init__(self):
        self.marksheet = []

     def has_marks(self):
        return bool(self.__marksheet)

    def update(self, student, mark):
        self.__marksheet.append((student, mark))

    def get_list(self):
        return self.__marksheet

if __name__ == '__main__':
                ('Input student info', student),
                ('Input course info', course),
                ('Input marks of a course', marks),
                ('Exit', lambda: )]))
