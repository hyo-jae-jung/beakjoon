from sys import stdin  
from collections import deque 

N,M = map(int,stdin.readline().strip().split())
ladders_and_snakes = list(range(101))

for _ in range(N):
    x,y = map(int,stdin.readline().strip().split())
    ladders_and_snakes[x] = y

for _ in range(M):
    u,v = map(int,stdin.readline().strip().split())
    ladders_and_snakes[u] = v

board = [float('inf')]*101
q = deque([(1,0)])

while q:
    loc,step = q.popleft()
    if loc == 100:
        ans = step
        break
    for i in range(1,7):
        if 1 <= loc+i <= 100 and board[loc+i] > step + 1:
            q.append((ladders_and_snakes[loc+i],step+1))
            board[loc+i] = step + 1

print(ans)
