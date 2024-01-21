# Task:
# Create a solution that accepts an input identifying the name of a text file, for example, "WordTextFile1.txt". Each text file contains three rows with one word per row. Using the open() function and write() and read() methods, interact with the input text file to write a new sentence string composed of the three existing words to the end of the file contents on a new line. Output the new file contents.
# The solution output should be in the format
# word1
# word2
# word3 
# sentence
# Sample Input/Output:
# If the input is
# WordTextFile1.txt
# then the expected output is
# cat
# chases
# dog
# cat chases dog

def modify_and_read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            words = file.readlines()
            words = [word.strip() for word in words]

        sentence = ' '.join(words)
        
        with open(file_name, 'a') as file:
            file.write(sentence + '\n')

        with open(file_name, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return "File not found"

def main():
    file_name = input("Enter the name of the text file: ")
    file_contents = modify_and_read_text_file(file_name)
    print(file_contents)

if __name__ == "__main__":
    main()
    
