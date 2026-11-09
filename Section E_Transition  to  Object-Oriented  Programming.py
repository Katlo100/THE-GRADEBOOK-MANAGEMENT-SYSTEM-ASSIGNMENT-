class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []

        self.grades[subject].append(grade)

    def calculate_average(self):
        total = 0
        count = 0

        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)

        if count == 0:
            return 0

        return total / count

    def display_details(self):
        print("\n----- STUDENT REPORT ------")
        print("Student Name:", self.name)

        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")

        print("Average:", round(self.calculate_average(), 2))


class Gradebook:
    def __init__(self):
        self.students = {}

    def add_student(self, student):

        if student.name in self.students:
            print("Student already exists.")
            return False

        self.students[student.name] = student
        print(f"{student.name} added successfully.")
        return True

    def remove_student(self, name):

        student = self.search_student(name)

        if student:
            del self.students[student.name]
            print("Student removed successfully.")
        else:
            print("Student not found.")

    def search_student(self, name):

        for student in self.students.values():

            if student.name.lower() == name.lower():
                return student

        return None

    def display_all_students(self):

        if not self.students:
            print("No students found.")
            return

        for student in self.students.values():
            student.display_details()

    def sort_by_average(self):

        sorted_students = sorted(
            self.students.values(),
            key=lambda student: student.calculate_average(),
            reverse=True
        )

        print("\n-----STUDENTS SORTED BY AVERAGE-----")

        rank = 1

        for student in sorted_students:
            print(
                f"{rank}. {student.name:<15} "
                f"Average: {student.calculate_average():.2f}"
            )

            rank += 1

    def sort_by_subject(self, subject):
        subject = subject.title()
        subject_students = []

        for student in self.students.values():
            if subject in student.grades:
                average = (
                    sum(student.grades[subject]) /
                    len(student.grades[subject])
                )

                subject_students.append(
                    (student.name, average)
                )

        if not subject_students:
            print(f"No grades found for {subject}.")
            return

        subject_students.sort(
            key=lambda x: x[1],
            reverse=True
        )

        print(f"\n-----RANKING FOR {subject.upper()}-----")
        rank = 1
        previous_average = None

        for index, (student_name, average) in enumerate(subject_students):
            if previous_average is not None and average < previous_average:
                rank = index + 1

            print(
                f"{rank}. {student_name:<15} Average: {average:.2f}"
            )

            previous_average = average

        highest_average = subject_students[0][1]

        print("\nTop Student(s):")

        for student_name, average in subject_students:
            if average == highest_average:
                print(f"{name} ({average:.2f})")

    def total_students(self):
        return len(self.students)

gradebook = Gradebook()

s1 = Student("Katlo")
s1.add_grade("Chemistry", 85)
s1.add_grade("Chemistry", 67)
s1.add_grade("Chemistry", 80)
s1.add_grade("Physics", 69)
s1.add_grade("Physics", 69)
s1.add_grade("Physics", 90)
s1.add_grade("English", 80)
s1.add_grade("English", 90)
s1.add_grade("English", 89)
s1.add_grade("Biology", 92)
s1.add_grade("Biology", 69)
s1.add_grade("Biology", 50)
gradebook.add_student(s1)

s2 = Student("Bonolo")
s2.add_grade("Chemistry", 56)
s2.add_grade("Chemistry", 67)
s2.add_grade("Chemistry", 59)
s2.add_grade("Physics", 84)
s2.add_grade("Physics", 68)
s2.add_grade("Physics", 68)
s2.add_grade("English", 75)
s2.add_grade("English", 68)
s2.add_grade("English", 90)
s2.add_grade("Biology", 43)
s2.add_grade("Biology", 67)
s2.add_grade("Biology", 69)
gradebook.add_student(s2)

