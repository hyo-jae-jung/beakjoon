import sys
sys.setrecursionlimit(10**7)

N,K = map(int, sys.stdin.readline().strip().split())
M = 10000
time = 1e6
visited_cnt = [time]*(M+1)

def dfs(x,cnt=0):
    if x < 1 or x > M:
        return False
    
    if x == K:
        visited_cnt[x] = min(visited_cnt[x],cnt)
        return True
    
    if x*2 <= M:
        if visited_cnt[x*2] > cnt:
            visited_cnt[x*2] = cnt
            dfs(x*2,cnt)
    
    if x-1 > 0:
        if visited_cnt[x-1] > cnt+1:
            visited_cnt[x-1] = cnt+1
            dfs(x-1,cnt+1)
    
    if x+1 <= M:
        if visited_cnt[x+1] > cnt+1:
            visited_cnt[x+1] = cnt+1
            dfs(x+1,cnt+1)

dfs(N)
print(visited_cnt)
print(visited_cnt[K])
