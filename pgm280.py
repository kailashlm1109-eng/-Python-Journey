"""
Created on Thu Sep 17 21:06:26 2026
Find the key with the largest value
@author: KAILASH L M
"""
# Find the key with the largest value
marks = {"Math": 85, "Python": 92, "English": 78}
subject = max(marks, key=marks.get)
print(subject, marks[subject])
