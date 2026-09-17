"""
Created on Thu Sep 17 21:06:26 2026
Find the sum of every matrix row
@author: KAILASH L M
"""
# Find the sum of every matrix row
matrix = [[int(value) for value in input("Enter a row: ").split()] for row in range(3)]
for row in matrix:
    print("Row sum:", sum(row))
