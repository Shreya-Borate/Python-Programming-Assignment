'''Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

Input : 11 5
Output : 16'''
def Add (No1,No2):
    return No1 + No2

def main():
    n1 = int(input("Enter 1st number : "))
    n2 = int(input("Enter 2nd number : "))
    Ret = Add(n1,n2)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()