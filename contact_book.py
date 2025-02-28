import json
import csv

contacts = {
    "Family": [], 
    "Friends": [],
    "Work": []
} 

def add_contact():
    group = input("Enter group (Family, Friends, Work): ")
    if group not in contacts:
        print("Invalid group.")
        return
    
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
        
    contacts[group].append({"name": name, "phone": phone, "email": email})
    print("Contact added!")

def view_contacts():
    found = False  # To track if we have any contacts

    print("Contacts:")
    for group, contact_list in contacts.items():  # Iterate over each group and its list
        if contact_list:  # Only print if the group has contacts
            print(f"\n{group} Contacts:")
            for i, contact in enumerate(contact_list, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
                found = True
    
    if not found:
        print("No contacts found.")



def search_contact():
    name = input("Enter name to search: ")
    found = False
    for group, contact_list, in contacts.items(): # Iterate through groups
        for contact in contact_list: # Iterate through contacts in each group
            if contact["name"].lower() == name.lower():
                print(f"\nGroup: {group}")
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
    except json.JSONDecodeError:
        print("Error: File is corrupted or not in JSON format.")

def export_contacts(): 
    with open("contacts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Header Row
        writer.writerow(["Group","Name", "Phone", "Email"])
        # Iterate through groups and contacts
        for group, contact_list in contacts.items(): 
            for contact in contact_list:  
                # Write a row for each contact, including group
                writer.writerow([group, contact["name"], contact["phone"], contact["email"]])
    print("Contacts exported to CSV file.")

def import_contacts():
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            next(reader) # Skip header row
            for row in reader:
                group, name, phone, email = row
                # Check if group exists
                if group not in contacts:
                    contacts[group] = []

                # Check if contact already exists
                if any(contact["name"] == name and contact["phone"] == phone and contact["email"] == email for contact in contacts[group]):
                    print(f"Duplicate contact found: {name} ({phone}, {email}) - Skipping.")
                    continue  # Skip adding duplicate

                
                contacts[group].append({"group": row[0], "name": row[1], "phone": row[2], "email": row[3]})
        print("Contacts imported from CSV.")
    
    except FileNotFoundError:
        print("No CSV file found.")

def delete_contact():
    group = input("Enter the group (Family, Friends, Work): ")
    if group not in contacts:
        print("Group not found.")
        return

    name = input("Enter the name of the contact to delete: ")
    
    for contact in contacts[group]:
        if contact["name"].lower() == name.lower():
            contacts[group].remove(contact)
            print(f"Contact '{name}' has been deleted from {group}.")
            return
        

    print("Contact not found.")

def update_contact():
    group = input("Enter the group (Family, Friends, Work): ")
    if group not in contacts:
        print("Group not found.")
        return

    name = input("Enter the name of the contact to update: ")

    for contact in contacts[group]:
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

            print(f"Contact '{name}' in {group} has been updated.")
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
        print("6. Export Contacts")
        print("7. Import Contacts")
        print("8. Delete Contact")
        print("9. Update Contact")
        print("10. Exit")
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
            export_contacts()
        elif choice == "7": 
            import_contacts()
        elif choice == "8":
            delete_contact()
        elif choice == "9":
            update_contact()
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()