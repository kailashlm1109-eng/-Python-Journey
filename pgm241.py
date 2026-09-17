"""
Created on Thu Sep 17 21:06:26 2026
Check whether a number is an Armstrong number
@author: KAILASH L M
"""
# Check whether a number is an Armstrong number
number = int(input("Enter a number: "))
digits = str(abs(number))
total = sum(int(digit) ** len(digits) for digit in digits)
print("Armstrong number" if total == abs(number) else "Not an Armstrong number")
