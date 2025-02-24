# Chapter 5 - Iteration
# 5.3 Infinite Loops

# Example - while statement infinite loop example

#----- while statement -----
# The items in the while statement execute
# as long as the expression is True. The loop is always true until
# the user types in done.
while True:
    line = input('> ')
    # if the user types done then this while statement exits.
    if line == 'done':
        break
    # If the user types anything besides done, the value is printed here
    # and then the while loop starts again.
    print(line)
#----- while statement -----
# after the while exits this string will be printed to the console.
print('Done!')