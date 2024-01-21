# Task:
# Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site. Output the total distance traveled to two decimal places given the following miles per employee commute to the job site. Output the total distance traveled to two decimal places given the following miles per employee commute to the job site:
#    Employee A: 15.62 miles
#    Employee B: 41.85 miles
#    Employee C: 32.67 miles
# The solution output should be in the format
# Distance: total_miles_traveled
# Sample Input/Output:
# If the input is
# 1
# 2
# 3
# then the expected output is
# Distance: 197.33 miles

def total_distance_traveled(travels_a, travels_b, travels_c):
    miles_employee_a = 15.62
    miles_employee_b = 41.85
    miles_employee_c = 32.67

    # total_distance = (miles_employee_a * travels_a) + (miles_employee_b * travels_b) + (miles_employee_c * travels_c)
    return round((miles_employee_a * travels_a) + (miles_employee_b * travels_b) + (miles_employee_c * travels_c), 2)

def main():
    # Get user input for the number of travels for each employee
    travels_employee_a = int(input("Enter the number of travels for Employee A: "))
    travels_employee_b = int(input("Enter the number of travels for Employee B: "))
    travels_employee_c = int(input("Enter the number of travels for Employee C: "))

    # Calculate the total distance traveled
    total_miles_traveled = total_distance_traveled(travels_employee_a, travels_employee_b, travels_employee_c)

    # Display the result
    print(f"Distance: {total_miles_traveled} miles")

if __name__ == "__main__":
    main()

