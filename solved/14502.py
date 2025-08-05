from sys import stdin   
from copy import deepcopy
from itertools import combinations as comb
from collections import deque

N,M = map(int,stdin.readline().strip().split())
laboratory = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

build_wall = []
for i in range(N):
    for j in range(M):
        if laboratory[i][j] == 0:
            build_wall.append((i,j))

ans = 0
for i in comb(build_wall,3):
    sample_lab = deepcopy(laboratory)
    for y,x in i:
        sample_lab[y][x] = 1
    

    for k in range(N):
        for l in range(M):
            if sample_lab[k][l] == 2:
                q = deque([(l,k)])
                while q:
                    x,y = q.popleft()
                    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N:
                            if sample_lab[ny][nx] == 0:
                                sample_lab[ny][nx] = 3
                                q.append((nx,ny))

    safe_loc_cnt = 0
    for i in range(N):
        for j in range(M):
            if sample_lab[i][j] == 0:
                safe_loc_cnt+=1

    ans = max(ans,safe_loc_cnt)

print(ans)
