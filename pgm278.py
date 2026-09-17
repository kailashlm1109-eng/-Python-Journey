"""
Created on Thu Sep 17 21:06:26 2026
Build a dictionary from two lists
@author: KAILASH L M
"""
# Build a dictionary from two lists
keys = input("Enter keys: ").split()
values = input("Enter values: ").split()
result = {}
for index in range(min(len(keys), len(values))):
    result[keys[index]] = values[index]
print(result)
