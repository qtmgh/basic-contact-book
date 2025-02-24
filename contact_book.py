contacts = [] 

def add_contact(): 
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
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
    with open("contacts.txt", "w") as file: 
        for contact in contacts:
            file.write(f"{contact['name']}, {contact['phone']}, {contact['email']}\n")
            print("Contacts saved to file.")

def load_contacts(): 
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts.append({"name": name, "phone": phone, "email": email})
                print("Contacts loaded from file.")
    except FileNotFoundError:
        print("No contacts file found.")

def main(): 
    while True:
        print("\n=== Contact Book ====")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Save Contacts")
        print("5. Load Contacts")
        print("6. Exit")
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
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()