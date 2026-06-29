def string_operations():
    s = ""
    while True:
        print("\n--- String Operations Menu ---")
        print("1. Input New String")
        print("2. Reverse String")
        print("3. Convert to Uppercase")
        print("4. Convert to Lowercase")
        print("5. Count Vowels")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '6':
            print("Exiting String Operations. Goodbye!")
            break

        if choice == '1':
            s = input("Enter new string: ")
        elif choice == '2':
            print("Reversed String:", s[::-1])
        elif choice == '3':
            print("Uppercase:", s.upper())
        elif choice == '4':
            print("Lowercase:", s.lower())
        elif choice == '5':
            vowels = "aeiouAEIOU"
            count = sum(1 for ch in s if ch in vowels)
            print(f"Vowel Count: {count}")
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    string_operations()
