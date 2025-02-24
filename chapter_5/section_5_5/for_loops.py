# Chapter 5 - Iteration
# 5.5 Definite loops using for

# Difference between and indefinite loop and a definite loop
# A while statement is an indefinite loop because it simply loops until some condition becomes False.
# We don't really know how many times it will loop.
# The for loop is a definite loop.
# The reason it's a definite loop is because it loops through a known set of items.
# It runs through as many iterations as there are items in the set.

# Example - using a for loop
# This example uses a for loop to go through a list of strings and print each string in the list
# one at a time. After the last string in the list, the loop exits and prints the message Done!
# for and in are reserved Python keywords.

# define a list of strings and save it in a variable called friends
friends = ['Joseph', 'Glenn', 'Sally']
#----- for loop -----
# the for loop goes through the list stored in the friends variable and executes the body once
# for each of the three strings in the list.
for friend in friends:
    # In each iteration of the for loop the string prints the string stored in the friend variable
    print('Happy New Year:', friend)
#----- for loop -----
# after the for loop exits this string will be printed to the console.
print('Done!')