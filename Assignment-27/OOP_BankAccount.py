'''• The class should contain two instance variables:
    o Name (Account holder name)
    o Amount (Account balance)

• The class should contain one class variable:
    o ROI (Rate of Interest), initialized to 10.5

• Define a constructor (__init__) that accepts Name and initial Amount.

• Implement the following instance methods:
    o Display() – displays account holder name and current balance.
    o Deposit() – accepts an amount from the user and adds it to the balance.
    o Withdraw() – accepts an amount from the user and subtracts it from the balance (ensure withdrawal is allowed only if sufficient balance exists).
    o CalculateInterest() – calculates and returns interest using the formula:
      Interest = (Amount * ROI) / 100

• Create multiple objects and demonstrate all methods.'''

class BankAccount:

    # Class Variable
    ROI = 10.5

    # Constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    # Display Method
    def Display(self):
        print("Account Holder Name :", self.Name)
        print("Current Balance :", self.Amount)

    
    def Deposit(self):
        deposit = float(input("Enter Deposit Amount: "))
        self.Amount += deposit
        print("Amount Deposited Successfully.")

    
    def Withdraw(self):
        withdraw = float(input("Enter Withdrawal Amount: "))
        if withdraw <= self.Amount:
            self.Amount -= withdraw
            print("Amount Withdrawn Successfully.")
        else:
            print("Insufficient Balance.")

    # Calculate Interest
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest



obj1 = BankAccount("Shreya", 10000)
obj2 = BankAccount("Rahul", 5000)


print("Details of Object 1")
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
print("Interest =", obj1.CalculateInterest())
obj1.Display()


print("\nDetails of Object 2")
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
print("Interest =", obj2.CalculateInterest())
obj2.Display()