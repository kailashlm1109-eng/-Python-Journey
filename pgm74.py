# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:05:04 2026
digit in words
@author: KAILASH L M
"""
digit = input("Enter a digit: ")
words = {
	"0": "ZERO",
	"1": "ONE",
	"2": "TWO",
	"3": "THREE",
	"4": "FOUR",
	"5": "FIVE",
	"6": "SIX",
	"7": "SEVEN",
	"8": "EIGHT",
	"9": "NINE",
}

if digit in words:
	print(digit, "-", words[digit])
else:
	print("Invalid digit")

