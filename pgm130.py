# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:44:10 2026
sum of squares of 10 integers
@author: KAILASH L M
"""
sum_of_squares = 0
for i in range(10):
	number = int(input("Enter a number: "))
	sum_of_squares += number * number
print("The sum of squares:", sum_of_squares)

