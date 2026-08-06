'''Write a Python program which accepts a file name from the user and checks whether that file exists in the current directory or not.

Input:
Demo.txt

Expected Output:
Display whether Demo.txt exists or not.'''


import os

def main():
    filename = input("Enter file name: ")
    if(os.path.exists(filename)):
        print("File present in current directory")
    
    else:
        print("File does not exists")


if __name__ == "__main__":
    main()