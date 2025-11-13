#Object-Oriented Programming Part I: Classes and Objects Fundamentals 
#Unit 1: What is Class?
    #A blueprint for creating objects
        #blueprint -> creates many houses
        #recipe    -> creates many cakes
        #class     -> creates many objects
    #Real World Example 
        #Student ID Card (Name, ID Number, Photo)
        #The ID Card template is a class, the actual ID Card is an object 
    #Definitions
        #Class: A template for creating objects
            #Defines what data an object can hold
            #Defines what actions an object can perform
        #Object: A specific instance created from a class
            #Has its own unique data
            #Can perform the actions defined by its class
    #Syntax
'''
    class Student:
        def __init__(self, name, student_id):
            self.name = name
            self.student_id = student_id
'''
        #class Student -> Creates a new class called Student
        #def __init__(self, name, student_id) -> Special method that runs when creating a new student
        #self.name = name -> Saves the name for this specific student
        #self.student_id = student_id -> Saves the ID for this specific student
    #Creating Objects
'''
    alice = Student("Alice Johnson", 12345) #Student 1
    bob = Student("Bob Smith", 12346)       #Student 2
    print(alice.name)                       #Prints: Alice Johnson
    print(bob.student_id)                   #Prints: 12346
'''
print("="*50)

#Practice Exercises
#Beginner - Create a Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
#test
my_book = Book("Python Basics", "Jane Doe")
print(my_book.title)
print("="*50)

#Intermediate - Add a display method
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

#Advanced: Create a Library
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
#create a library
library = []
#add at least 3 books to library
library.append(Book("Catharsis", "D. Andrew Campbell"))
library.append(Book("What Everyone Knows", "Liberty Sherron"))
library.append(Book("The Princess Bride", "William Goldman"))
#print the books
print("Books in the library:")
for book in library:
    print(f"- {book.title} by {book.author}")
print("="*50)

#Unit 2: Constructors, Instance Variables and Instance Methods
#Understanding init
    #__init__ Method
        #it's a conststructor
        #automatically runs when a new object is created
    #Self
        #Refers to the current object being made 
        #Links data and methods to specific objects
        #Passed automatically by Python
        #Allows each object to maintain its own state
#Instance Variables & Methods
    #Instance Variables
        #Variables that belong to each object
        #Each object gets its own copy
        #Defined using -> self.variable_name
        #Example
            #Each BankAccount has its own owner and balance
            #Changing one account's balance doesn't affect others
    #Instance Methods
        #Functions defined inside a class
        #Must have self as first parameter
        #Can access and modify instance variables
        
#Student Practice
#Beginner: Create a Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
#test
my_car = Car("Toyota", "Camry", 2020)
print(f"{my_car.year} {my_car.make} {my_car.model}")
print("="*50)

#Intermediate: Add mileage tracking
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
    def drive(self, miles):
        #add miles to mileage
        self.mileage += miles
        #print total mileage
        print(f"The {self.year} {self.make} {self.model} has driven {self.mileage} miles.")
#test
my_car = Car("Jeep", "Compass", 2008)
my_car.drive(98020)
print("="*50)

#Advanced: Fuel consumption
class Car:
    def __init__(self, make, model, year, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
        self.tank = 10
        self.mpg = mpg
        if self.mpg < 0:
            print("Error, car needs more than 0 miles")
    def drive(self, miles):
        if miles < 0:
            print("We can't drive on negative miles")
            return
        #calculate fuel level needed
        gas_needed = miles / self.mpg 
        if self.tank < gas_needed:
            print(f"Not enough gas to drive {miles} miles")
            return 
        self.mileage += miles
        self.tank -= gas_needed
#test
my_car = Car("Jeep", "Compass", 2008, 35)
my_car.drive(50)
print(f"The {my_car.year} {my_car.make} {my_car.model} has driven {my_car.mileage} miles and has {my_car.tank:.2f} gallons left.")
print("="*50)

#UNIT 3: Object Interactions
#Objects Working Together
    #Objects can interact with each other, just like in real life
        #A teacher has students
        #A shopping cart contains products
        #A team has players

#Student Practice
#Beginner: Teacher with students
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []
    #add method to add students
    def add_student(self, student):
        self.students.append(student)
        print(f"{student} has been added to {self.name}'s class.")
#test
teacher = Teacher("Mr. Johnson")
teacher.add_student("Alice")    
print(teacher.students)
print("="*50)

#Intermediate: Add/remove students
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []
        
    def add_student(self, student_name):
        self.students.append(student_name)
        print(f"{student_name} has been added to {self.name}'s class.")
        
    def remove_student(self, student_name):
        #check if student exists, if found, remove
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"{student_name} has been removed from {self.name}'s class.")
        else:
            print(f"{student_name} is not in {self.name}'s class.")
#test
teacher = Teacher("Mr. Johnson")
teacher.add_student("Alice")
teacher.add_student("Bob")
teacher.add_student("Charlie")
teacher.remove_student("Bob")
print(teacher.students)
print("="*50)

#Advanced: Grade tracking
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = {} #dict: name -> grade
    def add_student(self, name, initial_grade=0):
        self.students[name] = initial_grade
    def grade_student(self, name, grade):
        #update grade if student exists
        if name in self.students:
            self.students[name] = grade         
    def class_average(self):
        #calculate and return average grade
        if self.students != {}:
            return sum(self.students.values) / len(self.students)


#Unit 4: Destructor and Object Lifecyle
#Object Birth and Death
    #Birth: object created with __init__
    #Life: object used in program
    #Death: object destroyed when no longer needed
    #When Objects Die
        #When they go out of scope
        #When explicitly deleted with "del"
        #When program ends
        #When no more references exist
