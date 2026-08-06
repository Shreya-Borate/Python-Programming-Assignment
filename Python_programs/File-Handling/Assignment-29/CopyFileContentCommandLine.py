'''Write a Python program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.

Input (Command Line):
ABC.txt

Expected Output:
Create ABC.txt and copy contents of Demo.txt into ABC.txt.'''


import sys

source = sys.argv[1]

file1 = open(source, "r")
file2 = open("ABC.txt", "w")

for line in file1:
    file2.write(line)

file1.close
file2.close

print("Contents copied successfully")