s3 = Student("Kabelo")
s3.add_grade("Chemistry", 58)
s3.add_grade("Chemistry", 69)
s3.add_grade("Chemistry", 78)
s3.add_grade("Physics", 67)
s3.add_grade("Physics", 78)
s3.add_grade("Physics", 53)
s3.add_grade("English", 84)
s3.add_grade("English", 69)
s3.add_grade("English", 68)
s3.add_grade("Biology", 94)
s3.add_grade("Biology", 69)
s3.add_grade("Biology", 69)
gradebook.add_student(s3)

s4 = Student("Mighty")
s4.add_grade("Chemistry", 56)
s4.add_grade("Chemistry", 90)
s4.add_grade("Chemistry", 59)
s4.add_grade("Physics", 90)
s4.add_grade("Physics", 70)
s4.add_grade("Physics", 59)
s4.add_grade("English", 56)
s4.add_grade("English", 69)
s4.add_grade("English", 70)
s4.add_grade("Biology", 84)
s4.add_grade("Biology", 78)
s4.add_grade("Biology", 65)
gradebook.add_student(s4)

s5 = Student("Marang")
s5.add_grade("Chemistry", 60)
s5.add_grade("Chemistry", 79)
s5.add_grade("Chemistry", 89)
s5.add_grade("Physics", 69)
s5.add_grade("Physics", 80)
s5.add_grade("Physics", 79)
s5.add_grade("English", 94)
s5.add_grade("English", 79)
s5.add_grade("English", 69)
s5.add_grade("Biology", 89)
s5.add_grade("Biology", 70)
s5.add_grade("Biology", 69)
gradebook.add_student(s5)

s6 = Student("Rachael")
s6.add_grade("Chemistry", 83)
s6.add_grade("Chemistry", 79)
s6.add_grade("Chemistry", 90)
s6.add_grade("Physics", 56)
s6.add_grade("Physics", 78)
s6.add_grade("Physics", 60)
s6.add_grade("English", 60)
s6.add_grade("English", 88)
s6.add_grade("English", 78)
s6.add_grade("Biology", 64)
s6.add_grade("Biology", 77)
s6.add_grade("Biology", 68)
gradebook.add_student(s6)

while True:
    print("\n-----GRADEBOOK MENU-----")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Remove Student")
    print("4. Display All Students")
    print("5. Sort by Average")
    print("6. Sort by Subject")
    print("7. Total Students")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        try:
            name = input("Enter Student Name: ").title()
            if gradebook.search_student(name):
                print("A student with that name already exists.")
                continue

            student = Student(name)
            subjects = [
                "Chemistry",
                "Physics",
                "English",
                "Biology"
            ]

            for subject in subjects:
                print(f"\nEnter grades for {subject}")

                for i in range(3):
                    while True:
                        try:
                            grade = float(
                                input(
                                    f"{subject} Grade {i+1}: "
                                )
                            )

                            if 0 <= grade <= 100:

                                student.add_grade(
                                    subject,
                                    grade
                                )
                                break

                            else:
                                print(
                                    "Grade must be between 0 and 100."
                                )

                        except ValueError:
                            print(
                                "Invalid input. Enter a number."
                            )

            gradebook.add_student(student)

        except Exception as e:
            print("Error:", e)

    elif choice == "2":
        name = input("Enter Student Name: ")
        student = gradebook.search_student(name)

        if student:
            student.display_details()
        else:
            print("Student not found.")

    elif choice == "3":
        name = input("Enter Student Name: ")
        gradebook.remove_student(name)

    elif choice == "4":
        gradebook.display_all_students()

    elif choice == "5":
        gradebook.sort_by_average()

    elif choice == "6":
        subject = input(
            "Enter Subject (Chemistry, Physics, English, Biology): "
        )
        gradebook.sort_by_subject(subject)

    elif choice == "7":
        print(
            f"Total Students: {gradebook.total_students()}"
        )

    elif choice == "8":
        print("Program Ended.")
        break
    else:
        print("Invalid Choice.")