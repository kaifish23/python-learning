# Project 1 - Contact Creation
### by Kai Broviak

## Project Description and Its Features
This project is a contact management system using Python dictionaries. It consists of various functions, including but not limited to, merging two dictionaries, a search function, adding and modifying pre-existing contacts and deleting a created contact. 

## How to Run the Program
Once you have initiated the run code, you will be prompted to enter your own contact information to begin with. Once that has been completed, a "Contact Main Menu" will be displayed, where numbers 1-9 will have an assigned function. To search for a contact, enter the persons name. When listing contacts, the contact ID (contact_1), the persons name and their number will be displayed. To update a contact, enter the contact ID, then choose which field you want to update. Everything else is very self-explainitory.

## Function Documentation With Examples
def list_all_contacts(contacts_db):
    display a summary list of all contacts (ID, name, phone)

    Args:
        contact_db (dictionary): the main contacts database
    

    Example:
    contact_1: firstname lastname | XXX-XXX-XXXX

def export_conacts_by_category(contacts_db, category):
    export contacts from a specific category as a formatted string.
    include all contacts information in a readable format

    Args:
        contacts_db (dict): the main database
        category (str): category to export
    
    Returns:
        str: formatted string representation of all contacts in category

    Example:
    enter category: personal
    ID: contact_1
    Name: firstname lastname
    Phone: XXX-XXX-XXXX
    Email: email@email.com
    Address: 1600 E Washington Blvd, Fort Wayne, IN 46308
    Notes: note
    Created: 2025-08-28
    Last Modified: 2025-09-01

## Known Limitations and Future Improvements
The known limitations within this project are the inabilities to sort contacts alphabetically, unable to assign contact images or photos, and unable to block saved contacts. In the future, there might be a patch where might be able to add contacts to a "favorite" dictionary, to provide an easier way to contact those people.

## Sample Usage Scenarios
You would use this code when wanting a contact-like dictionary that is able to store names, numbers, addresses, emails, notes, and even categories on how you know the person. It works similarly to how a phone's contact application might. 