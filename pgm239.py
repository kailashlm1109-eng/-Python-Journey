"""
Created on Thu Sep 17 21:06:26 2026
Find the digits of a number in reverse order
@author: KAILASH L M
"""
# Find the digits of a number in reverse order
number = int(input("Enter a number: "))
while number > 0:
    print(number % 10, end=" ")
    number //= 10
print()
