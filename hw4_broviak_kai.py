import re
from collections import Counter 

#Problem 1: Grouping and Capturing
def problem1():
    #Extract date components from various date formats
    dates_text = """
    Important dates:
    - Project due: 2024-03-15
    - Meeting on: 12/25/2024
    - Holiday: July 4, 2025
    """
    #Write a pattern that captures dates in format YYYY-MM-DD
    pattern_iso = r"(\d{4})-(\d{2})-(\d{2})"
    #Extract all ISO format dates (YYYY-MM-DD)
    iso_dates = re.findall(pattern_iso, dates_text)
    #Parse email addresses and extract username and domain
    emails_text = "Contact john.doe@example.com or alice_smith@university.edu for info"
    #Write pattern with named groups for username and domain
    pattern_email = r"(?P<username>[\w\.-]+)@(?P<domain>[\w\.-]+\.\w+)"
    #Extract all emails with their components
    email_parts = [match.groupdict() for match in re.finditer(pattern_email, emails_text)]
    phones_text = "Call (555) 123-4567 or 800-555-1234 for support"
    #Write pattern to capture area code and number separately
    pattern_phone = r"\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})"
    #Extract all phone numbers as tuples (area_code, number)
    phone_numbers = [(area, f"{first}-{last}") for area, first, last in re.findall(pattern_phone, phones_text)]
    repeated_text = "The the quick brown fox jumped over the the lazy dog"
    #Write pattern to find consecutive repeated words
    pattern_repeated = r"\b(\w+)\s+\1\b"
    #Find all repeated words
    repeated_words = [words.lower() for words in re.findall(pattern_repeated, repeated_text)] # List of repeated words (just the word, not the duplicate)
    return {
        'iso_dates': iso_dates,
        'email_parts': email_parts,
        'phone_numbers': phone_numbers,
        'repeated_words': repeated_words
    }
print(problem1())
print("="*75)

#Probelm 2: Alternation Patterns
def problem2():
    #Match different file extensions
    files_text = """
    Documents: report.pdf, notes.txt, presentation.pptx
    Images: photo.jpg, diagram.png, icon.gif, picture.jpeg
    Code: script.py, program.java, style.css
    """
    #Pattern to match image files (jpg, jpeg, png, gif)
    pattern_images = r"\b\w+\.(jpg|jpeg|png|gif)\b"
    #Find all image filenames
    image_files = [match.group(0) for match in re.finditer(pattern_images, files_text)]
    #Match different date formats
    mixed_dates = "Meeting on 2024-03-15 or 03/15/2024 or March 15, 2024"
    #Pattern to match all three date formats using alternation
    pattern_dates = r"(\d{4}-\d{2}-\d{2})|(\d{2}/\d{2}/\d{4})|([A-Za-z]+ \d{1,2}, \d{4})"
    #Find all dates regardless of format
    all_dates = [match.group(0) for match in re.finditer(pattern_dates, mixed_dates)]
    #Extract prices in different formats
    prices_text = "$19.99, USD 25.00, 30 dollars, €15.50, £12.99"
    #Pattern to match prices with different currency symbols
    pattern_prices = r"(\$\d+(\.\d{2})?)|(USD \d+(\.\d{2})?)|(\d+ dollars)|([€£]\d+(\.\d{2})?)"
    #Extract all prices with their currency indicators
    prices = [match.group(0) for match in re.finditer(pattern_prices, prices_text)]
    #Match programming language mentions
    code_text = """
    We use Python for data science, Java for enterprise apps,
    JavaScript or JS for web development, and C++ or CPP for systems.
    """
    #Pattern to match language names and their abbreviations
    pattern_langs = r"\b(Python|Java|JavaScript|JS|C\+\+|CPP)\b"
    #Find all programming language mentions
    languages = [match.group(0) for match in re.finditer(pattern_langs, code_text)]
    return {
        'image_files': image_files,
        'all_dates': all_dates,
        'prices': prices,
        'languages': languages
    }
print(problem2())
print("="*75)

