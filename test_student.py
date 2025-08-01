from student import Student

# create a sample student
student = Student("S001", "Tejas")
student.add_subject("Math", 90)
student.add_subject("Science", 85)

print("Subjects:", student.subjects)
print("Average:", student.calculate_average())
print("Grade:", student.calculate_grade())
