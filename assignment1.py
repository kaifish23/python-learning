#Part 1: Core Contact Management
#1.1 Contact Data Structure Design
from datetime import date
contacts_db = {}
def create_contact():
    first_name =input("First Name: ")
    last_name = input("Last Name: ")
    phone = input("Phone Number (please use XXX-XXX-XXXX format): ")
    email = input("Email: ")
    street = input("Street: ")
    city = input("City: ")
    state = input("State (abbrv.): ")
    zip_code = input("ZIP Code: ")
    category = input("Category (personal, work, family): ")
    notes = input("Notes: ")
    today = str(date.today())
    
    contact = {
    'first_name': first_name,
    'last_name': last_name,
    'phone': phone,
    'email': email,
    'address': {
        'street': street,
        'city': city,
    'state': state,
    'zip_code': zip_code,
    },
    'category': category, # 'personal', 'work', 'family'
    'notes': notes,
    'created_date' : today,
    'last_modified' : today
}
    return contact

#1.2 Contact Storage System
def add_contact(contacts_db, contact_data):
    if type(contact_data) != dict:
        print("Invalid contact data")
        return None
    new_id_number = len(contacts_db) + 1
    contact_id = "contact_" + str(new_id_number)
    contacts_db[contact_id] = contact_data
    print("Contact with id:", contact_id)
    return contact_id

def display_contact(contacts_db, contact_id):
    if contact_id not in contacts_db:
        print("Contact not found")
        return False
    contact = contacts_db[contact_id]
    print("\nContact ID:", contact_id)
    print("Name:", contact['first_name'], contact['last_name'])
    print("Phone:", contact['phone'])
    print("Email:", contact['email'])
    print("Address:")
    print(" ", contact['address']['street'])
    print(" ", contact['address']['city'] + ",", contact['address']['state'], contact['address']['zip_code'])
    print("Category:", contact['category'])
    print("Notes:", contact['notes'])
    print("Created:", contact['created_date'])
    print("Last Modified:", contact['last_modified'])
    return True

def list_all_contacts(contacts_db):
    if len(contacts_db) == 0:
        print("No contacts available")
        return
    print("\n All Contacts: ")
    print("-----------")
    for contact_id in contacts_db:
        contact = contacts_db[contact_id]
        name = contact['first_name'] + " " + contact['last_name']
        print(contact_id + ":", name, "|", contact['phone'])
    print("-----------")

new_contact = create_contact()
new_id = add_contact(contacts_db, new_contact)  
display_contact(contacts_db, new_id)
list_all_contacts(contacts_db)

#1.3 Search and Retrieval
def search_contacts_by_name(contacts_db, search_term):
    results = {}
    search_term_lower = search_term.lower()
    for contact_id in contacts_db:
        contact = contacts_db[contact_id]
        first_name = contact['first_name'].lower()
        last_name = contact['last_name'].lower()
        if search_term_lower in first_name or search_term_lower in last_name:
            results[contact_id] = contact
    return results

def search_contacts_by_category(contacts_db, category):
    results = {}
    for contact_id in contacts_db:
        contact = contacts_db[contact_id]
        if contact['category'].lower() == category.lower():
            results[contact_id] = contact
    return results

def find_contact_by_phone(contacts_db, phone_number):
    for contact_id in contacts_db:
        contact = contacts_db[contact_id]
        if contact['phone'] == phone_number:
            return contact_id, contact
    return None, None

#Part 2: Advanced Operations
#2.1 Contact Modification and Deletion
def update_contact(contacts_db, contact_id, field_updates):
    if contact_id not in contacts_db:
        print("Contact not found")
        return False
    contact = contacts_db[contact_id]
    for key in field_updates:
        if key == 'address':
            for addr_key in field_updates['address']:
                contact['address'][addr_key] = field_updates['address'][addr_key]
        else:
            contact[key] = field_updates[key]
    contact['last_modified'] = str(date.today())
    print("Contact updated successfully!")
    return True

def delete_contact(contacts_db, contact_id):
    if contact_id not in contacts_db:
        print("Contact not found")
        return False
    confirm = input("Delete this contact? (yes/no): ")
    if confirm.lower() == 'yes':
        del contacts_db[contact_id]
        print("Successfully deleted")
        return True
    else:
        print("Deletion cancelled")
        return False

def merge_contacts(contacts_db, contact_id1, contact_id2):
    if contact_id1 not in contacts_db or contact_id2 not in contacts_db:
        print("One or both contacts not found")
        return None
    contact1 = contacts_db[contact_id1]
    contact2 = contacts_db[contact_id2]
    merged_contact = {}
    for key in contact1:
        if key == 'address':
            merged_contact['address'] = {}
            for addr_key in contact1['address']:
                val1 = contact1['address'][addr_key]
                val2 = contact2['address'][addr_key]
                if val1 != val2:
                    choice = input("Conflict in {field}: 1={v1} 2={v2}. Choose to keep 1 or 2: ".format(field=addr_key, v1=val1, v2=val2))
                    merged_contact['address'][addr_key] = val2 if choice == '2' else val1
                else:
                    merged_contact['address'][addr_key] = val1
        elif key in ['created_date', 'last_modified']:
            merged_contact['created_date'] = contact1['created_date']
            merged_contact['last_modified'] = max(contact1['last_modified'], contact2['last_modified'])
        else:
            val1 = contact1[key]
            val2 = contact2[key]
            if val1 != val2:
                choice = input("Conflict in {field}: 1={v1} 2={v2}. Choose to keep 1 or 2: ".format(field=key, v1=val1, v2=val2))
                merged_contact[key] = val2 if choice == '2' else val1
            else:
                merged_contact[key] = val1
    return merged_contact


