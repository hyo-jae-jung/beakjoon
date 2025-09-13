from sys import stdin  
from heapq import heappop, heappush

M,N = map(int,stdin.readline().strip().split())
room = [list(map(int,list(stdin.readline().strip()))) for _ in range(N)]
visited = [[float('inf')]*M for _ in range(N)]

h = [(0,0,0)]
visited[0][0] = 0

while h:
    break_cnt,x,y = heappop(h)

    if x == M-1 and y == N-1:
        print(break_cnt)
        break

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        tmp = break_cnt
        if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N:
            if room[ny][nx] == 1:
                tmp+=1
            if visited[ny][nx] > tmp:
                visited[ny][nx] = tmp
                heappush(h,(tmp,nx,ny))

