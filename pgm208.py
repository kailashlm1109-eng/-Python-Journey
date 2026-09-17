"""
Created on Thu Sep 17 21:06:26 2026
Reverse a list without reverse()
@author: KAILASH L M
"""
# Reverse a list without reverse()
numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
reversed_numbers = []
for index in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[index])
print(reversed_numbers)
