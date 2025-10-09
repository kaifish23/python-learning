#Problem 1: Restaurant Order System
'''
add_to_order(order, item_name, quantity, price_per_item)
    - add item to order (or update quantity)
    - quantity must be positive integer
    - price must be positive number
    - return True if successful, False otherwise
remove_from_order(order, item_name)
    - remove item completely from order
    - return True if removed, False if itme not found
calculate_bill(order, tax_rates)
    - calculate total bill including tax
    - tax_rate is percentage (8 for 8%)
    - return total amount
Example:
    order = {}
    add_to_order(order, "Pizza", 2, 12.99)
    add_to_order(order, "Soda", 3, 2.50)
    bill = calculate_bill(order, 8) #8% tax
    print(f"Total: ${bill:.2f}")
'''
def add_to_order(order, item_name, quantity, price_per_item):
    if quantity <= 0: #quantity positive
        return False
    if price_per_item <= 0: #price positive
        return False 
    if item_name in order: #update quantity if in order
        order[item_name][0] += quantity
    else: #adding to order
        order[item_name] = [quantity, price_per_item]
    return True

def remove_from_order(order, item_name):
    if item_name in order:
        del order[item_name]
        return True
    else:
        return False
        
def calculate_bill(order, tax_rates):
    subtotal = 0
    for item in order:
        quantity = order[item][0]
        price = order[item][1]
        subtotal += quantity * price
    total = subtotal + (subtotal * tax_rates / 100) 
    return total

#test function
if __name__ == "__main__":
    order = {}
    #test add
    print("="*12)
    print(add_to_order(order, "Burger", 2, 8.99)) #True
    print(add_to_order(order, "Fries", -1, 3.50)) #False
    print(add_to_order(order, "Drink", 2, 2.99))  #True
    print(f"Order: {order}")
    #test bill calculations
    total = calculate_bill(order, 10) #10% tax
    print(f"Total with 10% tax: ${total:.2f}")
    #test removal
    print(remove_from_order(order, "Drink")) #True
    print(remove_from_order(order, "Pizza")) #False
    print("="*12)

#example
order = {}
add_to_order(order, "Pizza", 2, 12.99)
add_to_order(order, "Soda", 3, 2.50)
bill = calculate_bill(order, 8) #8% tax
print(f"Total: ${bill:.2f}")
print("="*12)
    
#Problem 2: Movie Theater Seating
'''
reserve_seats(reservations, movie_name, seat_numbers)
    - reserve seats for a movie
    - reservations: dict where keys = movie_names, values = sets of reserved seats
    - seat_numbers: list of seat numbers to reserve
    - add movie if it doesnt exist
cancel_reservation(reservations, movie_name, seat_numbers)
    - cancel specific seat reservations
    - return True if cancelled, False if movie doesnt exist
get_available_seats(reservations, movie_name, total_seats)
    - find available seats (not reserved)
    - total_seats: set of all seat numbers in theater
    - return set of available seats
find_common_viewers(reservations, movie1, movie2)
    - find seats (people) who reserved both movies
    - assume same seat number = same person
    - return set of seat numbers
Example:
    reservations = {}
    reserve_seats(reservations, "Avatar", [1, 2, 3, 5])
    reserve_seats(reservations, "Inception", [2, 3, 6, 7])
    common = find_common_viewers(reservations, "Avatar", "Inception")
    print(common) #{2, 3}
'''
def reserve_seats(reservations, movie_name, seat_numbers):
    if movie_name not in reservations: #add movie
        reservations[movie_name] = set()
    for seat in seat_numbers: #add all seats from list
        reservations[movie_name].add(seat)
        
def cancel_reservation(reservations, movie_name, seat_numbers):
    if movie_name not in reservations: #return False if movie doesnt exist
        return False
    for seat in seat_numbers:
        if seat in reservations[movie_name]: #cancel specific seat reservations
            reservations[movie_name].remove(seat)
    return True

def get_available_seats(reservations, movie_name, total_seats):
    if movie_name not in reservations: #if movie not in reservations, all seats available
        return total_seats
    reserved = reservations[movie_name]
    available = total_seats - reserved
    return available #available = total seats - reserved seats

