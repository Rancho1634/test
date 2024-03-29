"""
Letter Case Counter Function

Objective:
Write a function named 'case_counter' that counts the number of uppercase and lowercase letters in a given string.

Function Parameter:
text (string): The string in which the letters need to be counted.

Instructions:
- The function should calculate and print two numbers: the count of uppercase letters and the count of lowercase letters in the string.
- If there are no letters of a particular case (uppercase or lowercase) in the string, the function should print 0 for that case.
- Non-alphabetic characters in the string should be ignored and not counted.

Example Test Cases:
1. case_counter("Hello World!") should print the counts of uppercase and lowercase letters.
2. case_counter("PYTHON") should print the counts of uppercase and lowercase letters.
3. case_counter("python") should print the counts of uppercase and lowercase letters.
4. case_counter("1234!@#$") should print 0 for both counts.
"""


def case_counter(text):  # define case_counter(text) function
    uppercase_count = 0  # initial number equals zero
    lowercase_count = 0  # initial number equals zero
    for char in text:    # consider the characters in the text
        if char.isalpha():  # if the character is alphabet
             if char.isupper():  # if character is uppercase
                  uppercase_count += 1  # then the number of uppercase plus 1
             elif char.islower():  # if character is lowercase
                  lowercase_count += 1  # then the number of lowercase plus 1
    
    print(f"Uppercase Count: {uppercase_count}")   # print the number of uppercase out
    print(f"Lowercase Count: {lowercase_count}")   # print the number of lowercase out
    
        

    # Your code goes here
    # Remember to count uppercase and lowercase letters and ignore non-alphabetic characters
    pass  # Delete this after implementing some code inside this function.


# Test cases
case_counter("Hello World!")  # Expected: Uppercase letters: 2, Lowercase letters: 8
case_counter("PYTHON")  # Expected: Uppercase letters: 6, Lowercase letters: 0
case_counter("python")  # Expected: Uppercase letters: 0, Lowercase letters: 6
case_counter("1234!@#$")  # Expected: Uppercase letters: 0, Lowercase letters: 0
