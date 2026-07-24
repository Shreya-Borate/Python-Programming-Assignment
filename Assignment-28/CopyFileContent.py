'''Write a Python program which accepts two file names from the user.

• First file is an existing file.

• Second file is a new file.

Copy all contents from the first file into the second file.

Input:
ABC.txt Demo.txt

Expected Output:
Contents of Demo.txt copied into ABC.txt .'''

filename1 = input("Enter existing file name: ")
filename2 = input("Enter new file name: ")

file1 = open(filename1, "r")
file2 = open(filename2, "w")

for line in file1:
    file2.write(line)

file1.close()
file2.close()

print("Contents of", filename1, "copied into", filename2)