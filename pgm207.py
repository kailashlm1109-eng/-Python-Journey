"""
Created on Thu Sep 17 21:06:26 2026
Count occurrences of a value
@author: KAILASH L M
"""
# Count occurrences of a value
numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
value = int(input("Enter the value: "))
print("Occurrences:", numbers.count(value))
