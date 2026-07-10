'''Write a program that counts how many odd numbers exist between 1 and N.
Input
Data = [1000000, 2000000, 3000000, 4000000]
Expected Output Format
Process ID : 1237
Input Number : 1000000
Odd Number Count : 500000'''
import multiprocessing
import os 

def SumOdd(n):
    sum = 0
    
    for i in range (1,n+1,2):
            sum +=1
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

    print("Sum of Even Numbers is : ")
    print(result)



if __name__ == "__main__":
    main()
