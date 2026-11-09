class StudentNotFoundError(Exception):
    pass

class InvalidGradeError(Exception):
    pass

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if grade < 0 or grade > 100:
            raise InvalidGradeError(
                "Grade must be between 0 and 100."
            )

        self.grades.append(grade)

    def average(self):
        if len(self.grades) == 0:
            return 0      # Prevent division by zero

        return sum(self.grades) / len(self.grades)

    def display(self):
        print(f"\nName: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.average():.2f}")

class GradingSystem:

    def __init__(self):
        self.students = []

    def add_student (self, name):
        name = name.strip()

        for student in self.students:
            if student.name.lower() == name.lower():
                print("Duplicate student names are not allowed.")
                return

        self.students.append(Student(name))
        print("Student added successfully.")

    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student

        raise StudentNotFoundError(
            f"Student '{name}' not found."
        )

    def add_grade(self, name):
        try:
            student = self.find_student(name)

            while True:
                try:
                    grade = float(
                        input("Enter grade (0-100): ")
                    )

                    student.add_grade(grade)
                    print("Grade added successfully.")
                    break

                except ValueError:
                    print("Error: Grade must be numeric.")

                except InvalidGradeError as e:
                    print(e)

        except StudentNotFoundError as e:
            print(e)

    def remove_student(self, name):

        student = self.find_student(name)

        self.students.remove(student)
        print("Student removed successfully.")

    def search_student(self, name):

        try:
            student = self.find_student(name)
            student.display()

        except StudentNotFoundError as e:
            print(e)

    def sort_by_name(self):

        n = len(self.students)

        for i in range(n):

            for j in range(0, n - i - 1):

                if (self.students[j].name.lower() >
                        self.students[j + 1].name.lower()):

                    self.students[j], self.students[j + 1] = \
                        self.students[j + 1], self.students[j]

        print("Students sorted by name.")

    def sort_by_average(self):

        n = len(self.students)

        for i in range(n):

            for j in range(0, n - i - 1):

                if (self.students[j].average() >
                        self.students[j + 1].average()):

                    self.students[j], self.students[j + 1] = \
                        self.students[j + 1], self.students[j]

        print("Students sorted by average grade.")

    def display_students(self):

        if len(self.students) == 0:
            print("No students available.")
            return

        for student in self.students:
            student.display()

system = GradingSystem()

while True:

    print("\n-----STUDENT GRADING SYSTEM-----")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Sort By Name")
    print("6. Sort By Average")
    print("7. Display All Students")
    print("8. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            name = input("Enter student name: ")
            system.add_student(name)

        elif choice == "2":
            name = input("Enter student name: ")
            system.add_grade(name)

        elif choice == "3":
            name = input("Enter student name: ")
            system.search_student(name)

        elif choice == "4":
            name = input("Enter student name: " )

            try:
                system.remove_student(name)

            except StudentNotFoundError as e:
                print(e)

        elif choice == "5":
            system.sort_by_name()

        elif choice == "6":
            system.sort_by_average()

        elif choice == "7":
            system.display_students()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid menu option.")

    except Exception as e:
        print("Unexpected Error:", e)