#write program to display
#Data type
#memory address
#size in bytes
#of variable entered by the user.

import sys

value = eval(input("Enter the value : "))

print("Data type is : ",type(value))
print("Memory Address : ", id(value))
print("size in Bytes :", sys.getsizeof(value))
