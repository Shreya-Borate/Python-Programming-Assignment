'''• The class should contain two instance variables:
    o Name (Book Name)
    o Author (Book Author)

• The class should contain one class variable:
    o NoOfBooks (initialize it to 0)

• Define a constructor (__init__) that accepts Name and Author and initializes the instance variables.

• Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created.

• Implement an instance method:
    o Display() – should display book details in the following format:
      <BookName> by <Author>. No of books: <NoOfBooks>

• Create multiple objects of the BookStore class and invoke the Display() method.'''

class BookStore:

    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks +=1
    
    def Display(self):
        print(self.Name, "by",self.Author + "." , "No of books : ", BookStore.NoOfBooks)


obj1 = BookStore("Linux System Programing","Robert Love")
obj1.Display()

obj2 = BookStore("Linux System Programing","Robert Love")
obj2.Display()

obj3 = BookStore("C Programming", "Dennis Ritchie")
obj3.Display()