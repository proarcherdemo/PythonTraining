class Person:   # Base/ Parent class
    # Attributes
    def __init__(self, i, n, a):
        self.id = i
        self.name = n
        self.address = a

    # Behaviours/Methods/Functions
    def walks(self):
        print(self.name + ' is walking')


    def works(self):
        print(self.name + ' is working')


# Child/ Derived class 
class Employee(Person):  # class Employee inherits from Person class
    def __init__(self, i, n , a, cn):
        self.company_name = cn                 # addition attribute to Employee
        super().__init__(i, n , a)

    def learn_coding(self):                   # Additional Behaviour to Employee
        print(self.name + ' is learing how to code')
        




# creating the person instance
person = Person(1001, 'Ramesh', 'Pune')

# Accessing the base class members
print(person.id)
print(person.name)
print(person.address)
person.walks()
person.works()


# Creating the instance of derived class., Employee
emp = Employee(1002, 'Mohan', 'Pune', 'XYZ tech') # invoke __init__()
# emp = Employee() # invoke __init__()

# Accessing the child class members
print(emp.id)
print(emp.name)
print(emp.address)
print(emp.company_name)
emp.walks()
emp.works()
emp.learn_coding()

person.learn_coding()
