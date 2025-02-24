# Chapter 5 - Iteration
# 5.6 Loop patterns
#     5.6.2 Maximum and minimum loops

# Maximum and minimum loops Example 2
# This example finds the smallest number in a list

# Declare a variable called smallest and set it's value to None
# In Python, None is a special keyword that represents the absence of a value or a null value.
smallest = None
# The value saved in variable smallest will be printed to the console
print('Before:', smallest)
#----- for loop -----
# This for loop goes through the list of integers.
# The iteration variable in this loop is called itervar.
for itervar in [3, 41, 12, 9, 74, 15]:
    # During each for loop iteration it checks if the value stored in the variable smallest is None
    # or the value stored itervar is less than smallest.
    if smallest is None or itervar < smallest :
        # If either of the two if statement conditions are true
        # then the value stored in itervar is saved in variable smallest.
        smallest = itervar
    # During each for loop iteration the values in the variables itervar and smallest are printed in console.
    # After the last integer in the list is reached, after printing these variables, the for loop exits.
    print('Loop:', itervar, smallest)
# ----- for loop -----
# After the for loop exits this string will be printed to the console
# which displays the value saved in the variable called smallest.
print('Smallest:', smallest)