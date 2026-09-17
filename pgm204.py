"""
Created on Thu Sep 17 21:06:26 2026
Count even and odd values
@author: KAILASH L M
"""
# Count even and odd values
numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
even = odd = 0
for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)
