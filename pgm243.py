"""
Created on Thu Sep 17 21:06:26 2026
Find the greatest common divisor
@author: KAILASH L M
"""
# Find the greatest common divisor
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
while second:
    first, second = second, first % second
print("GCD:", abs(first))
