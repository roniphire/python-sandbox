"""
JSON is commonly used with data APIS. 
Here to parse JSON into a Python dictionary
"""

import json

# JSON sample
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 18}'

# Parse to dict
user = json.loads(userJSON)
print(user)
print(user['first_name'])

# Parse to JSON
car = {'make': 'Ford', 'model': 'mustang', 'year': 1960}
carJSON = json.dumps(car)
print(carJSON)
