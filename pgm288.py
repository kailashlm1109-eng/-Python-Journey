"""
Created on Thu Sep 17 21:06:26 2026
Function returning quotient and remainder
@author: KAILASH L M
"""
# Function returning quotient and remainder
def divide(dividend, divisor):
    return dividend // divisor, dividend % divisor

first = int(input("Enter dividend: "))
second = int(input("Enter divisor: "))
if second != 0:
    quotient, remainder = divide(first, second)
    print("Quotient:", quotient)
    print("Remainder:", remainder)
