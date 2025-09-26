# Student Course Registration System
students = {
    "Student1": {"name": "Cynthia", "courses": ["English", "Math"]},
    "Student2": {"name": "Ann", "courses": ["Science", "Technology"]},
    "Student3": {"name": "Louis", "courses": []}
}

print("Welcome to Student Course Registration System")

while True:
    print("\nMenu:")
    print("1. Register Student")
    print("2. Add Course")
    print("3. View Courses")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    match choice:
        case "1":
            # Register Student
            studentId = input("Enter Student ID: ").strip()
            if studentId in students:
                print("Student is registered.")
            else:
                name = input("Enter Student Name: ").strip()
                students[studentId] = {"name": name, "courses": []}
                print(f"Student {name} registered successfully!")

        case "2":
            # Add Course
            studentId = input("Enter Student ID: ").strip()
            if studentId in students:
                course = input("Enter Course Name: ").strip()
                students[studentId]["courses"].append(course)
                print(f"Course '{course}' added for {students[studentId]['name']}")
            else:
                print("Student ID not found. Please register first.")

        case "3":
            # View Courses
            studentId = input("Enter Student ID: ").strip()
            if studentId in students:
                name = students[studentId]["name"]
                courses = students[studentId]["courses"]
                print(f"\n{name}'s Registered Courses:")
                if courses:
                    for c in courses:
                        print(f"- {c}")
                else:
                    print("No courses registered yet.")
            else:
                print("Student ID is not found.")

        case "4":
            print("End Closed. Goodbye!")
            break

        case _:
            print("Invalid choice. Please enter 1-4.")