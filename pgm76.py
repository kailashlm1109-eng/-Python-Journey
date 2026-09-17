# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:05:56 2026
number to word(match)
@author: KAILASH L M
"""
number = int(input("Enter a number from 0 to 99: "))
ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
special = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

if number < 0 or number > 99:
	print("Invalid number")
elif number < 10:
	print(ones[number])
elif number < 20:
	print(special[number - 10])
else:
	word = tens[number // 10]
	if number % 10:
		word += "-" + ones[number % 10]
	print(word)

