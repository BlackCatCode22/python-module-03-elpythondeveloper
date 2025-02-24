# Chapter 5 - Iteration
# 5.2 The while statement

# Example 1 - while statement example

# declare a variable called n and assign it a value of 5
n = 5

#----- while statement -----
# the items in the while statement execute multiple times
# as long as the value in n is greater than 0
while n > 0:
    # print the value stored in n
    print(n)
    # Update variable n by subtracting 1 from it and then stored that value back in n
    # After the variable is updated the while loop starts over and checks
    # to see if variable n is greater than zero, if it isn't the loop exits.
    n = n - 1
#----- while statement -----
# after the while exits this string will be printed to the console.
print('Blastoff!')