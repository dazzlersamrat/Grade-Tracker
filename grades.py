import students

def enter_marks():
    students.list_students()
    
    if len(students.students) == 0:
        return
    
    name = input("\nEnter student name to add marks: ")
    student = students.get_student(name)
    
    if student is None:
        print("Student not found!")
        return
    
    print(f"\nEntering marks for {student['name']}")
    print("Enter marks for 5 subjects (0-100):")
    
    subject_names = ["Maths", "Physics", "Chemistry", "English", "Programming"]
    student["marks"] = []
    
    for subject in subject_names:
        while True:
            try:
                mark = float(input(f"  {subject}: "))
                if 0 <= mark <= 100:
                    student["marks"].append({
                        "subject": subject,
                        "mark": mark
                    })
                    break
                else:
                    print("  Please enter a value between 0 and 100.")
            except ValueError:
                print("  Invalid input. Enter a number.")

def calculate_average(student):
    if len(student["marks"]) == 0:
        return 0
    total = sum(m["mark"] for m in student["marks"])
    return total / len(student["marks"])

def calculate_grade(average):
    if average >= 90:
        return "O"
    elif average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "B+"
    elif average >= 50:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"