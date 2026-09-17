"""
Created on Thu Sep 17 21:06:26 2026
Find the factorial of a number
@author: KAILASH L M
"""
# Find the factorial of a number
n = int(input("Enter a non-negative number: "))
factorial = 1
for number in range(2, n + 1):
    factorial *= number
print("Factorial:", factorial)
