# Chapter 6 - Strings
# 6.8 String comparison
# The comparison operators work on strings. To see if two strings are equal.
# Python does not handle uppercase and lowercase letters the same way that people do.
# All the uppercase letters come before all the lowercase letters.

# File: string_comparison.py
# Description - Check if two strings are equal.

# Example 1 - Check two strings and if they are equal print a message to the console
print('----- Example 1 output -----')
# Declare a variable called word and assign it a string of banana.
word = 'banana'
# if the string stored in variable word equals banana then print string All right, bananas.
if word == 'banana':
    print('All right, bananas.')
print('----- Example 1 output -----')

# Example 2 - Check a sting using if statement and display a different message depending on condition
print('----- Example 2 output -----')
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')
print('----- Example 2 output -----')