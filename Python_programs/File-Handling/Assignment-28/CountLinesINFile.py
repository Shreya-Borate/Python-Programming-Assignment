'''Problem Statement:
Write a Python program which accepts a file name from the user and counts how many lines are present in the file.

Input:
Demo.txt

Expected Output:
Total number of lines in Demo.txt.'''

filename = input("Enter file name : ")

file = open(filename, "r")

count = 0

for line in file:
    count+=1

file.close()

print("Total Number of lines : ",count)