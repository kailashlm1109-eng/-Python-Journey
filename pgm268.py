"""
Created on Thu Sep 17 21:06:26 2026
Convert a list of strings to uppercase
@author: KAILASH L M
"""
# Convert a list of strings to uppercase
values = input("Enter words separated by spaces: ").split()
result = [value.upper() for value in values]
print(result)
