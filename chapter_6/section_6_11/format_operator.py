# Chapter 6 - Strings
# 6.11 Format operator

# The format operator, % allows us to construct strings, replacing parts of the strings
# with the data stored in variables.
# When applied to integers, % is the modulus operator.
# But when the first operand is a string, % is the format operator.
# The first operand is the format string, which contains one or more format sequences
# that specify how the second operand is formatted. The result is a string.

# File: format_operator.py
# Description - Pull out a slice of a string from another string.

# Declare a variable called camels and assign it integer 42.
camels = 42
# the format sequence %d means that the second operand should be
# formatted as an integer (d stands for decimal).
# Print the value of the camels variable to the console, formatting it as a decimal integer.
# The '%d' is a format specifier that indicates an integer should be inserted at that location.
# The % operator is used to perform the string formatting.
# The value printed to the console is a string.
# Even though it represents the number 42,
# the %d format specifier in the print statement converts it into a string before displaying it.
print('%d' % camels)



#
# # Tasks to be performed:
# # Task 1 - First, we will find the position of the at-sign in the string.
# # Task 2 - Then we will find the position of the first space after the at-sign.
# # Task 3 - Then we will use string slicing to extract the portion of the string which we are looking for.
#
# # This is the string data I will be parsing in this example
# # Declare a variable called data and assign it a string.
# data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
#
# # Task 1 - find the position of the at-sign in the string saved in variabl data and save it in variable atpos
# atpos = data.find('@')
# # Print the value stored in variable atpos to the console.
# print('Task 1 output - at-sign position: ',atpos)
#
# # Task 2 - find the position of the first space after the at-sign and save it in variable sppos
# sppos = data.find(' ',atpos)
# # Print the value stored in variable sppos to the console.
# print('Task 2 output - position of the first space after the at-sign: ',sppos)
#
# # Task 3 - use string slicing to extract the portion of the string which we are looking for.
# # Get the string sliave from index 22 to 31 and save it in variable sppos
# # the character at index 21 is @,
# # the character at index 22 is u
# # so to get the string starting with u which is index 22 we add 1 (atpos+1) to start with index 22
# # gets the string slice from index 22 to 31 [22:31] and save it in variable valled host
# host = data[atpos+1:sppos]
# # Print the value stored in variable host to the console.
# print('Task 3 output - the string slice I am looking for: ',host)

# Reference
# https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/library/stdtypes.html#string-methods