#2.2 Data Analysis and Reporting
from collections import Counter
def generate_contact_statistics(contacts_db):
    stats = {
        "total_contacts": len(contacts_db),
        "contacts_by_category": {},
        "contacts_by_state": {},
        "average_contacts_per_category": 0,
        "most_common_are_code": None,
        "contacts_without_email": 0
    }
    if len(contacts_db) == 0:
        return stats
    category_counter = Counter()
    state_counter = Counter()
    area_codes = []
    no_email_count = 0
    for contact in contacts_db.values():
        category_counter[contact['category']] += 1
        state_counter[contact['address']['state']] += 1
        if "-" in contact['phone']:
            area_code = contact['phone'].split("-")[0]
            area_codes.append(area_code)
        if not contact['email']:
            no_email_count += 1
    stats["contacts_by_category"] = dict(category_counter)
    stats["contacts_by_state"] = dict(state_counter)
    stats["average_contacts_per_category"] = round(len(contacts_db) / len(category_counter), 2)
    stats["contacts_without_email"] = no_email_count
    if area_codes:
        stats["most_common_area_code"] = Counter(area_codes).most_common(1)[0][0]
    return stats

def find_duplicate_contacts(contacts_db):
    duplicates = {
        "phone_duplicates": [],
        "email_duplicates": [],
        "name_duplicates": []
    }
    phone_map = {}
    email_map = {}
    name_map = {}
    for contact_id, contact in contacts_db.items():
        phone = contact['phone']
        email = contact['email']
        name = (contact['first_name'].lower(), contact['last_name'].lower())
        if phone in phone_map:
            duplicates["phone_duplicates"].append([phone_map[phone], contact_id])
        else:
            phone_map[phone] = contact_id
        if email in email_map:
            duplicates["email_duplicates"].append([email_map[email], contact_id])
        else:
            email_map[email] = contact_id
        if name in name_map:
            duplicates["name_duplicates"].append([name_map[name], contact_id])
        else:
            name_map[name] = contact_id
    return duplicates

def export_contacts_by_category(contacts_db, category):
    output = []
    for contact_id, contact in contacts_db.items():
        if contact['category'].lower() == category.lower():
            contact_str = (
                f"ID: {contact_id}\n"
                f"Name: {contact['first_name']} {contact['last_name']}\n"
                f"Phone: {contact['phone']}\n"
                f"Email: {contact['email']}\n"
                f"Address: {contact['address']['street']}, "
                f"{contact['address']['city']}, {contact['address']['state']} {contact['address']['zip_code']}\n"
                f"Notes: {contact['notes']}\n"
                f"Created: {contact['created_date']}\n"
                f"Last Modified: {contact['last_modified']}\n"
                "--------------"  
            )
            output.append(contact_str)
    if not output:
        return f"No contacts found in category: {category}"
    return "\n".join(output)

#Part 3: User Interface and Integration
#3.1 Command-Line Interface
def main_menu():
    print("\n--- Contact Main Menu ---")
    print("1. Add new contact")
    print("2. Search contacts")
    print("3. List all contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Generate statistics")
    print("7. Find duplicates")
    print("8. Export by category")
    print("9. Exit")
    choice = input("Enter your choice (1-9): ")
    return choice

def run_contact_manager():
    while True:
        choice = main_menu()
        if choice == "1":
            new_contact = create_contact()
            add_contact(contacts_db, new_contact)
        elif choice == "2":
            term = input("Enter name to search: ")
            results = search_contacts_by_name(contacts_db, term)
            if results:
                for contact_id in results:
                    display_contact(contacts_db, contact_id)
            else:
                print("No contacts found")
        elif choice == "3":
            list_all_contacts(contacts_db)
        elif choice == "4":
            contact_id = input("Enter contact id to update: ")
            updates = {}
            field = input("Enter field to update (first_name, last_name, phone, email, address, notes): ")
            value = input("Enter new value: ")
            if field == "address":
                addr_field = input("Which address field to update? (street, city, state, zip_code): ")
                updates['address'] = {addr_field: value}
            else:
                updates[field] = value
            update_contact(contacts_db, contact_id, updates)
        elif choice == "5":
            contact_id = input("Enter contact ID to delete: ")
            delete_contact(contacts_db, contact_id)
        elif choice == "6":
            stats = generate_contact_statistics(contacts_db)
            print(stats)
        elif choice == "7":
            duplicates = find_duplicate_contacts(contacts_db)
            print(duplicates)
        elif choice == "8":
            category = input("Enter category: ")
            export = export_contacts_by_category(contacts_db, category)
            print(export)
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please choose a number 1-9")
run_contact_manager()

#3.2 Data Persistence
def save_contacts_to_file(contacts_db, filename):
    f = open(filename, "w")
    for contact_id, contact in contacts_db.items():
        f.write(contact_id + "\n")
        for key, value in contact.items():
            if key == "address":
                f.write(" address: \n")
                for addr_key, addr_val in value.items():
                    f.write(f" {addr_key}: {addr_val} \n")
            else:
                f.write(f" {key}: {value} \n")
        f.write("----\n")
    f.close()
    print(f"Contacts saved to {filename}")
    