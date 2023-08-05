from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
locs = []
for i in range(N):
    for j,k in enumerate(list(stdin.readline().strip().split())):
        if k == '1':
            locs.append((i,j))

print(abs(locs[0][0]-locs[1][0])+abs(locs[0][1]-locs[1][1]))
