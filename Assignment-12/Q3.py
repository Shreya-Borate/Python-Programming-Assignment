#accept no and do add, sub, mul,div

def Operation(No1,No2):
    Add = No1 + No2
    Sub = No1 - No2
    Mul = No1 * No2
    Div = No1 / No2
    print("Addition is : ",Add)
    print("Subtraction is : ",Sub)
    print("Multiplication is : ",Mul)
    print("Division is : ",Div)
    

def main():
    n1=int(input("Enter a 1st Number : "))
    n2=int(input("Enter a 1st Number : "))
    Operation(n1,n2)
    


if __name__ =="__main__":
    main()