class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}"


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, department):
        self.employees.append(Employee(emp_id, name, department))
        print(" Employee record added successfully.")

    def display_employees(self):
        if not self.employees:
            print(" No employee records found.")
        for emp in self.employees:
            print(emp)


if __name__ == "__main__":
    ems = EmployeeManagementSystem()
    ems.add_employee(201, "Shivank Singh", "IT")
    ems.add_employee(202, "Surbhi Gupta", "HR")
    ems.display_employees()
