from tabulate import tabulate
# Library management system
## doubt -> can we alias Book or any classname to something shorter
class Book:
    collection = []
    isbnList = []
    copies = []
    # def _init_(self, title, author, isbn ,copies):
    #     self.title = title
    #     self.author = author
    #     Book.copies.append(copies)
    #     self.isbn = isbn

    def addBook(self, book, author, isbn, copies):
        self.book = book
        self.author = author
        self.isbn = isbn
        # dict.update({book: isbn})
        Book.collection.append(book)
        Book.isbnList.append(isbn)
        Book.copies.append(copies)

    def removeBook(self, isbn):
        self.isbn = isbn
        if isbn in Book.isbnList:
            index = Book.isbnList.index(isbn)
            Book.copies[index] -= 1
            print(f"Book removed! Remaining copies: {Book.copies[index]}")
            if Book.copies[index] == 0:
                Book.isbnList.pop(index)
                Book.collection.pop(index)
                Book.copies.pop(index)
    @classmethod
    def findBook(cls, isbn):
        if isbn in cls.isbnList:
            index = cls.isbnList.index(isbn)
            print(f"Book found! Book name is {cls.collection[index]}")
        else:
            print("Book not found")
    @staticmethod
    def displayBookDetails():
        data = list(zip(Book.collection, Book.isbnList, Book.copies))
        print(tabulate(data, headers=["Book Name", "ISBN", "Copies"], tablefmt="grid"))
        print(f"Total copies of books in library are: {sum(Book.copies)}")
end = ''
while end!='n' and end!='N':
    choice = int(input("\n1. Press 1 to add book\n2. Press 2 to remove book\n3. Press 3 to display book details\n4. Press 4 to find book\n5. Exit\nEnter choice: "))
    match choice:
        case 1:
            title = input("Enter title of book: ")
            author = input("Enter author of book: ")
            isbn = int(input("Enter ISBN of book: "))
            copies = int(input("Enter number of copies of book: "))
            book1 = Book()
            book1.addBook(title, author, isbn, copies)
        case 2:
            isbn = int(input("Enter ISBN of book: "))
            Book.removeBook(isbn)
        case 3:
            Book.displayBookDetails()
        case 4:
            isbn = int(input("Enter ISBN of book: "))
            Book.findBook(isbn)
        case 5:
            exit()
# book1 = Book("compound effect", "darren hardy", 211982, 2)
# book1.addBook("the compound effect", 211982)
# book2 = Book("rich dad poor dad", "robert kiyosaki", 121218, 3)
# book2.addBook("rich dad poor dad", 121218)
# Book.displayBookDetails()
# Book.findBook(211982)
# Book.findBook(121921)
# Book.findBook(121218)


# ************************** question-2 ********************************************************

class Employee:
    total_employees = 0
    def _init_(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.total_employees += 1
class Manager(Employee):
    def _init_(self, name, age, salary, department):
        super()._init_(name, age, salary)
        self.department = department
class Developer(Employee):
    def _init_(self, name, age, salary, skill):
        super()._init_(name, age, salary)
        self.skill = skill

m = int(input("Enter the number of managers: "))
d = int(input("Enter the number of developers: "))
manager_data = []
developer_data = []
for i in range(m):
    name = input("Enter the name of manager: ")
    age = int(input("Enter the age of manager: "))
    salary = float(input("Enter the salary of manager: "))
    department = input("Enter the department of manager: ")
    manager = Manager(name, age, salary, department)
    row = [i+1, name, age, salary, department]
    manager_data.append(row)
for i in range(d):
    name = input("Enter the name of developer: ")
    age = int(input("Enter the age of developer: "))
    salary = float(input("Enter the salary of developer: "))
    skill = input("Enter the Skill of developer: ")
    developer = Developer(name, age, salary, skill)
    row = [i+1, name, age, salary, skill]
    developer_data.append(row)
end = ''
while end != 'n' and end != 'n':
    choice = int(input("\n1. Press 1 to display manager details\n2. Press 2 to display developer details\n3. Press 3 to display total number of employees\n4. Enter skill to find developers with specific skill\n5. Print total employees in every department\n6. Exit\nEnter choice: "))
    match choice:
        case 1:
            print("Manager details")
            print(tabulate(manager_data, headers=["#", "Name", "Age", "Salary", "Department"], tablefmt="grid"))
        case 2:
            print("Developer details")
            print(tabulate(developer_data, headers=["#", "Name", "Age", "Salary", "Skill"], tablefmt="grid"))
        case 3:
            print(f"Total number of employees are: {Employee.total_employees}")
        case 4:
            skill = input("Enter the skill to find developers: ")
            for i in developer_data:
                if skill in i:
                    print(f"Name: {i[1]}, Age: {i[2]}, Salary: {i[3]}, Skill: {i[4]}")
        case 5:
            all_employees = manager_data + developer_data
            print(tabulate(all_employees, headers=["#", "Name", "Age", "Salary", "Department/Skill"], tablefmt="grid"))
        case 6:
            exit()
    end = input(f"Do you continue? (y/n): ")
# switch in a function
def switcher(choice):
    match choice:
        case 1:
            print("Manager details")
            result = tabulate(manager_data, headers=["#", "Name", "Age", "Salary", "Department"], tablefmt="grid")
            return result
        case 2:
            print("Developer details")
            result = tabulate(developer_data, headers=["#", "Name", "Age", "Salary", "Skill"], tablefmt="grid")
            return result
        case 3:
            result = f"Total number of employees are: {Employee.total_employees}"
            return result
        case 4:
            skill = input("Enter the skill to find developers: ")
            for i in developer_data:
                if skill in i:
                    print(f"Name: {i[1]}, Age: {i[2]}, Salary: {i[3]}, Skill: {i[4]}")
        case 5:
            exit()
        case _:
            return "Invalid choice"