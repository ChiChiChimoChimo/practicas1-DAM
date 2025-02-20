import math

print(math.pi)
print(math.e)

result = math.sqrt(25)
result = math.ceil(2.9) # Redondea hacia arriba
result = math.floor(2.9) # Redondea hacia abajo

print(result)

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"The circumference of the circle is {round(circumference), 2}.")
print(f"The area of the circle is {round(area), 2}.")

a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse of the triangle is {round(c), 2}.")