def find_common_viewers(reservations, movie1, movie2):
    if movie1 not in reservations or movie2 not in reservations: #if neither exist, return empty set
        return set()
    return reservations[movie1] & reservations[movie2] #common viewers

#test function
if __name__ == "__main__":
    print("="*12)
    reservations = {}
    theater_seats = set(range(1, 21)) #seats 1-20
    #reserve seats
    reserve_seats(reservations, "Spider-Man", [1, 2, 3, 4, 5])
    reserve_seats(reservations, "Batman", [3, 4, 7, 8, 9])
    reserve_seats(reservations, "Superman", [2, 5, 10, 11])
    print(f"Reservations: {reservations}")
    #find available seats
    available = get_available_seats(reservations, "Spider-Man", theater_seats)
    print(f"Available for Spider-Man: {available}")
    #find common viewers
    common = find_common_viewers(reservations, "Spider-Man", "Batman")
    print(f"Watched both Spider-Man and Batman: {common}")
    #cancel seats
    print(cancel_reservation(reservations, "Batman", [7,8]))
    print(f"After cancellation: {reservations['Batman']}")
    print("="*12)

#example
reservations = {}
reserve_seats(reservations, "Avatar", [1, 2, 3, 5])
reserve_seats(reservations, "Inception", [2, 3, 6, 7])
common = find_common_viewers(reservations, "Avatar", "Inception")
print(common) #{2, 3}
print("="*12)

#Problem 3: Student Test Scores with NumPy
'''
create_random_scores(num_students, num_tests)
    - generate random test scores between 50-100
    - return 2D array (students x tests)
identify_failing_tests(scores, passing_grade)
    - find which tests each student failed
    - return 2D boolean array (True = failed)
calculate_student_ranks(scores)
    - rank students by their average score
    - return array of student indices sorted by average (highest first)
apply_curve(scores, curve_type, value)
    - apply curve to all scores
    - curve_type: "add" (add points) or "multiply" (multiply by factor)
    - cap scores at 100
    - return curved scores
Example:
    scores = create_random_scores(5, 3) #5 students, 3 tests
    print(scores)
    failing = indentify_failing_tests(scores, 70)
    print(f"Failed tests: {failing}")
    ranks = calculate_student_ranks(scores)
    print(f"Student rankings: {ranks}")
'''
import numpy as np
import random
def create_random_scores(num_students, num_tests):
    scores = []
    for i in range(num_students):
        student_scores = []
        for j in range(num_tests):
            score = random.randint(50,100)
            student_scores.append(score)
        scores.append(student_scores)
    return scores

def identify_failing_tests(scores, passing_grade):
    failing = []
    for student_scores in scores:
        failed = []
        for score in student_scores:
            if score < passing_grade:
                failed.append(True)
            else:
                failed.append(False)
        failing.append(failed)
    return failing 

def calculate_student_ranks(scores):
    averages = []
    for i in range(len(scores)):
        avg = sum(scores[i]) / len(scores[i])
        averages.append((i, avg))
    averages.sort(key=lambda x: x[1], reverse=True)
    ranks = [student_index for student_index, avg in averages]
    return ranks

def apply_curve(scores, curve_type, value):
    new_scores = []
    for student_scores in scores:
        curved_scores = []
        for score in student_scores:
            if curve_type == "add":
                new_score = score + value
            elif curve_type == "multiply":
                new_score = score * value
            else:
                new_score = score
            if new_score > 100:
                new_score = 100
            curved_scores.append(round(new_score, 2))
        new_scores.append(curved_scores)
    return new_scores

