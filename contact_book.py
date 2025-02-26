import json

contacts = [] 

def add_contact(): 
    name = input("Enter name: ")
    while True:
        phone = input("Enter phone (10 digits): ")
        if phone.isdigit() and len(phone) == 10:
            break
        print("Invalid phone number. Please enter 10 digits.")
    while True:
        email = input("Enter email: ")
        if "@" in email:
            break
        print("Invalid email. Please include '@'.")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print ("Contacts:")
        for i, contact in enumerate(contacts, start = 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
        if not found:
            print("Contact not found.")

def save_contacts(): 
    with open("contacts.json", "w") as file: 
        json.dump(contacts,file)
    print("Contacts saved to file.")

def load_contacts(): 
    try:
        with open("contacts.json", "r") as file:
            global contacts
            contacts = json.load(file)
        print("Contacts loaded from file.")
    except FileNotFoundError:
        print("No contacts file found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact '{name} has been deleted.")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Current details: Phone: {contact['phone']}, Email: {contact['email']}")
            # Validate phone number
            while True:
                phone = input("Enter new phone (10 digits): ")
                if phone.isdigit() and len(phone) == 10:
                    contact["phone"] = phone
                    break
                print("Invalid phone number. Please enter 10 digits")
            # Validate email
            while True:
                email = input("Enter new email: ")
                if "@" in email:
                    contact["email"] = email
                    break
                print("Invalid email. Please include '@'.")
            print("Contact has been updated.")
            return
    print("Contact not found.")

def main(): 
    while True:
        print("\n=== Contact Book ====")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Save Contacts")
        print("5. Load Contacts")
        print("6. Delete Contact")
        print("7. Update Contact")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            save_contacts()
        elif choice == "5":
            load_contacts()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            update_contact()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()