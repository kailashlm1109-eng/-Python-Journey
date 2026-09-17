"""
Created on Thu Sep 17 21:06:26 2026
Count values with a dictionary
@author: KAILASH L M
"""
# Count values with a dictionary
values = input("Enter values: ").split()
counts = {}
for value in values:
    counts[value] = counts.get(value, 0) + 1
print(counts)
