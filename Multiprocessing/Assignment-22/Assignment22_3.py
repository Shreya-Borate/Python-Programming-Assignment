'''3. For every number in the given list, count how many prime numbers exist between 1 and N using a multiprocessing Pool.

Example Input

10000
20000
30000
40000

Display

Total prime count for each number.'''
import multiprocessing
import os 

def CountPrime(n):
    count = 0
    for num in range (2,n+1):
        is_prime = True
        for i in range (2,num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count +=1
        
    return count

    

def main():
    lst = [1000,2000,3000,4000]
    
    print(lst)

    pobj = multiprocessing.Pool()

    result =pobj.map(CountPrime,lst)

    pobj.close()

    pobj.join()

    print("Count of prime number is  : ")
    print(result)



if __name__ == "__main__":
    main()

