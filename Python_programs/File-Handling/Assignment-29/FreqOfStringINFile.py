'''Write a Python program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.

Input:
Demo.txt
Marvellous

Expected Output:
Count how many times "Marvellous" appears in Demo.txt.'''

filename = input("Enter file name: ")
word = input("Enter string to search: ")

file = open(filename, "r")

data = file.read()

file.close()

count = data.count(word)

print("Frequency of", word, "is:", count)