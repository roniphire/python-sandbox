"""
A module is basically a file containing a set of functions to include in your application. 
There are core python modules, modules you can install using the pip package manager (including Django) as well as 
custom modules
"""

# Core modules
# import datetime # import all module attributes
# from datetime import date # import part attribute of module

# today = datetime.date.today()
# today = date.today()
# print(today)

# pip modules
# import camelcase

# camel = camelcase.CamelCase()
# text = 'hello world'
# print(camel.hump(text))

# Custom module
import validator

email = 'test@test.com'
if validator.validate_email(email):
    print('Email is valid.')
else:
    print('Email not valid')

