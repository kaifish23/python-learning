import numpy as np
np.random.seed(1350)
import re


#Problem 1: array creation and basic operations // extra credit 
def problem1():
    #create a 1D array from 10-50, store in arr1
    arr1 = np.arange(10, 51, 1) #starts 10, ends 50, increase by 1
    #create a 2D array of shape (3, 4) filled with zeros, store in arr2
    arr2 = np.zeros((3, 4))
    #create a 3x3 matrix, store in identity
    identity = np.eye(3)
    #create an array of 10 evenly spaced numbers 0-5, store in linspace_arr
    linspace_arr = np.linspace(0, 5, 10)
    #create a random array of shape (2, 5) with values 0 and 1, store in random_arr
    random_arr = np.random.rand(2, 5)
    return arr1, arr2, identity, linspace_arr, random_arr
problem1()

#Problem 2: Array Mathematics and Broadcastings // extra credit
def problem2():
    #given arrays
    arr_a = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
    arr_b = np.array([10, 20, 30])
    #Add arr_b to each row of arr_a
    result_add = arr_a + arr_b
    #Multiply each column of arr_a by the corresponding element in arr_b
    result_multiply = arr_a * arr_b
    #Calculate the square of all elements in arr_a
    result_square = np.square(arr_a)
    #Calculate the mean of each column in arr_a
    column_means = np.mean(arr_a, axis=0)
    #Subtract the column means from each element in the respective column
    centered_arr = arr_a - column_means
    return result_add, result_multiply, result_square, centered_arr, column_means

    
#Part 1: Advanced String Methods
#Problem 1.1: String Formatting and Alignment
def format_receipt(items, prices, quantities):
    print("="*40)
    print(f"{'Item':<20} {'Quantity':>5} {'Price':>8}")
    print("="*40)
    for item, price, quantity in zip(items, prices, quantities):
        total = price * quantity
        print(f"{item: <20} {quantity: ^5} ${total:>8.2f}")
    print("="*40)
    total_amount = sum(price * quantity for price, quantity in zip(prices, quantities))
    print(f"{'Total': <26} ${total_amount:>8.2f}")
    print("="*40)

items = ["Coffee", "Sandwich", "Cookie"]
prices = [3.50, 8.99, 2.00]
quantities = [2, 1, 3]
print(format_receipt(items, prices, quantities))
print("="*40)

#Problem 1.2: String Transformation Methods
def process_user_data(raw_data):
    cleaned_data = {}
    #clean name
    name = raw_data.get('name','').strip().title()
    cleaned_data['name'] = name
    #clean email
    email = raw_data.get('email','').strip().lower().replace(' ', '')
    cleaned_data['email'] = email
    #clean phone
    phone = raw_data.get('phone','').strip().replace('(', '').replace(')', '').replace('-', '').replace(' ','')
    cleaned_data['phone'] = phone
    #clean address
    address = ' '.join(raw_data.get('address','').strip().title().split())
    cleaned_data['address'] = address
    #generate username
    if name:
        first_last = cleaned_data['name'].split()
        username = f"{first_last[0].lower()}_{first_last[-1].lower()}"
    else:
        username = ' '
    cleaned_data['username'] = username
    #validate data
    validation = {
        'name': bool(name),
        'email': bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)),
        'phone': phone.isdigit() and 7 <= len(phone) <= 15,
        'address': bool(address)
    }
    cleaned_data['validation'] = validation
    return cleaned_data
data = {
    'name': ' john DOE ',
    'email': ' JOHN.DOE @EXAMPLE.COM ',
    'phone': '(555) 123-4567',
    'address': '123 main street, apt 5'
}
result = process_user_data(data)
for key, value in result.items():
    print(f"result['{key}']")
    print(repr(value))

