from student import Student
from data_manager import save_students, load_students

# Create and save students
s1 = Student("S001", "Tejas", {"Math": 90, "Science": 80})
s2 = Student("S002", "Ankit", {"Math": 75, "Science": 65})
students = [s1, s2]

save_students(students)  # saves to grades.json

# Load and display students
loaded_students = load_students()
for s in loaded_students:
    print(f"ID: {s.id}, Name: {s.name}, Subjects: {s.subjects}")
