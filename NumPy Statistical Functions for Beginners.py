import numpy as np

test_array = np.array([1, 2, 3])
print("NumPy is working! Your test array is:", test_array)
print("NumPy version:", np.__version__)

#Unit 1: Quick Review of NumPy Arrays
#Key Operations Review
#Array Creation
arr = np.array([1, 2, 3, 4, 5]) #from list
arr = np.arange(10)              #numbers 0-9
arr = np.linspace(0, 10, 5)     #5 points from 0 to 10
#Indexing and Slicing
arr[0] #first element
arr[-1] #last element
arr[1:4] #elements 1, 2, 3
arr[::2] #every other element
#Broadcasting
arr + 10 #add 10 to all elements
arr * 2 #multiply all elements by 2

#Student Practice: Review Exercise
def practice_1_review():
    print("\n" + "="*50)
    print("Review Exercise: Array Basics")
    print("="*50)
    #given array of temperatures
    temps = np.array([68, 72, 75, 71, 77, 73, 70])
    print("This weeks temperatures:", temps)
    #Add 5 degrees to all temperatures (Heat Wave!)
    heatwave = temps + 5
    #Convert to Celsius (F-32)*5/9
    celsius = temps - 32 * 5 / 9
    #Find temperatures above 72
    warm_days = temps > 72
    print(f"Heat wave temps: {heatwave}")
    print(f"In Celsius: {celsius}")
    print(f"Days above 72: {warm_days}")
    print(f"Number of warm days: {np.sum(warm_days) if warm_days is not None else '?'}")
practice_1_review()

#Unit 2: Basic Statistical Operations
#Finding average (mean)
numbers = np.array([10, 20, 30, 40, 50])
average = np.mean(numbers) #returns 30
#Finding min/max
np.min(numbers) #returns 10
np.max(numbers) #retuns 50
#Finding the sum
np.sum(numbers) #returns 150
#Standard deviation
#close together (small std = similar numbers)
close = np.array([48, 50, 49, 50, 51])
np.std(close) #small number (about 1.0)
#spread out (large std = different numbers)
spread = np.array([10, 90, 5, 95, 50])
np.std(spread) #large number (about 40)

#Student Practice: Calculate Statistics
def practice_2a_basic_stats():
    print("\n" + "="*50)
    print("Exercise 2.1: Homework Score Statistics")
    print("="*50)
    #given homework scores out of 100
    homework_scores = np.array([85, 92, 78, 95, 88, 73, 90, 82, 97, 91])
    print("Homework scores", homework_scores)
    #calculate average score
    average = np.mean(homework_scores)
    #find highest score
    highest = np.max(homework_scores)
    #find lowest score
    lowest = np.min(homework_scores)
    #calculate total points earned
    total = np.sum(homework_scores)
    print(f"Average score: {average}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Total points: {total}")
    #Bonus: how many students scored above 85?
    above_85 = homework_scores > 85   #true/false array
    count_above_85 = np.sum(above_85) #true = 1 / false = 0
    print(f"Students scoring above 85: {count_above_85}")
practice_2a_basic_stats()

def practice_2b_shopping_analysis():
    print("\n" + "="*50)
    print("Exercise 2.2: Shopping Cart Analysis")
    print("="*50)
    #prices of items in a shopping cart
    item_prices = np.array([5.99, 12.50, 3.25, 8.75, 15.00, 7.50, 4.99, 9.99])
    print("Item prices: $", item_prices)
    #calculate total cost
    total_cost = np.sum(item_prices)
    #find most expensive item
    most_expensive = np.max(item_prices)
    #find cheapest item
    cheapest = np.min(item_prices)
    #find average price
    average_price = np.mean(item_prices)
    print(f"Total cost: ${total_cost:.2f}")
    print(f"Most exepensive item: ${most_expensive:.2f}")
    print(f"Cheapest item: ${cheapest:.2f}")
    print(f"Average item price: ${average_price:.2f}")
    #Bonus: apply 10% discount to all items
    discounted = item_prices * 0.9
    savings = total_cost - np.sum(discounted) if total_cost else 0
    print(f"After 10% discount, you save: ${savings:.2f}")
practice_2b_shopping_analysis()

