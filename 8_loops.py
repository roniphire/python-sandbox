"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
"""

numbers = [1, 2, 3, 4, 5]
alpha = ['a', 'b', 'c', 'd', 'e']

# Simple for loops
# for numbers in numbers:
#     print('Current number:', numbers)

# Break out
# for numbers in numbers:
#     if numbers == 2:
#         break
#     print('Current number:', numbers)
    # if numbers == 2:
    #     break

# Continue
# for numbers in numbers:
#     if numbers == 2:
#         continue
#     print('Current number:', numbers)

# for alpha in alpha:
#     if alpha == 'b':
#         continue
#     print('Current alphabet:', alpha)

# Range
# for i in range(len(alpha)):
#     print('Current alphabeth:', alpha[i])

# for i in range(0, 10):
#     print('Number: ', i)


# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10:
    print('Count: ', count)
    count += 1