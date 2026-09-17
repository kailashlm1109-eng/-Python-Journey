"""
Created on Thu Sep 17 21:06:26 2026
Print the multiplication table
@author: KAILASH L M
"""
# Print the multiplication table
number = int(input("Enter a number: "))
for multiplier in range(1, 11):
    print(number, "x", multiplier, "=", number * multiplier)
