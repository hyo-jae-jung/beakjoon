from sys import stdin 

N = int(stdin.readline().strip())

cars = dict()
for i in range(N):
    cars[stdin.readline().strip()]=i

for i in range(N):
    cars[stdin.readline().strip()]-=i

print(N-len([i for i in list(cars.values()) if i < 0]))