#Unit 3: Working with 2D Arrays (tables)
#1D Array: List
scores = np.array([85, 90, 78]) #scores of one student
#2D Array: Table
all_scores = np.array([
    [85, 90, 78], #Student 1 scores
    [92, 88, 95], #Student 2 scores
    [78, 82, 80]  #Student 3 scores
])
#Statistics on 2D Arrays
#overall stats
np.mean(all_scores) #average of ALL scores
#row stats
np.mean(all_scores, axis=1) #average for each student
#column stats
np.mean(all_scores, axis=0) #average for each test
#axis=1 means down vertical columns, axis=0 means across horizontal rows

#Student Practice: 2D Array Analysis
def practice_3a_sales_data():
    print("\n" + "="*50)
    print("EXERCISE 3.1: Store Sales Data")
    print("="*50)
    #Sales data: 3 stores x 5 days (Mon-Fri)
    #row=store, column=day
    sales = np.array([
        [100, 150, 120, 180, 200], #Store A
        [90, 110, 130, 160, 190],  #Store B
        [120, 140, 110, 170, 210]  #Store C
    ])
    print("Sales Data (rows=stores, columns=days):")
    print("Store A:", sales[0])
    print("Store B:", sales[1])
    print("Store C:", sales[2])
    #calculate total sales for each store
    store_totals = np.sum(sales, axis=1)
    #calculate average dails sales across all stores
    daily_averages = np.mean(sales, axis=0)
    #find the highest sales for the entire week
    highest_sale = np.max(sales)
    #calculate total sales for whole week
    total_sales =  np.sum(sales)
    print(f"\n Store totals: {store_totals}")
    print(f"Daily averages: {daily_averages}")
    print(f"Highest sale: ${highest_sale}")
    print(f"Total weekly sales: ${total_sales}")
practice_3a_sales_data()

#Unit 4: Universal Functions (ufuncs)
#Without ufuncs (the hard way)
numbers = [1, 2, 3, 4, 5]
squared = []
for n in numbers: #square each number using a for loop
    squared.append(n ** 2)
#With ufuncs (easy way)
numbers = np.array([1, 2, 3, 4, 5])
squared = np.square(numbers)
'''
#Common Universal Functions

#Basic Math ufuncs
np.add(a, b)      #Addition (same as a + b)
np.subtract(a, b) #Subtraction (same as a - b)
np.multiply(a, b) #Multiplication (same as a * b
np.divide(a, b)   #Division (same as a / b)
np.square(a)      #Square each element
np.sqrt(a)        #Square root of each element
np.power(a, 3)    #Cube each element

#Comparison unfuncs
np.greater(a, b)  #same as a > b
np.lesser(a, b)   #same as a < b
np.equal(a, b)    #same as a == b

#Useful ufuncs
np.abs(a)         #absolute value (removes negative)
np.round(a)       #round to nearest integer
np.floor(a)       #round down
np.ceil(a)        #round up
'''
def practice_4a_price_calc():
    print("\n" + "="*50)
    print("Exercise 4.1: Price Updates with ufuncs")
    print("="*50)
    #Original prices
    prices = np.array([10.00, 25.50, 15.75, 30.00, 8.99])
    print("Original Prices: $", prices)
    #Add 8% tax to all prices
    prices_with_tax = np.multiply(prices, 1.08)
    #Apply 20% discount
    discounted_prices = np.multiply(prices, 0.8)
    #Round all prices to nearest dollar
    rounded_prices = np.round(prices)
    #Find which prices are under $20
    under_20 = np.less(prices, 20)
    print(f"With 8% tax: ${prices_with_tax}")
    print(f"With 20% discount: ${discounted_prices}")
    print(f"Rounded prices: ${rounded_prices}")
    print(f"Under $20 (True/False): {under_20}")
practice_4a_price_calc()

def practice_4b_grade_curve():
    print("\n" + "="*50)
    print("Exercise 4.2: Grade Curving")
    print("="*50)
    #Test Scores
    scores = np.array([65, 72, 78, 81, 69, 75, 83, 77, 70, 68])
    print("Original scores:", scores)
    #Add 10 points to all scores
    curved_scores = np.add(scores, 10)
    #Make sure nothing exceeds 100
    capped_scores = np.minimum(curved_scores, 100)
    #Calculate square root curve
    sqrt_curved = np.sqrt(scores)*10
    print(f"After +10 curve: {curved_scores}")
    print(f"Capped at 100: {capped_scores}")
    print(f"Square root curve: {sqrt_curved}")
