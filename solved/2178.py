from sys import stdin 
from collections import deque 

N,M = map(int,stdin.readline().strip().split())
maze = []
for _ in range(N):
    maze.append([int(i) for i in stdin.readline().strip()])

def bfs(graph):
    queue = deque([(0,0)])
    dn = [1,0,-1,0]
    dm = [0,1,0,-1]
    visited = deque([(0,0)])
    while queue:
        n,m = queue.popleft()

        if n == N-1 and m == M-1:
            return graph[n][m]
        
        for dn_idx,dm_idx in zip(dn,dm):
            next_n,next_m = dn_idx+n,dm_idx+m
            if next_n<=-1 or next_n >=N or next_m <= -1 or next_m >= M:
                continue
            elif graph[next_n][next_m] == 0:
                continue
            elif (next_n,next_m) in visited:
                continue
            else:
                queue.append((next_n,next_m))
                graph[next_n][next_m] = graph[n][m]+1
                visited.append((next_n,next_m))

print(bfs(maze))

"""
1. 가장 빠른 방법만 생각하면 되서 중간에 겹치거나 돌아가는 경우를 생각 할 필요는 없음
"""