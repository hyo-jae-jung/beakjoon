from sys import stdin 

date = int(stdin.readline().strip())
cars = list(map(int,stdin.readline().strip().split()))
print(cars.count(date))
