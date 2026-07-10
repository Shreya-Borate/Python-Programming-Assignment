'''2. Write a Python program using multiprocessing.Pool to calculate the sum of all odd numbers from 1 to N.
Input
Data = [1000000, 2000000, 3000000, 4000000]
Expected Task

For each number N, calculate:

1 + 3 + 5 + .... + N
Expected Output Format
Process ID : 1235
Input Number : 1000000
Sum of Odd Numbers : 250000000000'''
import multiprocessing
import os 

def SumOdd(n):
    sum = 0
    
    for i in range (1,n+1,2):
            sum +=i
    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Sum of Odd Numbers :", sum)
    print()  
        
    return sum

    

def main():
    lst = [1000,2000,3000,4000]
    
    print(lst)

    pobj = multiprocessing.Pool()

    result =pobj.map(SumOdd,lst)

    pobj.close()

    pobj.join()

    print("Sum of Odd Numbers is : ")
    print(result)



if __name__ == "__main__":
    main()
