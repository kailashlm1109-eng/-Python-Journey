"""
Created on Thu Sep 17 21:06:26 2026
Swap the first and last list values
@author: KAILASH L M
"""
# Swap the first and last list values
values = input("Enter values: ").split()
if values:
    values[0], values[-1] = values[-1], values[0]
print(values)
