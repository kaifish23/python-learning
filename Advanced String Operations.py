import numpy as np #just in case we use numpy

#Unit 1: String Methods - Changing Case and Cleaning
#Case Methods
text = "Hello World"
text.upper()      #"HELLO WORLD"
text.lower()      #"hello world"
text.title()      #"Hello World"
text.capitalize() #"Hello world"
text.swapcase()   #"hELLO wORLD"
#Strip Methods
text = "    Hello World    "
text.strip()  #"Hello World" - removes spaces at both ends
text.lstrip() #"Hello World    " - removes spaces from left end
text.rstrip() #"    Hello World" - removes spaces from right end

#Student Practice: String Cleaning
def practice_1a_beginner():
    print("\n" + "="*50)
    print("Exercise 1a: Clean the Name (Beginner)")
    print("="*50)
    #Messy name from user input
    messy_name = "  jOhN sMiTh  "
    print(f"Messy name: '{messy_name}'")
    #remove spaces from both ends
    no_spaces = messy_name.strip()
    #convert to title case
    clean_name = no_spaces.title()
    print(f"After removing spaces: '{no_spaces}'")
    print(f"Final clean name: '{clean_name}'")
practice_1a_beginner()

def practice_1b_intermediate():
    print("\n" + "="*50)
    print("Exercise 1b: Email Standardizer (Intermediate)")
    print("="*50)
    #list of messy emails
    emails = [
        "   JOHN@GMAIL.COM",
        "Alice@Yahoo.com    ",
        "   Bob@HOTMAIL.COM    "
    ]
    print("Messy emails:")
    for email in emails:
        print(f"    '{email}'")
    cleaned_emails = []
    for email in emails:
        #remove spaces
        cleaned = email.strip()
        #convert to lowercase
        cleaned = cleaned.lower()
        #add to clean email list
        cleaned_emails.append(cleaned)
        print("\n Cleaned emails:")
        for email in cleaned_emails:
            print(f"✓ {email}")
practice_1b_intermediate()

def practice_1c_advanced():
    print("\n" + "="*50)
    print("Exercise 1c: Data Processor (Advanced)")
    print("="*50)
    #user registration data (messy!)
    user_data = {
        "name":"    JANE DOE    ",
        "email":"   Jane@Email.COM",
        "username":"    JaNe_DoE_123    ",
        "country":"united states"
    }
    print("Original data:")
    for key, value in user_data.items():
        print(f"    {key}: '{value}'")
    #clean all fields appropriately
    cleaned_data = {}
    #Name: strip spaces and title case
    cleaned_data["name"] = user_data["name"].strip().title()
    #Email: strip spaces and lowercase
    cleaned_data["email"] = user_data["email"].strip().lower()
    #Username: strip spaces and lowercase
    cleaned_data["username"] = user_data["username"].strip().lower()
    #Country: strip spaces and title case
    cleaned_data["country"] = user_data["country"].strip().title()
    print("\n Cleaned data:")
    for key, value in cleaned_data.items():
        print(f"    {key}: '{value}'")
    #Bonus: check if all fields were cleaned
    expected = {
        "name": "Jane Doe",
        "email": "jane@email.com",
        "username": "jane_doe_123",
        "country": "United States"
    }
    if cleaned_data == expected:
        print("\n Excellent!")
    else:
        print("\n Try again!")
practice_1c_advanced()

#Unit 2: String Searching and Checking
#Finding substrings
text = "Python programming is fun"
#Check if something exists
"Python" in text #True
"java" in text   #False
#Find position
text.find("programming") #7 - returns index where found
text.find("java")        #-1 - returns -1 if not found
text.index("programming")#7 - works like text.find
text.count("n")          #3 - how many times "n" is there
#Checking string content
#Is it alphabetic?
"Hello".isalpha()    #True - only letters
"Hello123".isalpha() #False - has numbers
#Is it numeric?
"12345".isdigit() #True - only digits
"12.34".isdigit() #False - decimal is not a digit
#Is it alphanumeric?
"Hello123".isalnum()  #True - letters/numbers
"Hello 123".isalnum() #False - a space isnt letter/numbers
#Other checks
"   ".isspace()   #True - only whitespace
"Hello".isupper() #False - not all uppercase/caps
"HELLO".isupper() #True - all uppercase/caps
"hello".lower()   #True - all lowercase
#Starts and ends checking
filename = "report.pdf"
filename.startswith("report") #True
filename.endswith(".pdf")     #True
filename.endswith(".doc")     #False
filename.endswith((".pdf", ".doc", ".txt")) #True if ANY match, multiple checks at once

