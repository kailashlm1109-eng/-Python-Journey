"""
Created on Thu Sep 17 21:06:26 2026
Find the sum of every matrix column
@author: KAILASH L M
"""
# Find the sum of every matrix column
matrix = [[int(value) for value in input("Enter a row: ").split()] for row in range(3)]
if matrix and all(len(row) == len(matrix[0]) for row in matrix):
    for column in range(len(matrix[0])):
        total = 0
        for row in matrix:
            total += row[column]
        print("Column sum:", total)
