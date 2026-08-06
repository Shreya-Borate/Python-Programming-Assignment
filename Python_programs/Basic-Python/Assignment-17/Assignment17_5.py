'''Write a program which accept one number for user and check whether number is prime or not.

Input : 5
Output : It is Prime Number'''
def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def main():
    n = int(input("Enter Number : "))

    Ret = ChkPrime(n)

    if Ret:
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")

if __name__ == "__main__":
    main()