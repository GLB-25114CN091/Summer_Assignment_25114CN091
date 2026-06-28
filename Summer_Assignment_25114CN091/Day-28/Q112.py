class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        # Prevent duplicate phone numbers
        for c in self.contacts:
            if c.phone == phone:
                print("Contact with this phone number already exists.")
                return
        self.contacts.append(Contact(name, phone))
        print(f"Contact '{name}' added successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\n--- Contact List ---")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, keyword):
        found = [c for c in self.contacts if keyword.lower() in c.name.lower() or keyword in c.phone]
        if not found:
            print("No matching contacts found.")
            return
        print("\n--- Search Results ---")
        for c in found:
            print(f"{c.name} - {c.phone}")

    def delete_contact(self, phone):
        for c in self.contacts:
            if c.phone == phone:
                self.contacts.remove(c)
                print(f"Contact '{c.name}' deleted successfully.")
                return
        print("Contact not found.")

def contact_menu():
    manager = ContactManager()

    while True:
        print("\n--- Contact Management Menu ---")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            if not phone.isdigit():
                print("Phone number must be numeric.")
                continue
            manager.add_contact(name, phone)
        elif choice == "2":
            manager.display_contacts()
        elif choice == "3":
            keyword = input("Enter name or phone to search: ").strip()
            manager.search_contact(keyword)
        elif choice == "4":
            phone = input("Enter phone number to delete: ").strip()
            manager.delete_contact(phone)
        elif choice == "5":
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    contact_menu()
