#accept one Number and print reverse of that many numbers starting from 1.
def Operation(No):
   for i in range (No,0,-1):
       print(i)
    

def main():
    n=int(input("Enter a Number : "))
    Operation(n)
    


if __name__ =="__main__":
    main()