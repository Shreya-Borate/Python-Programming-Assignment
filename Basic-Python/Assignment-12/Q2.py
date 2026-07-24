#print factors of number

def Factors(No):
    for i in range (1,No+1):
        if (No % i ==0):
            print(i)

    
def main():
    n=int(input("Enter a Number : "))
    Factors(n)


if __name__ =="__main__":
    main()