"""
Created on Thu Sep 17 21:06:26 2026
Find the largest value in a list
@author: KAILASH L M
"""
# Find the largest value in a list
numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
if numbers:
    print("Largest:", max(numbers))
