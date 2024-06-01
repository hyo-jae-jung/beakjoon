from sys import stdin 

weight = float(stdin.readline().strip())
height = float(stdin.readline().strip())

BMI = weight/(height**2)

if BMI > 25:
    print("Overweight")
elif 18.5 <= BMI <= 25:
    print("Normal weight")
else:
    print("Underweight")
