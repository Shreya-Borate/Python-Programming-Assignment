'''• The class should contain one instance variable:
    o Value

• Define a constructor (__init__) that accepts a number from the user and initializes Value.

• Implement the following instance methods:
    o ChkPrime() – returns True if the number is prime, otherwise returns False.
    o ChkPerfect() – returns True if the number is perfect, otherwise returns False.
    o Factors() – displays all factors of the number.
    o SumFactors() – returns the sum of all factors.

• Create multiple objects and call all methods.'''

class Numbers:

    # Constructor
    def __init__(self, Value):
        self.Value = Value

    
    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True

  
    def ChkPerfect(self):
        sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i

        if sum == self.Value:
            return True
        else:
            return False

  
    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()


    def SumFactors(self):
        sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum += i

        return sum



obj1 = Numbers(6)
obj2 = Numbers(11)

# Object 1
print("Object 1")
print("Prime:", obj1.ChkPrime())
print("Perfect:", obj1.ChkPerfect())
obj1.Factors()
print("Sum of Factors:", obj1.SumFactors())

# Object 2
print("\nObject 2")
print("Prime:", obj2.ChkPrime())
print("Perfect:", obj2.ChkPerfect())
obj2.Factors()
print("Sum of Factors:", obj2.SumFactors())