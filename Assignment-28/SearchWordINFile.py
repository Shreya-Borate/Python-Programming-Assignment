'''Write a Python program which accepts a file name and a word from the user and checks whether that word is present in the file or not.

Input:
Demo.txt
Ganesh

Expected Output:
Display whether the word Ganesh is found in Demo.txt or not.'''

filename = input("Enter file name: ")
word = input("Enter word to search: ")

file = open(filename, "r")

data = file.read()

file.close()

if word in data:
    print(f"{word} is present in the file. ")

else:
   print(f"{word} is not present in the file. ")  
