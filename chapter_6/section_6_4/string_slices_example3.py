# Chapter 6 - Strings
# 6.4 String slices

# File: string_slice_example2.py
# Description - In this example I get a slice of a string and display the first 5 characters in the console.
# A segment of a string is called a slice.

# The operator [n:m] returns the part of the string from the “n-th” character to the
# “m-th” character, including the first but excluding the last.
# If I omit the first index (before the colon), the slice starts at the beginning of
# the string. If I omit the second index, the slice goes to the end of the string.

# Declare a variable called fruit and assign it a string of banana.
fruit = 'banana'

# Since I omitted the second index, the slice goes to the end of the string.
# So the first character is 3 and goes all the way to the end.
# Index 3 in the string is the second a
# So the characters displayed start with the second a in banana and go to the end
# In this case ana should be displayed in the console.
print(fruit[3:])