#Probelm 3: Using re.findall() and re.finditer() 
def problem3():
    log_text = """
    [2024-03-15 10:30:45] INFO: Server started on port 8080
    [2024-03-15 10:31:02] ERROR: Connection failed to database
    [2024-03-15 10:31:15] WARNING: High memory usage detected (85%)
    [2024-03-15 10:32:00] INFO: User admin logged in from 192.168.1.100
    [2024-03-15 10:32:30] ERROR: File not found: config.yml
    """
    #Use findall() to extract all timestamps
    #Pattern for timestamp [YYYY-MM-DD HH:MM:SS]
    pattern_timestamp = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]"
    #Extract all timestamps
    timestamps = [match for match in re.findall(pattern_timestamp, log_text)]
    #Use findall() with groups to extract log levels and messages
    #Pattern with groups for log level and message
    pattern_log = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] (\w+): (.+)"
    #Extract tuples of (level, message)
    log_entries = [(level, message) for level, message in re.findall(pattern_log, log_text)]
    #Use finditer() to get positions of all IP addresses
    #Pattern for IP addresses
    pattern_ip = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    #Find all IP addresses with their positions
    ip_addresses = [(match.group(0), match.start(), match.end()) for match in re.finditer(pattern_ip, log_text)]
    #Use finditer() to create a highlighted version of errors
    #Replace ERROR entries with **ERROR** (highlighted)
    highlighted_log = log_text
    #Create function to highlight all ERROR entries
    def highlight_errors(text):
        pattern_error = r"(ERROR: .+)"
        return re.sub(pattern_error, r"**\1**", text)
    highlighted_log = highlight_errors(log_text)
    return {
        'timestamps': timestamps,
        'log_entries': log_entries,
        'ip_addresses': ip_addresses,
        'highlighted_log': highlighted_log
    }
if __name__ == "__main__":
    result = problem3()
    print("\n" + "=" * 60)
    print("PROBLEM 3 OUTPUT".center(60))
    print("=" * 60)
    for key, value in result.items():
        print(f"\n{key.upper()}:")
        if isinstance(value, str):
            print(value.strip())
        elif isinstance(value, list) and all(isinstance(i, tuple) for i in value):
            for item in value:
                print("  ", item)
        elif isinstance(value, list):
            for item in value:
                print("  ", item)
        else:
            print(value)
        print("-" * 60)
print("="*75)

#Problem 4: Using re.sub() for Text Transformation
def problem4():
    #Clean and format phone numbers
    messy_phones = """
    Contact list:
    - John: 555.123.4567
    - Jane: (555) 234-5678
    - Bob: 555 345 6789
    - Alice: 5554567890
    """
    #Standardize all phone numbers to format: (555) 123-4567
    def standardize_phones(text):
        pattern = r"\(?(\d{3})\)?[.\s-]?(\d{3})[.\s-]?(\d{4})"
        replacement = r"(\1) \2-\3"
        return re.sub(pattern, replacement, text)
    cleaned_phones = standardize_phones(messy_phones)
    #Redact sensitive information
    sensitive_text = """
    Customer: John Doe
    SSN: 123-45-6789
    Credit Card: 4532-1234-5678-9012
    Email: john.doe@email.com
    Phone: (555) 123-4567
    """
    #Redact SSN and Credit Card numbers
    def redact_sensitive(text):
        text = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "XXX-XX-XXXX", text)
        text = re.sub(r"\b\d{4}-\d{4}-\d{4}-\d{4}\b", "XXXX-XXXX-XXXX-XXXX", text)
        return text
    redacted_text = redact_sensitive(sensitive_text)
    #Convert markdown links to HTML
    markdown_text = """
    Check out [Google](https://google.com) for search.
    Visit [GitHub](https://github.com) for code.
    Read documentation at [Python Docs](https://docs.python.org).
    """
    #Convert [text](url) to <a href="url">text</a>
    def markdown_to_html(text):
        pattern = r"\[([^\]]+)\]\((https?://[^\)]+)\)"
        replacement = r'<a href="\2">\1</a>'
        return re.sub(pattern, replacement, text)
    html_text = markdown_to_html(markdown_text)
    #Implement a simple template system
    template = """
    Dear {name},
    Your order #{order_id} for {product} has been shipped.
    Tracking number: {tracking}
    """
    values ={
        'name': 'John Smith',
        'order_id': '12345',
        'product': 'Python Book',
        'tracking': 'TRK789XYZ'
    }
    #Replace {key} with corresponding values
    def fill_template(template, values):
        def replace_placeholder(match):
            key = match.group(1)
            return values.get(key, match.group(0))  
        pattern = r"\{(\w+)\}"
        return re.sub(pattern, replace_placeholder, template)
    filled_template = fill_template(template, values)
    return {
        'cleaned_phones': cleaned_phones,
        'redacted_text': redacted_text,
        'html_text': html_text,
        'filled_template': filled_template
    }

if __name__ == "__main__":
    result = problem4()
    for key, value in result.items():
        print(f"\n=== {key.upper()} ===")
        print(value.strip())
        print("=" * 60)
print("="*75)

