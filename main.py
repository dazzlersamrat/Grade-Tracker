import students
import grades
import report
import storage

def show_menu():
    print("\n===== Student Grade Tracker =====")
    print("1. Add a student")
    print("2. Enter marks for a student")
    print("3. View report")
    print("4. Exit")
    print("=================================")

def main():
    storage.load_data()
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            students.add_student()
            storage.save_data()
        elif choice == "2":
            grades.enter_marks()
            storage.save_data()
        elif choice == "3":
            report.view_report()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()