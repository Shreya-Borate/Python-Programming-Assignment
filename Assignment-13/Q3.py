# write a program which accepts one no and checks whatether it is perfect number or not.
def ChkPerfect(No):
    sum = 0
    for i in range (1,No):
        if No % i == 0:
            sum += i

    if sum == No:
        return True
    else:
        return False

    
def main():
    n=int(input("Enter a Number : "))
    
    Ret = ChkPerfect(n)

    if (Ret==True) :
        print("The Number is perfect ")
    else:
        print("The Number is not perfect ")

    

if __name__ =="__main__":
    main()