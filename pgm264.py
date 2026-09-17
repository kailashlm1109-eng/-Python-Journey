"""
Created on Thu Sep 17 21:06:26 2026
Copy a list using a loop
@author: KAILASH L M
"""
# Copy a list using a loop
values = input("Enter values separated by spaces: ").split()
copy = []
for value in values:
    copy.append(value)
print(copy)
