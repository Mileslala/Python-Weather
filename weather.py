import random


days = int(input("Enter the number of days: "))


for i in range(days):

    temp = random.randint(50, 100)
    print(f"Day {i + 1} temperature: {temp}°F")
