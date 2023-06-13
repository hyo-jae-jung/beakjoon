import sys
from collections import defaultdict
sys.setrecursionlimit(10**4)

N,M = map(int,sys.stdin.readline().strip().split())
chart = defaultdict(set)
for _ in range(M):
    a,b = map(int,sys.stdin.readline().strip().split())
    chart[a].add(b)
    chart[b].add(a)
    
def dfs(n,cnt=0):
    if cnt == 4:
        global answer
        answer = 1
        return True
    
    for i in chart[n]:
        if not visited[i]:
            visited[i] = True
            dfs(i,cnt+1)
            visited[i] = False
            
answer = 0
for i in range(N):
    visited = defaultdict(bool)
    visited[i] = True
    if not answer:
        dfs(i)

print(answer)
