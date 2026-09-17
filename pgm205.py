"""
Created on Thu Sep 17 21:06:26 2026
Copy only positive values to another list
@author: KAILASH L M
"""
# Copy only positive values to another list
numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
positive = []
for number in numbers:
    if number > 0:
        positive.append(number)
print(positive)
