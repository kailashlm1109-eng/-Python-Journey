"""
Created on Thu Sep 17 21:06:26 2026
Create a list of squares
@author: KAILASH L M
"""
# Create a list of squares
n = int(input("Enter n: "))
squares = [number * number for number in range(1, n + 1)]
print(squares)
