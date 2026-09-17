"""
Created on Thu Sep 17 21:06:26 2026
Add two lists element by element
@author: KAILASH L M
"""
# Add two lists element by element
first = [int(value) for value in input("Enter first list: ").split()]
second = [int(value) for value in input("Enter second list: ").split()]
size = min(len(first), len(second))
result = []
for index in range(size):
    result.append(first[index] + second[index])
print(result)
