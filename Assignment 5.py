



'''Implement a recursive function to calculate the factorial of a non-negative integer.
Instructions:
Write a recursive function     factorial(n) that returns the factorial of the non-negative integer     n.
The factorial of     n (denoted as     n!) is defined as:
n! = n * (n-1)! for n > 0
0! = 1
Write test cases to verify the function works correctly for different values of     n.
'''

# Define a function to calculate factorials
def factorial(number):

    #base case
    if number == 0:
        return 1

    # Recursive case
    else:
        return number * factorial(number - 1)

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))