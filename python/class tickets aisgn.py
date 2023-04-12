class Ticket:
    counter = 0
    tickets = []

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.counter + 2001
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.counter += 1
        Ticket.tickets.append(self)
    def resolve_ticket_pass_change(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.response = f"New password: {new_password}"
            print(self.response)
            self.status = "Closed"


    def resolve_ticket(self):
        self.status = "Closed"

    def reopen_ticket(self):
        self.status = "Open"


    @staticmethod
    def print_tickets():
        for ticket in Ticket.tickets:
            print(f"Ticket Number: {ticket.ticket_number}")
            print(f"Ticket Creator: {ticket.creator_name}")
            print(f"Staff ID: {ticket.staff_id}")
            print(f"Email Address: {ticket.contact_email}")
            print(f"Description: {ticket.description}")
            print(f"Response: {ticket.response}")
            print(f"Ticket Status: {ticket.status}")
            print()

    @staticmethod
    def ticket_stats():
        total_tickets = len(Ticket.tickets)
        resolved_tickets = sum(1 for ticket in Ticket.tickets if ticket.status == "Closed")
        open_tickets = sum(1 for ticket in Ticket.tickets if ticket.status == "Open")
        return total_tickets, resolved_tickets, open_tickets


# Example usage
# Creating tickets
ticket1 = Ticket("1001", "Frank", "Frank@gmail.com", "My computer is not turning on")
ticket2 = Ticket("1002", "Ben", "Ben@hotmail.com", "I forgot my password")
ticket3 = Ticket("1003", "Elise", "Elise@live.com", "I need access to a shared folder")

# Resolving ticket1
ticket1.resolve_ticket()

# Reopening ticket2
ticket2.reopen_ticket()

# Displaying ticket information
Ticket.print_tickets()

# Displaying ticket statistics
total_tickets, resolved_tickets, open_tickets = Ticket.ticket_stats()
print("Displaying Ticket Statistics")
print(f"Tickets Created: {total_tickets}")
print(f"Tickets Resolved: {resolved_tickets}")
print(f"Tickets To Solve: {open_tickets}")


while True:
    print("1. Create a new ticket")
    print("2. Resolve a ticket")
    print("3. Reopen a ticket")
    print("4. Print all tickets")
    print("5. Print ticket statistics")
    print("6. Exit")
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        staff_id = input("Enter staff ID: ")
        creator_name = input("Enter creator name: ")
        contact_email = input("Enter contact email: ")
        description = input("Enter description: ")
        ticket = Ticket(staff_id, creator_name, contact_email, description)
        ticket.resolve_ticket_pass_change()
        print("Ticket created successfully!")
    elif choice == '2':
        ticket_number = int(input("Enter ticket number to resolve: "))
        for ticket in Ticket.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.resolve_ticket()
                print("Ticket resolved successfully!")
                break
        else:
            print("Ticket not found.")
    elif choice == '3':
        ticket_number = int(input("Enter ticket number to reopen: "))
        for ticket in Ticket.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.reopen_ticket()
                print("Ticket reopened successfully!")
                break
        else:
            print("Ticket not found.")
    elif choice == '4':
        Ticket.print_tickets()
    elif choice == '5':
        total_tickets, resolved_tickets, open_tickets = Ticket.ticket_stats()
        print("Displaying Ticket Statistics")
        print(f"Tickets Created: {total_tickets}")
        print(f"Tickets Resolved: {resolved_tickets}")
        print(f"Tickets To Solve: {open_tickets}")
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")