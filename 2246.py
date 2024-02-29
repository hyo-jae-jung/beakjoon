from sys import stdin 

N = int(stdin.readline().strip())

DC = []
for _ in range(N):
    DC.append(tuple(map(int,stdin.readline().strip().split())))

for i in sorted(DC):
    print(*i)
