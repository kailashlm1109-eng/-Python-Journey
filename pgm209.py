"""
Created on Thu Sep 17 21:06:26 2026
Remove duplicate values while keeping order
@author: KAILASH L M
"""
# Remove duplicate values while keeping order
numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
