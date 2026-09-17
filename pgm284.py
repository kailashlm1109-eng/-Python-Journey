"""
Created on Thu Sep 17 21:06:26 2026
Define a function that returns the largest value
@author: KAILASH L M
"""
# Define a function that returns the largest value
def largest(values):
    return max(values)

numbers = [int(value) for value in input("Enter numbers: ").split()]
if numbers:
    print(largest(numbers))
