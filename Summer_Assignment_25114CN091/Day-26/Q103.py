def atm_simulation():
    print(" ATM Simulation ")
    balance = 500000  # Initial balance
    pin = "1234"      # Default PIN

    entered_pin = input("Enter your ATM PIN: ")
    if entered_pin != pin:
        print("❌ Incorrect PIN. Access denied.")
        return

    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"💰 Current Balance: ₹{balance:.2f}")
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: ₹"))
                if amount <= 0:
                    print("Deposit amount must be positive.")
                else:
                    balance += amount
                    print(f"✅ ₹{amount:.2f} deposited successfully.")
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: ₹"))
                if amount <= 0:
                    print("Withdrawal amount must be positive.")
                elif amount > balance:
                    print("❌ Insufficient balance.")
                else:
                    balance -= amount
                    print(f"✅ ₹{amount:.2f} withdrawn successfully.")
            except ValueError:
                print("Invalid amount.")
        elif choice == "4":
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm_simulation()
