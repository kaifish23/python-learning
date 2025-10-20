#Week 7 Lecture 1: Unit 1: Introduction to Files
#File I/O
    #Input: Reading data FROM a file INTO your program
    #Output: Writing data FROM your program INTO a file
#Why is it important?
    #Data Persistence: save data between program runs
    #Data Sharing: exchange information
    #Handle Large Data: process data too big for memory
    #Real-World Applications
'''
#Student Practice
#Exercise 1a: Beginner - Understanding File Concepts
def practice_1_beginner():
    print("\n" + "="*50)
    print("Exercise 1.1: Save Your Name")
    print("="*50)
    #Get User's Name
    name = input("Enter your name: ")
    #Open a file called "myname.txt" for writing
    file = open("myname.txt", "w")
    #Write the name to the file
    file.write(name)
    #Close the file
    file.close()
    #Print
    print(f"Name '{name}' saved to myname.txt!")
    #Read it back
    file = open("myname.txt", "r")
    #Read the content
    saved_name = file.read()
    #Close the file
    print(f"Read back: '{saved_name}'")
practice_1_beginner()

#Exercise 1b: Intermediate - Save and Load Settings
def practice_1_intermediate():
    print("\n" + "="*50)
    print("Exercise 1.2: Settings Manager")
    print("="*50)
    #Game settings to save
    username = input("Enter username: ")
    difficulty = input("Enter difficulty (easy/medium/hard): ")
    sound = input("Sound on? (yes/no): ")
    #Save all settings to "settings.txt"
    file = open("settings.txt","w")
    #Write each setting on a new line
    file.write(username + "\n")
    file.write(difficulty + "\n")
    file.write(sound)
    #Close the file
    print("Settings saved!")
    #Load settings back
    print("\nLoading settings...")
practice_1_intermediate()

#Exercise 1c: Advanced - Data Persistence System
def practice_1_advanced():
    print("\n" + "="*50)
    print("Exercise 1.3: Persistent Counter")
    print("="*50)
    #File
    counter_file_name = "counter.txt"
    #Check if counter file exists and load value
    counter_file = open(counter_file_name, "r")
    counter = int(counter_file.read())
    counter_file.close()
    print(f"Loaded existing counter: {counter}")
    #Increment counter
    counter += 1
    print(f"Incremented to: {counter}")
    #Save updated counter
    counter_file = open(counter_file_name, "w")
    counter_file.write(str(counter))
    counter_file.close()
    #Create a visit log
    visit_file = open("visits.txt", "a") #"a" = append
    visit_file.write("Visit #" + str(counter) + "\n")
    visit_file.close()
    #Read and display last 5 visits
    print("\nLast visits:")
    visit_file = open("visits.txt", "r")
    visits = visit_file.readlines()
    visit_file.close()
    #Print last 5
    for line in visits[-5:]:
        print(line.strip())
practice_1_advanced()

#Week 7 Lecture 1: Unit 2: Python File Types and Objects
#Text vs Binary
    #Text (Human-readable):
        #.py, .txt, .csv, .html
        #Can open in Notepad
        #Uses string operations
        #Contains readable characters
    #Binary (Machine-readable):
        #.jpg, .mp3, .exe, .pdf
        #Looks like gibberish in Notepad
        #Contains bytes/binary data
#File Objects
    #When you open a file, Python creates a file object - like a remote control for the file
        #file.read()  = read content
        #file.write() = write content
        #file.close() = close file 
    #End-Of-File (EOF):
        #Reading past EOF returns empty string
        #Similar to reaching the last page in a book
    #Standard File Objectives
        #sys.stdin  = standard input  (keyboard)
        #sys.stdout = standard output (screen)
        #sys.stderr = standard error  (error message)

#Student Exercise
#Exercise 2a: Beginner - File Types
def practice_2_beginner():
    print("\n" + "="*50)
    print("Exercise 2.1: File Object Basics")
    print("="*50)
    #Create a text file with 3 lines
    number_text = open("numbers.txt", "w")
    number_text.write("10\n")
    number_text.write("20\n")
    number_text.write("30\n")
    number_text.close()
    #Open the file and check its properties
    number_text = open("numbers.txt", "r")
    #Print file name
    print(f"File name: {number_text.name}")
    #Print file mode
    print(f"File mode: {number_text.mode}")
    #Check if file is closed
    print(f"Is the file closed?", number_text.closed)
    #Read one line at a time until EOF
    while True:
        line = number_text.readline()
        if line == "": # Check for EOF
            print("Reached end!")
            break
        print(f"Read: {line.strip()}")
    number_text.close()
practice_2_beginner()

#Exercise 2b: Intermediate - File Position
def practice_2_intermediate():
    print("\n" + "="*50)
    print("Exercise 2.2: File Position Tracking")
    print("="*50)
    #Create a file with alphabet
    alphabet_file = open("alphabet.txt", "w")
    alphabet_file.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alphabet_file.close()
    #Open and read specific positions
    alphabet_file = open("alphabet.txt", "r")
    #Read first 5 characters
    chunk1 = alphabet_file.read(5)
    print(f"First 5: {chunk1}")
    #Check current position
    position = alphabet_file.tell()
    print(f"Current position: {position}")
    #Read next 5 characters
    chunk2 = alphabet_file.read(5)
    print(f"Next 5: {chunk2}")
    #Check position again
    position = alphabet_file.tell()
    print(f"Current position: {position}")
    #Read until EOF
    remaining = alphabet_file.read()
    print(f"Remaining: {remaining}")
    #Close file
    alphabet_file.close()
practice_2_intermediate()

#Exercise 2c: Advanced - Multi-File System
def practice_2_advanced():
    print("\n" + "="*50)
    print("Exercise 2.3: Multi-File Log System")
    print("="*50)
    #Import
    import sys 
    from datetime import datetime
    #Create three different log files
    info_log = open("info.log", "w")
    error_log = open("error.log", "w")
    debug_log = open("debug.log", "w")
    #Write appropriate messages to each
    info_log.write("System started\n")
    error_log.write("System error\n")
    debug_log.write("System debug\n")
    #Close all files
    info_log.close()
    error_log.close()
    debug_log.close()
    #Create a master log reader
    print("Log Summary:")
    #Read and count lines in each log
    for log_name in ["info.log", "error.log", "debug.log"]:
        log_file = open(log_name, "r")
        lines = log_file.readlines()
        log_file.close()
        print(f"{log_name}: {len(lines)} entries")
    #Show first line of each log
        if lines:
            print(f"First Entry for {log_name.split('.')[0].capitalize()}: {lines[0].strip()}")
practice_2_advanced()

#Week 7 Lecture 1: Unit 3: Text File Processing Operations
#Opening Files - The Modes
    #Common Modes
        #'r'  = read (default) - file must exist
            #read()      = read everything
            #readline()  = read one line
            #readlines() = read all lines into list
        #'w'  = write - creates new/overwrites existing
            #write()      = write string
            #writelines() = write list of strings
        #'a'  = append - adds to the end
        #'r+' = read AND write
        #'x'  = exclusive creation - fails if exists
    #seek() = jump to position
        #seek(0)    = beginning
        #seek(10)   = byte 10
        #seek(0, 2) = end of file

#Student Practice
#Exercise 3a: Beginner - Basic Read/Write
def practice_3_beginner():
    print("\n" + "="*50)
    print("Exercise 3.1: Student Grades File")
    print("="*50)
    #Write student grades to file
    grades_file = open("grades.txt", "w")
    #Write these grades (each on new line)
    grades_file.write("Alice: 90\n")
    grades_file.write("Bob: 85\n")
    grades_file.write("Charlie: 92\n")
    #Close file
    grades_file.close()
    print("Grades written!")
    #Read the file using read()
    grades_file = open("grades.txt", "r")
    content = grades_file.read()
    print(f"\nAll grades:\n{content}")
    grades_file.close()
    #Read line by line
    print("\nReading line by line:")
    grades_file = open("grades.txt", "r")
    #Use readline() three times
    line1 = grades_file.readline()
    line2 = grades_file.readline()
    line3 = grades_file.readline()
    print(f"Student 1: {line1}")
    print(f"Student 2: {line2}")
    print(f"Student 3: {line3}")
    grades_file.close()
practice_3_beginner()

#Exercise 3b: Intermediate - File Updates
def practice_3_intermediate():
    print("\n" + "="*50)
    print("Exercise 3.2: Todo List Manager")
    print("="*50)
    #Create initial todo list
    todos = [
        "Buy groceries\n",
        "Study Python\n",
        "Exercise\n"
    ]
    todo_file = open("todo.txt", "w")
    #Use writelines() to write todos
    todo_file.writelines(todos)
    todo_file.close()
    print("Initial todos created!")
    #Read and display with numbers
    todo_file = open("todo.txt", "r")
    lines = todo_file.readlines()
    todo_file.close()
    #Display
    print("\nCurrent Todo List:")
    for i, task in enumerate(lines, 1):
        print(f"{i}. {task.strip()}")
    #Append new tasks
    new_task = input("\nAdd a task: ")
    todo_file = open("todo.txt", "a")
    #Write the new task with newline
    todo_file.write(new_task + "\n")
    todo_file.close()
    #Show updated list
    todo_file = open("todo.txt", "r")
    lines = todo_file.readlines()
    todo_file.close()
    print("\nUpdated Todo List:")
    for i, task in enumerate(lines, 1):
        print(f"{i}. {task.strip()}")
practice_3_intermediate()
'''
#Exercise 3c: Advanced - Seek Operations
def practice_3_advanced():
    print("\n" + "="*50)
    print("Exercise 3.3: Random Access File")
    print("="*50)
    #Create a file with position markers
    positions_file = open("positions.txt", "w")
    positions_file.write("0123456789" * 5) # 50 characters
    positions_file.close()
    #Read specific ranges using seek
    positions_file = open("positions.txt", "r")
    #Read characters 0-9
    chunk1 = positions_file.read(10)
    print(f"Chars 0-9: {chunk1}")
    #Jump to position 20 and read 10 chars
    positions_file.seek(20)
    chunk2 = positions_file.read(10)
    print(f"Chars 20-29: {chunk2}")
    #Get current position
    current = positions_file.tell()
    print(f"Current position: {current}")
    #Go back to beginning
    positions_file.seek(0)
    #Create a "bookmark" system
    bookmarks = {}
    #Save positions
    positions_file.seek(10)
    bookmarks["chapter1"] = positions_file.tell()
    positions_file.seek(25)
    bookmarks["chapter2"] = positions_file.tell()
    positions_file.seek(40)
    bookmarks["chapter3"] = positions_file.tell()
    print(f"\nBookmarks: {bookmarks}")
    #Jump to bookmarks
    for name, position in bookmarks.items():
        positions_file.seek(position)
        content = positions_file.read(5)
        print(f"{name} (pos {position}): {content}")
    positions_file.close()
