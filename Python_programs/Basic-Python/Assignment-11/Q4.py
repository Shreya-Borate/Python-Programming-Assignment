#write a program which accepts one number and prints reverse of that number.
def ReverseNo(No):
    rev = No[::-1]
    return rev



def main():
    n=input("Enter a number : ")
    Ret = ReverseNo(n)
    
    print("Reverse is : ",Ret)

if __name__ == "__main__":
    main()