# Chapter 5 - Iteration
# 5.6 Loop patterns
#     5.6.2 Maximum and minimum loops

# Maximum and minimum loops Example 3
# This example finds the smallest number in a list using the Python built-in min() function

# define a list of integer and save it in a variable called values
values = [3, 41, 12, 9, 74, 15]

#----- function - min -----
# This function uses the Python built-in min() function to
# get the smallest number of a list.
# Input - list - This function takes in one argument, a list of integers that is saved in variable values.
# Output - integer - This function returns the smallest integer number from the list that was passed into the function.
def min(values):
    # Declare a variable called smallest and set it's value to None
    smallest = None
    # The iteration variable in this loop is called value.
    for value in values:
        # During each for loop iteration it checks if the value stored in the variable smallest is None
        # or the value stored value is less than smallest.
        if smallest is None or value < smallest:
            # If either of the two if statement conditions are true
            # then the value stored in value is saved in variable smallest.
            smallest = value
    # After the last integer in the list is reached, the for loop exits
    # and the function returns the smallest number.
    return smallest
#----- function - min -----

# Call the min function and pass it the list of integers stored in variable values.
# The integer value returned by the function is then saved in the variable called smallest_value.
smallest_value = min(values)

# Display the value saved in the variable called smallest_value to the console
print('Smallest:', smallest_value)