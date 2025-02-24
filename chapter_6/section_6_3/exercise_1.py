# Chapter 6 - Strings
# 6.3 Traversal through a string with a loop

# File: exercise_1.py
# Exercise 1: Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

# Declare a variable called fruit and assign it a string of watermelon.
fruit = 'watermelon'

#----- for loop -----
# Iterate through each character in the fruit string.
# I use the python reversed functino to traverse the string in reverse order.
# The iteration variable in this loop is called letter.
# The for loop iterates through the string saved in variable fruit and saves it
# in variable letter each iteration. After each iteration the for loop prints the letter.
# After the last letter in the string the for loop exits.
for letter in reversed(fruit):
    # Print the current letter to the console.
    print(letter)
#----- for loop -----

# Reference:
# https://docs.python.org/3/library/functions.html
# https://docs.python.org/3/library/functions.html#reversed
# The reversed() function in Python returns an iterator that accesses the given sequence
# in this case a string in the reverse order.
# It doesn't modify the original sequence.
# it just provides a way to access its elements from back to front.