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