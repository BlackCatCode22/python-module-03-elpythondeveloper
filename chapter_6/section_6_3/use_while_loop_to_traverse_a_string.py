# Chapter 6 - Strings
# 6.3 Traversal through a string with a loop

# File: use_while_loop_to_traverse_a_string.py
# Description - In this example I traverse a string using a while loop
# and display each letter on a line by itself.

# Declare a variable called fruit and assign it a string of watermelon.
fruit = 'watermelon'

# declare a variable called index and assign it a value of 0
index = 0
#----- while loop -----
# The items in the while statement execute multiple times
# as long as the index is less than the string length of the string stored in variable fruit.
# When index is equal to the length of the string,
# the condition is false, and the body of the loop is not executed.
# A while loop that continues as long as the index is less than the length of the fruit string.
# This ensures we process every character.
while index < len(fruit):
    # Get the character at the current index position in the fruit string and assign it to the variable letter.
    letter = fruit[index]
    # # Print the current letter to the console.
    print(letter)
    # Increment the index by 1 to move to the next character in the string.
    index = index + 1
#----- while loop -----