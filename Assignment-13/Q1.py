#program that accepts len and width and returns area.
def RecArea(Len,Wid):
    Area = Len*Wid
    return Area

    
def main():
    length=int(input("Enter a length Number : "))
    width=int(input("Enter a width Number : "))
    Ret = RecArea(length,width)

    print("Area of rectangle is : ",Ret)

if __name__ =="__main__":
    main()