"""
List:  Collection which is ordered and changeable. Allows duplicate members.
"""

# Create list explicitly
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Using a constructor
fruits = list(('apple', 'mango', 'orange', 'lemon'))
print(fruits)

# Get value
print(fruits[1])

# Get len
print(len(fruits))

# Append to list
fruits.append('grapes')

# Remove from list
fruits.remove('grapes')

# Insert into position
fruits.insert(2, 'blueberries')

# Remove from position
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)
