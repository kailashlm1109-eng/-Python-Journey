"""
Created on Thu Sep 17 21:06:26 2026
Sort a list in descending order
@author: KAILASH L M
"""
# Sort a list in descending order
numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
numbers.sort(reverse=True)
print(numbers)
