import random

low = 1
high = 100
options = ["rock", "paper", "scissors"]
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numer = random.randint(low, high)
numer = random.random()
numer = random.choice(options)
random.shuffle(cards)
print(numer)
print(cards)

# print(dir(random))

