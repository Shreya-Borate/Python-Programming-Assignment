#program that accepts radius and returns area of circle.
def CircleArea(rad):
    Area = 3.14 *rad*rad
    return Area

    
def main():
    radius=int(input("Enter a Radius of circle : "))
    
    Ret = CircleArea(radius)

    print("Area of Circle is : ",Ret)

if __name__ =="__main__":
    main()