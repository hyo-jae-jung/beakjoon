from sys import stdin 

n = int(stdin.readline().strip())
adjacency_list = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent,child,w = map(int,stdin.readline().strip().split())
    adjacency_list[parent].append((child,w))
    adjacency_list[child].append((parent,w))

end_nodes = set()
for i in range(1,n+1):
    if len(adjacency_list[i]) == 1:
        end_nodes.add(i)

def dfs(start):
    global n,adjacency_list,end_nodes
    result = 0
    visited = [False]*(n+1)
    stack = [(start,0)]
    visited[start] = True

    while stack:
        u,val = stack.pop()

        if u in end_nodes:
            result = max(result,val)
            continue

        for v,w in adjacency_list[u]:
            if not visited[v]:
                visited[v] = True
                stack.append((v,val+w))

    return result

ans = 0
while end_nodes:
    u = end_nodes.pop()
    ans = max(ans,dfs(u))

print(ans)
