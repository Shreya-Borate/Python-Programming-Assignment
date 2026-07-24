'''Problem Statement:
Write a Python program which accepts a file name from the user and counts the total number of words in that file.

Input:
Demo.txt

Expected Output:
Total number of words in Demo.txt.'''

filename = input("Enter file name : ")

file = open(filename, "r")

count = 0

for line in file:
    words = line.split()
    count +=len(words)

file.close()

print("Total Number of words : ",count)