practice_3_advanced()

#Week 7 Lecture 2: Unit 1: Working with File Formats
#Common Text-Based Formats
    #Plain Text (.txt)
        #Simple and human-readable
        #No formatting
        #Universal compatibility
    #Comma-Separated Values (.csv)
        #Tabular data in text form
        #Rows and columns
        #Used by Excel databases
    #JavaScript Object Notation (.json)
        #Structured data format
        #Human and machine-readable
        #Standard for web APIs

#Student Practice
#Set 1: Beginner - Text to CSV
def practice_1a_beginner():
    print("\n" + "="*50)
    print("Exercise 1.1: Text to CSV Converter")
    print("="*50)
    #Create a text file with data
    with open("employees.txt", "w") as employees:
        employees.write("John Smith 35 Engineer\n")
        employees.write("Jane Doe 28 Designer\n")
        employees.write("Bob Johnson 42 Manager\n")
    #Read text file and convert to CSV
    with open("employees.txt", "r") as employees:
        with open("employees.csv", "w") as employees_csv: 
            #Write CSV header
            employees_csv.write("First,Last,Age,Job\n")
            #Read each line and convert
            for line in employees: 
                parts = line.strip().split()
                first = parts[0]
                last = parts[1]
                age = parts[2]
                job = parts[3]
                #Write as CSV line
                csv_line = f"{first},{last},{age},{job}"
                employees_csv.write(csv_line + "\n")
    #Read and verify CSV
    print("\nCSV Contents:")
    with open("employees.csv", "r") as employees_csv:
        for line in employees_csv:
            print(line.strip())
