from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    A,B = map(int,stdin.readline().strip().split())
    indegree[B]+=1
    graph[A].append(B)

stack = []
ans = []

for i in range(1,N+1):
    if indegree[i] == 0:
        stack.append(i)

while stack:
    n = stack.pop()
    ans.append(n)
    for i in graph[n]:
        indegree[i]-=1
        if indegree[i] == 0:
            stack.append(i)

print(*ans)
