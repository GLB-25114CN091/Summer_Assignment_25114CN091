class TicketBooking:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_ticket(self, seats):
        if seats <= 0:
            print("Invalid seat count.")
            return
        if self.booked_seats + seats > self.total_seats:
            print("Not enough seats available.")
            return
        self.booked_seats += seats
        print(f"Booked {seats} seat(s). Remaining: {self.total_seats - self.booked_seats}")

    def cancel_ticket(self, seats):
        if seats <= 0 or seats > self.booked_seats:
            print("Invalid cancellation request.")
            return
        self.booked_seats -= seats
        print(f"Cancelled {seats} seat(s). Remaining: {self.total_seats - self.booked_seats}")

    def display_status(self):
        print(f"Total Seats: {self.total_seats}, Booked: {self.booked_seats}, Available: {self.total_seats - self.booked_seats}")

def ticket_menu():
    try:
        total = int(input("Enter total seats: "))
        booking = TicketBooking(total)
    except ValueError:
        print("Invalid number of seats.")
        return

    while True:
        print("\n--- Ticket Menu ---")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. View Status")
        print("4. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            try:
                seats = int(input("Enter seats to book: "))
                booking.book_ticket(seats)
            except ValueError:
                print("Invalid input.")
        elif choice == "2":
            try:
                seats = int(input("Enter seats to cancel: "))
                booking.cancel_ticket(seats)
            except ValueError:
                print("Invalid input.")
        elif choice == "3":
            booking.display_status()
        elif choice == "4":
            print("Exiting Ticket System.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    ticket_menu()
