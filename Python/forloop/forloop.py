# for loops = excute a block of code a specified number of times
#            You can iterate over a range, string, sequence etc.

for x in range(10):
    print(x)

for x in reversed(range(10)):
    print(x)

for x in range(5, 10):
    print(x)

for x in range(0, 10, 2):
    print(x)

for x in range(10, 0, -2):
    print(x)

for x in "Python":
    print(x)

for x in range(1, 21):
    if x == 13:
        continue
    print(x)

for x in range(1, 21):
    if x == 13:
        break
    print(x)

for x in range(1, 21):
    if x == 13:
        pass
    print(x)

for x in range(1, 21):
    if x == 13:
        print("Found")
        break
    print(x)


