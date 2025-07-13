Python File Handling Tasks
Task 1: Reading a File and Handling Errors
Problem Statement
Create a program in Python that:

Opens and reads the file sample.txt.

Prints its content line-by-line.

Handles errors gracefully in case the file does not exist. 

Python Code
python
Copy
Edit
try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
Expected Output
If the file exists:

arduino
Copy
Edit
(This will print each line in sample.txt)
If the file does not exist:

javascript
Copy
Edit
Error: The file 'sample.txt' does not exist.
Task 2: Write and Append Data to a File
Problem Statement
Create a Python program that asks:

Takes input from the user and writes it to a file called output.txt.

Stores some more data in the same file.

Reads and prints out the final content of the output file.

Python Code
python
Copy
Edit
# Step 1: Get input from the user and write it to output.txt
user_input = input("Enter some data: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append some more data
with open("output.txt", "a") as file:
    file.write("Additional data appe
