"""
Compound Interest Calculator Function #复利计算器功能

Objective:
Write a function named 'compound_interest_calculator' to calculate compound interest.

Function Parameters:
1. P (float): Principal amount.#本金。
2. r (float): Annual interest rate in decimal.#以十进制表示的年利率。
3. n (integer): Number of times interest is compounded per year.#每年复利的次数。
4. t (integer): Number of years for investment.#投资年数。

Instructions:
- Use the formula: A = P(1 + r/n)^(nt) to calculate compound interest.
- Return the accumulated amount A after t years.
- Handle edge cases for inputs.

Example Test Cases:
1. compound_interest_calculator(1000, 0.05, 12, 5) should calculate the amount.
2. compound_interest_calculator(500, 0.07, 4, 10) should calculate the amount.
3. compound_interest_calculator(1500, 0.03, 6, 7) should calculate the amount.
"""


def compound_interest_calculator(P, r, n, t): # define compound_interest_calculator
    #p = float(input("Prinicial amount:"))    
    #r = float(input("Annual interest rate in decimal:"))
    #n = int(input("Number of times interest is compounded per year:"))
    #t = int(input("Number of years for investment:"))
    #Final = p * ((1 + (r/n)) ** (n*t))
    #return Final
     
    if P <= 0 or r < 0 or n <= 0 or t < 0:   # ensure input is valid number
         return "Invalid inputs. Please provide positive values for Principal, Annual interest rate, Number of times compounded, and Number of years."
    A = P * ((1 + r/n)**(n*t))  # Compound interest formula
    return A 
    #Your code goes here
    # Implement the compound interest calculation
    pass  # Delete this after implementing some code inside this function


# Test cases
print(compound_interest_calculator(1000, 0.05, 12, 5))  # Expected: Amount after 5 years
print(compound_interest_calculator(500, 0.07, 4, 10))  # Expected: Amount after 10 years
print(compound_interest_calculator(1500, 0.03, 6, 7))  # Expected: Amount after 7 years
