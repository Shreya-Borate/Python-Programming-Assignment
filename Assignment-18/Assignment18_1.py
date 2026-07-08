'''Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

Input : Number of elements : 6

Input Elements : 13 5 45 7 4 56

Output : 130'''
def Display(List):
    sum = 0
    for l in List:
        sum +=l

    return sum

    
def main():
    lst = []
    n = int(input("Enter Number of elements : "))
    for i in range (n):
        numbers=int(input())
        lst.append(numbers)

    Ret = Display(lst)
    print(Ret)

if __name__ == "__main__":
    main()