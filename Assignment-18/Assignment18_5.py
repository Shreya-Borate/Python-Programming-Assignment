'''Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().

Input : Number of elements : 11

Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 54'''
from MarvellousNum import *
def ListPrime(List):
    sum = 0
    for i in List:
        if ChkPrime(i):
            sum += i

    return sum
    

    
def main():
    lst = []
    n = int(input("Enter Number of elements : "))
    for i in range (n):
        numbers=int(input())
        lst.append(numbers)
    

    Ret = ListPrime(lst)
    print(f"Addition of prime num is  : {Ret} ")

if __name__ == "__main__":
    main()