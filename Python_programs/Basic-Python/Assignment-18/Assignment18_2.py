'''Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.

Input : Number of elements : 7

Input Elements : 13 5 45 7 4 56 34

Output : 56'''
def Display(List):
    largest = 0
    for i in List:
        if i > largest:
            largest = i        

    return largest

    
def main():
    lst = []
    n = int(input("Enter Number of elements : "))
    for i in range (n):
        numbers=int(input())
        lst.append(numbers)

    Ret = Display(lst)
    print(f"Largest Number is : {Ret} ")

if __name__ == "__main__":
    main()