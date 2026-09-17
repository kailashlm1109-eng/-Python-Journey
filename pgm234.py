"""
Created on Thu Sep 17 21:06:26 2026
Print the first n natural numbers and their sum
@author: KAILASH L M
"""
# Print the first n natural numbers and their sum
n = int(input("Enter n: "))
total = 0
for number in range(1, n + 1):
    total += number
print("Sum:", total)
