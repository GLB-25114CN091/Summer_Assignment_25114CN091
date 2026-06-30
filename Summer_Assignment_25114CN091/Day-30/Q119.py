employees = []

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
        print("No employees found.")
        return
    print("\n--- Employee Records ---")
    for e in employees:
        print(f"Name: {e['name']}, ID: {e['id']}, Dept: {e['dept']}")

def search_employee():
    emp_id = input("Enter employee ID to search: ").strip()
    for e in employees:
        if e['id'] == emp_id:
            print(f" Found: Name: {e['name']}, Dept: {e['dept']}")
            return
    print(" Employee not found.")

def delete_employee():
    emp_id = input("Enter employee ID to delete: ").strip()
    for e in employees:
        if e['id'] == emp_id:
            employees.remove(e)
            print("✅ Employee deleted.")
            return
    print(" Employee not found.")

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ").strip()
    if choice == '1':
        add_employee()
    elif choice == '2':
        display_employees()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        break
    else:
        print(" Invalid choice!")
