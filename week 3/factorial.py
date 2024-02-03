"""
Factorial Calculator Function #阶乘计算器功能

Objective:
Write a function named 'calculate_factorial' to compute the factorial of a number using a for loop.
#编写一个名为“calculate_factorial”的函数，使用 for 循环计算数字的阶乘。
Function Parameter:
1. number (integer): A non-negative integer for which the factorial is to be calculated.

Instructions:
- Use a for loop to calculate the factorial of 'number'.
- Return the factorial result.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. calculate_factorial(5) should return the factorial of 5.
2. calculate_factorial(0) should return 1.
3. calculate_factorial(3) should return the factorial of 3.
4. calculate_factorial(-1) should handle negative input.
"""


def calculate_factorial(number): # define calculate_factorial(number) function
    a = 1
    if number == 0 or number == 1:
        return 1
    elif number < 0:
        return "Error message or specific value"
    for i in range(1,number+1):
        a = a * i
    return(a)
       

    # Your code goes here
    # Implement the factorial calculation using a for loop
    pass  # Delete this after implementing some code inside this function


# Test cases
print(calculate_factorial(5))  # Expected output: 120
print(calculate_factorial(0))  # Expected output: 1
print(calculate_factorial(3))  # Expected output: 6
print(calculate_factorial(-1))  # Expected: Error message or specific value