#The Destructor: __del__
    #Dunder Delete (double underscore del)
    #Purpose
        #It is called when an object is about to be "destroyed" (deleted) by Python's Garbage Collector
        #It's used for cleanup (like closing a file or network connection)
    #Practical Uses
        #closing files
        #releasing network connections
        #cleanup operations
        #logging
        
#Student Practice
#Beginner: Book class
class Book:
    def __init__(self, title):
        #take a book object, print its title, then delete it with del.
        self.title = title
        print(f"Book '{self.title}' has been created")
    def __del__(self):
        print(f"Book '{self.title}' is being deleted")
#test
my_book = Book("Wuthering Heights")
del my_book
print("="*50)

#Intermediate - Zoo and Animals
class Animal:
    def __init__(self, name):
        #Add 2 animals to zoo, print zoo list, then delete zoo
        self.name = name
        print(f"Animal {self.name} has been created")
    def __del__(self):
        print(f"Animal {self.name} has been deleted")
class Zoo:
    def __init__(self):
        self.animals = []
    def add(self, animal):
        self.animals.append(animal)
#test
zoo = Zoo()
zoo.add(Animal("Lion"))
zoo.add(Animal("Monkey"))
print([a.name for a in zoo.animals])
del zoo
print("="*25)

#Week 2 - Lecture 2 - Unit 1: Public vs Private Attributes
#Python's Privacy Mechanism
    #the "_" means private in naming conventions
        #self.public    = Not hidden at all
            #When to use: Public API, meant for external use
        #self._internal = Somewhat hidden
            #When to use: Internal use, subclasses OK
        #self.__private = Completely hidden
            #When to use: Really internal, even subclasses shouldn't access

#Student Practice
#Beginner - Person with private age
class Person:
    #Create Person class with private _age
    def __init__(self, name, age):
        self.name = name #public (.)
        self._age = age  #private (._)
        
    def get_age(self):
         #Return the private age
        return self._age
#test
person = Person("Bob", 25)
print(person.get_age())
print("="*25)

#Intermediate - Age Validation
class Person:
    #Add set_age() with validation
    def __init__(self, name, age):
        self.name = name #public (.)
        self._age = age  #private (._)
    def get_age(self):
         #Return the private age
        return self._age
    def set_age(self, new_age):
        #Only allow age between 0 and 150
        if 0 <= new_age <= 150:
            self._age = new_age
        else:
            print("Error: Age must be between 0 and 150.")
#test
person = Person("Alice", 25)
person.set_age(30)
print(person.get_age())
print("="*25)

#Advanced - SSN with masked display
class Person:
    #Store SSN privately, show only last 4 digits
    def __init__(self, name, ssn):
        self.name = name
        self._ssn = ssn  #private
    def get_masked_ssn(self):
        #Return like: ***-**-6789
        last_four = self._ssn[-4:]
        return f"***-**-{last_four}"
    def verify_ssn(self, ssn_to_check):
        #Return True if matches stored SSN
        return ssn_to_check == self._ssn

#Week 2 - Lecture 2 - Unit 2: Property Decorators
#The Magic @property
    #Properties let us use methods like they're variables. 
    #Without Properties (Clunky)
        #person.get_age()   ---> have to call method
        #person.set_age(30) ---> have to call method
    #With Properties (Natural)
        #person.age      ---> looks like a variable
        #person.age = 30 ---> looks like assignment
    #Properties let us use simple attribute syntax with validation
    #Benefits of properties
        #Clean syntax: Use like normal attributes
        #Backward compatible: Can add validation later
        #Computed properties: Calculate values on the fly
        #Lazy evaluation: Only compute when needed
    #When to use properties
        #Validation needed: Check values before setting
        #Computed values: Calculate on access
        #Lazy loading: Load data only when needed
        #Logging/Debugging: Track access to attributes
        #Type conversion: Ensure correct data type
    #When to NOT use properties
        #Simple storage: No validation needed
        #Heavy computation: Use methods instead
        #Side effects: Properties shouldn't modify other state
        #Complex parameters: Properties can't take arguments
        
#Student Practice
#Beginner - Rectangle area property
class Rectangle:
    #Make area a property (calculated)
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        area = self.width * self.height
        return area
#test
rect = Rectangle(5, 3)
print(rect.area)
print("="*25)

#Intermediate - Email domain property
class Email:
    #Extract domain from email
    def __init__(self, address):
        self.address = address
    @property
    def username(self):
        #Return part before @
        return self.address.split("@")[0]
    @property
    def domain(self):
        #Return part after @
        return self.address.split("@")[1]
#test
email = Email("alice@gmail.com")
print(email.username)
print(email.domain)
print("="*25)

#Advanced - Age from Birthdate
from datetime import datetime
class Person:
    #Calculate age from birthdate
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    @property
    def age(self):
        #Calculate age from birth_year
        current_year = datetime.now().year
        return current_year - self.birth_year
    @property
    def can_vote(self):
        # Return True if age >= 18
        return self.age >= 18
#test
person = Person("Bob", 2000)
print(f"Age: {person.age}")
print(f"Can vote: {person.can_vote}")
print("="*25)

#Week 2 - Lecture 2 - Unit 3: Getters and Setters
#Getters and Setters
    #Getter: A method used to get (read) the value of an attribute.
        #Ex: get_salary()
    #Setter: A method used to set (change/write) the value of an attribute.
        #This is where validation rules are put
        #@setter lets us control what happens when someone tries to change a property
        #When to use setters
            #Data validation
            #Data transformation
            #Side effects (like logging)

#Student Practice
#Beginner - Score with validation
class Score:
    #Create Score class (0-100 range)
    def __init__(self, value=0):
        self._value = 0
        self.value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        #Check if between 0 and 100
        if 0 <= new_value <= 100:
            self._value = new_value
            print(f"Value has been set to {self._value}")
        else:
            print("Error, value must be between 0 and 100")
