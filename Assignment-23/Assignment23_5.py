'''Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.
Input
Data = [10, 15, 20, 25]
Expected Task

For every N, calculate:

N!
Expected Output Format
Process ID : 1240
Input Number : 20
Factorial : 2432902008176640000'''
import multiprocessing
import os 

def Factorial(n):
    Fact = 1
    
    for i in range (1,n+1):
            Fact = Fact*i
    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Factorial of  Numbers :", Fact)
    print()  
        
    return Fact

    

def main():
    lst = [10,15,20,25]
    
    print(lst)

    pobj = multiprocessing.Pool()

    result =pobj.map(Factorial,lst)

    pobj.close()

    pobj.join()

    print("Factorial of  Numbers is : ")
    print(result)



if __name__ == "__main__":
    main()
