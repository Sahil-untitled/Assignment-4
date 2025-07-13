
def read_file():
    file_path = "C:\\Users\\Sahil\\Desktop\\Assignments\\sample.txt"
    try:
        with open(file_path, "r") as file:
            print("File content: ""\n")
            for line in file:
                print(line.strip())            
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def write_file():
    user_input = input("Enter the content you want to add: ")
    file_path = "C:\\Users\\Sahil\\Desktop\\Assignments\\sample.txt"
    with open(file_path, "w") as file:
        file.write(user_input)
        
    additional_content = input("Add additional input(if any)(1 if no additional input): ")
    while additional_content != "1":
        with open(file_path, "a") as file:
           file.write("\n" + additional_content)
        additional_content = input("Add more input (or type '1' to finish): ")

        
    with open(file_path, "r") as file:
        content = file.read()
        
    print("Final content of the file: ")
    print(content)
        
write_file()