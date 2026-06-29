def array_operations():
    arr = []
    while True:
        print("\n--- Array Operations Menu ---")
        print("1. Insert Element")
        print("2. Delete Element")
        print("3. Search Element")
        print("4. Display Array")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '5':
            print("Exiting Array Operations. Goodbye!")
            break

        if choice == '1':
            try:
                val = int(input("Enter element to insert: "))
                arr.append(val)
                print(f"{val} inserted.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice == '2':
            try:
                val = int(input("Enter element to delete: "))
                if val in arr:
                    arr.remove(val)
                    print(f"{val} deleted.")
                else:
                    print("Element not found.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice == '3':
            try:
                val = int(input("Enter element to search: "))
                if val in arr:
                    print(f"{val} found at index {arr.index(val)}.")
                else:
                    print("Element not found.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice == '4':
            print("Array:", arr)

        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    array_operations()
