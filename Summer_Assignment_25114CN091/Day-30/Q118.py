library = []

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    library.append({"title": title, "author": author, "available": True})
    print(" Book added successfully!")

def display_books():
    if not library:
        print("No books in library.")
        return
    print("\n--- Library Books ---")
    for idx, book in enumerate(library, start=1):
        status = "Available" if book["available"] else "Issued"
        print(f"{idx}. {book['title']} by {book['author']} - {status}")

def issue_book():
    title = input("Enter book title to issue: ").strip()
    for book in library:
        if book["title"].lower() == title.lower() and book["available"]:
            book["available"] = False
            print(" Book issued successfully!")
            return
    print(" Book not available.")

def return_book():
    title = input("Enter book title to return: ").strip()
    for book in library:
        if book["title"].lower() == title.lower() and not book["available"]:
            book["available"] = True
            print("✅ Book returned successfully!")
            return
    print(" Book not found or already available.")

while True:
    print("\n--- Mini Library System ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ").strip()
    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        issue_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        break
    else:
        print(" Invalid choice!")