#test function
if __name__ == "__main__":
    print("="*12)
    #create test scores
    scores = create_random_scores(6,4)
    print("Original scores:")
    print(scores)
    #indentify failing tests (< 70)
    failing = identify_failing_tests(scores, 70)
    print(f"\nFailing tests (True = failed):")
    print(failing)
    #get student rankings
    ranks = calculate_student_ranks(scores)
    print(f"\nStudent rankings (by average): {ranks}")
    #apply curve
    curved_add = apply_curve(scores.copy(), "add", 5)
    print(f"\nAfter adding 5 points:")
    print(curved_add)
    curved_mult = apply_curve(scores.copy(), "multiply", 1.1)
    print(f"\nAfter 10% increase:")
    print(curved_mult)
    print("="*12)
    
#example
scores = create_random_scores(5, 3) #5 students, 3 tests
print(scores)
failing = identify_failing_tests(scores, 70)
print(f"Failed tests: {failing}")
ranks = calculate_student_ranks(scores)
print(f"Student rankings: {ranks}")
print("="*12)

#Problem 4: Email Address Processor
'''
extract_username(email)
    - extract part before @ symbol
    - return username or None if invalid
extract_domain(email)
    - extract part after @ symbol
    - return domain or None if invalid
standardize_email(email)
    - convert to lowercase
    - remove leading/trailing spaces
    - remove dots from username
    - return standardized email
validate_email_list(email_string)
    - input: comma-separated emails
    - validate each (must have @ and .)
    - return two lists (valid and invalid emails)
Example:
    email = "   John.Doe@GMAIL.COM  "
    clean = standardize_email(email)
    print(clean)
    emails = "alice@test.com, bad-email, bob@site.org"
    valid, invalid = validate_email_list(emails)
    print(f"Valid: {valid}")
    print(f"Invalid: {invalid}")
'''
def extract_username(email):
    if "@" not in email:
        return None
    parts = email.split("@")
    if len(parts) != 2:
        return None
    return parts[0]

def extract_domain(email):
    if "@" not in email:
        return None
    parts = email.split("@")
    if len(parts) != 2:
        return None
    return parts[1]

def standardized_email(email):
    email = email.strip().lower() #remove spaces & lowercase
    if "@" not in email: #split into user and domain
        return None
    parts = email.split("@")
    if len(parts) != 2:
        return None
    username = parts[0].replace(".", "") #removing periods
    domain = parts[1]
    clean_email = username + "@" + domain
    return clean_email

def validate_email_list(email_string):
    valid = []
    invalid = []
    emails = email_string.split(",") #split string with commas
    for email in emails:
        clean_email = email.strip()
        if "@" in clean_email and "." in clean_email:
            valid.append(clean_email)
        else:
            invalid.append(clean_email)
    return valid, invalid

#test function
if __name__ == "__main__":
    #test extraction
    email1 = "student@university.edu"
    print(f"Username: {extract_username(email1)}")
    print(f"Domain: {extract_domain(email1)}")
    #test standardization
    messy_emails = [
        "   John.Smith@GMAIL.COM    ",
        "alice.jones@YAHOO.COM",
        "Bob@COMPANY.ORG"
    ]
    print("\n Standardized emails:")
    for email in messy_emails:
        clean = standardized_email(email)
        print(f"{email} -> {clean}")
    #test validation
    email_list = "good@email.com, another@test.org, bad-email, missing@, @nodomain.com"
    valid, invalid = validate_email_list(email_list)
    print(f"\n Valid emails: {valid}")
    print(f"Invalid emails: {invalid}")
    
#example
email = "   John.Doe@GMAIL.COM  "
clean = standardize_email(email)
print(clean)
emails = "alice@test.com, bad-email, bob@site.org"
valid, invalid = validate_email_list(emails)
print(f"Valid: {valid}")
print(f"Invalid: {invalid}")

#Problem 5: Log File Analyzer with Regex
'''
extract_ip_addresses(log_text)
    - find all IP addresses (format: XXX.XXX.XXX.XXX)
    - each part is 1-3 digits
    - return list of IP addresses
extract_timestamps(log_text)
    - find timestamps (format: HH:MM:SS)
    - return list of timestamps
count_log_levels(log_text)
    - count occurances of [INFO], [WARNING], [ERROR]
    - return dictionary with counts
extract_error_message(log_text)
    - find all text after "[ERROR]" until end of line
    - return list of error messages
'''