# Chapter 6 - Strings
# 6.4 String slices

# File: string_slice_example1.py
# Description - In this example I get a slice of a string and display the first 5 characters in the console.
# A segment of a string is called a slice.

# Declare a variable called s and assign it a string of Monty Python.
s = 'Monty Python'

# The operator [n:m] returns the part of the string from the “n-th” character to the
# “m-th” character, including the first but excluding the last.
# If I omit the first index (before the colon), the slice starts at the beginning of
# the string. If I omit the second index, the slice goes to the end of the string.

# In this example the characters from index 0 to index 5, which are Monty will be displayed in the console
print(s[0:5])