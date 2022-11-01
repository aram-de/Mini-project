students = ["Faaruq", "Aram"]
subjects = ["Maths", "English"]


def show_students(students, subjects):
    for student in students:
        print(student)
    menu(students, subjects)

def show_subjects(students, subjects):
    for subject in subjects:
        print(subject)
    menu(students, subjects)

def delete_students(students):
    students.clear()
    print("Deleted all students")
    menu(students, subjects)

def add_student(students):
    student = input("Enter a student name")
    students.append(student)
    menu(students, subjects)

def menu(students, subject):
    print("Enter 1 to see student list, 2 to delete the student list or 3 to add a student")
    choice = input("Enter 4 to see subject list, 2 to delete the subject list or 3 to add a subject")

    if choice == "1":
        show_students(students, subjects)
    elif choice == "2":
        delete_students(students, subjects)
    elif choice == "3":
        add_student(students, subjects)
    if choice == "4":
        show_subjects(students, subjects)
    # elif choice == "5":
    #     delete_subjects(students, subjects)
    # elif choice == "6":
    #     add_subject(students, subjects)

menu(students, subjects)