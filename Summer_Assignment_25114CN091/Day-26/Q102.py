def voting_eligibility():
    print(" Voting Eligibility Checker ")
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
        elif age >= 18:
            print("✅ You are eligible to vote.")
        else:
            print(f"❌ You are not eligible to vote. Wait {18 - age} more years.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")

if __name__ == "__main__":
    voting_eligibility()
