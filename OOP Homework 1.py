#Problem 1: Bank Account Hierarchy
#Part 1A: BankAccount Base Class
class BankAccount:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self._balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return self._balance
        else:
            print("Error: Amount must be more than 0")
            return self._balance
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return self._balance
        else:
           print("Error: amount must be less than the current balance")
           return self._balance
    @property
    def balance(self):
        return self._balance
    def __str__(self):
        return f"Account #{self.account_number} - {self.owner} - Balance: ${self._balance:.2f}"

#Part 1B: SavingsAccount Derived Class
class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, initial_balance=0, interest_rate=0.02):
        super().__init__(account_number, owner, initial_balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return interest
    def withdraw(self, amount):
        if self._balance - amount < 100:
            print("Cannot be less than the $100 minimum")
            return self._balance
        else:
            return super().withdraw(amount)

#Problem 2: Student Management System
#Part 2A: Base Student Class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self._grades = []
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self._grades.append(grade)
        else:
            print("Error: grade must be between 0-100")
    @property
    def gpa(self):
        if not self._grades:
            return 0.0
        return sum(self._grades)/len(self._grades)
    def get_letter_grade(self):
        if not self._grades:
            return "N/A"
        avg = self.gpa
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    def __str__(self):
        return f"{self.name} (ID: {self.student_id}) - GPA: {self.gpa:.1f}"

#Part 2B: Specialized Student Classes
class GraduateStudent(Student):
    def __init__(self, name, student_id, thesis_topic):
        super().__init__(name, student_id)
        self.thesis_topic = thesis_topic
    def get_letter_grade(self):
        if not self._grades:
            return "N/A"
        avg = self.gpa
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        else:
            return "F"

class HonorsStudent(Student):
    def __init__(self, name, student_id, honors_thesis=None):
        super().__init__(name, student_id)
        self.honors_thesis = honors_thesis
    @property
    def is_eligible_for_honors(self):
        return self.gpa >= 87.5
    def set_thesis(self, topic):
        if self.is_eligible_for_honors:
            self.honors_thesis = topic
        else:
            print("Not eligible for honors thesis")

#Part 2C: StudentRoster Class
class StudentRoster:
    def __init__(self):
        self.students = []
    def add_students(self, student):
        self.students.append(student)
    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None
    def list_honor_roll(self):
        found = False
        for s in self.students:
            if s.gpa >= 85:
                print(f" - {s.name} (GPA: {s.gpa:.1f})")
                found = True
        if not found:
            print("No honor roll students")
    def class_average(self):
        if not self.students:
            return 0.0
        total = sum(s.gpa for s in self.students)
        return total / len(self.students)
