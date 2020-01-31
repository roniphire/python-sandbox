"""
Strings:  Surrounded by either single or double quotation marks.
"""

dog = 'Pluto'
age = 200

# Concatenate
print('hello ' + dog + ' I am ' + str(age) + ' years old, bro...')

# Arguments by position
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name
print('My world is {emotion} and I am {action}'.format(
    emotion='sad', action='kill'))

# F-string (only v3.6+)
print(f'my name is {dog} and {age} years old.')

# String Methods
s = 'hello world'

# Capitalize 1st letter
print(s.capitalize())

# All uppercase
print(s.upper())

# All lowercase
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'hell'))

# Count letter
sub = 'H'
print(s.count(sub))

# Start with
print(s.startswith('hello'))

# End with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
