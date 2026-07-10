'''2. Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().

Input

[10, 15, 20, 25]

Display

Process ID
Input Number
Factorial'''
import multiprocessing
import os 

def Factorial(list):
    print("Process is running with pid : ",os.getpid())
    fact=1
    for i in range (1,list+1):
        fact = fact*i
    
    return fact

    

def main():
    lst = []
    result = []
    n=int(input("Enter Number of Elements: "))
    
    for i in range (n):
        nums = int(input("Enter Elements :"))
        lst.append(nums)
    print(lst)

    pobj = multiprocessing.Pool()

    result =pobj.map(Factorial,lst)

    pobj.close()

    pobj.join()

    print("Factorial is  is : ")
    print(result)



if __name__ == "__main__":
    main()