#test
score = Score(85)
score.value = 95
score.value = 105
print("="*25)

#Intermediate - Username validation
import re
class Username:
    #Username with format checking
    def __init__(self, name):
        self._name = ""
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        #Check: 3-20 characters
        #Check: only letters, numbers, underscore
        if re.fullmatch(r"[A-Za-z0-9_]{3,20}", value):
            self._name = value
            print(f"Username has been set to: {self._name}")
        else:
            print("Error, username must be 3-20 characters and only certain characters")
#test
user = Username("alice_123")
user.name = "ab" 
user.name = "alice@123"
print("="*25)

#Advanced - Password with requirements
class Password:
    #Password with strength requirements
    def __init__(self):
        self._value = None 
    @property
    def value(self):
        #Never show actual password!
        return "*" * len(self._value) if self._value else None
    @value.setter
    def value(self, password):
        #Check: at least 8 characters
        if len(password) < 8:
            print("Error, password must be at least 8 characters long")
            return
        #Check: has uppercase, lowercase, and numbers
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        if not (has_upper and has_lower and has_digit):
            print("Error, password must have upper and lowercase and at least one digit")
            return
        #Store if valid
        self._value = password
        print("Password set successfully")
    def verify(self, password):
        return password == self._value

#Week 2 - Lecture 2 - Unit 4: Encapsulation Design Patterns
#Encapsulation
    #Encapsulation Principles
        #Hide implementation details
        #Expose only necessary interfaces
        #Protect object's internal state
        #Maintain invariants (rules that must always be true)
    #Design Guidelines
        #Make attributes private by default
        #Use properties for controlled access
        #Validate data in setters
        #Keep public interface simple and stable
    #Use Private Variables When
        #Data should not be changed directly
        #You need to validate changes
        #You want to track access
    #Use Properties When
        #You want natural syntax (no parentheses)
        #Values are calculated on-the-fly
        #You need backward compatibility
    #Complete Encapsulation Checklist
        #A. Private data with "__" or "_"
        #B. Properties for controlled access
        #C. Validation in setters
        #D. Computed properties for derived values
        #E. Public methods as interface
        #F. Private helper methods
        #G. No direct data access from outside
    #Design Process
        #1. Identify the data the class needs
        #2. Decide access levels (public/protected/private)
        #3. Create properties for controlled access
        #4. Add validation where needed
        #5. Hide complexity with private methods
        #6. Provide clean public interface
    #Why Hide Information
        #Reduce Complexity: Users don't need to know internals
        #Prevent Misuse: Can't break what you can't touch
        #Enable Changes: Internal implementation can change
        #Maintain Invariants: Ensure data stays valid

#Student Practice
#Beginner - Inventory manager
class Inventory:
    #Create Inventory with protected stock
    def __init__(self, product_name):
        self.product_name = product_name
        self._stock = 0
    @property
    def stock(self):
        #Return current stock
        return self._stock
    def add_stock(self, quantity):
        #Add to stock if quantity > 0
        if quantity > 0:
            self._stock += quantity
            print(f"Added {quantity} units. Current stock: {self._stock}")
        else:
            print("Error, quantity must be higher than 0")
    def remove_stock(self, quantity):
        #Remove if enough stock
        if quantity > self._stock:
            print(f"Error, Not enough stock to remove {quantity} units.")
        elif quantity <= 0:
            print("Error, Quantity must be positive.")
        else:
            self._stock -= quantity
            print(f"Removed {quantity} units. Current stock: {self._stock}")
#test
inv = Inventory("Widgets")
inv.add_stock(100)
inv.remove_stock(30)
print(f"Stock: {inv.stock}")
print("="*25)

#Intermediate - Low stock warnings
class Inventory:
    #Add low stock warnings
    def __init__(self, product_name, reorder_point=10):
        self.product_name = product_name
        self._stock = 0
        self.reorder_point = reorder_point
    @property
    def needs_reorder(self):
        #Return True if stock below reorder_point
        return self._stock < self.reorder_point
    def add_stock(self, quantity):
        #Add to stock if quantity > 0
        if quantity > 0:
            self._stock += quantity
            print(f"Added {quantity} units. Current stock: {self._stock}")
        else:
            print("Error, quantity must be higher than 0")
    def remove_stock(self, quantity):
        #Remove if enough stock
        if quantity > self._stock:
            print(f"Error, Not enough stock to remove {quantity} units.")
        elif quantity <= 0:
            print("Error, Quantity must be positive.")
        else:
            self._stock -= quantity
            print(f"Removed {quantity} units. Current stock: {self._stock}")

