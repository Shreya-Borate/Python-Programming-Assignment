'''Write a program which accept one number and display below pattern.

Input : 5

Output :

*    *    *    *    *
*    *    *    *    *
*    *    *    *    *
*    *    *    *    *
*    *    *    *    *'''
def Display(No):
    for i in range(No):
        for j in range (No):
            print("*",end=" ")
        print()


def main():
    n = int (input("Enter Number : "))
    Display(n)
    

if __name__ == "__main__":
    main()