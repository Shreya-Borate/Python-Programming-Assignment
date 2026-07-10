'''3. Write a program that counts how many even numbers exist between 1 and N using Pool.map().
Input
Data = [1000000, 2000000, 3000000, 4000000]
Expected Output Format
Process ID : 1236
Input Number : 1000000
Even Number Count : 500000'''
import multiprocessing
import os 

def SumEven(n):
    sum = 0
    
    for i in range (2,n+1,2):
            sum +=1
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
