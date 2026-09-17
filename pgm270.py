"""
Created on Thu Sep 17 21:06:26 2026
Create a list of even numbers
@author: KAILASH L M
"""
# Create a list of even numbers
n = int(input("Enter n: "))
even_numbers = [number for number in range(1, n + 1) if number % 2 == 0]
print(even_numbers)
