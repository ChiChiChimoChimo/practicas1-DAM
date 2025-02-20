

item = input("What is the item? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many items are you buying? "))
total = price * quantity

print(f"The total price of {quantity} {item} is ${total}.")