practice_1a_beginner()

#Set 2: Intermediate - CSV Processing
def practice_2a_intermediate():
    print("\n" + "="*50)
    print("Exercise 1.2: Grade Calculator")
    print("="*50)
    #Create grades CSV
    with open("grades.csv", "w") as grades:
        grades.write("Student,Math,Science,English\n")
        grades.write("Alice,95,87,92\n")
        grades.write("Bob,78,85,88\n")
        grades.write("Charlie,92,94,85\n")
        grades.write("Diana,88,91,95\n")
    #Read CSV and calculate averages
    with open("grades.csv", "r") as grades:
        header = grades.readline().strip().split(",")
        print(f"Subjects: {header[1:]}")
        student_averages = []
        for line in grades: 
            parts = line.strip().split(",")
            name = parts[0]
            #Convert grades to numbers
            grades_list = [int(score) for score in parts[1:]]
            #Calculate average
            average = sum(grades_list) / len(grades_list)
            student_averages.append((name, average))
            print(f"{name}: {average:.1f}")
    #Save results to new CSV
    with open("averages.csv", "w") as averages: 
        averages.write("Student,Average\n")
        #Write each student's average
        for name, avg in student_averages:
            averages.write(f"{name},{avg:.1f}\n")
practice_2a_intermediate()

