import os

# File to store contacts
CONTACTS_FILE = "contacts.txt"

# Function to load contacts from file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return {}
    
    contacts = {}
    with open(CONTACTS_FILE, 'r') as f:
        for line in f:
            name, details = line.strip().split(":")
            contacts[name] = details
    return contacts

# Function to save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        for name, details in contacts.items():
            f.write(f"{name}:{details}\n")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the name of the contact: ")
    details = input("Enter the details (phone number, email, etc.): ")
    contacts[name] = details
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, details in contacts.items():
            print(f"Name: {name}, Details: {details}")

# Function to search for a contact
def search_contact(contacts):
    name = input("Enter the name to search for: ")
    if name in contacts:
        print(f"Name: {name}, Details: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

# Main function to run the contact book application
def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Delete a contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()