# main.py

from student import Student
from data_manager import save_students, load_students

students = load_students()

def generate_student_id():
    return f"S{1000 + len(students)}"

def find_student_by_id(student_id):
    for student in students:
        if student.id == student_id:
            return student
    return None

def add_student():
    name = input("Enter student name: ")
    student_id = generate_student_id()
    subjects = {}
    while True:
        subject = input("Enter subject (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            score = float(input(f"Enter score for {subject}: "))
            subjects[subject] = score
        except ValueError:
            print("Invalid score. Please enter a number.")
    student = Student(student_id, name, subjects)
    students.append(student)
    print(f"Student '{name}' added with ID: {student.id}")

def update_score():
    student_id = input("Enter student ID to update: ")
    student = find_student_by_id(student_id)
    if not student:
        print("❌ Student not found.")
        return

    subject = input("Enter subject to update: ")
    try:
        score = float(input(f"Enter new score for {subject}: "))
        student.update_score(subject, score)
        print("✅ Score updated.")
    except ValueError:
        print("Invalid score input.")

def view_reports():
    if not students:
        print("No students found.")
        return
    for student in students:
        print("\n" + "-" * 40)
        print(f"ID      : {student.id}")
        print(f"Name    : {student.name}")
        print("Subjects:")
        for subject, score in student.subjects.items():
            print(f"  {subject}: {score}")
        print(f"Average : {student.calculate_average():.2f}")
        print(f"Grade   : {student.calculate_grade()}")
        print("-" * 40)

def delete_student():
    student_id = input("Enter student ID to delete: ")
    global students
    before_count = len(students)
    students = [s for s in students if s.id != student_id]
    after_count = len(students)
    if before_count == after_count:
        print("❌ No such student found.")
    else:
        print("✅ Student deleted.")

def main():
    print("\n📘 Welcome to Student Report Card Manager 📘")
    while True:
        print("\nChoose an option:")
        print("1. Add Student")
        print("2. Update Score")
        print("3. View Reports")
        print("4. Delete Student")
        print("5. Save & Exit")

        choice = input("Enter choice (1–5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_score()
        elif choice == '3':
            view_reports()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            save_students(students)
            print("💾 Data saved to grades.json. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1–5.")

if __name__ == "__main__":
    main()
