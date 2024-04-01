try:    
    with open("my_file.txt", "w") as file:
        file.write("My name is Kelvin\n")
        file.write("This is a test file.\n")
        file.write("0795501941")
# File Reading and Display
    with open("my_file.txt", "r") as file:
        print(file.read())        
        # File Appending
    with open("my_file.txt", "a") as file:
        file.write("\nI go to PLP Academy.")
        file.write("\nMy other number is 0708905030")
        file.write("\nFinal line.")

    with open("my_file.txt", "r") as file:
        print(file.read())
        
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("File handling operations completed. Make sure to check the 'my_file.txt' file for the output.")