from sys import stdin 

N,M = map(int,stdin.readline().strip().split())

paint = []
for _ in range(N):
    paint.append(list(stdin.readline().strip()))

for i in range(N):
    for j in range(M):
        if paint[i][j] != '.':
            paint[i][-1-j] = paint[i][j]

for i in paint:
    print(''.join(i))
