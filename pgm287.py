"""
Created on Thu Sep 17 21:06:26 2026
Recursive factorial function
@author: KAILASH L M
"""
# Recursive factorial function
def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)

number = int(input("Enter a non-negative number: "))
print(factorial(number))
