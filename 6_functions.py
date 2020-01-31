"""
A function is a block of code which only runs when it is called. 
In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces
"""

# Create function

def sayHello():
    print('Hello')

sayHello()

# Create function with arg

def sayHello(name = 'Default'):
    """
    Print Helo and name.
    """
    print('Hello ' + name)

# sayHello()
sayHello('Roni')

# Return value
# def getSum(num1, num2):
#     total = num1 + num2
#     return total

# print(total)

# print(getSum(2, 2))

# numSum = getSum(3, 3)
# print(numSum)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
print(getSum(9,9))