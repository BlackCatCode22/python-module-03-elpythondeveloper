# Chapter 5 - Iteration
# 5.4 Finishing iterations with continue

# Example - using continue statement in while statement
# This example copies its input until the user types “done”,
# but treats lines that start with the hash character as lines not to be printed

# The Continue statement
# We can use the continue statement to skip to the next iteration
# without finishing the body of the loop for the current iteration.

#----- while statement -----
# The items in the while statement execute
# as long as the expression is True.
# The loop is always true until the user types in done.
while True:
    # prompt the user to enter text from the keyboard.
    # Whatever the user types and then presses Enter,
    # that text is captured and stored as a string in the variable named line.
    line = input('> ')
    # treats lines that start with the hash character as lines not to be printed
    # if the user types something that starts with the hash tag, the loop skips everything
    # and goes to the next iteration of the loop.
    if line[0] == '#':
        continue
    # if the user types done then this while statement exits.
    if line == 'done':
        break
    # If the user types anything besides done, the value is printed here
    # and then the while loop starts again.
    print(line)
#----- while statement -----
# after the while exits this string will be printed to the console.
print('Done!')