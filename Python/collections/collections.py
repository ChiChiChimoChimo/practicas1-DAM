# collection = single "variuable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set  = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


fruits = ["apple", "banana", "cherry", "coconut"]
#print(dir(fruits))
#print(help(fruits))
print(len(fruits))
print("apple" in fruits) # Returns True

fruits[2] = "orange"
print(fruits)

fruits.append("grape")
fruits.insert(1, "mango")
fruits.remove("banana")
fruits.sort()
fruits.reverse()
fruits.clear()
fruits.index("apple")
fruits.count("apple")
fruits.pop()

print(fruits[0:3])

for fruit in fruits:
    print(fruit)

fruits = {"apple", "banana", "cherry", "coconut"}
# print(dir(fruits))
# print(help(fruits))
print(len(fruits))
fruits.add("lemon")
fruits.remove("apple")
fruits.pop()
fruits.clear()

fruits = ("apple", "banana", "cherry", "coconut")
# print(dir(fruits))
# print(help(fruits))
print(len(fruits))
print(fruits[0])
print(fruits.index("apple"))