#Problem 1.3: String Analysis and Manipulation
def analyze_text(text):
   lines = text.splitlines()
   words = re.findall(r"\b\w+\b", text)
   sentences = re.split(r'(?<=[.!?])\s+', text.strip())
   #totals
   total_chars = len(text)
   total_words = len(words)
   total_lines = len(lines)
   avg_word_length = round(sum(len(w) for w in words) / total_words, 2) if words else 0
   #most common word 
   most_common_word = max((word.lower() for word in words), key=lambda x: sum(1 for word in words if word.lower() == x))
   #longest line
   longest_line = max(lines, key=len, default="")
   #words per line
   words_per_line = [len(re.findall(r"\b\w+\b", line)) for line in lines]
   #sentence analysis
   capitalized = sum(1 for s in sentences if s and s[0].isupper())
   questions = sum(1 for s in sentences if s.endswith('?'))
   exclaimations = sum(1 for s in sentences if s.endswith('!'))
   return {
       'total_chars': total_chars,
        'total_words': total_words,
        'total_lines': total_lines,
        'avg_word_length': avg_word_length,
        'most_common_word': most_common_word,
        'longest_line': longest_line,
        'words_per_line': words_per_line,
        'capitalized_sentences': capitalized,
        'questions': questions,
        'exclamations': exclaimations
   }
print("="*40)
text = "Hello world! How are you? This is a test. Hello again!"
print(analyze_text(text)['total_words'])
print(analyze_text(text)['questions'])
print("="*40)

#Part 2: Introduction to Regular Expressions
#Problem 2.1: Basic Pattern Matching
def find_patterns(text):
    patterns = {
        'decimals': r'\b\d+\.\d+\b',
        'integers': r'\b\d+\b',
        'words_with_digits': r'\b\w*\d\w*\b',
        'capitalized_words':  r'\b[A-Z][a-z]*\b',
        'all_capped_words':  r'\b[A-Z]{2,}\b',
        'repeated_chars': r'\b\w*(\w)\1\w*\b'
    }
    results = {}
    #fixes integer!!! giving me problems uhgggg
    results['decimals'] = re.findall(patterns['decimals'], text)
    text_without_decimals = re.sub(patterns['decimals'], '', text)
    results['integers'] = re.findall(patterns['integers'], text_without_decimals)
    #for rest of stuff
    for key in ['words_with_digits', 'capitalized_words', 'all_capped_words', 'repeated_chars']:
        results[key] = re.findall(patterns[key], text)
    return results
text = "I have 25 apples and 3.14 pies. HELLO W0RLD!"
result = find_patterns(text)
for key, value in result.items():
    print(f"{key}: {value}")

#Probelm 2.2: Pattern Validation
print("="*40)
def validate_format(input_string, format_type):
    patterns = {
        #Phone: (XXX) XXX-XXXX or XXX-XXX-XXXX)
        'phone': r"^(?:\((?P<area_code>\d{3})\)\s(?P<prefix>\d{3})-(?P<line>\d{4})|(?P<area_code2>\d{3})-(?P<prefix2>\d{3})-(?P<line2>\d{4}))$",
        #Date:MM/DD/YYYY
        'date': r"^(?P<month>0[1-9]|1[0-2])/(?P<day>0[1-9]|[12]\d|3[01])/(?P<year>\d{4})$",
        #Time: HH:MM AM/PM or 24-hour HH:MM
        'time': r"^(?:(?P<hour12>0?[1-9]|1[0-2]):(?P<min12>[0-5]\d)\s?(?P<ampm>AM|PM)|(?P<hour24>[01]?\d|2[0-3]):(?P<min24>[0-5]\d))$",
        #Email: basic format username@domain.extension
        'email':  r"^(?P<username>[\w\.-]+)@(?P<domain>[\w\.-]+)\.(?P<extension>\w+)$",
        #URL: http:// or https:// followed by domain
        'url':r"^(?P<scheme>https?)://(?P<domain>[\w\.-]+)(?P<path>/.*)?$",
        #SSN: XXX-XX-XXXX
        'ssn':r"^(?P<area>\d{3})-(?P<group>\d{2})-(?P<serial>\d{4})$"
    }
    if format_type not in patterns:
        raise ValueError(f"Unknown format type: {format_type}")
    pattern = re.compile(patterns[format_type])
    match = pattern.match(input_string)
    if not match:
        return False, None
    #Merge groups/handle alt names
    parts = {key: value for key, value in match.groupdict().items() if value is not None}
    #phone numbers with alt group names
    if format_type == 'phone':
        if 'area_code2' in parts:
            parts = {
                'area_code': parts.pop('area_code2'),
                'prefix': parts.pop('prefix2'),
                'line': parts.pop('line2')
            }
    return True, parts
#print statements
print(validate_format("(555) 123-4567", "phone"))
print(validate_format("12/31/2024", "date"))
print(validate_format("11:45 PM", "time"))
print(validate_format("23:15", "time"))
print(validate_format("user@example.com", "email"))
print(validate_format("https://example.com/path", "url"))
print(validate_format("123-45-6789", "ssn"))
print("="*40)

