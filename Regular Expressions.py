import re

#Unit 1: Introduction to Regular Expressions and Core Concepts
#re.search(pattern,text)

#Exercise 1a: Find the word "dog"
text = "The dog barked at the mailman"
pattern = "dog"
result = re.search(pattern, text)
if result:
    print("Found the dog!")
    
#Exercise 2a: Find "2024" and find its position
print("="*20)
text = "The year 2024 will be exciting"
pattern = "2024"
result = re.search(pattern, text)
#Search for 2024, print where it started and where it ended
if result:
    print(f"Match: {result.group()}")
    print(f"Start position: {result.start()}")
    print(f"End position: {result.end()}")

#Exercise 3a: Create a function that checks if a word exists in text
def word_exists(text, word):
    pattern = rf"\b{re.escape(word)}\b"
    return bool(re.search(pattern, text))
print("="*20)
print(word_exists("Hello world", "world"))  #print True
print(word_exists("Hello world", "python")) #print False

#Unit 2: Character Classes
#Basic Syntax
#[abc] = matches either 'a', 'b' or 'c'
#[0-9] = matches any digit 0-9
#[a-z] = matches any lowercase letter
#[A-Z] = matches any uppercase letter
#[a-zA-Z] = matches any letter
#[^abc] = mtaches any letter EXCEPT 'a', 'b' or 'c'
#[^0-9] = matches any non-digit character

#Exercise 1b: Match any vowel (a, e, i, o, u) in the text
text = "Hello World"
pattern = r"[aeiou]"
matches = re.findall(pattern, text.lower())
print("="*20)
print(f"Vowels found: {matches}")

#Exercise 2b: Find all hexadecimal digits (0-9, A-F, a-f)
text = "Color code: #FF5A2B"
pattern = r"[0-9A-Fa-f]"
matches =  re.findall(pattern, text)
print("="*20)
print(f"Color code: {matches}")

#Exercise 3b: Extract all non-alphabetic characters from text
text = "Hello World! 123"
pattern = r"[^A-Za-z]"
matches = re.findall(pattern, text)
print("="*20)
print(f"Non-alphabetic characters: {matches}")

#Unit 3: Shorthand Character Classes, Metacharacters & Quantifiers
#\d = [0-9]
#\D = [^0-9]
#\w = any word character [a-zA-Z0-9_]
#\W = [^a-zA-Z0-9_]
#\s = any whitespace
#\S = any non-whitespace
#Metacharacters
    #(.) = wildcard 
        #Matches ANY single character except newline
        #Like a blank tile in Scrabble
        #Example: a.c matches "abc", "a1c", "a c", etc.
    #(^) = start anchor
        #Matches the beginning of a string
        #Does NOT consume characters
        #Example: ^Hello matches "Hello world" but not "Say Hello
    #($) = end anchor
        #Matches the end of a string
        #Does NOT consume characters
        #Example: world$ matches "Hello world" but not "world peace"
#Combining Anchors
    #^Hello$ matches ONLY the exact string "Hello"
    #^\d+$ matches strings that contain ONLY digits
#Escaping Metacharacters
    #\ escapes it and will only match the literal character (\. only matches ".")
#Quantifiers
    #(*) = Zero or More
        #Matches 0 or more of the preceding character/group
        #ab*c matches "ac", "abc", "abbc", "abbbc", etc.
        #Always matches (even if 0 occurrences)
    #(+) = One or more
        #Matches 1 or more of the preceding character/group
        #ab+c matches "abc", "abbc", "abbbc" but NOT "ac"
        #Must have at least one occurrence
    #(?) = Zero or one (optional)
        #Matches 0 or 1 of the preceding character/group
        #colou?r matches both "color" and "colour"
        #Makes the preceding element optional
#Combining with Character Classes
    #\d* - Zero or more digits
    #\d+ - One or more digits (at least one required)
    #\d? - Zero or one digit (optional single digit
#Common Patterns:
    #\d+ - Whole numbers
    #\w+ - Words
    #\s* - Optional whitespace
    #.+ - Any non-empty string

#Exercise 1c: Count how many digits are in the text
text = "I have 2 cats and 3 dogs"
pattern = r"\d+" #one or more digits
matches = re.findall(pattern, text)
print("="*20)
print(f"All numbers: {matches}")

