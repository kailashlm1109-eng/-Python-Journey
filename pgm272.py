"""
Created on Thu Sep 17 21:06:26 2026
Find common values in two lists
@author: KAILASH L M
"""
# Find common values in two lists
first = input("Enter first list: ").split()
second = input("Enter second list: ").split()
common = [value for value in first if value in second]
print(common)
