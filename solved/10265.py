import sys  
sys.setrecursionlimit(10**5)

n,k = map(int,sys.stdin.readline().strip().split())
X = list(map(int,sys.stdin.readline().strip().split()))

undiredcted_graph = [[] for _ in range(n+1)]
diredcted_graph = [[] for _ in range(n+1)]
for i,j in enumerate(X,1):
    undiredcted_graph[i].append(j)
    diredcted_graph[i].append(j)
    if i != j:
        undiredcted_graph[j].append(i)

def dfs(v,g=undiredcted_graph):
    visited[v] = False
    global tmp_list
    tmp_list.append(v)
    for i in g[v]:
        if visited[i]:
            dfs(i)

def dfs2(v,g=diredcted_graph):
    visited[v] = False
    for i in g[v]:
        if visited[i]:
            dfs2(i)
        else:
            vs.append(i)

visited = [True]*(n+1)
groups = []
for i in range(1,n+1):
    tmp_list = []
    if visited[i]:
        dfs(i)
        groups.append(tmp_list)

vs = []
visited = [True]*(n+1)
for i in groups:
    for j in i:
        if visited[j]:
            dfs2(j)
            break

items = []
def dfs3(v,g=diredcted_graph):
    global n 
    n+=1
    visited[v] = False
    for i in g[v]:
        if visited[i]:
            dfs3(i)

visited = [True]*(n+1)
mm = []
for i in vs:
    n = 0
    dfs3(i)
    mm.append(n)

for i in range(len(mm)):
    items.append(range(mm[i],len(groups[i])+1))

dp = [0]*(k+1)
for i in items:
    tmp_dp = dp.copy()
    for j in i:
        for l in range(k,j-1,-1):
            tmp_dp[l] = max(tmp_dp[l],dp[l-j]+j)

    for m in range(k+1):
        dp[m] = max(dp[m],tmp_dp[m])

print(max(dp))
