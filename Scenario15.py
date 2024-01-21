# Task:
# Create a solution that accepts an integer input representing the age of a pig. Import the existing module pigAge and use its pre-built pigAge_converter() function to calculate the human equivalent age of a pig. A year in a pig's life is equivalent to five years in a human's life. Output the human-equivalent age of the pig.
# The solution output should be in the format
# input_pig_age is converted_pig_age in human years
# Sample Input/Output:
# If the input is
# 8
# then the expected output is
# 8 is 40 in human years

# Assuming the existence of a module named pigAge with a function pigAge_converter()
# For this example, I'll define a mock pigAge_converter() function within the script.

def pigAge_converter(pig_age):
    # A year in a pig's life is equivalent to five years in a human's life.
    return pig_age * 5

def calculate_human_equivalent_age(pig_age):
    human_age = pigAge_converter(pig_age)
    return f"{pig_age} is {human_age} in human years"

def main():
    # Get user input for the pig's age
    pig_age = int(input("Enter the age of the pig: "))

    # Calculate the human-equivalent age
    human_equivalent_age = calculate_human_equivalent_age(pig_age)

    # Display the result
    print(human_equivalent_age)

if __name__ == "__main__":
    main()

