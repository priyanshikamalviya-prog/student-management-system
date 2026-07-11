
from database import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    close_connection
)

print("=" * 40)
print("     STUDENT MANAGEMENT SYSTEM")
print("Learning Git")
print("=" * 40)

while True:

    print("\nChoose an Option")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # =========================
    # ADD STUDENT
    # =========================
    if choice == "1":

        print("\nADD NEW STUDENT")

        while True:
            student_id = input("Enter Student ID: ").strip()

            if student_id == "":
                print("Student ID cannot be empty.")
            else:
                break

        while True:
            name = input("Enter Student Name: ").strip()

            if name == "":
                print("Name cannot be empty.")
            else:
                break

        while True:
            age = input("Enter Age: ")

            if age.isdigit():

                age = int(age)

                if 1 <= age <= 120:
                    break
                else:
                    print("Age must be between 1 and 120.")

            else:
                print("Age must be a number.")

        while True:
            course = input("Enter Course: ").strip()

            if course == "":
                print("Course cannot be empty.")
            else:
                break

        while True:
            email = input("Enter Email: ").strip()

            if "@" in email and "." in email:
                break
            else:
                print("Invalid Email.")

        add_student(
            student_id,
            name,
            age,
            course,
            email
        )

    # =========================
    # VIEW STUDENTS
    # =========================
    elif choice == "2":

        view_students()

    # =========================
    # SEARCH STUDENT
    # =========================
    elif choice == "3":

        search_id = input("Enter Student ID to Search: ")

        search_student(search_id)

    # =========================
    # UPDATE STUDENT
    # =========================
    elif choice == "4":

        update_id = input("Enter Student ID to Update: ")

        print("\nEnter New Details")

        name = input("Enter New Name: ")

        while True:
            age = input("Enter New Age: ")

            if age.isdigit():
                age = int(age)
                break
            else:
                print("Age must be a number.")

        course = input("Enter New Course: ")
        email = input("Enter New Email: ")

        update_student(
            update_id,
            name,
            age,
            course,
            email
        )

    # =========================
    # DELETE STUDENT
    # =========================
    elif choice == "5":

        delete_id = input("Enter Student ID to Delete: ")

        delete_student(delete_id)

    # =========================
    # EXIT
    # =========================
    elif choice == "6":

        close_connection()

        print("\nThank you for using Student Management System.")
        break

    # =========================
    # INVALID CHOICE
    # =========================
    else:

        print("Invalid Choice! Please enter a number between 1 and 6.")