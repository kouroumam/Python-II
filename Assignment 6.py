

'''
Implement a recursive function to compute the nth Fibonacci number.
Instructions:
Write a recursive function     fibonacci(n) that returns the nth Fibonacci number.
The Fibonacci sequence is defined as:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1
Write test cases to verify the function works correctly for different values of     n.
'''

# Create fibonacci function
def fibonacci(number):
    #base case

    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))