#Advanced - Transaction history
from datetime import datetime 
class Inventory:
    #Track all inventory changes
    def __init__(self, product_name):
        self.product_name = product_name
        self._stock = 0
        self._history = []
    @property
    def stock(self):
        return self._stock
    @property
    def history(self):
        #Return copy of history
        return self._history.copy()
    def add_stock(self, quantity, reason=""):
        #Add stock and record in history
        #Include timestamp, action, quantity, reason
        if quantity <= 0:
            print("Error, quantity must be positive.")
            return
        self._stock += quantity
        entry = {
            "timestamp": datetime.now(),
             "action": "add",
             "quantity": quantity,
             "reason": reason
        }
        self._history.append(entry)
        print(f"Added {quantity} units. Current stock: {self._stock}")
    def get_history_summary(self):
        summary = []
        for entry in self._history:
            time = entry["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            action = entry["action"]
            quantity = entry["quantity"]
            reason = entry["reason"]
            summary.append(f"{time} - {action} {quantity} units. Reason : {reason}")
            return "\n".join(summary)

#Week 2 - Lecture 3 - Unit 1: Inheritance
#Inheritance
    #Definitions
        #Base/Parent:       the class being inherited from
            #ex: Animal
        #Derived/Child:     the class that inherits
            #ex: dog, cat, bird
        #IS-A Relationship: child IS-A type of parent
            #ex: dog IS-A animal (✓)
            #ex: cat IS-A animal (✓)
            #ex: animal IS-A dog (X)
    #Why use Inheritance?
        #Code Reuse:           Don't repeat yourself (DRY principle)
        #Logical Organization: Model real-world relationships
        #Extensibility:        Add features without changing original
        #Polymorphism:         Treat related objects uniformly
        
#Student Practice
#Beginner - Vehicle and Car
class Vehicle:
    #Create Vehicle base class and Car derived class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def start(self):
        print(f"{self.brand} {self.model} is starting")
        
class Car(Vehicle):
    #Create Car class that inherits from Vehicle
    def honk(self):
        print("Beep Beep!!")
#test
my_car = Car("Toyota", "Camry")
my_car.start()
my_car.honk()
print("="*25)

#Intermediate - Add Truck and Motorcycle
class Vehicle:
    #Create multiple vehicle types
    def __init__(self, brand, model, wheels):
        self.brand = brand
        self.model = model
        self.wheels = wheels
    def start(self):
        print(f"{self.brand} {self.model} is starting")

class Car(Vehicle):
    def __init__(self, brand, model):
        #cars have 4 wheels
        Vehicle.__init__(self, brand, model, 4)

class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        Vehicle.__init__(self, model, brand, 2)
#test
car = Car("Honda", "Civic")
bike = Motorcycle("Harley-Davidson", "Street Glide")
car.start()
bike.start()
print("="*25)

#Advanced - Registration System
class Vehicle:
    vehicle_count = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.registrationid = None
        Vehicle.vehicle_count += 1
    def register(self, state):
        self.registration_id = f"{state.upper()}-{Vehicle.vehicle_count:05d}"
        print(f"{self.brand} {self.model} registered as {self.registration_id}.")

class Car(Vehicle):
    def __init__(self, brand, model, doors=4):
        Vehicle.__init__(self, brand, model)
        self.doors = doors
    def honk(self):
        print("Beep Beep!!")

class Truck(Vehicle):
    def __init__(self, brand, model, cargo_capacity):
        Vehicle.__init__(self, brand, model)
        self.cargo_capacity = cargo_capacity
    def load_cargo(self, weight):
        if weight <= self.cargo_capacity:
            print(f"Loaded {weight} tons of cargo into {self.brand} {self.model}")
        else:
            print(f"Cannot load {weight} tons, capacity is only {self.cargo_capacity} tons")
#test
car = Car("Jeep", "Cherokee")
truck = Truck("Ford", "F-150", 1400)
car.register("MI")
truck.register("CA")
car.honk()
truck.load_cargo(1600)
truck.load_cargo(800)
print("="*25)

#Week 2 - Lecture 3 - Unit 2: Method Overriding
#Overriding 
    #Types of Overriding
        #Complete Override - Replace Entirely
        #Extension         - Add to Parenet Behavior
        #Modification      - Change Part of Behavior
    #Override Rules
        #Method name must match exactly
        #Can change implementation completely
        #Can call parent with super()
        #Should maintain the expected interface
        #Can have different behavior
        
#Student Practice
#Beginner - Shape Areas
class Shape:
    #Override area calculation
    def __init__(self, name):
        self.name = name
    def area(self):
        return 0 #base shape has no area

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    def area(self):
        #override to return width * height
        return self.width * self.height
#test
rect = Rectangle(5,3)
print(f"Area: {rect.area()}")
print("="*25)

#Intermediate - Student Grades
class Student:
    #Different grading for different students
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def calculate_grade(self):
        #regular grading
        if self.score >= 90: return "A"
        if self.score >= 80: return "B"
        if self.score >= 70: return "C"
        if self.score >= 60: return "D"
        else: return "F"
    
class Honors(Student):
    def __init__(self, name, score):
        super().__init__(name, score)
    def calculate_grade(self):
        if self.score >= 95: return "A+"
        if self.score >= 85: return "B+"
        if self.score >= 75: return "C+"
        if self.score >= 65: return "D+"
        else: return "F"
#test
reg = Student("Alice", 88)
honors = Honors("John", 96)
print(f"{reg.name}: {reg.calculate_grade()} (Regular Student)")
print(f"{honors.name}: {honors.calculate_grade()} (Honors Student)")
print("="*25)

#Advanced - Game Characters
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
    def attack(self):
        return 10 #base dmg
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} of damage!")
        
class Warrior(Character):
    def __init__(self, name, health):
        super().__init__(name, health)
    def attack(self):
        #do 2x dmg
        damage = super().attack() * 2
        print(f"{self.name} swings their sword for {damage} damage!")
        return damage
    def take_damage(self, amount):
        #reduce dmg by 3 (armor)
        reduced = max(0, amount - 3)
        super().take_damage(reduced)

class Mage(Character):
    def __init__(self, name, health, mana):
        #initialize parent AND mana
        super().__init__(name, health)
        self.mana = mana
    def attack(self):
        #if mana, 3x dmg, else normal
        base_damage = super().attack()
        if self.mana > 0:
            self.mana -= 10
            damage = base_damage * 3
            print(f"{self.name} casts a spell for {damage} damage! (Mana left: {self.mana})")
            return damage
        else:
            print(f"{self.name} is out of mana and does a normal attack for {base_damage} damage!")
            return base_damage
#test
warrior = Warrior("Thor", 100)
mage = Mage("Wanda", 80, 30)
damage = warrior.attack()
mage.take_damage(damage)
damage = mage.attack()
warrior.take_damage(damage)
damage = mage.attack()
warrior.take_damage(damage)
print("\n Final Health:")
print(f"{warrior.name} health: {warrior.health}/{warrior.max_health}")
print(f"{mage.name} health: {mage.health}/{mage.max_health}")
print("="*25)

