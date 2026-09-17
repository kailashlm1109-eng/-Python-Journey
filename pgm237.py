"""
Created on Thu Sep 17 21:06:26 2026
Check whether a number is prime
@author: KAILASH L M
"""
# Check whether a number is prime
n = int(input("Enter a number: "))
prime = n >= 2
for divisor in range(2, int(n ** 0.5) + 1):
    if n % divisor == 0:
        prime = False
        break
print("Prime" if prime else "Not prime")
