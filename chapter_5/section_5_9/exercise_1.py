# Chapter 5 - Iteration
# 5.14 Exercises
# ------------------
# Exercise 1: What will the following Python program print out?
# Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.
# ------------------
# Example output is:
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333
# ------------------

num = 0
tot = 0.0
# ----- while loop -----
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    # ----- try except block -----
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    # ----- try except block -----
    #print(fval)
    num = num + 1
    tot = tot + fval
# ----- while loop -----
#print('ALL DONE')
print(tot,num,tot/num)
