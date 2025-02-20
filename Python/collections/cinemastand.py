menu = {"popcorn": 5.00, "soda": 2.50, "candy": 3.20, "pizza": 7.00, "hotdog": 4.99}

cart = []
total = 0

print("--------Menu--------")
for key, value in menu.items():
    print(f"{key:10} - ${value:.2f}")
print("--------------------")

while True:
    item = input("What would you like to order? (q to quit): ").lower()
    if item == "q":
        break
    elif menu.get(item) is not None:
        cart.append(item)
        total += menu[item]

print("--------Cart--------")
for item in cart:
    print(item)
print("--------------------")
print(f"Total: ${total:.2f}")