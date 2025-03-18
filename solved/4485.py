from sys import stdin   
from collections import deque 

def bfs(x,y,n,c):
    visited = [[10*(i+j+1) for j in range(n)] for i in range(n)]
    visited[0][0] = c[0][0]
    q = deque([(x,y)])
    ans = visited[-1][-1]
    while q:
        a,b = q.popleft()

        if a == n-1 and b == n-1:
            ans = min(ans,visited[b][a])
            continue

        for da,db in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= a+da < n and 0 <= b+db < n:
                if visited[b+db][a+da] > visited[b][a]+c[b+db][a+da]:
                    q.append((a+da,b+db))
                    visited[b+db][a+da] = visited[b][a]+c[b+db][a+da]

    return ans

i = 1
ans = []
while (N:=int(stdin.readline().strip())) > 0:
    cave = []
    for _ in range(N):
        cave.append(list(map(int,stdin.readline().strip().split())))

    ans.append(f"Problem {i}: {bfs(0,0,N,cave)}")
    i+=1

print(*ans,sep='\n')
