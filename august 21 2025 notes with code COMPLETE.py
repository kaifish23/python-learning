#what is a Dictionary?
    #a dictionary is a mutable collection of key-value pairs
    #aka "associative arrays", "hash maps", or "hash tables"
    #implements an Abstract Data Type (ADT) called "mapping"
    #keys must be immutable and unique
    #values can be any data type and can be duplicated

#Abstract Data Type (ADT) Persepctive 
    #Insert(key, value): add a key-value pair
    #Lookup(key): retrieve value associated with key
    #Delete(key): remove key-value pair
    #Update(key, value): modify value for existing key

#Internal Implementation (Hash Table)
#Key > Hash Function > Index > Bucket > Value 

#Hash Function Properties
    #Deterministic: same key always produces the same hash
    #Uniform Distribution: minimizes collisions
        #collision: two hash keys equal same value
            #ex: key=1 / h("apple") = 1 & h("banana") = 1 also
            #to fix it: python uses a psuedorandom sequence; it would go to 1 then 20 then 13, etc. 
            #therefore making apple = 1, banana = 20, lime = 13, etc.
    #Fast Computation: O(1) time complexity

#Collision Resolution: python uses open addressing with random probing
    #1. if bucket is occupied, probe next question
    #2. use pseudorandom sequence to find alternative positions
    #3. maintains load factor < 2/3 to ensure performance

#Why use dictionaries? (Computational Complexity)

#Time Complexity Analysis
    #table header - operation / dictionary / list / sorted list
        #search / O(1) avg, O(n) worst / O(n) / O(log n)
        #insert /  O(1) avg, O(n) worst / O(1) append, O(n) insert / O(n)
        #delete /  O(1) avg, O(n) worst / O(n) / O(n)
        #update /  O(1) avg, O(n) worst / O(1) if index known / O(n)

#Space Complexity
    #Space: O(n) where n is number of key-value pairs
    #Load Factor: ratio of entries to available slots
    #Dynamic Resizing: automatically grows/shrinks to maintain performance

#Data Structure Property
    #Associative Property
        student_grades['Mathematics'] = 95 # type: ignore
        grades_list[0] = 95 # type: ignore
    #Uniqueness Constraint
        scores = {'Alice':85} 
        scores = ['Alice'] = 90 #overwrites previous value
        print(scores) #prints {'Alice':90}
    #Immutable Key Requirement
        valid_dict = {
            'string':1,        #string
            42:2,              #integer
            (1, 2, 3):3,       #tuple
            frozenset([1,2]):4 #frozensest
        }

#Memory Model and Performance
    #Memory Layout
        #Hash Table Array (buckets)
        #Key Objects (references)
        #Value Objects (references)
        #Metadata size (size, version, etc)
    #Dynamic Resizing Behavior
        import sys
        #observe memory growth
            d = {}
            for i in range(10):
                d[i]: i
                print(f"Size {len(d)}: {sys.getsizeof(d)} bytes")
                #output shows periodic jumps in hash table resizes
        

#Load Factor Impact
    #Low Load Factor: (< 0.5): wastes memory, fast lookup
    #Optimal Load Factor: (0.67): balance of speed and memory
    #High Load Factor (> 0.8): more collisions, slower operations


#Real World Analogies and Applications

#Computer Science Applications
    #Symbol Tables: variable names -> memory addresses in compilers
    #Caching: URLs -> cached web pages
    #Database Indexing: primary keys -> record locations
    #Routing Tables: IP addresses -> next hop destinations


#Creating Dictionaries
    #Literal Syntax (most common)
        empty_dict = {} #empty dictionary
        #dictionary with initial values
        student = {
            'name': 'Alice Johnson',
            'id': 12345,
            'gpa': 3.8,
            'major': 'Computer Science'
        }
        #mixed data types
        mixed_dict = {
            'string_key':'Hello',
            42:'Integer key',
            3.14:'Float key',
            True:'Boolean key'
        }
    #dict() constructor
        #from keyword arguements
            student = dict(name = 'Alice Johnson', id = 12345, gpa = 2.8)
        #from list of tuples
            grades = dict([('Math', 95), ('Science', 87), ('English', 92)])
        #from zip of two lists
            subjects = ['Math', 'Science', 'English']
            scores = [95, 87, 92]
            grade_dict = dict(zip(subjects, scores))
    #Dictionary Comprehension
        #creates dictionary of squares
            squares = {x: x**2 for x in range(1,6)}
                #result: {1:1, 2:4, 3:9, 4:16, 5:25}


#Accessing Dictionary Elements
    #Basic Access Using Keys
        #dictionary
            student = {
                'name':'Alice Johnson',
                'id':12345,
                'gpa':3.8,
                'major':'Computer Science'
            }
        #access values using keys
            print(student['name']) #ALice Johnson
            print(student['gpa']) #3.8
    #Safe Access Using get() Method
        #provide default value
            age = student.get('age', 20) #Returns 20
            print(f"Age: {age}") #prints Age: 20
        #compare with direct access
            name = student.get('name') #returns Alice Johnson
            print(name) #prints Alice Johnson
    #Checking if key exists
        #using 'in' operator (recommended)
            if 'name' in student:
                print(f"Student name: {student['name']}")
            if 'age' not in student:
                print(f"Age not specified")
        #alternative using get() with a sentinel value
            if student.get('age') is not None:
                print(f"Age: {student['age']}")


