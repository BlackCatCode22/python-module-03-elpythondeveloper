# Chapter 6 - Strings
# 6.2 Getting the length of a string using len

# File: get_last_letter_of_string.py
# Description - This example gets the last letter of a string.
# len is a built-in function that returns the number of characters in a string

# Declare a variable called fruit and assign it a string of banana.
fruit = 'banana'
# The sequence stored in variable fruit is passed to the len function.
# The len function returns the length of the string.
# The string length is then saved in variable length.
length = len(fruit)
# To get the last character of the string we subtract 1 from the string length
# In this example we save the last character in variable last.
last = fruit[length-1]
# Display the value stored in variable last in the console.
print(last)