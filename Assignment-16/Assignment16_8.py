'''Write a program which accept number from user and print that number of "*" on screen.

Input : 5

Output :

*  *  *  *  *'''
def Display(No):
    for i in range (No):
        print("*")

def main():
    no = int(input("Enter a number : "))
    Display(no)
    

if __name__ == "__main__":
    main()