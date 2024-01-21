# Task:
# Create a solution that accepts an integer input representing a 9-digit unformatted student identification number. Output the identification number as a string with no spaces.
# The solution output should be in the format
# 111-22-3333
# Sample Input/Output:
# If the input is
# 154175430
# then the expected output is
# 154-17-5430

def format_student_id(unformatted_id):
    str_id = str(unformatted_id)
    formatted_id = f"{str_id[:3]}-{str_id[3:5]}-{str_id[5:]}"
    return formatted_id

def main():
    # Get user input for the unformatted student ID
    unformatted_id = int(input("Enter the 9-digit unformatted student ID: "))

    # Format the student ID
    formatted_student_id = format_student_id(unformatted_id)

    # Display the formatted student ID
    print(formatted_student_id)

if __name__ == "__main__":
    main()
