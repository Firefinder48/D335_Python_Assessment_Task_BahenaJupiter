# Task:
# Create a solution that accepts an integer input. Import the built-in module math and use its factorial() method to calculate the factorial of the integer input. Output the value of the factorial, as well as a Boolean value identifying whether the factorial output is greater than 100.
# The solution output should be in the format
# factorial_value
# Boolean_value
# Sample Input/Output:
# If the input is
# 10
# then the expected output is
# 3628800
# True
# Alternatively, if the input is
# 3
# then the expected output is
# 6
# False

import math

def calculate_factorial_and_compare(input_value):
    factorial_value = math.factorial(input_value)
    is_greater_than_100 = factorial_value > 100
    return factorial_value, is_greater_than_100

def main():
    # Get user input for the integer value
    input_value = int(input("Enter an integer: "))

    # Calculate the factorial and check if it's greater than 100
    factorial_value, is_greater_than_100 = calculate_factorial_and_compare(input_value)

    # Display the results
    print(f"{factorial_value}\n{is_greater_than_100}")

if __name__ == "__main__":
    main()

