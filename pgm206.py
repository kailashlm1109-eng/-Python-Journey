"""
Created on Thu Sep 17 21:06:26 2026
Search for a value in a list
@author: KAILASH L M
"""
# Search for a value in a list
numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
value = int(input("Enter the value to search: "))
if value in numbers:
    print("Value found")
else:
    print("Value not found")