#Week 2 - Lecture 3 - Unit 3: Using super()
#super()
    #Why use it?
        #Avoid Repetition: reuse parent code
        #Maintain Inheritance Chain: proper initialization
        #Future-proof: parent changes automatically included
        #Multiple Inheritance: handles complex heirarchies
        #Let's you use the parent method for child class
    #Common super() Patterns
        #Extending __init__
        #Extending Methods
        #Wrapping Parent Behavior
    #super() vs Direct Parent Call
        #super(): flexible, maintains inheritance (good)
        #Direct Parent Call: brittle, breaks with changes (bad)
        
#Student Practice
#Beginner - SportsCar from Car
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    def accelerate(self):
        self.speed += 10
        print(f"Speed: {self.speed} mph")
        
class SportsCar(Car):
    def __init__(self, brand, model, year, turbo):
        super().__init__(brand, model, year)
        self.turbo = turbo
    def accelerate(self):
        if self.turbo:
            self.speed += 20
            print(f"{self.brand} {self.model} (Turbo ON) speed: {self.speed} mph")
        else:
            super().accelerate()
#test
ferrari = SportsCar("Ferrari", "488", 2023, True)
ferrari.accelerate()
print("="*25)

#Intermediate - Graduate Student
class Student:
    def __init__(self, name, student_id):
        self.name = name 
        self.student_id = student_id
        self.courses = []
        self.gpa = 0.0
    def enroll(self, course):
        self.courses.append(course)
        print(f"Student enrolled in {course}")
        
class Graduate(Student):
    def __init__(self, name, student_id, thesis):
        super().__init__(name, student_id)
        self.thesis = thesis
        self.advisor = None
    def set_advisor(self, advisor_name):
        self.advisor = advisor_name
        print(f"{self.name}'s advisor set to {advisor_name}")
    def enroll(self, course):
        #grad students can only take lvl 500+ courses, check course num
        digits = ''.join([c for c in course if c.isdigit()])
        if digits and int(digits) >= 500:
            self.courses.append(course)
            print(f"{self.name} enrolled in graduate course {course}")
        else:
            print(f"Error: Graduate students cannot take lower-level course {course}")

#Week 3 - Lecture 4 - Unit 1: Polymorphism
#Introduction to Polymorphism
    #What is it?
        #Poly = many, Morph = forms
        #Objects of different types can be used interchangeably
    #Types of Polymorphism
        #Method Overriding: Child classes provide own implementation
        #Method Overloading: Same method name, different parameters
        #Operator Overloading: Operators work with custom objects
        #Duck Typing: If it walks like a duck and quacks like a duck...
    #Why use it?
        #Flexibility: Add new types without changing existing code
        #Maintainability: Single interface for multiple implementations
        #Extensibility: Easy to add new classes
        #Clean Code: Reduces if/elif chains

#Student Practice
#Beginner - Shapes Drawing
class Shape:
    #Different shapes, same draw() method
    def __init__(self, color):
        self.color = color
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return f"Drawing a {self.color} circle"

class Square(Shape):
    def draw(self):
        return f"Drawing a {self.color} square"

#test
shape = [Circle("red"), Square("blue"), Circle("green")]
for s in shape:
    print(s.draw())
print("="*25)

#Intermediate - Payment Processing
class Payment:
    #Different payment methods
    def __init__(self, amount):
        self.amount = amount
    def process(self):
        pass

