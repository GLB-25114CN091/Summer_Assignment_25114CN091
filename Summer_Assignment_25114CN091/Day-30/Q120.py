# Data storage
students = []
library = []
employees = []

#  STUDENT FUNCTIONS 
def add_student():
    name = input("Enter student name: ").strip()
    roll = input("Enter roll number: ").strip()
    for s in students:
        if s['roll'] == roll:
            print(" Roll number already exists!")
            return
    students.append({"name": name, "roll": roll})
    print(" Student added successfully!")

def display_students():
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}")

# LIBRARY FUNCTIONS 
def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    library.append({"title": title, "author": author, "available": True})
    print(" Book added successfully!")

def display_books():
    if not library:
        print("No books in library.")
        return
    print("\n--- Library Books ---")
    for idx, book in enumerate(library, start=1):
        status = "Available" if book["available"] else "Issued"
        print(f"{idx}. {book['title']} by {book['author']} - {status}")

def issue_book():
    title = input("Enter book title to issue: ").strip()
    for book in library:
        if book["title"].lower() == title.lower() and book["available"]:
            book["available"] = False
            print(" Book issued successfully!")
            return
    print(" Book not available.")

def return_book():
    title = input("Enter book title to return: ").strip()
    for book in library:
        if book["title"].lower() == title.lower() and not book["available"]:
            book["available"] = True
            print(" Book returned successfully!")
            return
    print(" Book not found or already available.")

#  EMPLOYEE FUNCTIONS 
def add_employee():
    name = input("Enter employee name: ").strip()
    emp_id = input("Enter employee ID: ").strip()
    dept = input("Enter department: ").strip()
    for e in employees:
        if e['id'] == emp_id:
            print(" Employee ID already exists!")
            return
    employees.append({"name": name, "id": emp_id, "dept": dept})
    print(" Employee added successfully!")

def display_employees():
    if not employees:
        print("No employee records found.")
        return
    print("\n--- Employee Records ---")
    for e in employees:
        print(f"Name: {e['name']}, ID: {e['id']}, Dept: {e['dept']}")

#   MAIN FUNCTION
def student_menu():
    while True:
        print("\n--- Student Menu ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Back to Main Menu")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            break
        else:
            print(" Invalid choice!")

def library_menu():
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Back to Main Menu")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            add_book()
        elif choice == '2':
            display_books()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            break
        else:
            print(" Invalid choice!")

def employee_menu():
    while True:
        print("\n--- Employee Menu ---")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Back to Main Menu")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            break
        else:
            print(" Invalid choice!")

#  PROGRAM START 
while True:
    print("\n=== Complete Mini Project ===")
    print("1. Student Management")
    print("2. Library Management")
    print("3. Employee Management")
    print("4. Exit")
    main_choice = input("Enter choice: ").strip()

    if main_choice == '1':
        student_menu()
    elif main_choice == '2':
        library_menu()
    elif main_choice == '3':
        employee_menu()
    elif main_choice == '4':
        print("Exiting program... ")
        break
    else:
        print(" Invalid choice! Please try again.")