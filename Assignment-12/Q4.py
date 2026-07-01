#accept one Number and print that many numbers starting from 1.
def Operation(No):
   for i in range (1,No+1):
       print(i)
    

def main():
    n=int(input("Enter a Number : "))
    Operation(n)
    


if __name__ =="__main__":
    main()