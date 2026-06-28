class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Book '{title}' added successfully.")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return
        for idx, book in enumerate(self.books, start=1):
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{idx}. {book.title} by {book.author} - {status}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You borrowed '{book.title}'.")
                return
        print("Book not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                print(f"You returned '{book.title}'.")
                return
        print("Invalid return request.")

def library_menu():
    lib = Library()
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            lib.add_book(title, author)
        elif choice == "2":
            lib.display_books()
        elif choice == "3":
            title = input("Enter book title to borrow: ").strip()
            lib.borrow_book(title)
        elif choice == "4":
            title = input("Enter book title to return: ").strip()
            lib.return_book(title)
        elif choice == "5":
            print("Exiting Library System.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    library_menu()
