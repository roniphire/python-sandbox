"""
Dictionary: Collection which is unordered, changeable and indexed. No duplicate members.
"""

# Create dict explicitly
person = {
    'first_name': 'Roni',
    'last_name': 'Moe',
    'age': 18
}

# create dict using constractor
person_cst = dict(
    first_name='Roni',
    last_name='Moe',
    age=18
)

# Access value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '0818637559'

# Get keys
print(person.keys())

# Get items
print(person.items())

# Make copy
person2 = person.copy()
person2['city'] = 'Bogor'
print(person2)

# Remove item
del(person['age'])
print(person)
person.pop('phone')
print(person)

# Clear
person.clear()
print(person)

# Length
print(len(person2))

# List of dict
people = [
    {'name': 'Agung', 'age': 40},
    {'name': 'Bagong', 'age': 10}
]
print(people[1]['name'])
