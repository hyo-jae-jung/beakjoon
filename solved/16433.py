import sys

N,R,C = map(int,sys.stdin.readline().strip().split())

farm = [["."]*N for _ in range(N)]

rest = (R+C)%2

for i in range(N):
    for j in range(N):
        if (i+j)%2 == rest:
            farm[i][j] = 'v'

for i in farm:
    print(''.join(i))
