import assignment1
def test_create_contact():
    contacts_db = {}
    contact_data = {
        'first_name' : 'Molly',
        'last_name' : 'Stewart',
        'phone' : '317-258-8005',
        'email' : 'mollystewart@yahoo.com', 
        'address' : {
            'street' : '10203 Holly Berry Circ',
            'city' : 'Noblesville',
            'state' : 'IN',
            'zip_code' : '46060'
        },
        'category' : 'family'
    }
    contact_id = assignment1.add_contact(contacts_db, contact_data)
    assert contact_id in contacts_db
    print("test passed!")
    
def test_search_function():
    contacts_db = {}
    contact_id = assignment1.add_contact(contacts_db, {
        'first_name' : 'david',
        'last_name' : 'broviak',
        'phone' : '317-413-8872',
        'email' : 'broviak@evilteacher.com',
        'address' : {
            'street' : '13890 Meadow Lake Dr',
            'city' : 'fishers',
            'state' : 'IN',
            'zip_code' : '46038'
        },
        'category' : 'personal'
    })
    result = assignment1.search_contacts(contacts_db, 'david')
    assert contact_id in result
    result = assignment1.search_contacts(contacts_db, '317-413-8872')
    assert contact_id in result
    result = assignment1.search_contacts(contacts_db, 'personal')
    assert contact_id in result
    print("search passed")
    
def test_contact_operation():
    contacts_db = {}
    contact_id = assignment1.add_contact(contacts_db, {
        'first_name' : 'ian',
        'last_name' : 'byczek',
        'phone' : '460-606-6060',
        'email' : 'ianbyczek@gmail.com',
        'address' : {
            'street' : '11594 Boothbay Ln',
            'city' : 'Iron River',
            'state' : 'MI',
            'zip_code' : '49935'
        },
        'category' : 'work'
    })
    assert contact_id in contacts_db
    updates = {'phone' : '123-456-7890'}
    assignment1.update_contact(contacts_db, contact_id, updates)
    assert contacts_db[contact_id]['phone'] == '123-456-7890'
    assignment1.delete_contact(contacts_db, contact_id)
    assert contact_id not in contacts_db
    print("test update/delete passed")
    
def test_data():
    contacts_db = {}
    contact_1 = assignment1.add_contact(contacts_db, {
        'first_name' : 'jenna',
        'last_name' : 'bachmann',
        'phone' : '317-517-1674',
        'email' : 'jennabroviak@gmail.com',
        'address' : {
            'street' : '10859 Thistle Ridge',
            'city' : 'West Lafayette',
            'state' : 'IN',
            'zip_code' : '47907'
        },
        'category' : 'work'
    })
    contact_2 = assignment1.add_contact(contacts_db, {
        'first_name' : 'kai',
        'last_name' : 'broviak',
        'phone' : '317-864-2952',
        'email' : 'kaileybroviak@gmail.com',
        'address' : {
            'street' : '1600 E Washington Blvd',
            'city' : 'Fort Wayne',
            'state' : 'IN',
            'zip_code' : '46308'
        },
        'category' : 'personal'
    })
    stats = assignment1.generate_contact_statistics(contacts_db)
    assert stats["total_contacts"] == 2
    duplicates = assignment1.find_duplicate_contacts(contacts_db)
    assert any(contact_1 in dupe and contact_2 in dupe for dupe in duplicates['phone_duplicates'])
    print('test data passed!')
    
def run_all_tests():
    test_create_contact()
    test_contact_operation()
    test_data()
    test_search_function()
    print("\n all tests passed!")
    
if __name__ == "__main__":
    run_all_tests()