#Problem 5: Pattern Compilation and Optimization
def problem5():
    #Create a class to hold compiled patterns
    class PatternLibrary:
        #Compile these patterns
        #Email validation pattern
        EMAIL = re.compile(
            r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
            re.IGNORECASE
        )
        #URL pattern
        URL = re.compile(
            r"^(https?:\/\/)?(www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(/.*)?$",
            re.IGNORECASE
        )
        #US ZIP code
        ZIP_CODE = re.compile( r"^\d{5}(-\d{4})?$")
        #Strong password
        #Requirements: 8+ chars, uppercase, lowercase, digit, special char
        PASSWORD = re.compile(
            r"""
            ^(?=.*[A-Z])
            (?=.*[a-z])
            (?=.*\d)
            (?=.*[@$!%*?&])
            [A-Za-z\d@$!%*?&]{8,}$
            """,
            re.VERBOSE
        )
        #Credit card number
        CREDIT_CARD = re.compile(r"^(?:\d{4}[- ]?){3}\d{4}$")
    #test patterns
    test_data = {
        'emails': ['valid@email.com', 'invalid.email', 'user@domain.co.uk'],
        'urls': ['https://example.com', 'www.test.org', 'invalid://url'],
        'zips': ['12345', '12345-6789', '1234', '123456'],
        'passwords': ['Weak', 'Strong1!Pass', 'nouppercas3!', 'NoDigits!'],
        'cards': ['1234 5678 9012 3456', '1234-5678-9012-3456', '1234567890123456']
    }
    #Validate each item using your compiled patterns
    validation_results = {
        'emails': [bool(PatternLibrary.EMAIL.match(e)) for e in test_data['emails']],
        'urls': [bool(PatternLibrary.URL.match(u)) for u in test_data['urls']],
        'zips': [bool(PatternLibrary.ZIP_CODE.match(z)) for z in test_data['zips']],
        'passwords': [bool(PatternLibrary.PASSWORD.match(p)) for p in test_data['passwords']],
        'cards': [bool(PatternLibrary.CREDIT_CARD.match(c)) for c in test_data['cards']]
    }
    return validation_results
print(problem5())
print("="*75)

#Probelm 6: Real-World Application
def problem6():
    log_data = """
    192.168.1.1 - - [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 5234
    192.168.1.2 - - [15/Mar/2024:10:30:46 +0000] "POST /api/login HTTP/1.1" 401 234
    192.168.1.1 - - [15/Mar/2024:10:30:47 +0000] "GET /images/logo.png HTTP/1.1" 304 0
    192.168.1.3 - - [15/Mar/2024:10:30:48 +0000] "GET /admin/dashboard HTTP/1.1" 403 0
    192.168.1.2 - - [15/Mar/2024:10:30:49 +0000] "POST /api/login HTTP/1.1" 200 1234
    192.168.1.4 - - [15/Mar/2024:10:30:50 +0000] "GET /products HTTP/1.1" 200 15234
    192.168.1.1 - - [15/Mar/2024:10:30:51 +0000] "GET /contact HTTP/1.1" 404 0
    """
    #Parse log entries to extract IP, tiemstamp, HTTP method, URL path, status code, response size
    #Create pattern to parse log lines
    log_pattern = re.compile(
        r"""
        (?P<ip>\d{1,3}(?:\.\d{1,3}){3})
        \s+-\s+-\s+
        \[(?P<timestamp>[^\]]+)\]\s+
        "(?P<method>[A-Z]+)\s+
        (?P<path>[^\s]+)\s+HTTP/[0-9.]+"\s+
        (?P<status>\d{3})\s+
        (?P<size>\d+)
        """,
        re.VERBOSE
    )
    #Extract all log entries as structured data
    parsed_logs = []
    for match in log_pattern.finditer(log_data):
        entry = {
            "ip": match.group("ip"),
            "timestamp": match.group("timestamp"),
            "method": match.group("method"),
            "path": match.group("path"),
            "status": int(match.group("status")),   
            "size": int(match.group("size"))        
        }
    parsed_logs.append(entry)
    #Analyze the logs
    total_requests = len(parsed_logs)
    unique_ips = sorted(set(e["ip"] for e in parsed_logs))
    error_count = sum(1 for e in parsed_logs if 400 <= e["status"] < 600)
    total_bytes = sum(e["size"] for e in parsed_logs)
    method_counts = Counter(e["method"] for e in parsed_logs)
    path_counts = Counter(e["path"] for e in parsed_logs)
    most_requested_path = path_counts.most_common(1)[0][0] if path_counts else ""
    analysis = {
      "total_requests": total_requests,
        "unique_ips": unique_ips,
        "error_count": error_count,
        "total_bytes": total_bytes,
        "most_requested_path": most_requested_path,
        "methods_used": list(method_counts.keys())   
    }
    return {
        "parsed_logs": parsed_logs,
        "analysis": analysis
    }
print(problem6())