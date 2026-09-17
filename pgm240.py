"""
Created on Thu Sep 17 21:06:26 2026
Count the digits in a number
@author: KAILASH L M
"""
# Count the digits in a number
number = abs(int(input("Enter a number: ")))
if number == 0:
    count = 1
else:
    count = 0
    while number > 0:
        count += 1
        number //= 10
print("Digits:", count)
