# Chapter 6 - Strings
# 6.5 Strings are immutable

# File: strings_are_immutable.py
# Description - In this example I modify a string and save it in a new string variable.

# Strings are immutable.
# We can’t change an existing string.
# The best we can do is create a new string that is a variation on the original.

# Declare a variable called greeting and assign it a string of Hello, world!
greeting = 'Hello, world!'

# I create a new string variable called new_greeting.
# The character 'J' is concatenated with a slice of the original greeting string.
# The slice greeting[1:] takes all characters from the original greeting
# starting from index 1 (the 'e' in 'Hello') to the end of the string.
# This replaces the H with J  in the original string.
new_greeting = 'J' + greeting[1:]

# print the value stored in variable new_greeting in the console.
print(new_greeting)