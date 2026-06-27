class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

    def __str__(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Course: {self.course}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, course):
        self.students.append(Student(roll_no, name, course))
        print(" Student record added successfully.")

    def display_students(self):
        if not self.students:
            print(" No student records found.")
        for student in self.students:
            print(student)


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.add_student(101, "Aman Sharma", "B.Tech")
    sms.add_student(102, "Varsha Sharma", "MBBS")
    sms.display_students()
