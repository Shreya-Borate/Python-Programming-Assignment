'''1. Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.

Example Input

[1000000, 2000000, 3000000, 4000000]

Expected Output

[
333333833333500000,
2666668666667000000,
9000004500000500000,
21333341333334000000
]'''
import multiprocessing
import os 

def SumSquare(list):
    print("Process is running with pid : ",os.getpid())
    sum = 0
    for i in range (1,list+1):
        sum = sum + (i**2)
    
    return sum 

    

def main():
    lst = []
    result = []
    n=int(input("Enter Number of Elements: "))
    
    for i in range (n):
        nums = int(input("Enter Elements :"))
        lst.append(nums)

    pobj = multiprocessing.Pool()

    result =pobj.map(SumSquare,lst)

    pobj.close()

    pobj.join()

    print("Result is : ")
    print(result)



if __name__ == "__main__":
    main()