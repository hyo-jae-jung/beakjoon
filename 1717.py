from sys import stdin 

n,m = map(int,stdin.readline().strip().split())
chart = [set([i]) for i in range(n+1) if i]

def dfs(v,e):
    visited = [False]*(n+1)
    stack = set([v])
    
for _ in range(m):
    i,a,b = map(int,stdin.readline().strip().split())
    if i == 0:
        chart[a].union(chart[b])
        chart[b] = chart[a]
    else:




answer = []

print(*answer,sep='\n')
