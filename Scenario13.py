# Task:
# Create a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv". Each file contains two rows of comma-separated values. Import the built-in module csv and use its open() function and reader() method to create a dictionary of key:value pairs for each row of comma-separated values in the specified file. Output the file contents as two dictionaries.
# The solution output should be in the format
# {'key': 'value', 'key': 'value', 'key': 'value'}
# {'key': 'value', 'key': 'value', 'key': 'value'}
# Sample Input/Output:
# If the input is
# input1.csv
# then the expected output is
# {'a': '100', 'b': '200', 'c': '300'}
# {'bananas': '1.85', 'steak': '19.99', 'cookies': '4.52'}
# Alternatively, if the input is
# input2.csv
# then the expected output is
# {'d': '400', 'e': '500', 'f': '600'}
# {'celery': '2.81', 'milk': '4.34', 'bread': '5.63'}

import csv

def printDict(record_dict):
    formatted_dict = ", ".join(f"'{k}': '{v}'" for k, v in record_dict.items())
    print(f"{{{formatted_dict}}}")

def readCsvRecords(filename):
    records = []
    try:
        with open(filename, 'r') as inFile:
            csv_reader = csv.reader(inFile)
            for record in csv_reader:
                record_dict = {record[i].strip(): record[i + 1].strip() for i in range(0, len(record), 2)}
                records.append(record_dict)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
    return records

def main():
    # Prompt for the CSV file name
    filename = input("Enter the CSV file name: ")
    # Read the records from the CSV file
    records = readCsvRecords(filename)
    # Print each record's dictionary
    for record in records:
        printDict(record)

if __name__ == "__main__":
    main()

