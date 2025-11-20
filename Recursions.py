#Recursions
#Unit 2: Anatomy of Recursion
#Recursions
    #Base Case
        #The condition that stops the recursion
        #Without it, you get infinite recursion (stack overflow!)
        #Usually the simplest possible input
            #if n == 0 or n == 1
                #return 1
    #Recursive Step
        #The function calling itself with a smaller/simpler input
        #Must make progress toward the base case
        #Contains the problem decomposition logic
            #return n * factorial_recursive(n - 1)
    #Recursive Thinking Pattern
        #Identify the simplest case (base case)
        #Express the problem in terms of smaller subproblems
        #Combine solutions of subproblems to solve the original

#Practice Exercises
#Exercise 2.1: Beginner - Sum of Natural Numbers
def sum_natural(n):
    #Calculate sum of natural numbers from 1 to n recursively.
    #base case
    if n <= 1:
        return n
    #recursive case
    return n + sum_natural(n - 1)
#test
print(sum_natural(5))
print(sum_natural(10))
print(sum_natural(1))
print("="*25)

#Exercise 2.2: Intermediate - Count Digits
def count_digits(n):
    #Count the number of digits in n recursively
    #base case
    if n < 10:
        return 1
    #recursion case
    return 1 + count_digits(n // 10)
#test
print(count_digits(1234))
print(count_digits(987654321))
print(count_digits(5))
print("="*25)

#Exercise 2.3: Advanced - Palindrome Checker
def is_palindrome(s):
    #Check if string s is a palindrome recursively
    #Ignore case and consider only alphanumeric characters
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    #base case
    if len(s) <= 1:
        return True
    #recursion case (compare first, last and middle letters)
    return s[0] == s[-1] and is_palindrome(s[1:-1])
#test
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("a"))
print("="*25)

#Unit 3: Implementation - Visualizing the Call Stack