#Exercise 2c: Extract all "words" (continuous word characters)
text = "user@email.com has user_id=12345"
pattern = r"\w+"
matches = re.findall(pattern, text)
print("="*20)
print(f"Words: {matches}")

#Exercise 3c: Clean text by removing all non-word characters except spaces
text = "Hello! How are you? I'm fine... Thanks!"
matches = re.sub(r"[^\w\s]", "", text)
print("="*20)
print(f"Cleaned text: {matches}")

#Week 6: Unit 1: Metacharacters Repition {m, n}
#{m,n}
    #{n} - exactly "n" times
        #\d{4} matches exactly 4 digits (like a year)
        #[A-Z]{2} matches exactly 2 uppercase letters
    #{m,n} - Between m and n times (inclusive)
        #\d{2,4} matches 2, 3, or 4 digits
        #\w{3,8} matches words 3 to 8 characters long
    #{m,} - at least "m" times
        #\d{2,} matches 2 or more digits
        #a{3,} matches "aaa", "aaaa", etc.
    #{,n} - at most "n" times
        #\d{,3} matches 0, 1, 2, or 3 digits
#Relationship to Other Quantifiers
    #* = {0,}
    #+ = {1,}
    #? = {0,1}

#Exercise 1a - Match years (exactly 4 digits)
text = "Born in 1995, graduated 2017, now it's 24"
pattern = r"\d{4}"
matches = re.findall(pattern, text)
print("="*25)
print(f"Years found: {matches}")

#Exercise 2a - Validate hex color codes (#RGB or #RRGGBB)
colors = ["#FFF", "#FFFFFF", "#12AB56", "#GGG", "#12"]
pattern = r"#[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3}$" #$ = matches end of string/line
print("="*25)
for c in colors:
    matches = re.findall(pattern, c)
    print(f"Hex codes: {matches}")

#Exercise 3a - Extract and validate US Social Security Numbers
text = "SSN: 123-45-6789, Invalid: 12-345-6789, 123-4-5678"
pattern = r"\b\d{3}-\d{2}-\d{4}\b" #\b = boundary
results = re.findall(pattern, text)
print("="*25)
print(f"SSN: {results}")

#Week2: Unit 2: Grouping
#Basic Grouping Syntax
    #(abc)   = groups 'abc' as one unit
    #(abc)+  = one or more 'abc' sequences
    #(ab|cd) = either 'ab' or 'cd'
#Types of groups
    #Capturing groups (pattern)
        #Saves matched text for later use
        #Can be referenced by number
    #Non-Capturing Groups (?:pattern)
        #Groups without saving
#Nested groups - ((ab)+c)

#Exercise 1b - Match repeated words like "very very" or "really really"
text = "It's very very important and really really cool"
pattern = r"(\w+) \1"
matches = re.findall(pattern, text)
print("="*25)
print(f"Repeated words: {matches}")

#Exercise 2b - Extract date components (MM/DD/YYYY)
dates = ["12/25/2024", "01/01/2025", "13/40/2024"]
pattern = r"([01][0-9])\/([0-3][0-9])\/(\d{4})"
print("="*25)
for d in dates:
    matches = re.search(pattern, d)
    if matches != None:
        print(f"Matches: {matches.group(0)}")
    else:
        print(f"Invalid")

#Exercise 3b - Parse URLs: protocol://domain/path
urls = ["http://example.com/page", "https://site.org/path/to/file"]
pattern = r"(\w+)://([^/]+)/(.+)"
print("="*25)
for url in urls:
    matches = re.match(pattern, url)
    if matches:
        protocol, domain, path = matches.groups()
        print(f"URL: {url}")
        print(f"Protocol: {protocol}")
        print(f"Domain: {domain}")
        print(f"Path: {path}")

#Week 6: Unit 3: Capturing
#Accessing Captured Groups
    #By Index
        #group(0) = entire match
        #group(1) = first group
        #group(2) = second group, etc.
    #Named Groups
        #(?P<name>pattern)
        #access with group('name')

#Exercise 1c - Extract name and age from text
text = "My name is Alice and I am 25 years old"
pattern = r"name is (\w+) and I am (\d+)"
match = re.search(pattern, text)
print("="*25)
if match:
    print(f"Name: {match.group(1)}")
    print(f"Age: {match.group(2)}")

