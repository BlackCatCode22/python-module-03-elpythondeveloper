# Chapter 6 - Strings
# 6.1 A string is a sequence

# File: a_string_sequence.py
# Description - In this example I get the 2nd character of sequence and display it in the console.
# A string is a sequence of characters.
# We can access the characters one at a time with the bracket operator.
# We can use any expression, including variables and operators, as an index, but
# the value of the index has to be an integer.

# Declare a variable called fruit and assign it a string of banana.
fruit = 'banana'
# The expression in brackets is called an index. An index starts with 0.
# To access the first character we would use this index [0]
# In this example since we want to access the 2nd character we use index [1]
# The 2nd character of the sequence is then saved in variable letter
letter = fruit[1]
# display the value stored in variable letter in the console.
print(letter)