#Set 3: Advanced - JSON Data Manager
def practice_3a_advanced():
    print("\n" + "="*50)
    print("Exercise 1.3: JSON Database")
    print("="*50)
    import json 
    #Create a product database in JSON
    products = {
        "inventory": [
            {"id": 1, "name": "Laptop", "price": 999.99, "stock": 5},
            {"id": 2, "name": "Mouse", "price": 29.99, "stock": 15},
            {"id": 3, "name": "Keyboard", "price": 79.99, "stock": 8}
        ],
        "last_updated": "2024-01-15",
        "store": "Tech Store"
    }
    #Save to JSON
    with open("products.json", "w") as file:
        json.dump(products, file, indent=4)
    print("Product database created")
    #Load and modify JSON
    with open("products.json", "r") as file:
        data = json.load(file)
    #Add a new product
    new_product = {
        "id": 4,
        "name": "Monitor",
        "price": 299.99,
        "stock": 3
    }
    #Add to inventory
    data["inventory"].append(new_product)
    print("New product added: Monitor")
    #Update stock levels
    for item in data["inventory"]:
        if item["name"] == "Mouse":
            item["stock"] += 5
        elif item["name"] ==  "Laptop":
            item["stock"] -= 1
    #Save updated data
    with open("products.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Updated product database saved.")
    #Generate report from JSON
    print("\nInventory Report:")
    total_value = 0
    for item in data["inventory"]:
        item_value = item["price"] * item["stock"]
        total_value += item_value
        print(f"{item['name']}: {item['stock']} in stock (${item_value:.2f} value)")
practice_3a_advanced()

#Week 7 Lecture 2: Unit 2: JSON Serialization
#Serialization: Converting Python objects to a format that can be stored or transmitted (pack)
#Deserialization: Converting stored data back to Python objects (unpack)
#JSON Module Methods
    #Serialize to string 
        #json.dumps(obj)       = Object to JSON string
    #Serialize to file
        #json.dump(onj, file) = Object to JSON file
    #Deserialize from string
        #json.loads(string)    = JSON string to object
    #Deserialize from file
        #json.load(file)       = JSON file to object
#Python to JSON conversion
    #dict -> object
    #list, tuple -> array
    #str -> string
    #int, float -> number
    #True/False -> true/false
    #None -> null
#JSON Formatting Options
    #Pretty Printing
        #json.dump(data, file, indent=4) = Indented output
    #Sorting Keys
        #json.dump(data, file, sort_keys=True)
    #Compact output
        #json.dump(data, file, separators=(',', ':'))

#Student Practice
#Set 1: Beginner - JSON Basics
def practice_1b_beginner():
    print("\n" + "="*50)
    print("Exercise 2.1: JSON Contact Card")
    print("="*50)    
    import json 
    #Create a contact dictionary
    contact = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "555-1234",
        "age": 25
    }
    #Convert to JSON string
    json_str = json.dumps(contact)
    print(f"JSON String: {json_str}")
    #Save to file
    with open("contact.json", "w") as c: 
        json.dump(contact, c, indent=4)
    print("Contact saved to file")
    #Load from file 
    with open("contact.json", "r") as c:
        loaded_contact = json.load(c)
    #Access data
    print(f"\nLoaded contact:")
    print(f"Name: {loaded_contact['name']}")
    print(f"Email: {loaded_contact['email']}")