#Student Practice: String Searching
def practice_2a_beginner():
    print("\n" + "="*50)
    print("Exercise 2a: Find Words (Beginner)")
    print("="*50)
    sentence = "Python programming is really fun and programming is useful"
    print(f"Sentence: {sentence}")
    #Check if "Python" is in the sentence
    has_python = "Python" in sentence
    #Count how many times "programming" appears
    prog_count = sentence.count("programming")
    #Find the positon of "fun"
    fun_position = sentence.find("fun")
    print(f"Contains 'Python': {has_python}")
    print(f"'Programming' appears: {prog_count} times")
    print(f"'Fun' starts at position: {fun_position}")
practice_2a_beginner()

def practice_2b_intermediate():
    print("\n" + "="*50)
    print("Exercise 2b: Password Checker (Intermediate)")
    print("="*50)
    #passwords
    passwords = ["abc123", "PASSWORD", "Pass123!", "12345678"]
    for password in passwords:
        print(f"\n Checking: {password}")
        #Check if password has any digits
        has_digit = any(char.isdigit() for char in password)
        #Check if password has uppercase
        has_upper = any(char.isupper() for char in password)
        #Check if password has lowercase
        has_lower = any(char.islower() for char in password)
        #Check if length is at least 8 characters
        long_enough = len(password) >= 8
        print(f" Has digit: {has_digit}")
        print(f" Has uppercase: {has_upper}")
        print(f" Has lowercase: {has_lower}")
        print(f" Length >= 8: {long_enough}")
        #Check if strong
        if all([has_digit, has_upper, has_lower, long_enough]):
            print("Strong password!")
        else:
            print("Weak password!")
practice_2b_intermediate()

def practice_2c_advanced():
    print("\n" + "="*50)
    print("Exercise 2c: File Type Detector (Advanced)")
    print("="*50)
    #files
    files = [
     "document.pdf",
     "image.jpg",
     "photo.PNG",
     "script.py",
     "data.CSV",
     "video.mp4",
     "archive.zip",
     "webpage.html"   
    ]
    #Categories
    documents = []
    images = []
    code = []
    other = []
    for filename in files:
        #Convert to lowercase
        lower_name = filename.lower()
        #Categorize files based on extension
        if lower_name.endswith(('.pdf', '.doc', '.txt')):
            documents.append(filename)
        elif lower_name.endswith(('.jpg', '.png', '.jpeg', '.gif')):
            images.append(filename)
        elif lower_name.endswith(('.py', '.js', '.html', '.css')):
            code.append(filename)
        else:
            other.append(filename)
    print("File Categories:")
    print(f"Documents: {documents}")
    print(f"Images: {images}")
    print(f"Code Files: {code}")
    print(f"Other: {other}")
    #Bonus Statistics
    total = len(files)
    print(f"\n Statistics:")
    print(f"Total files: {total}")
    print(f"Total Documents: {len(documents)}/{total}")
    print(f"Total Images: {len(images)}/{total}")
    print(f"Total Code Files: {len(code)}/{total}")
    print(f"Total Other Files: {len(other)}/{total}")
practice_2c_advanced()

#Unit 3: String Replacement and Splitting
#The replace() method
text = "I love Java. Java is great!"
#replace all occurances
new_text = text.replace("Java", "Python") #I love Python. Python is great!
#replace limited occurances
new_text = text.replace("Java", "Python", 1) #I love Python. Java is great!
#chain replacement
text = "Hello World"
result = text.replace("Hello", "Hi").replace("World", "Earth") #Hi Earth
#Splitting Strings
#Breaking strings into lists
#split by spaces (default)
text = "apple banana orange"
fruits = text.split()       #['apple', 'banana', 'orange']
#split by specific character
data = "john,25,engineer"
fields = data.split(",")    #['john', '25', 'engineer']
#limit splits
data = "a-b-c-d"
parts = data.split("-", 2)  #['a', 'b', 'c-d'] only 2 splits
#split lines
text = "Line 1\nLine 2\nLine 3"
lines = text.splitlines()   #['Line 1', 'Line 2', 'Line 3']
#Joining Strings
#combining lists into strings
#join with separator
words = ['Hello', 'World']
sentence = " ".join(words)   #"Hello World"
#join with different separators
items = ['apple', 'banana', 'orange']
csv = ",".join(items)        #"apple,banana,orange"
dashed = "-".join(items)     #"apple-banana-orange"
#join letters with empty strings
letters = ['p', 'y', 't', 'h', 'o', 'n']
word = "".join(letters)      #"python"

