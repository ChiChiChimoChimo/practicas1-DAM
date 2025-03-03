# List comprehension = A concise way to create lists
#                      Compact and easier to read than traditional for loops
#                      Syntax: [expression for value in iterable if condition]
#                      The condition is optional

# doubles = []
# for x in range(1, 6):
#     doubles.append(x * 2)

# print(doubles)

doubles = [x * 2 for x in range(1, 6)]
print(doubles)

triples = [y * 3 for y in range(1, 6)]
print(triples)

squares = [z ** 2 for z in range(1, 6)]
print(squares)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits_upper = [fruit.upper() for fruit in fruits]
print(fruits_upper)