class CreditCard(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    def process(self):
        return f"Processing ${self.amount} via credit card ending in {self.card_number}"

class PayPal(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email
    def process(self):
        return f"Prcoessing ${self.amount} via PayPal account {self.email}"

#Advanced - File Formats
class FileHandler:
    #Save/load for different file types
    def __init__(self, filename):
        self.filename = filename
        self.data = None
    def save(self, content):
        self.content = content
    def load(self):
        pass
    
class TextFile(FileHandler):
    def save(self, content):
        print("Saving text to file")
        self.data = content
    def load(self):
        return self.data
    
#Week 3 - Lecture 4 - Unit 2: Abstract Base Classes
#Abstract Base Classes
    #Enforcing the Contract
        #Sometimes we want to force child classes to implement certain methods
        #Abstract classes are like contracts
    #Abstract Base Class (ABC)
        #A class that cannot be instantiated and defines methods that must be implemented by subclasses
    #Why use ABCs?
        #Enforce contracts: Subclasses must implement certain methods
        #Prevent errors: Can't forget to implement required methods
        #Documentation: Clear about what subclasses must provide
        #Type safety: Better for type checking
    #ABC Rules
        #Import from "abc" module
        #Inherit from "ABC"
        #Use "@abstractmethod" decorator
        #Subclasses must implement all abstract methods
        #Can have concrete methods too
        
#Student Practice
#Beginner - Abstract Vehicle
from abc import ABC, abstractmethod
class Vehicle(ABC):
    #Create abstract Vehicle class
    def __init__(self, brand):
        self.brand = brand
    @abstractmethod
    def start(self):
        #this forces all vehicles to have start()
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine is starting..."
    
#test
car = Car("Toyota")
print(car.start())
print("="*25)

#Intermediate - Database connections
from abc import ABC, abstractmethod
class Database(ABC):
    #Abstract database interface
    def __init__(self, host):
        self.host = host
        self.connected = False
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
    @abstractmethod
    def execute_query(self):
        pass

class MySQL(Database):
    def connect(self):
        self.connected = True
        return f"Connected to MySQL database at {self.host}"
    def disconnect(self):
        self.connected = False
        return f"Disconnected from MySQL database"
    def execute_query(self, query):
        if not self.connected:
            return "Error: Not Connected to MySQL"
        return f"MySQL executing: {query}"

class Postgres(Database):
    def connect(self):
        self.connected = True
        return f"Connected to PostgreSQL database at {self.host}"
    def disconnect(self):
        self.connected = False
        return "Disconnected from PostgreSQL database"
    def execute_query(self, query):
        if not self.connected:
            return "Error: Not connected to PostgreSQL"
        return f"PostgreSQL executing: {query}"

#test
mysql = MySQL("localhost")
print(mysql.connect())
print(mysql.execute_query("SELECT * FROM users"))
print(mysql.disconnect())
print()
post = Postgres("127.0.0.1")
print(post.connect())
print(post.execute_query("SELECT * FROM products"))
print(post.disconnect())
print("="*25)

#Advanced - Plugin System
from abc import ABC, abstractmethod
class Plugin(ABC):
    #Create plugin architecture
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.enabled = False
    @abstractmethod
    def activate(self):
        #Called when Plugin is enabled
        pass
    @abstractmethod
    def deactivate(self):
        #Called when Plugin is disabled
        pass
    @abstractmethod
    def process(self, data):
        #Main plugs functionality
        pass

class SpellChecker(Plugin):
    def activate(self):
        self.enabled = True
        print(f"{self.name} v{self.version} activated")
    def deactivate(self):
        self.enabled = False
        print(f"{self.name} deactivated.")
    def process(self, data):
        if not self.enabled:
            return "Error: Plugin not active."
        corrected = data.replace("teh", "the")
        return f"Spell-checked text: {corrected}"

#test
spell = SpellChecker("SpellerPro", "1.0")
spell.activate()
print(spell.process("This is teh best plugin system!"))
spell.deactivate()
print("="*25)

#Week 3 - Lecture 4 - Unit 3: Duck Typing
#Duck Typing
    #Duck Typing Principles
        #No type checking: Python doesn't care about class
        #Method presence: Only cares if method exists
        #Runtime checking: Errors happen when method called
        #Maximum flexibility: Any object with right methods works
    #Pros and Cons
        #Pros:
            #Very flexible
            #No inheritance required
            #Simple and pythonic
            #Encourages clean interface
        #Cons:
            #Errors at runtime, not compile time
            #Less explicit contracts
            #Can be confusing
            #Harder to document

#Student Practice
#Beginner - Compatible Interfaces
class Calculator:
    #Create objects with compatible methods
    def compute(self, x, y):
        return x + y
    
class ScientificCalc:
    #No inheritance!
    def compute(self, x, y):
        return x * y

def process_num(processor, a, b):
    result = processor.compute(a, b)
    print(f"Result: {result}")

#test
basic = Calculator()
scientific = ScientificCalc()
process_num(basic, 3, 5)
process_num(scientific, 3, 5)
print("="*25)

#Week 3 - Lecture 4 - Unit 4: Interface Design Patterns
#Interface Design Patterns
    #Interface
        #A contract that defines what methods a class must have
            #In Python: Informal (duck typing) or formal (ABC)
            #Defines the "what" not the "how"
    #Common Patterns
        #Iterator: Provides way to traverse collection
        #Context Manager: Manages resources (with statement)
        #Callable: Object that can be called like function
        #Comparable: Objects that can be compared
    #Designing Good Interfaces
        #Small and focused: Single responsibility
        #Consistent naming: Similar operations, similar names
        #Minimal: Only essential methods
        #Clear contracts: Well-documented behavior
        #Stable: Don't change frequently

#Student Practice
#Beginner - Notification Strategies
class Notification:
    def notify(self, message):
        pass
        
class EmailNotif(Notification):
    def notify(self, message):
        print(f"Email sent: {message}")

class TextNotif(Notification):
    def notify(self, message):
        print(f"Text sent: {message}")
        
class App:
    def __init__(self, notifier):
        self.notifier = notifier
    def alert_user(self, message):
        self.notifier.notify(message)

#test
email_notifier = EmailNotif()
sms_notifier = TextNotif()
app1 = App(email_notifier)
app2 = App(sms_notifier)
app1.alert_user("You have a new message!")
app2.alert_user("Your verification code is 1234.")
print("="*25)

#Week 4 - Lecture 5 - Unit 1: Class Methods
#Methods for the class
    #Bound to the class, not the instance
    #Use @classmethod decorator
    #First parameter is "cls"
#When to use Class Methods
    #Alternative ways to create objects
    #Working with class-level data
    #Factory methods (creating objects)
    #Operations that affect the entire class
    #When you need access to class but not instance
#Key Points
    #Called on class: ClassName.method()
    #Can also be called on instances
    #Inherited by subclasses

#Student Practice
#Beginner - Person from birth year
from datetime import datetime
class Person:
    #create person with from_birth_year class method
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_birth_year(cls, name, birth_year):
        #calculate age from birth_year
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(name, age)
#test
person = Person.from_birth_year("Alice", 2000)
print(f"{person.name} is {person.age} years old")
print("="*25)

#Intermediate - Config from File
import json
class Config:
    #load configuration from different sources
    def __init__(self, host, port, debug):
        self.host = host
        self.port = port
        self.debug = debug
    @classmethod
    def from_json_string(cls, json_str):
        #parse json-like string
        json_str = json_str.replace("'", '"')
        data = json.loads(json_str)
        return cls(data["host"], data["port"], data["debug"])
    @classmethod
    def default_config(cls):
        #return config with default values
        return cls("localhost", 8080, False)
    def __str__(self):
        return f"Config(host={self.host}, port={self.port}, debug={self.debug})"
#test
json_str = "{'host': '127.0.0.1', 'port': 5000, 'debug': true}"
config1 = Config.from_json_string(json_str)
print(config1)
config2 = Config.default_config()
print(config2)
print("="*25)

#Advanced - Database Model
class User:
    user_count = 0
    #create model that loads from database
    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1
    @classmethod
    def from_database_row(cls, row):
        #row is a tuple
        username, email = row
        return cls(username, email)
    @classmethod
    def create_guest(cls):
        #create guest user with generated names
        guest_name = f"guest_{cls.user_count + 1:03}"
        guest_email = f"{guest_name}@example.com"
        return cls(guest_name, guest_email)
    @classmethod
    def get_total_users(cls):
        return cls.user_count
    def __str__(self):
        return f"User(username='{self.username}', email='{self.email}')"
#test
user1 = User.from_database_row(('alice', 'alice@email.com'))
print(user1)
guest1 = User.create_guest()
guest2 = User.create_guest()
print(guest1)
print(guest2)
print("Total users:", User.get_total_users())
print("="*25)

#Week 4 - Lecture 5 - Unit 2: Static Methods
#Static Method
    #Not bound to class or instance
    #Takes no required parameters like "self" or "cls"
    #Is decorated with @staticmethod
    #Is a function that belongs logically to the class but does not interact with the data (self, cls)
#When to use Static Methods?
    #Utility functions related to the class
    #Operations that don't need class or instance data like validation functions
    #Helper methods that don't need object data
#Key Points
    #Called on class or instance
    #Cannot access class or instance variables
    #Good for organization
    
#Student Practice
#Beginner - Email Validator
class EmailValidator:
    #create static email validation
    @staticmethod
    def is_valid_email(email):
        #check has @ and .
        if "@" in email:
            return True
        parts = email.split('@')
        if len(parts) != 2:
            return False
    @staticmethod
    def get_domain(email):
        #return part after @ or None if invalid
        if not EmailValidator.is_valid_email(email):
            return None
        return email.split("@")[1]
#test
print(EmailValidator.is_valid_email("test@gmail.com"))
print(EmailValidator.get_domain("user@example.org"))
print("="*25)

#Intermediate - File Utilities
class FileHelper:
    #File Helper static methods
    @staticmethod
    def get_extension(filename):
        #return file extension (after ".")
        if "." in filename:
            return filename.split(".")[-1].lower()
        return ""
    @staticmethod
    def is_image(filename):
        #check if jpg, png, gif
        ext = FileHelper.get_extension(filename)
        return ext in ("jpg", "png", "gif")
    @staticmethod
    def make_safe_filename(text):
        #replace spaces with underscore
        #remove special characters
        safe = ""
        for char in text:
            if char.isalnum() or char in ("_", "-", "."):
                safe += char
            elif char == " ":
                safe += "_"
        return safe
#test
print(FileHelper.get_extension("photo.png"))
print(FileHelper.is_image("holiday.jpg"))
print(FileHelper.is_image("report.pdf"))
print(FileHelper.make_safe_filename("My File @ 2025!.jpg"))
print("="*25)

#Week 4 - Lecture 5 - Unit 3: Method Types Comparison
#Three Types of Methods
    #Instance Methods
        #Needs instance data, use "self"
        #You need "self" (object's data)
        #Different for each object
        #Most common method
    #Class Methods
        #Needs class data, use "cls"
        #You need "cls" (the class itself)
        #Alternative constructors
        #Working with class variables
    #Static Methods
        #Need neither, no special parameters
        #Don't need "self" OR "cls"
        #Utility/helper functions
        #Could be standalone but related to class
#Memory Considerations
    #Feature | Instance Method | Class Method | Static Method
        #First Arg  | self                     | cls               | none
        #Access     | instance attributes      | class variables   | neither
        #Use case   | Object-specific behavior | alt. constructors | utility/helper functions
        #Decoration | None                     | @classmethod      | @staticmethod

#Student Practice
#Beginner - Mixed Methods
class Temperature:
    #create class with all 3 types
    #Instance (self)
    def __init__(self, celsius):
        self.celsius = celsius
    def to_fahrenheit(self):
        #convert C to F
        return self.celsius * 9/5 + 32
    #Class Method
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        #convert F to C
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)
    #Static Method
    @staticmethod
    def is_freezing(celsius):
        return celsius <= 0
#test
temp1 = Temperature(0)
print(temp1.to_fahrenheit())                
print(Temperature.is_freezing(temp1.celsius)) 
temp2 = Temperature.from_fahrenheit(212)
print(temp2.celsius)                        
print(temp2.to_fahrenheit())              
print("="*25)

#Intermediate - User System
class User:
    #user management with mixed methods
    all_users = []
    def __init__(self, username):
        self.username = username
        self.logged_in = False
        User.all_users.append(self)
    #Instance method
    def login(self, password):
        #set logged_in to True if password is "secret"
        if password == "secret":
            self.logged_in = True
        else:
            print("Wrong password")
    #Class Method
    @classmethod
    def get_active_users(cls):
        #return list of logged-in users
        return [user.username for user in cls.all_users if user.logged_in]
    #Static Method
    @staticmethod
    def validate_username(username):
        #check 3-20 chars, alphanumeric only
        return 3 <= len(username) <= 20 and username.isalnum()
#test
print(User.validate_username("Kai123"))
user1 = User("Alice")
user2 = User("Bob")
user1.login("secret")
user2.login("secret")
print(User.get_active_users())
print("="*25)

#Week 4 - Lecture 5 - Unit 4: Factory Method Pattern
#Factory Method
    #Problem: the "__init__" must always take a fixed set of arguments. What if you want diff formats?
    #Solution: Factory Method is a class method that creates and returns an instance of the class
    #Naming Convention: starts with "from_" (eg from_string, from_dict, etc.)
#Factory Pattern
    #Creational pattern for creating objects
    #Centralize object creation logic
    #Hide implementation details from client
    #Can return different subclasses based on input
#Types of Factories
    #Factory Methods: Class methods that create objects
    #Static Factory Methods: Static Methods for object creation
    #Alternative Constructors: Multiple ways to create same object type

#Student Practice
#Beginner - Animal Factory
class Animal:
    #create animal factory
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            print("Unknown animal type")
            return None
#test
pet1 = AnimalFactory.create_animal("dog")
pet2= AnimalFactory.create_animal("cat")
print(pet1.speak())
print(pet2.speak())
print("="*25)

#Week 4 - Lecture 6 - Unit 1: Essential Magic Methods
#Magic Methods
    #AKA "Dunder" methods
    #Special Methods: Methods that have double underscores at the start and end
    #Purpose: They allow your objects to integrate seamlessly with built-in Python language features
    #Example: When you call "len(my_list)", Python is secretly calling the "my_list.__len__()" method
    #Most Important Methods:
        #__init__    = Called when creating object
        #__str__     = Called by print()
        #__repr__    = Called by repr() - for debugging
        #__len__     = Called by len()
        #__bool__    = Called by if statements
        #__getitem__ = indexing support

#Student Practice
#Beginner - Book with str
class Book:
    #add __str__
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author} has {self.pages} pages"
#test
book = Book("Python 101", "Jane Doe", 250)
print(book)
print("="*25)

