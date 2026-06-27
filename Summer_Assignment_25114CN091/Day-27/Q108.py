"""
Marksheet Generation System
Author: Your Name
Description:
    This program takes student details and marks in subjects,
    calculates total, percentage, and assigns grades.
    It includes input validation and handles edge cases.
"""

# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

# Function to validate marks input
def get_valid_marks(subject_name):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject_name} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print(" Marks must be between 0 and 100. Try again.")
        except ValueError:
            print(" Invalid input. Please enter a numeric value.")

# Main function
def main():
    print("="*40)
    print("       MARKSHEET GENERATION SYSTEM")
    print("="*40)

    # Student details
    student_name = input("Enter Student Name: ").strip()
    roll_number = input("Enter Roll Number: ").strip()

    # Number of subjects
    while True:
        try:
            num_subjects = int(input("Enter number of subjects: "))
            if num_subjects > 0:
                break
            else:
                print(" Number of subjects must be greater than 0.")
        except ValueError:
            print(" Invalid input. Please enter an integer.")

    subjects = {}
    for i in range(num_subjects):
        subject_name = input(f"Enter name of subject {i+1}: ").strip()
        subjects[subject_name] = get_valid_marks(subject_name)

    # Calculations
    total_marks = sum(subjects.values())
    percentage = total_marks / num_subjects
    grade = calculate_grade(percentage)

    # Display Marksheet
    print("\n" + "="*40)
    print("              MARKSHEET")
    print("="*40)
    print(f"Name       : {student_name}")
    print(f"Roll No.   : {roll_number}")
    print("-"*40)
    print(f"{'Subject':20} {'Marks':>10}")
    print("-"*40)
    for subject, marks in subjects.items():
        print(f"{subject:20} {marks:>10.2f}")
    print("-"*40)
    print(f"{'Total':20} {total_marks:>10.2f}")
    print(f"{'Percentage':20} {percentage:>9.2f}%")
    print(f"{'Grade':20} {grade:>10}")
    print("="*40)

# Run the program
if __name__ == "__main__":
    main()