#Student Practice: Replace and Split
def practice_3a_beginner():
    print("\n" + "="*50)
    print("Exercise 3a: Word Replacer (Beginner)")
    print("="*50)
    #given story
    story = "The cat sat on the cat mat. The cat was happy."
    print(f"Original Story: {story}")
    #Replace "cat" with "dog"
    dog_story = story.replace("cat", "dog")
    #Replace "mat" with "rug"
    final_story = dog_story.replace("mat", "rug")
    #Split the story into sentences (split on ". ")
    sentences = final_story.split(". ")
    print(f"After replacing cat: {dog_story}")
    print(f"Final story: {final_story}")
    print(f"Sentences: {sentences}")
practice_3a_beginner()

def practice_3b_intermediate():
    print("\n" + "="*50)
    print("Exercise 3b: CSV Processor (Intermediate)")
    print("="*50)
    #CSV data as strings
    csv_data = [
        "Alice,Smith,28,Teacher",
        "Bob,Jones,35,Engineer",
        "Carol,White,42,Doctor"
    ]
    print("Processing Employee Data:\n")
    employees = []
    for line in csv_data:
        #Split each line by commma
        fields = line.split(",")
        #Format "FirstName LastName (Age) - Job"
        if fields:
            formatted = f"{fields[0]} {fields[1]} ({fields[2]}) - {fields[3]}"
            employees.append(formatted)
    #Join all employees on new line
    employee_list = "\n".join(employees)
    print("Employee Directory:")
    print(employee_list)
practice_3b_intermediate()

def practice_3c_advanced():
    print("\n" + "="*50)
    print("Exercise 3c: Template System (Advanced)")
    print()


#Unit 4: String Formatting
#Old Style (% formatting)
name = "Alice"
age = 25
sentence = "My name is %s and I am %d years old" % (name, age)
#Format Method
name = "Alice"
age = 25
sentence = "My name is {} and I am {} years old".format(name, age)
    #With positional arguments
text = "{1} is {0} years old".format(name, age)
    #With named arguments
text = "{name} is {age} years old".format(name="Alice", age=25)
#F-strings
name = "Alice"
age = 25
text = f"My name is {name} and I am {age} years old" 
    #With expressions
text = f"Next year I will be {age + 1} years old"
#Formatting Numbers
#Controlling decimal places
price = 19.99523
formatted = f"${price:.2f}"  #$19.99 - 2 decimal places
percentage = 0.856
formatted = f"${price:.1%}"  #85.6% - as a percentage
large_num = 1234567
formatted = f"{large_num:,}" #1,234,567 - with commas
#Padding and Alignment
text = "Hi"
padded = f"{text:>10}"  #"        Hi" - right align in 10 chars
padded = f"{text:<10}"  #"Hi        " - left align in 10 chars
padded = f"{text:^10}"  #"    Hi    " - centered align text
padded = f"{text:*^10}" #"****Hi****" - centered and fill


#Student Practice: Formatting
def practice_4a_beginner():
    print("\n" + "="*50)
    print("Exercise 4a: Info Formatter (Beginner)")
    print("="*50)
    #Personal Info
    name = "John Doe"
    age = 25
    height = 5.9
    weight = 170.5
    #Create f-string with name and age // Format: "Name: John Doe, Age: 25"
    info1 = f"Name: {name}, Age: {age}"
    #Format height to one decimal place // Format: "Height: 5.9 feet"
    info2 = f"Height: {height:.1f} feet"
    #Format weight to no decimal place // Format: "Weight: 171 lbs"
    info3 = f"Weight: {weight:.0f} lbs"
    #print
    print(info1)
    print(info2)
    print(info3)
practice_4a_beginner() 

