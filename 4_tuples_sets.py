"""
Tuple: Collection which is ordered and unchangeable. Allows duplicate members.
"""

# Create tuple explicit
fruit_tuple = ('apple', 'mango', 'orange')

# Create tuple using constructor
fruit_tuple = tuple(('apple', 'mango', 'orange'))

# Get single value
print(fruit_tuple[1])

# Can't change value
fruit_tuple[1] = 'bla'

# Tuple with one value should have trailing comma
fruit_tuple_one = ('apple',)
print(fruit_tuple_one)

# Tuple only can be deleted whole
del fruit_tuple_one

# Get length
print(len(fruit_tuple))