#Problem 2.3: Search and Extract
def extract_information(text):
    results = {}
    #Prices format $X.XX or $X,XXX.XX
    results['prices'] = re.findall(r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?", text)
    #Percentages format X% or X.X%
    results['percentages'] = re.findall(r"\b\d+(?:\.\d+)?%", text)
    #Years
    results['years'] = re.findall(r"\b(19\d{2}|20\d{2})\b", text)
    #Sentences
    results['sentences'] = re.findall(r"[^.!?]*[.!?]", text)
    #Questions
    results['questions'] = [s for s in results['sentences'] if s.strip().endswith('?')]
    #Quoted text
    results['quoted_text'] = re.findall(r'"(.*?)"', text)
    return results
#Example info
text = 'The price is $19.99 (20% off). "Great deal!" she said.'
result = extract_information(text)
print(result['prices'])
print(result['percentages'])
print(result['quoted_text'])

#Part 3: Combining String Methods and Regex
#Problem 3.1: Text Cleaning Pipeline
print("="*40)
def clean_text_pipeline(text, operations):
    steps = []
    current_text = text
    for ope in operations:
        if ope == 'trim':
            current_text = current_text.strip()
        elif ope == 'lowercase':
            current_text = current_text.lower()
        elif ope == 'remove_punctuation':
            current_text = re.sub(r'[^\w\s]', '', current_text)
        elif ope == 'remove_digits':
            current_text = re.sub(r'\d', '', current_text)
        elif ope == 'remove_extra_space':
            current_text = " ".join(current_text.split())
        elif ope == 'remove_urls':
            current_text = re.sub(r'https?://\S+', '', current_text)
        elif ope == 'remove_emails':
            current_text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '', current_text)
        elif ope == 'capitalize_sentences':
            current_text = re.sub(
                r'(^|[.!?]\s+)([a-z])',
                lambda match: match.group(1) + match.group(2).upper(),
                current_text
            )
        steps.append(current_text)
    return {
        'original': text,
        'cleaned': current_text,
        'steps': steps
    }
#example info
text = " Hello WORLD! Visit https://example.com "
ops = ['trim', 'lowercase', 'remove_urls', 'remove_extra_spaces']
result = clean_text_pipeline(text, ops)
print(result['cleaned'])

#Problem 3.2: Smart Text Replacement
print("="*40)
def smart_replace(text, replacement):
    #contractions
    contractions = {
        "don't": "do not",
        "won't": "will not",
        "can't": "cannot",
        "I'm": "I am",
        "you're": "you are",
        "it's": "it is",
        "he's": "he is",
        "she's": "she is",
        "we're": "we are",
        "they're": "they are",
        "I've": "I have",
        "you've": "you have",
        "we've": "we have",
        "they've": "they have"
    }
    #phone replace
    if replacement.get('censor_phone'):
        text = re.sub(r'\b\d{3}[-.)\s]?\d{3}[-.\s]?\d{4}\b', 'XXX-XXX-XXXX', text)
    #email replace
    if replacement.get('censor_email'):
        text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '[EMAIL]', text)
    #fix spacing
    if replacement.get('fix_spacing'):
        text = re.sub(r'\s+([,.!?])', r'\1', text)
        text = re.sub(r'([,.!?])(?!\s|$)', r'\1 ', text)
        text = re.sub(r'\s+', ' ', text).strip()
    #replace contractions
    if replacement.get('expand_contractions'):
        text = re.sub(r'\b(' + '|'.join(re.escape(key) for key in contractions.keys()) + r')\b', lambda match: contractions[match.group(0)], text)
    #number to word
    if replacement.get('number_to_word'):
        digits = {
             "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
             "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"
        }
        text = re.sub(r'\b\d\b', lambda match: digits[match.group()], text)
    return text
#test info
text = "Call me at 555-123-4567. I'm busy. Email me at test@example.com! I have 2 dogs."
rules = {
    'censor_phone': True,
    'censor_email': True,
    'fix_spacing': True,
    'expand_contractions': True,
    'number_to_word': True
}
print(smart_replace(text, rules))

