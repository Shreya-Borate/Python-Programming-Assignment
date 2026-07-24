'''Problem Statement:
Write a Python program which accepts a file name from the user and displays the contents of the file line by line on the screen.

Input:
Demo.txt

Expected Output:
Display each line of Demo.txt one by one.'''

filename = input("Enter file name : ")

file = open(filename, "r")

count = 0

for line in file:
    print(line)

file.close()

