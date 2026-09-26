# Grade Tracker

A command-line application built in Python to manage student grades.

## Features
- Add students
- Enter subject marks for each student
- Automatically calculate average and grade
- View detailed report for each student
- Save and load data from file

## Technologies Used
- Python 3
- File handling (data.txt)

## Project Structure
grade_tracker/
├── main.py
├── students.py
├── grades.py
├── report.py
├── storage.py
├── README.md
└── statement.md

## How to Run
1. Make sure Python 3 is installed on your system
2. Clone the repository:
   git clone https://github.com/dazzlersamrat/Grade-Tracker.git
3. Navigate to the folder:
   cd Grade-Tracker
4. Run the application:
   python main.py

## How to Use
1. Choose option 1 to add a student
2. Choose option 2 to enter marks for a student
3. Choose option 3 to view the grade report
4. Choose option 4 to exit

## Grading System
- O  : 90 - 100
- A+ : 80 - 89
- A  : 70 - 79
- B+ : 60 - 69
- B  : 50 - 59
- C  : 40 - 49
- F  : Below 40

## Testing
Run the app and:
1. Add a student named "Test"
2. Enter marks for all 5 subjects
3. View the report to verify grades are calculated correctly