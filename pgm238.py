"""
Created on Thu Sep 17 21:06:26 2026
Print prime numbers in a range
@author: KAILASH L M
"""
# Print prime numbers in a range
limit = int(input("Enter the limit: "))
for number in range(2, limit + 1):
    prime = True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            prime = False
            break
    if prime:
        print(number, end=" ")
print()
