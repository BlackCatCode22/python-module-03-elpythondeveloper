# CIT-95-21257-2024SP: Python Programming
# Miguel Quezada
# Module 3
# Chapter 5 - Iteration
# file: ex_05_02.py
# ------------------
# Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.
# ------------------
# Example input and output:
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# maximum number:  7.0
# minimum number:  4.0
# ------------------

num = 0
tot = 0.0
largest = None
smallest = None
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

    # find the maximum number and save it in variable largest
    if largest is None or fval > largest :
        # If either of the two if statement conditions are true
        # then the value stored in fval is saved in variable largest.
        largest = fval

    # find the minimum number and save it in variable smallest
    if smallest is None or fval < smallest :
        # If either of the two if statement conditions are true
        # then the value stored in fval is saved in variable smallest.
        smallest = fval
# ----- while loop -----
#print('ALL DONE')
print('maximum number: ', largest)
print('minimum number: ', smallest)