#Week 4 - Lecture 6 - Unit 2: Arithmetic Operator Overloading
#Common Arithmetic Magic Methods
    #Arithmetic Operators
        #+  = __add__, __radd__
        #-  = __sub__, __rsub__
        #*  = __mul__, __rmul__
        #/  = __truediv__
        #// = __floordiv__
        #%  = __mod__
    #Right-side Methods
        #__radd__ handles other + obj when obj doesnt support "+"
        #ensures operations work both ways
    #In-place Operators
        #+= -> __iadd__
        #-= -> __isub__

#Student Practice
#Beginner - Money class
class Money:
    #add money with "+"" operator
    def __init__(self, dollars):
        self.dollars = dollars
    def __str__(self):
        return f"${self.dollars:.2f}"
    def __add__(self, other):
        total = self.dollars + other.dollars
        return Money(total)
#test
m1 = Money(10.50)
m2 = Money(5.25)
m3 = m1 + m2
print(m3)
print("="*25)

#Intermediate - Fraction Arithmetic
class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator
    def __str__(self):
        return f"{self.num}/{self.den}"
    def __add__(self, other):
        #add fractions: a/b + c/d = (a*d + b*c)/(b*d)
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    def __mul__(self, other):
        #multiply: a/b * c/d = (a*c)/(b*d)
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
#test
f1 = Fraction(1 ,2)
f2 = Fraction(1, 3)
print(f1 + f2)
print(f1 * f2)
print("="*25)

