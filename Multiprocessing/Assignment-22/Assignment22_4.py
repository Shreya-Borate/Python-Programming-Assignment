'''4. Write a program that calculates

1^5 + 2^5 + 3^5 + ... + N^5

for multiple values of N simultaneously using Pool.

Input

[
1000000,
2000000,
3000000,
4000000
]

Measure

Total execution time.'''
import multiprocessing
import os 
import time


def SumSquare(list):
    print("Process is running with pid : ",os.getpid())
    for i in range (1,list+1):
        sum =  (i**5)
    
    return sum 

    

def main():
    lst = []
    result = []
    n=int(input("Enter Number of Elements: "))

    
    for i in range (n):
        nums = int(input("Enter Elements :"))
        lst.append(nums)
    
    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    result =pobj.map(SumSquare,lst)

    pobj.close()

    pobj.join()

    end_time = time.perf_counter()

    

    print("Result is : ")
    print(result)

    print(f"Time Required : {end_time - start_time:.4f} seconds ")

if __name__ == "__main__":
    main()