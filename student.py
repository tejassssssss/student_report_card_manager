class Student:
    def __init__(self, student_id, name, subjects=None):
        self.id = student_id
        self.name = name
        self.subjects = subjects if subjects else {}

    def add_subject(self, subject, score):
        self.subjects[subject] = score

    def update_score(self, subject, score):
        if subject in self.subjects:
            self.subjects[subject] = score

    def delete_subject(self, subject):
        if subject in self.subjects:
            del self.subjects[subject]

    def calculate_average(self):
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "subjects": self.subjects
        }

    @staticmethod
    def from_dict(data):
        return Student(
            student_id=data['id'],
            name=data['name'],
            subjects=data['subjects']
        )