practice_1b_beginner()

#Set 2: Intermediate - Settings Manager
def practice_2b_intermediate():
    print("\n" + "="*50)
    print("Exercise 2.2: Settings Manager")
    print("="*50)
    import json
    #Default settings
    default_settings = {
        "app_name": "My App",
        "version": "1.0.0",
        "user_preferences": {
            "theme": "dark",
            "font_size": 12,
            "auto_save": True
        },
        "recent_files": [],
        "window_size": [800, 600]
    }
    #Save default settings
    with open("settings.json", "w") as settings_json:
        json.dump(default_settings, settings_json, indent=4)
    print("Default settings created")
    #Load and modify settings
    with open("settings.json", "r") as settings_json:
        settings = json.load(settings_json)
    #Save updated settings
    with open("settings.json", "w") as settings_json:
        json.dump(settings, settings_json, indent=4)
    #Create backup
    with open("settings.json", "r") as settings_json:
        backup_data = settings_json.read()
    with open("settings_backup.json", "w") as settings_backup:
        settings_backup.write(backup_data)
    print("Settings backed up")
practice_2b_intermediate()

#Week 7 Lecture 2: Unit 3: Pickle and File Paths
#What is Pickle?
    #Python-specific serialization
    #Can save ANY Python object
    #Binary format (not human-readable)
    #Use when JSON isn't enough
#File Paths
    #Absolute Path: Complete path from root
        #Windows: C:\Users\John\Documents\file.txt
        #Unix/Linux: /home/john/documents/file.txt
    #Relative Path: Path from current location
        #./file.txt      = current directory
        #../file.txt     = parent directory
        #folder/file.txt = subdirectory
#Path Differences
    #Windows vs Unix/Linux:
        #Windows: \
        #Unix/Linux: /
        #Python accepts both or use: os.path.join()
#Pathlib (Modern Approach)
    #Path operations
        #path.exists()  = check if path exists
        #path.is_file() = check if it is a file
        #path.is_dir()  = check if it is a directory
        #path.parent    = get parent directory 
        
#Student Practice
#Set 1: Beginner - Simple Pickle
def practice_1c_beginner():
    print("\n" + "="*50)
    print("Exercise 3.1: Pickle Basics")
    print("="*50)
    import pickle
    #Create a list to pickle
    shopping_list = ["Apples", "Bananas", "Milk", "Bread"]
    #Save with pickle
    with open("shopping.pkl", "wb") as shop:
        pickle.dump(shopping_list, shop)
    print("Shopping list pickled!")
    #Load with pickle
    with open("shopping.pkl", "rb") as shop:
        loaded_list = pickle.load(shop)
    print(f"Loaded list: {loaded_list}")
    #Add items and re-save
    loaded_list.append("Eggs")
    loaded_list.append("Cheese")
    with open("shopping.pkl", "wb") as shop:
        pickle.dump(loaded_list, shop)
    print("Updated list saved")
practice_1c_beginner()

#Set 2: Intermediate - Path Operations
def practice_2c_intermediate():
    print("\n" + "="*50)
    print("Exercise 3.2: File Navigator")
    print("="*50)
    import os
    from pathlib import Path
    #Get current directory
    current = Path.cwd()
    print(f"Current directory: {current}")
    #Create file paths
    #Relative path
    rel_path = "data/file.txt"
    #Absolute path
    abs_path = "/home/john/documents/file.txt"
    print(f"Relative: {rel_path}")
    print(f"Absolute: {abs_path}")
    #Check multiple files
    files_to_check = [
        "students.pkl",
        "data.json",
        "nonexistent.txt"
    ]
    print("\nFile Check:")
    for filename in files_to_check:
        exists = os.path.exists(filename)
        #Print status
        print(f"{filename}: {'Found' if exists else 'Not Found'}")
    #Use pathlib
    path = Path("test_file.txt")
    #Create the file
    if not path.exists():
        path.write_text("Hello, this is a test file!")
        print(f"Created: {path.name}")
    else:
        print(f"File already exists: {path.name}")
    #Check path properties
    print(f"Exists: {path.exists()}")
    print(f"Absolute path: {path.resolve()}")
    print(f"File name: {path.name}")
    print(f"Parent directory: {path.parent}")
practice_2c_intermediate()