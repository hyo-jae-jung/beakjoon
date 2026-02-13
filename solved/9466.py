import sys 
sys.setrecursionlimit(10**7)

def dfs(i,cnt=1):
    global adjacency_list, visited, result, d
    visited[i] = True
    d.update({i:cnt})
    if not visited[adjacency_list[i]-1]:
        dfs(adjacency_list[i]-1,cnt+1)
    else:
        if d.get(adjacency_list[i]-1):
            result-= cnt - d.get(adjacency_list[i]-1) + 1


T = int(sys.stdin.readline().strip())
ans = []
for _ in range(T):
    n = int(sys.stdin.readline().strip())   
    result = n
    adjacency_list = list(map(int,sys.stdin.readline().strip().split()))
    visited = [False]*n
    for i in range(n):
        d = {}
        if not visited[i]:
            dfs(i)

    ans.append(result)

print(*ans,sep='\n')
