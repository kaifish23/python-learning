#Exception Handling and Exceptions
#Unit 1: try/except handling

#Student Practice: Basic Exception Handling
def practice_1_basic_exceptions():
    print("\n" + "="*50)
    print("Exercise 1: Handle the Exceptions")
    print("="*50)
    #1. Fix the division by zero (return a/b or None if error)
    def safe_divide(a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return None
    #test
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    #2. Fix list index error (return item at index or 'not found')
    def safe_get_item(lst, index):
        try:
            return lst[index]
        except IndexError:
            return "Not found"
    #test
    my_list = [1, 2, 3]
    print(f"Item at index 1: {safe_get_item(my_list, 1)}")
    print(f"Item at index 10: {safe_get_item(my_list, 10)}")
    #3. Handle multiple exceptions (convert to int/float, None if impossible)
    def convert_to_number(value):
        try:
            return int(value)
        except (ValueError, TypeError):
            try:
                return float(value)
            except (ValueError, TypeError):
                return None
    #test
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = convert_to_number(val)
        print(f"Converting '{val}': {result}")
practice_1_basic_exceptions()

#Unit 2: Python's Exception Hierarchy
#Common Exception Categories
    #Value/Type
    #Lookup
    #File/IO
    #Attribute/Name
    
#Student Practice: Exception Hierarchy
def practice_2_exception_hierarchy():
    print("\n" + "="*50)
    print("Exercise 2: Exception Hierarchy")
    print("="*50)
    #1. Catch multiple related exceptions efficiently ()
    