#Accepts no and return cube of that number

def CubeNo(No):
    result = No**3
    return result
    

def main():
    n = int(input("Enter one number : "))
    Ret = CubeNo(n)
    print("Cube of number is : ",Ret)

if __name__ == "__main__":
    main()