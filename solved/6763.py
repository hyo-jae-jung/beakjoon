from sys import stdin  

speed_limit = int(stdin.readline().strip())
speed_of_car = int(stdin.readline().strip())

diff = speed_of_car - speed_limit

if diff < 1:
    print("Congratulations, you are within the speed limit!")
elif 1<= diff <=20:
    print("You are speeding and your fine is $100.")
elif 21<= diff <=30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")
    