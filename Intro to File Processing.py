#Week 7 Lecture 1: Unit 1: Introduction to Files
#File I/O
    #Input: Reading data FROM a file INTO your program
    #Output: Writing data FROM your program INTO a file
#Why is it important?
    #Data Persistence: save data between program runs
    #Data Sharing: exchange information
    #Handle Large Data: process data too big for memory
    #Real-World Applications

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
