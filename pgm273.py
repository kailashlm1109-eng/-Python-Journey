"""
Created on Thu Sep 17 21:06:26 2026
Merge two lists without duplicates
@author: KAILASH L M
"""
# Merge two lists without duplicates
first = input("Enter first list: ").split()
second = input("Enter second list: ").split()
merged = []
for value in first + second:
    if value not in merged:
        merged.append(value)
print(merged)
