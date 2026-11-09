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
        "Physics": [67,67, 69],
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

while True:
    print("\n---- STUDENT MANAGEMENT SYSTEM ----")
    print("1. Add Student")
    print("2. Update Grades")
    print("3. Remove Student")
    print("4. View Subject Grades")
    print("5. Search Student")
    print("6. View All Students")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Student Name: ").title()

        if name in students:
            print("Student already exists.")
        else:
            students[name] = {}
            subjects = ["Chemistry", "Physics", "English", "Biology"]

            for subject in subjects:
                grades = []

                for i in range(3):
                    while True:
                        try:
                            grade = int(
                                input(f"{subject} Grade {i+1}: ")
                            )

                            if 0 <= grade <= 100:
                                grades.append(grade)
                                break
                            else:
                                print("Grade must be between 0 and 100.")

                        except ValueError:
                            print("Enter a valid number.")

                students[name][subject] = grades

            print(f"{name} added successfully.")

    elif choice == "2":
        name = input("Enter Student Name: ").title()

        if name in students:
            subject = input(
                "Enter Subject (Chemistry, Physics, English, Biology): "
            ).title()

            if subject in students[name]:
                while True:
                    try:
                        grade = int(input("Enter New Grade: "))

                        if 0 <= grade <= 100:
                            students[name][subject].append(grade)
                            print("Grade added successfully.")
                            break
                        else:
                            print("Grade must be between 0 and 100.")

                    except ValueError:
                        print("Enter a valid number.")
            else:
                print("Subject not found.")
        else:
            print("Student not found.")
    elif choice == "3":

        name = input("Enter Student Name: ").title()
        if name in students:
            del students[name]
            print(f"{name} removed successfully.")
        else:
            print("Student not found.")

    elif choice == "4":

        subject = input(
            "Enter Subject (Chemistry, Physics, English, Biology): "
        ).strip().title()

        found = False

        print(f"\n===== {subject.upper()} GRADES =====")

        for student, subjects in students.items():
            if subject in subjects:
                print(f"{student}: {subjects[subject]}")
                average = sum(subjects[subject]) / len(subjects[subject])

                print(f"Subject Average: {average:.2f}")
                print("-" * 30)

                found = True
        if not found:
            print("Subject not found.")

    elif choice == "5":
        name = input("Enter Student Name: ").strip()
        found = False

        for student in students:
            if student.lower() == name.lower():

                print("\n===== STUDENT REPORT =====")
                print("Student:", student)
                total = 0
                count = 0

                for subject, grades in students[student].items():
                    print(subject, ":", grades)

                    total += sum(grades)
                    count += len(grades)
                average = total / count

                print("Average:", round(average, 2))

                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "6":
        print("\n---- REGISTERED STUDENTS ----")

        for student in students:
            print(student)

    elif choice == "7":
        print("Program Ended.")
        break
    else:
        print("Invalid choice.")