# Step 1: Initialize the Phonebook
phonebook = {}

# Step 2: Display menu options and handle user input
def display_menu():
    print("\nPhonebook Application")
    print("1. Add New Contact")
    print("2. Search for a Contact")
    print("3. Delete a Contact")
    print("4. List All Contacts")
    print("5. Exit")

def add_contact():
    name = input("Enter contact name: ")
    if name in phonebook:
        print("Contact already exists.")
    else:
        phone = input("Enter phone number: ")
        phonebook[name] = phone
        print(f"Contact {name} added successfully.")

def search_contact():
    name = input("Enter contact name to search: ")
    if name in phonebook:
        print(f"{name}'s phone number is: {phonebook[name]}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

def list_contacts():
    if phonebook:
        print("\nPhonebook Contacts:")
        for name, phone in phonebook.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts available.")

# Main program loop
while True:
    display_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        list_contacts()
    elif choice == '5':
        print("Exiting Phonebook Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")