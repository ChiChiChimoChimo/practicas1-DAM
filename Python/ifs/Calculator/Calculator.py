operator = input("Enter operator (+ - * /): ")
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2
else:
    result = "Invalid operator."

print(f"The result is {result}.")