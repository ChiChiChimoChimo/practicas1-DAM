# input() = A function that prompts the user to enter a data.
# It reads the data entered by the user and returns it as a string.

name = input("What is your name? ")
age = int(input("What is your age? ")) # Convert the string to an integer.

age = age + 1

print(f"Hello, {name}!")
print("Happy Birthday!")
print(f"You are {age} years old.")