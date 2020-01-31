"""
Set: Collection which is unordered and un-indexed. No duplicate members.
"""

# Create sets explicitly
fruit_set = {'mango', 'apple', 'banana', 'apple'}

# Check if in set
print('apple' in fruit_set)

# Add to set
fruit_set.add('carrot')

# Remove to set
fruit_set.remove('carrot')

# Clear set
fruit_set.clear()

# Delete set
del fruit_set

print(fruit_set)
