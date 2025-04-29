import sys
sys.setrecursionlimit(10**5)

N,M,K = map(int,sys.stdin.readline().strip().split())
C = [0] + list(map(int,sys.stdin.readline().strip().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

friend_groups = []

visited_friend_nums = [False]*(N+1)

def dfs(node):
    global visited_friend_nums,n,v
    n+=1
    v+=C[node]
    for i in graph[node]:
        if not visited_friend_nums[i]:
            visited_friend_nums[i] = True
            dfs(i)

for node in range(1,N+1):
    if not visited_friend_nums[node]:
        visited_friend_nums[node] = True
        n,v = 0,0
        dfs(node)
        if n < K and v > 1:
            friend_groups.append((n,v))
        
dp = [0]*(K)
for n,v in friend_groups:
    for i in range(K-1,n-1,-1):
        dp[i] = max(dp[i],dp[i-n]+v)

print(max(dp))