#Part 4: Practical Application
#Problem 4.1: Log File Analyzer
print("="*40)
def analyze_log_info(log_text):
    pattern = re.compile(
        r"\[(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2})\]\s+"
        r"(?P<level>INFO|ERROR|WARNING): (?P<message>.+)"
    )
    entries = []
    for match in pattern.finditer(log_text):
        entries.append(match.groupdict())
    if not entries:
        return {
            'total_entries': 0,
            'error_count': 0,
            'warning_count': 0,
            'info_count': 0,
            'dates': [],
            'error_messages': [],
            'time_range': None,
            'most_active_hour': None
        }
    #count entries by level
    total_entries = len(entries)
    error_count = sum(1 for e in entries if e['level'] == 'ERROR')
    warning_count = sum(1 for e in entries if e['level'] == 'WARNING')
    info_count = sum(1 for e in entries if e['level'] == 'INFO')
    #unique dates
    dates = sorted(set(e['date'] for e in entries))
    #error messages
    error_messages = [e['message'] for e in entries if e['level'] == 'ERROR']
    #time range
    times = [e['time'] for e in entries]
    earliest_time = min(times)
    latest_time = max(times)
    #count activity
    hour_counts = {}
    for e in entries:
        hour = int(e['time'].split(":")[0])
        hour_counts[hour] = hour_counts.get(hour, 0) + 1
    most_active_hour = max(hour_counts, key=hour_counts.get)
    return {
        'total_entries': total_entries,
        'error_count': error_count,
        'warning_count': warning_count,
        'info_count': info_count,
        'dates': dates,
        'error_messages': error_messages,
        'time_range': (earliest_time, latest_time),
        'most_active_hour': most_active_hour
    }




def run_tests():
    print("="*40)
    print("Testing Part 1: String Methods")
    print("="*40)
    # Test 1.1: Receipt formatting
    items = ["Coffee", "Sandwich"]
    prices = [3.50, 8.99]
    quantities = [2, 1]
    receipt = format_receipt(items, prices, quantities)
    print("Receipt Test:")
    print(receipt)
    # Test 1.2: User data processing
    test_data = {
        'name': ' john DOE ',
        'email': ' JOHN@EXAMPLE.COM ',
        'phone': '(555) 123-4567',
        'address': '123 main street'
    }
    cleaned = process_user_data(test_data)
    print(f"\nCleaned name: {cleaned.get('name', 'ERROR')}")
    print(f"Cleaned email: {cleaned.get('email', 'ERROR')}")
    print("\n" + "="*40)
    print("Testing Part 2: Regular Expressions")
    print("="*40)
    # Test 2.1: Pattern finding
    test_text = "I have 25 apples and 3.14 pies"
    patterns = find_patterns(test_text)
    print(f"Found integers: {patterns.get('integers', [])}")
    print(f"Found decimals: {patterns.get('decimals', [])}")
    # Test 2.2: Format validation
    phone_valid, phone_parts = validate_format("(555) 123-4567", "phone")
    print(f"\nPhone validation: {phone_valid}")
    if phone_parts:
        print(f"Extracted parts: {phone_parts}")
    # Test 2.3: Information extraction
    info_text = 'The price is $19.99 (20% off).'
    info = extract_information(info_text)
    print(f"\nPrices found: {info.get('prices', [])}")
    print(f"Percentages found: {info.get('percentages', [])}")
    print("\n" + "="*40)
    print("Testing Part 3: Combined Operations")
    print("="*40)
    # Test 3.1: Cleaning pipeline
    dirty_text = " Hello WORLD! "
    operations = ['trim', 'lowercase', 'remove_extra_spaces']
    cleaned_result = clean_text_pipeline(dirty_text, operations)
    print(f"Original: '{cleaned_result.get('original', '')}'")
    print(f"Cleaned: '{cleaned_result.get('cleaned', '')}'")
    print("\n" + "="*40)
    print("Testing Part 4: Log Analysis")
    print("="*40)
    # Test 4.1: Log analysis
    sample_log = """[2024-01-15 10:30:45] ERROR: Connection failed
    [2024-01-15 10:31:00] INFO: Retry attempt
    [2024-01-15 10:32:00] WARNING: Timeout warning"""
    log_analysis = analyze_log_info(sample_log)
    print(f"Total entries: {log_analysis.get('total_entries', 0)}")
    print(f"Error count: {log_analysis.get('error_count', 0)}")
    print(f"Unique dates: {log_analysis.get('dates', [])}")
    print("\n" + "="*40)
    print("All tests completed!")
    print("="*40)
    
if __name__ == "__main__":
    run_tests()
