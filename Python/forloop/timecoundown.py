import time

my_time = int(input("Enter the time in seconds: "))
for i in range(my_time, 0 , -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02d}:{seconds:02d}", end="\r")
    time.sleep(1)

print("TIME IS UP!")

