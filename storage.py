import students
import grades

def save_data():
    file = open("data.txt", "w")
    for student in students.students:
        file.write(f"STUDENT:{student['name']}\n")
        for m in student["marks"]:
            file.write(f"MARK:{m['subject']}:{m['mark']}\n")
    file.close()
    print("Data saved successfully!")

def load_data():
    try:
        file = open("data.txt", "r")
        current_student = None
        for line in file:
            line = line.strip()
            if line.startswith("STUDENT:"):
                name = line.split(":")[1]
                students.students.append({
                    "name": name,
                    "marks": []
                })
                current_student = students.students[-1]
            elif line.startswith("MARK:") and current_student:
                parts = line.split(":")
                current_student["marks"].append({
                    "subject": parts[1],
                    "mark": float(parts[2])
                })
        file.close()
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("No saved data found. Starting fresh.")