practice_4b_grade_curve()


#Unit 5: Comparing Arrays and Finding Values
#Comparing Arrays with Conditions
scores = np.array([85, 92, 78, 95, 88])
passed = scores >= 80 #returns true/false
num_passed = np.sum(passed) #returns 4 (true=1, false=0)
#Finding Specific Values
passing_scores = scores[scores >= 80] #returns [85, 92, 95, 88]
highest_position = np.argmax(scores) #returns 3 (position index of 95)
#Multiple Conditions
in_range = (scores >= 80)&(scores <= 90) #scores between 80 and 90
extreme = (scores > 90) | (scores < 70) #scores higher than 90 OR scores lower than 70

#Student Practice: Finding and Filtering
def practice_5a_temp_analysis():
    print("\n" + "="*50)
    print("Exercise 5.1: Finding Temperature Patterns")
    print("="*50)
    #Daily temp for 2 weeks
    temps = np.array([68, 72, 75, 71, 80, 82, 79, 77, 73, 70, 69, 74, 78, 76])
    print("Two weeks of temperatures:", temps)
    #Find how many days were above 75
    hot_days = np.sum(temps > 75)
    #Find temperature on cold days (below 70)
    cold_days = temps[temps < 70]
    #Find days with perfect weather (70-75)
    perfect_days = (temps >= 70)&(temps <= 75)
    num_perfect = np.sum(perfect_days)
    #Find positon of hottest day
    hottest_day = np.argmax(temps)
    print(f"Days above 75°F: {hot_days}")
    print(f"Cool day temperatures: {cold_days}")
    print(f"Number of perfect days: {num_perfect}")
    print(f"Hottest day was #{hottest_day + 1 if hottest_day is not None else "?"}")
practice_5a_temp_analysis()

#Unit 6: Putting It All Together
#Student Practice: Complete Analysis Project
def practice_6_student_gradebook():
    print("\n" + "="*50)
    print("Final Project: Class Gradebook System")
    print("="*50)
    #Student grades: 6 students x 4 assignments
    grades = np.array([
        [88, 92, 85, 90], # Student 1
        [75, 80, 78, 82], # Student 2
        [93, 95, 91, 94], # Student 3
        [67, 70, 72, 68], # Student 4
        [82, 85, 88, 86], # Student 5
        [90, 88, 92, 89]  # Student 6
    ])
    print("Class Gradebook:")
    print("Student HW1, HW2, HW3, HW4")
    for i in range(len(grades)):
        print(f" #{i + 1} ", end="")
        for grade in grades[i]:
            print(f" {grade}", end="")
        print()
    #Calculate each student's average (per row)
    student_avgs = np.mean(grades, axis=1)
    #Calculate each assignment's average (per column)
    assignment_avgs = np.mean(grades, axis=0)
    #Find highest grade in class
    highest_grade = np.max(grades)
    #Count how many students have an average >= 85
    if student_avgs is not None:
        honor_roll = student_avgs >= 85
        num_honor_roll = np.sum(honor_roll)
    #Add 5 bonus points to all grades (but cap at 100)
    curved_grades = np.minimum(grades + 5, 100)
    #print results
    print("\n--- ANALYSIS RESULTS ---") 
    if student_avgs is not None:
        print(f"Student averages: {student_avgs}")
    if assignment_avgs is not None:
        print(f"Assignment averages: {assignment_avgs}")
    if highest_grade is not None:
        print(f"Highest grade: {highest_grade}")
    if 'num_honor_roll' in locals() and num_honor_roll is not None:
        print(f"Students on honor roll: {num_honor_roll}")
    #Show letter grades
    if student_avgs is not None:
        print("\n--- LETTER GRADES ---")
        for i, avg in enumerate(student_avgs):
            if avg >= 90:
                letter = 'A'
            elif avg >= 80:
                letter = 'B'
            elif avg >= 70:
                letter = 'C'
            else:
                letter = 'D'
            print(f"Student #{i+1}: {avg:.1f} ({letter})")
practice_6_student_gradebook()