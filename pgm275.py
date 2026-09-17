"""
Created on Thu Sep 17 21:06:26 2026
Remove an item from a list
@author: KAILASH L M
"""
# Remove an item from a list
values = input("Enter values: ").split()
value = input("Enter the value to remove: ")
if value in values:
    values.remove(value)
print(values)
