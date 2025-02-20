fruits = ["apple", "banana", "cherry", "coconut"]
vegetables = ["carrot", "cucumber", "celery", "cabbage"]
meats = ["beef", "chicken", "pork", "lamb"]
foods = [fruits, vegetables, meats]
print(foods)

for food in foods:
    for x in food:
        print(x, end=" ")
    print()