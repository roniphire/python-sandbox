"""
Python functions for creating, reading, updating, and deleting files.
"""


# Open file
myFile = open('myfile.txt', 'w')

# Get info on file
print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

# Write to file
myFile.write('Python in me.')
myFile.write('Js is the king.')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' But PHP still ruling!')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(10)
print(text)
