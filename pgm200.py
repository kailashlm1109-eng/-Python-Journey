"""
Created on Thu Sep 17 21:06:26 2026
Read numbers into a list
@author: KAILASH L M
"""
# Read numbers into a list
count = int(input("How many numbers: "))
numbers = []
for i in range(count):
    numbers.append(int(input("Enter a number: ")))
print(numbers)
