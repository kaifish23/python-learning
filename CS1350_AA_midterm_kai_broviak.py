#Problem 1: Grade Book Dictionary 
def add_student(gradebook, name, grade):
    if not isinstance(name, str) or not isinstance(grade, (int, float)):
        return False
    if grade < 0 or grade > 100:
        return False
    if name in gradebook:
        return False
    gradebook[name] = grade
    return True 

def get_class_average(gradebook):
    if not gradebook:
        return 0
    total = sum(gradebook.values())
    count = len(gradebook)
    return total / count 

def get_passing_students(gradebook):
    return {name: grade for name, grade in gradebook.items() if grade >= 60}

#test
if __name__ == "__main__":
    gradebook = {}
    print(add_student(gradebook, "Alice", 85))
    print(add_student(gradebook, "Bob", 150))
    print(add_student(gradebook, "Charlie", 45))
    print(f"Average: {get_class_average(gradebook):.2f}")
    print(f"Passing: {get_passing_students(gradebook)}")
    
print("="*50)
#Problem 4: String Processing
def clean_name(name):
    cleaned_name = name.strip().title()
    return cleaned_name
    
def validate_email(email):
    if email.count("@") != 1:
        return False 
    _, domain = email.split("@", 1)
    if "." not in domain:
        return False 
    return True

def format_phone(phone):
    digits = ''.join(p for p in phone if p.isdigit())
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return "Invalid"

def process_registration(data_string):
    parts = [d.strip() for d in data_string.split(",")]
    if len(parts) != 3:
        return None
    raw_name, raw_email, raw_phone = parts
    name = clean_name(raw_name)
    if not name:
        return None
    if not validate_email(raw_email):
        return None 
    email = raw_email.strip()
    phone = format_phone(raw_phone)
    if not phone:
        return None
    return {"name": name, "email": email, "phone": phone}

#test
if __name__ == "__main__":
    print(clean_name("  john smith  "))
    print(validate_email("test@email.com"))
    print(validate_email("bad.email"))
    print(format_phone("555-123-4567"))
    print(format_phone("123"))
    test_data = "   alice jones , alice@example.com, 9871234567"
    print(process_registration(test_data))
print("="*50)

#Problem 3: NumPy Array Analysis (bonus points)
import numpy as np
def calculate_daily_averages(temps):
    arr = np.array(temps, dtype=float)
    return arr.mean(axis=1)

def find_hottest_day(temps):
    avg = calculate_daily_averages(temps)
    return int(avg.argmax())

def count_cold_readings(temps, threshold):
    arr = np.array(temps)
    return int((arr < threshold).sum())

def normalize_temperatures(temps):
    arr = np.array(temps, dtype=float)
    min_temp = arr.min()
    max_temp = arr.max()
    if max_temp == min_temp:
        return np.zeros_like(arr)
    return(arr - min_temp) / (max_temp - min_temp) * 100

#test
if __name__ == "__main__":
    temps = np.array([
        [65, 75, 70],
        [68, 78, 72],
        [70, 80, 75],
        [62, 73, 68],
        [67, 77, 71],
        [69, 79, 74],
        [64, 74, 69]
    ])
    print("Daily averages:", calculate_daily_averages(temps))
    print("Hottest day index:", find_hottest_day(temps))
    print("Cold readings (< 70):", count_cold_readings(temps, 70))
    print("Normalized (first day):", normalize_temperatures(temps)[0])
    
print("="*50)
#Problem 5: RegEx (bonus points)
import re
def find_all_phones(text):
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

def find_all_prices(text):
    pattern = r'\$\d{1,3}\.\d{2}\b'
    return re.findall(pattern, text)

def extract_emails(text):
    pattern = r'\b\w+@\w+\.\w+\b'
    return re.findall(pattern, text)

def validate_student_id(student_id):
    pattern = r'^[A-Za-z]{2}\d{4}$'
    return re.match(pattern, student_id) is not None

#test
if __name__ == "__main__":
    test_text = """
    For info, call 555-123-4567 or (555) 987-6543.
    Email us at info@school.edu or admin@college.com
    Course feed: $50.00 for materials, $150.50 for tuition
    """
    print("Phones:", find_all_phones(test_text))
    print("Prices:", find_all_prices(test_text))
    print("Emails:", extract_emails(test_text))
    print("Valid ID 'CS1234'?", validate_student_id("CS1234"))
    print("Valid ID '12ABCD'?", validate_student_id("12ABCD"))
    print("Valid ID 'AB12345'?", validate_student_id("AB12345"))