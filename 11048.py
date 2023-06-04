import sys
sys.setrecursionlimit(10**6)

N,M = map(int,sys.stdin.readline().strip().split())
arr = []
memo = []
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().strip().split())))
    memo.append([0]*M)

def dfs(x=0,y=0,cnt=0):
    if x < 0 or y < 0 or x >= M or y >= N:
        return False
    
    present_cnt = arr[y][x]+cnt

    if x == M-1 and y == N-1:
        memo[y][x] = present_cnt
        return True

    if present_cnt > memo[y][x]:
        memo[y][x] = present_cnt

        dfs(x+1,y,present_cnt)
        dfs(x,y+1,present_cnt)
        
dfs()
print(memo[N-1][M-1])
