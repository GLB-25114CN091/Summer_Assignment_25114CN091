class SalaryRecord:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_net_salary(self):
        hra = 0.20 * self.basic_salary
        da = 0.10 * self.basic_salary
        deductions = 0.05 * self.basic_salary
        return self.basic_salary + hra + da - deductions

    def __str__(self):
        return (f"ID: {self.emp_id}, Name: {self.name}, "
                f"Net Salary: ₹{self.calculate_net_salary():.2f}")


class SalaryManagementSystem:
    def __init__(self):
        self.salary_records = []

    def add_salary_record(self, emp_id, name, basic_salary):
        self.salary_records.append(SalaryRecord(emp_id, name, basic_salary))
        print(" Salary record added successfully.")

    def display_salaries(self):
        if not self.salary_records:
            print(" No salary records found.")
        for record in self.salary_records:
            print(record)


if __name__ == "__main__":
    sms = SalaryManagementSystem()
    sms.add_salary_record(301, "Aakash Singh", 500000)
    sms.add_salary_record(302, "Prince Yadav", 100000)
    sms.display_salaries()
