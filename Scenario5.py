# Task:
# Create a solution that accepts five integer inputs. Output the sum of the five inputs three times, converting the inputs to the requested data type prior to finding the sum.
#    First output: sum of five inputs maintained as integer values
#    Second output: sum of five inputs converted to float values
#    Third output: sum of five inputs converted to string values (concatenate)
# The solution output should be in the format
# Integer: integer_sum_value
# Float: float_sum_value
# String: string_sum_value
# Sample Input/Output:
# If the input is
# 1
# 3
# 6
# 2
# 7
# then the expected output is
# Integer: 19
# Float: 19.0
# String: 13627

def sum_of_inputs_as_different_types(input1, input2, input3, input4, input5):
    # Sum as integers
    integer_sum = input1 + input2 + input3 + input4 + input5

    # Sum as floats
    float_sum = float(input1) + float(input2) + float(input3) + float(input4) + float(input5)

    # Concatenation as strings
    string_sum = str(input1) + str(input2) + str(input3) + str(input4) + str(input5)

    return integer_sum, float_sum, string_sum

def main():
    # Get user input for the five integers
    inputs = []
    for i in range(1, 6):
        value = int(input(f"Enter integer {i}: "))
        inputs.append(value)

    # Calculate the sums in different formats
    integer_sum, float_sum, string_sum = sum_of_inputs_as_different_types(*inputs)

    # Display the results
    print(f"Integer: {integer_sum}\nFloat: {float_sum}\nString: {string_sum}")

if __name__ == "__main__":
    main()

