import students
import grades

def view_report():
    students.list_students()
    
    if len(students.students) == 0:
        return
    
    name = input("\nEnter student name to view report: ")
    student = students.get_student(name)
    
    if student is None:
        print("Student not found!")
        return
    
    if len(student["marks"]) == 0:
        print("No marks entered for this student yet.")
        return
    
    average = grades.calculate_average(student)
    grade = grades.calculate_grade(average)
    
    print("\n=============================")
    print(f"  Report for {student['name']}")
    print("=============================")
    for m in student["marks"]:
        print(f"  {m['subject']}: {m['mark']}")
    print("-----------------------------")
    print(f"  Average : {average:.2f}")
    print(f"  Grade   : {grade}")
    print("=============================")