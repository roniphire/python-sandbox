"""
A class is a blueprint for creating objects. 
An object has properties and methods(functions) associated with it. 
Almost everything in Python is an object
"""

# Create class


class User:
    # Constructor/property
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # Method
    def greeting(self):
        return f'My name is {self.name} and {self.age} years old.'

    def has_birthday(self):
        self.age += 1

# Passing Class


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and {self.age} years old. Balance: {self.balance}.'


# Init user object
roni = User('Roni', 'test@test.com', 17)

# Edit property
roni.age = 27
print(roni.age)
roni.has_birthday()

# Call property
print(roni.name)

# Call Method
print(roni.greeting())

# Init Customer
ronimoe = Customer('Roni Moe', 'test@test.com', 17)
ronimoe.set_balance(200000)
print(ronimoe.greeting())
