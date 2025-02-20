age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age < 0:
    print("You are not born yet.")
elif age >= 100:
    print("You are a centenary.")
else:
    print("You are an adult.")