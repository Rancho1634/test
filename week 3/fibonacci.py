"""
Fibonacci Sequence Calculator Function #斐波那契数列计算器功能

Objective:
Write a function named 'fibonacci_sequence' to generate the Fibonacci sequence up to a given number using a while loop.
#编写一个名为'fibonacci_sequence'的函数，使用while循环生成给定数字以内的斐波那契数列。
Function Parameter:
1. max_value (integer): Maximum value for the Fibonacci sequence.

Instructions:
- Use a while loop to generate the Fibonacci sequence up to 'max_value'.
- Return the sequence as a list.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. fibonacci_sequence(10) should return the Fibonacci sequence up to 10.
2. fibonacci_sequence(1) should return the Fibonacci sequence up to 1.
3. fibonacci_sequence(0) should return a sequence with 0.
4. fibonacci_sequence(-5) should handle negative input.
"""


def fibonacci_sequence(max_value): # define fibonacci_sequence(max_value) function
    if max_value == 0:
        return 0
    elif max_value < 0:
        return "Empty list or error message"
    sequence = [0, 1]  # initial sequance
    while sequence[-1] + sequence[-2] <= max_value:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
    # Your code goes here
    # Implement the Fibonacci sequence calculation using a while loop
    pass  # Delete this after implementing some code inside this function


# Test cases
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))  # Expected output: [0, 1, 1]
print(fibonacci_sequence(0))  # Expected output: [0]
print(fibonacci_sequence(-5))  # Expected: Empty list or error message
