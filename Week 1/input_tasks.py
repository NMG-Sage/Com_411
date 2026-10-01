# Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")

print("How old are you (in years)?")
age = int(input())

print("How tall are you (in meters)?")
height = float(input())

print("How much do you weigh (in kilograms)?")
weight = float(input())
heightsquared = height * height
bmi = weight / heightsquared
print(f"Your bmi is {bmi}, {name}")
