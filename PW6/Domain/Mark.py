def __init__(self):
        self.marksheet = []

     def has_marks(self):
        return bool(self.marksheet)

    def update(self, student, mark):
        self.marksheet.append((student, mark))

    def get_list(self):
        return self.marksheet