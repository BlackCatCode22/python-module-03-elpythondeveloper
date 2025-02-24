# Chapter 6 - Strings
# 6.6 Looping and counting

# File: exercise_4.py
# Exercise 4: There is a string method called count that is similar to
# the function in the previous exercise. Read the documentation of this
# method at: https://docs.python.org/library/stdtypes.html#string-methods

# Description - Count the number of times a letter appears in a string using a function.
# The function is named count and takes in 2 parameters, the string and the letter that is to be counted.

# ----- Function - count -----
# input - Takes 2 string arguments. A string and the letter that is to be counted in the string.
# output - The integer count of the occurrences of the letter in the string.
def count(param_string, param_letter):

    # Declare a variable called word and assign it the value stored in variable param_string
    word = param_string
    # Declare a variable called count and assign it a string of 0.
    count = 0
    # ----- for loop -----
    # The iteration variable in this loop is called letter.
    # The for loop iterates through the string saved in variable word and saves it
    # in variable letter each iteration.
    for letter in word:
        # During each iteration the character saved in variable letter is checked.
        # If the value is the character stored in variable param_letter
        # then 1 is added to the value stored in count variable.
        if letter == param_letter:
            count = count + 1
    # ----- for loop -----

    # The function returns the integer count
    return count
# ----- Function - count -----

# This invocation calls the count function.
# Call the count function and pass in the string banana and letter as arguments
# stored the count retuned by the count function in a variable called letter_count
letter_count = count('banana','a')

# Print the value stored in variable letter_count to the console.
print(letter_count)






