"""
Created on Thu Sep 17 21:06:26 2026
Find the sum and average of list values
@author: KAILASH L M
"""
# Find the sum and average of list values
numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
if numbers:
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))
