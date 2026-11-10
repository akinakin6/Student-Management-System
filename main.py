
import json

# Load existing student records
def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save student records
def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


students = load_students()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    
    if choice == 1:

        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        roll = int(input("Enter roll number: "))
        course = input("Enter course: ")

        duplicate = False

        for student in students:
            if student["roll"] == roll:
                duplicate = True
                break

        if duplicate:
            print("Roll number already exists!")

        else:
            student = {
                "name": name,
                "age": age,
                "roll": roll,
                "course": course
            }

            students.append(student)
            save_students()

            print("Student added successfully!")

    elif choice == 2:

        if len(students) == 0:
            print("No students found!")

        else:
            for student in students:
                print("\nStudent Details:")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Roll:", student["roll"])
                print("Course:", student["course"])

    elif choice == 3:

        search_roll = int(input("Enter roll number: "))
        found = False

        for student in students:

            if student["roll"] == search_roll:

                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Roll:", student["roll"])
                print("Course:", student["course"])

                found = True
                break

        if not found:
            print("Student not found!")

    elif choice == 4:

        update_roll = int(input("Enter roll number to update: "))
        found = False

        for student in students:

            if student["roll"] == update_roll:

                student["name"] = input("Enter new name: ")
                student["age"] = int(input("Enter new age: "))
                student["course"] = input("Enter new course: ")

                save_students()

                print("Student updated successfully!")
                found = True
                break

        if not found:
            print("Student not found!")

    elif choice == 5:

        delete_roll = int(input("Enter roll number to delete: "))
        found = False

        for student in students:

            if student["roll"] == delete_roll:

                students.remove(student)
                save_students()

                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found!")

    elif choice == 6:

        print("Thank you for using our application!")
        break

    else:
        print("Invalid choice!")
