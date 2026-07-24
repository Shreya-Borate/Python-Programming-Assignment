'''1. Write a Python program using multiprocessing.Pool to calculate the sum of all even numbers from 1 to N for every number from the given list.
Input
Data = [1000000, 2000000, 3000000, 4000000]
Expected Task

For each number N, calculate:

2 + 4 + 6 + .... + N
Expected Output Format
Process ID : 1234
Input Number : 1000000
Sum of Even Numbers : 250000500000'''
import multiprocessing
import os 

def SumEven(n):
    sum = 0
    
    for i in range (2,n+1,2):
            sum +=i
    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Sum of Even Numbers :", sum)
    print()  
        
    return sum

    

def main():
    lst = [1000,2000,3000,4000]
    
    print(lst)

    pobj = multiprocessing.Pool()

    result =pobj.map(SumEven,lst)

    pobj.close()

    pobj.join()

    print("Sum of Even Numbers is : ")
    print(result)



if __name__ == "__main__":
    main()
