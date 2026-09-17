"""
Created on Thu Sep 17 21:06:26 2026
Display a matrix row by row
@author: KAILASH L M
"""
# Display a matrix row by row
rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))
matrix = []
for row in range(rows):
    values = []
    for column in range(columns):
        values.append(int(input("Enter a value: ")))
    matrix.append(values)
for values in matrix:
    print(values)
