"""
Created on Thu Sep 17 21:06:26 2026
Separate positive and negative values
@author: KAILASH L M
"""
# Separate positive and negative values
numbers = [int(value) for value in input("Enter numbers: ").split()]
positive = [number for number in numbers if number >= 0]
negative = [number for number in numbers if number < 0]
print("Positive:", positive)
print("Negative:", negative)
