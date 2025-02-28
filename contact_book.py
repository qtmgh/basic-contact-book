import json
import csv
import sqlite3

contacts = {
    "Family": [], 
    "Friends": [],
    "Work": []
} 

def initialize_db(): 
    # Connect to the database (creates one if it doesn't exist)
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    # Create the contacts table
    cursor.execute("""CREATE TABLE IF NOT EXISTS contacts (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   contact_group TEXT NOT NULL,
                   name TEXT NOT NULL,
                   phone TEXT NOT NULL,
                   email TEXT NOT NULL)
                   """)
    # Commit changes and close connection
    conn.commit()
    conn.close()
# Call this function once to initalize database
initialize_db()

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
        
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO contacts (contact_group, name, phone, email) 
                   VALUES (?, ?, ?, ?)""", (group, name, phone, email))
    conn.commit()
    conn.close()
    print("Contact added!")

def view_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute("SELECT contact_group, name, phone, email FROM contacts")
    rows = cursor.fetchall()

    if not rows:
        print("No contacts found.")
    else:
        print("Contacts: ")
        for row in rows:
            group, name, phone, email = row
            print(f"Group: {group}, Name: {name}, Phone: {phone}, Email: {email}")
    # Close the connection
    conn.close()

def search_contact():
    name = input("Enter name to search: ")
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    # Search for contacts by name
    cursor.execute(""" SELECT contact_group, name, phone, email FROM contacts
                   WHERE name LIKE ?
                   """, (f"%{name}%",))
    rows = cursor.fetchall()
    if not rows:
        print("No contacts found.")
    else:
        print("Matching contacts: ")
        for row in rows:
            group, name, phone, email = row
            print(f"Group: {group}, Name: {name}, Phone: {phone}, Email: {email}")
    # Close the connection
    conn.close()

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
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    # Fetch all contacts
    cursor.execute("SELECT contact_group, name, phone, email FROM contacts")
    rows = cursor.fetchall()

    # Write to CSV
    with open("contacts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Group", "Name", "Phone", "Email"]) # Write header
        writer.writerows(rows) # Write rows
    
    # Close the connection
    conn.close()
    print("Contacts exported to CSV")

def import_contacts():
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            conn = sqlite3.connect("contacts.db")
            cursor = conn.cursor()
            
            for row in reader:
                group, name, phone, email = row
                cursor.execute("""
                    INSERT INTO contacts (contact_group, name, phone, email)
                    VALUES (?, ?, ?, ?)
                """, (group, name, phone, email))
            
            # Commit changes and close the connection
            conn.commit()
            conn.close()
            print("Contacts imported from CSV.")
    except FileNotFoundError:
        print("No CSV file found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    # Delete contact using name
    cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))

    # Check affected rows (if any)
    if cursor.rowcount > 0:
        print(f"Contact '{name}' deleted successfully.")
    else: 
        print("Contact not found.")

    # Commit changes and close connection
    conn.commit()
    conn.close()

def update_contact():
    name = input("Enter the name of the contact to update: ")
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    # Fetch current contact details
    cursor.execute("SELECT contact_group, name, phone, email FROM contacts WHERE name = ?", (name,))
    row = cursor.fetchone()

    if not row: 
        print("Contact not found.")
        conn.close()
        return
    
    group, name, phone, email = row
    print(f"Current details: Group: {group}, Name: {name}, Phone: {phone}, Email: {email}")

    # Get new details
    new_phone = input("Enter new phone (10 digits): ")
    while not (new_phone.isdigit() and len(new_phone) == 10):
        print("Invalid phone number. Please enter 10 digits: ")
        new_phone = input("Enter new phone (10 digits): ")
    
    new_email = input("Enter new email: ")
    while '@' not in new_email:
        print("Invalid email. Please include '@'.")
        new_email = input("Enter new email: ")

    # Update the contact
    cursor.execute(""" UPDATE contacts
                   SET phone = ?, email = ?
                   WHERE name = ?
                   """, (new_phone, new_email, name))
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print(f"Contact '{name}' updated successfully.")

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