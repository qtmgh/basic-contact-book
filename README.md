# Contact Book Application

![Python](https://img.shields.io/badge/Python-3.x-blue) ![GitHub](https://img.shields.io/github/license/your-username/contact-book)

A simple **Contact Book Application** built with Python. This program allows users to manage their contacts by adding, viewing, searching, updating, and deleting contacts. Contacts can also be saved to and loaded from a file.

---

## **Features**
- **Add Contact**: Add a new contact with a name, phone number, and email.
- **View Contacts**: Display all saved contacts in a user-friendly format.
- **Search Contact**: Search for a contact by name.
- **Update Contact**: Update the phone number or email of an existing contact.
- **Delete Contact**: Remove a contact from the contact book.
- **Save Contacts**: Save all contacts to a file (`contacts.txt` or `contacts.json`).
- **Load Contacts**: Load contacts from a file.

---

## **Getting Started**

### **Prerequisites**
- Python 3.x installed on your system.
- Basic knowledge of running Python scripts.

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/contact-book.git
2. Navitate to the project directory: 
    cd contact-book

### **Running the Application**
1. Run the Python script: 
    python3 contact_book.py
2. Follow the on-screen menu to manage your contacts. 

### **Usage**

**Main Menu**

=== Contact Book ===
1. Add Contact
2. View Contacts
3. Search Contact
4. Save Contacts
5. Load Contacts
6. Delete Contact
7. Update Contact
8. Exit

<details> <summary><strong>Examples (Click to Expand)</strong></summary>

1. **Add a contact:**

    Enter name: Alice
    Enter phone (10 digits): 1234567890
    Enter email: alice@example.com
    Contact added!

2. **View Contacts:**
    
    Contacts:
    1. Name: Alice 
    Phone: 1234567890 
    Email: alice@example.com

3. **Search for a Contact:**
   
    Enter name to search: Alice
    Name: Alice 
    Phone: 1234567890
    Email: alice@example.com
    
4. **Update a Contact:**
    
    Enter the name of the contact to update: Alice
    Current details: 
    Phone: 1234567890
    Email: alice@example.com
    Enter new phone (10 digits): 0987654321
    Enter new email: alice.new@example.com
    Contact updated.

5. **Delete a Contact:**
    
    Enter the name of the contact to delete: Alice
    Contact 'Alice' deleted.
</details>