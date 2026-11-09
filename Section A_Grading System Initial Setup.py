num_students = int(input("Enter the number of students: "))

student_names = []
student_marks = []

for i in range(num_students):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    mark = float(input("Enter mark: "))

    if mark >= 95:
        grade = "A*"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    elif mark >= 40:
        grade = "E"
    else:
        grade = "F"

    print("Name:", name)
    print("Mark:", mark)
    print("Grade:", grade)