#Exercise 2c - Parse email addresses with named groups
emails = ["john.doe@company.com", "alice_smith@university.edu"]
pattern = r"(?P<user>[\w.]+)@(?P<domain>[\w.]+)"
print("="*25)
for email in emails:
    match = re.match(pattern, email)
    if match:
        print(f"Email: {email}")
        print(f"Username: {match.group('user')}")
        print(f"Domain: {match.group('domain')}")

#Exercise 3c - Extract and validate time in HH:MM:SS format
times = ["12:30:45", "25:00:00", "10:65:30", "09:15:22"]
pattern = r"^(?P<hour>[01]\d|2[0-3]):(?P<minute>[0-5]\d):(?P<second>[0-5]\d)$"
print("="*25)
for t in times:
    match = re.match(pattern, t)
    if match:
        print(f"{t} is valid: {match.groupdict()}")
    else:
        print(f"{t} is NOT valid")

#Week 6: Unit 4: Alternation
#| = or
#Important Concepts
    #Order Matters: regex tries left to right
        #cats|cat = will match "cats" in "cats" (not just "cat")
        #cat|cats = will match "cat" in "cats" (stops at first match)
    #Scope of Alternation
        #without grouping: affects entire pattern
        #with grouping: limited to group
        #^cat|dog$ = "starts with cat" OR "ends with dog"
        #^(cat|dog)$ = exactly "cat" or "dog"
    #Combining with Other Patterns
        #(Mr|Mrs|Ms)\.?\s+\w+ = titles with names
        #\.(jpg|jpeg|png|gif)$ = file extensions
        #(https?|ftp):// = URL protocols
    
#Exercise 4a: Match different greetings
text = "Hello there! Hi everyone. Hey you. Goodbye."
pattern = r"Hello|Hi|Hey"
matches = re.findall(pattern, text)
print("="*25)
print(f"Greetings found: {matches}")

#Exercise 4b: Validate file extensions for documents
files = ["report.doc", "image.jpg", "data.xlsx", "notes.txt"]
pattern = re.compile(r".+\.(docx?|pdf|txt)$", re.IGNORECASE)
print("="*25)
for f in files:
    if pattern.match(f):
        print(f"{f} is a valid extension")
    else:
        print(f"{f} is an invalid extension")

#Exercise 4c: Parse different date formats
dates = ["2024-01-15", "15/01/2024", "Jan 15, 2024", "January 15, 2024"]
pattern = re.compile(
    r"^("
     r"\d{4}-\d{2}-\d{2}"   #YYYY-MM-DD
     r"|"
     r"\d{2}/\d{2}/\d{4}"   #DD/MM/YYYY
     r"|"
     r"(?:[A-Z][a-z]{2}|) \d{1,2}, \d{4}"   #Mon DD, YYYY
     r")$"
)
print("="*25)
for d in dates:
    if pattern.match(d):
        print(f"{d} is a valid date")
    else:
        print(f"{d} is an invalid date")

#Week 6: Unit 5: Module re - Match Object
#Match Object Attributes and Methods
    #.group(n) - Return captured group n (0 = entire match)
    #.groups() - Return all captured groups as tuple
    #.start()  - Starting position of match
    #.end()    - Ending position of match
    #.span()   - Return (start, end) as tuple
    #.string   - The original string
    #.re       - The regex pattern used
#Multiple Groups
    #match.group()  = entire match
    #match.group(0) = entire match
    #match.group(1) = first group
    #match.group(2) = second group

#Exercise 5a: Find a number and print its position
text = "The temperature is 72 degrees"
pattern = r"\d+"
match = re.search(pattern, text)
print("="*25)
if match:
    print(f"Number's position: {match.span()}")
else:
    print(f"No match found")

#Exercise 5b: Extract URL components and their positions
url = "https://www.example.com/path/to/page"
pattern = r"(https?)://([^/]+)(.*)"
print("="*25)
match = re.search(pattern, url)
if match:
    print(f"Protocol: {match.group(1)}")
    print(f"Protocol position: {match.span(1)}")
    print(f"Domain: {match.group(2)}")
    print(f"Domain position: {match.span(2)}")
    print(f"Path: {match.group(3)}")
    print(f"Path position: {match.span(3)}")

