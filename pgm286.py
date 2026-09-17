"""
Created on Thu Sep 17 21:06:26 2026
Return a list of factors
@author: KAILASH L M
"""
# Return a list of factors
def factors(number):
    return [value for value in range(1, number + 1) if number % value == 0]

number = int(input("Enter a positive number: "))
print(factors(number))
