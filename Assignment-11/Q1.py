#check prim or not
#accept one no and print all odd numbers till that number
def ChkPrime(No):
    if No <=1:
        return False
    else:
        for i in range (2,int(No**0.5)+1):
            if (No % i == 0):
                return False
            else:
                return True


def main():
    n = int(input("Enter the Number :"))
    
    Ret = ChkPrime(n)
    
    if (Ret==True):
        print("Number ",n," is prime ")
    else:
        print("Number ",n," is not prime ")
if __name__ == "__main__":
    main()