#Exercise 5c: Build a function that returns match details as dictionary
print("="*25)
def get_match_info(text, pattern):
    match = re.search(pattern, text)
    if not match:
        return {
            "found": False,
            "match": None,
            "groups": (),
            "position": None,
            "before": None,
            "after": None,
        }
    start, end = match.span()
    return {
        "found": True,
        "match": match.group(0),
        "groups": match.groups(),
        "position": (start, end),
        "before": text[:start],
        "after": text[end:],
    }
text = "Price: $19.99 (discounted)"
pattern = r"\$(\d+)\.(\d{2})"
info = get_match_info(text, pattern)
print(info)

#Week 6: Unit 6: re.match() function
#re.match() - Only matches at the BEGINNING of string
#re.search() - Searches ANYWHERE in string
#When to use re.match()
    #Validating input format - Entire string must match pattern
    #Parsing structured data - Known format from start
    #Command parsing - Check if string starts with command
    #Protocol detection - URL starts with http/https
#Important Behavior
text = "Hello World"
re.match("World", text)  # Returns None (not at start)
re.search("World", text) # Returns Match object (found)
re.match("Hello", text)  # Returns Match object
re.search("Hello", text) # Also returns Match object
#Common Pattern
re.match("^Hello", text) # ^ is unnecessary
re.match("Hello", text)  # Same effect

#Exercise 6a: Check if string starts with "Hello"
print("="*25)
texts = ["Hello World", "Say Hello", "Hello", "HELLO"]
pattern = r"Hello"
for text in texts:
    if re.match(pattern, text):
        print(f"{text!r} starts with 'Hello'")   #!r makes the string start with ''
    else:
        print(f"{text!r} does not start with 'Hello'")

#Exercise 6b: Validate phone number format from start of string
print("="*25)
phones = ["(555) 123-4567", "555-123-4567", "Call 555-1234", "123-4567"]
pattern = re.compile(r"^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$")
for p in phones:
    if re.match(pattern, p):
        print(f"{p} is a valid number format")
    else:
        print(f"{p} is an invalid number format")

#Exercise 6c: Parse variable assignments
print("="*25)
assignments = ["x = 10", "name = 'John'", "flag = True", "= invalid", "no equals"]
pattern = re.compile(r"^([a-zA-Z_]\w*)\s*=\s*(.+)$")
for ass in assignments:
    match = pattern.match(ass)
    if match:
        var, val = match.groups()
        print(f"{ass} variable={var}, value={val}")
    else:
        print(f"{ass} is an invalid assignment")

#Week 6 Lecture 2: Unit 1: re.findall() function
#re.findall() - returns a list of ALL non-overlapping matches in the string
#Return Values
    #No groups in pattern: Returns list of matched strings
        re.findall(r"\d+", "12 cats, 5 dogs") # ['12', '5']
    #One group: Returns list of group contents
        re.findall(r"#(\w+)", "#tag1 #tag2") # ['tag1', 'tag2']
    #Multiple groups: Returns list of tuples
        re.findall(r"(\w+)=(\d+)", "x=5 y=10") # [('x', '5'), ('y', '10')]

#Exercise 1a: Find all capital letters in text
print("="*30)
text = "HTML and CSS are Not Programming Languages"
pattern = r"[A-Z]"
capitals = re.findall(pattern, text)
print(f"Capital letters: {capitals}")

#Exercise 1b: Extract all quoted strings from text
print("="*30)
text = 'He said "hello" and she replied "hi there" quietly'
pattern = r'"(.*?)"'
matches = re.findall(pattern, text)
print(f"Quoted phrases: {matches}")

#Exercise 1c: Parse log entries: [LEVEL] timestamp - message
print("="*30)
text = """
[INFO] 2024-01-15 10:30:15 - Server started
[ERROR] 2024-01-15 10:35:22 - Connection failed
[WARNING] 2024-01-15 10:40:00 - High memory usage
"""
log_pattern = r"\[(\w+)\]\s+([\d-]+\s[\d:]+)\s+-\s+(.+)"
    #\[(\w+)\]        = level inside brackets
    #s+               = whitespace
    #([\d-]+\s[\d:]+) = timestamp (YYYY-MM-DD HH:MM:SS)
    #\s+-\s+          = separator (-)
    #(.+)             = message
