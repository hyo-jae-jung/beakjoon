from sys import stdin 

M = int(stdin.readline().strip())
cups = [0,1,0,0]
for _ in range(M):
    X,Y = map(int,stdin.readline().strip().split())
    cups[X],cups[Y] = cups[Y],cups[X]

print(cups.index(1))
