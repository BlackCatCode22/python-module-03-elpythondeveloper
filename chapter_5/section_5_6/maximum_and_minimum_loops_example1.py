# Chapter 5 - Iteration
# 5.6 Loop patterns
#     5.6.2 Maximum and minimum loops

# Maximum and minimum loops Example 1
# This example finds the largest number in a list

# Declare a variable called largest and set it's value to None
# In Python, None is a special keyword that represents the absence of a value or a null value.
largest = None
# The value saved in variable largest will be printed to the console
print('Before:', largest)
#----- for loop -----
# This for loop goes through the list of integers.
# The iteration variable in this loop is called itervar.
for itervar in [3, 41, 12, 9, 74, 15]:
    # During each for loop iteration it checks if the value stored in the variable largest is None
    # or the value stored itervar is greater than largest.
    if largest is None or itervar > largest :
        # If either of the two if statement conditions are true
        # then the value stored in itervar is saved in variable largest.
        largest = itervar
    # During each for loop iteration the values in the variables itervar and largest are printed in console.
    # After the last integer in the list is reached, after printing these variables, the for loop exits.
    print('Loop:', itervar, largest)
# ----- for loop -----
# After the for loop exits this string will be printed to the console
# which displays the value saved in the variable called largest.
print('Largest:', largest)