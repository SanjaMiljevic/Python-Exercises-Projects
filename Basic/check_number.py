# The program prompts the user to submit a number in the console.
# Once the user submits a number (e.g., -11), the program checks
# the sign of the number (e.g., negative, zero, or positive) and
# returns a message accordingly.

number_input = int(input("Enter a number: "))

if number_input == 0:
    print("The number is zero.")
elif number_input > 0:
    print("The number is positive")
else:
    print("The number is negative.")
