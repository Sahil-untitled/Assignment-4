# Python File Handling Tasks

## Task 1: Read a File and Handle Errors

### Problem Statement

Write a Python program that:
1. Opens and reads a text file named `sample.txt`.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.

### Python Code
```python
try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
```

### Expected Output

**If the file exists:**
```
(This will print each line in sample.txt)
```

**If the file does not exist:**
```
Error: The file 'sample.txt' does not exist.
```

---

## Task 2: Write and Append Data to a File

### Problem Statement

Write a Python program that:
1. Takes user input and writes it to a file named `output.txt`.
2. Appends additional data to the same file.
3. Reads and displays the final content of the file.

### Python Code
```python
# Step 1: Take user input and write to output.txt
user_input = input("Enter some data: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data
with open("output.txt", "a") as file:
    file.write("Additional data appended.\n")

# Step 3: Read and display final content
with open("output.txt", "r") as file:
    print("\nFinal content of output.txt:")
    for line in file:
        print(line.strip())
```

### Expected Output

If the user enters:
```
25
```

Then the output will be:
```
Final content of output.txt:
25
Additional data appended.
```
