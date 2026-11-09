students = [
    ("bida25-100", "Katlo", {"Chemistry": 85, "Physics": 69, "English": 80, "Biology": 92}),
    ("bida24-136", "Bonolo", {"Chemistry": 56, "Physics": 84, "English": 75, "Biology": 43}),
    ("bida25-94", "Kabelo",  {"Chemistry": 58, "Physics": 67, "English": 84, "Biology": 94}),
    ("bida25-273", "Mighty",  {"Chemistry": 56, "Physics": 90, "English": 56, "Biology": 84}),
    ("cse25-234", "Marang",  {"Chemistry": 60, "Physics": 69, "English": 94, "Biology": 89}),
    ("bida25-032", "Rachael", {"Chemistry": 83, "Physics": 56, "English": 60, "Biology": 66})
]

for student in students:

    StudentID = student[0]
    name = student[1]
    subjects = student[2]

    average = sum(subjects.values()) / len(subjects)

    if average >= 95:
        grade = "A*"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    elif average >= 40:
        grade = "E"
    else:
        grade = "F"

    print("\n----- STUDENT_SUMMARY_REPORT -----")
    print("Student_ID:", StudentID)
    print("Student_Name:", name)
    print("Student_Marks:", subjects)
    print("Average_Mark:", round(average, 2))
    print("Final_Grade:", grade)

for subject in subjects:

        marks = []

        for student in students:
            marks.append(student[2][subject])

        highest = max(marks)
        lowest = min(marks)

        print("\nSubject:", subject)
        print("Highest Mark:", highest)
        print("Lowest Mark:", lowest)