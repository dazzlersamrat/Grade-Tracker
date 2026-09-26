students = []
def add_student():
    name = input("Enter student name: ")
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student already exists!")
            return
    students.append({
        "name": name,
        "marks": []
    })
    print(f"Student '{name}' added successfully!")
def get_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None
def list_students():
    if len(students) == 0:
        print("No students added yet.")
    else:
        print("\n--- Student List ---")
        for i, student in enumerate(students):
            print(f"{i+1}. {student['name']}")