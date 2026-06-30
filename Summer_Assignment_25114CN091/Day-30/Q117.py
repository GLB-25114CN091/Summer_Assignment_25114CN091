# List to store student records
students = []

def add_student():
    """Add a new student record."""
    name = input("Enter student name: ").strip()
    roll = input("Enter roll number: ").strip()
    course = input("Enter course name: ").strip()

    # Check for duplicate roll number
    for s in students:
        if s['roll'] == roll:
            print(" Roll number already exists!")
            return

    students.append({"name": name, "roll": roll, "course": course})
    print(" Student added successfully!")

def display_students():
    """Display all student records."""
    if not students:
        print("No records found.")
        return
    print("\n--- Student Records ---")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Course: {s['course']}")

def search_student():
    """Search student by roll number."""
    roll = input("Enter roll number to search: ").strip()
    for s in students:
        if s['roll'] == roll:
            print(f" Found: Name: {s['name']}, Course: {s['course']}")
            return
    print(" Student not found.")

def delete_student():
    """Delete student by roll number."""
    roll = input("Enter roll number to delete: ").strip()
    for s in students:
        if s['roll'] == roll:
            students.remove(s)
            print(" Student deleted.")
            return
    print(" Student not found.")

# Menu-driven program
while True:
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ").strip()
    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print(" Invalid choice! Please try again.")
