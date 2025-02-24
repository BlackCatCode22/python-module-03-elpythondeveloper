# Chapter 5 - Iteration
# 5.6 Loop patterns
#     5.6.1 Counting and summing loops

# Counting and summing loops Example 2
# This example computers the total by adding all the integers in a list.

# declare a variable called total and set it's value to 0
total = 0
#----- for loop -----
# This for loop goes through the list of integers.
# The iteration variable in this loop is called itervar.
for itervar in [3, 41, 12, 9, 74, 15]:
    # Each times the loop iterates through each integer in the list
    # the integer is saved in the iteration variable calle itervar.
    # The variable total is then updated, the value stored in variable itervar
    # is added to the value stored in total. Then the next iteration of the loop starts.
    # After the for loop reaches the last item in the list, the for lop exits.
    total = total + itervar
#----- for loop -----
# After the for loop exits this string will be printed to the console
# which displays the value saved in the variable called total.
print('Total: ', total)






