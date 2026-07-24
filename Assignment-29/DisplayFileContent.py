'''Write a Python program which accepts a file name from the user, opens that file, and displays the entire contents on the console.

Input:
Demo.txt

Expected Output:
Display contents of Demo.txt on console.'''
filename = input("Enter file name: ")

file = open(filename, "r")

data = file.read()

print(data)

file.close()