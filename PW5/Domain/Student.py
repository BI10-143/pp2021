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