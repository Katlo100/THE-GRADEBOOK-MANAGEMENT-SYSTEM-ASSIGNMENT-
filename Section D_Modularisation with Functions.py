students = {
    "Katlo": {
        "Chemistry": [85, 67, 80],
        "Physics": [69, 69, 90],
        "English": [80, 90, 89],
        "Biology": [92, 69, 50]
    },
    "Bonolo": {
        "Chemistry": [56, 67, 59],
        "Physics": [84, 68, 68],
        "English": [75, 68, 90],
        "Biology": [43, 67, 69]
    },
    "Kabelo": {
        "Chemistry": [58, 80, 68],
        "Physics": [67, 67, 69],
        "English": [84, 58, 78],
        "Biology": [94, 69, 69]
    },
    "Mighty": {
        "Chemistry": [56, 90, 59],
        "Physics": [90, 70, 59],
        "English": [56, 69, 70],
        "Biology": [84, 78, 65]
    },
    "Marang": {
        "Chemistry": [60, 79, 89],
        "Physics": [69, 80, 79],
        "English": [94, 79, 69],
        "Biology": [89, 70, 69]
    },
    "Rachael": {
        "Chemistry": [83, 79, 90],
        "Physics": [56, 78, 60],
        "English": [60, 88, 78],
        "Biology": [66, 77, 68]
    }
}

def get_valid_grade():
    while True:
        try:
            grade = int(input("Enter Grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Error: Grade must be between 0 and 100.")

        except ValueError:
            print("Error: Please enter a valid number.")

def add_student():
    student_name = input("Enter Student Name: ").title()

    if student_name in students:
        print("Student already exists.")
        return

    students[name] = {}
    subjects = ["Chemistry", "Physics", "English", "Biology"]

    for subject in subjects:
        grades = []
        print(f"\nEnter grades for {subject}")

        for i in range(3):
            print(f"Test {i + 1}")
            grade = get_valid_grade()
            grades.append(grade)

        students[name][subject] = grades
    print(f"{name} added successfully.")

def calculate_average(student_name):

    total = 0
    count = 0

    for grades in students[student_name].values():
        total += sum(grades)
        count += len(grades)

    return total / count

def display_student(student_name):
    if student_name not in students:
        print("Student not found.")
        return

    print("\n----- STUDENT REPORT -----")
    print("Name:", student_name)

    for subject, grades in students[student_name].items():
        print(subject, ":", grades)

    average = calculate_average(student_name)
    print("Average:", round(average, 2))

def display_student_summary():
    print("\n----- STUDENT SUMMARY -----")

    for student in students:
        average = calculate_average(student)
        print(
            f"{student} - Average: {average:.2f}"
        )

def search_and_update():
    student_name = input("Enter Student Name: ").title()

    if student_name not in students:
        print("Student not found.")
        return
    print("\nStudent Found")
    display_student(name)

    choice = input(
        "\nDo you want to update grades? (yes/no): "
    ).lower()

    if choice == "yes":
        subject = input(
            "Enter Subject (Chemistry, Physics, English, Biology): "
        ).title()

        if subject not in students[name]:
            print("Subject not found.")
            return

        grade = get_valid_grade()
        students[name][subject].append(grade)

        print("Grade updated successfully.")

def remove_student():
    student_name = input("Enter Student Name: ").title()

    if student_name in students:
        del students[name]
        print("Student removed successfully.")
    else:
        print("Student not found.")

def view_subject_grades():
    subject = input(
        "Enter Subject (Chemistry, Physics, English, Biology): "
    ).title()
    subject_marks = []

    print(f"\n----- {subject} GRADES -----")

    for student, subjects in students.items():

        if subject in subjects:
            print(student, ":", subjects[subject])
            subject_marks.extend(subjects[subject])

    if len(subject_marks) > 0:

        print("\nHighest Grade:", max(subject_marks))
        print("Lowest Grade:", min(subject_marks))
        print(
            "Subject Average:",
            round(sum(subject_marks) / len(subject_marks), 2)
        )

    else:
        print("Subject not found.")

while True:

    print("\n----- STUDENT MANAGEMENT SYSTEM -----")
    print("1. Add Student")
    print("2. Search and Update Student")
    print("3. Remove Student")
    print("4. View Subject Grades")
    print("5. Display Student")
    print("6. Display Students Summary")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_and_update()

    elif choice == "3":
        remove_student()

    elif choice == "4":
        view_subject_grades()

    elif choice == "5":

        name = input("Enter Student Name: ").title()
        display_student(name)

    elif choice == "6":
        display_student_summary()

    elif choice == "7":
        print("Program Ended.")
        break

    else:
        print("Invalid choice.")