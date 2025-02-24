# Chapter 6 - Strings
# 6.6 Looping and counting

# File: looping_and_counting.py
# Description - Count the number of times the letter a appears in a string.

# Declare a variable called word and assign it a string of banana.
word = 'banana'
# Declare a variable called count and assign it a string of 0.
count = 0
#----- for loop -----
# The iteration variable in this loop is called letter.
# The for loop iterates through the string saved in variable word and saves it
# in variable letter each iteration.
for letter in word:
    # During each iteration the character saved in variable letter is checked.
    # If the value is the character a then 1 is added to the value stored in count variable.
    if letter == 'a':
        count = count + 1
#----- for loop -----
# Print the value stored in variable count to the console.
print(count)