log = re.findall(log_pattern, text)
print(f"Parsed log entries: {log}")

#Week 6 Lecture 2: Unit 2: re.finditer() function
#re.finditer() = Returns an iterator of Match objects for all matches

#Exercise 2a: Find all words and their positions
print("="*30)
text = "The quick brown fox"
pattern = r"\w+"
for match in re.finditer(pattern, text):
    print(f"'{match.group()}' at positions {match.span()}")

#Exercise 2b: Find overlapping patterns (findall can't do this)
print("="*30)
text = "aaaa"
pattern = r"(?=(aa))"
matches = [(match.start(), match.group(1)) for match in re.finditer(pattern, text)]
print(matches)

#Exercise 2c: Build a concordance (word index with positions)
print("="*30)
text = "the cat and the dog and the bird"
pattern = r"\w+"
concordance = {}
for match in re.finditer(pattern, text):
    word = match.group()
    position = match.start()
    concordance.setdefault(word, []).append(position)
print(concordance)

# Week 6 Lecture 2: Unit 3: re.sub() function
#re.sub() =  Replaces occurrences of pattern with replacement
#re.sub(pattern, replacement, string, count=0, flags=0)
#Replacement Options:
    #Static string: re.sub(r"\d+", "X", text)
    #Backreferences: re.sub(r"(\w+) (\w+)", r"\2, \1", text)
    #Function: re.sub(r"\d+", lambda m: str(int(m.group())*2), text)
#Backreference Syntax:
    #\1, \2, etc. - Refer to captured groups
    #\g<1>, \g<2> - Alternative syntax
    #\g<name> - Named group reference

#Exercise 3a: Replace all spaces with underscores
print("="*30)
text = "Convert this to snake case"
pattern = r"\s"
replacement = "_"
result = re.sub(pattern, replacement, text)
print(f"Snake case: {result}")

#Exercise 3b: Mask email addresses (keep first letter and domain)
print("="*30)
text = "Contact john@example.com or mary@company.org"
pattern = r"\b(\w)\w*(@\w+\.\w+)"
replacement = r"\1***\2"
result = re.sub(pattern, replacement, text)
print(f"Censored emails: {result}")

#Exercise 3c: Convert markdown links to HTML
print("="*30)
text = "Check [Google](https://google.com) and [GitHub](https://github.com)"
pattern = r"\[(.+?)\]\((.+?)\)"
replacement = r'<a href="\2">\1</a>'
result = re.sub(pattern, replacement, text)
print(f"HTML text: {result}")

#Week 6 Lesson 2: Unit 4: Compilation
#re.compile() = creates a reusable pattern object

#Exercise 4a: Compile a pattern to find all words starting with 'c'
print("="*30)
text = "The cat chased the clever mouse carefully"
pattern = re.compile(r"c\w*")
matches = pattern.findall(text)
print(f"C words: {matches}")

#Exercise 4b: Create a validation class with compiled patterns
print("="*30)
class Validator:
    email = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
    phone = re.compile(r"^\d{10}$")
    zipcode = re.compile(r"^\d{5}$")
    @staticmethod
    def is_valid_email(text):
        return bool(Validator.email.match(text))
    def is_valid_phone(text):
        return bool(Validator.phone.match(text))
    def is_valid_zip(text):
        return bool(Validator.zipcode.match(text))
    
print(Validator.is_valid_email("john.doe@example.com"))
print(Validator.is_valid_email("not-areal-email"))
print(Validator.is_valid_phone("3172738255"))
print(Validator.is_valid_phone("1-800-273-8255"))
print(Validator.is_valid_zip("46036"))
print(Validator.is_valid_zip("460360"))

#Exercise 4c: Create a text processor with multiple compiled patterns
print("="*30)
class TextProcessor:
    def __init__(self):
        #urls to links
        self.URL = re.compile(r'\[(\w+)\]\((https?://\w+\.\w+)\)')
        #emails to masked
        self.email = re.compile(r"\w+@\w+\.\w+")
        #phone numbers to formatted
        self.phone = re.compile(r"\d{10}")
    def process(self, text):
        result = re.sub(self.URL, r'<a href="\2">\1</a>', text)
        result = re.sub(self.email, r'\1***\3', result)
        result = re.sub(self.phone, r"(\1) \2-\3", result)
        return result