#Modifying Dictionaries
    #Adding New Key-Value Pairs
        student = {'name':'Alice', 'id':12345}
        #add new elements
            student['Major'] = 'Computer Science'
            student['gpa'] = 3.8
            print(student)
    #Updating Existing Values
        #update existing value
            student['gpa'] = 3.9
            print(f"Updated GPA: {student['gpa']}")
        #update multiple values at once
            student.update({'major':'Data Science','year':'Senior'})
            print(student)
    #Removing Elements
        #dictionary
            student = {
                'name':'Alice',
                'id':12345,
                'gpa':3.8,
                'major':'Computer Science'
            }
        #removing using "del" statement
            del student['major']
            print(student) #the 'major' key is removed
        #removing using pop() - returns the value
            gpa = student.pop('gpa')
            print(f"Removed GPA: {gpa}") #removed GPA: 3.8
        #pop() with default value
            year = student.pop('year','Not specified')
            print(f"Year: {year}") #Year: Not specified
        #remove and return arbitrary item
            item = student.popitem()
            print(f"Removed item: {item}")


#Dictionary vs List: Data Structure Analysis
    #Computational Complexity Comparison
        #table header - operation / dictionary / list / analysis
            #access by key/index / O(1) avg, O(n) worst / O(1) / dictionary amortized constant time
            #search by value / O(n) / O(n) / must check all entries
            #insert at end / O(1) avg, O(n) worst / O(1) amortized / both resize when needed
            #insert at position / N/A / O(n) / list must shift elements
            #delete by key/index / O(1) avg, O(n) worst / O(n) / list must shift after deletion
            #memory overhead / higher / low / dictionary needs hash table + keys
    #Structural Differences
        #Memory Layout
            #List: contiguous memory, sequential access
                list_memory = [value1, value2, value3]
            #Dictionary: hash table with key-value points
                dict_memory = {
                    hash(key1) % size #(key1, value1)
                    hash(key2) % size #(key2, value2)
                }
        #Access Patterns
            #List: positional access (must know position)
                grades = [85, 90, 78, 92] #what subject is index 2?
                math_grade = grades[2] #unclear without external mapping
            #Dictionary: semantic access (self-documenting)
                grades = {'Math':85, 'Science':90, 'English':78, 'History':92}
                math_grade = grades['Math'] #clear meaning
    #When to Use Each Data Structure
        #Lists:
            #Sequential Data: natural ordering matters
            #Indexed Access: need to access by position
            #Memory Efficiency: minimal overhead required
            #Mathematical Operations: vector/matrix computations
            #Stack/Queue Operations: LIFO/FIFO behavior (last/first in first out)
            #code examples
                temperatures = [20.1, 21.5, 19.8, 22.3] #time series data
                fibonacci = [0, 1, 1, 2, 3, 5, 8, 13] #sequential pattern
                rgb_color = [255, 128, 64] #ordered components
        #Dictionaries:
            #Key-Value Relationships: natural associations exist
            #Fast Lookups: need O(1) access by identifier
            #Sparse Data: not all possible indices used
            #Semantic Clarity: keys provide meaning
            #Configuration: named parameters/settings
            #code examples
                student_records = {'12345': {'name': 'Alice', 'gpa':3.8}} #id lookup
                word_counts = {'python':15, 'java':8, 'C++':12} #frequency
                config = {'debug':True, 'port':8080, 'timeout':30} #settings
        #Hybrid Approaches:
            #List of Dictionaries
                #when you need ordered collection of structured data
                    students = [
                        {'name': 'Alice', 'gpa': 3.8, 'major':'CS'},
                        {'name': 'Bob', 'gpa': 3.5, 'major':'Math'},
                        {'name': 'Carol', 'gpa': 3.9, 'major':'Physics'}
                    ] #Access: students[0]['name'] -> 'Alice'
            #Dictionary of Lists
                #when keys map to multiple related values
                    course_grades = {
                        'Alice': [95, 87, 92, 89],
                        'Bob' : [78, 85, 79, 90],
                        'Carol' : [92, 94, 88, 95]
                    } #Access: course_grades['Alice'][2] -> 92

#Valid Keys and Common Mistakes
    #Valid Key Types (Immutable Objects)
        valid_keys = {
            'string': 'string keys work',
            42: 'integer keys work',
            3.14: 'float keys work',
            True: 'boolean keys work',
            (1, 2): 'tuple keys work'
        } #invalid keys are list keys [1,2], dict keys {'a',1}, and set keys {1,2}
        
    
#Practical Examples
    #Example 1: Inventory System
        inventory = {
            'apples' = 50,
            'bananas'  = 30,
            'oranges' = 25
        }
        #check stock
        item = 'apples'
        if item in inventory:
            print(f"{item.title()}: {inventory[item]} in stock")
        else:
            print(f"{item.title()}: out of stock")
        #add new item
            inventory['grapes'] = 40
        #update existing item
            inventory['bananas'] += 10 #recieved shipment
            print("Current inventory: ", inventory)
    #Example 2: Grade Calculator
        def calculate_average(grades_dict):
            """Calculate average grade from a dictionary of subject grades"""
            if not grade_dict:
                return 0
            total = sum(grades_dict.values())
            count = len(grades_dict)
            return total/count
        student_grades = {
            'Math' = 95,
            'Science' = 87,
            'English' = 92,
            'History' = 89
        }
        average = calculate_average(student_grades)
        print(f"Average grade: {average:.2f}")
        #add new grade
        student_grades['Art'] = 94
        print(f"New average: {calculate_average(student_grades):.2f}")