def practice_4b_intermediate():
    print("\n" + "="*50)
    print("Exercise 4b: Grade Report (Intermediate)")
    print("="*50)
    #Students info
    students = [
        {"name": "Alice", "score": 92.5, "grade": "A"},
        {"name": "Bob", "score": 78.3, "grade": "C"},
        {"name": "Charlie", "score": 85.7, "grade": "B"}
    ]
    #Print header
    print(f"{'Name':<15} {'Score':>10} {'Grade':>10}")
    print("-" * 35)
    for student in students:
        #Format name left-aligned in 15 characters
        name_formatted = f"{student['name']:<15}"
        #Format score right-aligned with 1 decimal
        score_formatted = f"{student['score']:>10.1f}"
        #Format grade right-aligned in 10 characters
        grade_formatted = f"{student['grade']:>10}"
        #Combine all formatted parts
        print(f"{name_formatted}{score_formatted}{grade_formatted}")
    #Calculate and display average
    avg_score = sum(s['score'] for s in students) / len(students)
    #Format average with 2 decimal places
    print("-"*35)
    print(f"Class average: {avg_score:.2f}")
practice_4b_intermediate()

def practice_4c_advanced():
    print("\n" + "="*50)
    print("Exercise 4c: Sales Data Table (Advanced)")
    print("="*50)
    #Sales Data
    sales_data = [
        {"product": "Laptop", "units": 15, "price": 899.99},
        {"product": "Mouse", "units": 45, "price": 29.99},
        {"product": "Keyboard", "units": 28, "price": 79.99},
        {"product": "Monitor", "units": 12, "price": 299.9},
        {"product": "USB Cable", "units": 67, "price": 9.99}
    ]
    #Create a Formatted Table
    #Calculate totals for each product
    for item in sales_data:
        item["total"] = item["units"] * item["price"]
    #Print Header
    print("┌" + "─"*50 + "┐")
    print(f"│{'SALES REPORT':^50}│")
    print("├" + "─"*50 + "┤")
    #Format column headers
    headers = f"│{'Product':<15}│{'Units':>8}│{'Price':>10}│{'Total':>12}│"
    print(headers)
    print("├" + "─"*15 + "┼" + "─"*8 + "┼" + "─"*10 + "┼" + "─"*12 + "┤")
    #Format each row
    grand_total = 0
    for item in sales_data:
        #Format each field
        row = f"│{item['product']:<15}│{item['units']:>8}│${item['price']:>9.2f}│${item['total']:>11.2f}│"
        print(row)
        grand_total += item["total"]
    #Print footer
    print("├" + "─"*15 + "┴" + "─"*8 + "┴" + "─"*10 + "┼" + "─"*12 + "┤")
    #Format grand total
    print(f"│{'Grand Total':>36}│${grand_total:>11.2f}│")
    print("└" + "─"*37 + "┴" + "─"*12 + "┘")
practice_4c_advanced()

#Unit 5: String Slicing and Indexing
#String Indexing
#Accessing individual characters
text = "python"
    #Positive indexing
text[0] #'p' - first character
text[1] #'y' - second character
text[2] #'t' - third character
    #Negative indexing
text[-1] #'n' - last character
text[-2] #'o' - second to last character
text[-6] #'p' - first character
#String Slicing
#Getting Substrings
text = "Hello World"
    #Basic slicing [start:end]
text[0:5]  #'Hello' - characters 0-4 (end not included)
text[6:11] #'World' - characters 6-10
    #Omitting indices
text[:5]   #'Hello' - from beginning to index 5
text[6:]   #'World' - from index 6 to end
text[:]    #'Hello World' - entire string
    #Step parameter [start:end:step]
text[::2]  #'HloWrd' - every second character
text[1::2] #'el ol' - every second starting at index 1
text[::-1] #'dlroW olleH' - reverse the sting

#Student Practice
def practice_5a_beginner():
    print("\n" + "="*50)
    print("Exercise 5a: String Extraction (Beginner)")
    print("="*50)
    #Full name
    full_name = "John Michael Smith"
    print(f"Full name: {full_name}")
    #Get first name (first 4 characters)
    first_name = full_name[:4]
    #Get last name (last 5 characters)
    last_name = full_name[-5:]
    #Email address
    email = "user@example.com"
    print(f"\nEmail: {email}")
    #Get username (before @)
    at_position = email.find("@")
    username = email[:at_position]
    #Get domain (after @)
    domain = email[at_position+1:]
    #Print
    print(f"\nExtracted from name:")
    print(f" First name: {first_name}")
    print(f" Last name: {last_name}")
    print(f"\nExtracted from email:")
    print(f" Username: {username}")
    print(f" Domain: {domain}")
practice_5a_beginner()

