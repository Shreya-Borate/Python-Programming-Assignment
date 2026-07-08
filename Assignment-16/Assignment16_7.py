'''Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.

Input : 8
Output : False

Input : 25
Output : True'''
def Numchk(No):
    return (No%5 == 0)
def main():
    no = int(input("Enter a number : "))
    Ret = Numchk(no)
    print(Ret)
  
    

if __name__ == "__main__":
    main()