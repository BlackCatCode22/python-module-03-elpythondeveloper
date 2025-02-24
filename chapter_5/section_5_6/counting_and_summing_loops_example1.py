# Chapter 5 - Iteration
# 5.6 Loop patterns
#     5.6.1 Counting and summing loops

# Counting and summing loops Example 1
# This example counts the number of items in a list

# declare a variable called count and set it's value to 0
count = 0
#----- for loop -----
# This for loop goes through the list of integers.
# The iteration variable in this loop is called itervar.
for itervar in [3, 41, 12, 9, 74, 15]:
    # Each times the loop iterates through each integer in the list
    # the variable count is updated, 1 is added to the value stored in count.
    # After the last item in the list, the for lop exits.
    # In this example, since there are 6 numbers in the list, the value 6 is
    # saved in the variable count before the loop exits.
    count = count + 1
#----- for loop -----
# after the for loop exits this string will be printed to the console
# which displays the value saved in the variable called count.
print('Count: ', count)