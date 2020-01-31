"""
Variable: a container for a value, which can be of various types

VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
"""
x = 1           # int
y = 2.5         # float
name = 'me'     # string
is_cool = True  # bool
print(is_cool)

# multiple assignment
x, y, name, is_cool = (1, 2.5, 'Me', True)
print(x, y, name, is_cool)

# basic math
a = x + y

# check type
print(type(a))

# casting
x = str(x)
print(type(x))
