import json
from student import Student

def save_students(students, filename="grades.json"):
    with open(filename, 'w') as f:
        json.dump([s.to_dict() for s in students], f, indent=4)

def load_students(filename="grades.json"):
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            if not content:
                return []
            data = json.loads(content)
            return [Student.from_dict(d) for d in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: grades.json is not a valid JSON file. Resetting it.")
        return []
