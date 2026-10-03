import random

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


print("=== BMI Calculator ===")

person = input("Are you an Adult or a Child? ").lower()

name = input("Enter your name: ")
surname = input("Enter your surname: ")

if person == "adult":
    age = random.randint(18, 80)
    print(f"Age: {age} years old")

    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)

    print(f"\nYour BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 24.9:
        print("Category: Normal weight")
    elif bmi < 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obese")


elif person == "child":
    age = random.randint(2, 17)
    print(f"Age: {age} years old")

    gender = input("Enter your gender (boy/girl): ").lower()

    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)

    print(f"\nYour BMI is: {bmi:.2f}")

    print("For children, BMI is interpreted according to age and gender.")
    print("A BMI percentile is needed to determine the exact category.")


else:
    print("Please enter Adult or Child.")