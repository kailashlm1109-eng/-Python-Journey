"""
Created on Thu Sep 17 21:06:26 2026
Find the smallest value in a list
@author: KAILASH L M
"""
# Find the smallest value in a list
numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
if numbers:
    print("Smallest:", min(numbers))
