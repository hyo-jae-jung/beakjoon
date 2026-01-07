from sys import stdin   

n,k = map(int,stdin.readline().strip().split())
adjacency_list = [[] for _ in range(n+1)]
for _ in range(n-1):
    p,c = map(int,stdin.readline().strip().split())
    adjacency_list[p].append(c)
    adjacency_list[c].append(p)

apple = list(map(int,stdin.readline().strip().split()))

ans = 0
visited = [False]*n
stack = [(0,0)] # node, distance

while stack:
    n,d = stack.pop()
    if visited[n]:
        continue
    visited[n] = True
    ans+=apple[n]

    if d < k:
        for v in adjacency_list[n]:
            stack.append((v,d+1))

print(ans)