#Week 4 - Lecture 6 - Unit 3: Overloading Comparison Operators
#Comparison Magic Methods
    #Methods
        #__eq__ : ==
        #__ne__ : !=
        #__lt__ : <
        #__le__ : <=
        #__gt__ : >
        #__ge__ : >=
    #Purpose: to define how objects of your class are compared using operators like ==, >, <, etc.
    #Rule: these methofs must return a boolean value (true/false)
    #Hashable Objects: if __eq__ defined, should define __hash__ also
    
#Student Practice
#Beginner - Score Comparison
class Score:
    #compare game scores
    def __init__(self, points):
        self.points = points
    def __str__(self):
        return f"Score: {self.points}"
    def __eq__(self, other):
        #return true if points are equal
        if self.points == other.points:
            return True
        else:
            print("Scores are not equal")
    def __lt__(self, other):
        #return true if less points
        if self.points < other.points:
            return True
        else:
            return False
#test
s1 = Score(100)
s2 = Score(85)
print(s1 > s2)
print("="*25)

#Week 4 - Lecture 6 - Unit 4: Container Protocols
#Methods:
    #__getitem__  : indexing   : obj[key]
    #__setitem__  : assignment : obj[key] = value
    #__delitem__  : deletion   : del obj[key]
    #__contains__ : itermation : for item in obj
#Sequence Protocols:
    #__len__      = implements the len() functions
    #__getitem__  = implements the bracket notation for indexing/slicing
    #__iter__     = allows your object to be used in a for loop
    #__reversed__ = reverse iteration
#Making classes iterable
    #Implement "__iter__" returning iterator
    #or __getitem__ with sequential indexing
    
#Student Practice
#Beginner - Simple Gradebook
class SimpleGrades:
    #basic indexing
    def __init__(self):
        self.grades = {}
    def __getitem__(self, name):
        #return grade or 0 if not found
        return self.grades.get(name, 0)
    def __setitem__(self, name, grade):
        #store the grade
        self.grades[name] = grade
#test
book = SimpleGrades()
book["Alice"] = 95
book["John"] = 79
print(book["Alice"])
print(book["John"])
print("="*25)

#Intermediate - Cache with access
class Cache:
    def __init__(self, max_size=3):
        self.data = {}
        self.max_size = max_size
    def __getitem__(self, key):
        #return value or None
        return self.data.get(key, None)
    def __setitem__(self, key, value):
        #add to cache, if full remove oldest item
        if len(self.data) >= self.max_size and key not in self.data:
            oldest_key = next(iter(self.data))
            del self.data[oldest_key]
        self.data[key] = value
    def __contains__(self, key):
        return key in self.data

#Week 4 - Lecture 6 - Unit 5: Context Managers
#Context Managers:
    #__enter__ = called when entering with block
    #__exit__  = called when exiting with block
#Other Useful Magic Methods
    #__getattr__ = attribute access fallback
    #__setattr__ = attribute assignment
    #__call__    = make objects callable
#Advanced Protocols
    #__getattribute__ = all attribtues access
    #__getattr__ = only when attribute not found