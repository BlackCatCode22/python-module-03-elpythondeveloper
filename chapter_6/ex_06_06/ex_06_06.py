# CIT-95-21257-2024SP: Python Programming
# Miguel Quezada
# Module 3
# Chapter 6 - Strings
# file: ex_06_06.py
# ------------------
# Prompt the user for a list of numbers, storing these numbers in a list,
# and then calculating the maximum and minimum numbers after the user
# has finished entering their numbers.
# The user indicates they are done by entering "done".
# ------------------

# Initialize an empty list to store numbers
numbers = []

while True:
    # Prompt the user to enter a number or done
    user_input = input("Enter a number or 'done' to finish: ")

    # Check if the user entered 'done' to break the loop
    if user_input == 'done':
        break

    try:
        # Try to convert the input to a float and add it to the list
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        # If conversion fails, notify the user and continue the loop
        print("Invalid input. Please enter a number value or 'done' to finish: ")

# Check if the list is not empty before calculating min and max
if numbers:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
else:
    print("No numbers were entered.")