class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}")

def bank_menu():
    name = input("Enter account holder name: ").strip()
    account = BankAccount(name)

    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            try:
                amt = float(input("Enter deposit amount: "))
                account.deposit(amt)
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            try:
                amt = float(input("Enter withdrawal amount: "))
                account.withdraw(amt)
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            print("Exiting Bank System.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    bank_menu()
