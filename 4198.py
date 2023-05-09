from sys import stdin 

N = int(stdin.readline().strip())
vehicles = [0]
for _ in range(N):
    vehicles.append(int(stdin.readline().strip()))
D = [0]

for i in range(1,len(vehicles)):
    for j in range(i):
        if vehicles[i] > vehicles[j]: