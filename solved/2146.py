import sys
sys.setrecursionlimit(10**5)
from collections import deque

N = int(sys.stdin.readline().strip())
island_map = []
for _ in range(N):
    island_map.append(list(map(int,sys.stdin.readline().strip().split())))

def dfs(x,y):

    if island_map[y][x] == 1:
        island_map[y][x] = 2

        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if x+dx >= 0 and y+dy >= 0 and x+dx < N and y+dy < N and island_map[y+dy][x+dx] != 2:
                dfs(x+dx,y+dy)
        return True

    if island_map[y][x] <= 0:
        island_map[y][x] = -1
        s.add((x,y))

def bfs(s):

    q = deque(s)

    while q:
        a,b = q.popleft()

        for da,db in [(-1,0),(1,0),(0,-1),(0,1)]:
            if a+da >= 0 and b+db >= 0 and a+da < N and b+db < N:
                if island_map[b+db][a+da] == 0:
                    island_map[b+db][a+da] = island_map[b][a] - 1
                    q.append((a+da,b+db))
                elif island_map[b+db][a+da] == 1:
                    return -island_map[b][a]
                
    return 200

ans = 200
for i in range(N):
    for j in range(N):
        s = set()
        if island_map[i][j] == 1:
            dfs(j,i)
            ans = min(ans,bfs(s))

print(ans)

"""
오랜 시간이 걸린 해결로 그냥 넘기기 싫어서 메모를 남긴다.

기본적으로 섬은 dfs로 찾고 다리는 bfs로 찾는 방법론으로

섬을 찾아마자 최단거리 다리를 찾는 방식으로 중복 연산을 피하는 방식이다.

추상적인 컨셉은 어렵지 않았는데 메모리 초과로 애를 먹었다.

어디서 메모리를 많이 사용하는지 생각해보니 bfs 큐가 문제였다.

거리를 측정하려면 좌표정보도 알아야 하는데 섬의 테두리 각각 bfs를 시행할 때 메모리 초과가 난다.

그래서 먼저 개별 섬 테두리 전체로 bfs를 실행하고

거리정보를 맵에 기록을 하는 방식으로 메모리 초과를 해결했다.

"""